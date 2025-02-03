
from . import views


from django.urls import path
# from .views import user_login, signup
# from django.contrib.auth.views import LogoutView

#urls is what the urls that we have available,
# as we add new pages, we need to urls, which is the first value in the path function
# the second is basically which function it is going to use from views.py
# the last is basically a field that allow us to see where we are in the website
# name isn't the only thing we can add

# app_name = 'accounts'  # This sets the namespace for this app

urlpatterns = [
    path('', views.index, name='index'), # this should have all of our movie lists together, then have a login button in the top right and a register button.
    # we can have a login button, and there it has a "register here" in there like most websites, which wouldn't be hard to change the path underneath as you'll see ***
    #'login/register' actually that doesn't make sense
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),

]
