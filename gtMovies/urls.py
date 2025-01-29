
from . import views


from django.urls import path
from .views import register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"), #this should have all of our movie lists together, then have a login button in the top right and a register button.
    # we can have a login button, and there it has a "register here" in there like most websites, which wouldn't be hard to change the path underneath as you'll see ***
    #'login/register' actually that doesn't make sense
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

# added the final 3 paths. It hasn't broke yet!!
