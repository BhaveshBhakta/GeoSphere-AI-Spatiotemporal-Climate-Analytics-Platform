import API from "../services/api";

const ReportGenerator = ({
  city
}) => {

  const generateReport =
    async () => {

      try {

        const response =
          await API.get(
            `/report/${city}`
          );

        alert(
          response.data.message
        );

      } catch (error) {

        console.error(error);

      }
    };

  return (

    <button
      className="report-button"
      onClick={generateReport}
    >
      Generate Climate Report
    </button>

  );
};

export default ReportGenerator;