from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^userInfos/(?P<username>\S+)/$', views.userInfos, name = 'userInfos'),
    url(r'^gamesList/(?P<username>\S+)/$', views.showGames, name = 'userGameList'),
    url(r'^gameInfos/(?P<appid>[0-9]+)/$', views.gameInfos, name = "gameInfos"),

]