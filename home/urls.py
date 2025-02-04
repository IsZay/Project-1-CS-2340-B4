from django.urls import path
from . import views

import home

urlpatterns = [
    path('', views.index, name='home.index'),
path('about/', views.about, name='home.about'), #TODO MAY SWITCH YOU TO OURSITE.urls
]