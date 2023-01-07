from typing import List, Optional

from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from social_network import tables
from social_network.db import get_session
from social_network.models.action import Action, ActionCreate, ActionUpdate, ActionType


class ActionsService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, action_id: int) -> tables.Action:
        action = self.session.query(tables.Action) \
            .get(id=action_id) \
            .first()
        if not action:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return action

    def get_list(self, user_id: int) -> List[tables.Action]:
        actions = self.session.query(tables.Action).filter_by(user_id=user_id).all()

        return actions

    def create(self, user_id: int, post_id: int, action_type: ActionType) -> Optional[tables.Action]:
        posts_id = [post.author_id for post in self.session.query(tables.Post).filter_by(author_id=user_id).all()]
        if post_id not in posts_id:
            action = tables.Action(action_type=action_type,
                                   user_id=user_id,
                                   post_id=post_id)
            self.session.add(action)
            self.session.commit()
            return action
        raise HTTPException(status_code=405, detail="Can't like your posts !")

    # def delete(self, user_id: int, post_id: int) -> None:
    #     post = self._get(user_id, post_id)
    #     self.session.delete(post)
    #     self.session.commit()
    #     return Response(status_code=status.HTTP_204_NO_CONTENT)
