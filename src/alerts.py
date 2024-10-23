import json
from database import get_latest_weather_data

with open("src/config.json", "r") as config_file:
    config = json.load(config_file)

threshold = config["temperature_threshold"]
alert_city = config["alert_city"]

latest_updates = get_latest_weather_data(alert_city)
if latest_updates:
    temp1, time1 = latest_updates[0]  # Most recent entry
    temp2, time2 = latest_updates[1]  # Second most recent entry

    print(f"Latest temperature for {alert_city}: {temp1}°C")
    if temp1 > threshold:
        print(f"Temperature breach detected for {alert_city}: {temp1}°C")

    # Check if both entries exceed the threshold
    if temp1 > threshold and temp2 > threshold:
        print(f"⚠️ ALERT: {alert_city} temperature has exceeded {threshold}°C for 2 consecutive updates!")
else:
    print(f"Not enough weather data for {alert_city}.")
