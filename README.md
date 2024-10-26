

## **Project Title and Overview**

### **Project Title**  
**Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates**  

---

### **Project Overview**

#### **Description:**  

This project implements a real-time weather monitoring system that collects, processes, and summarizes weather data from the OpenWeatherMap API. The system focuses on metro cities in India and allows users to define alert thresholds for temperature or weather conditions. 

The data is periodically fetched, aggregated into daily summaries, and stored for historical analysis. Summaries include metrics such as average, maximum, and minimum temperatures, along with the dominant weather condition for each day. Additionally, alert notifications are triggered when user-defined thresholds are breached.

The project supports visualizations to display trends over time, providing insights into historical weather conditions.

#### **Key Objectives:**
- **Real-time monitoring:** Continuously fetch weather data for major cities in India.
- **Rollups and aggregation:** Generate daily summaries with key metrics.
- **Alerts:** Trigger notifications when weather conditions cross defined thresholds.
- **Visualization:** Display trends and insights using graphs.

---

## **Features and Functionalities**

###  **Real-Time Data Retrieval**
- **Description:**  
  The system continuously fetches weather data from the OpenWeatherMap API at a **configurable interval** (e.g., every 5 minutes).  
- **Monitored Cities:** Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad.
- **Weather Data Retrieved:**  
  - **Main:** Main weather condition (e.g., Rain, Snow, Clear).  
  - **Temp:** Current temperature in Celsius.
  - **Feels_like:** Perceived temperature in Celsius.
  - **dt:** Timestamp of the data update (Unix timestamp).

---

### **Daily Weather Summary (Rollups and Aggregates)**
- **Description:**  
  At the end of each day, the system rolls up the collected data and generates **daily summaries**.  
- **Metrics in Daily Summary:**
  - **Average Temperature:** Calculated across all updates for the day.
  - **Maximum Temperature:** The highest recorded temperature during the day.
  - **Minimum Temperature:** The lowest recorded temperature during the day.
  - **Dominant Weather Condition:** The most frequently occurring weather condition for the day (e.g., Rain, Clear). If two conditions occur with the same frequency, the earliest one is selected.

---

### **Alerting System with Configurable Thresholds**
- **Description:**  
  Users can define alert thresholds to track specific weather conditions (e.g., a temperature above 35°C for two consecutive updates).  
- **Alert Triggers:**  
  - If a defined temperature threshold is breached, a notification is triggered.
  - Alerts can be displayed on the **console** or configured for **email notifications** (open-ended for future development).

---

### **Visualizations**
- **Description:**  
  The system supports visualization of:
  - **Daily summaries** with metrics like average, max, and min temperatures.
  - **Historical weather trends** to analyze patterns.
  - **Triggered alerts** for easier tracking and insights.

---

### **User Configurable Settings**
- **Configurable Options:**
  - **API Key:** Users can provide their own API key to access the OpenWeatherMap API.
  - **Interval Duration:** Set how frequently the system fetches weather data (e.g., every 5 minutes)..
  - **Alert Thresholds:** Define specific weather conditions or temperature limits to receive alerts.

---

### **3. System Design and Architecture**

In this section, we will document how the system is structured and the flow of data across various components. This will include a high-level overview and descriptions of each part of the architecture.

---

## **System Design and Architecture**

### **High-Level Architecture**
The system follows a **modular design**, allowing easy extension and maintainability. Below is an overview of the main components:  

**Components:**
1. **Data Fetcher Module:** 
   - Fetches real-time weather data from the OpenWeatherMap API.
2. **Scheduler:** 
   - Triggers periodic API calls at configurable intervals.
3. **Aggregator Module:** 
   - Computes daily weather summaries and aggregates.
4. **Alert Manager:** 
   - Monitors thresholds and triggers alerts when necessary.
5. **Persistent Storage:** 
   - Stores the weather data and daily summaries (e.g., in files or a database).
6. **Visualization Interface:** 
   - Displays data summaries, historical trends, and triggered alerts.

---

