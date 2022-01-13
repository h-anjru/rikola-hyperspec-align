import os
import csv

# edit root directory
path = 'C:\\UFUASRP UAS Data\\Hyperscripting\\'

# get to root directory
os.chdir(path)

# initialize lists
readdata = []
newdata = []

# read CSV into list
with open('camerasOut.txt') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        readdata.append(row)

# delete first and last rows (not needed)
del readdata[0]
del readdata[-1]

# keep only needed values from CSV
for row in readdata:
        nam = row[0]
        lon = row[16]
        lat = row[17]
        alt = row[18]
        yaw = row[19]
        pit = row[20]
        rol = row[21]
        #acc = row[8]
        acc = 0.02
        newdata.append(str(nam)+','+str(lon)+','+str(lat)+','+str(alt)+','+str(yaw)+','+str(pit)+','+str(rol)+','+str(acc)+'\n')

# write new CSV
newf = open('control2.txt','w')
newf.writelines(newdata)
newf.close()

# Next step: open new Phtoscan project and run hyp_align3.py