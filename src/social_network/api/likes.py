from typing import List, Optional

from fastapi import APIRouter, Depends

from social_network.models.user import User
from social_network.models.likes import Like

from social_network.services.auth import get_current_user
from social_network.services.like import LikesService

router = APIRouter(
    prefix='/likes',
    tags=['Like']
)


@router.post('/create/{post_id}', response_model=Like)
async def create_like(post_id: int,
                user: User = Depends(get_current_user),
                service: LikesService = Depends()
                ):
    """
    Создание лайка для поста с определённым пользователем
    """
    return service.create(user_id=user.id,
                          post_id=post_id)


@router.post('/delete/{post_id}', response_model=None)
async def delete_like(post_id: int,
                user: User = Depends(get_current_user),
                service: LikesService = Depends()
                ):
    """
    Удаление лайка для поста с определённым пользователем
    """
    return service.delete(user_id=user.id,
                          post_id=post_id)