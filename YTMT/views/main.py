from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime
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

    # 사용자의 좋아했던 메뉴를 로드
    history_list = History.objects.filter(user_id = login_user)
    menu_list = []

    for food in history_list:
        menu_name = food.menu
        cos = sim_df[str(menu_name)].sort_values(ascending=False)
        for name in cos.head(3).index:
            menu_list.append(Menu.objects.get(name = name))

    return render(request, 'menureco/menureco.html',{ 'menu_list': menu_list })

def friendreco(request):
    return render(request, 'menureco/friendreco.html')
