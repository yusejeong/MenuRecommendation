from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from YTMT.models import *
from django.contrib import auth
import datetime
from . import session as SS
from . import utils

'''
    회원가입 관련 기능이 저장되는 view 파일입니다.
    회원가입에 추가적인 기능이 필요하면 추가하십시요.

'''

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
    return render(request, 'user/allergy.html')

def allergy(request):
    return render(request, 'user/allergy.html')

def allergysave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    ingre_list = []
    menu_list = []
    for ingre in Ingredient.objects.all():
        ingre_list.append(ingre.name)

    for menu in Menu.objects.all():
        menu_list.append(Menu.name)

    # 일대다
    return render(request, 'user/hatelist.html',{'ingredient_list': ingre_list})

def hatelist(request):
    return render(request, 'user/hatelist.html')

def hatelistsave(request):
    login_user = SS.find_user(request)
    userProfile = Profile.objects.get(user_id = login_user)

    request.session.modified = True
    del request.session['username']
    return render(request, 'user/signin.html')