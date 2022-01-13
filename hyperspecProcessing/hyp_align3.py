import os
import PhotoScan as ps

# edit these
bands = 10
path = 'C:\\Users\\halassiter\\Dropbox\\StriplingDeliv\\Peanut\\'   # path where the band subfolders are; use \\ for slashes!
save_as = 'alignTest2.psx'
outputCoordSys = "EPSG::32616"  # recommend using a projected coordinate system with units in meters (eg UTM)
res = 0.02  # resolution of orthomosiacs in m; if using an output coordinate system that is not in meters, you must convert this value!

doc = ps.app.document

# create separate chunk for each band
chunkNames = []
for x in range(bands):
    chunkNames.append('chunk'+str(x+1))

# change to working directory and save (specify filename)
os.chdir(path)
doc.save(path = save_as)

for y in range(bands):
    currentChunk = chunkNames[y]
    currentChunk = doc.addChunk()
    currentChunk.crs = ps.CoordinateSystem("EPSG::4326")
    path2 = path + 'band' + str(y+1)
    files = next(os.walk(path2))[2]
    os.chdir(path2)
    # add all photos from each subfolder to respective chunks
    currentChunk.addPhotos(files)
    currentChunk.loadReference(path+'\\control2.txt','csv',columns='nxyzabcs',delimiter=',',group_delimiters=False,skip_rows=1)
    # set rotation accuracy
    currentChunk.accuracy_cameras_ypr = (2,2,2)

print(doc.chunks)

# align photos and produce dense cloud for each chunk
for z in range(bands):
    chunk = doc.chunks[z]
    # align photos
    chunk.matchPhotos(accuracy=ps.LowAccuracy,preselection=ps.NoPreselection,filter_mask=False,keypoint_limit=4000,tiepoint_limit=2500)
    chunk.alignCameras()
    doc.save()
    # build dense cloud
    chunk.buildDenseCloud(quality = ps.HighQuality, filter = ps.AggressiveFiltering, keep_depth=False, reuse_depth=False)
    doc.save()
    # build DEM
    chunk.buildDem(source=ps.DataSource.DenseCloudData,interpolation=ps.Interpolation.EnabledInterpolation)
    doc.save()
    # build orthomosaic
    chunk.buildOrthomosaic(surface=ps.DataSource.ElevationData,blending=ps.BlendingMode.MosaicBlending,color_correction=False)
    doc.save()
    # export orthomosaic as TIF, export world file
    chunk.exportOrthomosaic(path+'\\orthoband'+str(z+1)+'.tif',format='tif',raster_transform=ps.RasterTransformType.RasterTransformNone,projection=ps.CoordinateSystem(outputCoordSys),dx=res,dy=res,write_kml=False,write_world=True,tiff_compression='none',tiff_big=False)
    doc.save()

# Next step: run QGIS_merge.py from QGIS console