from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api.router import api_router
from settings.config import settings
from views.router import view_router


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.include_router(router=view_router)
    app.include_router(router=api_router, prefix="/api")

    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app
