from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


admin.site.register(Profile)
admin.site.register(Menu)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(History)
admin.site.register(Hate_ingredient)
admin.site.register(Hate_menu)
admin.site.register(Vegetarian_case)
admin.site.register(Religion_case)
admin.site.register(Allergy)
admin.site.register(Friend_list)
admin.site.register(Restaurant)
admin.site.register(Menu_store)
