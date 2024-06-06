# Добавьте этот код в конец вашего файла crud.py

from sqlalchemy.orm import Session
from datetime import datetime
from database import models
from database.database import get_db
from schemas import distributing

def get_companies(db: Session, owner_id: int):
    return db.query(models.Extranet).filter(models.Extranet.id == owner_id).first().companies



def create_company(db: Session, company: distributing.CompanyBase, owner_id: int):
    company.company_type = company.company_type.name
    content = company.model_dump()
    content.update({"extranet_id": owner_id})
    new_company = models.Company(**content)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

def search_trips(db: Session, trip_info: distributing.TripInfoRequest ):
    
    
    return db.query(models.Trip).select_from(models.Fare).filter(
        models.Fare.departure_station.has(name=trip_info.departure),
        models.Fare.arrival_station.has(name=trip_info.arrival),
        models.Trip.departure_date == datetime.strptime(trip_info.date, "%d.%M.%Y")
    ).all()