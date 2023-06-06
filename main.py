from typing import Optional

from fastapi.params import Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_post():
    return {"data": "This is your post"}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    return {"data": "post"}
# title str, content str, category, Boolean published/draft
