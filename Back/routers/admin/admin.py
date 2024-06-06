from typing import List

from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session


from database.database import get_db
from crud import Admin as crud
from crud import User as user_crud
from schemas.auth import User, RegUser
from schemas import admin as schemas


router = APIRouter(
    prefix='/admin',
    tags=['admin-CRUD']
)



@router.post('/customers', response_model=User)
def create_new_customer(user:RegUser,db = Depends(get_db)):
    return user_crud.create_customer(db, user)

@router.post('/extranets', response_model=User)
def create_new_extranet(user:RegUser,db = Depends(get_db)):
    return user_crud.create_extranet(db, user)

@router.post('/admins', response_model=User)
def create_new_admin(user:RegUser,db = Depends(get_db)):
    return user_crud.create_admin(db, user)

@router.get("/user")
def user_list(db = Depends(get_db)) -> list[User]:
    users = user_crud.get_all_user(db)

    return users



@router.post("/countries/", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)


@router.get("/countries/", response_model=List[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_countries(db, skip=skip, limit=limit)


@router.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


@router.put("/countries/{country_id}", response_model=schemas.Country)
def update_country(country_id: int, country: schemas.CountryUpdate, db: Session = Depends(get_db)):
    return crud.update_country(db, country_id=country_id, country=country)


@router.delete("/countries/{country_id}", response_model=schemas.Country)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    return crud.delete_country(db, country_id=country_id)


@router.post("/regions/", response_model=schemas.Region)
def create_region(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    return crud.create_region(db=db, region=region)

@router.get("/regions/", response_model=List[schemas.Region])
def read_regions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_regions(db, skip=skip, limit=limit)

@router.get("/regions/{region_id}", response_model=schemas.Region)
def read_region(region_id: int, db: Session = Depends(get_db)):
    db_region = crud.get_region(db, region_id=region_id)
    if db_region is None:
        raise HTTPException(status_code=404, detail="Region not found")
    return db_region

@router.put("/regions/{region_id}", response_model=schemas.Region)
def update_region(region_id: int, region: schemas.RegionUpdate, db: Session = Depends(get_db)):
    return crud.update_region(db, region_id=region_id, region=region)

@router.delete("/regions/{region_id}", response_model=schemas.Region)
def delete_region(region_id: int, db: Session = Depends(get_db)):
    return crud.delete_region(db, region_id=region_id)


@router.post("/cities/", response_model=schemas.City)
def create_city(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db=db, city=city)

@router.get("/cities/", response_model=List[schemas.City])
def read_cities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cities(db, skip=skip, limit=limit)

@router.get("/cities/{city_id}", response_model=schemas.City)
def read_city(city_id: int, db: Session = Depends(get_db)):
    db_city = schemas.get_city(db, city_id=city_id)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.put("/cities/{city_id}", response_model=schemas.City)
def update_city(city_id: int, city: schemas.CityUpdate, db: Session = Depends(get_db)):
    return crud.update_city(db, city_id=city_id, city=city)

@router.delete("/cities/{city_id}", response_model=schemas.City)
def delete_city(city_id: int, db: Session = Depends(get_db)):
    return crud.delete_city(db, city_id=city_id)




@router.post("/stations/", response_model=schemas.Station)
def create_station(station: schemas.StationCreate, db: Session = Depends(get_db)):
    return crud.create_station(db=db, station=station)

@router.get("/stations/", response_model=List[schemas.Station])
def read_stations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_stations(db, skip=skip, limit=limit)

@router.get("/stations/{station_id}", response_model=schemas.Station)
def read_station(station_id: int, db: Session = Depends(get_db)):
    db_station = crud.get_station(db, station_id=station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Station not found")
    return db_station

@router.put("/stations/{station_id}", response_model=schemas.Station)
def update_station(station_id: int, station: schemas.StationUpdate, db: Session = Depends(get_db)):
    return crud.update_station(db, station_id=station_id, station=station)

@router.delete("/stations/{station_id}", response_model=schemas.Station)
def delete_station(station_id: int, db: Session = Depends(get_db)):
    return crud.delete_station(db, station_id=station_id)




@router.post("/tickets/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db=db, ticket=ticket)

@router.get("/tickets/", response_model=List[schemas.Ticket])
def read_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, skip=skip, limit=limit)

@router.get("/tickets/{ticket_id}", response_model=schemas.Ticket)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    db_ticket = crud.get_ticket(db, ticket_id=ticket_id)
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.put("/tickets/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: int, ticket: schemas.TicketUpdate, db: Session = Depends(get_db)):
    return crud.update_ticket(db, ticket_id=ticket_id, ticket=ticket)

@router.delete("/tickets/{ticket_id}", response_model=schemas.Ticket)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    return crud.delete_ticket(db, ticket_id=ticket_id)



@router.post("/trips/", response_model=schemas.Trip)
def create_trip(trip: schemas.TripCreate, db: Session = Depends(get_db)):
    return crud.create_trip(db=db, trip=trip)

@router.get("/trips/", response_model=List[schemas.Trip])
def read_trips(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_trips(db, skip=skip, limit=limit)

    
@router.get("/trips/{trip_id}", response_model=schemas.Trip)
def read_trip(trip_id: int, db: Session = Depends(get_db)):
    db_trip = crud.get_trip(db, trip_id=trip_id)
    if db_trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return db_trip

@router.put("/trips/{trip_id}", response_model=schemas.Trip)
def update_trip(trip_id: int, trip: schemas.TripUpdate, db: Session = Depends(get_db)):
    return crud.update_trip(db, trip_id=trip_id, trip=trip)

@router.delete("/trips/{trip_id}", response_model=schemas.Trip)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    return crud.delete_trip(db, trip_id=trip_id)



@router.post("/fares/", response_model=schemas.Fare)
def create_fare(fare: schemas.FareCreate, db: Session = Depends(get_db)):
    return crud.create_fare(db=db, fare=fare)

@router.get("/fares/", response_model=List[schemas.Fare])
def read_fares(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_fares(db, skip=skip, limit=limit)

@router.get("/fares/{fare_id}", response_model=schemas.Fare)
def read_fare(fare_id: int, db: Session = Depends(get_db)):
    db_fare = crud.get_fare(db, fare_id=fare_id)
    if db_fare is None:
        raise HTTPException(status_code=404, detail="Fare not found")
    return db_fare

@router.put("/fares/{fare_id}", response_model=schemas.Fare)
def update_fare(fare_id: int, fare: schemas.FareUpdate, db: Session = Depends(get_db)):
    return crud.update_fare(db, fare_id=fare_id, fare=fare)

@router.delete("/fares/{fare_id}", response_model=schemas.Fare)
def delete_fare(fare_id: int, db: Session = Depends(get_db)):
    return crud.delete_fare(db, fare_id=fare_id)



@router.post("/passengers/", response_model=schemas.Passanger)
def create_passenger(passenger: schemas.PassangerCreate, db: Session = Depends(get_db)):
    return crud.create_passenger(db=db, passenger=passenger)

@router.get("/passengers/", response_model=List[schemas.Passanger])
def read_passengers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_passengers(db, skip=skip, limit=limit)

@router.get("/passengers/{passenger_id}", response_model=schemas.Passanger)
def read_passenger(passenger_id: int, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger(db, passenger_id=passenger_id)
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return db_passenger

@router.put("/passengers/{passenger_id}", response_model=schemas.Passanger)
def update_passenger(passenger_id: int, passenger: schemas.PassangerUpdate, db: Session = Depends(get_db)):
    return crud.update_passenger(db, passenger_id=passenger_id, passenger=passenger)

@router.delete("/passengers/{passenger_id}", response_model=schemas.Passanger)
def delete_passenger(passenger_id: int, db: Session = Depends(get_db)):
    return crud.delete_passenger(db, passenger_id=passenger_id)



@router.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@router.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

@router.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return crud.update_order(db, order_id=order_id, order=order)

@router.delete("/orders/{order_id}", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return crud.delete_order(db, order_id=order_id)
