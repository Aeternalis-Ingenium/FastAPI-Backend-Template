import fastapi

import src
from src.main import backend_app


def test_src_version() -> None:
    assert src.__version__ == "0.0.1"


def test_application_is_fastapi_instance() -> None:
    assert isinstance(backend_app, fastapi.FastAPI)
    assert backend_app.redoc_url == "/redoc"
    assert backend_app.docs_url == "/docs"
    assert backend_app.openapi_url == "/openapi.json"
    assert backend_app.redoc_url == "/redoc"
