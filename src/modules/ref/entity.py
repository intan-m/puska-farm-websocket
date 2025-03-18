from typing import Tuple

from pydantic import BaseModel, Field


# Entity
class Location(BaseModel):
    nama_unit: str = Field(validation_alias="nama unit")
    longitude: float
    latitude: float
    lokasi: str
    populasi: float
    point: Tuple[float, float]