import sys

sys.path.append(R"F:\University\OOP\Сourse paper\BookingAplictaion\Back\models")

from typing import Annotated

from fastapi import APIRouter, Path, Query
from fastapi.exceptions import HTTPException

from Passenger import Passenger

router = APIRouter(
    prefix='/passenger',
    tags=['Passengers']
)

passenger_db = {}
id = 0


@router.post('/create/')
def add_passenger(passenger: Passenger):
    global id
    data = passenger.model_dump()
    data = {id: data}
    passenger_db.update(data)
    id += 1
    return data


@router.get('/{uuid}')
def get_passenger(uuid: Annotated[int, Path()]):
    return Passenger(**passenger_db[uuid])


@router.get('/')
def get_passenger_by_name(name: Annotated[str, Query()]):
    for passenger in passenger_db.values():
        if passenger['name'] == name:
            return Passenger(**passenger)
    raise HTTPException(detail="User with this name does not exist", status_code=404)
