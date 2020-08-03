rowValues = [
    ['Benton', (-123.40, 44.49)],
    ['Linn', (-122.49, 44.48)],
    ['Polk', (-123.38, 44.89)],
    ['Tillamook', (-123.65, 45.45)]
]

cursor = arcpy.da.InsertCursor('C:/data/texas.gdb/counties',
                               ['NAME', 'SHAPE@XY'])