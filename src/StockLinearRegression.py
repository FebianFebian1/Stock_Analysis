import numpy as np
import matplotlib.pyplot as plt
from src.data_prep import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



def StockLinearRegression(data):

    #reverse the data so that it is in chronological order
    data = reverse_list(data)

    #collect the date column and the closing price column
    date = data_date(data)
    closing_price = data_closing_price(data)
    volume = data_volume(data)

    #convert the closing price to a float
    closing_price = float_price(closing_price)
    numeric_date = data_numeric_date(date)

    # Linear Regression Implementation
    # Reshape the data
    start_date = min(numeric_date)
    numeric_dates = [(d - start_date).days for d in numeric_date]
    numeric_dates = np.array(numeric_dates).reshape(-1, 1)
    closing_price = np.array(closing_price).reshape(-1, 1)

    # split the data
    X_train, X_test, y_train, y_test = train_test_split(numeric_dates, closing_price, test_size=0.2, random_state=0)

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Plot the results
    plt.figure()
    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.title('Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.show()