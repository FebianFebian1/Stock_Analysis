import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_prep import *
from src.PlotStockTrend import *
from src.StockLinearRegression import *

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
# data = pd.read_csv('src/HistData5Y_walmart.csv')
data = pd.read_csv('src/HistData5Y_apple.csv')

# Plot the stock trend
PlotStockTrend(data)

# Linear Regression
StockLinearRegression(data)


# fft closing price
# plt.figure()
# closing_price_fft = np.fft.fft(closing_price)
# closing_price_fft = np.abs(closing_price_fft)
# plt.plot(period_length[100:1000], closing_price_fft[100:1000])
# plt.show()  