import MapRoute from './components/MapRoute';
import TripTracker from './components/TripTracker';

function App() {
  return (
    <div className="p-5">
      <h1 className="text-xl font-bold mb-4">Route Deviation Tracker</h1>
      <MapRoute />
      <TripTracker tripId={1} />
    </div>
  );
}

export default App;