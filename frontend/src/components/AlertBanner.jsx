const AlertBanner = ({
  alerts
}) => {

  if (
    !alerts ||
    alerts.length === 0
  ) {

    return null;
  }

  return (

    <div
      className="alert-banner"
    >

      <h3>
        Active Climate Alerts
      </h3>

      {

        alerts.map(
          (
            alert,
            index
          ) => (

            <div
              key={index}
            >

              <strong>
                {alert.type}
              </strong>

              {" - "}

              {alert.message}

            </div>

          )
        )

      }

    </div>

  );
};

export default AlertBanner;