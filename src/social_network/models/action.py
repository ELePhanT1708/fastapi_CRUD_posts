from pydantic import BaseModel


from sqlalchemy import Enum


class ActionType(str, Enum):
    DISLIKE = 'Dislike'
    LIKE = 'Like'


class BaseAction(BaseModel):
    user_id: int
    post_id: int
    action_type: ActionType


class ActionCreate(BaseAction):
    pass


class ActionUpdate(BaseAction):
    pass


class Action(BaseAction):
    id: int

    class Config:
        orm_mode = True
