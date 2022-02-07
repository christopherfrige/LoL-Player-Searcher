import requests
import json
from utils.enviroment_variables import RIOT_API_KEY

class Requester:
    def __init__(self):
        self.header = RIOT_API_KEY

    def get_content(self, url):
        response = requests.get(
            url=url,
            headers=self.header
        )

        if response.status_code == 200:
            return json.loads(response.content)
        
        return response

if __name__ == "__main__":
    pegar_data = Requester()
    print(pegar_data.get_content("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Koshi o Duelista"))
