from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from crud import Distributing as crud
from schemas import distributing as schemas
from database.database import get_db


router = APIRouter(
    prefix='/distributing',
    tags=['Customer']
)

@router.get("/extranet/{owner_id}/company")
def read_all_extranet_companies(owner_id: int, db = Depends(get_db)) -> List[schemas.Company]:
    return crud.get_companies(db, owner_id)

@router.post("/extranet/{owner_id}/company", response_model=schemas.Company)
def create_new_company(owner_id: int, company: schemas.CompanyBase, db = Depends(get_db)):
    return crud.create_company(db, company, owner_id)
 
 
@router.get("/extranet/{owner_id}/company/{company_id}")
def get_company_details(company_id: int, db: Session = Depends(get_db)):
    company = crud.get_company(db, company_id=company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
   
    

@router.get("/trips", response_model=List[schemas.TripInfo])
def customer_seacrh_trips (date: Annotated[str, Query()], departure: Annotated[str, Query()], 
                          arrival: Annotated[str, Query()],  db = Depends(get_db)
                          ):
    return  crud.search_trips(db, schemas.TripInfoRequest(date=date,departure=departure, arrival=arrival))

