from django.apps import AppConfig

#https://docs.djangoproject.com/en/5.1/


class GtmoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gtMovies' #Must be unique.
    # Full Python path to the application, e.g. 'django.contrib.admin'.
    # This attribute defines which application the configuration applies to. It must be set in all AppConfig subclasses.


