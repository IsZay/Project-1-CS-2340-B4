from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['title'] #Maybe id might look better?
    search_fields = ['title']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)

#Did not do the last part of chapter 7 using a more robust database other than sqllite
