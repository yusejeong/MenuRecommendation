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