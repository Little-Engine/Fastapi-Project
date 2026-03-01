from pydantic import BaseModel, EmailStr, ConfigDict, Field
from typing import Optional, Annotated
from datetime import datetime

# Request Schemas


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

# Response Schemas


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    # class Config:
    #     orm_mode = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]
