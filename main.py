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


my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {
        "title": "favourite foods", "content": "I like pizza", "id": 2}]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_post():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
# title str, content str, category, Boolean published/draft
