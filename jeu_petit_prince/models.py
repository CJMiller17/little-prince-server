from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    account_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    butterflies = models.BooleanField(blank=True, default=False)
    elephants = models.IntegerField(blank=True, null=True)
    games = models.TextField(blank=True, null=True)
    fav_color = models.CharField(max_length=100, blank=True, null=True)

    birds_collected = models.IntegerField(blank=True, null=True)
    
    score_little_prince = models.IntegerField(blank=True, null=True)
    score_king = models.IntegerField(blank=True, null=True)
    score_conceited_man = models.IntegerField(blank=True, null=True)
    score_drunkard = models.IntegerField(blank=True, null=True)
    score_business_man = models.IntegerField(blank=True, null=True)
    score_lamplighter = models.IntegerField(blank=True, null=True)
    score_geographer = models.IntegerField(blank=True, null=True)
    score_earth = models.IntegerField(blank=True, null=True)

    total_score = models.IntegerField(blank=True, null=True)

    item_1 = models.IntegerField(blank=True, null=True)
    item_2 = models.IntegerField(blank=True, null=True)
    item_3 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name



