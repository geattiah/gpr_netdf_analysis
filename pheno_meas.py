import sys
import os
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import csv

csv_direct =  "C:/Users/ReSEC2021/Downloads"

data = pd.read_csv("C:/Users/ReSEC2021/Downloads/NW_2.csv",sep = ",", engine = 'python', header = 0)
print(data)


with open(os.path.join(csv_direct,'NW_2_ph_2')+".csv", 'w', newline = '') as table:
    writer = csv.writer(table)
    writer.writerow(['Date',])
    


    for (idx, row) in data.iterrows():              
        year = row.loc['DATE']
        ice_cover = row.loc['ICE_COVER']

        if ice_cover == 0:
            writer.writerow([year])



