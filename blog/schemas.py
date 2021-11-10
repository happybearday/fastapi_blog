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