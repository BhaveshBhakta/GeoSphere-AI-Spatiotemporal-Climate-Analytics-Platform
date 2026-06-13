import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const RiskTrendChart = ({
  data
}) => {

  return (

    <div
      className="chart-container"
    >

      <h3>
        Climate Risk Trend
      </h3>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <LineChart data={data}>

          <XAxis
            dataKey="date"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="risk_score"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>

  );
};

export default RiskTrendChart;