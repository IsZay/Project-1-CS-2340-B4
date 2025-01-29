from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Our views page actually shows what the consumer is viewing
# a pretty convienient name
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
