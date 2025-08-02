from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSecret(BaseSettings):
    DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")


class SecretKey(BaseSettings):
    SECRET: str
    
    model_config = SettingsConfigDict(env_prefix='HMAC_')
