import uvicorn
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user
from .routers import authentification as auth


app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)
