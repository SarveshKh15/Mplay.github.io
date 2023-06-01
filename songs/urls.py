from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [

    path('', views.index, name="SongHome"),
    path('<int:id>',views.play,name="playsongs"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('watchlater',views.watchlater,name="watchlater"),
    path('c/<str:channel>',views.channel,name='channel') ,
    path('upload',views.upload,name='upload'),
    path('search',views.search,name='search')
]