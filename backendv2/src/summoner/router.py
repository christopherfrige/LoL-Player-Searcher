from fastapi import APIRouter, Depends
from src.schemas.summoner import SummonersRequest, SummonersResponse
from src.dependencies import aiohttp_session
from src.summoner import Summoner
import asyncio

router = APIRouter(
    prefix="/summoner"
)

@router.post("")# response_model=SummonersResponse
async def retrieve_summoners(
    summoners: SummonersRequest, 
    aiohttp=Depends(aiohttp_session)
) -> SummonersResponse:

    summoner = Summoner(summoners.region, aiohttp=aiohttp)
    tasks = []
    for player in summoners.summoners:
        task = asyncio.create_task(summoner.get_status(player))
        tasks.append(task)
        
    response = await asyncio.gather(*tasks, return_exceptions=False)

    return SummonersResponse(summoners=response)