import { useEffect, useState } from "react";

import API from "../services/api";

const ClimateInsights = ({
  city
}) => {

  const [insights, setInsights] =
    useState("");

  useEffect(() => {

    const loadInsights =
      async () => {

        try {

          const response =
            await API.get(
              `/insights/${city}`
            );

          setInsights(
            response.data.insights
          );

        } catch (error) {

          console.error(error);

        }
      };

    loadInsights();

  }, [city]);

  return (

    <div
      className="insights-card"
    >

      <h2>
        AI Climate Insights
      </h2>

      <pre>
        {insights}
      </pre>

    </div>

  );
};

export default ClimateInsights;