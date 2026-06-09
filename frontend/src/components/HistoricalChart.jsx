import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const HistoricalChart = ({ historyData }) => {

  const formattedData = historyData.map((item, index) => ({
    index: index + 1,
    temperature: item.temperature
  }));

  return (
    <div className="chart-container">

      <h2>Historical Temperature Trends</h2>

      <ResponsiveContainer width="100%" height={300}>

        <LineChart data={formattedData}>

          <XAxis dataKey="index" />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="temperature"
            stroke="#4ade80"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  );
};

export default HistoricalChart;