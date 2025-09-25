from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://username:password@localhost:5432/kalamkari_db"

    class Config:
        env_file = ".env"

settings = Settings()