### **Flow of Data Across the System**
1. **Weather Data Retrieval:**
   - The **Scheduler** triggers the **Scheduler** module at a configurable interval (e.g., every 5 minutes).
   - The **Scheduler Module** retrieves weather data from the OpenWeatherMap API and sends it to the **Weather.db**.

2. **Data Processing:**
   - The **Weather.db** Stores the individual weather updates in the **Persistent Storage** for later use.

3. **Daily Rollups and Aggregates:**
   - At the end of each day, the **Aggregator Module**:
     - Fetches the weather updates from storage.
     - Calculates metrics such as average, min, max temperature, and dominant weather condition.
     - Stores the daily summary in the **Persistent Storage**.

4. **Alerting System:**
   - The **Alert Manager** continuously monitors the latest weather updates.
   - If any user-defined thresholds are breached (e.g., temperature exceeds 35°C for two consecutive updates), the **Alert Manager** triggers an alert.

5. **Visualization Interface:**
   - Users can view:
     - Daily weather summaries.
     - Historical trends.
     - Triggered alerts.

---

### **Detailed Module Descriptions**

#### **1. Scheduler Module:**
- **Function:** 
  - Triggers API calls at set intervals using the `schedule` library.
- **Implementation:** 
  - Uses `schedule.every(interval).minutes` to trigger the **Data Fetcher**.

#### **2. Data Fetcher Module:**
- **Function:** 
  - The `weather_api.py` connects to the OpenWeatherMap API, retrieves weather data, and passes it to the **Data Processor**.
- **Implementation:** 
  - Uses Python's `requests` library to perform API calls.

#### **3. Aggregator Module:**
- **Function:** 
  - Rolls up daily data and computes summary statistics.
- **Implementation:** 
  - Uses built-in Python functions for averages and condition frequency.

#### **4. Alert Manager Module:**
- **Function:** 
  - `alerts.py` monitors user-defined thresholds and triggers alerts.
- **Implementation:** 
  - Supports console alerts, with future scope for email notifications.

#### **6. Visualization Interface:**
- **Function:** 
  - `Visualizations.py` Displays weather summaries and trends in a user-friendly format.
- **Implementation:** 
  - Placeholder for future visualization implementation (e.g., using `matplotlib`).

---

## **Setup and Installation Guide**

### 1. **Prerequisites**
Before setting up the project, ensure you have the following tools and resources installed:

- **Python 3.11.9** installed.  
  Verify using:
  ```bash
  python --version
  ```
- **API Key from OpenWeatherMap**  
  Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate an API key.

- **Virtual Environment (Optional)**  
  It’s recommended to use a virtual environment to manage dependencies:
  ```bash
  python -m venv venv
  source venv/bin/activate    # On Linux/Mac
  venv\Scripts\activate       # On Windows
  ```

---

### 2. **Clone the Repository**
If using GitHub, clone the repository using:
```bash
git clone "https://github.com/nikhilgugwad/weather-monitoring.git"
cd <repository-folder>
```

---

### 3. **Install Dependencies**
Use the provided `requirements.txt` file to install all necessary dependencies:
```bash
pip install -r requirements.txt
```

#### **Dependencies:**
- `requests`: For making API calls.
- `schedule`: To trigger periodic tasks.
- `sqlite3` (Built-in with Python): To store data summaries.
- `matplotlib` (Optional): For future visualization.

---

### 4. **Configuration**
Create a **`.env`** file in the root directory to store your API key and other configurable settings.

**Example `.env` file:**
```
API_KEY=<your-openweathermap-api-key>
```

---

### 5. **Running the Application**

1. **Start the Scheduler and Data Fetcher:**
   Use the following command to run the scheduler and start periodic weather data retrieval:
   ```bash
   python scheduler.py
   ```

2. **Simulate Data Rollups:**
   To simulate daily rollups and view summary results, run:
   ```bash
   python database.py
   ```

