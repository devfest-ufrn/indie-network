import requests
import json
from indie_network.settings import BASE_DIR
from django.db import models


class SteamUser:
    _STEAM_USER_URL = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={steamKey}&vanityurl={username}&format=json"
    _STEAM_WONED_GAMES_URL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steamKey}&steamid={steam64id}&format=json"
    _STEAM_KEY = "C0A26A72E4EC723F45C3EA9543B7B7F1"
    _STEAM_USER_INFOS_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={steamKey}&steamids={steam64ID}"
    
    def __init__(self, steam64id):
        self._steam64ID = steam64id
        self._getUserInfos()
        self.getGames()

    #requests methods
    def _getUserInfos(self):
        self._infos = requests.get(self._STEAM_USER_INFOS_URL.replace("{steamKey}", self._STEAM_KEY).replace("{steam64ID}", self._steam64ID)).json().get('response').get('players')[0]

    def getGames(self):
        self.games = requests.get(self._STEAM_WONED_GAMES_URL.replace('{steamKey}', self._STEAM_KEY).replace('{steam64id}', self._steam64ID)).json().get('response').get('games')
        
    def formatedGamesList(self):
        #'''
        games = {}
        for item in self.games:
            print(item['appid'])
            games[item['appid']] = SteamGame(str(item['appid']))
        return games
        #'''

    #simple methods
    def asJson(self):
        self._infos['games'] = self.games
        return self._infos
        '''
        attributes = [item for item in dir(self) if not item.startswith('__') and not item.startswith('_') and not callable(getattr(self, item))]
        json = {}
        for item in attributes:
            json[item] = getattr(self, item)
        return json
        '''

class SteamGame:
    _STEAM_KEY = "C0A26A72E4EC723F45C3EA9543B7B7F1"
    
    def __init__(self, appID):
        self.appID = appID
        self._getGameInfos()
        self.name = self.gameInfos['app_name']

    def _getGameInfos(self):
        print(self.appID)
        with open(BASE_DIR + '\\util\\base.json') as data_file:    
            data = json.load(data_file)
        self.gameInfos = data[self.appID]