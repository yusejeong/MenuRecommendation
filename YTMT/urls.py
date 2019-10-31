from django.urls import path

from . import views

app_name = 'YTMT'
urlpatterns = [
    # 로그인
    path('', views.signin, name = 'signin'),
    path('signinrequest', views.signinrequest, name = 'signinrequest'),

    # 회원가입
    path('signup', views.signup, name = 'signup'),
    path('signup/birthandgender', views.birthandgender, name = 'birthandgender'),
    path('signup/signuprequeset', views.signuprequest, name = 'signuprequest'),

    # 회원가입 추가정보
    path('signup/religion', views.religion, name = 'religion'),
    path('signup/allergy', views.allergy, name = 'allergy'),
    path('signup/vegetarian', views.vegetarian, name = 'vegetarian'),
    path('signup/hatelist', views.hatelist, name = 'hatelist'),

    # 회원정보찾기
    path('findinfo', views.findinfo, name = 'findinfo'),
    path('findinfo/findid', views.findid, name = 'findid'),
    path('findinfo/findpw', views.findpw, name = 'findpw'),

    # 메인
    path('mainpage', views.mainpage, name = 'mainpage'),
]