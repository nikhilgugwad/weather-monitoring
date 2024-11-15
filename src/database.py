import sqlite3  # SQLite library to interact with the database
from collections import Counter
from typing import List, Dict, Optional

DB_NAME = "weather.db"  # Database file name

def create_table() -> None:
    """Create the weather_data and daily_summary tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)  # Connect to the database (creates it if not exists)
    cursor = conn.cursor()  # Cursor to execute SQL commands

    # SQL query to create the weather_data table
    query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        weather_main TEXT NOT NULL,
        temp REAL NOT NULL,
        feels_like REAL NOT NULL,
        timestamp INTEGER NOT NULL
    )
    """
    cursor.execute(query)  # Execute the query to create the table

    # Create daily_summary table for storing aggregates
    summary_query = """
    CREATE TABLE IF NOT EXISTS daily_summary (
        date TEXT PRIMARY KEY,
        city TEXT NOT NULL,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_weather TEXT
    )
    """
    cursor.execute(summary_query)

    conn.commit()  # Commit the changes
    conn.close()  # Close the database connection
    print("Databases and tables created successfully.")

def calculate_daily_summary(city: str, date: str) -> Optional[None]:
    """Calculate and store the daily summary for a given city and date.

    Args:
        city (str): The name of the city.
        date (str): The date in 'YYYY-MM-DD' format.

    Returns:
        None: If successful; prints an error message if no data is found.
    """
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Fetch all weather records for the specified city and date
    query = """
    SELECT temp, weather_main FROM weather_data
    WHERE city = ? AND DATE(timestamp, 'unixepoch') = ?
    """
    cursor.execute(query, (city, date))
    rows = cursor.fetchall()

    # If no data is found, return None
    if not rows:
        print(f"No data found for {city} on {date}")
        return None

    # Calculate min, max, and average temperatures
    temps = [row[0] for row in rows]
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    # Find the dominant weather condition
    weather_conditions = [row[1] for row in rows]
    dominant_weather = Counter(weather_conditions).most_common(1)[0][0]

    # Insert or update the summary into the daily_summary table
    insert_query = """
    INSERT INTO daily_summary (date, city, avg_temp, max_temp, min_temp, dominant_weather)
    VALUES (?, ?, ?, ?, ?, ?)
    ON CONFLICT(date) DO UPDATE SET
        avg_temp = excluded.avg_temp,
        max_temp = excluded.max_temp,
        min_temp = excluded.min_temp,
        dominant_weather = excluded.dominant_weather
    """
    
    cursor.execute(insert_query, (date, city, avg_temp, max_temp, min_temp, dominant_weather))
    
    conn.commit()
    conn.close()

def get_daily_summary(city: str, date: Optional[str] = None) -> Optional[List[tuple]]:
    """Retrieve the daily summary for a specific city and optional date.

    Args:
        city (str): The name of the city.
        date (str, optional): The date in 'YYYY-MM-DD' format. If None, fetches all summaries for the city.

    Returns:
        List[tuple]: A list of tuples containing summary data if found; otherwise None.
    """
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if date:
        # If a specific date is provided, search for that date
        query = "SELECT * FROM daily_summary WHERE city = ? AND date = ?"
        cursor.execute(query, (city, date))
    else:
        # If no date is provided, fetch all summaries for the city
        query = "SELECT * FROM daily_summary WHERE city = ?"
        cursor.execute(query, (city,))

    summary = cursor.fetchall()  # Use fetchall() to get multiple rows
    conn.close()

    if summary:
        print(f"Found {len(summary)} summaries for {city}.")
        return summary
    else:
        print(f"No summary found for {city}.")
        return None

def insert_weather_data(data: Dict[str, str]) -> None:
    """Insert a weather data record into the weather_data table.

    Args:
        data (dict): A dictionary containing weather data with keys 
                     'city', 'weather_main', 'temp', 'feels_like', and 'timestamp'.

    Returns:
        None: Prints a success message upon successful insertion.
    """
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # SQL query to insert data into the table
    query = """
    INSERT INTO weather_data (city, weather_main, temp, feels_like, timestamp)
    VALUES (?, ?, ?, ?, ?)
    """

   # Debug: Print the values being inserted
    print(f"Inserting data: {data}")

   # Execute the query with data values
    cursor.execute(query, (data["city"], data["weather_main"], data["temp"], data["feels_like"], data["timestamp"]))
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

    print(f"Data for {data['city']} inserted successfully.")

def get_latest_weather_data(city: str) -> Optional[List[tuple]]:
   """Retrieve the latest two weather data entries for a specific city.

   Args:
       city (str): The name of the city.

   Returns:
       List[tuple]: A list of tuples containing temperature and timestamp 
                    if two entries are found; otherwise None.
   """
   
   conn = sqlite3.connect(DB_NAME)
   cursor = conn.cursor()

   query = """
   SELECT temp, timestamp FROM weather_data
   WHERE city = ?
   ORDER BY timestamp DESC LIMIT 2
   """
   cursor.execute(query, (city,))
   rows = cursor.fetchall()  # Fetch two latest rows
   conn.close()

   return rows if len(rows) == 2 else None

# Test the database setup and functions when this script is run directly.
if __name__ == "__main__":
   create_table()  # Create the tables when the script is run
   calculate_daily_summary("Delhi", "2024-10-24")  # Example test case
   print(get_daily_summary("Delhi"))  # Print available summaries for verification