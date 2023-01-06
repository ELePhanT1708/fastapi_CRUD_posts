from pydantic import BaseModel


class BasePost(BaseModel):
    name: str
    body: str


class PostCreate(BasePost):
    pass


class PostUpdate(BasePost):
    pass


class Post(BasePost):
    id: int

    class Config:
        orm_mode = True
