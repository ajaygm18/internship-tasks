from passlib.context import CryptContext
import jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

SECRET_KEY = "78y4cx3nic47y8xmn2"

def hash_password(password: str) -> str:
    hashed = pwd_context.hash(password)
    return hashed


def verify_password(plain: str, hashed: str) -> bool:
    is_valid = pwd_context.verify(plain, hashed)
    return is_valid


def create_access_token(data: dict) -> str:
    encoded = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return encoded


def decode_access_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or Expired token')
    return decoded


def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    decoded = decode_access_token(token)
    return decoded.get('email')
