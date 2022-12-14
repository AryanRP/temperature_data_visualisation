import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get Dates and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            lows.append(low)
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Daily high and low temperatures, 2018\nDeath Valley, CA", fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ylim([20, 130])
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
