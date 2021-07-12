import pandas as pd
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#filename = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\gpr_out.csv"
filename = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis\GBL_10m_50pSBL RH N-S 0_2017-02-02.csv"

outputfolder = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University\slideanalysis"

df = pd.read_csv(filename,sep=',')
print(df)

fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)   
fontP = FontProperties()
fontP.set_size('small')
y = df['GPR_Th']
x = range(23148)
y1 = df['Model_Th']
x2 = df['Latlon']
print(x)
p0 = plt.scatter(x, y, s=3)
p1 = plt.plot(x, y1, 'r')

plt.xlabel("Point")
plt.title('GPr vrs Model')
plt.xticks(x[::1000], rotation = 45)
#plt.locator_params(axis='x', nbins=len(x)/2)
plt.ylabel("Ice Thickness(cm)")
plt.legend(handles=[p0], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
# plt.legend(loc='upper left')
plt.tight_layout()
figfile = os.path.join(outputfolder, 'roll_1000' + '_IC' + ".png")
plt.show()
plt.savefig(figfile)
