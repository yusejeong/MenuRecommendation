from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Ingredient, Menu2


# Register your models here.
# admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Menu2)
admin.site.register(Ingredient)