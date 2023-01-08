from fastapi import APIRouter, Depends

from social_network.models.dislikes import Dislike
from social_network.models.user import User

from social_network.services.auth import get_current_user
from social_network.services.dislike import DislikesService

router = APIRouter(
    prefix='/dislikes',
    tags=['Dislike']
)


@router.post('/create/{post_id}', response_model=Dislike)
def create_dislike(post_id: int,
                   user: User = Depends(get_current_user),
                   service: DislikesService = Depends()
                   ):
    """
    Создание лайка для поста с определённым пользователем
    """
    return service.create(user_id=user.id,
                          post_id=post_id)


@router.post('/delete/{post_id}', response_model=None)
def delete_dislike(post_id: int,
                   user: User = Depends(get_current_user),
                   service: DislikesService = Depends()
                   ):
    """
    Удаление лайка для поста с определённым пользователем
    """
    return service.delete(user_id=user.id,
                          post_id=post_id)
