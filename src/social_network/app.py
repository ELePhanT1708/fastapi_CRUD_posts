from fastapi import FastAPI
from social_network.tables import Base
from social_network.db import engine
from social_network.api.user import router as user_router
from social_network.api.post import router as post_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Social Network',
    description='Социальная сеть с постами',
    version='1.0.0',
)

app.include_router(user_router)
app.include_router(post_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
