
from . import views


from django.urls import path
from .views import register, user_login
from django.contrib.auth.views import LogoutView

#urls is what the urls that we have available,
# as we add new pages, we need to urls, which is the first value in the path function
# the second is basically which function it is going to use from views.py
# the last is basically a field that allow us to see where we are in the website
# name isn't the only thing we can add


urlpatterns = [
    path("", views.index, name="index"), # this should have all of our movie lists together, then have a login button in the top right and a register button.
    # we can have a login button, and there it has a "register here" in there like most websites, which wouldn't be hard to change the path underneath as you'll see ***
    #'login/register' actually that doesn't make sense
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

# added the final 3 paths. It hasn't broke yet!!
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
