from typing import List, Optional

from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from social_network import tables
from social_network.db import get_session
from social_network.models.action import ActionType
from social_network.models.post  import Post, PostCreate, PostUpdate


class PostsService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> tables.Post:
        post = self.session.query(tables.Post)\
            .filter_by(id=post_id,
                       author_id=user_id)\
            .first()
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return post

    def get_list(self, user_id: int) -> List[tables.Post]:
        posts = self.session.query(tables.Post).filter_by(author_id=user_id).all()

        return posts

    def get_likes(self, post_id: int) -> List[tables.Action]:
        likes = self.session.query(tables.Action).filter_by(post_id=post_id, action_type=ActionType.LIKE).all()
        return likes

    def get_dislikes(self, post_id: int) -> List[tables.Action]:
        dislikes = self.session.query(tables.Action).filter_by(post_id=post_id, action_type=ActionType.DISLIKE).all()
        return dislikes

    def create(self, user_id: int, post_data: PostCreate) -> tables.Post:
        post = tables.Post(**post_data.dict(), author_id=user_id)
        self.session.add(post)
        self.session.commit()
        return post

    def update(self, user_id: int, post_id: int, post_data: PostUpdate) -> tables.Post:
        post = self._get(user_id, post_id)
        for key, value in post_data:
            setattr(post, key, value)
        self.session.commit()
        return post

    def delete(self, user_id: int, post_id: int) -> None:
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)