import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



    # Load dataset
df = pd.read_csv('../dataset/climate_change_dataset.csv')

    # Show basic information
print("First 5 Rows:\n", df.head())
print("\n Summary Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())



    # Scatter Plot: Temperature vs Burned Area
if {'temp', 'area'}.issubset(df.columns):
  plt.figure(figsize=(8, 5))
  plt.scatter(df['temp'], df['area'], alpha=0.5, color='crimson')
  plt.title('🌡️ Temperature vs Burned Area')
  plt.xlabel('Temperature (°C)')
  plt.ylabel('Burned Area (ha)')
  plt.grid(True)
  plt.savefig('output/plots/temp_vs_area.png')
  plt.close()

    # Scatter Plot: Wind Speed vs Burned Area
if {'wind', 'area'}.issubset(df.columns):
  plt.figure(figsize=(8, 5))
  plt.scatter(df['wind'], df['area'], alpha=0.5, color='teal')
  plt.title('💨 Wind Speed vs Burned Area')
  plt.xlabel('Wind Speed (km/h)')
  plt.ylabel('Burned Area (ha)')
  plt.grid(True)
  plt.savefig('output/plots/wind_vs_area.png')
  plt.close()

    # Bar Plot: Average Burned Area by Month
if {'month', 'area'}.issubset(df.columns):
  month_avg = df.groupby("month", observed=False)["area"].mean().sort_index()
  plt.figure(figsize=(10, 6))
  month_avg.plot(kind="bar", color="orange", edgecolor="black")
  plt.title("📆 Average Burned Area by Month")
  plt.ylabel("Average Burned Area (ha)")
  plt.xlabel("Month")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig('output/plots/monthwise_area.png')
  plt.close()

    # Bar Plot: Average Burned Area by Day of Week
if {'day', 'area'}.issubset(df.columns):
  day_avg = df.groupby("day", observed=False)["area"].mean().sort_index()
  plt.figure(figsize=(10, 6))
  day_avg.plot(kind="bar", color="green", edgecolor="black")
  plt.title("📅 Average Burned Area by Day of Week")
  plt.ylabel("Average Burned Area (ha)")
  plt.xlabel("Day of Week")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig('output/plots/daywise_area.png')
  plt.close()


