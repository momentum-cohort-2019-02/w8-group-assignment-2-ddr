from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Deck(models.Model):
    card = models.ForeignKey('Card', on_delete_model=CASCADE)








class Game(models.Model):
    deck =     
    













class Card(models.Model):