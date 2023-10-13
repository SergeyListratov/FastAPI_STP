from datetime import date

from app.database import async_session_maker
from app.bookings.models import Bookings
from sqlalchemy import select, and_, or_, func
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
            ):
        '''
        WITH booked_rooms as (
        select * from bookings
            where room_id = 1 and
            (date_from >= '2023-05-15' and date_from <= '2023-06-20') or
            (date_from <= '2023-05-15' and date_to > '2023-05-15')
            )
        SELECT rooms.quantity - count(booked_rooms.room_id) FROM rooms

        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        where rooms.id = 1
        Group BY rooms.quantity, booked_rooms.room_id
        '''
        booked_rooms = select(Bookings).where(
            and_(
                Bookings.room_id == 1,
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    ),
                )
            )
        ).cte('booked_rooms')

        # '''
        # SELECT rooms.quantity - count(booked_rooms.room_id) FROM rooms
        #
        # LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        # where rooms.id = 1
        # Group BY rooms.quantity, booked_rooms.room_id
        # '''

        rooms_left = select(
            (Rooms.quantity - func.count(booked_rooms.c.room_id)).label('rooms_left')
            ).select_from(Rooms).join(
                booked_rooms, booked_rooms.c.room_id == Rooms.id
            ).where(Rooms.id == 1).group_by(
                Rooms.quantity, booked_rooms.c.rooms.c.room_id
            )
        print(rooms_left)
