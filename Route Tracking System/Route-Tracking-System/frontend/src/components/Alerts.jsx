export default function Alerts({ message }) {
  return (
    <div className="bg-red-500 text-white p-3 rounded-lg">
      🚨 {message}
    </div>
  );
}