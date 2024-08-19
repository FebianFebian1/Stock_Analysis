import numpy as np
import matplotlib.pyplot as plt
from src.data_prep import Data_prep

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class ML_analysis(Data_prep):
    def __init__(self, data):
        super().__init__(data)

    def StockLinearRegression(self):

        # Linear Regression Implementation
        # Reshape the data
        start_date = min(self.date)
        numeric_dates = [(d - start_date).days for d in self.date]
        numeric_dates = np.array(numeric_dates).reshape(-1, 1)
        self.closing_price = np.array(self.closing_price).reshape(-1, 1)

        # split the data
        X_train, X_test, y_train, y_test = train_test_split(numeric_dates, self.closing_price, test_size=0.2, random_state=0)

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