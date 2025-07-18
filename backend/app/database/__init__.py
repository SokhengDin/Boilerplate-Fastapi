from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings
from contextlib import contextmanager
from typing import Generator

database_url    = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine          = create_engine(
    database_url,
    pool_size       = settings.DB_POOL_SIZE,
    pool_pre_ping   = True,
    pool_recycle    = 300,
    echo            = settings.DEBUG
)

SessionLocal = sessionmaker(
    autocommit  = False,
    autoflush   = False,
    bind        = engine
)

def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()