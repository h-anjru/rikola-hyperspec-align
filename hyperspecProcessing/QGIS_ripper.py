import os
import glob

#set number of bands below
numbands = 10

#set path of images below
mypath = 'D:\Dropbox\Stripling\StriplingCorn1Hyp\\'

ii = 0
for infile in os.listdir(mypath):
    if infile.endswith(".dat") :
        ii = ii+1
        print("working on "+infile)
        for bandnum in range(1, numbands+1):
            if not os.path.exists(mypath+"band"+str(bandnum)+"\\"):
                os.makedirs(mypath+"band"+str(bandnum)+"\\")
            mycommand = "gdal_translate -b "+str(bandnum)+" \""+mypath+infile+"\""+" \""+mypath+"band"+str(bandnum)+"\\"+infile+"band"+str(bandnum)+".tif"+"\""
            os.system(mycommand)

#Next step: run rip_rename.py