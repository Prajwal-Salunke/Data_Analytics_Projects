# 🌦️ Weather Data Analysis

This project explores historical weather data to uncover seasonal trends, correlations, and extreme events.  
Built using **Python**, it leverages powerful libraries like **Pandas**, **NumPy**, and **Matplotlib/Seaborn** for data cleaning, analysis, and visualization.

---

## 📌 Project Objective

To analyze time-series weather data and extract meaningful insights about temperature, humidity, visibility, and their interrelationships. These insights provide valuable context for climate understanding and operational planning.

---

## 🧾 Dataset Description

The dataset contains daily historical weather metrics.

| Column Name   | Description                                           |
|---------------|-------------------------------------------------------|
| Date          | Daily date (YYYY-MM-DD)                              |
| Temperature   | Daily average temperature (°C)                       |
| Humidity      | Daily average humidity (%)                           |
| Visibility    | Daily average visibility (km)                        |
| (Other cols)  | (If your dataset has additional metrics, list them)  |

---

## 🛠️ Tools & Technologies Used

- **Python 3.8+**
- **Pandas** – data manipulation
- **NumPy** – numerical analysis
- **Matplotlib** & **Seaborn** – data visualization
- **Jupyter Notebook** – exploratory analysis environment

---

## 🔍 Exploratory Data Analysis (EDA)

This analysis includes:

- 🗓️ **Monthly and seasonal average trends** for temperature, humidity, and visibility  
- 📉 **Correlation analysis** among weather variables  
- 🌡️ **Identification of extreme days** (e.g., highest temperature, highest humidity)  
- 📊 **Distribution visualizations** using box plots and scatter plots

---

## 📈 Key Insights Summary

| **Aspect**                | **Key Insight**                                                                 |
|---------------------------|----------------------------------------------------------------------------------|
| Monthly Temperature       | Distinct **seasonal pattern** – highs in summer, lows in winter                |
| Humidity Trends           | Peak **humidity during monsoon**, lowest in late winter                         |
| Visibility Patterns       | **Visibility drops in rainy months**, improves in dry seasons                   |
| Correlation Analysis      | **Negative correlation (~‑0.7)** between temperature & humidity; moderate between temp & visibility (+0.4) |
| Extreme Weather Events    | Noted instances: **hottest days (>40 °C)** and **most humid days (>90 % RH)**   |

## 📁 Folder Structure

- `Weather_Data_Analysis/`
  - `weather_data_analysis.ipynb` – Main Jupyter notebook
  - `weather_data.csv` – Raw dataset
  - `visuals/` – (Optional) Folder for saved charts and plots
  - `README.md` – Project documentation
