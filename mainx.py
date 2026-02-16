from fastapi import FastAPI
from enum import Enum
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="Test API",
    version="1.0.0",
    description='This is a simple Test api'
)

@app.get("/")
def root():
    return {"Message": "Hello world"}

@app.get("/about")
def about():
    return {
        "Author": "Ajay Gonhalmath",
        'app': "Fast App tutorial"
    }

#path parameters
@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict:
    return {
        "user_id": user_id
    }

#multiple path parameters
@app.get("/posts/{post_id}/comments/{comment_id}")
def get_comments(post_id: int, comment_id: int):
    return {
        "post_id": post_id,
        "comment_id": comment_id
    }

#enums in Paths
class Model(str, Enum):
    alex = "alex"
    dj = "dj"


@app.get("/models/{model_name}")
def get_model(model_name: Model):
    if model_name == Model.alex:
        return {
            "model": model_name,
            "message": "DL FTW!"
        }
    return {
        "model": model_name
    }


@app.get("/xd")
def xd():
    return {
        'data': {
            'xd': 'xxd'
        }
    }

class Blog(BaseModel):
    title: str
    body: str

@app.post("/testpost/{pth}")
def testpost(request: Blog):
    return {
        'x': request.title,
        'd': request.body
    }

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
