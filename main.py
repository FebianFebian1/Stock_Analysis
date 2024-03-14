import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_prep import float_price, data_date, data_closing_price, reverse_list

# Load the data
# data = pd.read_csv('src/HistData5Y_walmart.csv')
data = pd.read_csv('src/HistData5Y_apple.csv')

data = reverse_list(data)

#collect the date column and the closing price column
date = data_date(data)
closing_price = data_closing_price(data)

#convert the closing price to a float
closing_price, period_length = float_price(closing_price)

#plot the data
plt.figure()
plt.plot(period_length[100:1000], closing_price[100:1000])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Walmart Stock Price')

# fft closing price
plt.figure()
closing_price_fft = np.fft.fft(closing_price)
closing_price_fft = np.abs(closing_price_fft)
plt.plot(period_length[100:1000], closing_price_fft[100:1000])
plt.show()  