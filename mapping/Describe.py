import arcpy
arcpy.env.workspace = r'C:\data_Jan\arcpy\arcgis_map\Describe\Corvallis.gdb'
featureclasses = arcpy.ListFeatureClasses()

for fc in featureclasses:
    desc = arcpy.Describe(fc)
    result = arcpy.GetCount_management(fc)
    count = int(result.getOutput(0))
    print("El nombre del FeatureClass es: {0}, de un tipo {1}, con un numero de entidades: {2} y un Sistema de Refencia Espacial de '{3}'."
        .format(desc.name, desc.shapeType, count, desc.spatialReference.name))

