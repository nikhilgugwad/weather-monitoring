import schedule
import time
from alerts import check_alerts
from database import calculate_daily_summary, insert_weather_data
from weather_api import get_weather_data

def job_manual_insert(city: str) -> None:
    """Simulate manual data insertion into the weather database.

    Args:
        city (str): The name of the city for which to insert weather data.
    """
    print(f"Inserting weather data for {city}...")
    weather_data = get_weather_data(city)
    if weather_data:
        insert_weather_data(weather_data)  # Insert the data using database.py
    else:
        print(f"No weather data retrieved for {city}.")

def job_check_alerts(city: str) -> None:
    """Check for temperature alerts in the specified city.

    Args:
        city (str): The name of the city to check for alerts.
    """
    print("Checking temperature alerts...")
    check_alerts(city)  # Check alerts and print results

def job_update_summary(city: str) -> None:
    """Update the daily summary for the specified city.

    Args:
        city (str): The name of the city for which to update the summary.
    """
    print(f"Updating daily summary for {city}...")
    date = time.strftime("%Y-%m-%d")  # Get today's date in YYYY-MM-DD format
    calculate_daily_summary(city, date)  # Update the summary

def scheduler(city: str) -> None:
    """Schedule jobs for weather data management.

    Args:
        city (str): The name of the city to manage.
    """
    
    # Schedule jobs
    schedule.every(5).minutes.do(job_manual_insert, city)  # Insert weather data
    schedule.every(5).minutes.do(job_check_alerts, city)  # Check alerts
    schedule.every().day.at("23:59").do(job_update_summary, city)  # Update summary

    print("Scheduler started. Press Ctrl+C to stop.")

    # Keep the script running to execute scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait 1 second between checks

# Run the main function when the script is executed
if __name__ == "__main__":
    scheduler("Delhi")