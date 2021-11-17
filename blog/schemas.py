from typing import Optional, List
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class BlogBase(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


class Blog(BlogBase):
    title: str
    body: str
    published_at: Optional[bool]

    class Config:
        orm_mode = True


class ShowUser(User):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
