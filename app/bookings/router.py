from fastapi import APIRouter, Request

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get("")
async def get_bookings(request: Request): #-> list[SBooking]:
    print(request.cookies)
    print(request.url)
    print(request.client)
    return request.cookies
    # return await BookingDAO.find_all()


# @router.get("")
# async def get_bookings():
#     async with async_session_maker() as session:
#         query = select(Bookings.__table__.columns)
#         result = await session.execute(query)
#         return result.mappings().all()


# async def get_bookings_example(mode: str):
#     async with async_session_maker() as session:
#         if mode == 'mappings':
#             query = select(Bookings.__table__.columns).limit(3)
#         else:
#             query = select(Bookings).limit(3)
#         result = await session.execute(query)
#         if mode == 'all':
#             return result.all()
#         if mode == 'scalars':
#             return result.scalars().all()
#         if mode == 'mappings':
#             return result.mappings().all()
