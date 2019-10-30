from django.urls import path

from . import views

app_name = 'YTMT'
urlpatterns = [
    path('', views.signin, name = 'signin'),
    path('signinrequest', views.signinrequest, name = 'signinrequest'),

    path('signup', views.signup, name = 'signup'),
    path('signup/birthandgender', views.birthandgender, name = 'birthandgender'),
    path('signup/religion', views.religion, name = 'religion'),
    path('signup/allergie', views.AllergieView.as_view(), name = 'allergie'),
    path('signup/vegetarian', views.VegetarianView.as_view(), name = 'vegetarian'),
    path('signup/hatelist', views.HatelistView.as_view(), name = 'hatelist'),

    path('pagemain', views.pagemain, name = 'pagemain'),
]