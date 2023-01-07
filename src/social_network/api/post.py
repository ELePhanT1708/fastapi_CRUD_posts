from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from social_network.models.action import Action
from social_network.models.user import (
    Token, User
)
from social_network.models.post import (
    Post, PostUpdate, PostCreate
)

from social_network.services.auth import get_current_user
from social_network.services.post import PostsService

router = APIRouter(
    prefix='/post',
    tags=['Post']
)


@router.post('/create', response_model=Post)
def create_post(post_data: PostCreate,
                user: User = Depends(get_current_user),
                service: PostsService = Depends()
                ):
    """
    Регистрация пользователя в системе по логину и паролю
    :param user:
    :param service:
    :type post_data: object
    """
    return service.create(user_id=user.id,
                          post_data=post_data)


@router.put('/{post_id}', response_model=Post)
def update_post(
        post_id: int,
        post_data: PostUpdate,
        service: PostsService = Depends(),
        user: User = Depends(get_current_user)
):
    return service.update(user_id=user.id, post_id=post_id, post_data=post_data)


@router.get('/posts', response_model=List[Post])
def get_posts(
        service: PostsService = Depends(),
        user: User = Depends(get_current_user)):
    return service.get_list(user_id=user.id)


@router.get('/posts/{post_id}', response_model=Post)
def get_operations(post_id: int,
                   service: PostsService = Depends(),
                   user: User = Depends(get_current_user)):
    return service._get(user_id=user.id, post_id=post_id)


@router.delete('/{post_id}')
def delete_operation(post_id: int,
                     service: PostsService = Depends(),
                     user: User = Depends(get_current_user)):
    return service.delete(user_id=user.id, post_id=post_id)


@router.get('/likes/{post_id}', response_model=List[Action])
def get_likes(post_id: int,
              service: PostsService = Depends()):
    return service.get_likes(post_id=post_id)


@router.get('/dislikes/{post_id}', response_model=List[Action])
def get_dislikes(post_id: int,
                 service: PostsService = Depends()):
    return service.get_dislikes(post_id=post_id)
