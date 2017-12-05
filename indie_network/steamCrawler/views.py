from django.http import HttpResponse
from django.shortcuts import render
from .models import SteamUser
from .models import SteamGame
from django.http import JsonResponse
from indie_network.authentication.models import SteamUser as user


def index(request):
    for u in user.objects.all():
        if (u.is_authenticated):
            return render(request, 'steamCrawler/index.html', {'user': (SteamUser(u.steamid)).asJson()})

def userInfos(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).asJson())

def userGames(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).formatedGamesList())
    #return render(request, 'steamCrawler/dashboard_user.html', {'user': SteamUser(steamid).asJson(), 'games': SteamUser(steamid).formatedGamesList()})

def gameInfos(request, appid = ""):
    return JsonResponse(SteamGame(appid).gameInfos, safe = False)