from django.urls import path

from . import views

app_name = 'YTMT'
urlpatterns = [
    path('', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signup/birthandgender', views.BirthandGenderView.as_view(), name = 'birthandgender'),
    path('signup/religion', views.ReligionView.as_view(), name = 'religion'),
    path('signup/allergie', views.AllergieView.as_view(), name = 'allergie'),
    path('signup/vegetarian', views.VegetarianView.as_view(), name = 'vegetarian'),
    path('signup/hatelist', views.HatelistView.as_view(), name = 'hatelist'),
]