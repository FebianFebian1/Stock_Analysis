# This file contains the class Data_prep which is used to prepare the data for analysis
# The source for the data are taken from NASDAQ donwloaded csv files. 
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

class Data_prep:

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
        '''
        Plot the closing price of the stock against the date
        '''
        plt.figure()
        plt.plot(self.date, self.closing_price)
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title('Stock Price against Date')
        plt.show()

    def volume_date(self):
        '''
        Plot the volume of the stock against the date
        '''
        plt.figure()
        plt.plot(self.date, self.volume)
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.title('Stock Volume against Date')
        plt.show()


