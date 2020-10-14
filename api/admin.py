from django.contrib import admin
from .models import Movie, Rating

admin.site.register([Movie, Rating])
