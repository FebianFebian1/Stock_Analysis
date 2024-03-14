import pandas as pd
import numpy as np

def data_date(data):
    date = np.array(data['Date'])
    return date

def data_closing_price(data):
    closing_price = np.array(data['Close/Last'])
    return closing_price

def reverse_list(data):
    return data[::-1]

def float_price(closing_price):
    period_length = np.arange(1,len(closing_price)+1)

    for i in range(len(closing_price)):
        closing_price[i] = float(closing_price[i].replace('$', ''))
    return closing_price, period_length