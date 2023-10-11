from fastapi import HTTPException, status


class BookingException(HTTPException):  # <-- наследуемся от HTTPException, который наследован от Exception
    status_code = 500  # <-- задаем значения по умолчанию
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


# UserAlreadyExistException = HTTPException(
#     status_code=status.HTTP_409_CONFLICT,
#     detail='Пользователь уже существует'
# )

class IncorrectEmailOrPassword(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"


# IncorrectEmailOrPassword = HTTPException(
#     status_code=status.HTTP_401_UNAUTHORIZED,
#     detail='Неверная почта или пароль'
# )

class TokenExpireException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен истек'


class TokenAbsentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутствует'


class IncorrectTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен имеет неверный формат'


class UserIsNotPresent(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверные данные о пользователе в токене'
