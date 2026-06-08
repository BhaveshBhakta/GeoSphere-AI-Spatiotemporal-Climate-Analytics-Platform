import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const ForecastChart = ({ forecastData }) => {

  return (
    <div className="chart-container">

      <h2>7-Day Temperature Forecast</h2>

      <ResponsiveContainer width="100%" height={300}>

        <LineChart data={forecastData}>

          <XAxis dataKey="day" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="temp"
            stroke="#00bcd4"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
};

export default ForecastChart;