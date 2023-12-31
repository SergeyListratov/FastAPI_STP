from fastapi import HTTPException, Request, Depends, status
from jose import jwt, JWTError, ExpiredSignatureError

from app.config import settings
from app.exeptions import TokenExpireException, TokenAbsentException, IncorrectTokenException, UserIsNotPresent
from app.users.dao import UsersDAO
from app.users.models import Users


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALG
        )
    except ExpiredSignatureError:
        raise TokenExpireException
    except JWTError:
        raise IncorrectTokenException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresent
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != 'admin':
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return current_user
