import pandas as pd
import numpy as np

class Banmen:
    ban = np.empty((1,1))
    def __init__(self, tatenum, yokonum):
        self.ban = np.zeros((tatenum+2, yokonum+2))
        #枠の作成
        self.ban[0] = 1
        self.ban[tatenum+1] = 1
        for i in range(yokonum+2):
            self.ban[i, 0] = 1
            self.ban[i, yokonum+1] = 1
    
    def ban_check(self):
        return self.ban