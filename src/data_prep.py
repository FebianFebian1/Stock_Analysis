import pandas as pd
import numpy as np
from datetime import datetime

def data_date(data):
    date = np.array(data['Date'])
    return date

def data_closing_price(data):
    closing_price = np.array(data['Close/Last'])
    return closing_price

def data_volume(data):
    volume = np.array(data['Volume'])
    return volume

def reverse_list(data):
    return data[::-1]

def float_price(closing_price):
    period_length = np.arange(1,len(closing_price)+1)

    for i in range(len(closing_price)):
        closing_price[i] = float(closing_price[i].replace('$', ''))
    return closing_price, period_length

def data_numeric_date(data):
    date = [datetime.strptime(i, '%m/%d/%Y') for i in data]
    return date