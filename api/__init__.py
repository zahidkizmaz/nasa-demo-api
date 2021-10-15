from fastapi import FastAPI

from api.router import api_router
from settings.config import settings


def create_app() -> FastAPI:
    app = FastAPI(debug=settings.DEBUG)
    app.include_router(router=api_router, prefix="/api")
    return app
