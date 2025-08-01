from fastapi import FastAPI
from app.routes import trip_routes

app = FastAPI()

app.include_router(trip_routes.router)
