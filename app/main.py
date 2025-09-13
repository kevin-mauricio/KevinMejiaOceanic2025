from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db import init_db
from app.nasa_api import get_insight_data, store_data

@asynccontextmanager
async def startup_event(app: FastAPI):
    init_db()
    yield
app = FastAPI(lifespan=startup_event, title="Mars weather API", version="1.0.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Mars weather API!"}

@app.get("/fetch-and-store-data")
async def fetch_and_store_data():
    return store_data()
    