#-*-coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import json
import datetime
from . import session as SS
from . import utils

'''
    회원가입 관련 기능이 저장되는 view 파일입니다.
    회원가입에 추가적인 기능이 필요하면 추가하십시요.
'''
menu_list = []
ingre_list = []

for ingre in Ingredient.objects.all():
    ingre_list.append(ingre.name)

for menu in Menu.objects.all():
    menu_list.append(menu.name)

# 회원가입
def signup(request):
    auth.logout(request)
    return render(request, 'user/signup.html')

def signuprequest(request):
    if request.method == "POST":
        if request.POST["pwd"] == request.POST["pwdchk"]:
            request.session['username'] = request.POST["id"]
            request.session['pwd'] = request.POST["pwd"]
            if request.POST["email2"] != "etc":
                request.session['email'] = request.POST["email"] + "@" + request.POST["email2"]
            else:
                request.session['email'] = request.POST["email"]
            request.session['name'] = request.POST["name"]
            return render(request, 'user/birthandgender.html')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

# 아이디 중복확인
def idcheck(request):
    id_check = request.POST.get('id')
    chk = User.objects.filter(username = id_check).exists()
    return HttpResponse(json.dumps({"chk" : chk}), content_type="application/json")

def birthandgendersave(request):
    # 성별 구분
    gender = request.POST.get("gender")
    if gender == "M":
        gender_num = 1
    else:
        gender_num = 2

    birthday_str = request.POST.get('birth')

    request.session['gender'] = gender_num
    request.session['birthday_str'] = birthday_str

    return render(request, 'user/religion.html')


# 회원가입 추가정보
def religionsave(request):
    request.session['religion'] = utils.get_reli_id(request.POST.get("religion"))
    return render(request, 'user/vegetarian.html')

def vegetariansave(request):
    request.session['vegetarian'] = utils.get_vege_id(request.POST.get("vegetarian"))
    return render(request, 'user/allergy.html', {"ingre_list" : ingre_list})

def allergysave(request):
    allergy_list = request.POST.get("allergy_list")
    allergy_list = json.loads(allergy_list)

    request.session['allergy'] = allergy_list
    # 일대다
    return render(request, 'user/hatelist.html',{'ingredient_list': ingre_list,'menu_list' : menu_list})

def hatelistsave(request):
    hate_menu_list = request.POST.get("menu_list")
    hate_menu_list = json.loads(hate_menu_list)

    hate_ingredient_list = request.POST.get("ingredient_list")
    hate_ingredient_list = json.loads(hate_ingredient_list)

    request.session['hate_menu'] = hate_menu_list
    request.session['hate_ingre'] = hate_ingredient_list

    # profilecheck.html 을 rendering하기 위한 작업
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
    
    # POST 방식으로 받아온 birth가 String값이기 때문에 DateTime 객체로 변환
    birthday_obj = datetime.datetime.strptime(request.session['birthday_str'], '%Y-%m-%d')

    userProfile = {
        "username" : request.session['username'],
        "email" : request.session['email'],
        "name" : request.session['name'],
        "gender" : Gender_TYPE[request.session['gender'] - 1][1],
        "birth" : birthday_obj.date(),
        "religion" : Religion_TYPE[request.session['religion'] -1][1],
        "vegetarian" : Vegetarian_TYPE[request.session['vegetarian']- 1][1],
    }    

    allergy = request.session['allergy']

    return render(request, 'user/profilecheck.html', {"profile" : userProfile, "hate_ingredient_list" : hate_ingredient_list, "allergy_list" : allergy, "hate_menu_list" : hate_menu_list })

# 입력정보 확인
def profilecheck(request):
    return render(request, 'user/profilecheck.html')


# 최종 회원가입
def signupfinal(request):
    login_user = User.objects.create_user(
        username = request.session['username'], password = request.session['pwd'], email = request.session['email']
    )
    
    birthday_obj = datetime.datetime.strptime(request.session['birthday_str'], '%Y-%m-%d')

    userProfile = Profile.objects.create(
        user_id = login_user, name = request.session['name'], gender = request.session['gender'], birth = birthday_obj, reli_id = request.session['religion'], vege_id = request.session['vegetarian']
    )
    userProfile.save()

    for allergy in request.session['allergy']:
        i = Ingredient.objects.get(name = allergy)
        if(i):
            Allergy(user_id = login_user, ingre = i).save()
        else:
             i = Ingredient(name = allergy)
             i.save()
             Allergy(user_id = login_user, ingre = i).save()

    for hate_menu in request.session['hate_menu']:
        temp = Menu.objects.get(name = hate_menu)
        if(temp):
            Hate_menu(user_id = login_user, menu = temp).save()

    for ingredient in request.session['hate_ingre']:
        i = Ingredient.objects.get(name = ingredient)
        if(i):
            Hate_ingredient(user_id = login_user, ingre = i).save()
        else:
            i = Ingredient(name = ingredient)
            i.save()
            Hate_ingredient(user_id = login_user, ingre = i).save()

    request.session.modified = True
    del request.session['username'], request.session['pwd'], request.session['email'], request.session['name'], request.session['gender'], request.session['birthday_str'], request.session['religion'], request.session['vegetarian'], request.session['allergy'], request.session['hate_menu'], request.session['hate_ingre']
    return render(request, 'user/signin.html')