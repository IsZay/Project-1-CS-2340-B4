from django.urls import path
from . import views


from django.urls import path
from .views import register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]

# added the final 3 paths. It hasn't broke yet!!
