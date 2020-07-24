
import arcpy

import arcpy.mapping as mapping

arcpy.env.workspace = r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb'

mxd = mapping.MapDocument(r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\CorvallisMeters.mxd')

mxd.relativePaths

mxd.title

mapping.ListBrokenDataSources(mxd)

list_perdidas = mapping.ListBrokenDataSources(mxd)

for capas in list_perdidas:
    print capas.name

mxd.findAndReplaceWorkspacePaths(r'C:\Student\PYTH\Map_production\Corvallis.gdb',r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb')

mxd.findAndReplaceWorkspacePaths(r'C:\Student\PYTH\Map_production\Corvallis.gdb',r'\\Map_Production\Corvallis.gdb')

mxd.findAndReplaceWorkspacePaths(r'C:\Student\PYTH\Map_production\Corvallis.gdb','C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb')

mxd.findAndReplaceWorkspacePaths('C:\Student\PYTH\Map_production\Corvallis.gdb','C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb')

mxd.findAndReplaceWorkspacePaths('C:\Student\PYTH\Map_production\Corvallis.gdb',r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb')

mxd = mapping.MapDocument("CURRENT")

mxd.findAndReplaceWorkspacePaths('C:\Student\PYTH\Map_production\Corvallis.gdb',r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Corvallis.gdb')

df = mapping.ListDataFrames(mxd)

layers = mapping.ListLayers(mxd)

for capas in layers:
    print capas.name

for dataframe in df:
    print dataframe


for dataframe in df:
    print dataframe.name

mapping.Layer(r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\ParkingMeters.lyr')

pakingNew = mapping.Layer(r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\ParkingMeters.lyr')

# mapping.AddLayer(df,pakingNew,"TOP")

# mapping.AddLayer(mxd,pakingNew,"TOP")

# mapping.AddLayer(mxd,pakingNew,"TOP")

SchoolsNew = mapping.Layer(r'C:\Users\jan.pereira\Desktop\janpereira\Map_Production\Schools.lyr')

# mapping.AddLayer(df,SchoolsNew,"TOP")


# mapping.AddLayer(dataFrame,SchoolsNew,"TOP")

# dataFrame = arcpy.mapping.ListDataFrames(mxd, df_Target)[0]

df_Target = arcpy.GetParameterAsText(1)

dataFrame = arcpy.mapping.ListDataFrames(mxd, df_Target)[0]

mapping.AddLayer(dataFrame,SchoolsNew,"TOP")

mapping.UpdateLayer(dataFrame,layers[0],pakingNew)
