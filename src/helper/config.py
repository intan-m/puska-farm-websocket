from pydantic_settings import BaseSettings


class Config(BaseSettings):
    WS_HOSTNAME: str
    WS_PORT: int

CONFIG = Config()
