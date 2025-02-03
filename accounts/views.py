from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

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
from .forms import CustomUserCreationForm
from django.shortcuts import redirect


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})

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
