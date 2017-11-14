# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)
    birth_day = models.IntegerField()
    birth_month = models.IntegerField()
    birth_year = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username + " " + self.password

class Developer(models.Model):
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=datetime.now())

class Follow(models.Model):
    user = models.ForeignKey(User)
    developer = models.ForeignKey(Developer)
    created_at = models.DateTimeField(default=datetime.now())

class Game(models.Model):
    picture = models.TextField() # url to image
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    suported_languages = models.TextField()
    genre = models.TextField()
    full_audio = models.BooleanField(default=False)
    subtitle = models.BooleanField(default=False)
    launched = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

class DevelopedGames(models.Model):
    game = models.ForeignKey(Game)
    developer = models.ForeignKey(Developer)
