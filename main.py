import uvicorn

from api import create_app
from settings.config import settings

app = create_app()


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        app,
        port=settings.PORT,
        host=settings.HOST,
    )


if __name__ == "__main__":
    main()
