from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
from . import session as SS

'''
    로그인 관련 기능이 저장되는 view 파일입니다.
    로그인에 추가적인 기능이 필요하면 추가하십시요.
'''

def signin(request):
    return render(request, 'user/signin.html')

def signinrequest(request):
    if request.method == "POST":
        id = request.POST['username']
        pwd = request.POST['password']
        
        res_data = {}
        if not (id):
            res_data['error']="아이디를 입력하세요."
        elif not (pwd):
            res_data['error']="비밀번호를 입력하세요."
        else:
            user = auth.authenticate(request, username = id, password = pwd)
            if user is not None:
                auth.login(request, user)
                SS.create_session(request, id, pwd)
                return redirect('YTMT:mainpage')
            else:
                res_data['error'] = "아이디 또는 비밀번호가 잘못되었습니다."
        return render(request,'user/signin.html', res_data)
    else:
        return render(request, 'user/signin.html')

def signout(request):
    request.session.modified = True
    del request.session['username'], request.session['password']

    auth.logout(request)
    return render(request, 'user/signin.html')