from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.database import get_session
from app.services.auth_service import AuthService
from app.database.schemas.auth_schema import LoginRequest, TokenResponse, RefreshTokenRequest

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
def login(
    login_data  : LoginRequest,
    request     : Request,
    db          : Session     = Depends(get_session)
):
    ip_address      = request.client.host
    token_response  = AuthService.login(
        db, 
        login_data.email, 
        login_data.password, 
        ip_address
    )
    
    if not token_response:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail      = "Invalid credentials"
        )
    
    return token_response

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(
    refresh_data: RefreshTokenRequest,
    db          : Session   = Depends(get_session)
):
    token_response          = AuthService.refresh_access_token(db, refresh_data.refresh_token)
    
    if not token_response:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail      = "Invalid or expired refresh token"
        )
    
    return token_response

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    refresh_data: RefreshTokenRequest,
    db          : Session = Depends(get_session)
):
    success = AuthService.logout(db, refresh_data.refresh_token)
    
    if not success:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail      = "Invalid refresh token"
        )