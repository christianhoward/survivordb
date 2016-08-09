from django.shortcuts import render
from .models import Player

def home(request):
    players = Player.objects.order_by('pid')
    return render(request, 'webapp/home.html', {'players': players})
