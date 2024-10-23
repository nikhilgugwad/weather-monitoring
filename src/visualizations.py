import matplotlib.pyplot as plt
from database import get_daily_summary

def plot_temperature_trend(city):
    """Visualize average, max, and min temperature trends for a city."""
    # Fetch all daily weather summaries for the city
    summaries = get_daily_summary(city)
    print(summaries) # JJO:JIHOLHIJ
    if not summaries:
        print(f"No weather summary available for {city}.")
        return
    
    # Extract data for plotting
    dates = [entry[0] for entry in summaries] # Assuming date is the 0th column
    avg_temps = [entry[2] for entry in summaries] # Assuming avg_temp is the 2th column
    max_temps = [entry[3] for entry in summaries] # Assuming max_temp is the 3rd column
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

# Call the function with the city name
if __name__ == "__main__":
    plot_temperature_trend("Delhi")
    