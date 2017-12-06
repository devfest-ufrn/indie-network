import requests
import json
from bs4 import BeautifulSoup
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
            games[item['appid']] = SteamGame(str(item['appid'])).infos
        return games
        #'''

    #simple methods
    def asJson(self):
        self._infos['games'] = self.games
        return self._infos

class SteamGame:
    def __init__(self, appID):
        self.appID = appID
        self._getGameInfos()

    def _getGameInfos(self): 
        self.infos = SteamAppCrawler(self.appID).details

class SteamAppCrawler:
    BASE_URL = "http://store.steampowered.com/app/"

    def __init__(self, appid):
        self.appid = appid
        self.details = {}
        self._getInfos()

    def _getInfos(self):
        r = requests.get(self.BASE_URL + str(self.appid))
        s = BeautifulSoup(r.text, 'html.parser')
        self.getTags(s)
        self.getDetails(s)

    def getTags(self, soup):
        self._tags = []
        for item in soup.find_all(class_= 'game_area_details_specs'):
            self._tags.append(item.get_text())
        self.details['Tags'] = self._tags

    def getDetails(self, soup):
        try:
            item = soup.find_all(class_= 'details_block')[0]
            item = item.get_text().split('\n')

            for line in item:
                for prop in [ 'Title', 'Genre', 'Release Date' ]:
                    if prop in line:
                        self.details[prop] = line.replace(prop, '').replace(':', '').strip()
        except TypeError as te:
            self.details['Title'] = 'Null'
            self.details['Genre'] = 'Null'
            self.details['Release Date'] = 'Null'
        except IndexError as ie:
            self.details['Title'] = 'Null'
            self.details['Genre'] = 'Null'
            self.details['Release Date'] = 'Null'

class Games(models.Model):
    name = models.CharField("Nome",max_length=30)
    genre = models.CharField("Gênero",max_length=30)
    photo = models.ImageField(upload_to = 'pics/', default = 'pics/jogos.jpg')

    def __str__(self):
        return self.name + " - " + self.genre