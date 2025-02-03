from django.urls import path
from . import views

import home

urlpatterns = [
    path('', views.index, name='home.index'),
]