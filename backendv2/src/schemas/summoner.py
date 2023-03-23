from typing import List, Optional
from src.schemas.league import RegionEnum

from pydantic import BaseModel

class SummonerDataError(BaseModel):
    name: str
    code: str
    message: str


class SummonerData(BaseModel):
    name: str
    last_match_end_timestamp: Optional[int]
    in_match: Optional[bool]


class SummonersRequest(BaseModel):
    region: RegionEnum
    summoners: List[SummonerData]


class SummonersResponse(BaseModel):
    summoners: List[SummonerDataError | SummonerData]


class Summoner(BaseModel):
    accountId: str
    profileIconId: int
    revisionDate: int
    name: str
    id: str
    puuid: str
    summonerLevel: int