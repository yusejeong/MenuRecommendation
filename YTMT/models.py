from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

# 메뉴
class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    img_url = models.ImageField(null=True, max_length=100)
    text = models.TextField(null=True)

    likes = models.IntegerField(default= 0)

    def __str__(self):
        return self.name
        
class Ingredient(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank = False, null = False)
    # type(유제품/육류/어류)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    ingre = models.ForeignKey(Ingredient, on_delete = models.CASCADE)
 
    def __str__(self):
        return self.menu.name + " " + self.ingre.name

# 회원정보
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50, blank = False, null = False)

    Gender_TYPE = (
        (1, "남자"),
        (2, "여자"),
    )

    Religion_TYPE = (
        (1, "힌두교"), (2, "불교"),
        (3, "기독교"), (4, "천주교"),
        (5, "이슬람교"), (6, "유대교"),
        (7, "시크교도"), (8, "무교"),
    )

    Vegetarian_TYPE = (
        (1, "비건"), (2, "락토 베지테리언"),
        (3, "오보 베지테리언"), (4, "락토 오보 베지테리언"),
        (5, "페스코 베지테리언"), (6, "플로 베지테리언"),
        (7, "플렉시테리언"), (8, "해당사항없음"),
    )
    
    locationX = models.DecimalField(default = 0, max_digits=19, decimal_places=10)
    locationY = models.DecimalField(default = 0, max_digits=19, decimal_places=10)

    gender = models.IntegerField(blank = False, null = False, choices=Gender_TYPE, default=1)
    birth = models.DateTimeField(blank = False, null = False)
    reli_id = models.IntegerField(choices=Religion_TYPE, default=8)
    vege_id = models.IntegerField(choices=Vegetarian_TYPE, default=8)

    def __str__(self):
        return self.user_id.username


class Allergy(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    ingre = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username + ":" + self.ingre.name

class Hate_menu(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id.username + " : " + self.menu.name

    
class Hate_ingredient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    ingre = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username + " : " + self.ingre.name

class Vegetarian_case(models.Model):

    Vegetarian_TYPE = (
        (1, "비건"), (2, "락토 베지테리언"),
        (3, "오보 베지테리언"), (4, "락토 오보 베지테리언"),
        (5, "페스코 베지테리언"), (6, "플로 베지테리언"),
        (7, "플렉시테리언"), (8, "해당사항없음"),
    )
    vege_id = models.IntegerField(choices=Vegetarian_TYPE, default=8)
    ingre = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vege_id) + " : " + self.ingre.name

class Religion_case(models.Model):

    Religion_TYPE = (
        (1, "힌두교"), (2, "불교"), 
        (3, "기독교"), (4, "천주교"), 
        (5, "이슬람교"), (6, "유대교"),
        (7, "시크교도"), (8, "무교"),
    )

    reli_id = models.IntegerField(choices=Religion_TYPE, default=8)
    ingre = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reli_id) + " : " + self.ingre.name

class History(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE)

    def __str__(self):
        return self.user_id.username + " : " + self.menu.name

class Restaurant(models.Model):
    rest_id = models.AutoField(primary_key=True)
    rest_name = models.CharField(max_length = 50, default="None")
    img = models.FileField(null=True,max_length=50)
    text = models.CharField(null=True, max_length=50)

    locationX = models.DecimalField(default = 0, max_digits=19, decimal_places=10)
    locationY = models.DecimalField(default = 0, max_digits=19, decimal_places=10)

    def __str__(self):
        return self.rest_name


class Menu_store(models.Model):
    menu = models.ForeignKey(Menu, on_delete= models.CASCADE)
    rest_id = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    price = models.IntegerField(default= 0) 

    def __str__(self):
        return self.rest_id.rest_name + " 판매 메뉴 : " + self.menu.name

class Friend_list(models.Model):
    user_id = models.ManyToManyField(User)
    friend_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name="owner", null=True)
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return self.user_id.username + " : " + self.friend_id.username
