import pandas as pd
import os

def save_queries(path,file_name,df):
    
    check_path(path)
    final_path = path + '/' + file_name + '.csv'
    
    df.to_csv(final_path,index = False,)

    
def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)