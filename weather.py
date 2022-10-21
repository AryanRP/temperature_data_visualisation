import csv
from datetime import datetime


class LowHighs:

    # Set the file path
    def __init__(self, file):
        self.file = file
        self.reader = None
        self.header_row = None
        self.dates, self.highs, self.lows = None, None, None
        self.station_name = None

    def read_temp(self):
        # Read the file and Get Dates and high and low temperatures from this file
        with open(self.file) as f:
            self.reader = csv.reader(f)
            self.header_row = next(self.reader)
            self.dates, self.highs, self.lows = [], [], []
            for row in self.reader:
                try:
                    high = int(row[self.header_row.index('TMAX')])
                    low = int(row[self.header_row.index('TMIN')])
                except ValueError:
                    pass
                else:
                    self.highs.append(high)
                    self.lows.append(low)
                    current_date = datetime.strptime(row[self.header_row.index('DATE')], '%Y-%m-%d')
                    self.dates.append(current_date)
                    self.station_name = row[1]
