import uvicorn
from fastapi import FastAPI

from blog.schemas import Blog
from . import models, schemas
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("/blog")
def create(blog: Blog):
    return blog
