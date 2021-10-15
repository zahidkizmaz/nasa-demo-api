from urllib.parse import urljoin

import aiohttp
from fastapi import APIRouter

from settings.config import settings

router = APIRouter()


@router.get("/")
async def get_apod():
    apod_url = urljoin(settings.NASA_API_URL, settings.APOD_URL_PATH)
    async with aiohttp.ClientSession() as session:
        async with session.get(apod_url, params=settings.NASA_API_KEY) as response:
            return await response.json()
