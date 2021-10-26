import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"data": "index page"}


@app.get("/blog")
def index(published: bool = True, limit: int = 10, sort: Optional[str] = None):
    if published:
        return {"data": {"name": "Sims", "limit": limit}}
    else:
        return {"data": "false"}


@app.get("/blog/unpublished")
def get_unpublished_blog():
    return {"data": "all unpublished blog"}


@app.get("/blog/{id}")
def about(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def showComments(id: int):
    return {"data": id, "comments": ["hello"]}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"blog is created with title as {blog.title}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
