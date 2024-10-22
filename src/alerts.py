from database import get_latest_weather_data

latest_updates = get_latest_weather_data("Delhi")
if latest_updates:
    temp1, time1 = latest_updates[0]  # Most recent entry
    temp2, time2 = latest_updates[1]  # Second most recent entry

    print(f"Latest temperature for Delhi: {temp1}°C")
    if temp1 > 35:
        print(f"Temperature breach detected for Delhi: {temp1}°C")

    # Check if both entries exceed the threshold
    if temp1 > 35 and temp2 > 35:
        print(f"⚠️ ALERT: Delhi temperature has exceeded 35.0°C for 2 consecutive updates!")
else:
    print("Not enough weather data for Delhi.")
