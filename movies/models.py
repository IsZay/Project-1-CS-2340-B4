from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
# class Movie(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='movie_images/')
#     def __str__(self):
#         return str(self.id) + ' - ' + self.name


import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



class Movie(models.Model):
    RATING_CHOICES = [
        ('G', 'G - General Audience'),
        ('PG', 'PG - Parental Guidance Suggested'),
        ('PG-13', 'PG-13 - Parents Strongly Cautioned'),
        ('R', 'R - Restricted'),
        ('NR', 'NR - Not Rated')
    ]

    title = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    intended_audience = models.CharField(
        max_length=10,
        choices=RATING_CHOICES,
        default='G'
    )

    def __str__(self):
        return f"{self.id} - {self.title}"

    def get_price(self):
        return self.price

    def old_movie(self):
        return self.year < 2005

    @admin.display(
        boolean=True,
        ordering="title",
        description="Published recently?",
    )
    def old_movie(self):
        now = timezone.now()
        return now.year - self.year < 1  # Adjusted to check if the movie was released in the last year


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.title