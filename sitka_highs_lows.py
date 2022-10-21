import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get Dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        high = int(row[header_row.index('TMAX')])
        highs.append(high)
        low = int(row[header_row.index('TMIN')])
        lows.append(low)
        current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        dates.append(current_date)
        station_name = row[1]

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title(f"Daily high and low temperatures, {station_name}, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ylim([20, 130])
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

