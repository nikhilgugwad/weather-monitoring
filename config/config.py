# API Key for OpenWeatherMap API
API_KEY = "2ee97be830bf48de065739854cb8e914"

# List of cities to monitor
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Time interval for fetching data (in minutes)
FETCH_INTERVAL = 5  # Fetch data every 5 minutes

# Alert thresholds for temperature (in Celsius)
TEMP_THRESHOLD = 35  # Example: Alert if temp exceeds 35°C

# Debug: Printing initial config values to verify
# print("Configurations Loaded:")
# print(f"API_KEY: {API_KEY}")
# print(f"CITIES: {CITIES}")
# print(f"BASE_URL: {BASE_URL}")
# print(f"FETCH_INTERVAL: {FETCH_INTERVAL} minutes")
# print(f"TEMP_THRESHOLD: {TEMP_THRESHOLD}°C")
