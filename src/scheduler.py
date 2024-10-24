import schedule
import time
import json
from alerts import check_alerts 
from database import calculate_daily_summary, insert_weather_data # Functions from database.py

def load_config():
    """Load the user configuration from config.json."""
    with open("src/config.json", "r") as config_file:
        config = json.load(config_file)
    return config


def job_manual_insert(city):
    """Simulate manual data insertion into the weather database."""
    data = {
        "city": city,
        "weather_main": "Clear",
        "temp": 32.5,
        "feels_like": 34.0,
        "timestamp": int(time.time()) # Current Unix timestamp
    }
    print(f"Inserting weather data: {data}")
    insert_weather_data(data) # Insert the data using database.py

def job_check_alerts():
    """Check for temperature alerts."""
    print("Checking temperature alerts...")
    print(check_alerts())

def job_update_summary(city):
    """Update daily summary for the city at the end of the day."""
    print(f"Updating daily summary for {city}...")
    date = time.strftime("%Y-%m-%d") # Get today's date in YYYY-MM-DD format
    calculate_daily_summary(city, date) # Update the summary

def scheduler():
    """Main function to schedule jobs and start the scheduler."""
    config = load_config() # Load configuration from config.json
    city = config["alert_city"]  # City to monitor
    
    # Schedule jobs
    schedule.every(1).minutes.do(job_manual_insert, city)  # Insert weather data
    schedule.every(1).minutes.do(job_check_alerts) # Check alerts
    schedule.every().day.at("23:59").do(job_update_summary, city)  # Update summary

    print("Scheduler started. Press Ctrl+C to stop.")

    # Keep the script running to execute scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1) # Wait 1 second between checks

# Run the main function when the script is executed
if __name__ == "__main__":
    scheduler()

