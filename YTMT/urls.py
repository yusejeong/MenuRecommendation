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

    # 로그아웃
    path('signout', views.signout, name = 'signout'),

    # 메인
    path('mainpage', views.mainpage, name = 'mainpage'),

    # 마이페이지_수정
    path('mypage', views.mypagemain, name = 'mypagemain'),
    path('mypage/infomodify', views.infomodify, name = 'infomodify'),
    path('mypage/infomodifysave', views.infomodifysave, name = 'infomodifysave'),
    path('mypage/infomodifynext', views.infomodifynext, name = 'infomodifynext'),
    path('mypage/selectinfo', views.selectinfo, name ='selectinfo'),
    path('mypage/religionmodify', views.religionmodify, name ='religionmodify'),
    path('mypage/religionmodifysave', views.religionmodifysave, name ='religionmodifysave'),
    path('mypage/vegetarianmodify', views.vegetarianmodify, name ='vegetarianmodify'),
    path('mypage/vegetarianmodifysave', views.vegetarianmodifysave, name ='vegetarianmodifysave'),
    path('mypage/allergymodify', views.allergymodify, name ='allergymodify'),
    path('mypage/allergymodifysave', views.allergymodifysave, name ='allergymodifysave'),
    path('mypage/hatemodify', views.hatemodify, name ='hatemodify'),
    path('mypage/hatemodifysave', views.hatemodifysave, name ='hatemodifysave'),

    # 마이페이지_기타
    path('mypage/history', views.history, name ='history'),
    path('mypage/friendlist', views.friendlist, name ='friendlist'),

    # 기능1
    path('menureco', views.menureco, name = 'menureco'),
   path('friendreco', views.friendreco, name = 'friendreco'),
]
