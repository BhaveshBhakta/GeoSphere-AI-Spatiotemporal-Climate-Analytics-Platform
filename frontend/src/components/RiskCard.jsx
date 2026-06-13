const RiskCard = ({ score }) => {

  return (

    <div className="weather-card">

      <h3>
        Climate Risk Score
      </h3>

      <h2>
        {score}
      </h2>

      <p>/100</p>

    </div>

  );

};

export default RiskCard;