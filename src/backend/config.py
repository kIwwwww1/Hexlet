from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    db_url: str = 'sqlite:///database.db'

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

settings = Config()