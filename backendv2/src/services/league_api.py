from src.config import settings
from src.schemas.summoner import Summoner
from src.schemas.match import InMatch, InHistoryMatch, SummonerMatches
from src.utils import get_continent_by_region
from aiohttp import ClientSession

class LeagueAPI:
    def __init__(self, region: str, aiohttp: ClientSession) -> None:
        self.aiohttp = aiohttp
        self.base_url = f"https://{region}.api.riotgames.com"
        self.base_url_continent = f"https://{get_continent_by_region(region)}.api.riotgames.com"
        self.headers = {
            "X-Riot-Token": settings.riot_api_key
        }

    async def get_summoner(self, summoner_name: str) -> Summoner:
        url = f"{self.base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
        async with self.aiohttp.get(
            url=url,
            headers=self.headers
        ) as get:
            response = await get.json()
            if get.status == 200:
                return Summoner(**response)
            print("get_summoner", response)
            return {}
        
    async def get_active_match(self, summoner_id: str) -> InMatch:
        url = f"{self.base_url}/lol/spectator/v4/active-games/by-summoner/{summoner_id}"
        async with self.aiohttp.get(
            url=url,
            headers=self.headers
        ) as get:
            response = await get.json()
            if get.status == 200:
                return InMatch(**response)
            print("get_active_match", response)
            return {}
        
    async def get_summoner_matches(self, summoner_puu_id: str) -> SummonerMatches:
        url = f"{self.base_url_continent}/lol/match/v5/matches/by-puuid/{summoner_puu_id}/ids"
        async with self.aiohttp.get(
            url=url,
            headers=self.headers
        ) as get:
            response = await get.json()
            if get.status == 200:
                if response:
                    return SummonerMatches(__root__=response)
            print("get_summoner_matches", response)
            return []
        
    async def get_finished_match(self, match_id: str) -> InHistoryMatch:
        url = f"{self.base_url_continent}/lol/match/v5/matches/{match_id}"
        async with self.aiohttp.get(
            url=url,
            headers=self.headers
        ) as get:
            response = await get.json()
            if get.status == 200:
                return InHistoryMatch(**response)
            print("get_finished_match", response)
            return {}