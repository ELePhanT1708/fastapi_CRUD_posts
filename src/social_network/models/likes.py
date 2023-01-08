from pydantic import BaseModel


class BaseLike(BaseModel):
    pass


class LikeCreate(BaseLike):
    pass


class LikeUpdate(BaseLike):
    pass


class Like(BaseLike):
    id: int
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
