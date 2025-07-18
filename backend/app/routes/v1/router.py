from fastapi import APIRouter
from app.routes.v1.handlers import user_handler, auth_handler

router  = APIRouter()


router.include_router(user_handler.router       , prefix="/users"        , tags=["USERS"])
router.include_router(auth_handler.router       , prefix="/auths"        , tags=["AUTHS"])