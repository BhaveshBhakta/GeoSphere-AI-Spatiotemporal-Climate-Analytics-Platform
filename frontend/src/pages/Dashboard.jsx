import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import WeatherCard from "../components/WeatherCard";
import ForecastChart from "../components/ForecastChart";
import ClimateMap from "../components/ClimateMap";

import API from "../services/api";

const Dashboard = () => {

  const [weather, setWeather] = useState(null);

  const [city, setCity] = useState("Delhi");

  const [inputCity, setInputCity] = useState("");

  const fetchWeather = async (selectedCity) => {

    try {

      const response = await API.get(`/weather/${selectedCity}`);

      setWeather(response.data);

    } catch (error) {

      console.error("Error fetching weather:", error);

    }
  };

  useEffect(() => {

    fetchWeather(city);

  }, [city]);

  const handleSearch = () => {

    if (inputCity.trim() !== "") {

      setCity(inputCity);

      setInputCity("");
    }
  };

  return (
    <div>

      <Navbar />

      <div className="dashboard-container">

        <div className="search-bar">

          <input
            type="text"
            placeholder="Search city..."
            value={inputCity}
            onChange={(e) => setInputCity(e.target.value)}
          />

          <button onClick={handleSearch}>
            Search
          </button>

        </div>

        <h2 className="location-title">
          {weather?.city}, {weather?.country}
        </h2>

        <div className="card-grid">

          <WeatherCard
            title="Temperature"
            value={`${weather?.temperature || "--"} °C`}
          />

          <WeatherCard
            title="Humidity"
            value={`${weather?.humidity || "--"} %`}
          />

          <WeatherCard
            title="Rainfall"
            value={`${weather?.rainfall || "--"} mm`}
          />

          <WeatherCard
            title="Wind Speed"
            value={`${weather?.wind_speed || "--"} km/h`}
          />

        </div>

        <ForecastChart
          forecastData={weather?.forecast || []}
        />

        <ClimateMap />

      </div>

    </div>
  );
};

export default Dashboard;