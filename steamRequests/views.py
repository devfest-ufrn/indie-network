from django.http import HttpResponse
from django.shortcuts import render
from steamRequests.models import SteamUser
from steamRequests.models import SteamGame
from django.http import JsonResponse


def index(request):
    return HttpResponse("You are at Steam requests index")

def userInfos(request, username = ''):
    return JsonResponse(SteamUser(username).asJson())

def userGames(request, username = ''):
    return JsonResponse(SteamUser(username).formatedGamesList(), safe = False)

def gameInfos(request, appid = ""):
    return JsonResponse(SteamGame(appid).gameInfos, safe = False)
