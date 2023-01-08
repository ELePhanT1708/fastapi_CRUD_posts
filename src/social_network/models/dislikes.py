from pydantic import BaseModel


class BaseDislike(BaseModel):
    pass


class DislikeCreate(BaseDislike):
    pass


class DislikeUpdate(BaseDislike):
    pass


class Dislike(BaseDislike):
    id: int
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
