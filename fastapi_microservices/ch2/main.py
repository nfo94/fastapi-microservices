from fastapi import FastAPI
from .routes.login import user
from .routes.places import destination

app = FastAPI()

app.include_router(user.router)
app.include_router(destination.router)
