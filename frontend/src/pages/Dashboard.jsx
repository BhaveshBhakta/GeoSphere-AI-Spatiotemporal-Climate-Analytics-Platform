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

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [predictions, setPredictions] = useState({
    lstm: null,
    xgboost: null
  });

  const [city, setCity] = useState("Delhi");

  const [inputCity, setInputCity] = useState("");

  const fetchWeather = async (selectedCity) => {

    try {

      setLoading(true);

      setError("");

      const [

        weatherResponse,

        historyResponse,

        predictionResponse,

        riskResponse,

        riskHistoryResponse,

        alertsResponse

      ] = await Promise.all([

        API.get(
          `/weather/${selectedCity}`
        ),

        API.get(
          `/history/${selectedCity}`
        ),

        API.get(
          "/predict"
        ),

        API.get(
          `/risk/${selectedCity}`
        ),

        API.get(
          `/risk-history/${selectedCity}`
        ),

        API.get(
          `/alerts/${selectedCity}`
        )

      ]);

      setWeather(
        weatherResponse.data
      );

      setHistoryData(
        historyResponse.data
      );

      setPredictions({

        lstm:
          predictionResponse.data
            .lstm_prediction,

        xgboost:
          predictionResponse.data
            .xgboost_prediction

      });

      setRiskScore(

        riskResponse.data
          .risk_report
          .overall_score

      );

      setRiskHistory(
        riskHistoryResponse.data
      );

      setAlerts(
        alertsResponse.data.alerts
      );

    } catch (error) {

      console.error(error);

      setError(
        "Unable to load climate data."
      );

    } finally {

      setLoading(false);

    }
  };

  useEffect(() => {

    fetchWeather(city);

  }, [city]);

  const handleSearch = () => {

    if (!inputCity.trim())
      return;

    setCity(inputCity);

    setInputCity("");

  };

  if (loading) {

    return (

      <div>

        <Navbar />

        <div
          className="dashboard-container"
        >

          <h2>
            Loading Climate Data...
          </h2>

        </div>

      </div>

    );
  }

  if (error) {

    return (

      <div>

        <Navbar />

        <div
          className="dashboard-container"
        >

          <h2>
            {error}
          </h2>

        </div>

      </div>

    );
  }

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

        {/* Alerts */}

        <AlertBanner
          alerts={alerts}
        />

        {/* AI Insights */}

        <ClimateInsights
          city={city}
        />

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

        {/* Climate Map */}

        <ClimateMap
          weather={weather}
        />

        {/* AI Tools */}

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