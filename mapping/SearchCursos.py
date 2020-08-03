import arcpy

arcpy.env.workspace = r'C:\data_Jan\arcpy\arcgis_map\Errores\SanDiego.gdb'

fc = 'MajorAttractions'

field = ["NAME", "ADDR", "CITYNM", "ZIP"]

with arcpy.da.SearchCursor(fc, field) as cursor:
	for row in sorted(cursor):
		print('{0}\t {1}\t {2}\t {3}\n'.format(row[0], row[1], row[2], row[3]))

del(cursor)
