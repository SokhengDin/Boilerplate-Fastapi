from sqlalchemy import String, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.models.base import Base
from datetime import datetime

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    
    id          : Mapped[int]           = mapped_column(primary_key=True, index=True)
    token       : Mapped[str]           = mapped_column(String(500), unique=True, index=True)
    user_id     : Mapped[int]           = mapped_column(ForeignKey("users.id"))
    expires_at  : Mapped[datetime]      = mapped_column(DateTime(timezone=True))
    created_at  : Mapped[datetime]      = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    user        : Mapped["User"]        = relationship("User", back_populates="refresh_tokens")

class LoginAttempt(Base):
    __tablename__ = "login_attempts"
    
    id          : Mapped[int]           = mapped_column(primary_key=True, index=True)
    email       : Mapped[str]           = mapped_column(String(255), index=True)
    ip_address  : Mapped[str]           = mapped_column(String(45))
    success     : Mapped[bool]          = mapped_column()
    attempted_at: Mapped[datetime]      = mapped_column(DateTime(timezone=True), server_default=func.now())