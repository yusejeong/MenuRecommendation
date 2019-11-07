from django.urls import path

from . import views

app_name = 'YTMT'
urlpatterns = [
    # 로그인
    path('', views.signin, name = 'signin'),
    path('signinrequest', views.signinrequest, name = 'signinrequest'),

    # 회원가입
    path('signup', views.signup, name = 'signup'),
    path('signup/signuprequeset', views.signuprequest, name = 'signuprequest'),
    path('signup/birthandgender', views.birthandgender, name = 'birthandgender'),
    path('signup/birthandgendersave', views.birthandgendersave, name = 'birthandgendersave'),

    # 회원가입 추가정보
    path('signup/religion', views.religion, name = 'religion'),
    path('signup/religionsave', views.religionsave, name = 'religionsave'),
    path('signup/vegetarian', views.vegetarian, name = 'vegetarian'),
    path('signup/vegetariansave', views.vegetariansave, name = 'vegetariansave'),
    path('signup/allergy', views.allergy, name = 'allergy'),
    path('signup/allergysave', views.allergysave, name = 'allergysave'),
    path('signup/hatelist', views.hatelist, name = 'hatelist'),
    path('signup/hatelistsave', views.hatelistsave, name = 'hatelistsave'),

    # 회원정보찾기
    path('findinfo', views.findinfo, name = 'findinfo'),
    path('findinfo/findid', views.findid, name = 'findid'),
    path('findinfo/findpw', views.findpw, name = 'findpw'),

    # 메인
    path('mainpage', views.mainpage, name = 'mainpage'),
    
    #마이페이지
    path('mypagemain', views.mypagemain, name= 'mypagemain'),
    path('mypagemain/infomodify', views.infomodify, name= 'infomodify'),
    path('mypagemain/infomodifysave', views.infomodifysave, name= 'infomodifysave'),
    path('mypagemain/infomodifynext', views.infomodifynext, name= 'infomodifynext'),
    path('mypagemain/selectinfo', views.selectinfo, name='selectinfo'),
]