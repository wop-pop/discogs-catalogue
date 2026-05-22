from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    discogs_user_token: str

    class Config:
        env_file = ".env"


settings = Settings()