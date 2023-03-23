from aiohttp import ClientSession
from src.services import LeagueAPI
from src.schemas.summoner import SummonerData, SummonerDataError
from src.summoner.constants import MAX_SUMMONER_NAME_CHARACTERS

class Summoner:
    def __init__(self, region: str, aiohttp: ClientSession) -> None:
        self.region = region
        self.aiohttp = aiohttp
        self.league_api = LeagueAPI(self.region, aiohttp=self.aiohttp)

    async def get_status(self, summoner: SummonerData) -> SummonerData | SummonerDataError:
        valid_name, error = await self.validate_summoner_name(summoner)
        if not valid_name:
            return error

        summoner_data = await self.league_api.get_summoner(summoner.name)
        if not summoner_data:
            return SummonerDataError(
                name=summoner.name,
                code="SummonerNameNotFound",
                message="Não foi possível encontrar um jogador com esse nome."
            )
        summoner.name = summoner_data.name

        in_match_data = await self.league_api.get_active_match(summoner_data.id)
        if in_match_data:
            summoner.in_match = True
            return summoner

        summoner_matches = await self.league_api.get_summoner_matches(summoner_data.puuid)
        if not summoner_matches:
            return SummonerDataError(
                name=summoner.name,
                code="SummonerHasNoMatches",
                message="Não foi possível encontrar partidas no histórico desse jogador."
            )
            
        match_data = await self.league_api.get_finished_match(summoner_matches.__root__[0])
        match_start = match_data.info.gameStartTimestamp
        match_duration = match_data.info.gameDuration
        match_end_timestamp = match_start + match_duration / 1000 # All in milliseconds

        summoner.last_match_end_timestamp = match_end_timestamp
        summoner.in_match = False
        return summoner
    
    async def validate_summoner_name(self, summoner: SummonerData) -> tuple[bool, None] | tuple[bool, SummonerDataError]:
        if len(summoner.name.strip()) > MAX_SUMMONER_NAME_CHARACTERS:
            return False, SummonerDataError(
                name=summoner.name,
                code="SummonerNameMaxLengthExceeded",
                message="O nome de invocador ultrapassou o limite de 16 caracteres."
            )
        return True, None
