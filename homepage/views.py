from django.shortcuts import render
from .models import GamePortfolio, MarketingPortfolio

def index(request):
    games = GamePortfolio.objects.all()
    marketings = MarketingPortfolio.objects.all()

    return render(request, 'homepage/index.html', {
        'games':games,
        'marketings': marketings
    })
