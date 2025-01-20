from fastapi import FastAPI
from login import user
from manager import manager
from places import destination
from visitor import visitor
from feedback import post

app = FastAPI()

app.include_router(manager.router)
app.include_router(user.router)
app.include_router(destination.router)
app.include_router(visitor.router)
app.include_router(post.router, prefix="/post")
