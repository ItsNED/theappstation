from django.shortcuts import render
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import GamePortfolio, MarketingPortfolio


def index(request):
    games = GamePortfolio.objects.all().order_by('-id')[:8]
    marketings = MarketingPortfolio.objects.all()

    return render(request, 'homepage/index.html', {
        'games':games,
        'marketings': marketings
    })

def lazy_load_posts(request):
    page = request.POST.get('page')
    games = GamePortfolio.objects.all().order_by('-id')
    print('page: {}\npost: {}'.format(page, games))
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 8
    paginator = Paginator(games, results_per_page)
    try:
        games = paginator.page(int(page))
        print('try: {}'.format(games))
    except PageNotAnInteger:
        print('except1: {}'.format(games))
        games = paginator.page(2)
    except EmptyPage:
        print('except2: {}'.format(games))
        games = paginator.page(paginator.num_pages)
		
    # build a html posts list with the paginated posts
    games_html = loader.render_to_string('homepage/game_portfolio.html', {'games': games})
  
    print('{}{}'.format(games_html, games.has_next))
    # package output data and return it as a JSON object
    output_data = {'games_html': games_html, 'has_next': games.has_next()}
    return JsonResponse(output_data)