import pandas as pd

from src.data_prep import Data_prep
from src.StockLinearRegression import ML_analysis


# Load the data
# data = pd.read_csv('src/csv_files/HistData5Y_walmart.csv')
data = pd.read_csv('src/csv_files/HistData5Y_apple.csv')

# Plot the stock trend
stock = Data_prep(data)
stock.price_date()

# Linear Regression
stock_analysis = ML_analysis(data)
stock_analysis.StockLinearRegression()
