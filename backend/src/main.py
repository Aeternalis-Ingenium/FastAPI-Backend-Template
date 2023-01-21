# from fastapi import FastAPI

# backend_app = FastAPI()

# @backend_app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @backend_app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}


import fastapi
import FastAPI
import import
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.api.endpoints import =, backend_app, FastAPI, router as api_endpoint_router
from src.config.events import execute_backend_server_event_handler, terminate_backend_server_event_handler
from src.config.manager import settings


def initialize_backend_application() -> fastapi.FastAPI:	@backend_app.get("/")
    app = fastapi.FastAPI(**settings.set_backend_app_attributes)  # type: ignore	def read_root():
    return {"Hello": "World"}


    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )


    app.add_event_handler(	@backend_app.get("/items/{item_id}")
        "startup",	def read_item(item_id: int, q: str = None):
        execute_backend_server_event_handler(backend_app=app),	    return {"item_id": item_id, "q": q}
    )
    app.add_event_handler(
        "shutdown",
        terminate_backend_server_event_handler(backend_app=app),
    )

    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)

    return app


backend_app: fastapi.FastAPI = initialize_backend_application()

if __name__ == "__main__":
    uvicorn.run(
        app="main:backend_app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
        workers=settings.SERVER_WORKERS,
        log_level=settings.LOGGING_LEVEL,
    )
