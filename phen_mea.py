import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os

file_name = (r"C:\Users\ReSEC2021\Downloads\gpr.csv")

outputfolder = (r"C:\Users\ReSEC2021\Downloads\plots")

filename = pd.read_csv(r"C:\Users\ReSEC2021\Downloads\gpr.csv")
#filename['Rolling'] = filename['GPR_Th'].rolling(window=100).mean()
print(filename)


data = filename.loc[(filename["GPR_Th"] >= 80)]
data = data.loc[(data["GPR_Th"] <= 140)]
#data = data[0:5000]
data['Roll_5'] = data['GPR_Th'].rolling(window=5).mean()
data['Roll_10'] = data['GPR_Th'].rolling(window=10).mean()
data['Roll_50'] = data['GPR_Th'].rolling(window=50).mean()
data['Roll_100'] = data['GPR_Th'].rolling(window=100).mean()
data['Roll_500'] = data['GPR_Th'].rolling(window=500).mean()
data['Roll_1000'] = data['GPR_Th'].rolling(window=1000).mean()


print(data)
#data = data[0:500]
# for filename in os.listdir(folder):
#     fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)
#     dat = os.path.join(folder,filename)
#     data = pd.read_csv(dat)
data.to_csv(r'C:\Users\ReSEC2021\Downloads\gpr_out.csv')
# print(data.columns)

# print(data["DATE"])
##Get ice thickness as %

    # data['GSL_Ice_Thickness'] = data['GSL_Ice_Thickness'].div(100)
    # print(data)
    
    
    ##plotTh0
    # fig0 = plt.figure(0)    
fig, axes = plt.subplots(nrows=1,ncols=1,sharex=True,sharey=True)   
fontP = FontProperties()
fontP.set_size('small')
p0, = plt.plot(data["0p"], 'b', label="0p")
p1, = plt.plot(data["25p"], 'm' , label="25p")
p2, = plt.plot(data["50p"], 'r', label="50p")
p3, = plt.plot(data["75p"], 'g',label="75p")
p4, = plt.plot(data["100p"], 'c',label="100p")
p5, = plt.plot(data["Roll_1000"],'y', label="inSitu")
plt.ylim([40, 160])
plt.xlabel("Point")
plt.title('GPr vrs Model')  
#plt.xticks(data.DATE[::2], rotation = 45)
plt.ylabel("Ice Thickness(cm)")
plt.legend(handles=[p0, p1, p2, p3, p4, p5], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)
# plt.legend(loc='upper left')
plt.tight_layout()
figfile = os.path.join(outputfolder, 'roll_1000' + '_IC' + ".png")
plt.savefig(figfile)
