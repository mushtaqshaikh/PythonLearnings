import pandas as pd
import os

class TickerList:
    
    def readdata(self):
        global gbl_df_ticker
        # print(os.getcwd())
        df = pd.read_csv('PythonLearnings/input/NSEList.csv')
        gbl_df_ticker = pd.DataFrame(df['Ticker'])
        return df
        print(gbl_df_ticker)
    
    


