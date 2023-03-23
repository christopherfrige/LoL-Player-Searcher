from pydantic import BaseSettings

class Settings(BaseSettings):
    riot_api_key: str = None

    class Config:
        env_file = ".env"

settings = Settings()
