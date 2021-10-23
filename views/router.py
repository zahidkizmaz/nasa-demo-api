from fastapi.routing import APIRouter

from views import apod_view

view_router = APIRouter()

view_router.include_router(apod_view.router, prefix="/apod")
