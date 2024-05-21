from pydantic_settings import BaseSettings


class Config(BaseSettings):
    API_HOSTNAME: str
    API_PORT: int
    WS_HOSTNAME: str
    WS_PORT: int

CONFIG = Config()
