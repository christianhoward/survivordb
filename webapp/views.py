from django.shortcuts import render
from .models import Player, Season

def home(request):
    players = Player.objects.order_by('pid')
    return render(request, 'webapp/home.html', {'players': players})

def player(request):
    players = Player.objects.order_by('pid')
    return render(request, 'webapp/player.html', {'players': players})
    #make player.html
    
def season(request):
    seasons = Season.objects.order_by('sid')
    return render(request, 'webapp/season.html', {'seasons': seasons})
    #make season.html
