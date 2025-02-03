from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie
class MovieAdmin(admin.ModelAdmin):
    ordering = ['title'] #Maybe id might look better?
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)

#Did not do the last part of chapter 7 using a more robust database other than sqllite
