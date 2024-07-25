from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    API_HOSTNAME: str = Field(alias="API_HOSTNAME")
    API_PORT: int = Field(alias="API_PORT")
    CERT_DIR: str = Field(alias="CERT_DIR")

CONFIG = Config()
