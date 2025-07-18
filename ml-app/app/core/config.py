from pydantic_settings import BaseSettings
from pydantic import Field
from decouple import config

class Settings(BaseSettings):

    APP_NAME        : str = Field(default="Dog/Cat Prediction API", description="Application name")
    APP_VERSION     : str = Field(default="1.0.0", description="Application version")
    API_HOST        : str = Field(default="0.0.0.0", description="API host")
    API_PORT        : int = Field(default=8000, description="API port")
    DEBUG           : bool = Field(default=False, description="Debug mode")

    MODEL_NAME      : str = Field(default="google/vit-base-patch16-224", description="Hugging Face model name")
    MAX_IMAGE_SIZE  : int = Field(default=224, description="Maximum image size for processing")
    
    LOG_LEVEL       : str = Field(default="INFO", description="Log level")
    
    class Config:
        env_file                = ".env"
        env_file_encoding       = "utf-8"
        case_sensitive          = False
        protected_namespaces    = ('settings_',)

def get_settings() -> Settings:
    return Settings()

settings = get_settings()