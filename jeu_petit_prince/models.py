from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    account_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="images/")

    butterflies = models.BooleanField(blank=True)
    elephants = models.IntegerField(blank=True)
    games = models.TextField(blank=True)
    fav_color = models.CharField(max_length=100)

    birds_collected = models.IntegerField(blank=True)
    
    score_little_prince = models.IntegerField(blank=True)
    score_king = models.IntegerField(blank=True)
    score_conceited_man = models.IntegerField(blank=True)
    score_drunkard = models.IntegerField(blank=True)
    score_business_man = models.IntegerField(blank=True)
    score_lamplighter = models.IntegerField(blank=True)
    score_geographer = models.IntegerField(blank=True)
    score_earth = models.IntegerField(blank=True)

    total_score = models.IntegerField(blank=True)

    item_1 = models.IntegerField(blank=True)
    item_2 = models.IntegerField(blank=True)
    item_3 = models.IntegerField(blank=True)

    def __str__(self):
        return self.name



