from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GOOGLE_APPLICATION_CREDENTIALS: str
    # GAMEXON RECOMMENDATION
    GAMEXONREC_URL: str
    GAMEXONREC_USERNAME: str
    GAMEXONREC_PASSWORD: str

    # PARMEAMAN URL
    PARMEAMAN_URL: str
    PARMEAMAN_USERNAME: str
    PARMEAMAN_PASSWORD: str

    MIDTRANS_SERVER_KEY: str

    DATABASE_USER : str
    DATABASE_PASSWORD : str
    DATABASE_HOST : str
    DATABASE_PORT : str
    DATABASE_NAME : str
    DATABASE_SSLMODE : str
    class Config:
        env_file = ".env"

settings = Settings()