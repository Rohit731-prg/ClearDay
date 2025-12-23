from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DB_URL: str = ""
    SERECT_KEY: str = ""
    CLOUDINARY_NAME: str = ""
    CLOUDINARY_KEY: str = ""
    CLOUDINARY_SECRET: str = ""

    class Config:
        env_file = ".env"

setting = Setting()