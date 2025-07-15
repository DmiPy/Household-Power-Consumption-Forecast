import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
# Data load
df = pd.read_csv(
    'household_power_consumption.txt',
    sep=';',
    parse_dates=[[0, 1]],  # Merge date and time
    na_values='?',
    infer_datetime_format=True,
    low_memory=False
)

# Rename column to datetime
df.rename(columns={'Date_Time': 'Datetime'}, inplace=True)

# Set time index
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%d/%m/%Y %H:%M:%S')
df.set_index('Datetime', inplace=True)

# Columns into float type
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'], errors='coerce')

df.dropna(subset=['Global_active_power'], inplace=True)

# Choose 1 day (e.g. 2007-01-01)
one_day = df.loc['2007-01-01']

plt.figure(figsize=(12, 4))
plt.plot(one_day.index, one_day['Global_active_power'], label='Global Active Power (kW)')
plt.title('Stromverbrauch an einem Tag (01.01.2007)')
plt.ylabel('Leistung in kW')
plt.xlabel('Zeit')
plt.grid(True)
plt.tight_layout()
plt.show()

