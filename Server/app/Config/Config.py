from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_URL: str = ""
    SERECT_KEY: str = ""

    class Config:
        env_file = ".env"

setting = Setting()