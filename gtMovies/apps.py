from django.apps import AppConfig

#https://docs.djangoproject.com/en/5.1/
# Maybe want to go ahead and read Settings too
# the apps.py is basically what our app looks like,
# an app goes in a website, but an app is not the website
# you can have another app say MusicBuyer, which would have its own page like
# musicBuyerApp vs gtMovies


class GtmoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gtMovies' #Must be unique.
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to. It must be set in all AppConfig subclasses.


# '''
# I know my notes are everywhere. What I did is create a Movie class (much like the Question class in our intro to Django)
# this is going to let us have multiple fields that people can search by? Or something?
# As we go through all of this code we are going to have to appropriately show what we named each variable and functions
# or rather what ChatGPT is naming the variables
# Also, we need our index to actually be where our movives are displayed at first
# we then will have  the login and register button in the top right
# and then the search bar right underneath it, (or in the Top Middle)
# We should have the image show by doing that ImageField I wrote before in the right function
# '''
#
