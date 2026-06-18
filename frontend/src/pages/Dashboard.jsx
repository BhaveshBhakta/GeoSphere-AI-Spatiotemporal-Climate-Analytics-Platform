import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import WeatherCard from "../components/WeatherCard";
import ForecastChart from "../components/ForecastChart";
import ClimateMap from "../components/ClimateMap";
import HistoricalChart from "../components/HistoricalChart";
import RiskTrendChart from "../components/RiskTrendChart";
import ClimateAssistant from "../components/ClimateAssistant";
import DocumentAssistant from "../components/DocumentAssistant";
import ReportGenerator from "../components/ReportGenerator";
import RiskCard from "../components/RiskCard";
import AlertBanner from "../components/AlertBanner";
import ClimateInsights from "../components/ClimateInsights";

import API from "../services/api";

const Dashboard = () => {

  const [weather, setWeather] = useState(null);

  const [riskScore, setRiskScore] = useState(null);

  const [riskHistory, setRiskHistory] = useState([]);

  const [alerts, setAlerts] = useState([]);

  const [historyData, setHistoryData] = useState([]);

  const [predictions, setPredictions] = useState({
    lstm: null,
    xgboost: null
  });

  const [city, setCity] = useState("Delhi");

  const [inputCity, setInputCity] = useState("");

  const fetchWeather = async (selectedCity) => {

    try {

      // Weather
      const weatherResponse = await API.get(
        `/weather/${selectedCity}`
      );

      setWeather(weatherResponse.data);

      // Historical Data
      const historyResponse = await API.get(
        `/history/${selectedCity}`
      );

      setHistoryData(
        historyResponse.data
      );

      // Forecast
      const predictionResponse = await API.get(
        "/predict"
      );

      setPredictions({
        lstm:
          predictionResponse.data
            .lstm_prediction,

        xgboost:
          predictionResponse.data
            .xgboost_prediction
      });

      // Risk Score
      const riskResponse = await API.get(
        `/risk/${selectedCity}`
      );

      setRiskScore(
        riskResponse.data
          .risk_report
          .overall_score
      );

      // Risk History
      const riskHistoryResponse =
        await API.get(
          `/risk-history/${selectedCity}`
        );

      setRiskHistory(
        riskHistoryResponse.data
      );

      // Alerts

      const alertsResponse =
        await API.get(
          `/alerts/${selectedCity}`
        );

      setAlerts(
        alertsResponse.data.alerts
      );

    } catch (error) {

      console.error(
        "Error fetching dashboard data:",
        error
      );

    }
  };

  useEffect(() => {

    fetchWeather(city);

  }, [city]);

  const handleSearch = () => {

    if (inputCity.trim()) {

      setCity(inputCity);

      setInputCity("");

    }
  };

  return (

    <div>

      <Navbar />

      <div className="dashboard-container">

        {/* Search */}

        <div className="search-bar">

          <input
            type="text"
            placeholder="Search city..."
            value={inputCity}
            onChange={(e) =>
              setInputCity(
                e.target.value
              )
            }
          />

          <button
            onClick={handleSearch}
          >
            Search
          </button>

        </div>

        {/* City */}

        <h2 className="location-title">

          {weather?.city},
          {" "}
          {weather?.country}

        </h2>

        <AlertBanner alerts={alerts}/>

        {/* Climate Insight */}

        <ClimateInsights city={city}/>

        {/* Metrics */}

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

          <WeatherCard
            title="PM2.5"
            value={`${weather?.pm25 || "--"}`}
          />

          <WeatherCard
            title="AQI Risk"
            value={`${weather?.aqi_risk || "--"}`}
          />

          <WeatherCard
            title="LSTM Forecast"
            value={`${predictions.lstm?.toFixed(1) || "--"} °C`}
          />

          <WeatherCard
            title="XGBoost Forecast"
            value={`${predictions.xgboost?.toFixed(1) || "--"} °C`}
          />

          <RiskCard
            score={riskScore || "--"}
          />

        </div>

        {/* Forecast */}

        <ForecastChart
          forecastData={
            weather?.forecast || []
          }
        />

        {/* Historical Weather */}

        <HistoricalChart
          historyData={historyData}
        />

        {/* Risk Trend */}

        <RiskTrendChart
          data={riskHistory}
        />

        {/* Map */}

        <ClimateMap
          weather={weather}
        />

        {/* AI Section */}

        <div className="assistant-section">

          <ClimateAssistant
            city={city}
          />

          <DocumentAssistant />

        </div>

        {/* Report */}

        <div className="report-section">

          <ReportGenerator
            city={city}
          />

        </div>

      </div>

    </div>

  );
};

export default Dashboard;