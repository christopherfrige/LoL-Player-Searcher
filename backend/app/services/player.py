from app.utils.global_variables import URL_PLAYER_DATA

from app.services.requester import Requester

class Player:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name.strip()

    def get_ids(self):
        player_data = Requester()
        return player_data.get_content(URL_PLAYER_DATA + self._name)

