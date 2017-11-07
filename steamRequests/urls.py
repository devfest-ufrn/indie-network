from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^user/(?P<username>\S+)/infos/$', views.userInfos, name = 'userInfos'),
    url(r'^user/(?P<username>\S+)/games/$', views.userGames, name = 'userGameList'),
    url(r'^game/(?P<appid>[0-9]+)/infos/$', views.gameInfos, name = "gameInfos"),

]