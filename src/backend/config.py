from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_url: str = 'postgresql+asyncpg://user:password@db:5432/hexlet'
    SECRET_KEY: str
    ALGORITHM: str = 'HS256'

    model_config = SettingsConfigDict(
        env_file='src/backend/.env',
        env_file_encoding='utf-8',
    )


settings = Config()
