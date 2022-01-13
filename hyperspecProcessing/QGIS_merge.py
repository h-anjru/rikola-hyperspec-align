import os

# edit directory with separate orthomosaics
path = 'C:\\UFUASRP UAS Data\\Hyperscripting\\'

#edit number of bands
bands = 10

# get to root directory
os.chdir(path)

# initialize list
orthoNames = []

# populate list with filenames of orthomosaics (naming convention set in hyp_align3.py)
for x in range(bands):
    orthoNames.append('"'+path+'orthoband'+str(x+1)+'.tif" ')

# initialize string
orthoList = ''

# populate string with names of orthomosaic files
for y in range(bands):
    orthoList += orthoNames[y]

# generate string for call to gdal_merge and execute
mycommand = 'gdal_merge.bat -init 0 -of GTiff -o "'+path+'orthomerge.tif" -separate '+orthoList
os.system(mycommand)