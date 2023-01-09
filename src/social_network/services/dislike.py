from typing import List, Optional

from fastapi import Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from social_network import tables
from social_network.db import get_session


class DislikesService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> tables.Dislikes:
        dislike = self.session.query(tables.Dislikes) \
            .filter_by(user_id=user_id,
                       post_id=post_id).first()
        if not dislike:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return dislike

    def get_list_for_user(self, user_id: int) -> List[tables.Dislikes]:
        dislikes = self.session.query(tables.Dislikes).filter_by(user_id=user_id).all()

        return dislikes

    def get_list_for_post(self, post_id: int) -> List[tables.Dislikes]:
        dislikes = self.session.query(tables.Dislikes).filter_by(post_id=post_id).all()

        return dislikes

    def create(self, user_id: int, post_id: int) -> Optional[tables.Dislikes]:
        if self.session.query(tables.Dislikes).filter_by(user_id=user_id, post_id=post_id).first():
            raise HTTPException(status_code=405, detail="Can't dislike again!")
        iterable = self.session.query(tables.Post).filter_by(author_id=user_id).all()
        posts_id = [post.id for post in iterable]
        if post_id not in posts_id:
            dislike = tables.Dislikes(user_id=user_id,
                                      post_id=post_id)
            self.session.add(dislike)
            self.session.commit()
            return dislike
        raise HTTPException(status_code=405, detail="Can't dislike your posts !")

    def delete(self, user_id: int, post_id: int) -> None:
        dislike = self._get(user_id=user_id, post_id=post_id)
        self.session.delete(dislike)
        self.session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
