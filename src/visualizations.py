import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sqlite3
from database import get_daily_summary, DB_NAME

def plot_temperature_trend(city: str) -> None:
    """Visualize average, max, and min temperature trends for a city.

    Args:
        city (str): The name of the city for which to plot temperature trends.
    """
    # Fetch all daily weather summaries for the city
    summaries = get_daily_summary(city)
    
    if not summaries:
        print(f"No weather summary available for {city}.")
        return
    
    # Extract data for plotting
    dates = [entry[0] for entry in summaries]  # Assuming date is the 0th column
    avg_temps = [entry[2] for entry in summaries]  # Assuming avg_temp is the 2nd column
    max_temps = [entry[3] for entry in summaries]  # Assuming max_temp is the 3rd column
    min_temps = [entry[4] for entry in summaries]  # Assuming min_temp is the 4th column

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, avg_temps, label='Average Temp (°C)', marker='o', color='b')
    plt.plot(dates, max_temps, label='Max Temp (°C)', marker='o', color='r')
    plt.plot(dates, min_temps, label='Min Temp (°C)', marker='o', color='g')

    # Customize the plot
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Trend for {city}')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    # Display the plot
    plt.tight_layout()
    plt.show()

def plot_dominant_weather(city: str) -> None:
    """Plot a bar chart of dominant weather conditions.

    Args:
        city (str): The name of the city for which to plot dominant weather conditions.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Retrieve the dominant weather condition and count per day
    query = """
    SELECT dominant_weather, COUNT(dominant_weather)
    FROM daily_summary
    WHERE city = ?
    GROUP BY dominant_weather
    ORDER BY COUNT(dominant_weather) DESC
    """
    
    cursor.execute(query, (city,))
    data = cursor.fetchall()
    
    conn.close()

    if not data:
        print(f"No dominant weather data available for {city}.")
        return

    # Prepare data for plotting
    conditions = [row[0] for row in data]
    counts = [row[1] for row in data]

    # Plot the bar chart
    plt.bar(conditions, counts, color='skyblue')
    plt.xlabel('Weather Condition')
    plt.ylabel('Count')
    plt.title(f'Dominant Weather Conditions in {city}')
    
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    
    plt.show()

def plot_alerts_timeline(city: str) -> None:
    """Plot a timeline showing the dates when alerts were triggered.

    Args:
        city (str): The name of the city for which to plot alert timelines.
    """
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Retrieve dates of alerts for the given city
    query = """
    SELECT date FROM daily_summary WHERE city = ?
    """
    
    cursor.execute(query, (city,))
    
    data = cursor.fetchall()
    
    conn.close()

    if not data:
        print(f"No alert data available for {city}.")
        return

    # Prepare data for plotting
    alert_dates = [row[0] for row in data]
    alert_dates_numeric = [mdates.datestr2num(date) for date in alert_dates]

    # Plot the timeline 
    fig, ax = plt.subplots()
    ax.plot(alert_dates_numeric, [1] * len(alert_dates_numeric), 'r|', markersize=12)  # Red markers for alerts
    ax.set_yticks([])  # Hide y-axis ticks
    ax.set_title(f'Temperature Alerts Timeline for {city}')
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    plt.show()

# Call the function with the city name when this script is executed directly.
if __name__ == "__main__":
   # Uncomment one of the following lines to visualize data for "Delhi".
   # plot_temperature_trend("Delhi")
   # plot_dominant_weather("Delhi") 
   plot_alerts_timeline("Delhi") 