"""
This module checks for temperature alerts in a specified city.

It retrieves the latest weather data for the city and compares the temperature
with a user-defined threshold. If the temperature exceeds the threshold,
an alert message is printed.
"""

from database import get_latest_weather_data
from config import TEMP_THRESHOLD

def check_alerts(city: str) -> None:
    """
    Checks for temperature alerts in the given city.

    Retrieves the latest weather data and compares the most recent temperatures
    against a predefined threshold. Alerts are printed if the temperature
    exceeds the threshold.

    Args:
        city (str): The name of the city for which to check alerts.

    Returns:
        None
    """
    
    # Retrieve the latest weather updates for the specified city
    latest_updates = get_latest_weather_data(city)

    # Check if sufficient data is available
    if not latest_updates or len(latest_updates) < 2:
        print(f"Not enough weather data for {city}.")
        return

    # Unpack the most recent temperature readings
    most_recent_temp, _ = latest_updates[0]
    second_recent_temp, _ = latest_updates[1]

    print(f"Latest temperature for {city}: {most_recent_temp}°C")

    # Check if the most recent temperature exceeds the threshold
    if most_recent_temp > TEMP_THRESHOLD:
        print(f"Temperature breach detected for {city}: {most_recent_temp}°C")

        # Check for consecutive breaches
        if second_recent_temp > TEMP_THRESHOLD:
            print(f"⚠️ ALERT: {city} temperature has exceeded {TEMP_THRESHOLD}°C for 2 consecutive updates!")

if __name__ == "__main__":
    # Example usage of the check_alerts function
    check_alerts("New York")