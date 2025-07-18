from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.logger import logger
from app.routes.v1.router import router
from app.database.models import Base
from app.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Application ...")
    
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
    
    yield
    logger.info("Shutting Application ...")

app = FastAPI(
    lifespan    = lifespan,
    title       = settings.PROJECT_NAME,
    version     = settings.VERSION
)

app.include_router(
    router 
    , prefix   = "/api/v1"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host        = settings.API_HOST,
        port        = settings.API_PORT,
        reload_dirs = ["app"],
        reload      = True
    )
