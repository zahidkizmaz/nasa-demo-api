from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse

from api.apod.views import get_apod

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def apod_view(request: Request):
    from main import templates

    response = await get_apod()

    context = {"request": request} | response
    return templates.TemplateResponse("apod/apod_detail.html", context)
