from django.db import models

# Create your models here.

#Pretty sure this is where I can add objects/classes

# this is where we made the
# class Question(models.Model):

# I have no idea what that does but I'm gonna copy all the same imports


# Create your models here.

import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#     @admin.display(
#         boolean=True,
#         ordering="pub_date",
#         description="Published recently?",
#     )
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
#
# def was_published_recently(self):
#     now = timezone.now()
#     return now - datetime.timedelta(days=1) <= self.pub_date <= now

#this page does not work at all
#Okay PyCharm AI filled this in for me
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    # poster = models.ImageField(upload_to='posters/') # Cannot use ImageField because Pillow is not installed

    @admin.display(
        #lets show something only admin should see
        boolean=True, # this obviously doesn't work logically
        ordering="title", #order the tings by the variable "title"  ideally
        description="Published recently?", # I want to sort it by title, and then output the year?? Why??

    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
# def __str__(self):
#         return self.title

#Alr it finishe