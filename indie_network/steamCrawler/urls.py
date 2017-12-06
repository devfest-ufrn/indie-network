from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/(?P<steamid>[0-9]+)/infos/$', views.userInfos, name = 'userInfos'),
    url(r'^user/(?P<steamid>[0-9]+)/games/$', views.userGames, name = 'userGameList'),
    url(r'^game/(?P<appid>[0-9]+)/infos/$', views.gameInfos, name = 'gameInfos'),
	url(r'^outros/(?P<steamid>[0-9]+)/$', views.gameRelacionados, name = 'gameRecomendacoes'),

]