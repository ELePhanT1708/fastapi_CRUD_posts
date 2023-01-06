from pydantic import BaseModel


class BaseUser(BaseModel):
    username: str
    age: int


class UserCreate(BaseUser):
    password: str


class UserUpdate(BaseUser):
    pass


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
