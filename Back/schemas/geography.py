from typing import List
from enum import Enum

from pydantic import BaseModel


class StationType(Enum):
    BUS = "Bus"
    TRAIN = "Train"
    AIRPORT = "Airport"


# Country schemas
class CountryBase(BaseModel):
    name: str


class Country(CountryBase):
    id: int

    class Config:
        orm_mode: True

# Region schemas
class RegionBase(BaseModel):
    name: str
    countr_name: str

class Region(RegionBase):
    id: int

    class Config:
        orm_mode: True

# City schemas
class CityBase(BaseModel):
    name: str
    region_name: str


class City(CityBase):
    id: int

    class Config:
        orm_mode: True


class StationBase(BaseModel):
    name: str
    station_type: StationType
    city_name: str



class Station(StationBase):
    id: int

    class Config:
        orm_mode: True

