"""

Project: Calorie Tracker program (CLI)

Name: Rudra Singh
Roll No: 2501730339
Section: C

Description: 
      A easy program to predict wheather data through python. 

"""

import pandas as pd
import matplotlib.pyplot as plt

#*****************************

        # Load Data

#*****************************

df = pd.read_csv("weather.csv")   # make sure weather.csv is in the same folder
print("Data Head:\n", df.head())

#*****************************

        # Clean Data

#*****************************
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna()   # drop rows with missing values

#*****************************

    # Basic Statistics

#*****************************

print("\nMean Temperature:", df["Temperature"].mean())
print("Max Temperature:", df["Temperature"].max())
print("Min Temperature:", df["Temperature"].min())
print("Std Dev Temperature:", df["Temperature"].std())

#**********************************

  # Line Chart: Daily Temperature

#**********************************

plt.figure(figsize=(8,4))
plt.plot(df["Date"], df["Temperature"], color="red")
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.savefig("daily_temperature.png")
plt.show()

#************************************

    # Bar Chart: Monthly Rainfall

#************************************

monthly_rain = df.groupby(df["Date"].dt.month)["Rainfall"].sum()
monthly_rain.plot(kind="bar", color="blue", figsize=(6,4))
plt.title("Monthly Rainfall Totals")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.tight_layout()
plt.savefig("monthly_rainfall.png")
plt.show()


#*****************************************

  # Scatter Plot: Humidity vs Temperature

#*****************************************

plt.figure(figsize=(6,4))
plt.scatter(df["Temperature"], df["Humidity"], alpha=0.7, color="green")
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.savefig("humidity_vs_temperature.png")
plt.show()

#*************************************

   # Grouping Example: Monthly Stats

#*************************************

monthly_stats = df.groupby(df["Date"].dt.month).agg({
    "Temperature": ["mean", "min", "max"],
    "Rainfall": "sum",
    "Humidity": "mean"
})
print("\nMonthly Statistics:\n", monthly_stats)

#*****************************

    # Export Cleaned Data

#*****************************

df.to_csv("cleaned_weather.csv", index=False)
print("\nCleaned data exported to cleaned_weather.csv")