import os;
# import geopandas;
# import fiona; 
# # help(fiona.open)

# print("this::",os.getcwd())
# url = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"
# testFile = open(os.getcwd()+"/resource/NF_A_A01000_A_A01000_000000.shp")
# df = geopandas.read_file(testFile)

# print(df)

import shapefile
from dbfread import DBF

sf = shapefile.Reader(os.getcwd()+"/resource/NF_A_B01000_A_B01000_000000.shp")
shapes = sf.shapes()

# print(shapes[0])
# print(dir(shapes[0]))
print("bbox\n",shapes[0].bbox)
print("parts\n",shapes[0].parts)
print("points\n",shapes[0].points)
print("length:\n", len(shapes))
print("shapeType\n",shapes[0].shapeType)
print("shapeTypeName\n",shapes[0].shapeTypeName)


arr = []
for record in DBF(os.getcwd()+"/resource/NF_A_B01000_A_B01000_000000.dbf"):
  # print(record)
  arr.insert(0,record)

print(arr[0])
print("length of dbf:", len(arr))
# for i in dir(shapes[0]):
#   print(i)