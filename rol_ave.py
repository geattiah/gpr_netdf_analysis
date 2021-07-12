import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import csv

file_name = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\GBL_10m_50pSBL RH N-S 0_2017-02-02.csv"

outputfolder = (r"C:\Users\ReSEC2021\Downloads")

filename = pd.read_csv(r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\GBL_10m_50pSBL RH N-S 0_2017-02-02.csv")
#filename['Rolling'] = filename['GPR_Th'].rolling(window=100).mean()
print(filename)

filename['Roll'] = filename['GPR_Th'].rolling(window=1000).mean()
print(filename)


filename.to_csv(r'C:\Users\ReSEC2021\Downloads\gpr_out.csv')


