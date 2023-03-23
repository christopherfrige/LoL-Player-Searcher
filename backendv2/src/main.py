from fastapi import FastAPI
from src.summoner.router import router as summoner_router

app = FastAPI()

app.include_router(summoner_router)
