import schedule
import time
from alerts import check_alerts 
from database import calculate_daily_summary, insert_weather_data # Functions from database.py
from weather_api import get_weather_data

def job_manual_insert(city):
    """Simulate manual data insertion into the weather database."""
    print(f"Inserting weather data of {city}")
    weather_data = get_weather_data(city)
    if weather_data:
        insert_weather_data(weather_data) # Insert the data using database.py

def job_check_alerts(city):
    """Check for temperature alerts."""
    print("Checking temperature alerts...")
    print(check_alerts(city))

def job_update_summary(city):
    """Update daily summary for the city at the end of the day."""
    print(f"Updating daily summary for {city}...")
    date = time.strftime("%Y-%m-%d") # Get today's date in YYYY-MM-DD format
    calculate_daily_summary(city, date) # Update the summary

def scheduler(city):
    
    # Schedule jobs
    schedule.every(5).minutes.do(job_manual_insert, city)  # Insert weather data
    schedule.every(5).minutes.do(job_check_alerts, city) # Check alerts
    schedule.every().day.at("23:59").do(job_update_summary, city)  # Update summary

    print("Scheduler started. Press Ctrl+C to stop.")

    # Keep the script running to execute scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1) # Wait 1 second between checks

# Run the main function when the script is executed
if __name__ == "__main__":
    scheduler("Delhi")

