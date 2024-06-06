from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from decimal import Decimal
from enum import Enum

# Enums
class StationType(str, Enum):
    BUS = "Bus"
    TRAIN = "Train"
    AIRPORT = "Airport"

class CustomerGender(str, Enum):
    male = "Мужчина"
    female = "Женщина"
    other = "Other"

class CompanyType(str, Enum):
    AIRLINE = "Airline"
    RAILWAY = "Railway"
    BUS = "Bus"

# Ticket schemas
class TicketBase(BaseModel):
    fare_id: int
    company_id: int

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode: True

# Trip schemas
class TripBase(BaseModel):
    ticket_id: int
    company_id: int
    ticket_count: int

class TripCreate(TripBase):
    pass

class TripUpdate(TripBase):
    pass

class Trip(TripBase):
    id: int

    class Config:
        orm_mode: True

# Fare schemas
class FareBase(BaseModel):
    price: Decimal
    description: Optional[str] = None
    company_id: int
    departure_station_id: int
    arrival_station_id: int

class FareCreate(FareBase):
    pass

class FareUpdate(FareBase):
    pass

class Fare(FareBase):
    id: int

    class Config:
        orm_mode: True

# Passanger schemas
class PassangerBase(BaseModel):
    firstname: str
    second_name: str
    gender: CustomerGender
    passport_series: str
    birthday: date
    customer_id: int

class PassangerCreate(PassangerBase):
    pass

class PassangerUpdate(PassangerBase):
    pass

class Passanger(PassangerBase):
    id: int

    class Config:
        orm_mode: True

# Order schemas
class OrderBase(BaseModel):
    customer_id: int
    ticket_count: int
    trip_id: int
    
class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode: True




# Country schemas
class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    pass

class CountryUpdate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    class Config:
        orm_mode: True

# Region schemas
class RegionBase(BaseModel):
    name: str
    country_id: int

class RegionCreate(RegionBase):
    pass

class RegionUpdate(RegionBase):
    pass

class Region(RegionBase):
    id: int

    class Config:
        orm_mode: True

# City schemas
class CityBase(BaseModel):
    name: str
    region_id: int

class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode: True

# Station schemas
class StationBase(BaseModel):
    name: str
    station_type: StationType
    city_id: int

class StationCreate(StationBase):
    pass

class StationUpdate(StationBase):
    pass

class Station(StationBase):
    id: int

    class Config:
        orm_mode: True
