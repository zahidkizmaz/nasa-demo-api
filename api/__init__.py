from fastapi import FastAPI

from api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=api_router, prefix="/api")
    return app
