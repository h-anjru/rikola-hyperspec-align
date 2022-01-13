import os

# type name of path where the band subfolders are; use \\ for slashes!
path = 'D:\\Dropbox\\StriplingDeliv\\Peanut\\'

# this stores names of band subfolders in a list; do not edit
folders = next(os.walk(path))[1]


for ii in range(0,len(folders)):
    new_path = path + folders[ii] + '\\'
    for filename in os.listdir(new_path):
        if filename.endswith('.tif'):
            os.rename(new_path + filename, path + new_path + filename[0:6] + '-' + folders[ii] + '.tif')

# Next step: run control_txt.py