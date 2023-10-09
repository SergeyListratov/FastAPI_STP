from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(date: dict) -> str:
    to_encode = date.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, 'q2345234sdfgsadgf0', 'HS256'
    )
    return encoded_jwt


hashed_password = '$2b$12$X9BbR9SdB7vP3z2mJBwbC.I/ViWTN0EVGeDdJqW7inU4oJW61xUgq'
plain_password = 'programmer'
plain_password1 = 'programmer1'


print(get_password_hash(plain_password))
print(verify_password(plain_password1, hashed_password))
print(create_access_token({'user': "Artem"}))


