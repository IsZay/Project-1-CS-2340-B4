from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the gtMovies index.")

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'gtMovies/register.html', {'form': form})
# observe this last line. We haven't made gtMovies.register.html yet. This will be done later

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'gtMovies/login.html', {'form': form})
#Chat says that django has a default ?user_login? or somn, but i added this anyway
# so far the code doesn't break


