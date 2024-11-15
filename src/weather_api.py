import requests  # Library to make HTTP requests
from config import API_KEY, BASE_URL, CITIES  # Importing configurations
from database import insert_weather_data  # Importing insert function

def get_weather_data(city: str) -> dict:
    """Fetches weather data for a specific city.

    Args:
        city (str): The name of the city for which to fetch weather data.

    Returns:
        dict: A dictionary containing weather data if successful; None if failed.
    """
    # Construct the complete API endpoint for the given city
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # Metric = Celsius

    # Debug: Printing the constructed URL
    print(f"Fetching weather data from: {url}")

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Extract relevant fields from the response
        weather_main = data["weather"][0]["main"]  # e.g., "Rain"
        temp = data["main"]["temp"]  # e.g., 30.5
        feels_like = data["main"]["feels_like"]  # e.g., 32.1
        timestamp = data["dt"]  # Unix timestamp

        # Return the parsed data as a dictionary
        weather_data = {
            "city": city,
            "weather_main": weather_main,
            "temp": temp,
            "feels_like": feels_like,
            "timestamp": timestamp
        }

        print(f"Data fetched for {city}: {weather_data}")

        # Insert the data into the database
        insert_weather_data(weather_data)
        
        return weather_data  # Return fetched data for further use if needed
    
    else:
        # If the request failed, print an error message and return None
        print(f"Failed to get data for {city}. Status Code: {response.status_code}")
        return None

# Test the function by fetching weather data for all cities
if __name__ == "__main__":
    for city in CITIES:
        get_weather_data(city)  # Fetch and store weather data for each city