import csv
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
import pandas as pd
import numpy as np

MyColumns = ['Date', 'CashRateSelling', 'CashRateBuying', 'SpotRateSelling', 'SpotRateBuying']

class MyExchangeRate:
    def __init__(self, FilePath, currency):
        self.currency = currency
        # Exchange Rate Data Frame
        self.ERDataFrame = self.ReadExchangeRate(FilePath)
        self.PNGFilename = '['+ datetime.date.today().strftime("%Y.%m.%d") + '][' + currency + '] Result.png'

    def ReadExchangeRate(self, FilePath):
        res = []
        with open(FilePath, newline='') as csvfile:
            next(csvfile)
            rows = csv.reader(csvfile)
            for row in rows:
                tmp = []
                tmpDate = datetime.datetime.strptime(row[0], "%Y%m%d")
                tmp.append(tmpDate)        # Date
                tmp.append(float(row[13])) # CashRateSelling
                tmp.append(float(row[3]))  # CashRateBuying
                tmp.append(float(row[14])) # SpotRateSelling
                tmp.append(float(row[4]))  # SpotRateBuying
                res.insert(0, tmp)
        DataFrame = pd.DataFrame(res, columns = MyColumns)
        return DataFrame

    def GenerateLineChart(self):
        print(self.ERDataFrame)
        mondays = WeekdayLocator(MONDAY)
        alldays = DayLocator()
        weekFormatter = DateFormatter('%Y%b%d')

        fig, (axCashRate, axSpotRate) = plt.subplots(2, 1, sharex = True)
        fig.subplots_adjust(bottom = 0.2)
        plt.ticklabel_format(style='plain')

        # Cash Rate
        axCashRate.set_title('Cash Rate')
        axCashRate.xaxis.set_major_locator(mondays)
        axCashRate.xaxis.set_minor_locator(alldays)
        axCashRate.xaxis.set_major_formatter(weekFormatter)
        axCashRate.grid(True)

        # Cash Rate - Line Chart
        for each in self.ERDataFrame:
            axCashRate.plot(self.ERDataFrame['Date'], self.ERDataFrame['CashRateSelling'], color='blue', label='Selling')
        for each in self.ERDataFrame:
            axCashRate.plot(self.ERDataFrame['Date'], self.ERDataFrame['CashRateBuying'], color='red', label='Buying')

        # Spot Rate
        axSpotRate.set_title('Spot Rate')
        axSpotRate.xaxis.set_major_locator(mondays)
        axSpotRate.xaxis.set_minor_locator(alldays)
        axSpotRate.xaxis.set_major_formatter(weekFormatter)
        axSpotRate.grid(True)

        # Spot Rate - Line Chart
        for each in self.ERDataFrame:
            axSpotRate.plot(self.ERDataFrame['Date'], self.ERDataFrame['SpotRateSelling'], color='blue', label='Selling')
        for each in self.ERDataFrame:
            axSpotRate.plot(self.ERDataFrame['Date'], self.ERDataFrame['SpotRateBuying'], color='red', label='Buying')

        plt.setp(plt.gca().get_xticklabels(), rotation = 45, horizontalalignment = 'right')
        plt.savefig(self.PNGFilename)

