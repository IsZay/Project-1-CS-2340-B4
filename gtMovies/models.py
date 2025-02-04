from django.db import models

# Create your models here.

#Pretty sure this is where I can add objects/classes

# this is where we made the
# class Question(models.Model):

# I have no idea what that does but I'm gonna copy all the same imports


# Create your models here.
# models are essentially the objects that we are going to continue using throughout the project
# like the Movie
# and maybe have the MoviePoster be a separate class if necessary
# searchRequests might have to be a Model. Maybe we keep a search history with it?
# I don't know what else

import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    # poster = models.ImageField(upload_to='posters/') # Cannot use ImageField because Pillow is not installed
    def __str__(self):
        return self.title
    def get_price(self):
        return self.price
    def old_movie(self):
        return self.year < 2005

    @admin.display(
        #lets show something only admin should see
        boolean=True,
        ordering="title",
        description="Published recently?",
    )

    def old_movie(self):
        now = timezone.now()
        return now > datetime.datetime(year=2025, month = 1, day = 1)
