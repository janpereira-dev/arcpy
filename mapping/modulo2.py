import arcpy
arcpy.env.workspace = r'C:\data_Jan\arcpy\arcgis_map\Describe\Corvallis.gdb'
rowValues = [
    ['Benton', (-123.40, 44.49)],
    ['Linn', (-122.49, 44.48)],
    ['Polk', (-123.38, 44.89)],
    ['Tillamook', (-123.65, 45.45)]
]

rowValues[2]
arcpy.env.overwriteOutput = True
out_path = r'C:\data_Jan\arcpy\arcgis_map\Describe\Corvallis.gdb'
out_name = 'NewPoints.shp'
geometry_type = 'POINT'
template = r'C:\data_Jan\arcpy\arcgis_map\Describe\Corvallis.gdb\WaterMeter'
has_m = 'DISABLED'
has_z = 'DISABLED'

spatial_ref = arcpy.Describe(r'C:\data_Jan\arcpy\arcgis_map\Describe\Corvallis.gdb').spatialReference
spatial_ref = arcpy.Describe("MajorAttractions").spatialReference
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_ref)
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z)
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type)
arcpy.CreateFeatureclass_management(arcpy.env.workspace, out_name, geometry_type)
arcpy.CreateFeatureclass_management(arcpy.env.workspace, 'NewPoints', geometry_type)

