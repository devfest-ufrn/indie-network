import requests
from django.db import models

class SteamUser:
    _STEAM_USER_URL = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={steamKey}&vanityurl={username}&format=json"
    _STEAM_WONED_GAMES_URL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamKey}&steamid={steam64id}&format=json"
    _STEAM_KEY = "C0A26A72E4EC723F45C3EA9543B7B7F1"
    _STEAM_USER_INFOS_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamKey}&steamids={steam64ID}"
    
    #remover depois
    _GAME_INFO_URL = "http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={steamKey}&appid={appid}&format=json"

    def __init__(self, username):
        self.username = username
        self.steam64ID = self._getSteamID(username)
        self._infos = self._getUserInfos()
        self.name = self._getName(self._infos)
        self.country = self._getCountry(self._infos)
        self.gamesList = self._getGames()

    def __str__(self):
        return  "Username: " + self.username + "\nReal name: " + self.name + "\nCountry: " + self.country

    def _getSteamID(self, username):
        url = self._STEAM_USER_URL.replace("{steamKey}", self._STEAM_KEY).replace("{username}", username)
        return requests.get(url).json().get('response').get('steamid')
    
    def _getUserInfos(self):
        url = self._STEAM_USER_INFOS_URL.replace("{steamKey}", self._STEAM_KEY).replace("{steam64ID}", self.steam64ID)
        return requests.get(url).json().get('response').get('players')[0]

    def _getName(self, player):
        return player.get('realname')

    def _getCountry(self, player):
        return player.get('loccountrycode')

    def _getGames(self):
        url = self._STEAM_WONED_GAMES_URL.replace('{steamKey}', self._STEAM_KEY).replace('{steam64id}', self.steam64ID)

        games = {}
        for item in requests.get(url).json().get('response').get('games'):
            games[item.get('appid')] = SteamGame(item.get('appid')).gameName
        #return requests.get(url).json().get('response').get('games')
        return games

    def showMyGames(self):
        for item in self.gamesList:
            url = self._GAME_INFO_URL.replace('{steamKey}', self._STEAM_KEY).replace('{appid}', str(item.get('appid')))
            gameName = requests.get(url).json().get('game').get('gameName')
            if gameName is None or gameName.find('ValveTestApp') != -1 or gameName is '':
                pass
            else:
                print(gameName)
    
    def asJson(self):
        attributes = [item for item in dir(self) if not item.startswith('__') and not item.startswith('_') and not callable(getattr(self, item))]
        json = {}
        for item in attributes:
            json[item] = getattr(self, item)
        return json

class SteamGame:
    _GAME_INFO_URL = "http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key={steamKey}&appid={appid}&format=json"
    _STEAM_KEY = "C0A26A72E4EC723F45C3EA9543B7B7F1"
    
    def __init__(self, appID):
        self.gameInfos = self._getGameInfos(appID)
        self.gameName = self.gameInfos.get('gameName')

    def _getGameInfos(self, appID):
        url = self._GAME_INFO_URL.replace('{steamKey}', self._STEAM_KEY).replace('{appid}', str(appID))
        return requests.get(url).json().get('game')
'''
#main
wgordo = SteamUser("wgordo")
print (wgordo.getGames())

game = SteamGame("400")
print (game.gameInfos)

'''