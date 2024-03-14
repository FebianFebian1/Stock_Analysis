import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_prep import *

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
# data = pd.read_csv('src/HistData5Y_walmart.csv')
data = pd.read_csv('src/HistData5Y_apple.csv')

#reverse the data
data = reverse_list(data)

#collect the date column and the closing price column
date = data_date(data)
closing_price = data_closing_price(data)
volume = data_volume(data)

#convert the closing price to a float
closing_price, period_length = float_price(closing_price)
numeric_date = data_numeric_date(date)


#plot the data
plt.figure()
plt.plot(numeric_date, closing_price)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Walmart Stock Price')
plt.show()

# fft closing price
# plt.figure()
# closing_price_fft = np.fft.fft(closing_price)
# closing_price_fft = np.abs(closing_price_fft)
# plt.plot(period_length[100:1000], closing_price_fft[100:1000])
# plt.show()  