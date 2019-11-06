from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth


#from django.template import loader

# Create your views here.

def save_user_session(request, User):
    request.session['user'] = User

def save_profile_session(request, Profile):
    request.session['profile'] = Profile

# 로그인
def signin(request):
    return render(request, 'user/signin.html')

def signinrequest(request):
    if request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username = id, password = pw)
        if user is not None:
            auth.login(request, user)
            save_user_session(request, user)
            return HttpResponseRedirect(reverse('YTMT:mainpage'))
        else:
            return render(request, 'user/signin.html', {'error':'id or pw is incorrect'})
        # 팝업창으로 띄우기
    else:
        return render(request, 'user/signin.html')


# 회원가입
def signup(request):
    return render(request, 'user/signup.html')

def signuprequest(request):
    if request.method == "POST":
        if request.POST["pwd"] == request.POST["pwdchk"]:
            # 이메일 유효성 체크
            user = User.objects.create_user(
                username = request.POST["id"], password = request.POST["pwd"], email = request.POST["email"]+request.POST["email2"])
            auth.login(request, user)
            save_user_session(request, user)
            return redirect('YTMT:birthandgender')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

def birthandgender(request):
    return render(request, 'user/birthandgender.html')

def birthandgendersave(request):
    user = request.session.get('user')
    profile = Profile(user)

    gender = request.POST.get("gender")
    if gender == "M":
        gender_num = 1
    else:
        gender_num = 0

    profile.gender = gender_num
    profile.birth = request.POST.get("birth")
    save_profile_session(request, profile)
    return render(request, 'user/religion.html')

# 회원가입 추가정보
def religion(request):
    return render(request, 'user/religion.html')

def get_reli_id(reli_name):
    return {'hindu':1, 'budd':2, 'christian':3, 'catholic':4, 'islam':5, 'juda':6, 'sikh':7, 'none':8}.get('reli_name', 8)

def religionsave(request):
    profile = request.session.get('profile')
    reli_name = request.POST.get("religion")
    profile.reli_id = get_reli_id(reli_name)
    return render(request, 'user/vegetarian.html')

def vegetarian(request):
    return render(request, 'user/vegetarian.html')

def get_vege_id(vege_name):
    return {'vegan':1, 'lacto':2, 'ovo':3, 'lactoovo':4, 'pesco':5, 'flo':6, 'flexi':7}.get('vege_name', 8)

def vegetariansave(request):
    profile = request.session.get('profile')
    vege_name = request.POST.get("vegetarian")
    profile.vege_id = get_vege_id(vege_name)
    return render(request, 'user/allergy.html')

def allergy(request):
    return render(request, 'user/allergy.html')

def allergysave(request):
    profile = request.session.get('profile')
    # 일대다
    return render(request, 'user/hatelist.html')

def hatelist(request):
    return render(request, 'user/hatelist.html')

def hatelistsave(request):
    profile = request.session.get('profile')
    expire_session(request)
    return render(request, 'user/signin.html')

def expire_session(request):
    request.session.modified = True
    del request.session['user'], request.session['profile']
    return render(request, 'user/signin.html')


# 회원정보찾기
def findinfo(request):
    return render(request, 'user/findinfo.html')

def findid(request):
    return render(request, 'user/findid.html') 

def findpw(request):
    return render(request, 'user/findpw.html')

def signout(request):
    request.session.modified = True
    del request.session['user']
    return render(request, 'user/signin.html')


# 메인
def mainpage(request):
    return render(request, 'main.html')


class MypageView(generic.DetailView):
    template_name = 'mypage/mypage.html'

class EditInforView(generic.DetailView):
    template_name = 'mypage/editinfo.html'

class EditMoreInfoView(generic.DetailView):
    template_name = 'mypage/editmoreinfo.html'

class EditReligionView(generic.DetailView):
    template_name = 'user/religion.html'

class EditAllergieView(generic.DetailView):
    template_name = 'user/allergie.html'

class EditVegetarianView(generic.DetailView):
    template_name = 'user/vegetarian.html'

class EditHatelistView(generic.DetailView):
    template_name = 'user/hatelist.html'

class HistoryView(generic.DetailView):
    template_name = 'mypage/history.html'

class FriendlistView(generic.DetailView):
    template_name = 'mypage/friendlist.html'
