import sqlite3  # SQLite library to interact with the database

DB_NAME = "weather.db"  # Database file name

def create_table():
    """Create the weather_data table if it doesn't exist."""
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
    conn.commit()  # Commit the changes
    conn.close()  # Close the database connection

    print("Database and table created successfully.")

def insert_weather_data(data):
    """Insert a weather data record into the weather_data table."""
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

# Test the database setup
if __name__ == "__main__":
    create_table()  # Create the table when the script is run
