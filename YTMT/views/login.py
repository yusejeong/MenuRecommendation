from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
from . import session as SS

def signin(request):
    return render(request, 'user/signin.html')

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

def signout(request):
    request.session.modified = True
    del request.session['username'], request.session['password']
    return render(request, 'user/signin.html')