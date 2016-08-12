from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Season

def home(request):
    seasons = Season.objects.order_by('sid')
    return render(request, 'webapp/home.html', {'seasons': seasons})

def player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'webapp/player.html', {'player': player})
    
def season(request, pk):
    season = get_object_or_404(Season, pk=pk)
    return render(request, 'webapp/season.html', {'season': season})

def seasons(request):
    seasons = Season.objects.order_by('sid')
    return render(request, 'webapp/seasons.html', {'seasons': seasons})
