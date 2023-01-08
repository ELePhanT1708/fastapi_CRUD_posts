from fastapi import FastAPI
from social_network.tables import Base
from social_network.db import engine
from social_network.api.user import router as user_router
from social_network.api.post import router as post_router
from social_network.api.likes import router as likes_router
from social_network.api.dislikes import router as dislikes_router
from social_network.api.web_ui import router as ui_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Social Network',
    description='Социальная сеть с постами',
    version='1.0.0',
)

app.include_router(user_router)
app.include_router(post_router)
app.include_router(likes_router)
app.include_router(dislikes_router)
app.include_router(ui_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
