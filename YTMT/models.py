from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

# 메뉴
class Menu(models.Model):
    menu_id = models.IntegerField(blank = False, null = False, primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)

class Ingredient(models.Model):
    ingre_id = models.IntegerField(blank = False, null = False, primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    # type(유제품/육류/어류)

class Recipe(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


# 회원정보
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)

    Gender_TYPE = (
        (1, "남자"),
        (2, "여자"),
    )

    Religion_TYPE = (
        (1, "힌두교"), (2, "불교"), (3, "기독교"),
        (4, "천주교"), (5, "이슬람교"), (6, "유대교"),
        (7, "회교도"), (8, "시크교도"), (9, "무교"),
    )

    Vegetarian_TYPE = (
        (1, "비건"), (2, "락토 베지테리언"),
        (3, "오보 베지테리언"), (4, "락토 오보 베지테리언"),
        (5, "페스코 베지테리언"), (6, "플로 베지테리언"),
        (7, "플렉시테리언"), (8, "해당사항없음"),
    )
    
    gender = models.IntegerField(blank = False, null = False, choices=Gender_TYPE, default=1)
    birth = models.DateField(blank = False, null = False, auto_now_add=True)
    reli_id = models.IntegerField(choices=Religion_TYPE)
    vege_id = models.IntegerField(choices=Vegetarian_TYPE)

class Allergy(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

class Hate_menu(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
class Hate_ingredient(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    ingre_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

# class History(models.Model):
#     user_id
#     menu_id

# class Relation(models.Model):
#     user_id
#     friend_id