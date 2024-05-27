from endpoints import router
from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    Create the FastAPI backend server application.
    """
    app = FastAPI()
    app.include_router(router)

    return app


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:create_app", factory=True, reload=True)
