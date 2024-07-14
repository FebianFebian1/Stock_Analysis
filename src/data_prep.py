import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class stock_data:

    def __init__(self, data):
        self.data = data[::-1]

        date, closing_price, volume = self.data_param()
        self.date = date
        self.closing_price = closing_price
        self.volume = volume

    def data_param(self):

        date = np.array(self.data['Date'])
        date = [datetime.strptime(i, '%m/%d/%Y') for i in date]
        closing_price = np.array(self.data['Close/Last'])
        for i in range(len(closing_price)):
            closing_price[i] = float(closing_price[i].replace('$', ''))
        volume = np.array(self.data['Volume'])

        return date, closing_price, volume
    
    def price_date(self):
        plt.figure()
        plt.plot(self.date, self.closing_price)
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title('Walmart Stock Price')
        plt.show()

    def volume_date(self):
        plt.figure()
        plt.plot(self.date, self.volume)
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.title('Walmart Stock Price')
        plt.show()


