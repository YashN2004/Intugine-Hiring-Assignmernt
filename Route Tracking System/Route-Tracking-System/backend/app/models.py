from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    source = Column(String)
    destination = Column(String)
    waypoints = Column(String)  # Stored as JSON string

class Truck(Base):
    __tablename__ = 'trucks'
    id = Column(Integer, primary_key=True)
    plate_no = Column(String)

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    truck_id = Column(Integer, ForeignKey("trucks.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))

class GPSLog(Base):
    __tablename__ = 'gps_logs'
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer, ForeignKey("trips.id"))
    latitude = Column(Float)
    longitude = Column(Float)

class Deviation(Base):
    __tablename__ = 'deviations'
    id = Column(Integer, primary_key=True)
    trip_id = Column(Integer)
    lat = Column(Float)
    lon = Column(Float)
    reason = Column(String)