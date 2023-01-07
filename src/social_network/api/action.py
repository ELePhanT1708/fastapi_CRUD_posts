from typing import List, Optional

from fastapi import APIRouter, Depends

from social_network.models.user import (
    Token, User
)
from social_network.models.action import (
    ActionCreate, Action, ActionType
)

from social_network.services.auth import get_current_user
from social_network.services.action import ActionsService

router = APIRouter(
    prefix='/actions',
    tags=['Action']
)


@router.post('/create/{post_id}', response_model=Optional[Action])
def create_action(post_id: int,
                  action_type: ActionType,
                  user: User = Depends(get_current_user),
                  service: ActionsService = Depends()
                  ):
    """
    Создание лайка или дизлайка для поста с определённым пользователем
    """
    return service.create(user_id=user.id,
                          action_type=action_type,
                          post_id=post_id)

# @router.put('/{post_id}', response_model=Post)
# def update_post(
#         post_id: int,
#         post_data: PostUpdate,
#         service: PostsService = Depends(),
#         user: User = Depends(get_current_user)
# ):
#     return service.update(user_id=user.id, post_id=post_id, post_data=post_data)
#
#
# @router.get('/posts', response_model=List[Post])
# def get_posts(
#         service: PostsService = Depends(),
#         user: User = Depends(get_current_user)):
#     return service.get_list(user_id=user.id)
#
#
# @router.get('/posts/{post_id}', response_model=Post)
# def get_operations(post_id: int,
#                    service: PostsService = Depends(),
#                    user: User = Depends(get_current_user)):
#     return service._get(user_id=user.id, post_id=post_id)
#
#
# @router.delete('/{post_id}')
# def delete_operation(post_id: int,
#                      service: PostsService = Depends(),
#                      user: User = Depends(get_current_user)):
#     return service.delete(user_id=user.id, post_id=post_id)
