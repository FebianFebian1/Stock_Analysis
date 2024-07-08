from src.data_prep import *
import matplotlib.pyplot as plt

def PlotStockTrend(data):
        #reverse the data so that it is in chronological order
    data = reverse_list(data)

    #collect the date column and the closing price column
    date = data_date(data)
    closing_price = data_closing_price(data)
    volume = data_volume(data)

    #convert the closing price to a float
    closing_price = float_price(closing_price)
    numeric_date = data_numeric_date(date)

    #plot the data
    plt.figure()
    plt.plot(numeric_date, closing_price)
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('Walmart Stock Price')
    plt.show()