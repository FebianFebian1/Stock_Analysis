from src.stock_data import StockData
from src.stock_linear_regression import ML_analysis



# # Load the data from donwloaded csv file from NASDAQ
# data = pd.read_csv('src/csv_files/HistData5Y_walmart.csv')
# data = pd.read_csv('src/csv_files/HistData5Y_apple.csv')

# # Plot the stock trend
# stock = Data_prep(data)
# stock.price_date()

ticker = 'AAPL'
data = StockData(ticker)
data.price_date()

# Linear Regression
stock_analysis = ML_analysis(ticker)
stock_analysis.StockLinearRegression()
