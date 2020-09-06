import pandas as pd
from pandas_datareader import data as web
from datetime import datetime
import matplotlib.pyplot as plt

class StockPlotter:
    def __init__(self):

        stock_data = pd.DataFrame()

        data = input('Enter the stocks here: ').upper()

        for datum in data:
            if datum == ',':
                data = data.replace(datum, '')

        stocks = data.split()
        self.stocks = stocks

        start_date = '2015-01-01'
        self.start_date = start_date

        end_date = datetime.today().strftime('%Y-%m-%d')
        self.end_date = end_date

        for stock in stocks:
            stock_data[stock] = web.DataReader(stock, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

        self.stock_data = stock_data


    def plotData(self):
        plt.plot(self.stock_data)
        plt.legend(self.stock_data)
        plt.show()

StockPlotter().plotData()


