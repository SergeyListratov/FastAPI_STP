from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_booking
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_users)
app.include_router(router_booking)


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None

    ):
        self.has_spa = has_spa
        self.stars = stars
        self.date_to = date_to
        self.location = location
        self.date_from = date_from


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get('/hotels')
def get_hotels(
        search_args: HotelsSearchArgs = Depends()
):
    hotels = [
        {
            'address': 'ул. Кедровая, д. 5',
            'name': 'Super',
            'stars': 5
        },
        {
            'address': 'ул. Кедровая, д. 5',
            'name': 'Super',
            'stars': 5
        }
    ]
    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/booking')
def add_booking(booking: SBooking):
    pass
