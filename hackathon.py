import numpy as np
import pandas as pd
import requests
import pickle
import operator
import time


def load_data():
    trend = requests.get('https://api.stocktwits.com/api/2/streams/trending.json?access_token=fdf4ddd7a52a0e54753b884627259c12ad2f13ba')
    suggest = requests.get('https://api.stocktwits.com/api/2/streams/suggested.json?access_token=fdf4ddd7a52a0e54753b884627259c12ad2f13ba')
    trending = trend.json()
    suggesting = suggest.json()
    df_trending = pd.DataFrame(trending['messages'])
    df_suggesting = pd.DataFrame(suggesting['messages'])
    
    return df_trending, df_suggesting


class Stock:
    def __init__(self, ticker, watch_count, total_occurances, bear, bull):
        self.ticker = ticker
        self.watch_count = watch_count
        self.total_occurances = total_occurances
        self.bear = bear
        self.bull = bull
        
    def __repr__(self):
        return ("{" + str(self.ticker) + ',' + " watch_count=" + str(self.watch_count) + ',' + " occurances=" + str(self.total_occurances) + ','  + " bear=" + str(self.bear) + ',' + " bull=" + str(self.bull) + ',' + "}")
        
    def __str__(self):
        return ("{" + str(self.ticker) + ',' + " watch_count=" + str(self.watch_count) + ',' + " occurances=" + str(self.total_occurances) + ','  + " bear=" + str(self.bear) + ',' + " bull=" + str(self.bull) + "}")
    
    def add_bear(self):
        self.bear += 1
    def add_bull(self):
        self.bull += 1
    def add_occurance(self):
        self.total_occurances += 1


def analyze(df):
    '''insert docstring'''
    for i in range(30):
        try:
        # we have to account for the fact the message may contain no ticker
            watch_count = df['symbols'].iloc[i][0]['watchlist_count']
            tickers = df['symbols'].iloc[i]#[0]['symbol']
            bull_bear_ticker = tickers[0]['symbol']

            for j in range(len(tickers)):
                tick = tickers[j]['symbol']
                watch = tickers[j]['watchlist_count']
                if (tick not in stock_set):
                    stock_set.add(tick)
                    stock_dict[tick] = Stock(tick,watch,1,0,0)
                else:
                    stock_dict[tick].add_occurance()
                    
                # we have to account that not all messages contain a sentiment
                try:
                    sent1 = df['entities'][i]['sentiment']['basic']
                    if(sent1 == 'Bullish'):
                        stock_dict[tick].add_bull()
                    elif(sentiment == 'Bearish'):
                        stock_dict[tick].add_bear()
                except:
                    pass
        except:
            pass
        

def evaluate():
    sorted_l = []
    for i in stock_set:
        sorted_l.append(stock_dict[i])
    sorted_l = sorted(sorted_l, key=operator.attrgetter('total_occurances'),reverse=True)
    for i in sorted_l:
        print(i)
    

def save_dict():
    pickle_stock = open("stock_dict.pickle", "wb")
    pickle.dump(stock_dict, pickle_stock)
    pickle_stock.close()
    

def save_set():
    pickle_stock_set = open("stock_set.pickle", "wb")
    pickle.dump(stock_set, pickle_stock_set)
    pickle_stock_set.close()


def load_dict():
    file = open('stock_dict.pickle', 'rb')
    data = pickle.load(file)
    file.close()
    return data


def load_set():
    file = open('stock_set.pickle','rb')
    data = pickle.load(file)
    file.close()
    return data


def main():
    
    print('\n')
    print('-'*20)
    
    #load data from api
    df_trending, df_suggesting = load_data()


    # #load pickles from memory
    # stock_dict = load_dict()
    # stock_set = load_set()
    
    #update dictionary/set
    analyze(df_suggesting)
    analyze(df_trending)
    evaluate()
    
    #save the new data
    save_dict()
    save_set()
    print('\n')
    print('-'*20)
    time.sleep(360)


if __name__ == '__main__':
    # stock_dict = {}
    # stock_set = set()
    #load pickles from memory
    stock_dict = load_dict()
    stock_set = load_set()
    while True:
        main()

