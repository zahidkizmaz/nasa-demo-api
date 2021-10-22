import uvicorn
from starlette.templating import Jinja2Templates

from api import create_app
from settings.config import settings

app = create_app()
templates = Jinja2Templates(directory="templates")


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        app,
        port=settings.PORT,
        host=settings.HOST,
    )


if __name__ == "__main__":
    main()
