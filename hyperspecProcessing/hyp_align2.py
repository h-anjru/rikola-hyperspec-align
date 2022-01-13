import os
import PhotoScan as ps

# edit these to match values from psAllAlign.py
path = 'C:\\Users\\halassiter\\Dropbox\\StriplingDeliv\\Peanut\\'
save_as = 'alignTest.psx'

# align photos
chunk.matchPhotos(accuracy=ps.LowAccuracy,preselection=ps.NoPreselection,filter_mask=False,keypoint_limit=4000,tiepoint_limit=2500)
chunk.alignCameras(adaptive_fitting=False)

# optimize?

# save camera locations
chunk.saveReference(path+'\\camerasOut.txt',format='csv',items='cameras')

# change to working directory and save
os.chdir(path)
doc.save(path = save_as)

# Next step: run control_txt2.py