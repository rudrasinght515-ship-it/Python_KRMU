"""

Project: Calorie Tracker program (CLI)

Name: Rudra Singh
Roll No: 2501730339
Section: C

Description: 
      A easy program to analyse energy consumption.

"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

#*************************************

    # Data Ingestion & Validation

#*************************************

def load_data(data_dir="data"):
    all_files = Path(data_dir).glob("*.csv")
    df_list = []
    for file in all_files:
        try:
            df = pd.read_csv(file, on_bad_lines="skip")
            # Add building name from filename
            df["Building"] = file.stem
            df_list.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")
    return pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()

#************************************

   # Load Your CSV Files From Data

#************************************

df_combined = load_data()
df_combined["Timestamp"] = pd.to_datetime(df_combined["Timestamp"])

#*****************************

    # Aggregation Logic 

#*****************************

def calculate_daily_totals(df):
    return df.resample("D", on="Timestamp")["kWh"].sum()

def calculate_weekly_aggregates(df):
    return df.resample("W", on="Timestamp")["kWh"].sum()

def building_wise_summary(df):
    return df.groupby("Building")["kWh"].agg(["mean", "min", "max", "sum"])

daily_totals = calculate_daily_totals(df_combined)
weekly_totals = calculate_weekly_aggregates(df_combined)
building_summary = building_wise_summary(df_combined)

# -------------------------------
# Task 3: Object-Oriented Modeling
# -------------------------------
#**********************************

    # Object-Oriented Modeling

#**********************************

class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, reading):
        self.meter_readings.append(reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        return f"{self.name}: {self.calculate_total_consumption()} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_reading(self, building_name, timestamp, kwh):
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
        self.buildings[building_name].add_reading(MeterReading(timestamp, kwh))

manager = BuildingManager()
for _, row in df_combined.iterrows():
    manager.add_reading(row["Building"], row["Timestamp"], row["kWh"])

#*****************************

        # Visualization

#*****************************

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

# Line Chart: Daily totals
#**********************************

    # Line Chart: Daily Totals

#**********************************

daily_totals.plot(ax=axes[0], color="blue", linewidth=2)
axes[0].set_title("Daily Campus Consumption")
axes[0].set_ylabel("kWh")
axes[0].grid(True)

# Bar Chart: Building averages
#************************************

    # Bar Chart: Building Averages

#************************************

building_summary["mean"].plot(kind="bar", ax=axes[1], color="orange")
axes[1].set_title("Average Usage per Building")
axes[1].set_ylabel("kWh")
axes[1].grid(axis="y")

# Scatter Plot: Hourly readings
#************************************

   # Scatter Plot: Hourly Readings

#************************************

axes[2].scatter(df_combined["Timestamp"], df_combined["kWh"], alpha=0.3, s=10, c="green")
axes[2].set_title("Hourly Consumption Scatter")
axes[2].set_ylabel("kWh")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

#*****************************

    # Persistence & Summary

#*****************************

df_combined.to_csv("cleaned_energy_data.csv", index=False)
building_summary.to_csv("building_summary.csv")

summary_text = f"""
Total Campus Consumption: {df_combined['kWh'].sum()} kWh
Highest Consuming Building: {building_summary['sum'].idxmax()}
Peak Load Time: {df_combined.loc[df_combined['kWh'].idxmax(), 'Timestamp']}
Weekly Trend (first 5):\n{weekly_totals.head()}
"""

with open("summary.txt", "w") as f:
    f.write(summary_text)

print(summary_text)