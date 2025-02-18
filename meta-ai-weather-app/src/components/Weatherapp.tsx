"use client";
import { useState } from "react";

const WeatherApp = () => {
  const [place, setPlace] = useState("");
  const [weather, setWeather] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchWeather = async () => {
    setWeather(null);
    setError(null);

    try {
      const res = await fetch(`/api/weather?place=${place}`);
      const data = await res.json();

      if (data.error) {
        setError(data.error);
      } else {
        setWeather(data.message);
      }
    } catch {
      setError("Failed to fetch weather.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-4">Meta AI Weather App</h1>
      <input
        type="text"
        placeholder="Enter city with country"
        value={place}
        onChange={(e) => setPlace(e.target.value)}
        className="p-2 border rounded-md mb-2"
      />
      <button
        onClick={fetchWeather}
        className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
      >
        Get Weather
      </button>
      {weather && <p className="mt-4 text-lg">{weather}</p>}
      {error && <p className="mt-4 text-red-500">{error}</p>}
    </div>
  );
};

export default WeatherApp;
