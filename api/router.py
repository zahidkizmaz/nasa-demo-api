from fastapi.routing import APIRouter

from api import apod

api_router = APIRouter()

api_router.include_router(apod.router, prefix="/apod")
