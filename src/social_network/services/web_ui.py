from fastapi import Depends
from social_network import tables
from social_network.db import get_session, Session


class UIService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_posts(self):
        posts = self.session.query(tables.Post).all()
        return posts

    def get_posts_by_user_id(self, user_id: int):
        my_posts = self.session.query(tables.Post).filter_by(author_id=user_id).all()
        return my_posts

    def get_likes_for_post(self, post_id: int):
        likes = self.session.query(tables.Likes).filter_by(post_id=post_id).all()
        return likes

    def get_dislikes_for_post(self, post_id: int):
        dislikes = self.session.query(tables.Dislikes).filter_by(post_id=post_id).all()
        return dislikes
