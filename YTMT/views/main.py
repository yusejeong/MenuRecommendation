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
    # print("사용자 종교, 채식 성향")
    # print(user_religion_type, user_vege_type)

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

    for food in history_list:
        menu_name = food.menu
        cos = sim_df[str(menu_name)].sort_values(ascending=False)
    
        for name in cos[1:4].index:
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


    return render(request, 'menureco/menureco.html',{ 'menu_list': menu_list })

def friendreco(request):
    return render(request, 'menureco/friendreco.html')
