from django.db import models

class User(models.Model):
    id = models.CharField(max_length=10)
    pw = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    birth = models.DateField()
    gender = 1

    religion = []
    vegetarian = []

    allergie = []
    hate_food = []
    hate_ingredient = []
    
class History(models.Model):
    user_id
    history = []

class Friendlist(models.Model):
    user_id
    friend_id = []

class Religion(models.Model):
    reli_id
    reli_name
    reli_prohibited = []

class Vegetarian(models.Model):
    vege_id
    vege_name
    vege_prohibited = []

class Menu(models.Model):
    menu_id
    menu_name
    ingredient = []
    PendingDeprecationWarning
