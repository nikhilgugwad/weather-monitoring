"""
This module defines configuration variables for the application.

It uses environment variables from a `.env` file for sensitive information
like the API key. It also defines default values for other configurations.
"""

import os
from dotenv import load_dotenv

def load_config() -> dict:
    """
    Loads configuration variables from the environment and the module itself.

    This function retrieves sensitive information from environment variables 
    and sets default values for other configurations.

    Returns:
        dict: A dictionary containing all configuration variables.

    Raises:
        ValueError: If required configuration values are missing or invalid.
    """
    
    load_dotenv()

    # Load configuration variables
    config = {
        "API_KEY": os.getenv("API_KEY"),
        "CITIES": ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"],
        "BASE_URL": "https://api.openweathermap.org/data/2.5/weather",
        "FETCH_INTERVAL": 5,  # Fetch data every 5 minutes (in minutes)
        "TEMP_THRESHOLD": 35,  # Alert if temp exceeds 35°C (in Celsius)
    }

    # Validate required configuration values
    if not config["API_KEY"]:
        raise ValueError("API_KEY must be set in the environment variables.")

    return config

# Load configuration
config = load_config()

# Access configuration values throughout the application
API_KEY = config["API_KEY"]
CITIES = config["CITIES"]
BASE_URL = config["BASE_URL"]
FETCH_INTERVAL = config["FETCH_INTERVAL"]
TEMP_THRESHOLD = config["TEMP_THRESHOLD"]

# Note: Debug printing is removed; consider using a logging library for debugging purposes.