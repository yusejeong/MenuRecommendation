from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'YTMT'
urlpatterns = [
    # 로그인
    path('', login.signin, name = 'signin'),
    path('signinrequest', login.signinrequest, name = 'signinrequest'),

    # 로그아웃
    path('signout', login.signout, name = 'signout'),

    # 회원가입
    path('signup', register.signup, name = 'signup'),
    path('signup/signuprequeset', register.signuprequest, name = 'signuprequest'),
    path('signup/idcheck', register.idcheck, name = 'idcheck'),
    path('signup/birthandgendersave', register.birthandgendersave, name = 'birthandgendersave'),

    # 회원가입 추가정보
    path('signup/religionsave', register.religionsave, name = 'religionsave'),
    path('signup/vegetariansave', register.vegetariansave, name = 'vegetariansave'),
    path('signup/allergysave', register.allergysave, name = 'allergysave'),
    path('signup/hatelistsave', register.hatelistsave, name = 'hatelistsave'),
    path('signup/profilecheck', register.profilecheck, name = 'profilecheck'),
    path('signup/signupfinal', register.signupfinal, name = 'signupfinal'),

    # 회원정보찾기
    path('findinfo', find_info.findinfo, name = 'findinfo'),
    path('findinfo/findid', find_info.findid, name = 'findid'),
    path('findinfo/findpw', find_info.findpw, name = 'findpw'),
    path('findinfo/sendpw', find_info.sendpw, name = 'sendpw'),
    path('findinfo/chkinfo', find_info.chkinfo, name = 'chkinfo'),
    
    # 메인
    path('mainpage', main.mainpage, name = 'mainpage'),
    # 기능1
    path('menureco', main.menureco, name = 'menureco'),
    path('friendreco', main.friendreco, name = 'friendreco'),
    # 기능2
    path('groupmenureco', main.groupmenureco, name = 'groupmenureco'),
    path('locationreco', main.locationreco, name = 'locationreco'),

    # 마이페이지_수정
    path('mypage', mypage.mypagemain, name = 'mypagemain'),
    path('mypage/selectinfo', mypage.selectinfo, name ='selectinfo'),
    path('mypage/infomodify', mypage.infomodify, name = 'infomodify'),
    path('mypage/infomodifysave', mypage.infomodifysave, name = 'infomodifysave'),
    path('mypage/religionmodify', mypage.religionmodify, name ='religionmodify'),
    path('mypage/religionmodifysave', mypage.religionmodifysave, name ='religionmodifysave'),
    path('mypage/vegetarianmodify', mypage.vegetarianmodify, name ='vegetarianmodify'),
    path('mypage/vegetarianmodifysave', mypage.vegetarianmodifysave, name ='vegetarianmodifysave'),
    path('mypage/allergymodify', mypage.allergymodify, name ='allergymodify'),
    path('mypage/allergymodifysave', mypage.allergymodifysave, name ='allergymodifysave'),
    path('mypage/hatemodify', mypage.hatemodify, name ='hatemodify'),
    path('mypage/hatemodifysave', mypage.hatemodifysave, name ='hatemodifysave'),

    # 마이페이지_기타
    path('mypage/history', mypage.history, name ='history'),
    path('mypage/friendlist', mypage.friendlist, name ='friendlist'),
    path('mypage/profile', mypage.profile, name= 'profile'),
    path('mypage/friendlistsave', mypage.friendlistsave, name ='friendlistsave'),

    #마이페이지_친구
    path('friends/find_friend', friends.find_friend, name = 'find_friend'),    
    path('friends/add_friend', friends.add_friend, name = 'add_friend'),
    path('friends/remove_friend', friends.remove_friend, name = 'remove_friend'),
    
    #좋아요
    path('menu/like', main.menu_like, name = 'menu_like'),
]
