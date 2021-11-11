from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


class ShowBlog(BaseModel):
    title: str

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(User):
    name: str
    email: str

    class Config():
        orm_mode = True
