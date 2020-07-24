#Declaraciones
import arcpy
import arcpy.mapping as mapping
# mxd = mapping.MapDocument("CURRENT")
mxd = mapping.MapDocument(r'C:\data_Jan\arcpy\arcgis_map\Map_Production\CorvallisMeters.mxd')
df = mapping.ListDataFrames(mxd)[0]
ParkingMeter = mapping.ListLayers(mxd)[0]
source_update = mapping.Layer(r'C:\data_Jan\arcpy\arcgis_map\Map_Production\ParkingMeters.lyr')
mapping.UpdateLayer(df,ParkingMeter,source_update)
School = mapping.Layer(r'C:\data_Jan\arcpy\arcgis_map\Map_Production\Schools.lyr')
mapping.AddLayer(df,School)
mxd.findAndReplaceWorkspacePaths('C:\Student\PYTH\Map_production\Corvallis.gdb',r'C:\data_Jan\arcpy\arcgis_map\Map_Production\Corvallis.gdb')
# mxdList = mapping.ListLayers(mxd)
ParkingMeter = mapping.ListLayers(mxd)[1]
School = mapping.ListLayers(mxd)[0]
mapping.MoveLayer(df,School,ParkingMeter,"BEFORE")
mxd.title = "Parquimetros en Central Park"
mxd.saveACopy(r'C:\data_Jan\arcpy\arcgis_map\Map_Production\ParkimetrosMeters.mxd')
del mxd