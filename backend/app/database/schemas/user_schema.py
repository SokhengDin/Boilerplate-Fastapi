from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email       : EmailStr
    username    : str = Field(min_length=3, max_length=50)
    is_active   : bool = True

class UserCreate(UserBase):
    password    : str = Field(min_length=8)

class UserUpdate(BaseModel):
    email       : Optional[EmailStr] = None
    username    : Optional[str] = Field(None, min_length=3, max_length=50)
    is_active   : Optional[bool] = None

class UserResponse(UserBase):
    id          : int
    is_superuser: bool
    created_at  : datetime
    updated_at  : datetime
    
    class Config:
        from_attributes = True

class UserInDB(UserResponse):
    hashed_password : str