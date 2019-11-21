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

def signinrequest(request):
    if request.method == "POST":
        id = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username = id, password = pwd)
        if user is not None:
            auth.login(request, user)
            SS.create_session(request, id, pwd)
            return HttpResponseRedirect(reverse('YTMT:mainpage'))
        else:
            '''
               수정 필요한 부분, 비동기적으로 로그인이 되지 않았음을 보내는 기능을 만들어야함
                현재는 Template의 수정이 우선되어야 기능구현을 확인할 수 있으므로 추후 방안논의
            '''
            return render(request, 'user/signin.html', {'error':'id or pwd is incorrect'})
        # 팝업창으로 띄우기
    else:
        return render(request, 'user/signin.html')


# 회원가입
def signup(request):
    auth.logout(request)
    return render(request, 'user/signup.html')

def signuprequest(request):
    if request.method == "POST":
        if request.POST["pwd"] == request.POST["pwdchk"]:
            if request.POST["email2"] != "etc":
                user = User.objects.create_user(
                    username = request.POST["id"], password = request.POST["pwd"], email = request.POST["email"] + "@" + request.POST["email2"])
            else:
                user = User.objects.create_user(
                    username = request.POST["id"], password = request.POST["pwd"], email = request.POST["email"])
            #프로필 객체를 생성
            userProfile = Profile.objects.create(user_id = user, birth = datetime.datetime.now(), name = request.POST["name"])
            userProfile.save()
            request.session['username'] = request.POST["id"]
            return render(request, 'user/birthandgender.html')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

def birthandgender(request):
    return render(request, 'user/birthandgender.html')

def birthandgendersave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    # 성별 구분
    gender = request.POST.get("gender")
    if gender == "M":
        gender_num = 1
    else:
        gender_num = 2

    brithday_str = request.POST.get('birth')
    # POST 방식으로 받아온 birth가 String값이기 때문에 DateTime 객체로 변환
    birthday_obj = datetime.datetime.strptime(brithday_str, '%Y-%m-%d')

    userProfile.gender = gender_num
    userProfile.birth = birthday_obj
    # 수정된 프로필을 저장
    userProfile.save()
    return render(request, 'user/religion.html')


# 회원가입 추가정보
def religion(request):
    return render(request, 'user/religion.html')

def religionsave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    reli_name = request.POST.get("religion")
    userProfile.reli_id = utils.get_reli_id(reli_name)

    userProfile.save()

    return render(request, 'user/vegetarian.html')

def vegetarian(request):
    return render(request, 'user/vegetarian.html')

def vegetariansave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    vege_name = request.POST.get("vegetarian")
    userProfile.vege_id = utils.get_vege_id(vege_name)

    userProfile.save()

    return render(request, 'user/allergy.html', {"ingre_list" : ingre_list})

def allergy(request):

    return render(request, 'user/allergy.html', {"ingre_list" : ingre_list})

def allergysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)
    allergy_list = request.POST.get("allergy_list")

    allergy_list = json.loads(allergy_list)

    for allergy in allergy_list:
        print(allergy)
        i = Ingredient.objects.get(name = allergy)
        if(i):
            Allergy(user_id = login_user, ingre = i).save()
        else:
             i = Ingredient(name = allergy)
             i.save()
             Allergy(user_id = login_user, ingre = i).save()

    # 일대다
    return render(request, 'user/hatelist.html',{'ingredient_list': ingre_list,'menu_list' : menu_list})

def hatelist(request):
    return render(request, 'user/hatelist.html')

def hatelistsave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    hate_menu_list = request.POST.get("menu_list")
    hate_menu_list = json.loads(hate_menu_list)

    hate_ingredient_list = request.POST.get("ingredient_list")
    hate_ingredient_list = json.loads(hate_ingredient_list)
    for hate_menu in hate_menu_list:
        temp = Menu.objects.get(name = hate_menu)
        if(temp):
            Hate_menu(user_id = login_user, menu = temp).save()

    for ingredient in hate_ingredient_list:
        i = Ingredient.objects.get(name = ingredient)
        if(i):
            Hate_ingredient(user_id = login_user, ingre = i).save()
        else:
            i = Ingredient(name = ingredient)
            i.save()
            Hate_ingredient(user_id = login_user, ingre = i).save()

    request.session.modified = True
    del request.session['username']
    return render(request, 'user/signin.html')
