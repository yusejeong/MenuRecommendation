from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime, random

from django.core.mail import EmailMessage


# 회원정보찾기
def findinfo(request):
    return render(request, 'findinfo/findinfo.html')

def findid(request):
    return render(request, 'findinfo/findid.html')

def chkinfo(request):
    if request.POST["email2"] != "etc":
        email = request.POST["email"] + "@" + request.POST["email2"]
    else:
        email = request.POST["email"]
    print(email)

    temp_user = User.objects.filter(email = email)
    print(temp_user.username)
    if temp_user is None:
        print("F")
        return HttpResponse("Failure")

    temp_profile = Profile.objects.filter(user_id = temp_user)
    print(temp_profile.name)
    if temp_profile is None:
        print("F")
        return HttpResponse("Failure")

    if temp_profile.name == request.POST["name"]:
        id = temp_user.username
        print("S")
        return HttpResponse(json.dumps({'id': id}), content_type="application/json")
    return HttpResponse("Failure")

def findpw(request):
    return render(request, 'findinfo/findpw.html')

def chkinfo(request):
    return httpResponse("success")

def sendpw(request):
    id = request.POST['id']
    temp_user = User.objects.get(username=id)
    if request.POST["email2"] != "etc":
        email = request.POST["email"] + "@" + request.POST["email2"]
    else:
        email = request.POST["email"]

    if temp_user.email == email:
        temp_user.is_active = True
        pw = random.randrange(10000, 100000)
        mail = EmailMessage('[니맛내맛] 임시 비밀번호 입니다', '임시비밀번호는 '+str(pw)+' 입니다.', to=[email])
        mail.send()
        temp_user.set_password(str(pw))
        temp_user.save()
    return render(request, 'user/signin.html')