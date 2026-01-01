from fastapi import FastAPI
from pydantic import BaseModel


class Blog(BaseModel):
    body: str

class ShowBlog(Blog):
    body: str
    class Config():
        from_attributes = True
