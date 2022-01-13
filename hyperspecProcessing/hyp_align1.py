import os
import PhotoScan as ps

# edit these
bands = 10
path = 'C:\\Users\\halassiter\\Dropbox\\StriplingDeliv\\Peanut\\'   # path where the band subfolders are; use \\ for slashes!
save_as = 'alignTest.psx'

# add chunk; set coordinate system to WGS84
doc = ps.app.document
chunk = doc.addChunk()
chunk.crs = ps.CoordinateSystem("EPSG::4326")

for x in range(1,bands + 1):
    # iterate through subfolders
    path2 = path + 'band' + str(x)
    files = next(os.walk(path2))[2]
    os.chdir(path2)
    # add all photos from each subfolder to same chunk
    chunk.addPhotos(files)

#load control.txt file
chunk.loadReference(path+'control.txt','csv',columns='nyxzabcs',delimiter=',',group_delimiters=False,skip_rows=0)

# set rotation accuracy to arbitrary high value
chunk.accuracy_cameras_ypr = (200,200,200)

# change to working directory and save (specify filename)
os.chdir(path)
doc.save(path = save_as)

# Next step: manually remove unneeded cameras (eg takeoff and landing), then run hyp_align2.py