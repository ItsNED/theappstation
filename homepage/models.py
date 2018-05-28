from django.db import models

class GamePortfolio(models.Model):
    CATEGORY_CHOICES = (
        ('r', 'RPG+'),
        ('c', 'CASUAL'),
        ('e', 'ETC'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=30)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class MarketingPortfolio(models.Model):
    CATEGORY_CHOICES = (
        ('e', '가전'),
        ('b', '뷰티'),
        ('l', '생활/서비스'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title