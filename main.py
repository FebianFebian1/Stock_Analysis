import pandas as pd

from src.data_prep import stock_data
from src.StockLinearRegression import ML_analysis


# Load the data
# data = pd.read_csv('src/HistData5Y_walmart.csv')
data = pd.read_csv('src/HistData5Y_apple.csv')

# Plot the stock trend
stock = stock_data(data)
stock.volume_date()

# Linear Regression
stock_analysis = ML_analysis(data)
stock_analysis.StockLinearRegression()


# fft closing price
# plt.figure()
# closing_price_fft = np.fft.fft(closing_price)
# closing_price_fft = np.abs(closing_price_fft)
# plt.plot(period_length[100:1000], closing_price_fft[100:1000])
# plt.show()  