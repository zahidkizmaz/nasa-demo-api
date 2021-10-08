import uvicorn

from api import create_app


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        create_app(),
        port=8080,
        host="127.0.0.1",
    )


if __name__ == "__main__":
    main()
