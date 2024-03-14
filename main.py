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
closing_price = float_price(closing_price)
numeric_date = data_numeric_date(date)

#plot the data
plt.figure()
plt.plot(numeric_date, closing_price)
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Walmart Stock Price')
plt.show()

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

# fft closing price
# plt.figure()
# closing_price_fft = np.fft.fft(closing_price)
# closing_price_fft = np.abs(closing_price_fft)
# plt.plot(period_length[100:1000], closing_price_fft[100:1000])
# plt.show()  