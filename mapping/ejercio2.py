#Declaraciones
import arcpy
import arcpy.mapping as mapping
# mxd = mapping.MapDocument("CURRENT")
mxd_origen = arcpy.GetParameterAsText(0)
mxd = mapping.MapDocument(mxd_origen)
df = mapping.ListDataFrames(mxd)[0]

ParkingMeter = mapping.ListLayers(mxd)[0]
LayerUpdate = arcpy.GetParameterAsText(1)
source_update = mapping.Layer(LayerUpdate)
mapping.UpdateLayer(df,ParkingMeter,source_update)

School = mapping.Layer(arcpy.GetParameterAsText(2))
mapping.AddLayer(df,School)
mxd.findAndReplaceWorkspacePaths('C:\Student\PYTH\Map_production\Corvallis.gdb',r'C:\data_Jan\arcpy\arcgis_map\Map_Production\Corvallis.gdb')
# mxdList = mapping.ListLayers(mxd)
ParkingMeter = mapping.ListLayers(mxd)[1]
School = mapping.ListLayers(mxd)[0]
mapping.MoveLayer(df,School,ParkingMeter,"BEFORE")

mxd.title = arcpy.GetParameterAsText(3)

mxd.saveACopy(arcpy.GetParameterAsText(4))

del mxd
