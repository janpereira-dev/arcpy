import arcpy

arcpy.env.workspace = r'C:\data_Jan\arcpy\arcgis_map\Errores\SanDiego.gdb'

arcpy.env.overwriteOutput = True

fc = 'Zipcodes'

fields = ['superficie_ha','SHAPE@AREA']

arcpy.AddField_management(fc, fields[0], "FLOAT")

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        row[0] = row[1] * 1/107639
        cursor.updateRow(row)

del(cursor)