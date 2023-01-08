from typing import List

from fastapi import APIRouter, Request, Depends
from starlette.responses import HTMLResponse, FileResponse

from social_network.models.user import User
from social_network.services.auth import get_current_user
from social_network.services.web_ui import UIService
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix='/ui',
    tags=['UI']
)


@router.get("/posts", response_class=HTMLResponse)
async def get_posts(request: Request,
                    service: UIService = Depends()):
    """
    Get all existing posts on platform
    """
    posts = service.get_posts()
    return templates.TemplateResponse("posts.html", {"request": request,
                                                     "title": 'POSTS',
                                                     "posts": posts
                                                     }
                                      )




