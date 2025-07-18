from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_session
from app.services.user_service import UserService
from app.database.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from typing import List

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_data   : UserCreate,
    db          : Session   = Depends(get_session)
):
    existing_user           = UserService.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code     = status.HTTP_400_BAD_REQUEST,
            detail          = "Email already registered"
        )
    
    existing_username       = UserService.get_user_by_username(db, user_data.username)
    if existing_username:
        raise HTTPException(
            status_code     = status.HTTP_400_BAD_REQUEST,
            detail          = "Username already taken"
        )
    
    return UserService.create_user(db, user_data)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_session)
):
    user = UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code     = status.HTTP_404_NOT_FOUND,
            detail          = "User not found"
        )
    return user

@router.get("/", response_model=List[UserResponse])
def get_users(
    skip    : int = 0,
    limit   : int = 100,
    db      : Session = Depends(get_session)
):
    return UserService.get_users(db, skip=skip, limit=limit)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id     : int,
    user_data   : UserUpdate,
    db          : Session = Depends(get_session)
):
    user = UserService.update_user(db, user_id, user_data)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail      = "User not found"
        )
    return user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id : int,
    db      : Session = Depends(get_session)
):
    success         = UserService.delete_user(db, user_id)
    if not success:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail      = "User not found"
        )