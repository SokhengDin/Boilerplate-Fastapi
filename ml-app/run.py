import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "main:app"
        , host      = settings.API_HOST
        , port      = settings.API_PORT
        , reload    = settings.DEBUG
    )