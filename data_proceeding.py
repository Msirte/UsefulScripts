import numpy as np
import pandas as pd
import os

filename = "data.txt"
num_split_lines = 63

col_list = []
row_list = []

with open(filename,'r') as f:
    for line in f:
        if line == "\n":
            col_list.append(row_list)
            row_list = []
        else:
            row_list.append(line.replace('\n', ''))

np_col_list = np.array(col_list)
np_row_list = np_col_list.T

df = pd.DataFrame(np_row_list)
df.to_excel('data.xlsx',header=None,index=None)
