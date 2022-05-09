from unicodedata import name
from django.apps import AppConfig


class App1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'



class Blogconfig(App1Config):
    name = 'app1'
    