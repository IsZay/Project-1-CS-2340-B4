from django.db import models
from django.utils import timezone  # Import timezone from django.utils
import datetime
from django.contrib import admin  # Add the missing admin import

class Movie(models.Model):  # Fix the 'Models' to 'models'
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', default='data:image/jpeg;base64,...')
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.title

    def get_price(self):
        return self.price

    def old_movie(self):
        return self.year < 2005

    @admin.display(  # Ensure this decorator is used properly
        boolean=True,
        ordering="title",
        description="Published recently?"
    )
    def old_movie(self):
        now = timezone.now()
        return now > datetime.datetime(year=2025, month=1, day=1)
