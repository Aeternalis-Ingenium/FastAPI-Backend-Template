from fastapi import FastAPI

backend_app = FastAPI()

@backend_app.get("/")
def read_root():
    return {"Hello": "World"}

@backend_app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
