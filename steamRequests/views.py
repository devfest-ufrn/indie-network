from django.http import HttpResponse
from django.shortcuts import render
from steamRequests.models import SteamUser
from django.http import JsonResponse


def index(request):
    return HttpResponse("You are at Steam requests index")

def showName(request, username = ''):
    user = SteamUser(username)
    #return wgordo.name
    return JsonResponse(user.asJson())

def showGames(request, username = ''):
    user = SteamUser(username)
    #return user.gamesList
    return HttpResponse(user.gamesList)
