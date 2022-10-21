import matplotlib.pyplot as plt
from weather import LowHighs

sitka = LowHighs('data/sitka_weather_2018_simple.csv')
sitka.read_temp()
death_valley = LowHighs('data/death_valley_2018_simple.csv')
death_valley.read_temp()

plt.style.use('classic')

plt.plot(sitka.dates, sitka.highs, c='red', alpha=0.5)
plt.plot(sitka.dates, sitka.lows, c='blue', alpha=0.5)
plt.fill_between(sitka.dates, sitka.highs, sitka.lows, facecolor='blue', alpha=0.1)

plt.plot(death_valley.dates, death_valley.highs, c='green', alpha=0.5)
plt.plot(death_valley.dates, death_valley.lows, c='yellow', alpha=0.5)
plt.fill_between(death_valley.dates, death_valley.highs, death_valley.lows, facecolor='red', alpha=0.1)

# Format plot.
plt.title(f"Daily high and low temperatures, {sitka.station_name} and {death_valley.station_name}, 2018", fontsize=12)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.ylim([20, 130])
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
