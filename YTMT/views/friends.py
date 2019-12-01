#-*-coding: utf-8
from django.shortcuts import render, get_list_or_404,get_object_or_404, redirect
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

def find_friend(request):
    name = request.POST.get("friend_name")

    profiles = get_list_or_404(Profile, name = name)
    find_list = []
    for profile in profiles:
        User_id = profile.user_id.username
        User_name = profile.name
        find_list.append([User_id, User_name])   
        
    return HttpResponse(json.dumps({'find_list': find_list}), content_type="application/json")

def add_friend(request):
    login_user = SS.find_user(request)
    temp_friend_id = request.POST.get("friend_id")
    friend = User.objects.get(username = temp_friend_id)

    Friend_list(user_id = login_user, friend_id = friend).save()

    return HttpResponse("success")

def remove_friend(request):
    login_user = SS.find_user(request)
    temp_friend_id = request.POST.get("friend_id")
    friend = User.objects.get(username = temp_friend_id)
    
    Friend_list.objects.filter(user_id = login_user, friend_id = friend).delete()
    
    return HttpResponse("Success")

def find_friend_from_list(request):
    login_user = SS.find_user(request)
    friend_name = request.POST.get("friend_id")
    
    
        #동명이인의 친구가 두명이상이라면
    
    return HttpResponse()