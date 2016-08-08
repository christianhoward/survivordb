from django.contrib import admin
from .models import Player, Season, PxS, Statistics

admin.register(Player, Season, PxS, Statistics)(admin.ModelAdmin)