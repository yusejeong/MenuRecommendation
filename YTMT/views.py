from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
import datetime
#from django.template import loader

# Create your views here.

def save_user_session(request, User):
    '''
        위와 같은 방식은 Session의 User영역에 User 객체를 넣는 시도를 의미함
        하지만 Session은 객체를 저장할 수 있는 방법이 없음
        따라서 아래와 같이 세션에 넣을 수 있는 사용자의 ID와 Password를 넘겨주는 방식으로
        로그인 상태를 유지해야함
    '''
    request.session['userid'] = User.username
    request.session['password'] = User.password
    '''
        세션에는 프로필 객체가 들어갈 수 없음,
        프로필 조회가 필요하다면 username 으로 프로필의 외래키를 조회하는 방식을 사용해야함
    '''


# 로그인
def signin(request):
    return render(request, 'user/signin.html')

def signinrequest(request):
    if request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']
        print(id,pw)
        user = auth.authenticate(request, username = id, password = pw)
        if user is not None:
            auth.login(request, user)
            save_user_session(request, user)
            return HttpResponseRedirect(reverse('YTMT:mainpage'))
        else:
            '''
               수정 필요한 부분, 비동기적으로 로그인이 되지 않았음을 보내는 기능을 만들어야함
                현재는 Template의 수정이 우선되어야 기능구현을 확인할 수 있으므로 추후 방안논의
            '''
            return render(request, 'user/signin.html', {'error':'id or pw is incorrect'})
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
            if request.POST["email2"] is not None:
                user = User.objects.create_user(
                    username = request.POST["id"], password = request.POST["pwd"], email = request.POST["email"] + "@" + request.POST["email2"])
            else:
                user = User.objects.create_user(
                    username = request.POST["id"], password = request.POST["pwd"], email = request.POST["email"])
            save_user_session(request, user)
            return redirect('YTMT:birthandgender')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

def birthandgender(request):
    return render(request, 'user/birthandgender.html')

def birthandgendersave(request):
    id = request.session.get('userid')
    #위에서 저장된 session 안의 userid를 저장

    login_user = User.objects.get(username = id)
    #id가 동일한 user객체를 검색하여 생성

    #프로필 객체를 생성
    userProfile = Profile.objects.create(user_id = login_user, birth = datetime.datetime.now())

    gender = request.POST.get("gender")
    if gender == "M":
        gender_num = 1
    else:
        gender_num = 2

    brithday_str = request.POST.get('birth')

    #POST 방식으로 받아온 birth가 String값이기 때문에 DateTime 객체로 변환
    birthday_obj = datetime.datetime.strptime(brithday_str, '%Y-%m-%d')

    userProfile.gender = gender_num
    userProfile.birth = birthday_obj
    #수정된 프로필을 저장
    userProfile.save()
    return render(request, 'user/religion.html')


# 회원가입 추가정보
def religion(request):
    return render(request, 'user/religion.html')

def get_reli_id(reli_name):
    return {'hindu':1, 'budd':2, 'christian':3, 'catholic':4, 'islam':5, 'juda':6, 'sikh':7, 'none':8}.get('reli_name', 8)

def religionsave(request):

    id = request.session.get('userid')

    userNow = User.objects.get(username = id)
    userProfile = Profile.objects.get(user_id = userNow)


    reli_name = request.POST.get("religion")
    userProfile.reli_id = get_reli_id(reli_name)

    userProfile.save()
    return render(request, 'user/vegetarian.html')

def vegetarian(request):
    return render(request, 'user/vegetarian.html')

def get_vege_id(vege_name):
    return {'vegan':1, 'lacto':2, 'ovo':3, 'lactoovo':4, 'pesco':5, 'flo':6, 'flexi':7}.get('vege_name', 8)

def vegetariansave(request):
    id = request.session.get('userid')
    userNow = User.objects.get(username = id)
    userProfile = Profile.objects.get(user_id = userNow)

    vege_name = request.POST.get("vegetarian")
    userProfile.vege_id = get_vege_id(vege_name)

    userProfile.save()
    return render(request, 'user/allergy.html')

def allergy(request):
    return render(request, 'user/allergy.html')

def allergysave(request):

    id = request.session.get('userid')
    userNow = User.objects.get(username = id)
    userProfile = Profile.objects.get(user_id = userNow)

    # 일대다
    return render(request, 'user/hatelist.html')

def hatelist(request):
    return render(request, 'user/hatelist.html')

def hatelistsave(request):
    id = request.session.get('userid')
    userNow = User.objects.get(username = id)
    userProfile = Profile.objects.get(user_id = userNow)

    expire_session(request)
    return render(request, 'user/signin.html')

def expire_session(request):
    request.session.modified = True
    del request.session['userid'], request.session['password']
    return render(request, 'user/signin.html')


# 회원정보찾기
def findinfo(request):
    return render(request, 'findinfo/findinfo.html')

def findid(request):
    return render(request, 'findinfo/findid.html')

def findpw(request):
    return render(request, 'findinfo/findpw.html')


# 로그아웃
def signout(request):
    request.session.modified = True
    del request.session['user']
    return render(request, 'user/signin.html')


# 메인
def mainpage(request):
    if request.session.get('userid') is not None:
        return render(request, 'main.html')
    return render(request, 'user/signin.html')

def menureco(request):
    return render(request, 'user/menureco.html')

# 마이페이지
def mypagemain(request):
    return render(request, 'mypage/mypagemain.html')

def infomodify(request):
    return render(request, 'mypage/infomodify.html')

def infomodifysave(request):
    id = request.session.get('userid')
    userNow = User.objects.get(username = id)
    if request.method == "POST":
        if request.POST["pwd"] == userNow.password:
            if request.POST["newpwd"] == request.POST["pwdchk"]:
                userNow.password = request.POST["newpwd"]
                if request.POST["email2"] is not None:
                    userNow.email = request.POST["email"] + "@" + request.POST["email2"]
                else:
                    userNow.email = request.POST["email"]
                userNow.save()
                return render(request, 'mypage/mypagemain.html')
            return render(request,'mypage/infomodify.html')
        return render(request,'mypage/infomodify.html')
    return render(request,'mypage/infomodify.html')

def infomodifynext(request):
    id = request.session.get('userid')
    userNow = User.objects.get(username = id)
    if request.method == "POST":
        if request.POST["pwd"] == userNow.password:
            if request.POST["newpwd"] == request.POST["pwdchk"]:
                userNow.password = request.POST["newpwd"]
                if request.POST["email2"] is not None:
                    userNow.email = request.POST["email"] + "@" + request.POST["email2"]
                else:
                    userNow.email = request.POST["email"]
                userNow.save()
                return render(request, 'mypage/selectinfo.html')
            return render(request,'mypage/infomodify.html')
        return render(request,'mypage/infomodify.html')
    return render(request,'mypage/infomodify.html')

def selectinfo(request):
    return render(request, 'mypage/selectinfo.html')

def religionmodify(request):
    return render(request, 'mypage/religionmodify.html')

def vegetarianmodify(request):
    return render(request, 'mypage/vegetarianmodify.html')

def allergymodify(request):
    return render(request, 'mypage/allergymodify.html')

def hatemodify(request):
    return render(request, 'mypage/hatemodify.html')




class HistoryView(generic.DetailView):
    template_name = 'mypage/history.html'

class FriendlistView(generic.DetailView):
    template_name = 'mypage/friendlist.html'
