from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Ingredient, Menu, Recipe, Hate_menu, History, Hate_ingredient, Allergy


admin.site.register(Profile)
admin.site.register(Menu)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(History)
admin.site.register(Hate_ingredient)
admin.site.register(Hate_menu)
admin.site.register(Allergy)
