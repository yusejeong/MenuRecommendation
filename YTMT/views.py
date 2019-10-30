from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth


#from django.template import loader

# from .models import User

# Create your views here.

def signin(request):
    return render(request, 'user/signin.html')

def signinrequest(request):
    if request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username = id, password = pw)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('YTMT:pagemain'))
        else:
            return render(request, 'user/signin.html', {'error':'id or pw is incorrect'})
    else:
        return render(request, 'user/signin.html')

def pagemain(request):
    return render(request, 'user/main.html')

def signup(request):
    return render(request, 'user/signup.html')

# def signuprequest(request):
#     if request.method == "POST":
#         if reuqest.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username = request.POST["username"], password = request.POST["password1"])
#             auth.login(request, user)
#             return redirect('main')
#         return render(request, 'user/signup.html')
#     return render(request, 'signup.html')


def birthandgender(request):
    return render(request, 'user/birthandgender.html')

def religion(request):
    return render(request, 'user/religion.html')

# class SignUpView(generic.DetailView):
#     template_name = 'user/signup.html'

# class BirthandGenderView(generic.DetailView):
#     template_name = 'user/birthandgender.html'

# class ReligionView(generic.DetailView):
#     template_name = 'user/religion.html'

class AllergieView(generic.DetailView):
    template_name = 'user/allergie.html'

class VegetarianView(generic.DetailView):
    template_name = 'user/vegetarian.html'

class HatelistView(generic.DetailView):
    template_name = 'user/hatelist.html'

class SignUpCompleteView(generic.DetailView):
    template_name = 'user/signupcomplete.html'


class FindInfoView(generic.DetailView):
    template_name = 'user/findinfo.html'

class FindIDView(generic.DetailView):
    template_name = 'user/findid.html'

class IDInfoView(generic.DetailView):
    template_name = 'user/idinfo.html'

class FindPWView(generic.DetailView):
    template_name = 'user/findpw.html'

class SendPWView(generic.DetailView):
    template_name = 'user/sendpw.html'


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
