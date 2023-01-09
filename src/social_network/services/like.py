from typing import List, Optional

from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from social_network import tables
from social_network.db import get_session
from social_network.models.likes import Like
from social_network.models.likes import Like


class LikesService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> tables.Likes:
        likes = self.session.query(tables.Likes) \
            .filter_by(user_id=user_id,
                       post_id=post_id) \
            .first()
        if not likes:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return likes

    def get_list_for_user(self, user_id: int) -> List[tables.Likes]:
        likes = self.session.query(tables.Likes).filter_by(user_id=user_id).all()

        return likes

    def get_list_for_post(self, post_id: int) -> List[tables.Likes]:
        likes = self.session.query(tables.Likes).filter_by(post_id=post_id).all()

        return likes

    def create(self, user_id: int, post_id: int) -> Optional[tables.Likes]:
        existing_like = self.session.query(tables.Likes).filter_by(user_id=user_id, post_id=post_id).first()
        if existing_like:
            raise HTTPException(status_code=405, detail="Can't like again!")
        iterable = self.session.query(tables.Post).filter_by(author_id=user_id).all()
        posts_id = [post.id for post in iterable]
        if post_id in posts_id:
            raise HTTPException(status_code=405, detail="Can't like your posts !")
        like = tables.Likes(user_id=user_id,
                            post_id=post_id)
        self.session.add(like)
        self.session.commit()
        return like

    def delete(self, user_id: int, post_id: int) -> None:
        like = self._get(user_id=user_id, post_id=post_id)
        self.session.delete(like)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
