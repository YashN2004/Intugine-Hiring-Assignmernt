from fastapi import APIRouter
from geopy.distance import geodesic
from app.database import SessionLocal
from app.models import GPSLog, Trip, Route, Deviation
import json

router = APIRouter()

@router.post("/update-location")
def update_location(trip_id: int, latitude: float, longitude: float):
    db = SessionLocal()
    log = GPSLog(trip_id=trip_id, latitude=latitude, longitude=longitude)
    db.add(log)
    db.commit()

    route = db.query(Route).filter(Route.id == Trip.route_id).first()
    waypoints = json.loads(route.waypoints)

    for wp in waypoints:
        if geodesic((latitude, longitude), tuple(wp)).meters < 100:
            return {"status": "On route"}

    # Log deviation
    deviation = Deviation(trip_id=trip_id, lat=latitude, lon=longitude, reason="Out of buffer zone")
    db.add(deviation)
    db.commit()

    return {"status": "Deviation detected"}