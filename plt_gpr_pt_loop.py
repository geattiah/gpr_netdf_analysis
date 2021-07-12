from matplotlib import colors
import pandas as pd
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from math import sqrt

direc = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University (1)\Documents\CLIMo\GPR\Processed_GPR\gpr_data\avg\GBL_25p"
print(direc)

outputfolder = r"C:\Users\ReSEC2021\OneDrive - Wilfrid Laurier University (1)\Documents\CLIMo\GPR\Processed_GPR\gpr_scatter\GBL_25p"

for fil in os.listdir(direc):
    filename = os.path.join(direc,fil)
    print(filename)

    df = pd.read_csv(filename,sep=',')
    print(df)

    fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)   
    fontP = FontProperties()
    fontP.set_size('small')
    y = df['GPR']
    y1 = df['Model']
    x2 = df['Lat_Long']
    p0 = plt.scatter(y, y, label = 'Measured',marker='s',color = 'red')
    p1 = plt.scatter(y, y1, label = 'Simulated',marker='s',color = 'blue')
    p2 = plt.plot(y, y, label = 'Simulated')

    #y = [11,20,19,17,10]
    #y_bar = [12,18,19.5,18,9]
    summation = 0  #variable to store the summation of differences
    n = len(y) #finding total number of items in list
    for i in range (0,n):  #looping through each element of the list
        difference = y[i] - y1[i]  #finding the difference between observed and predicted value
        squared_difference = difference**2  #taking square of the differene 
        summation = summation + squared_difference  #taking a sum of all the differences
    MSE = summation/n  #dividing summation by total values to obtain average
    rootMeanSquaredError = sqrt(MSE)
    print ("The Mean Square Error is: " , MSE)
    print ("The Root Mean Square Error is: " , rootMeanSquaredError)
    

    y_true = y
    y_pred =y1
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_true = y_true.reshape(len(y_true),1)
    y_pred = y_pred.reshape(len(y_pred),1)   
    diff = (y_pred-y_true)
    mbe = diff.mean()
    print('MBE = ', mbe)

    plt.xlabel("Location - (lat,long)")
    plt.title(fil[:-4])
    plt.xticks(rotation = 45)
    #plt.locator_params(axis='x', nbins=len(x)/2)
    plt.ylabel("Ice Thickness(cm)")
    #plt.ylim(50,150)
    #plt.xlim(50,150)
    plt.legend(handles=[p0,p1], loc='upper left', prop=fontP)
    #plt.legend(loc='upper left')
    #rmse = "RMSE : 2.55"
    # mbe = "MBE : -0.45"
   # plt.text(s=mbe,horizontalalignment='center', verticalalignment='center')
    plt.text(0.80, 0.15, 'MBE:'+ str(round(mbe,2)), transform=plt.gca().transAxes)
    plt.text(0.80, 0.20, 'RMSE:'+ str(round(rootMeanSquaredError,2)), transform=plt.gca().transAxes)

    # plt.text("(65.14,-123.44)", 83, rmse)
    # plt.text("(65.14,-123.44)", 81, mbe)

    plt.tight_layout()
    figfile = os.path.join(outputfolder, str(fil[:-4]) + ".png")
    plt.savefig(figfile)