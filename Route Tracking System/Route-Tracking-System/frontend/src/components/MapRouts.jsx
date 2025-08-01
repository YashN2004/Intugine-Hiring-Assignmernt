import { useState } from 'react';
import { GoogleMap, Polyline, useJsApiLoader } from '@react-google-maps/api';

export default function MapRoute() {
  const [path, setPath] = useState([]);
  const { isLoaded } = useJsApiLoader({ googleMapsApiKey: process.env.REACT_APP_GOOGLE_API_KEY });

  const handleClick = (e) => {
    setPath([...path, { lat: e.latLng.lat(), lng: e.latLng.lng() }]);
  };

  const saveRoute = async () => {
    const res = await fetch('/add-route', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source: 'City A', destination: 'City B', waypoints: path })
    });
    alert('Route saved!');
  };

  return isLoaded && (
    <GoogleMap mapContainerStyle={{ height: "400px", width: "100%" }} center={{ lat: 18.5, lng: 73.8 }} zoom={7} onClick={handleClick}>
      <Polyline path={path} options={{ strokeColor: "#ff2527", strokeWeight: 2 }} />
      <button onClick={saveRoute}>Save Route</button>
    </GoogleMap>
  );
}