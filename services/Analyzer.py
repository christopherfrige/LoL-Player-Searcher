import time
from utils.GlobalVariables import URL_ACTIVE_GAME, URL_MATCHHISTORY_IDS, URL_MATCH_DATA
from services.Player import Player
from services.Requester import Requester
from utils.TimeHandler import time_since_given_timestamp

class Analyzer:
    def __init__(self, nickname):
        self.player = Player(nickname)
        self.requester = Requester()

    def get_active_game_status(self):
        active_game = self.requester.get_content(URL_ACTIVE_GAME + self.player['encryptedid'])

        if active_game.status_code == 200:
            gameLength = active_game.json()['gameLength']
            return round(gameLength/60)
        return False

    def get_matchhistory_games_id(self):
        return self.requester.get(URL_MATCHHISTORY_IDS + self.player['puuid'] + "/ids")

    def get_time_since_last_game(self):
        last_game = self.requester.get(URL_MATCH_DATA + self.player['puuid'])
        game_info = last_game['info']
        # Divided by 1000 because that timestamp is given by Riot API in milisseconds
        return time_since_given_timestamp(game_info['gameStartTimestamp']/1000 + game_info['gameDuration'])
