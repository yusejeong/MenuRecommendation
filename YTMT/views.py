from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth


#from django.template import loader

# Create your views here.

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
                username = request.POST["id"], password = request.POST["pwd"])
            auth.login(request, user)
            return redirect('YTMT:birthandgender')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

def birthandgender(request):
    return render(request, 'user/birthandgender.html')

def birthandgendersave(request):
    if request.method = "POST":
        if request.POST["man"] = 1:
        
        
    return render(request, 'user/religion.html')

# 회원가입 추가정보
def religion(request):
    return render(request, 'user/religion.html')

def allergy(request):
    return render(request, 'user/allergy.html')

def vegetarian(request):
    return render(request, 'user/vegetarian.html')

def hatelist(request):
    return render(request, 'user/hatelist.html')


# 회원정보찾기
def findinfo(request):
    return render(request, 'user/findinfo.html')

def findid(request):
    return render(request, 'user/findid.html')

def findpw(request):
    return render(request, 'user/findpw.html')


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
