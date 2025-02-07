from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect

# from accounts.models import Movie


# Create your views here.
# Our views page actually shows what the consumer is viewing
# a pretty convienient name

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

# def index(request):
#     template_data = {}
#     template_data['title'] = 'Movies'
#     template_data['movies'] = Movie.objects.all()
#     return render(request, 'movies/index.html',
#                   {'template_data': template_data})

# def show(request, id):
#     movie = Movie.objects.get(id=id)
#     template_data = {}
#     template_data['title'] = movie.name
#     template_data['movie'] = movie
#     return render(request, 'movies/show.html',
#                   {'template_data': template_data})


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect


from django.contrib.auth.decorators import login_required
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})


# def forgot(request):
#     template_data = {}
#     template_data['title'] = 'Forgot'
#     if request.method == 'GET':
#         template_data['form'] = CustomUserCreationForm()
#         return render(request, 'accounts/signup.html',
#             {'template_data': template_data})










from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy


class ForgotPasswordView(PasswordResetView):
    template_name = 'accounts/forgot_password.html'  # Use your custom HTML file
    email_template_name = 'accounts/password_reset_email.html'  # Email template
    subject_template_name = 'accounts/password_reset_subject.txt'  # Email subject template
    success_url = reverse_lazy('accounts.password_reset_done')  # Redirect after form submission to "Email sent, go back to home page"

from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy


class ResetComplete(PasswordResetCompleteView):
    # Specify the template to display the success message
    template_name = 'accounts/password_reset_complete.html'
    success_url = reverse_lazy('accounts.login')

    # Optionally override the success redirection
    def get_success_url(self):
        # Change reverse_lazy to use a custom URL or any other logic
        # Example: Redirect to 'accounts.login' instead of the default
        return reverse_lazy('accounts.login')


# views.py (Temporary testing view)
# Quick way to send emails to yourself I think with this form

from django.core.mail import send_mail
from django.http import HttpResponse


def send_test_email(request):
    try:
        send_mail(
            subject='Test Email from Django',
            message='This is a test email.',
            from_email=None,  # Defaults to DEFAULT_FROM_EMAIL in settings.py
            recipient_list=['falsebooks3@gmail.com'],  # Replace with your recipient's email
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")


#
#     - `forgot_password.html`: To render the password reset form.
#     - `password_reset_email.html`: Template for the password reset email.
#     - `password_reset_done.html`: To show a confirmation message after the form is submitted.
#     - `password_reset_confirm.html`: To confirm the password reset via a token.
#     - `password_reset_complete.html`: To notify users once the password has been reset successfully.
# def register(request):
#     template_data = {}
#     template_data['title'] = 'Register'
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login page after successful registration
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {'form': form})





#
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')  # Redirect to home page after successful login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')  # Redirect to login page


# '''
# I know my notes are everywhere. What I did is create a Movie class (much like the Question class in our intro to Django)
# this is going to let us have multiple fields that people can search by? Or something?
# As we go through all of this code we are going to have to appropriately show what we named each variable and functions
# or rather what ChatGPT is naming the variables
# Also, we need our index to actually be where our movives are displayed at first
# we then will have  the login and register button in the top right
# and then the search bar right underneath it, (or in the Top Middle)
# We should have the image show by doing that ImageField I wrote before in the right function
# '''
#
