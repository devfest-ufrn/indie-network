from django.http import HttpResponse
from django.shortcuts import render
from .models import SteamUser
from .models import SteamGame, Games
from django.http import JsonResponse
from indie_network.authentication.models import SteamUser as user


def index(request):
    for u in user.objects.all():
        if (u.is_authenticated):
            return JsonResponse(SteamUser(u.steamid).asJson(), safe = False)

def userInfos(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).asJson())

def userGames(request, steamid = ''):
    return JsonResponse(SteamUser(steamid).formatedGamesList(), safe = False)

def gameInfos(request, appid = ""):
    return JsonResponse(SteamGame(appid).infos, safe = False)

def gameRelacionados(request, steamid):
	games_n = SteamUser(steamid).games
	games_recomendation = {}
	dbgames = Games.objects.all()
	recomendado = {}
	for game in games_n:
		jogo = SteamGame(game['appid'])

		if(jogo.infos['Genre'] != 'Null'):
			r = Games.objects.filter(genre = jogo.infos['Genre'])
			if len(r)==0:
				r = 0
			else:
				r = 1
			recomendado[jogo.infos['Genre']] = r
			# print(recomendado)

	context = {
		'recomendado':recomendado

	}

	return JsonResponse(recomendado,safe = False)
	# return render(request, 'dashboard_user.html',context)