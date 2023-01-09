from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from social_network.models.user import (
    UserCreate,
    Token, User
)
from social_network.services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth',
    tags=['User']
)


@router.post('/sign_up', response_model=Token)
async def sign_up(user_data: UserCreate,
            service: AuthService = Depends()
            ):
    """
    Регистрация пользователя в системе по логину и паролю
    """
    return service.register_user(user_data=user_data)


@router.post('/sign_in', response_model=Token)
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
            service: AuthService = Depends(),
            ):
    """
        Авторизация пользователя в системе по логину и паролю
        """
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@router.get('/user', response_model=User)
async def get_user(user: User = Depends(get_current_user)):
    return user