3. **Trigger Alerts:**
   Define temperature or weather condition thresholds in the **alert_manager.py** file and run:
   ```bash
   python alerts.py
   ```
   Alerts, if triggered, will be displayed in the console during execution.


1. **SQLite Database Viewer:**  
   You can use the following command to view the stored weather summaries:
   ```bash
   sqlite3 weather.db "SELECT * FROM daily_weather_summary;"
   ```

---

### 6. **Troubleshooting Common Issues**

1. **API Key Errors:**
   - If the system cannot connect to the OpenWeatherMap API, check the API key in the `.env` file.

2. **Module Not Found Errors:**
   - Run `pip install -r requirements.txt` again to ensure all dependencies are installed.

3. **Scheduler Not Running:**
   - Verify that `schedule` is properly installed and check for any syntax issues in `scheduler.py`.

---

### **Known Issues and Future Improvements**



#### **Known Issues**  

1. **Limited Error Handling:**  
   - If the OpenWeatherMap API is temporarily down or the API key is invalid, the system may crash or fail to fetch data.  
   - **Improvement:** Add retry logic and better exception handling for failed API calls.

2. **Static Alert Thresholds:**  
   - Currently, the alert thresholds are hardcoded through the `.env` file and do not support dynamic user input.  
   - **Improvement:** Implement a user interface or API to modify thresholds at runtime.

3. **Basic Storage in SQLite:**  
   - The current system stores data locally using SQLite, which might not scale for larger datasets.  
   - **Improvement:** Transition to a more scalable database like PostgreSQL or MySQL if needed.

4. **Limited Support for Weather Parameters:**  
   - Currently, the system only fetches basic parameters (temperature, feels-like, and weather conditions).  
   - **Improvement:** Extend support to more parameters like humidity, wind speed, and forecasts.



#### **Future Improvements**

1. **Support for Additional Cities:**  
   - Expand beyond Indian metros and allow users to specify any city globally for weather monitoring.

2. **Notification System:**  
   - Add email or SMS notifications for alerts using services like Twilio or SendGrid.

3. **Historical Data Visualization:**  
   - Implement visualizations to show trends over weeks or months, not just daily summaries.

4. **Deployment via Docker:**  
   - Package the system in a Docker container for easy deployment across environments.

5. **Unit and Integration Tests:**  
   - Develop a comprehensive test suite to ensure system reliability and catch potential bugs early.

---

### **Project Conclusion**

In this project, we developed a **Real-Time Data Processing System for Weather Monitoring** that efficiently retrieves and processes weather data from the OpenWeatherMap API. The system provides valuable insights through daily rollups and aggregates, along with configurable alerts for extreme weather conditions.  

#### **Key Accomplishments**  
1. **Real-Time Weather Monitoring:**  
   - Successfully integrated with OpenWeatherMap API to fetch live weather data for six major Indian metros at configurable intervals.

2. **Data Aggregation and Rollups:**  
   - Implemented logic to calculate daily aggregates such as average, maximum, and minimum temperatures and identified the dominant weather condition for each day.

3. **Storage and Persistence:**  
   - Stored weather data summaries in a local SQLite database for further analysis and historical tracking.

4. **Scalability and Maintainability:**  
   - Designed the system to be modular, allowing future integration with additional weather parameters, visualizations, and notification mechanisms.

#### **Challenges Encountered**  
- Handling network errors and API timeouts required robust exception handling.
- Limited scope for visualization, which can be improved in future iterations.
- Storage using SQLite has constraints in scalability for long-term data retention.

#### **Future Scope and Recommendations**  
- **Expand Data Coverage:** Support more cities or allow user-specified locations.
- **Enhanced User Experience:** Add dashboards and visualizations to display summaries and alerts.
- **Dynamic Alert Configuration:** Implement a user interface to update alert thresholds without needing to modify code or environment files.
- **Deploy to the Cloud:** Host the project using Docker or cloud services for better accessibility and scalability.

With this, the core objectives of the project have been successfully achieved. The system is functional, maintains good modularity, and provides the foundation for further enhancements in alerting, storage, and visualizations.
