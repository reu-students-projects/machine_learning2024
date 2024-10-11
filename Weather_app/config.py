from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    OPEN_API_KEY: str = Field(env='OPEN_API_KEY')
    WEATHER_API_KEY: str = Field(env='WEATHER_API_KEY')

    class Config:
        env_file = './.env'


config = Settings()
