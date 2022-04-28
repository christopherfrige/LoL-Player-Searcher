import json

import requests
from app.utils.enviroment_variables import RIOT_API_KEY


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
