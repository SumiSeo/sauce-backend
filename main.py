from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()
class Post(BaseModel):
    title:str
    content:str
    published:bool = True # setting default value
    rating: Optional[int] = None # fully optional field

my_posts = [
    {
        "id": 1,
        "title": "Title of Post 1",
        "content": "Content of Post 1"
    },
    {
        "id": 2,
        "title": "Title of Post 2",
        "content": "Content of Post 2"
    },
    {
        "id": 3,
        "title": "Title of Post 3",
        "content": "Content of Post 3"
    }
]

@app.get("/")
def root():
    return {"message": "coucou, welcome to my api"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
        
        
@app.get("/post/{id}")
def get_post(id:int):
    data = find_post(id)
    if not data:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message":f"Post with {id} was not found in posts"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with {id} was not found in posts")
    return {"data":data}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post:Post):
    post = new_post.model_dump()
    post["id"] = randrange(0, 100000)
    my_posts.append(post)
    return {"new_post": post}

