from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime
import random
from . import session as SS
import json
import os
import math
import pandas as pd

sim_df = pd.read_csv("similarity_matrix.csv", index_col = 0)

# 메인
def mainpage(request):
    if request.session.get('username') is not None:
        return render(request, 'main.html')
    return render(request, 'user/signin.html')

    # 기능1
def menureco(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    # 사용자의 싫어하는 메뉴, 싫어하는 재료, 알레르기 리스트를 로드함
    hate_menu_list = Hate_menu.objects.filter(user_id = login_user)
    hate_ingredient_list = Hate_ingredient.objects.filter(user_id = login_user)
    Allergy_list = Allergy.objects.filter(user_id = login_user)

    #사용자의 종교, 채식주의 성향 확인
    user_religion_type = userProfile.reli_id
    user_vege_type = userProfile.vege_id

    # 종교, 채식주의 성향에 따른 필터 재료 목록 가져오기
    vegetarian_list = Vegetarian_case.objects.filter(vege_id = user_vege_type)
    religion_list = Religion_case.objects.filter(reli_id= user_religion_type)

    filter_list = []

    for hate_religion_ingre in religion_list:
        filter_list.append(hate_religion_ingre.ingre.name)
    # #채식 성향 재료 필터
    for hate_vege_ingre in vegetarian_list:
        filter_list.append(hate_vege_ingre.ingre.name)
    # #싫어하는 재료 필터
    for hate_ingredient in hate_ingredient_list:
        filter_list.append(hate_ingredient.ingre.name)
    # #알레르기 재료 필터
    for allergy in Allergy_list:
        filter_list.append(allergy.ingre.name)



    #중복 요소 제거
    filter_list = list(dict.fromkeys(filter_list))


    # 사용자의 좋아했던 메뉴를 로드
    history_list = History.objects.filter(user_id = login_user)
    menu_list = []

    heart_list = []
    for food in history_list:
        menu_name = food.menu
        cos = sim_df[str(menu_name)].sort_values(ascending=False)
        heart_list.append(Menu.objects.get(name = food.menu))
        for name in cos[0:2].index:
            menu_obj = Menu.objects.get(name = name)
            recipes = Recipe.objects.filter(menu = menu_obj)
            can_append = True

            for recipe in recipes:
                if recipe.ingre.name in filter_list:
                    can_append = False
                    break

            if can_append:
                menu_list.append(menu_obj)

    filter_menu = []

    menu_cnt = Menu.objects.count()

    while True:
        while True:
            menu_id = random.randint(1, menu_cnt)
            if Menu.objects.filter(id = menu_id).exists():
                break
        menu_obj = Menu.objects.get(id = menu_id)
        recipes = Recipe.objects.filter(menu = menu_obj)
        can_append = True

        for recipe in recipes:
            if recipe.ingre.name in filter_list:
                # print(menu_obj.name + " has " + recipe.ingre.name)
                can_append = False
                break

        if can_append:
            # print("append : " + menu_obj.name)
            filter_menu.append(menu_obj)

        if len(filter_menu) >= 5:
            break

    menu_list.extend(filter_menu)

    return render(request, 'menureco/menureco.html',{ 'menu_list': menu_list, "heart_list": heart_list})
def locationreco(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)
    return render(request, 'menureco/locationreco.html')
def friendreco(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    temp_objects = Friend_list.objects.filter(user_id = login_user)
    temp_list = []
    for temp in temp_objects:
        temp_list.append(temp.friend_id)
    friend_list = Profile.objects.filter(user_id__in = temp_list)

    return render(request, 'menureco/friendreco.html', {"friend_list" : friend_list})

def groupmenureco(request):
    login_user = SS.find_user(request)
    friends_list = request.POST.get("friend_list")
    friends_list = json.loads(friends_list)

    friends_list.append(login_user.username)

    filter_list = []

    user_objects = User.objects.filter(username__in = friends_list)
    for user in user_objects:
        userProfile = Profile.objects.get(user_id = user)
        hate_menu_list = Hate_menu.objects.filter(user_id = user)
        hate_ingredient_list = Hate_ingredient.objects.filter(user_id = user)
        Allergy_list = Allergy.objects.filter(user_id = user)

        #사용자의 종교, 채식주의 성향 확인
        user_religion_type = userProfile.reli_id
        user_vege_type = userProfile.vege_id

        # 종교, 채식주의 성향에 따른 필터 재료 목록 가져오기
        vegetarian_list = Vegetarian_case.objects.filter(vege_id = user_vege_type)
        religion_list = Religion_case.objects.filter(reli_id= user_religion_type)

        for hate_religion_ingre in religion_list:
            filter_list.append(hate_religion_ingre.ingre.name)
            #채식 성향 재료 필터
        for hate_vege_ingre in vegetarian_list:
            filter_list.append(hate_vege_ingre.ingre.name)
        # #싫어하는 재료 필터
        for hate_ingredient in hate_ingredient_list:
            filter_list.append(hate_ingredient.ingre.name)
        # #알레르기 재료 필터
        for allergy in Allergy_list:
            filter_list.append(allergy.ingre.name)

    filter_list = list(dict.fromkeys(filter_list))

    menu_list = []

    filter_menu = []

    menu_cnt = Menu.objects.count()

    while True:
        menu_id = random.randint(1, menu_cnt)
        menu_obj = Menu.objects.get(id = menu_id)
        recipes = Recipe.objects.filter(menu = menu_obj)
        can_append = True

        for recipe in recipes:
            if recipe.ingre.name in filter_list:
                # print(menu_obj.name + " has " + recipe.ingre.name)
                can_append = False
                break

        if can_append:
            # print("append : " + menu_obj.name)
            filter_menu.append(menu_obj)

        if len(filter_menu) >= 5:
            break

    menu_list.extend(filter_menu)

    return render(request, 'menureco/menureco.html', { 'menu_list': menu_list })

def restaurantreco(request):
    restaurants = Restaurant.objects.filter()
    return render(request, 'menureco/restaurantreco.html',{'restaurants': restaurants})

def menu_like(request):
#    if request.method == "POST":
        login_user = SS.find_user(request)
        like_menu_id = request.POST.get("menu_id")
        like_menu = Menu.objects.get(id = like_menu_id)
        status = 0

        try:
            history =History.objects.get(user_id = login_user, menu = like_menu)
        except History.DoesNotExist:
            newHistory = History.objects.create(user_id = login_user, menu = like_menu)
            newHistory.save()
            status = 1

        if status == 0 :
            history.delete()
            status = -1

#        like_menu.likes = like_menu.likes + status
        like_menu.likes = History.objects.filter(menu = like_menu).count()
        like_menu.save()

        return HttpResponse(json.dumps({'like_id' : like_menu.id, 'like_count' : like_menu.likes, 'status' : status }), content_type="application/json")
#    return HttpResponse("posterror")
