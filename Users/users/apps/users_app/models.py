from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User as U


# Create your models here.
# Inside models.py

"""
NOTE TO SELF:
Need to remember to:

>>> python manage.py migrate
>>> python manage.py makemigrations

each time this file is changed
"""

#Admin users found in django.contrib.auth.models

class Customer(models.Model):
    user = models.OneToOneField(U, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

class Game(models.Model):
    game_name = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    complexity = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game_name




