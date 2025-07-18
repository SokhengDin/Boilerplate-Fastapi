from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class LoginRequest(BaseModel):
    email       : EmailStr
    password    : str

class TokenResponse(BaseModel):
    access_token    : str
    refresh_token   : str
    token_type      : str = "bearer"
    expires_in      : int

class RefreshTokenRequest(BaseModel):
    refresh_token   : str

class RefreshTokenResponse(BaseModel):
    id          : int
    token       : str
    user_id     : int
    expires_at  : datetime
    created_at  : datetime
    
    class Config:
        from_attributes = True

class LoginAttemptResponse(BaseModel):
    id          : int
    email       : str
    ip_address  : str
    success     : bool
    attempted_at: datetime
    
    class Config:
        from_attributes = True