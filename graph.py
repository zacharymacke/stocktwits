import numpy as np
import pandas as pd
import requests
import pickle
import operator
import time
import matplotlib.pyplot as plt
from stock_class import *
from pandas_datareader import data as web
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

ticker_set = load_set()
stock_data = load_dict()
stock_list = load_sorted_list()
stock_list = (sorted(stock_list, key=operator.attrgetter('total_occurances'), reverse=True))

for i in range(15):
    print(stock_list[i])

print(dt.now())
print(dt.now() - relativedelta(months=1)) 



# ticker = list(ticker_set)[1]
# print(ticker)
# df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+ticker+'/chart/1M')
#
# print(df_temp)


# for i,j in enumerate(ticker_set):
#     if(i<4):
#         ticker = str(j)
#         print(ticker)
#         df_temp = pd.read_json('https://api.iextrading.com/1.0/stock/'+ticker+'/chart/1M')
#         df_temp.plot(y='close')
#         plt.title(ticker)
#         plt.show()
#         print(df_temp)
#
# print(df_temp.columns)
