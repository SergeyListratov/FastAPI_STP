from fastapi import APIRouter, HTTPException, status, Response

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.shemas import SUserAuth
from app.users.dao import UsersDAO


router = APIRouter(
    prefix='/auth',
    tags=['Auth & Users']
)


@router.post('/register')
async def register_user(user_date: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_date.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    hashed_password = get_password_hash(user_date.password)
    await UsersDAO.add(email=user_date.email, hashed_password=hashed_password)


@router.post('/login')
async def login_user(response: Response, user_date: SUserAuth):
    user = await authenticate_user(user_date.email, user_date.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({'sub': user.id})
    response.set_cookie('booking_access_token', access_token, httponly=True)
    return {'access_token': access_token}




