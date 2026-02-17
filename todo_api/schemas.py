from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    id: int

    class Config:
        from_attributes = True


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class UserCreate(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    