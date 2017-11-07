import requests
from django.db import models

class SteamUser:
    _STEAM_USER_URL = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={steamKey}&vanityurl={username}&format=json"
    _STEAM_WONED_GAMES_URL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamKey}&steamid={steam64id}&format=json"
    _STEAM_KEY = "C0A26A72E4EC723F45C3EA9543B7B7F1"
    _STEAM_USER_INFOS_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamKey}&steamids={steam64ID}"
    
    def __init__(self, username):
        self.username = username
        self._getSteamID(username)
        self._getUserInfos()
        self.getGames()
        self.getName()
        self.getCountry()
        self.getProfileImage()

    #requests methods
    def _getSteamID(self, username):
        self._steam64ID = requests.get(self._STEAM_USER_URL.replace("{steamKey}", self._STEAM_KEY).replace("{username}", username)).json().get('response').get('steamid')

    def _getUserInfos(self):
        self._infos = requests.get(self._STEAM_USER_INFOS_URL.replace("{steamKey}", self._STEAM_KEY).replace("{steam64ID}", self._steam64ID)).json().get('response').get('players')[0]

    def getGames(self):
        self.games = requests.get(self._STEAM_WONED_GAMES_URL.replace('{steamKey}', self._STEAM_KEY).replace('{steam64id}', self._steam64ID)).json().get('response').get('games')
        
    def formatedGamesList(self):
        #'''
        games = {}
        for item in self.games:
            games[item.get('appid')] = SteamGame(item.get('appid')).gameName
        return games
        #'''

    #simple methods
    def getProfileImage(self):
        self.profileImage = self._infos.get('avatarfull')

    def getName(self):
        self.name = self._infos.get('realname')

    def getCountry(self):
        self.country = self._infos.get('loccountrycode')
    
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
        self.appID = appID
        self._getGameInfos()
        
    def _getGameInfos(self):
        self.gameInfos = requests.get(self._GAME_INFO_URL.replace('{steamKey}', self._STEAM_KEY).replace('{appid}', str(self.appID))).json().get('game')

    def getName(self):
        self.gameName = self.gameInfos.get('gameName')
        return self.gameName