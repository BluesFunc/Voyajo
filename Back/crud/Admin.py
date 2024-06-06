# Добавьте этот код в конец вашего файла crud.py

from sqlalchemy.orm import Session
from database import models
from database.database import get_db
from schemas import admin as schemas



# Ticket CRUD operations
def get_ticket(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def get_tickets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ticket).offset(skip).limit(limit).all()

def create_ticket(db: Session, ticket: schemas.TicketCreate):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def update_ticket(db: Session, ticket_id: int, ticket: schemas.TicketUpdate):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket:
        for key, value in ticket.dict().items():
            setattr(db_ticket, key, value)
        db.commit()
        db.refresh(db_ticket)
    return db_ticket

def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket

# Trip CRUD operations
def get_trip(db: Session, trip_id: int):
    return db.query(models.Trip).filter(models.Trip.id == trip_id).first()

def get_trips(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trip).offset(skip).limit(limit).all()

def create_trip(db: Session, trip: schemas.TripCreate):
    db_trip = models.Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def update_trip(db: Session, trip_id: int, trip: schemas.TripUpdate):
    db_trip = db.query(models.Trip).filter(models.Trip.id == trip_id).first()
    if db_trip:
        for key, value in trip.dict().items():
            setattr(db_trip, key, value)
        db.commit()
        db.refresh(db_trip)
    return db_trip

def delete_trip(db: Session, trip_id: int):
    db_trip = db.query(models.Trip).filter(models.Trip.id == trip_id).first()
    if db_trip:
        db.delete(db_trip)
        db.commit()
    return db_trip

# Fare CRUD operations
def get_fare(db: Session, fare_id: int):
    return db.query(models.Fare).filter(models.Fare.id == fare_id).first()

def get_fares(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fare).offset(skip).limit(limit).all()

def create_fare(db: Session, fare: schemas.FareCreate):
    db_fare = models.Fare(**fare.model_dump())
    db.add(db_fare)
    db.commit()
    db.refresh(db_fare)
    return db_fare

def update_fare(db: Session, fare_id: int, fare: schemas.FareUpdate):
    db_fare = db.query(models.Fare).filter(models.Fare.id == fare_id).first()
    if db_fare:
        for key, value in fare.dict().items():
            setattr(db_fare, key, value)
        db.commit()
        db.refresh(db_fare)
    return db_fare

def delete_fare(db: Session, fare_id: int):
    db_fare = db.query(models.Fare).filter(models.Fare.id == fare_id).first()
    if db_fare:
        db.delete(db_fare)
        db.commit()
    return db_fare

# Passanger CRUD operations
def get_passanger(db: Session, passanger_id: int):
    return db.query(models.Passanger).filter(models.Passanger.id == passanger_id).first()

def get_passangers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Passanger).offset(skip).limit(limit).all()

def create_passanger(db: Session, passanger: schemas.PassangerCreate):
    db_passanger = models.Passanger(**passanger.dict())
    db.add(db_passanger)
    db.commit()
    db.refresh(db_passanger)
    return db_passanger

def update_passanger(db: Session, passanger_id: int, passanger: schemas.PassangerUpdate):
    db_passanger = db.query(models.Passanger).filter(models.Passanger.id == passanger_id).first()
    if db_passanger:
        for key, value in passanger.dict().items():
            setattr(db_passanger, key, value)
        db.commit()
        db.refresh(db_passanger)
    return db_passanger

def delete_passanger(db: Session, passanger_id: int):
    db_passanger = db.query(models.Passanger).filter(models.Passanger.id == passanger_id).first()
    if db_passanger:
        db.delete(db_passanger)
        db.commit()
    return db_passanger

# Order CRUD operations
def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        for key, value in order.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_country = models.Country(name=country.name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country

def update_country(db: Session, country_id: int, country: schemas.CountryUpdate):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country:
        db_country.name = country.name
        db.commit()
        db.refresh(db_country)
    return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country:
        db.delete(db_country)
        db.commit()
    return db_country

# Region CRUD operations
def get_region(db: Session, region_id: int):
    return db.query(models.Region).filter(models.Region.id == region_id).first()

def get_regions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Region).offset(skip).limit(limit).all()

def create_region(db: Session, region: schemas.RegionCreate):
    db_region = models.Region(name=region.name, country_id=region.country_id)
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region

def update_region(db: Session, region_id: int, region: schemas.RegionUpdate):
    db_region = db.query(models.Region).filter(models.Region.id == region_id).first()
    if db_region:
        db_region.name = region.name
        db_region.country_id = region.country_id
        db.commit()
        db.refresh(db_region)
    return db_region

def delete_region(db: Session, region_id: int):
    db_region = db.query(models.Region).filter(models.Region.id == region_id).first()
    if db_region:
        db.delete(db_region)
        db.commit()
    return db_region

# City CRUD operations
def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(name=city.name, region_id=city.region_id)
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def update_city(db: Session, city_id: int, city: schemas.CityUpdate):
    db_city = db.query(models.City).filter(models.City.id == city_id).first()
    if db_city:
        db_city.name = city.name
        db_city.region_id = city.region_id
        db.commit()
        db.refresh(db_city)
    return db_city

def delete_city(db: Session, city_id: int):
    db_city = db.query(models.City).filter(models.City.id == city_id).first()
    if db_city:
        db.delete(db_city)
        db.commit()
    return db_city

# Station CRUD operations
def get_station(db: Session, station_id: int):
    return db.query(models.Station).filter(models.Station.id == station_id).first()

def get_stations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Station).offset(skip).limit(limit).all()

def create_station(db: Session, station: schemas.StationCreate):
    db_station = models.Station(name=station.name, station_type=station.station_type.name, city_id=station.city_id)
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

def update_station(db: Session, station_id: int, station: schemas.StationUpdate):
    db_station = db.query(models.Station).filter(models.Station.id == station_id).first()
    if db_station:
        db_station.name = station.name
        db_station.station_type = station.station_type
        db_station.city_id = station.city_id
        db.commit()
        db.refresh(db_station)
    return db_station

def delete_station(db: Session, station_id: int):
    db_station = db.query(models.Station).filter(models.Station.id == station_id).first()
    if db_station:
        db.delete(db_station)
        db.commit()
    return db_station
