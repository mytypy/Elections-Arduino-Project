from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseSecret(BaseSettings):
    DATABASE: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: int
    
    model_config = SettingsConfigDict(env_prefix="MYSQL_")


class SecretKey(BaseSettings):
    SECRET: str
    
    model_config = SettingsConfigDict(env_prefix='HMAC_')