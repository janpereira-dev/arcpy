import arcpy
arcpy.env.workspace = r'C:\data_Jan\arcpy\arcgis_map\Errores\SanDiego.gdb'
arcpy.env.overwriteOutput = True

MayorAtta = 'MajorAttractions'
Climate = 'Climate'
NewClimate = 'ClimateFilter'
NewMayorAtta = 'MajorAttractionsFilter'
MayorEnd = 'MajorAttractionsResult'
sql_Major = 'ESTAB < 1964 AND ESTAB > 0'
sql_Clima = "TYPE = 'Maritime'"

arcpy.MakeFeatureLayer_management(MayorAtta, NewMayorAtta, sql_Major)
arcpy.MakeFeatureLayer_management(Climate, NewClimate, sql_Clima)
arcpy.SelectLayerByLocation_management(NewMayorAtta, 'INTERSECT', NewClimate)
arcpy.CopyFeatures_management(NewMayorAtta, MayorEnd)

desc = arcpy.Describe(MayorEnd)
result = arcpy.GetCount_management(MayorEnd)
count = int(result.getOutput(0))

print("La nueva entidad se llama {0}, con un numero de entidades: {1}.".format(desc.name, count))

arcpy.Delete_management(MayorAtta)
arcpy.Delete_management(Climate)
arcpy.Delete_management(NewClimate)
arcpy.Delete_management(NewMayorAtta)