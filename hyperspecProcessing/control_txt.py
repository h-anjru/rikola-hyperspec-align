# Generates a control file in text format from Rikola TASKFILE for use in Agisoft Photoscan
# Each line will be in format: image_name,lat[dd.dd],lon[dd.dd],alt[m],yaw[dd.dd],pitch,roll,accuracy[m]
# Image name is in format 'K00000-band1.tif' as per rip_rename.py
# Altitude is assumed to be 0.
# Yaw is a contrived number with no effect on solution; it is used only to assist in 
#     sorting the control data within Photoscan.
# Pitch and roll are simply set to 0.
# Accuracy is set to 5 m for the control band (assumed to be band 1); the rest are set to 
#     contrived value of 1000 m.
# If no GNSS data, line is left blank

import os

# type name of path where the relevant TASKFILE.TXT is
path = 'C:\\Users\\halassiter\\Dropbox\\Stripling\\Peanut\\Hyperspectral\\'

# edit number of bands
bands = 10

# edit assumed altitude[m] if you want
alt = 0

os.chdir(path)
f = open('TASKFILE.TXT','r')

with f as myfile:
    data = myfile.readlines()

newdata = []


for x in range(45,len(data)):  # line 46 (45 in Python) is where control data begins
    loc = data[x].find(',N,')   # look for control data in each string in list generated from TASKFILE
    if loc == -1:               # if sequence ',N,' not found in line, find() returns -1
        newdata.append('\n')     # blank line if no control data
    else:
        latdm = float(data[x][loc-9:loc])
        londm = float(data[x][loc+3:loc+13])
        lat = int(.01*latdm) + 5.0/3 * (.01*latdm-int(.01*latdm))     # convert degrees/decimal minutes to decimal degrees
        lon = -(int(.01*londm) + 5.0/3 * (.01*londm-int(.01*londm)))  # DDMM.mm -> DD.dd (assumed Western hemisphere)
        for y in range(1,bands+1):                                 # write new list of strings in format ref'd above
            if y == 1:
                newdata.append(data[x][0:6]+'-band'+str(y)+'.tif,'+str(lat)+','+str(lon)+',0,'+str(0.1*float(y))+','+str(alt)+',0,5\n')
            else:
                newdata.append(data[x][0:6]+'-band'+str(y)+'.tif,'+str(lat)+','+str(lon)+',0,'+str(0.1*float(y))+','+str(alt)+',0,1000\n')

newf = open('control.txt','w')
newf.writelines(newdata)
newf.close()

# Next step: open Photoscan and run hyp_align1.py