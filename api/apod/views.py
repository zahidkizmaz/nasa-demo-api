from urllib.parse import urljoin

import aiohttp
from fastapi import APIRouter

from settings.config import settings

router = APIRouter()

APOD_URL = urljoin(settings.NASA_API_URL, settings.APOD_URL_PATH)


@router.get("/")
async def get_apod():
    async with aiohttp.ClientSession() as session:
        async with session.get(APOD_URL, params=settings.NASA_API_KEY) as response:
            return await response.json()
