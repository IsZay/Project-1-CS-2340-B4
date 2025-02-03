from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie
class MovieAdmin(admin.ModelAdmin):
    ordering = ['title']
admin.site.register(Movie, MovieAdmin)

