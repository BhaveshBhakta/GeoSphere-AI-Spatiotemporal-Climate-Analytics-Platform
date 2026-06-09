import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
} from "react-leaflet";

const ClimateMap = ({ weather }) => {

  if (!weather?.latitude || !weather?.longitude) {
    return null;
  }

  return (
    <div className="map-container">

      <h2>Climate Location Map</h2>

      <MapContainer
        center={[weather.latitude, weather.longitude]}
        zoom={8}
        scrollWheelZoom={true}
        style={{
          height: "500px",
          width: "100%",
          borderRadius: "12px",
          marginTop: "20px",
        }}
      >

        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={[weather.latitude, weather.longitude]}>

          <Popup>

            <div>

              <h3>
                {weather.city}
              </h3>

              <p>
                Temperature: {weather.temperature} °C
              </p>

              <p>
                Humidity: {weather.humidity} %
              </p>

              <p>
                Wind Speed: {weather.wind_speed} km/h
              </p>

            </div>

          </Popup>

        </Marker>

      </MapContainer>

    </div>
  );
};

export default ClimateMap;