from datetime import datetime, timedelta

from passlib.hash import bcrypt
from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from starlette.authentication import AuthenticationBackend, AuthenticationError

from .. import tables
from ..db import get_session
from ..models.user import User, Token, UserCreate
from ..settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign_in')


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return AuthService.validate_token(token=token)


class AuthService:

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"}, )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm]
            )

        except JWTError:
            raise credentials_exception from None
        user_data = payload.get('user')
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise credentials_exception from None
        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)
        # payload arguments
        now = datetime.utcnow()
        payload = {
            'iat': now,  # token creating time
            'nbf': now,  # token activating time
            'exp': now + timedelta(seconds=settings.jwt_exp_time),  # token expiring time
            'sub': str(user_data.id),
            'user': user_data.dict()
        }
        token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
        return Token(access_token=token)

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def register_user(self, user_data: UserCreate) -> Token:
        user = tables.User(
            username=user_data.username,
            age=user_data.age,
            password_hash=self.hash_password(user_data.password)
        )
        self.session.add(user)
        self.session.commit()
        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials! (username or password)",
            headers={"WWW-Authenticate": "Bearer"}, )

        user = self.session.query(tables.User).filter(tables.User.username == username).first()
        if not user:
            raise credentials_exception
        if not self.verify_password(password, user.password_hash):
            raise credentials_exception
        return self.create_token(user)