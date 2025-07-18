from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.models.base import Base
from datetime import datetime
from typing import List

class User(Base):
    __tablename__ = "users"
    
    id          : Mapped[int]           = mapped_column(primary_key=True, index=True)
    email       : Mapped[str]           = mapped_column(String(255), unique=True, index=True)
    username    : Mapped[str]           = mapped_column(String(100), unique=True, index=True)
    hashed_password : Mapped[str]       = mapped_column(String(255))
    is_active   : Mapped[bool]          = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool]          = mapped_column(Boolean, default=False)
    created_at  : Mapped[datetime]      = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at  : Mapped[datetime]      = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    refresh_tokens : Mapped[List["RefreshToken"]] = relationship("RefreshToken", back_populates="user")