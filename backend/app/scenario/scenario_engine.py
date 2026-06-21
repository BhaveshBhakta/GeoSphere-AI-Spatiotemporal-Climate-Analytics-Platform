def apply_scenario(

    weather,

    temp_change=0,

    rainfall_change=0,

    humidity_change=0

):

    simulated = weather.copy()

    simulated["temperature"] += temp_change

    simulated["rainfall"] += rainfall_change

    simulated["humidity"] += humidity_change

    return simulated