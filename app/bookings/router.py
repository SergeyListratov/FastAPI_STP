from fastapi import APIRouter, Request, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): #-> list[SBooking]:
    # print(user, type(user), user.email)
    # return await BookingDAO.find_all(user_id=user.id)
    return await BookingDAO.find_all(user_id=1)


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
