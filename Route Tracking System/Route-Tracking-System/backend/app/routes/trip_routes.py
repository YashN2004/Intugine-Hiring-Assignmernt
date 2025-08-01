from fastapi import APIRouter, Form
from typing import List

router = APIRouter()

# Route 1: Add Route
@router.post("/add-route")
async def add_route(
    source: str,
    destination: str,
    waypoints: List[str] = Form(...)
):
    return {
        "source": source,
        "destination": destination,
        "waypoints": waypoints
    }

# Route 2: Create Trip
@router.post("/create-trip")
async def create_trip(
    truck_id: int,
    route_id: int
):
    return {
        "truck_id": truck_id,
        "route_id": route_id,
        "status": "Trip created successfully"
    }

# Route 3: Update Location
@router.post("/update-location")
async def update_location(
    trip_id: int,
    latitude: float,
    longitude: float
):
    return {
        "trip_id": trip_id,
        "location": {
            "latitude": latitude,
            "longitude": longitude
        },
        "status": "Location updated"
    }

# Route 4: Send Alert
@router.post("/send-alert")
async def send_alert(
    phone: str,
    msg: str
):
    return {
        "phone": phone,
        "message": msg,
        "status": "Alert sent"
    }
