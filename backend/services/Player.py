from services.Requester import Requester
from utils.global_variables import URL_PLAYER_DATA
#URL_PLAYER_DATA = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

class Player:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.strip()

    def get_ids(self):
        player_data = Requester()
        return player_data.get_content(URL_PLAYER_DATA + self.__name)


if __name__ == "__main__":
    Test = Player("Koshi o Duelista")
    print(Test.get_ids())