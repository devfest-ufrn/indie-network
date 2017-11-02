from django.http import HttpResponse
from django.shortcuts import render
from steamRequests.models import SteamUser
from steamRequests.models import SteamGame
from django.http import JsonResponse


def index(request):
    return HttpResponse("You are at Steam requests index")

def userInfos(request, username = ''):
    user = SteamUser(username)
    #return wgordo.name
    return JsonResponse(user.asJson())

def showGames(request, username = ''):
    user = SteamUser(username)
    #return user.gamesList
    return JsonResponse(user.gamesList, safe = False)

def gameInfos(request, appid = ""):
    game = SteamGame(appid)
    return HttpResponse(game.gameName)
