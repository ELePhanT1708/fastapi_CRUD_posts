from enum import Enum

from pydantic import BaseModel


class ActionType(str, Enum):
    DISLIKE = 'Dislike'
    LIKE = 'Like'


class BaseAction(BaseModel):
    action_type: ActionType


class ActionCreate(BaseAction):
    pass


class ActionUpdate(BaseAction):
    pass


class Action(BaseAction):
    id: int
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
