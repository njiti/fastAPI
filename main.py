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

# s
@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}


@app.get("/posts")
def get_post():
    return {"data": "This is your post"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return {"data": "new post"}
# title str, content str, category, Boolean published/draft
