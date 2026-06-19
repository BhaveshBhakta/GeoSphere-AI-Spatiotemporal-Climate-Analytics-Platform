import { useState } from "react";

import API from "../services/api";

const CityComparison = () => {

    const [city1, setCity1] =
        useState("Delhi");

    const [city2, setCity2] =
        useState("Mumbai");

    const [comparison, setComparison] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const compareCities = async () => {

        setLoading(true);

        try {

            const response =
                await API.get(
                    `/compare/${city1}/${city2}`
                );

            setComparison(
                response.data
            );

        } catch (error) {

            console.error(error);

            setComparison(
                "Comparison failed."
            );

        }

        setLoading(false);
    };

    return (

        <div className="comparison-container">

            <h2>
                City Climate Comparison
            </h2>

            <div>

                <input
                    type="text"
                    placeholder="City 1"
                    value={city1}
                    onChange={(e) =>
                        setCity1(
                            e.target.value
                        )
                    }
                />

                <input
                    type="text"
                    placeholder="City 2"
                    value={city2}
                    onChange={(e) =>
                        setCity2(
                            e.target.value
                        )
                    }
                />

                <button
                    onClick={compareCities}
                >
                    Compare
                </button>

            </div>

            {loading && (
                <p>
                    Comparing...
                </p>
            )}

            {
                comparison && (

                    <div>

                        <h3>
                            Comparison Results
                        </h3>

                        <div>

                            <h4>
                                {comparison.city1}
                            </h4>

                            <p>
                                Temperature:
                                {" "}
                                {
                                    comparison.weather1.temperature
                                }°C
                            </p>

                            <p>
                                AQI:
                                {" "}
                                {
                                    comparison.weather1.aqi_risk
                                }
                            </p>

                            <p>
                                Risk Score:
                                {" "}
                                {
                                    comparison.risk1
                                        .overall_score
                                }
                            </p>

                        </div>

                        <div>

                            <h4>
                                {comparison.city2}
                            </h4>

                            <p>
                                Temperature:
                                {" "}
                                {
                                    comparison.weather2.temperature
                                }°C
                            </p>

                            <p>
                                AQI:
                                {" "}
                                {
                                    comparison.weather2.aqi_risk
                                }
                            </p>

                            <p>
                                Risk Score:
                                {" "}
                                {
                                    comparison.risk2
                                        .overall_score
                                }
                            </p>

                        </div>

                        <h3>
                            AI Climate Analysis
                        </h3>

                        <p>
                            {
                                comparison.analysis
                            }
                        </p>

                    </div>

                )
            }

        </div>

    );
};

export default CityComparison;