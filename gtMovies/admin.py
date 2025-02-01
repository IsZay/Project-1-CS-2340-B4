from django.contrib import admin

# Register your models here.
# I have no idea what admin really does, but
# i'm still looking at what we did for the first one



from django.contrib import admin

from .models import Movie

admin.site.register(Movie)
# These lines of code allow you to see the Movie's that we have available
