# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Table of Contents
1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Tech Stack Used](#tech-stack-used)
4. [Installation Instructions](#installation-instructions)
5. [Usage](#usage)
6. [Module Descriptions](#module-descriptions)
   - [alerts.py](#alertspy)
   - [config.py](#configpy)
   - [database.py](#databasepy)
   - [scheduler.py](#schedulerpy)
   - [visualizations.py](#visualizationspy)
   - [weather_api.py](#weather_apipy)
7. [Features](#features)
8. [Future Improvements](#future-improvements)
9. [Collaborations](#collaborations)

## Introduction

The **Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates** project is a Python-based application designed to monitor and analyze weather conditions in specified cities. It retrieves real-time weather data from an external API, stores this information in a local SQLite database, and provides various functionalities such as temperature alerts and visualizations of weather trends over time. The goal of this project is to empower users with insights into weather patterns, helping them make informed decisions based on current and historical weather data.

## Folder Structure

The project directory is organized as follows:

```
weather-monitoring/
│
├── src/                    # Source code for the application
│   ├── alerts.py           # Module for checking temperature alerts
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database interactions
│   ├── scheduler.py        # Job scheduling for data fetching and processing
│   ├── visualizations.py    # Data visualization functions
│   └── weather_api.py      # Module for fetching weather data from the API
│
├── .env                    # Environment variables (e.g., API key)
├── .gitignore              # Files and directories to ignore in Git
├── README.md               # Project overview and instructions
├── requirements.txt        # List of Python package dependencies
└── weather.db              # SQLite database file for storing weather data
```

## Tech Stack Used

- **Python**: The primary programming language used for developing the application.
- **SQLite**: A lightweight, serverless database used to store weather data locally.
- **Requests**: A Python library for making HTTP requests to fetch weather data from an external API.
- **Matplotlib**: A plotting library used for creating visualizations of weather trends.
- **Schedule**: A library for scheduling periodic tasks, such as fetching new weather data.
- **dotenv**: A library for loading environment variables from a `.env` file.

## Installation Instructions

To set up the Weather Monitoring project on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather-monitoring.git
   cd weather-monitoring
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv  # Create a virtual environment named 'venv'
   source venv/bin/activate  # Activate on macOS/Linux
   .\venv\Scripts\activate  # Activate on Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt  # Install required packages listed in requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory if it does not exist.
   - Add your API key to the `.env` file:
     ```
     API_KEY=your_api_key_here
     ```

5. **Initialize the Database**:
   - Run the `src/database.py` script to create the necessary tables in `weather.db`:
     ```bash
     python src/database.py
     ```

## Usage

To use the Weather Monitoring application, follow these steps:

1. **Run the Scheduler**:
   - Start the scheduler to begin fetching and processing weather data:
     ```bash
     python src/scheduler.py  # Replace "Delhi" with any city you want to monitor.
     ```

2. **Visualize Weather Data**:
   - You can visualize temperature trends, dominant weather conditions, and alerts by running the respective functions in `src/visualizations.py`:
     ```bash
     python src/visualizations.py  # Uncomment desired plot function calls at the bottom of the script.
     ```

3. **Check Alerts**:
   - The application will automatically check for temperature alerts based on predefined thresholds.

## Module Descriptions

### alerts.py

This module is responsible for checking temperature alerts based on predefined thresholds.

- **Functions**:
  - `check_alerts(city: str) -> None`: 
    - Retrieves the latest weather data for a specified city from the database.
    - Compares current temperatures against a threshold defined in `config.py`.
    - Prints alert messages if temperatures exceed the threshold or if there are consecutive breaches.

### config.py

This module defines configuration variables used throughout the application.

- **Functions**:
  - `load_config() -> dict`: 
    - Loads configuration variables from environment variables and sets default values.
    - Returns a dictionary containing all configuration variables such as API keys, cities to monitor, base URL for API requests, fetch intervals, and temperature thresholds.

### database.py

This module handles all interactions with the SQLite database.

- **Functions**:
  - `create_table() -> None`: 
    - Creates necessary tables (`weather_data` and `daily_summary`) in the SQLite database if they do not already exist.
  
  - `calculate_daily_summary(city: str, date: str) -> Optional[None]`: 
    - Computes daily summaries (average, max, min temperatures) for a specified city and date based on stored weather data.
  
  - `get_daily_summary(city: str, date: Optional[str] = None) -> Optional[List[tuple]]`: 
    - Retrieves daily summary records from the database for a specific city and optional date.
  
  - `insert_weather_data(data: dict) -> None`: 
    - Inserts new weather data records into the `weather_data` table.
  
  - `get_latest_weather_data(city: str) -> Optional[List[tuple]]`: 
    - Fetches the latest two entries of weather data for a specified city from the database.

### scheduler.py

This module manages scheduled tasks for fetching and processing weather data.

- **Functions**:
  - `job_manual_insert(city: str) -> None`: 
    - Fetches current weather data for a specified city using the `get_weather_data` function from `weather_api.py` and inserts it into the database.
  
  - `job_check_alerts(city: str) -> None`: 
    - Checks for temperature alerts by invoking `check_alerts` from `alerts.py`.
  
  - `job_update_summary(city: str) -> None`: 
    - Updates daily summaries by calculating them at a specific time each day (23:59).
  
  - `scheduler(city: str) -> None`: 
    - Schedules jobs to run periodically (every 5 minutes) or at specific times (daily summary update).

### visualizations.py

This module is responsible for visualizing weather data using Matplotlib.

- **Functions**:
  - `plot_temperature_trend(city: str) -> None`: 
    - Visualizes average, max, and min temperature trends over time using line plots.
  
  - `plot_dominant_weather(city: str) -> None`: 
    - Creates a bar chart showing dominant weather conditions based on historical data stored in the database.
  
  - `plot_alerts_timeline(city: str) -> None`: 
    - Plots a timeline indicating when temperature alerts were triggered for a specified city.

### weather_api.py

This module handles interactions with the external weather API to fetch current weather data.

- **Functions**:
  - `get_weather_data(city: str) -> dict`: 
    - Constructs an API request URL using parameters such as city name and API key.
    - Sends an HTTP GET request to retrieve current weather data.
    - Parses and returns relevant fields (temperature, feels like temperature, main weather condition).
    - Inserts fetched data into the database using `insert_weather_data`.

## Features

- Fetches real-time weather data from an external API.
- Stores historical weather data in a local SQLite database.
- Provides temperature alerts when thresholds are exceeded.
- Visualizes temperature trends, dominant weather conditions, and alert timelines using Matplotlib.

## Future Improvements

Here are some potential improvements that could be made to enhance the functionality of this project:

- **User Interface (UI)**: Develop a web or desktop UI for easier interaction with the application.
- **Notifications**: Implement a notification system (e.g., email or SMS) to alert users when certain conditions are met.
- **Extended Forecasts**: Integrate additional APIs to provide extended weather forecasts beyond current conditions.
- **Data Analysis**: Include more advanced data analysis features, such as predictive modeling based on historical data.

## Collaborations

This project is open for collaborations! If you would like to contribute, please fork the repository, make your changes, and submit a pull request. Contributions can include bug fixes, new features, documentation improvements, or anything else that enhances the project.