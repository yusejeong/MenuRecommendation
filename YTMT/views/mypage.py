from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime
from . import session as SS
from . import utils
menu_list = []
ingre_list = []
# friend_list=[]
# for friend in Friend_list.objects.all():
#     friend_list.append(friend.friend_id)



for ingre in Ingredient.objects.all():
    ingre_list.append(ingre.name)

for menu in Menu.objects.all():
    menu_list.append(menu.name)

# 마이페이지_수정
def mypagemain(request):
    return render(request, 'mypage/mypagemain.html')

# 마이페이지_개인정보 수정
def selectinfo(request):
    return render(request, 'mypage/selectinfo.html')

def infomodify(request):
    login_user = SS.find_user(request)

    return render(request, 'mypage/infomodify.html', {"user" : login_user})

def infomodifysave(request):
    login_user = SS.find_user(request)

    if request.method == "POST":
        if request.POST["pwd"] == request.session.get('password'):
            if request.POST["newpwd"] == request.POST["pwdchk"]:
                login_user.set_password(request.POST["newpwd"])
                request.session['password'] = request.POST["newpwd"]
                if request.POST["email2"] != "etc":
                    login_user.email = request.POST["email"] + "@" + request.POST["email2"]
                else:
                    login_user.email = request.POST["email"]
                login_user.save()
                return render(request, 'mypage/selectinfo.html')
            return render(request,'mypage/infomodify.html')
        return render(request,'mypage/infomodify.html')
    return render(request,'mypage/infomodify.html')

def religionmodify(request):
    return render(request, 'mypage/religionmodify.html')

def religionmodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    reli_name = request.POST.get("religion")
    userProfile.reli_id = utils.get_reli_id(reli_name)

    userProfile.save()
    return render(request, 'mypage/selectinfo.html')

def vegetarianmodify(request):
    return render(request, 'mypage/vegetarianmodify.html')

def vegetarianmodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    vege_name = request.POST.get("vegetarian")
    userProfile.vege_id = utils.get_vege_id(vege_name)

    userProfile.save()
    return render(request, 'mypage/selectinfo.html')

def allergymodify(request):
    login_user = SS.find_user(request)
    allergy_objects = Allergy.objects.filter(user_id = login_user)
    allergy_list = []

    for allergy in allergy_objects:
        allergy_list.append(allergy)

    return render(request, 'mypage/allergymodify.html',{"allergy_list" : allergy_list})

def allergymodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    # 일대다
    return render(request, 'mypage/selectinfo.html')

def hatemodify(request):
    return render(request, 'mypage/hatemodify.html',{'ingredient_list': ingre_list,'menu_list' : menu_list})

def hatemodifysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)
    hate_menu_list = request.POST.get("menu_list")
    hate_menu_list = json.loads(hate_menu_list)

    hate_ingredient_list = request.POST.get("ingredient_list")
    hate_ingredient_list = json.loads(hate_ingredient_list)

    return render(request, 'mypage/selectinfo.html')

# 마이페이지_기타
def history(request):
    return render(request, 'mypage/history.html')

def friendlist(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    friend_objects = Friend_list.objects.filter(user_id = login_user)
    friend_list = []
    for friend in friend_objects:
        friend_id = friend.friend_id.username 
        name = Profile.objects.get(user_id = friend.friend_id).name
        friend_list.append({"id" : friend_id, "name" : name})
    
    return render(request, 'mypage/friendslist.html', {"friend_list" : friend_list})

def friendlistsave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)
    return render(request, 'mypage/mypagemain.html')

def profile(request):
    login_user = SS.find_user(request)
    tempProfile = Profile.objects.get(user_id = login_user)   
    
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

    userProfile = {
        "name" : tempProfile.name,
        "religion" : Religion_TYPE[tempProfile.reli_id -1][1],
        "vegetarian" : Vegetarian_TYPE[tempProfile.vege_id- 1][1],
        "gender" : Gender_TYPE[tempProfile.gender - 1][1],
        "birth" : tempProfile.birth,
    }

    return render(request, 'mypage/profile.html',{"profile" : userProfile})
