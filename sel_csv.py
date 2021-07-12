import os

folder = r"C:\Users\ReSEC2021\Downloads\Deline Ice Profiles\Deline 2019-2020"

print(str(1))

for subdir, dirs, files in os.walk(folder):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        #print(subdir)
        #print(str(subdir[-12:]))
        print(str(subdir[66:76]))
        if not filepath.endswith(".csv"):
            os.remove(filepath)
        else:
            #new_name = filepath[:-5] + str(subdir[-12:]) + '.csv'
            new_name = filepath[:-5] +'_'+ str(subdir[66:76]) + '.csv'
            print(new_name)
            os.rename(filepath,new_name)


