import sys
sys.path.append("code")
import random as rn
from Utility import *

class Num:
    def __init__(self, column_at, given_name):
        self.capacity = 100
        #number of variable have seen
        self.n = 0
        self.low = float('inf')
        self.high = float('-inf')
        self.col_at = column_at if column_at != None else 0
        self.name = given_name if given_name != None else ''
        self.is_sorted = False
        self.data = []
        self.w = -1 if given_name != None and given_name[-1] == '-' else 1
        
    def nums(self):
        if not self.is_sorted:
            self.data.sort()
            self.is_sorted = True
        return self.data
    
    #I don't think add should have the parameter, I feel it is a bad structure.
    def add(self, v, the=None): #TODO should 'the' be a parameter? or a global var somewhere?
        #TODO maybe need to initialize pos
        if v != '?':
            pos = None
            self.n += 1
            self.low = min(v, self.low)
            self.high = max(v, self.high)

            if len(self.data) < self.capacity:
                pos = len(self.data)
                #add a dummy to avoid index out of bound
                self.data.append(None)
            # else:
            #     pos = len(self.data)-1
            elif rn.random() < self.capacity/self.n:
                pos = rn.randint(0, len(self.data) - 1)
            if pos is not None:
                self.is_sorted = False
                self.data[pos] = float(v) # TODO float or int?
    
    def div(self):
        if len(self.data) < 2:
            return None
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58
    
    def mid(self):
        return per(self.nums(), 0.5)
            
