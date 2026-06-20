import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const Forecast7Chart = ({
  data
}) => {

  return (

    <div>

      <h2>
        7-Day Forecast
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <LineChart data={data}>

          <XAxis
            dataKey="day"
          />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="temperature"
          />

        </LineChart>

      </ResponsiveContainer>

    </div>

  );
};

export default Forecast7Chart;