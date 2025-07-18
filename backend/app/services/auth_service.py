from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.models.auth_model import RefreshToken, LoginAttempt
from app.database.models.user_model import User
from app.services.user_service import UserService

from app.core.security import create_access_token, create_refresh_token
from app.database.schemas.auth_schema import TokenResponse

from datetime import datetime, timedelta
from typing import Optional

class AuthService:
    
    @staticmethod
    def login(db: Session, email: str, password: str, ip_address: str) -> Optional[TokenResponse]:
        AuthService.log_login_attempt(db, email, ip_address, False)
        
        user            = UserService.authenticate_user(db, email, password)
        if not user or not user.is_active:
            return None
        
        AuthService.log_login_attempt(db, email, ip_address, True)
        
        access_token    = create_access_token(data={"sub": str(user.id)})
        refresh_token   = create_refresh_token()
        
        AuthService.store_refresh_token(db, refresh_token, user.id)
        
        return TokenResponse(
            access_token    = access_token,
            refresh_token   = refresh_token,
            expires_in      = 1800
        )
    
    @staticmethod
    def refresh_access_token(db: Session, refresh_token: str) -> Optional[TokenResponse]:
        token_record = AuthService.get_refresh_token(db, refresh_token)
        if not token_record or token_record.expires_at < datetime.utcnow():
            return None
        
        new_access_token    = create_access_token(data={"sub": str(token_record.user_id)})
        new_refresh_token   = create_refresh_token()
        
        AuthService.delete_refresh_token(db, refresh_token)
        AuthService.store_refresh_token(db, new_refresh_token, token_record.user_id)
        
        return TokenResponse(
            access_token    = new_access_token,
            refresh_token   = new_refresh_token,
            expires_in      = 1800
        )
    
    @staticmethod
    def logout(db: Session, refresh_token: str) -> bool:
        return AuthService.delete_refresh_token(db, refresh_token)
    
    @staticmethod
    def store_refresh_token(db: Session, token: str, user_id: int) -> RefreshToken:
        expires_at  = datetime.utcnow() + timedelta(days=30)
        db_token    = RefreshToken(
            token       = token,
            user_id     = user_id,
            expires_at  = expires_at
        )
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
        return db_token
    
    @staticmethod
    def get_refresh_token(db: Session, token: str) -> Optional[RefreshToken]:
        return db.scalar(select(RefreshToken).where(RefreshToken.token == token))
    
    @staticmethod
    def delete_refresh_token(db: Session, token: str) -> bool:
        token_record = AuthService.get_refresh_token(db, token)
        if not token_record:
            return False
        
        db.delete(token_record)
        db.commit()
        return True
    
    @staticmethod
    def log_login_attempt(db: Session, email: str, ip_address: str, success: bool) -> LoginAttempt:
        attempt = LoginAttempt(
            email       = email,
            ip_address  = ip_address,
            success     = success
        )
        db.add(attempt)
        db.commit()
        db.refresh(attempt)
        return attempt