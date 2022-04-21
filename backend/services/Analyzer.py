from utils.global_variables import (URL_ACTIVE_GAME, URL_MATCH_DATA,
                                    URL_MATCHHISTORY_IDS)
from utils.time_handler import time_since_given_timestamp

from services.player import Player
from services.requester import Requester


class Analyzer:
    def __init__(self, nickname):
        self.player = Player(nickname).get_ids()
        self.requester = Requester()

    def get_active_game_status(self):
        active_game = self.requester.get_content(URL_ACTIVE_GAME + self.player['id'])
        if isinstance(active_game, dict):
            gameLength = active_game['gameLength']
            return round(gameLength/60)
        return False

    def get_matchhistory_games_id(self):
        return self.requester.get_content(URL_MATCHHISTORY_IDS + self.player['puuid'] + "/ids?count=1")

    def get_time_since_last_game(self):
        last_game = self.requester.get_content(URL_MATCH_DATA + self.get_matchhistory_games_id()[0])
        game_info = last_game['info']
        # Divided by 1000 because that timestamp is given by Riot API in milisseconds
        return time_since_given_timestamp(game_info['gameStartTimestamp']/1000 + game_info['gameDuration'])
