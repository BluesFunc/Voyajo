from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum

# Enums
class StationType(str, Enum):
    BUS = "Bus"
    TRAIN = "Train"
    AIRPORT = "Airport"

class CompanyType(str, Enum):
    AIRLINE = "Airline"
    RAILWAY = "Railway"
    BUS = "Bus"

class Station(BaseModel):
    id: int
    name: str
    
    class Config: 
        from_attributes = True

class TripInfo(BaseModel):
    id: int
    date: datetime
    departure: Station
    arrival: Station
    
    class Config: 
        from_attributes = True

class TripInfoRequest(BaseModel):
    date: str
    departure: str
    arrival: str


class CompanyBase(BaseModel):
    name: str
    company_link: str
    company_type: CompanyType


class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True