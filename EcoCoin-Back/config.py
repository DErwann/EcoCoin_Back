from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "EcoCoin"
    title: str = "EcoCoin"
    database_url: str = "postgresql://postgres:1234@localhost:5432/EcoCoin_db"


@lru_cache()
def get_settings():
    return Settings()

