from fastapi import APIRouter

from api.services import get_nasa_api_service

router = APIRouter()


@router.get("/")
async def get_apod():
    nasa_api_service = get_nasa_api_service()
    return await nasa_api_service.get_apod()
