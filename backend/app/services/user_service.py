from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.models.user_model import User
from app.database.schemas.user_schema import UserCreate, UserUpdate
from app.core.security import hash_password, verify_password

from typing import Optional, List

class UserService:
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        hashed_password = hash_password(user_data.password)
        db_user = User(
            email               = user_data.email,
            username            = user_data.username,
            hashed_password     = hashed_password,
            is_active           = user_data.is_active
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        return db.scalar(select(User).where(User.id == user_id))
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        return db.scalar(select(User).where(User.email == email))
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        return db.scalar(select(User).where(User.username == username))
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        return db.scalars(select(User).offset(skip).limit(limit)).all()
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[User]:
        user = UserService.get_user_by_id(db, user_id)
        if not user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        user = UserService.get_user_by_id(db, user_id)
        if not user:
            return False
        
        db.delete(user)
        db.commit()
        return True
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        user = UserService.get_user_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user