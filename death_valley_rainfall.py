import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get Dates and high and low temperatures from this file.
    dates, rain_falls = [], []
    for row in reader:
        rain_fall = float(row[3])
        rain_falls.append(rain_fall)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain_falls, c='red', alpha=0.5)

# Format plot.
ax.set_title("Death Valley rainfall, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Rainfall", fontsize=16)
fig.autofmt_xdate()
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
