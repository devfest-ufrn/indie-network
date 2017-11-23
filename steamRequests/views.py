from django.http import HttpResponse
from django.shortcuts import render
from steamRequests.models import SteamUser
from steamRequests.models import SteamGame
from django.http import JsonResponse
from authentication.models import SteamUser as user


def index(request):
    for u in user.objects.all():
        if (u.is_active):
            return JsonResponse(SteamUser(u.steamid).asJson(), safe = False)

def userInfos(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).asJson())

def userGames(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).formatedGamesList(), safe = False)

def gameInfos(request, appid = ""):
    return JsonResponse(SteamGame(appid).gameInfos, safe = False)