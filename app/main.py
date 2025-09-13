from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.params import Query

from app.db import init_db
from app.nasa_api import store_data
from app.gemini import query_gemini_api

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

@app.get("/gemini-prompt")
async def gemini_prompt(query: str = Query(str, description="Your question about Mars weather")):
    return query_gemini_api(query)