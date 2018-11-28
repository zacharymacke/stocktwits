import pickle


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
    def get_occurance(self):
        return self.total_occurances


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

def load_sorted_list():
    file = open('sorted_list.pickle','rb')
    data = pickle.load(file)
    file.close()
    return data

