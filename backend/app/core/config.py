from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Application Settings
    PROJECT_NAME                : str = Field(default="Backend API", description="Project name")
    VERSION                     : str = Field(default="1.0.0", description="API version")
    API_HOST                    : str = Field(default="0.0.0.0", description="API host")
    API_PORT                    : int = Field(default=8000, description="API port")
    DEBUG                       : bool = Field(default=False, description="Debug mode")
    
    # Database Settings
    POSTGRES_DB                 : str = Field(description="PostgreSQL database name")
    POSTGRES_USER               : str = Field(description="PostgreSQL username")
    POSTGRES_PASSWORD           : str = Field(description="PostgreSQL password")
    POSTGRES_PORT               : int = Field(default=5432, description="PostgreSQL port")
    DB_POOL_SIZE                : int = Field(default=10, description="Database pool size")

    # Security Settings
    SECRET_KEY                  : str = Field(description="Secret key for JWT")
    ALGORITHM                   : str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES : int = Field(default=30, description="Token expiry time")
    
    # Logging
    LOG_LEVEL                   : str = Field(default="INFO", description="Log level")
    
    class Config:
        env_file                = ".env"
        env_file_encoding       = "utf-8"
        case_sensitive          = False


settings = Settings()