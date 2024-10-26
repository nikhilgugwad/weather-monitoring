from database import get_latest_weather_data
from config import TEMP_THRESHOLD

def check_alerts(city):

    threshold = TEMP_THRESHOLD # User-defined temperature threshold
    alert_city = city  # City to monitor

    # Step 2: Fetch the latest two weather updates for the specified city
    latest_updates = get_latest_weather_data(alert_city)
    if latest_updates:
        temp1, time1 = latest_updates[0]  # Most recent entry
        temp2, time2 = latest_updates[1]  # Second most recent entry
        
        if temp1 > threshold:
            print(f"Temperature breach detected for {alert_city}: {temp1}°C")
        else:
            print(f"No alerts detected, latest temperature for {alert_city}: {temp1}°C")

        # Check if both entries exceed the threshold
        if temp1 > threshold and temp2 > threshold:
            print(f"⚠️ ALERT: {alert_city} temperature has exceeded {threshold}°C for 2 consecutive updates!")
        else:
            print(f"No alerts detected, latest temperature for {alert_city}: {temp1}°C")
    else:
        print(f"Not enough weather data for {alert_city}.")
