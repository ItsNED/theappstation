from django.contrib import admin
from .models import GamePortfolio, MarketingPortfolio

@admin.register(GamePortfolio)
class GamePortfolioAdmin(admin.ModelAdmin):
    pass

@admin.register(MarketingPortfolio)
class MarketingPortfolioAdmin(admin.ModelAdmin):
    pass
