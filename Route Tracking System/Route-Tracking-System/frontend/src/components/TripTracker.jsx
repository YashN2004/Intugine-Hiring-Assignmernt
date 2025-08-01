import { useEffect, useState } from 'react';

export default function TripTracker({ tripId }) {
  const [position, setPosition] = useState({ lat: 0, lng: 0 });

  useEffect(() => {
    const interval = setInterval(async () => {
      // Simulated or real GPS update
      const res = await fetch(/update-location?trip_id=${tripId}&latitude=18.5&longitude=73.8, { method: 'POST' });
      const data = await res.json();
      console.log(data);
    }, 5000);

    return () => clearInterval(interval);
  }, [tripId]);

  return <p>Tracking Trip #{tripId}...</p>;
}