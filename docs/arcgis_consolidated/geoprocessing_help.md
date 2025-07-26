# Geoprocessing and Analysis Help

*Consolidated from 93 individual documentation files*

---

## Understand skyline analysis

## Code Samples

### Example 1

```python
Geographic = (450 - Arithmetic) mod 360
```

### Example 2

```python
Geographic = (450 - Arithmetic) mod 360
```

### Example 3

```python
Geographic = (450 - Arithmetic) mod 360
```

### Example 4

```python
Geographic = (450 - Arithmetic) mod 360
```

### Example 5

```python
(450 - 180) mod 360 = 270 (west)
```

### Example 6

```python
(450 - 180) mod 360 = 270 (west)
```

### Example 7

```python
(450 - 30) mod 360 = 420 mod 360 = 60
```

### Example 8

```python
(450 - 30) mod 360 = 420 mod 360 = 60
```

---

## Work with interesting facts panels

## Code Samples

### Example 1

```python
if (site var value >= median var value) {        
   score = ((site var value - median var value) / (max var value - median var value)) * 100;
} else {
   score = ((median var value - site var value) / (median var value - min var value)) * 100;
}
```

### Example 2

```python
if (site var value >= median var value) {        
   score = ((site var value - median var value) / (max var value - median var value)) * 100;
} else {
   score = ((median var value - site var value) / (median var value - min var value)) * 100;
}
```

---

## Python and geoprocessing

## Code Samples

### Example 1

```python
import arcpy

roads = "c:/base/data.gdb/roads"
output = "c:/base/data.gdb/roads_Buffer"

# Run Buffer
arcpy.analysis.Buffer(roads, output, "100 Feet")
```

### Example 2

```python
import arcpy

roads = "c:/base/data.gdb/roads"
output = "c:/base/data.gdb/roads_Buffer"

# Run Buffer
arcpy.analysis.Buffer(roads, output, "100 Feet")
```

### Example 3

```python
import arcpy
arcpy.management.AddField("schools", "school_id", "LONG", "", "", "", "", "NON_NULLABLE")
```

### Example 4

```python
import arcpy
arcpy.management.AddField("schools", "school_id", "LONG", "", "", "", "", "NON_NULLABLE")
```

### Example 5

```python
import arcpy
arcpy.management.AddField("schools", "school_id", "LONG", field_is_nullable="NON_NULLABLE")
```

### Example 6

```python
import arcpy
arcpy.management.AddField("schools", "school_id", "LONG", field_is_nullable="NON_NULLABLE")
```

### Example 7

```python
import arcpy

arcpy.env.workspace = "c:/city/data.gdb"

# Geoprocessing tools return a Result object 
result = arcpy.management.CopyFeatures("roads", "urban_roads")

# A print function will display the string representation of the output.
print(result)

# A Result object can be indexed to get the output value.
result_value = result[0]
```

### Example 8

```python
import arcpy

arcpy.env.workspace = "c:/city/data.gdb"

# Geoprocessing tools return a Result object 
result = arcpy.management.CopyFeatures("roads", "urban_roads")

# A print function will display the string representation of the output.
print(result)

# A Result object can be indexed to get the output value.
result_value = result[0]
```

### Example 9

```python
import arcpy
arcpy.env.workspace = "c:/city/data.gdb"

result = arcpy.management.CopyFeatures("roads", "#")
```

### Example 10

```python
import arcpy
arcpy.env.workspace = "c:/city/data.gdb"

result = arcpy.management.CopyFeatures("roads", "#")
```

---

## Use a geoprocessing tool

## Code Samples

### Example 1

```python
<Geoprocessing>
  <ToolParameters>
    <Parameter toolName="calculatefield" toolboxAlias="management" name="expression_type" isLocked="true">ARCADE</Parameter>
  </ToolParameters>
</Geoprocessing>
```

### Example 2

```python
<Geoprocessing>
  <ToolParameters>
    <Parameter toolName="calculatefield" toolboxAlias="management" name="expression_type" isLocked="true">ARCADE</Parameter>
  </ToolParameters>
</Geoprocessing>
```

---

## Write geoprocessing output to memory

## Code Samples

### Example 1

```python
# Set the workspace and list the data saved to memory
arcpy.env.workspace = "memory"

print(f"Memory Feature Classes: {arcpy.ListFeatureClasses()}")
print(f"Memory Rasters: {arcpy.ListRasters()}")
print(f"Memory Tables: {arcpy.ListTables()}")
```

### Example 2

```python
# Set the workspace and list the data saved to memory
arcpy.env.workspace = "memory"

print(f"Memory Feature Classes: {arcpy.ListFeatureClasses()}")
print(f"Memory Rasters: {arcpy.ListRasters()}")
print(f"Memory Tables: {arcpy.ListTables()}")
```

### Example 3

```python
import arcpy

# Set the geoprocessing workspace
arcpy.env.workspace = r"C:\Data\Habitat.gdb"

# Buffer a Roads layer, writing output to memory 
arcpy.analysis.Buffer("Roads", r"memory\Buffers", 1000)

# Erase the buffers from a Vegetation layer
arcpy.analysis.Erase("Vegetation", r"memory\Buffers", r"memory\Erased")

# Dissolve the memory output of Erase to make a final output in the gdb workspace
arcpy.management.Dissolve(r"memory\Erased", "FinalOutput")
```

### Example 4

```python
import arcpy

# Set the geoprocessing workspace
arcpy.env.workspace = r"C:\Data\Habitat.gdb"

# Buffer a Roads layer, writing output to memory 
arcpy.analysis.Buffer("Roads", r"memory\Buffers", 1000)

# Erase the buffers from a Vegetation layer
arcpy.analysis.Erase("Vegetation", r"memory\Buffers", r"memory\Erased")

# Dissolve the memory output of Erase to make a final output in the gdb workspace
arcpy.management.Dissolve(r"memory\Erased", "FinalOutput")
```

---

## Use Arcade expressions in charts

## Code Samples

### Example 1

```python
# Format "CALIFORNIA" as "California"
Proper($feature.STATE_NAME);
```

### Example 2

```python
# Format "CALIFORNIA" as "California"
Proper($feature.STATE_NAME);
```

### Example 3

```python
# Combine CITY_NAME (eg "LOS_ANGELES") and STATE_NAME (eg "CALIFORNIA") into "LOS_ANGELES, CALIFORNIA"
Concatenate($feature.CITY_NAME, ", ", $feature.STATE_NAME);
```

### Example 4

```python
# Combine CITY_NAME (eg "LOS_ANGELES") and STATE_NAME (eg "CALIFORNIA") into "LOS_ANGELES, CALIFORNIA"
Concatenate($feature.CITY_NAME, ", ", $feature.STATE_NAME);
```

### Example 5

```python
# Split string on "," and return the second element (ie, the city name)
Split($feature.FULL_ADDRESS, ",")[1];
```

### Example 6

```python
# Split string on "," and return the second element (ie, the city name)
Split($feature.FULL_ADDRESS, ",")[1];
```

### Example 7

```python
if (Find($feature.EVENT_TYPE, "TORNADO") >= 0) {
    return "Tornado";
} else { 
    return "Other";
}
```

### Example 8

```python
if (Find($feature.EVENT_TYPE, "TORNADO") >= 0) {
    return "Tornado";
} else { 
    return "Other";
}
```

### Example 9

```python
Date($feature.YEAR, $feature.MONTH, $feature.DAY);
```

### Example 10

```python
Date($feature.YEAR, $feature.MONTH, $feature.DAY);
```

### Example 11

```python
DateDiff($feature.OPEN_DATE, $feature.CLOSE_DATE, "DAYS");
```

### Example 12

```python
DateDiff($feature.OPEN_DATE, $feature.CLOSE_DATE, "DAYS");
```

### Example 13

```python
ISOWeekday($feature.DATE);
```

### Example 14

```python
ISOWeekday($feature.DATE);
```

### Example 15

```python
$feature.POPULATION / AreaGeodetic($feature, 'square-miles')
```

### Example 16

```python
$feature.POPULATION / AreaGeodetic($feature, 'square-miles')
```

### Example 17

```python
Average([$feature.SCORE1, $feature.SCORE2, $feature.SCORE3])
```

### Example 18

```python
Average([$feature.SCORE1, $feature.SCORE2, $feature.SCORE3])
```

### Example 19

```python
if ($feature.MILES_PER_GALLON >= 30) {
    return "Good"
} else if ($feature.MILES_PER_GALLON >= 20) {
    return "Okay"
} else {
    return "Poor"
}
```

### Example 20

```python
if ($feature.MILES_PER_GALLON >= 30) {
    return "Good"
} else if ($feature.MILES_PER_GALLON >= 20) {
    return "Okay"
} else {
    return "Poor"
}
```

---

## Export a model to Python

## Code Samples

### Example 1

```python
def Model(InputFC=r"C:\Data.gdb\inFC", Output="C:\Output.gdb\outFC", Extent="1186925.51155726 -2378062.72079588 1240005.19719053 -2315230.04252389", Name="Canada Goose"):
```

### Example 2

```python
def Model(InputFC=r"C:\Data.gdb\inFC", Output="C:\Output.gdb\outFC", Extent="1186925.51155726 -2378062.72079588 1240005.19719053 -2315230.04252389", Name="Canada Goose"):
```

### Example 3

```python
arcpy.analysis.Buffer(in_features=_Name_.__str__().format(**locals(),**globals())if isinstance(_Name_, str) else _Name_, out_feature_class=Name_Buffer, buffer_distance_or_field="10 Meters")
```

### Example 4

```python
arcpy.analysis.Buffer(in_features=_Name_.__str__().format(**locals(),**globals())if isinstance(_Name_, str) else _Name_, out_feature_class=Name_Buffer, buffer_distance_or_field="10 Meters")
```

### Example 5

```python
arcpy.Statistics_analysis(in_table=a, out_table=b, statistics_fields=[["Type", "COUNT"], ["Year", "COUNT"]], case_field=["Type"])
```

### Example 6

```python
arcpy.Statistics_analysis(in_table=a, out_table=b, statistics_fields=[["Type", "COUNT"], ["Year", "COUNT"]], case_field=["Type"])
```

### Example 7

```python
field_mapping="Type \"Type\" true true false 20 Text 0 0,First,#,InputFC,Type,0,20;Year \"Year\" true true false 2 Short 0 0,First,#,InputFC,Year,-1,-1)
```

### Example 8

```python
field_mapping="Type \"Type\" true true false 20 Text 0 0,First,#,InputFC,Type,0,20;Year \"Year\" true true false 2 Short 0 0,First,#,InputFC,Year,-1,-1)
```

### Example 9

```python
import arcpy

def GnatcatcherHabitat():  # Gnatcatcher Habitat

    # Model Environment settings
    with arcpy.EnvManager(extent="3434731.64703611 -1534445.99025604 3485825.15860115 -1466080.56806995")

        # Process: Buffer (Buffer) 
        with arcpy.EnvManager(extent="1187538.76766617 -2377527.90888239 1230418.76331601 -2319961.0344503")
            arcpy.Buffer_analysis(in_features=r"C:\Data.gdb\A", out_feature_class=r"C:\Output.gdb\B", buffer_distance_or_field="500 Meters", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE",dissolve_field=[], method="PLANAR")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Output.gdb\", workspace=r"C:\Data.gdb\"):
        GnatcatcherHabitat()
```

### Example 10

```python
import arcpy

def GnatcatcherHabitat():  # Gnatcatcher Habitat

    # Model Environment settings
    with arcpy.EnvManager(extent="3434731.64703611 -1534445.99025604 3485825.15860115 -1466080.56806995")

        # Process: Buffer (Buffer) 
        with arcpy.EnvManager(extent="1187538.76766617 -2377527.90888239 1230418.76331601 -2319961.0344503")
            arcpy.Buffer_analysis(in_features=r"C:\Data.gdb\A", out_feature_class=r"C:\Output.gdb\B", buffer_distance_or_field="500 Meters", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE",dissolve_field=[], method="PLANAR")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Output.gdb\", workspace=r"C:\Data.gdb\"):
        GnatcatcherHabitat()
```

### Example 11

```python
if a and b:
    arcpy.Buffer_analysis(in_features=inFC, out_feature_class=outFC, buffer_distance_or_field="10 Meters", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")
```

### Example 12

```python
if a and b:
    arcpy.Buffer_analysis(in_features=inFC, out_feature_class=outFC, buffer_distance_or_field="10 Meters", line_side="FULL", line_end_type="ROUND", dissolve_option="NONE", dissolve_field=[], method="PLANAR")
```

### Example 13

```python
output = arcpy.JoinField_management(in_data=infc, in_field="Type", join_table=joinTable, join_field="Type", fields=["Year"])[0]
```

### Example 14

```python
output = arcpy.JoinField_management(in_data=infc, in_field="Type", join_table=joinTable, join_field="Type", fields=["Year"])[0]
```

---

## 00144: ArcGIS Server does not have the product or extension license <value> needed for tool <value>



---

## 00153: Cannot use result map service because output parameter <value> in task <value> is written to in-memory



---

## 00249: You cannot publish network analysis services with attribute parameters that are defined as arrays.



---

## 00393: At server version <value> the <value> task's parameter's data type <value> is not supported



---

## 24032: Data source used by tool <value> is not registered with the server and will be copied to the server: <value>



---

## Web tool properties advanced settings

## Code Samples

### Example 1

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "reusejobdir": true,
        "executionType": "Synchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

### Example 2

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "reusejobdir": true,
        "executionType": "Synchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

### Example 3

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "logGPMessages": true,
        "executionType": "Asynchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

### Example 4

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "logGPMessages": true,
        "executionType": "Asynchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

---

## Authoring geoprocessing services with Python scripts

## Code Samples

### Example 1

```python
import arcpy
import os

# The ArcGIS Project is used to build paths from the defaultGeodatabase and 
# homeFolder using os.path.join

# Reference the CURRENT project with ArcGIS Pro open, or point to an .aprx on 
# disk
prj = arcpy.mp.ArcGISProject("CURRENT")
arcpy.CopyFeatures_management(os.path.join(prj.defaultGeodatabase, "study_sites"), 
                              "in_memory/tempSite")

# Create a variable to reference the LYRX folder
lyrxFolder = os.path.join(prj.homeFolder, "LYRXs")
arcpy.ApplySymbologyFromLayer_management("in_memory/tempSite", 
                                         os.path.join(lyrxFolder, "Site4.lyrx"))
```

### Example 2

```python
import arcpy
import os

# The ArcGIS Project is used to build paths from the defaultGeodatabase and 
# homeFolder using os.path.join

# Reference the CURRENT project with ArcGIS Pro open, or point to an .aprx on 
# disk
prj = arcpy.mp.ArcGISProject("CURRENT")
arcpy.CopyFeatures_management(os.path.join(prj.defaultGeodatabase, "study_sites"), 
                              "in_memory/tempSite")

# Create a variable to reference the LYRX folder
lyrxFolder = os.path.join(prj.homeFolder, "LYRXs")
arcpy.ApplySymbologyFromLayer_management("in_memory/tempSite", 
                                         os.path.join(lyrxFolder, "Site4.lyrx"))
```

### Example 3

```python
import arcpy
import myutils

inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 4

```python
import arcpy
import myutils

inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 5

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
# for the duration of this script.
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils  # A Python file within myPythonModules
```

### Example 6

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
# for the duration of this script.
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils  # A Python file within myPythonModules
```

---

## Authoring web tools with Python scripts

## Code Samples

### Example 1

```python
import arcpy
import os

# The ArcGIS Project is used to build paths from the defaultGeodatabase and 
# homeFolder using os.path.join

# Reference the CURRENT project with ArcGIS Pro open, or point to an .aprx on 
# disk
prj = arcpy.mp.ArcGISProject("CURRENT")
arcpy.CopyFeatures_management(os.path.join(prj.defaultGeodatabase, "study_sites"), 
                              "in_memory/tempSite")

# Create a variable to reference the LYRX folder
lyrxFolder = os.path.join(prj.homeFolder, "LYRXs")
arcpy.ApplySymbologyFromLayer_management("in_memory/tempSite", 
                                         os.path.join(lyrxFolder, "Site4.lyrx"))
```

### Example 2

```python
import arcpy
import os

# The ArcGIS Project is used to build paths from the defaultGeodatabase and 
# homeFolder using os.path.join

# Reference the CURRENT project with ArcGIS Pro open, or point to an .aprx on 
# disk
prj = arcpy.mp.ArcGISProject("CURRENT")
arcpy.CopyFeatures_management(os.path.join(prj.defaultGeodatabase, "study_sites"), 
                              "in_memory/tempSite")

# Create a variable to reference the LYRX folder
lyrxFolder = os.path.join(prj.homeFolder, "LYRXs")
arcpy.ApplySymbologyFromLayer_management("in_memory/tempSite", 
                                         os.path.join(lyrxFolder, "Site4.lyrx"))
```

### Example 3

```python
import arcpy
import myutils

inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 4

```python
import arcpy
import myutils

inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 5

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
# for the duration of this script.
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils  # A Python file within myPythonModules
```

### Example 6

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
# for the duration of this script.
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils  # A Python file within myPythonModules
```

---

## Geoprocessing service settings: Advanced properties

## Code Samples

### Example 1

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "reusejobdir": "true",
        "executionType": "Synchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

### Example 2

```python
{
    "serviceName": "sample",
    "type": "GPServer",
    "manyotherkeys": "manyothervalues",
    "properties": {
        "manyotherkeys": "manyothervalues",
        "reusejobdir": "true",
        "executionType": "Synchronous"
    },
    "portalProperties": {},
    "extensions": []
}
```

---

## Packaging Python scripts

## Code Samples

### Example 1

```python
import arcpy
import os
import sys

# Get the pathname to this script, then strip off the
#  script file name to yield the containing folder
#
scriptPath = sys.path[0]
thisFolder = os.path.dirname(scriptPath)

# Construct paths to ../ToolData/SanFrancisco.gdb/Streets and
#                    ../ToolData/Warehouse.lyr
#
toolDataPath = os.path.join(thisFolder, "ToolData")
streetFeatures = os.path.join(toolDataPath, "SanFrancisco.gdb", "Streets")
streetLyr = os.path.join(toolDataPath, "Warehouse.lyr")
```

### Example 2

```python
import arcpy
import os
import sys

# Get the pathname to this script, then strip off the
#  script file name to yield the containing folder
#
scriptPath = sys.path[0]
thisFolder = os.path.dirname(scriptPath)

# Construct paths to ../ToolData/SanFrancisco.gdb/Streets and
#                    ../ToolData/Warehouse.lyr
#
toolDataPath = os.path.join(thisFolder, "ToolData")
streetFeatures = os.path.join(toolDataPath, "SanFrancisco.gdb", "Streets")
streetLyr = os.path.join(toolDataPath, "Warehouse.lyr")
```

### Example 3

```python
streetFeatures = 'e:/Warehousing/ToolData/SanFrancisco.gdb/Streets'
```

### Example 4

```python
streetFeatures = 'e:/Warehousing/ToolData/SanFrancisco.gdb/Streets'
```

### Example 5

```python
toolDataPath = r'e:\Warehousing\ToolData'
warehouseLyr = os.path.join(toolDataPath, "Warehouse.lyrx")
```

### Example 6

```python
toolDataPath = r'e:\Warehousing\ToolData'
warehouseLyr = os.path.join(toolDataPath, "Warehouse.lyrx")
```

### Example 7

```python
thePath = r"E:\data\telluride\newdata.gdb\slopes"
```

### Example 8

```python
thePath = r"E:\data\telluride\newdata.gdb\slopes"
```

### Example 9

```python
import arcpy
import myutils
inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 10

```python
import arcpy
import myutils
inFeatures = arcpy.GetParameterAsText(0)
inFID = myutils.getFIDName(inFeatures)
```

### Example 11

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
#  for the duration of this script.
#
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils # a Python file within myPythonModules
```

### Example 12

```python
import arcpy
import sys
import os

# Append the path to the utility modules to the system path
#  for the duration of this script.
#
myPythonModules = r'e:\Warehousing\Scripts'
sys.path.append(myPythonModules)
import myutils # a Python file within myPythonModules
```

---

## Use geoprocessing services in Python scripts

## Code Samples

### Example 1

```python
# arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;<optional folder>/<service name>;{username};{password}")
arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;GPFolder/BufferService;serverusername;serverpassword")
```

### Example 2

```python
# arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;<optional folder>/<service name>;{username};{password}")
arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;GPFolder/BufferService;serverusername;serverpassword")
```

### Example 3

```python
import arcpy
import time

arcpy.ImportToolbox("http://machine.domain.com/webadaptor/services;Elevation/viewshedAlias;serverusername;serverpassword")

result = arcpy.Viewshed_viewshedAlias(r'c:\data\inputPoint.shp', "10000 Kilometers")

while result.status < 4:
	   print(result.status)
	   time.sleep(0.2)
print("Execution Finished")

print(result.getMessages())
arcpy.CopyFeatures_management(result[0], 'localResult.shp')
```

### Example 4

```python
import arcpy
import time

arcpy.ImportToolbox("http://machine.domain.com/webadaptor/services;Elevation/viewshedAlias;serverusername;serverpassword")

result = arcpy.Viewshed_viewshedAlias(r'c:\data\inputPoint.shp', "10000 Kilometers")

while result.status < 4:
	   print(result.status)
	   time.sleep(0.2)
print("Execution Finished")

print(result.getMessages())
arcpy.CopyFeatures_management(result[0], 'localResult.shp')
```

### Example 5

```python
{"geometryType" : "esriGeometryPoint",
"spatialReference" : {"wkid" : 54003},
'features':[{'geometry':{'x': -13308192.1956127,
'y':  4221903.58555983}}]}
```

### Example 6

```python
{ 'distance' : 8.5, 'units' : 'esriMiles' }
```

### Example 7

```python
https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute?Input_Observation_Point={%22features%22%3A[{%22geometry%22%3A{%22x%22%3A-13308192.1956127%2C%22y%22%3A4221903.58555983}}]}&Viewshed_Distance={+%27distance%27+%3A+8.5%2C+%27units%27+%3A+%27esriMiles%27+}&env%3AoutSR=&env%3AprocessSR=&f=pjson
```

### Example 8

```python
https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute?Input_Observation_Point={%22features%22%3A[{%22geometry%22%3A{%22x%22%3A-13308192.1956127%2C%22y%22%3A4221903.58555983}}]}&Viewshed_Distance={+%27distance%27+%3A+8.5%2C+%27units%27+%3A+%27esriMiles%27+}&env%3AoutSR=&env%3AprocessSR=&f=pjson
```

### Example 9

```python
# Requires Python 3+
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json

inPts = {"geometryType" : "esriGeometryPoint",
         "spatialReference" : {"wkid" : 54003},
         'features':[{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance':8.5,'units':'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

URL = 'https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute'

req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
response = urlopen.urlopen(req)
response_bytes = response.read()
print(json.loads(response_bytes.decode('UTF-8')))
```

### Example 10

```python
# Requires Python 3+
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json

inPts = {"geometryType" : "esriGeometryPoint",
         "spatialReference" : {"wkid" : 54003},
         'features':[{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance':8.5,'units':'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

URL = 'https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute'

req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
response = urlopen.urlopen(req)
response_bytes = response.read()
print(json.loads(response_bytes.decode('UTF-8')))
```

### Example 11

```python
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json
import time

def sendReq(URL, data=None):

    req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
    response = urlopen.urlopen(req)
    response_bytes = response.read()
    return json.loads(response_bytes.decode('UTF-8'))

inPts = {"geometryType": "esriGeometryPoint",
         "spatialReference": {"wkid" : 54003},
         'features': [{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance': 8.5, 'units': 'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

taskUrl = "https://machine.domain.com/webadaptor/rest/services/Elevation/GPServer/viewshed"
submitUrl = taskUrl + "/submitJob"

submitJson = sendReq(submitUrl, data)

if 'jobId' in submitJson:
    jobID = submitJson['jobId']
    status = submitJson['jobStatus']
    jobUrl = taskUrl + "/jobs/" + jobID

    while status == "esriJobSubmitted" or status == "esriJobExecuting":
        print("checking to see if job is completed...")
        time.sleep(1)

        jobJson = sendReq(jobUrl, {"f": "json"})

        if 'jobStatus' in jobJson.keys():
            status = jobJson['jobStatus']

            if status == "esriJobSucceeded":
                if 'results' in jobJson:
                    resultsJson = jobJson['results']
                    for paramName in resultsJson.keys():
                        resultsUrl = jobUrl + "/" + resultsJson[paramName]['paramUrl']
                        resultJson = sendReq(resultsUrl, {"f": "json"})
                        print(resultJson)

            if status == "esriJobFailed":
                if 'messages' in jobJson.keys():
                    print(jobJson['messages'])

else:
    print("no jobId found in the response")
```

### Example 12

```python
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json
import time

def sendReq(URL, data=None):

    req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
    response = urlopen.urlopen(req)
    response_bytes = response.read()
    return json.loads(response_bytes.decode('UTF-8'))

inPts = {"geometryType": "esriGeometryPoint",
         "spatialReference": {"wkid" : 54003},
         'features': [{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance': 8.5, 'units': 'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

taskUrl = "https://machine.domain.com/webadaptor/rest/services/Elevation/GPServer/viewshed"
submitUrl = taskUrl + "/submitJob"

submitJson = sendReq(submitUrl, data)

if 'jobId' in submitJson:
    jobID = submitJson['jobId']
    status = submitJson['jobStatus']
    jobUrl = taskUrl + "/jobs/" + jobID

    while status == "esriJobSubmitted" or status == "esriJobExecuting":
        print("checking to see if job is completed...")
        time.sleep(1)

        jobJson = sendReq(jobUrl, {"f": "json"})

        if 'jobStatus' in jobJson.keys():
            status = jobJson['jobStatus']

            if status == "esriJobSucceeded":
                if 'results' in jobJson:
                    resultsJson = jobJson['results']
                    for paramName in resultsJson.keys():
                        resultsUrl = jobUrl + "/" + resultsJson[paramName]['paramUrl']
                        resultJson = sendReq(resultsUrl, {"f": "json"})
                        print(resultJson)

            if status == "esriJobFailed":
                if 'messages' in jobJson.keys():
                    print(jobJson['messages'])

else:
    print("no jobId found in the response")
```

---

## Use geoprocessing services in web apps

## Code Samples

### Example 1

```python
// esri.tasks.Geoprocessor is required for using Geoprocessor.
//  Add it along with other dojo.require statements.
dojo.require(esri.tasks.Geoprocessor); 

// Step 1: Initialize the geoprocessing and point to the REST URL
var gpUrl = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed";
var gp = new Geoprocessor(gpUrl);	

// Set output spatial reference 
gp.outSpatialReference = { wkid: 102100 };

function computeViewshed(event) { 
   graphicsLayer.removeAll();

   // Step 2: Set up input parameters and assign or collect inputs from user
   var point = new Point({ 
        longitude: event.mapPoint.longitude,
        latitude: event.mapPoint.latitude  
   });  

   var inputGraphic = new Graphic({
      geometry: point, 
      symbol: markerSymbol 
   }); 
   graphicsLayer.add(inputGraphic); 

   var inputGraphicContainer = [];
   inputGraphicContainer.push(inputGraphic);
   var featureSet = new FeatureSet();
   featureSet.features = inputGraphicContainer;  

   var vsDistance = new LinearUnit();  
   vsDistance.distance = 5;
   vsDistance.units = "miles";  
   var params = {  
      "Input_Observation_Point": featureSet,
      "Viewshed_Distance": vsDistance  
   };  

   // Step 3: Run the service. In this instance, the service is Synchronous; Execute
   // will be called. An Asynchronous service will use gp.submitJob.
   gp.execute(params).then(drawResultData); 
}  

// Step 4: Render the result. Symbology is assigned and the graphics are added to the map.
function drawResultData(result) { 
   var resultFeatures = result.results[0].value.features;  
   // Assign each resulting graphic a symbol  
   var viewshedGraphics = resultFeatures.map(function(feature) { 
      feature.symbol = fillSymbol;     
      return feature; 
   });       
   // Add the resulting graphics to the graphics layer  
   graphicsLayer.addMany(viewshedGraphics);
}
```

### Example 2

```python
// esri.tasks.Geoprocessor is required for using Geoprocessor.
//  Add it along with other dojo.require statements.
dojo.require(esri.tasks.Geoprocessor); 

// Step 1: Initialize the geoprocessing and point to the REST URL
var gpUrl = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed";
var gp = new Geoprocessor(gpUrl);	

// Set output spatial reference 
gp.outSpatialReference = { wkid: 102100 };

function computeViewshed(event) { 
   graphicsLayer.removeAll();

   // Step 2: Set up input parameters and assign or collect inputs from user
   var point = new Point({ 
        longitude: event.mapPoint.longitude,
        latitude: event.mapPoint.latitude  
   });  

   var inputGraphic = new Graphic({
      geometry: point, 
      symbol: markerSymbol 
   }); 
   graphicsLayer.add(inputGraphic); 

   var inputGraphicContainer = [];
   inputGraphicContainer.push(inputGraphic);
   var featureSet = new FeatureSet();
   featureSet.features = inputGraphicContainer;  

   var vsDistance = new LinearUnit();  
   vsDistance.distance = 5;
   vsDistance.units = "miles";  
   var params = {  
      "Input_Observation_Point": featureSet,
      "Viewshed_Distance": vsDistance  
   };  

   // Step 3: Run the service. In this instance, the service is Synchronous; Execute
   // will be called. An Asynchronous service will use gp.submitJob.
   gp.execute(params).then(drawResultData); 
}  

// Step 4: Render the result. Symbology is assigned and the graphics are added to the map.
function drawResultData(result) { 
   var resultFeatures = result.results[0].value.features;  
   // Assign each resulting graphic a symbol  
   var viewshedGraphics = resultFeatures.map(function(feature) { 
      feature.symbol = fillSymbol;     
      return feature; 
   });       
   // Add the resulting graphics to the graphics layer  
   graphicsLayer.addMany(viewshedGraphics);
}
```

---

## Use web tools in Python scripts

## Code Samples

### Example 1

```python
# arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;<optional folder>/<service name>;{username};{password}")
arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;GPFolder/BufferService;serverusername;serverpassword")
```

### Example 2

```python
# arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;<optional folder>/<service name>;{username};{password}")
arcpy.ImportToolbox("https://machine.domain.com/webadaptor/services;GPFolder/BufferService;serverusername;serverpassword")
```

### Example 3

```python
import arcpy
import time

arcpy.ImportToolbox("http://machine.domain.com/webadaptor/services;Elevation/viewshedAlias;serverusername;serverpassword")

result = arcpy.Viewshed_viewshedAlias(r'c:\data\inputPoint.shp', "10000 Kilometers")

while result.status < 4:
	   print(result.status)
	   time.sleep(0.2)
print("Execution Finished")

print(result.getMessages())
arcpy.CopyFeatures_management(result[0], 'localResult.shp')
```

### Example 4

```python
import arcpy
import time

arcpy.ImportToolbox("http://machine.domain.com/webadaptor/services;Elevation/viewshedAlias;serverusername;serverpassword")

result = arcpy.Viewshed_viewshedAlias(r'c:\data\inputPoint.shp', "10000 Kilometers")

while result.status < 4:
	   print(result.status)
	   time.sleep(0.2)
print("Execution Finished")

print(result.getMessages())
arcpy.CopyFeatures_management(result[0], 'localResult.shp')
```

### Example 5

```python
{"geometryType" : "esriGeometryPoint",
"spatialReference" : {"wkid" : 54003},
'features':[{'geometry':{'x': -13308192.1956127,
'y':  4221903.58555983}}]}
```

### Example 6

```python
{ 'distance' : 8.5, 'units' : 'esriMiles' }
```

### Example 7

```python
https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute?Input_Observation_Point={%22features%22%3A[{%22geometry%22%3A{%22x%22%3A-13308192.1956127%2C%22y%22%3A4221903.58555983}}]}&Viewshed_Distance={+%27distance%27+%3A+8.5%2C+%27units%27+%3A+%27esriMiles%27+}&env%3AoutSR=&env%3AprocessSR=&f=pjson
```

### Example 8

```python
https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute?Input_Observation_Point={%22features%22%3A[{%22geometry%22%3A{%22x%22%3A-13308192.1956127%2C%22y%22%3A4221903.58555983}}]}&Viewshed_Distance={+%27distance%27+%3A+8.5%2C+%27units%27+%3A+%27esriMiles%27+}&env%3AoutSR=&env%3AprocessSR=&f=pjson
```

### Example 9

```python
# Requires Python 3+
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json

inPts = {"geometryType" : "esriGeometryPoint",
         "spatialReference" : {"wkid" : 54003},
         'features':[{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance':8.5,'units':'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

URL = 'https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute'

req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
response = urlopen.urlopen(req)
response_bytes = response.read()
print(json.loads(response_bytes.decode('UTF-8')))
```

### Example 10

```python
# Requires Python 3+
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json

inPts = {"geometryType" : "esriGeometryPoint",
         "spatialReference" : {"wkid" : 54003},
         'features':[{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance':8.5,'units':'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

URL = 'https://machine.domain.com/webadaptor/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed/execute'

req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
response = urlopen.urlopen(req)
response_bytes = response.read()
print(json.loads(response_bytes.decode('UTF-8')))
```

### Example 11

```python
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json
import time

def sendReq(URL, data=None):

    req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
    response = urlopen.urlopen(req)
    response_bytes = response.read()
    return json.loads(response_bytes.decode('UTF-8'))

inPts = {"geometryType": "esriGeometryPoint",
         "spatialReference": {"wkid" : 54003},
         'features': [{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance': 8.5, 'units': 'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

taskUrl = "https://machine.domain.com/webadaptor/rest/services/Elevation/GPServer/viewshed"
submitUrl = taskUrl + "/submitJob"

submitJson = sendReq(submitUrl, data)

if 'jobId' in submitJson:
    jobID = submitJson['jobId']
    status = submitJson['jobStatus']
    jobUrl = taskUrl + "/jobs/" + jobID

    while status == "esriJobSubmitted" or status == "esriJobExecuting":
        print("checking to see if job is completed...")
        time.sleep(1)

        jobJson = sendReq(jobUrl, {"f": "json"})

        if 'jobStatus' in jobJson.keys():
            status = jobJson['jobStatus']

            if status == "esriJobSucceeded":
                if 'results' in jobJson:
                    resultsJson = jobJson['results']
                    for paramName in resultsJson.keys():
                        resultsUrl = jobUrl + "/" + resultsJson[paramName]['paramUrl']
                        resultJson = sendReq(resultsUrl, {"f": "json"})
                        print(resultJson)

            if status == "esriJobFailed":
                if 'messages' in jobJson.keys():
                    print(jobJson['messages'])

else:
    print("no jobId found in the response")
```

### Example 12

```python
import urllib.request as urlopen
import urllib.parse as urlencode
import urllib.request as request
import json
import time

def sendReq(URL, data=None):

    req = request.Request(URL, urlencode.urlencode(data).encode('UTF-8'))
    response = urlopen.urlopen(req)
    response_bytes = response.read()
    return json.loads(response_bytes.decode('UTF-8'))

inPts = {"geometryType": "esriGeometryPoint",
         "spatialReference": {"wkid" : 54003},
         'features': [{'geometry': {'x': -13308192.1956127, 'y': 4221903.58555983}}]}
dist = {'distance': 8.5, 'units': 'esriMiles'}

data = {'Input_Observation_Point': inPts,
        'Viewshed_Distance': dist,
        'f': 'pjson'}

taskUrl = "https://machine.domain.com/webadaptor/rest/services/Elevation/GPServer/viewshed"
submitUrl = taskUrl + "/submitJob"

submitJson = sendReq(submitUrl, data)

if 'jobId' in submitJson:
    jobID = submitJson['jobId']
    status = submitJson['jobStatus']
    jobUrl = taskUrl + "/jobs/" + jobID

    while status == "esriJobSubmitted" or status == "esriJobExecuting":
        print("checking to see if job is completed...")
        time.sleep(1)

        jobJson = sendReq(jobUrl, {"f": "json"})

        if 'jobStatus' in jobJson.keys():
            status = jobJson['jobStatus']

            if status == "esriJobSucceeded":
                if 'results' in jobJson:
                    resultsJson = jobJson['results']
                    for paramName in resultsJson.keys():
                        resultsUrl = jobUrl + "/" + resultsJson[paramName]['paramUrl']
                        resultJson = sendReq(resultsUrl, {"f": "json"})
                        print(resultJson)

            if status == "esriJobFailed":
                if 'messages' in jobJson.keys():
                    print(jobJson['messages'])

else:
    print("no jobId found in the response")
```

---

## Techniques to use web tools in web apps

## Code Samples

### Example 1

```python
// esri.tasks.Geoprocessor is required for using Geoprocessor.
//  Add it along with other dojo.require statements.
dojo.require(esri.tasks.Geoprocessor); 

// Step 1: Initialize the geoprocessing and point to the REST URL
var gpUrl = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed";
var gp = new Geoprocessor(gpUrl);	

// Set output spatial reference 
gp.outSpatialReference = { wkid: 102100 };

function computeViewshed(event) { 
   graphicsLayer.removeAll();

   // Step 2: Set up input parameters and assign or collect inputs from user
   var point = new Point({ 
        longitude: event.mapPoint.longitude,
        latitude: event.mapPoint.latitude  
   });  

   var inputGraphic = new Graphic({
      geometry: point, 
      symbol: markerSymbol 
   }); 
   graphicsLayer.add(inputGraphic); 

   var inputGraphicContainer = [];
   inputGraphicContainer.push(inputGraphic);
   var featureSet = new FeatureSet();
   featureSet.features = inputGraphicContainer;  

   var vsDistance = new LinearUnit();  
   vsDistance.distance = 5;
   vsDistance.units = "miles";  
   var params = {  
      "Input_Observation_Point": featureSet,
      "Viewshed_Distance": vsDistance  
   };  

   // Step 3: Run the service. In this instance, the service is Synchronous; Execute
   // will be called. An Asynchronous service will use gp.submitJob.
   gp.execute(params).then(drawResultData); 
}  

// Step 4: Render the result. Symbology is assigned and the graphics are added to the map.
function drawResultData(result) { 
   var resultFeatures = result.results[0].value.features;  
   // Assign each resulting graphic a symbol  
   var viewshedGraphics = resultFeatures.map(function(feature) { 
      feature.symbol = fillSymbol;     
      return feature; 
   });       
   // Add the resulting graphics to the graphics layer  
   graphicsLayer.addMany(viewshedGraphics);
}
```

### Example 2

```python
// esri.tasks.Geoprocessor is required for using Geoprocessor.
//  Add it along with other dojo.require statements.
dojo.require(esri.tasks.Geoprocessor); 

// Step 1: Initialize the geoprocessing and point to the REST URL
var gpUrl = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Elevation/ESRI_Elevation_World/GPServer/Viewshed";
var gp = new Geoprocessor(gpUrl);	

// Set output spatial reference 
gp.outSpatialReference = { wkid: 102100 };

function computeViewshed(event) { 
   graphicsLayer.removeAll();

   // Step 2: Set up input parameters and assign or collect inputs from user
   var point = new Point({ 
        longitude: event.mapPoint.longitude,
        latitude: event.mapPoint.latitude  
   });  

   var inputGraphic = new Graphic({
      geometry: point, 
      symbol: markerSymbol 
   }); 
   graphicsLayer.add(inputGraphic); 

   var inputGraphicContainer = [];
   inputGraphicContainer.push(inputGraphic);
   var featureSet = new FeatureSet();
   featureSet.features = inputGraphicContainer;  

   var vsDistance = new LinearUnit();  
   vsDistance.distance = 5;
   vsDistance.units = "miles";  
   var params = {  
      "Input_Observation_Point": featureSet,
      "Viewshed_Distance": vsDistance  
   };  

   // Step 3: Run the service. In this instance, the service is Synchronous; Execute
   // will be called. An Asynchronous service will use gp.submitJob.
   gp.execute(params).then(drawResultData); 
}  

// Step 4: Render the result. Symbology is assigned and the graphics are added to the map.
function drawResultData(result) { 
   var resultFeatures = result.results[0].value.features;  
   // Assign each resulting graphic a symbol  
   var viewshedGraphics = resultFeatures.map(function(feature) { 
      feature.symbol = fillSymbol;     
      return feature; 
   });       
   // Add the resulting graphics to the graphics layer  
   graphicsLayer.addMany(viewshedGraphics);
}
```

---

## Bivariate normal distributions

## Code Samples

### Example 1

```python
f(p,h) = Prob[Z(s) ≤ zp, Z(s + h) ≤ zp],
```

### Example 2

```python
f(p,h) = Prob[Z(s) ≤ zp, Z(s + h) ≤ zp],
```

### Example 3

```python
CI(h;p) = f(p,h) –p2,
```

### Example 4

```python
CI(h;p) = f(p,h) –p2,
```

### Example 5

```python
γI(h;p) = p - f(p,h).
```

### Example 6

```python
γI(h;p) = p - f(p,h).
```

---

## Box-Cox, arcsine, and log transformations

## Code Samples

### Example 1

```python
Y(s) = (Z(s)λ - 1)/λ,
```

### Example 2

```python
Y(s) = (Z(s)λ - 1)/λ,
```

### Example 3

```python
Y(s) = ln(Z(s)),
```

### Example 4

```python
Y(s) = ln(Z(s)),
```

### Example 5

```python
Y(s) = sin-1(Z(s)),
```

### Example 6

```python
Y(s) = sin-1(Z(s)),
```

---

## Empirical semivariogram and covariance functions

## Code Samples

### Example 1

```python
average[(z(si) - z(sj))2]
```

### Example 2

```python
average[(z(si) - z(sj))2]
```

---

## Estimating cross-covariance models for cokriging

## Code Samples

### Example 1

```python
C km (si,sj) = cov(Zk(si), Zm(sj))
```

### Example 2

```python
C km (si,sj) = cov(Zk(si), Zm(sj))
```

---

## How Densify Sampling Network works

## Code Samples

### Example 1

```python
O0(s) = maximum of stderr(s)
```

### Example 2

```python
O0(s) = maximum of stderr(s)
```

### Example 3

```python
O1(s) = maximum of stderr(s)(1-2·abs(prob[Z(s)>Zthreshold]-0.5))
```

### Example 4

```python
O1(s) = maximum of stderr(s)(1-2·abs(prob[Z(s)>Zthreshold]-0.5))
```

---

## Modeling a semivariogram

## Code Samples

### Example 1

```python
Semivariogram(distance h) = 0.5 * average [ (value at location i– value at location j)2]
```

### Example 2

```python
Semivariogram(distance h) = 0.5 * average [ (value at location i– value at location j)2]
```

---

## Semivariogram and covariance functions

## Code Samples

### Example 1

```python
γ(si,sj) = ½ var(Z(si) - Z(sj)),
```

### Example 2

```python
γ(si,sj) = ½ var(Z(si) - Z(sj)),
```

### Example 3

```python
C(si, sj) = cov(Z(si), Z(sj)),
```

### Example 4

```python
C(si, sj) = cov(Z(si), Z(sj)),
```

### Example 5

```python
γ(si, sj) = sill - C(si, sj),
```

### Example 6

```python
γ(si, sj) = sill - C(si, sj),
```

---

## Understanding cokriging

## Code Samples

### Example 1

```python
Z1(s) = µ1 + ε1(s)
```

### Example 2

```python
Z1(s) = µ1 + ε1(s)
```

### Example 3

```python
Z2(s) = µ2 + ε2(s),
```

### Example 4

```python
Z2(s) = µ2 + ε2(s),
```

---

## Understanding disjunctive kriging

## Code Samples

### Example 1

```python
f(Z(s)) = µ1 + ε(s),
```

### Example 2

```python
f(Z(s)) = µ1 + ε(s),
```

---

## How to remove trends from data

## Code Samples

### Example 1

```python
Z(s) = µ(s) + ε(s),
```

### Example 2

```python
Z(s) = µ(s) + ε(s),
```

---

## Understanding indicator kriging

## Code Samples

### Example 1

```python
I(s) = µ + ε(s),
```

### Example 2

```python
I(s) = µ + ε(s),
```

---

## Understanding measurement error

## Code Samples

### Example 1

```python
Z(s) = µ(s) + ε(s) + δ(s),
```

### Example 2

```python
Z(s) = µ(s) + ε(s) + δ(s),
```

---

## Understanding ordinary kriging

## Code Samples

### Example 1

```python
Z(s) = µ + ε(s),
```

### Example 2

```python
Z(s) = µ + ε(s),
```

---

## Understanding probability kriging

## Code Samples

### Example 1

```python
I(s) = I(Z(s) > ct) = µ1 + ε1(s)

Z(s) = µ2 + ε2(s),
```

### Example 2

```python
I(s) = I(Z(s) > ct) = µ1 + ε1(s)

Z(s) = µ2 + ε2(s),
```

---

## Understanding simple kriging

## Code Samples

### Example 1

```python
Z(s) = µ + ε(s)
```

### Example 2

```python
Z(s) = µ + ε(s)
```

---

## Understanding universal kriging

## Code Samples

### Example 1

```python
Z(s) = µ(s) + ε(s),
```

### Example 2

```python
Z(s) = µ(s) + ε(s),
```

---

## What are the different kriging models?

## Code Samples

### Example 1

```python
Z(s) = µ(s) + ε(s),
```

### Example 2

```python
Z(s) = µ(s) + ε(s),
```

### Example 3

```python
µ(s) = ß0 + ß1x + ß2y + ß3x2 + ß4y2 + ß5xy,
```

### Example 4

```python
µ(s) = ß0 + ß1x + ß2y + ß3x2 + ß4y2 + ß5xy,
```

---

## What is EBK Regression Prediction?

## Code Samples

### Example 1

```python
Dependent variable = (mean) + (error)
```

### Example 2

```python
Dependent variable = (mean) + (error)
```

---

## Deep learning models in ArcGIS

## Code Samples

### Example 1

```python
{
    "Framework": "TensorFlow",
    "ModelConfiguration": "ObjectDetectionAPI",
    "ModelFile":"C:\\ModelFolder\\ObjectDetection\\tree_detection.pb",
    "ModelType":"ObjectionDetection",
    "ImageHeight":850,
    "ImageWidth":850,
    "ExtractBands":[0,1,2],
    "Classes" : [
      {
        "Value": 0,
        "Name": "Tree",
        "Color": [0, 255, 0]
      }
    ]
}
```

### Example 2

```python
{
    "Framework": "TensorFlow",
    "ModelConfiguration": "ObjectDetectionAPI",
    "ModelFile":"C:\\ModelFolder\\ObjectDetection\\tree_detection.pb",
    "ModelType":"ObjectionDetection",
    "ImageHeight":850,
    "ImageWidth":850,
    "ExtractBands":[0,1,2],
    "Classes" : [
      {
        "Value": 0,
        "Name": "Tree",
        "Color": [0, 255, 0]
      }
    ]
}
```

### Example 3

```python
{
    "Framework": "PyTorch",
    "ModelConfiguration": "FasterRCNN",
    "ModelFile":"C:\\ModelFolder\\ObjectDetection\\river_detection.pb",
    "ModelType":"ObjectionDetection",
				"Description":"This is a river detection model for  imagery",
    "ImageHeight":448,
    "ImageWidth":448,
    "ExtractBands":[0,1,2,3],
				"DataRange":[0.1, 1.0],
				"ModelPadding":64,
				"BatchSize":8,
				"PerProcessGPUMemoryFraction":0.8,
				"MetaDataMode" : "PASCAL_VOC_rectangles",
				"ImageSpaceUsed" : "MAP_SPACE",
    "Classes" : [
      {
        "Value": 1,
        "Name": "River",
        "Color": [0, 255, 0]
      }
    ],
				"InputRastersProps" : {
						"RasterCount" : 1,
						"SensorName" : "Landsat 8",
						"BandNames" : [
								"Red",
								"Green",
								"Blue",
								"NearInfrared"
						]
				},
				"AllTilesStats" : [
      {
      		"BandName" : "Red",
      		"Min" : 1,
      		"Max" : 60419,
      		"Mean" : 7669.720049855654,
      		"StdDev" : 1512.7546387966217
      },
      {
      		"BandName" : "Green",
      		"Min" : 1,
      		"Max" : 50452,
      		"Mean" : 8771.2498195125681,
      		"StdDev" : 1429.1063589515179
      },
      {
      		"BandName" : "Blue",
      		"Min" : 1,
      		"Max" : 47305,
      		"Mean" : 9306.0475897744163,
      		"StdDev" : 1429.380049936676
      },
      {
      		"BandName" : "NearInfrared",
      		"Min" : 1,
      		"Max" : 60185,
      		"Mean" : 17881.499184561973,
      		"StdDev" : 5550.4055277121679
      }
    ],
}
```

### Example 4

```python
{
    "Framework": "PyTorch",
    "ModelConfiguration": "FasterRCNN",
    "ModelFile":"C:\\ModelFolder\\ObjectDetection\\river_detection.pb",
    "ModelType":"ObjectionDetection",
				"Description":"This is a river detection model for  imagery",
    "ImageHeight":448,
    "ImageWidth":448,
    "ExtractBands":[0,1,2,3],
				"DataRange":[0.1, 1.0],
				"ModelPadding":64,
				"BatchSize":8,
				"PerProcessGPUMemoryFraction":0.8,
				"MetaDataMode" : "PASCAL_VOC_rectangles",
				"ImageSpaceUsed" : "MAP_SPACE",
    "Classes" : [
      {
        "Value": 1,
        "Name": "River",
        "Color": [0, 255, 0]
      }
    ],
				"InputRastersProps" : {
						"RasterCount" : 1,
						"SensorName" : "Landsat 8",
						"BandNames" : [
								"Red",
								"Green",
								"Blue",
								"NearInfrared"
						]
				},
				"AllTilesStats" : [
      {
      		"BandName" : "Red",
      		"Min" : 1,
      		"Max" : 60419,
      		"Mean" : 7669.720049855654,
      		"StdDev" : 1512.7546387966217
      },
      {
      		"BandName" : "Green",
      		"Min" : 1,
      		"Max" : 50452,
      		"Mean" : 8771.2498195125681,
      		"StdDev" : 1429.1063589515179
      },
      {
      		"BandName" : "Blue",
      		"Min" : 1,
      		"Max" : 47305,
      		"Mean" : 9306.0475897744163,
      		"StdDev" : 1429.380049936676
      },
      {
      		"BandName" : "NearInfrared",
      		"Min" : 1,
      		"Max" : 60185,
      		"Mean" : 17881.499184561973,
      		"StdDev" : 5550.4055277121679
      }
    ],
}
```

---

## Multidimensional raster types

## Code Samples

### Example 1

```python
153 is the code
CONVfract  is the variable name
The text after the variable name is the long name
7 is the data center
12 is the data subcenter
130 is the table version
```

### Example 2

```python
153 is the code
CONVfract  is the variable name
The text after the variable name is the long name
7 is the data center
12 is the data subcenter
130 is the table version
```

---

## Detect pixel value change

## Code Samples

### Example 1

```python
Output = (To Raster) - (From Raster)
```

### Example 2

```python
Output = (To Raster) - (From Raster)
```

### Example 3

```python
Output = (To Raster - From Raster) / max(To Raster, From Raster)
```

### Example 4

```python
Output = (To Raster - From Raster) / max(To Raster, From Raster)
```

---

## Create a Python script tool using arcpy.nax

## Code Samples

### Example 1

```python
input_facilities = arcpy.GetParameterAsText(0)
output_polygons = arcpy.GetParameterAsText(1)
network = arcpy.GetParameterAsText(2)
travel_mode = arcpy.GetParameter(3)
cutoffs = arcpy.GetParameter(4)
cutoff_units = arcpy.GetParameterAsText(5)
time_of_day = arcpy.GetParameter(6)
```

### Example 2

```python
input_facilities = arcpy.GetParameterAsText(0)
output_polygons = arcpy.GetParameterAsText(1)
network = arcpy.GetParameterAsText(2)
travel_mode = arcpy.GetParameter(3)
cutoffs = arcpy.GetParameter(4)
cutoff_units = arcpy.GetParameterAsText(5)
time_of_day = arcpy.GetParameter(6)
```

### Example 3

```python
# Check out the Network Analyst extension license if the input network
# is a local network dataset and not a service.
if not network.startswith("http"):
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        # Throw an error if the license cannot be checked out.
        arcpy.AddError("The Network Analyst license is unavailable.")
        raise CustomError
```

### Example 4

```python
# Check out the Network Analyst extension license if the input network
# is a local network dataset and not a service.
if not network.startswith("http"):
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        # Throw an error if the license cannot be checked out.
        arcpy.AddError("The Network Analyst license is unavailable.")
        raise CustomError
```

### Example 5

```python
# Instantiate the ServiceArea solver object
sa = arcpy.nax.ServiceArea(network)
```

### Example 6

```python
# Instantiate the ServiceArea solver object
sa = arcpy.nax.ServiceArea(network)
```

### Example 7

```python
# Hard-code some non-default Service Area settings that we don't want
# the user to change
sa.geometryAtCutoff = arcpy.nax.ServiceAreaPolygonCutoffGeometry.Disks
sa.polygonBufferDistance = 150
sa.polygonBufferDistanceUnits = arcpy.nax.DistanceUnits.Feet

# Set analysis properties chosen by the user and passed in via tool
# parameters
sa.travelMode = travel_mode
sa.timeOfDay = time_of_day
sa.defaultImpedanceCutoffs = cutoffs
```

### Example 8

```python
# Hard-code some non-default Service Area settings that we don't want
# the user to change
sa.geometryAtCutoff = arcpy.nax.ServiceAreaPolygonCutoffGeometry.Disks
sa.polygonBufferDistance = 150
sa.polygonBufferDistanceUnits = arcpy.nax.DistanceUnits.Feet

# Set analysis properties chosen by the user and passed in via tool
# parameters
sa.travelMode = travel_mode
sa.timeOfDay = time_of_day
sa.defaultImpedanceCutoffs = cutoffs
```

### Example 9

```python
# Do special handling of cutoff units to convert them to the correct
# arcpy.nax enum
if cutoff_units in ["Hours", "Minutes"]:
    sa.timeUnits = convert_time_units_to_nax(cutoff_units)
elif cutoff_units in ["Kilometers", "Meters", "Miles", "Yards", "Feet"]:
    sa.distanceUnits = convert_distance_units_to_nax(cutoff_units)
```

### Example 10

```python
# Do special handling of cutoff units to convert them to the correct
# arcpy.nax enum
if cutoff_units in ["Hours", "Minutes"]:
    sa.timeUnits = convert_time_units_to_nax(cutoff_units)
elif cutoff_units in ["Kilometers", "Meters", "Miles", "Yards", "Feet"]:
    sa.distanceUnits = convert_distance_units_to_nax(cutoff_units)
```

### Example 11

```python
def convert_time_units_to_nax(time_units_str):
    """Convert string-based time units to the correct arcpy.nax enum."""
    if time_units_str == "Hours":
        return arcpy.nax.TimeUnits.Hours
    if time_units_str == "Minutes":
        return arcpy.nax.TimeUnits.Minutes
    arcpy.AddError(f"Invalid time units: {time_units_str}")
    raise CustomError


def convert_distance_units_to_nax(dist_units_str):
    """Convert string-based distance units to the correct arcpy.nax enum."""
    if dist_units_str == "Kilometers":
        return arcpy.nax.DistanceUnits.Kilometers
    if dist_units_str == "Meters":
        return arcpy.nax.DistanceUnits.Meters
    if dist_units_str == "Miles":
        return arcpy.nax.DistanceUnits.Miles
    if dist_units_str == "Yards":
        return arcpy.nax.DistanceUnits.Yards
    if dist_units_str == "Feet":
        return arcpy.nax.DistanceUnits.Feet
    arcpy.AddError(f"Invalid distance units: {dist_units_str}")
    raise CustomError
```

### Example 12

```python
def convert_time_units_to_nax(time_units_str):
    """Convert string-based time units to the correct arcpy.nax enum."""
    if time_units_str == "Hours":
        return arcpy.nax.TimeUnits.Hours
    if time_units_str == "Minutes":
        return arcpy.nax.TimeUnits.Minutes
    arcpy.AddError(f"Invalid time units: {time_units_str}")
    raise CustomError


def convert_distance_units_to_nax(dist_units_str):
    """Convert string-based distance units to the correct arcpy.nax enum."""
    if dist_units_str == "Kilometers":
        return arcpy.nax.DistanceUnits.Kilometers
    if dist_units_str == "Meters":
        return arcpy.nax.DistanceUnits.Meters
    if dist_units_str == "Miles":
        return arcpy.nax.DistanceUnits.Miles
    if dist_units_str == "Yards":
        return arcpy.nax.DistanceUnits.Yards
    if dist_units_str == "Feet":
        return arcpy.nax.DistanceUnits.Feet
    arcpy.AddError(f"Invalid distance units: {dist_units_str}")
    raise CustomError
```

### Example 13

```python
# Load the input facilities
sa.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
```

### Example 14

```python
# Load the input facilities
sa.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
```

### Example 15

```python
# Solve the analysis
result = sa.solve()
```

### Example 16

```python
# Solve the analysis
result = sa.solve()
```

### Example 17

```python
# Print warning messages if there are any
for warning in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
    arcpy.AddWarning(warning[1])
```

### Example 18

```python
# Print warning messages if there are any
for warning in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
    arcpy.AddWarning(warning[1])
```

### Example 19

```python
# Handle failed solves
if not result.solveSucceeded:
    arcpy.AddError("The Service Area solve failed.")
    # Print error messages and stop the tool from running further
    for error in result.solverMessages(arcpy.nax.MessageSeverity.Error):
        arcpy.AddError(error[1])
    # Stop tool run by raising an error
    raise CustomError
```

### Example 20

```python
# Handle failed solves
if not result.solveSucceeded:
    arcpy.AddError("The Service Area solve failed.")
    # Print error messages and stop the tool from running further
    for error in result.solverMessages(arcpy.nax.MessageSeverity.Error):
        arcpy.AddError(error[1])
    # Stop tool run by raising an error
    raise CustomError
```

### Example 21

```python
# Add a message with the total number of polygons that were generated
# in the analysis
num_polygons = result.count(
    arcpy.nax.ServiceAreaOutputDataType.Polygons)
arcpy.AddMessage(f"Number of polygons generated: {num_polygons}.")

# Export the Service Area polygons to the output feature class
result.export(
    arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
```

### Example 22

```python
# Add a message with the total number of polygons that were generated
# in the analysis
num_polygons = result.count(
    arcpy.nax.ServiceAreaOutputDataType.Polygons)
arcpy.AddMessage(f"Number of polygons generated: {num_polygons}.")

# Export the Service Area polygons to the output feature class
result.export(
    arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
```

### Example 23

```python
class CustomError(Exception):
    pass
```

### Example 24

```python
class CustomError(Exception):
    pass
```

### Example 25

```python
try:

    [...]

except CustomError:
    # We caught a known error and already added the message. Do nothing.
    pass

except Exception:
    # An unknown error occurred. Add the traceback as an error message.
    arcpy.AddError(
        "An unknown error occurred when generating Service Areas.")
    import traceback
    arcpy.AddError(traceback.format_exc())
```

### Example 26

```python
try:

    [...]

except CustomError:
    # We caught a known error and already added the message. Do nothing.
    pass

except Exception:
    # An unknown error occurred. Add the traceback as an error message.
    arcpy.AddError(
        "An unknown error occurred when generating Service Areas.")
    import traceback
    arcpy.AddError(traceback.format_exc())
```

### Example 27

```python
import arcpy


class CustomError(Exception):
    pass


def convert_time_units_to_nax(time_units_str):
    """Convert string-based time units to the correct arcpy.nax enum."""
    if time_units_str == "Hours":
        return arcpy.nax.TimeUnits.Hours
    if time_units_str == "Minutes":
        return arcpy.nax.TimeUnits.Minutes
    arcpy.AddError(f"Invalid time units: {time_units_str}")
    raise CustomError


def convert_distance_units_to_nax(dist_units_str):
    """Convert string-based distance units to the correct arcpy.nax enum."""
    if dist_units_str == "Kilometers":
        return arcpy.nax.DistanceUnits.Kilometers
    if dist_units_str == "Meters":
        return arcpy.nax.DistanceUnits.Meters
    if dist_units_str == "Miles":
        return arcpy.nax.DistanceUnits.Miles
    if dist_units_str == "Yards":
        return arcpy.nax.DistanceUnits.Yards
    if dist_units_str == "Feet":
        return arcpy.nax.DistanceUnits.Feet
    arcpy.AddError(f"Invalid distance units: {dist_units_str}")
    raise CustomError


def generate_service_areas():
    """Generate Service Area polygons."""
    try:
        input_facilities = arcpy.GetParameterAsText(0)
        output_polygons = arcpy.GetParameterAsText(1)
        network = arcpy.GetParameterAsText(2)
        travel_mode = arcpy.GetParameter(3)
        cutoffs = arcpy.GetParameter(4)
        cutoff_units = arcpy.GetParameterAsText(5)
        time_of_day = arcpy.GetParameter(6)

        # Check out the Network Analyst extension license if the input network
        # is a local network dataset and not a service.
        if not network.startswith("http"):
            if arcpy.CheckExtension("network") == "Available":
                arcpy.CheckOutExtension("network")
            else:
                # Throw an error if the license cannot be checked out.
                arcpy.AddError("The Network Analyst license is unavailable.")
                raise CustomError

        # Instantiate the ServiceArea solver object
        sa = arcpy.nax.ServiceArea(network)

        # Hard-code some non-default Service Area settings that we don't want
        # the user to change
        sa.geometryAtCutoff = arcpy.nax.ServiceAreaPolygonCutoffGeometry.Disks
        sa.polygonBufferDistance = 150
        sa.polygonBufferDistanceUnits = arcpy.nax.DistanceUnits.Feet

        # Set analysis properties chosen by the user and passed in via tool
        # parameters
        sa.travelMode = travel_mode
        sa.timeOfDay = time_of_day
        sa.defaultImpedanceCutoffs = cutoffs
        # Do special handling of cutoff units to convert them to the correct
        # arcpy.nax enum
        if cutoff_units in ["Hours", "Minutes"]:
            sa.timeUnits = convert_time_units_to_nax(cutoff_units)
        elif cutoff_units in ["Kilometers", "Meters", "Miles", "Yards", "Feet"]:
            sa.distanceUnits = convert_distance_units_to_nax(cutoff_units)

        # Load the input facilities
        sa.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)

        # Solve the analysis
        result = sa.solve()

        # Print warning messages if there are any
        for warning in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
            arcpy.AddWarning(warning[1])

        # Handle failed solves
        if not result.solveSucceeded:
            arcpy.AddError("The Service Area solve failed.")
            # Print error messages and stop the tool from running further
            for error in result.solverMessages(arcpy.nax.MessageSeverity.Error):
                arcpy.AddError(error[1])
            # Stop tool run by raising an error
            raise CustomError

        # Add a message with the total number of polygons that were generated
        # in the analysis
        num_polygons = result.count(
            arcpy.nax.ServiceAreaOutputDataType.Polygons)
        arcpy.AddMessage(f"Number of polygons generated: {num_polygons}.")

        # Export the Service Area polygons to the output feature class
        result.export(
            arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)

    except CustomError:
        # We caught a known error and already added the message. Do nothing.
        pass

    except Exception:
        # An unknown error occurred. Add the traceback as an error message.
        arcpy.AddError(
            "An unknown error occurred when generating Service Areas.")
        import traceback
        arcpy.AddError(traceback.format_exc())


if __name__ == "__main__":
    generate_service_areas()
```

### Example 28

```python
import arcpy


class CustomError(Exception):
    pass


def convert_time_units_to_nax(time_units_str):
    """Convert string-based time units to the correct arcpy.nax enum."""
    if time_units_str == "Hours":
        return arcpy.nax.TimeUnits.Hours
    if time_units_str == "Minutes":
        return arcpy.nax.TimeUnits.Minutes
    arcpy.AddError(f"Invalid time units: {time_units_str}")
    raise CustomError


def convert_distance_units_to_nax(dist_units_str):
    """Convert string-based distance units to the correct arcpy.nax enum."""
    if dist_units_str == "Kilometers":
        return arcpy.nax.DistanceUnits.Kilometers
    if dist_units_str == "Meters":
        return arcpy.nax.DistanceUnits.Meters
    if dist_units_str == "Miles":
        return arcpy.nax.DistanceUnits.Miles
    if dist_units_str == "Yards":
        return arcpy.nax.DistanceUnits.Yards
    if dist_units_str == "Feet":
        return arcpy.nax.DistanceUnits.Feet
    arcpy.AddError(f"Invalid distance units: {dist_units_str}")
    raise CustomError


def generate_service_areas():
    """Generate Service Area polygons."""
    try:
        input_facilities = arcpy.GetParameterAsText(0)
        output_polygons = arcpy.GetParameterAsText(1)
        network = arcpy.GetParameterAsText(2)
        travel_mode = arcpy.GetParameter(3)
        cutoffs = arcpy.GetParameter(4)
        cutoff_units = arcpy.GetParameterAsText(5)
        time_of_day = arcpy.GetParameter(6)

        # Check out the Network Analyst extension license if the input network
        # is a local network dataset and not a service.
        if not network.startswith("http"):
            if arcpy.CheckExtension("network") == "Available":
                arcpy.CheckOutExtension("network")
            else:
                # Throw an error if the license cannot be checked out.
                arcpy.AddError("The Network Analyst license is unavailable.")
                raise CustomError

        # Instantiate the ServiceArea solver object
        sa = arcpy.nax.ServiceArea(network)

        # Hard-code some non-default Service Area settings that we don't want
        # the user to change
        sa.geometryAtCutoff = arcpy.nax.ServiceAreaPolygonCutoffGeometry.Disks
        sa.polygonBufferDistance = 150
        sa.polygonBufferDistanceUnits = arcpy.nax.DistanceUnits.Feet

        # Set analysis properties chosen by the user and passed in via tool
        # parameters
        sa.travelMode = travel_mode
        sa.timeOfDay = time_of_day
        sa.defaultImpedanceCutoffs = cutoffs
        # Do special handling of cutoff units to convert them to the correct
        # arcpy.nax enum
        if cutoff_units in ["Hours", "Minutes"]:
            sa.timeUnits = convert_time_units_to_nax(cutoff_units)
        elif cutoff_units in ["Kilometers", "Meters", "Miles", "Yards", "Feet"]:
            sa.distanceUnits = convert_distance_units_to_nax(cutoff_units)

        # Load the input facilities
        sa.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)

        # Solve the analysis
        result = sa.solve()

        # Print warning messages if there are any
        for warning in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
            arcpy.AddWarning(warning[1])

        # Handle failed solves
        if not result.solveSucceeded:
            arcpy.AddError("The Service Area solve failed.")
            # Print error messages and stop the tool from running further
            for error in result.solverMessages(arcpy.nax.MessageSeverity.Error):
                arcpy.AddError(error[1])
            # Stop tool run by raising an error
            raise CustomError

        # Add a message with the total number of polygons that were generated
        # in the analysis
        num_polygons = result.count(
            arcpy.nax.ServiceAreaOutputDataType.Polygons)
        arcpy.AddMessage(f"Number of polygons generated: {num_polygons}.")

        # Export the Service Area polygons to the output feature class
        result.export(
            arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)

    except CustomError:
        # We caught a known error and already added the message. Do nothing.
        pass

    except Exception:
        # An unknown error occurred. Add the traceback as an error message.
        arcpy.AddError(
            "An unknown error occurred when generating Service Areas.")
        import traceback
        arcpy.AddError(traceback.format_exc())


if __name__ == "__main__":
    generate_service_areas()
```

### Example 29

```python
def updateMessages(self):
    # Customize messages for the parameters.
    # This gets called after standard validation.

    # Raise an error if any of the cutoffs are <= 0
    cutoffs_param = self.params[4]
    if cutoffs_param.valueAsText:
        for cutoff in cutoffs_param.values:
            if cutoff <= 0:
                cutoffs_param.setErrorMessage("Cutoffs must be positive.")
                break

    return
```

### Example 30

```python
def updateMessages(self):
    # Customize messages for the parameters.
    # This gets called after standard validation.

    # Raise an error if any of the cutoffs are <= 0
    cutoffs_param = self.params[4]
    if cutoffs_param.valueAsText:
        for cutoff in cutoffs_param.values:
            if cutoff <= 0:
                cutoffs_param.setErrorMessage("Cutoffs must be positive.")
                break

    return
```

### Example 31

```python
def updateParameters(self):
    # Modify parameter values and properties.
    # This gets called each time a parameter is modified, before
    # standard validation.

    # Set filter list of units in cutoff units parameter based on what type
    # of travel mode is selected
    travel_mode_param = self.params[3]
    cutoff_units_param = self.params[5]
    if travel_mode_param.valueAsText:
        try:
            tm_object = travel_mode_param.value
            if tm_object.impedance == tm_object.timeAttributeName:
                # The impedance has units of time, so present time units as
                # options
                cutoff_units_param.filter.list = ["Hours", "Minutes"]
            elif tm_object.impedance == tm_object.distanceAttributeName:
                # The impedance has units of distance, so present distance
                # units as options
                cutoff_units_param.filter.list = [
                    "Kilometers", "Meters", "Miles", "Yards", "Feet"]
            else:
                # The impedance has units that are neither time nor
                # distance, so present only one option, "Other". The
                # Service Area cutoffs will be interpreted in the impedance
                # units.
                cutoff_units_param.filter.list = ["Other"]
        except Exception:
            pass

    return
```

### Example 32

```python
def updateParameters(self):
    # Modify parameter values and properties.
    # This gets called each time a parameter is modified, before
    # standard validation.

    # Set filter list of units in cutoff units parameter based on what type
    # of travel mode is selected
    travel_mode_param = self.params[3]
    cutoff_units_param = self.params[5]
    if travel_mode_param.valueAsText:
        try:
            tm_object = travel_mode_param.value
            if tm_object.impedance == tm_object.timeAttributeName:
                # The impedance has units of time, so present time units as
                # options
                cutoff_units_param.filter.list = ["Hours", "Minutes"]
            elif tm_object.impedance == tm_object.distanceAttributeName:
                # The impedance has units of distance, so present distance
                # units as options
                cutoff_units_param.filter.list = [
                    "Kilometers", "Meters", "Miles", "Yards", "Feet"]
            else:
                # The impedance has units that are neither time nor
                # distance, so present only one option, "Other". The
                # Service Area cutoffs will be interpreted in the impedance
                # units.
                cutoff_units_param.filter.list = ["Other"]
        except Exception:
            pass

    return
```

---

## Geoprocessing service example: Get travel directions

## Code Samples

### Example 1

```python
"""Generate travel directions based on a travel mode."""

import arcpy


def get_directions():
    """Generate travel directions based on a travel mode."""
    # Read inputs
    stops = arcpy.GetParameter(0)
    # Performance tip: The network data source should be read using the arcpy.GetParameterAsText()
    # method instead of the arcpy.GetParameter() method since GetParameterAsText provides
    # access to the network data source much faster
    network_data_source = arcpy.GetParameterAsText(1)
    travel_mode = arcpy.GetParameter(2)
    start_time = arcpy.GetParameter(3)
    output_directions = arcpy.GetParameterAsText(4)

    # Initialize Route solver and set analysis settings
    route_solver = arcpy.nax.Route(network_data_source)
    route_solver.travelMode = travel_mode
    route_solver.timeOfDay = start_time
    route_solver.returnDirections = True

    # Load inputs
    route_solver.load(arcpy.nax.RouteInputDataType.Stops, stops)

    # Solve. A network analyst license is required when solving
    arcpy.CheckOutExtension("network")
    result = route_solver.solve()

    # Print all the warning and error messages in case the solve is not successful
    if not result.solveSucceeded:
        arcpy.AddMessage("Solve failed")
        warning_msgs = result.solverMessages(arcpy.nax.MessageSeverity.Warning)
        error_msgs = result.solverMessages(arcpy.nax.MessageSeverity.Error)
        for msg in warning_msgs:
            arcpy.AddWarning(msg[-1])
        for msg in error_msgs:
            arcpy.AddError(msg[-1])
        raise SystemExit(1)

    # Export the directions
    result.export(arcpy.nax.RouteOutputDataType.Directions, output_directions)


if __name__ == "__main__":
    get_directions()
```

### Example 2

```python
"""Generate travel directions based on a travel mode."""

import arcpy


def get_directions():
    """Generate travel directions based on a travel mode."""
    # Read inputs
    stops = arcpy.GetParameter(0)
    # Performance tip: The network data source should be read using the arcpy.GetParameterAsText()
    # method instead of the arcpy.GetParameter() method since GetParameterAsText provides
    # access to the network data source much faster
    network_data_source = arcpy.GetParameterAsText(1)
    travel_mode = arcpy.GetParameter(2)
    start_time = arcpy.GetParameter(3)
    output_directions = arcpy.GetParameterAsText(4)

    # Initialize Route solver and set analysis settings
    route_solver = arcpy.nax.Route(network_data_source)
    route_solver.travelMode = travel_mode
    route_solver.timeOfDay = start_time
    route_solver.returnDirections = True

    # Load inputs
    route_solver.load(arcpy.nax.RouteInputDataType.Stops, stops)

    # Solve. A network analyst license is required when solving
    arcpy.CheckOutExtension("network")
    result = route_solver.solve()

    # Print all the warning and error messages in case the solve is not successful
    if not result.solveSucceeded:
        arcpy.AddMessage("Solve failed")
        warning_msgs = result.solverMessages(arcpy.nax.MessageSeverity.Warning)
        error_msgs = result.solverMessages(arcpy.nax.MessageSeverity.Error)
        for msg in warning_msgs:
            arcpy.AddWarning(msg[-1])
        for msg in error_msgs:
            arcpy.AddError(msg[-1])
        raise SystemExit(1)

    # Export the directions
    result.export(arcpy.nax.RouteOutputDataType.Directions, output_directions)


if __name__ == "__main__":
    get_directions()
```

---

## Create a network dataset

## Code Samples

### Example 1

```python
def MetersToFeet(value):
 if value is None:
  return value
 return value / 0.3048
```

### Example 2

```python
def MetersToFeet(value):
 if value is None:
  return value
 return value / 0.3048
```

### Example 3

```python
def MetersToFeet(value):
 if value is None:
  return value
 return value / 0.3048
```

### Example 4

```python
def MetersToFeet(value):
 if value is None:
  return value
 return value / 0.3048
```

### Example 5

```python
int(!FUNC_CLASS!)
```

### Example 6

```python
int(!FUNC_CLASS!)
```

---

## Service multiple customers from a single distribution center using Last Mile Delivery

## Code Samples

### Example 1

```python
def BasedOnQuantity(quantity):
    if quantity == 1:
        time = 3
    elif quantity == 2:
        time = 4
    elif quantity == 3:
        time = 5
    else:
        time = 6
    return time
```

### Example 2

```python
def BasedOnQuantity(quantity):
    if quantity == 1:
        time = 3
    elif quantity == 2:
        time = 4
    elif quantity == 3:
        time = 5
    else:
        time = 6
    return time
```

---

## Script evaluator examples

## Code Samples

### Example 1

```python
Value:
calc_time(!RoadClass!, !Miles!)

Code Block:
def calc_time(rc, d):
    # This example assumes that the speed limit is in miles per hour
    # and that the distance field is in miles
    if rc == 1:  # Local roads
        speed_limit = 30
    elif rc == 6:  # Major roads
        speed_limit = 55
    elif rc == 2:  # Highways
        speed_limit = 70
    else:  # Set a default speed limit if RoadClass does not match any other option
        speed_limit = 45   
    return 60 * d / speed_limit
```

### Example 2

```python
Value:
calc_time(!RoadClass!, !Miles!)

Code Block:
def calc_time(rc, d):
    # This example assumes that the speed limit is in miles per hour
    # and that the distance field is in miles
    if rc == 1:  # Local roads
        speed_limit = 30
    elif rc == 6:  # Major roads
        speed_limit = 55
    elif rc == 2:  # Highways
        speed_limit = 70
    else:  # Set a default speed limit if RoadClass does not match any other option
        speed_limit = 45   
    return 60 * d / speed_limit
```

### Example 3

```python
Value:
cost_adjusted_for_slope("Minutes", "AverageSlope", "SteepUpFactor", "SteepDownFactor")

Code Block:
def cost_adjusted_for_slope(
    time_cost_attr_name, slope_attr_name,
    up_factor_param_name, down_factor_param_name
):
    # Retrieve the values of other attributes for this road
    time_cost = Edge.AttributeValueByName(time_cost_attr_name)
    slope = Edge.AttributeValueByName(slope_attr_name)

    # Retrieve the value of parameters for this attribute
    up_factor = ParameterValueByName(up_factor_param_name)
    down_factor = ParameterValueByName(down_factor_param_name)

    # Set default values in case the parameter values are null
    if up_factor is None: 
        up_factor = 1.25
    if down_factor is None: 
        down_factor = 0.80

    # Calculate the modified travel time cost based on slope
    factor = 1
    if slope < -0.05:  # Steep downhill
        factor = down_factor
    elif slope > 0.075: # Steep uphill
        factor = up_factor
    modified_cost = factor * time_cost

    return modified_cost
```

### Example 4

```python
Value:
cost_adjusted_for_slope("Minutes", "AverageSlope", "SteepUpFactor", "SteepDownFactor")

Code Block:
def cost_adjusted_for_slope(
    time_cost_attr_name, slope_attr_name,
    up_factor_param_name, down_factor_param_name
):
    # Retrieve the values of other attributes for this road
    time_cost = Edge.AttributeValueByName(time_cost_attr_name)
    slope = Edge.AttributeValueByName(slope_attr_name)

    # Retrieve the value of parameters for this attribute
    up_factor = ParameterValueByName(up_factor_param_name)
    down_factor = ParameterValueByName(down_factor_param_name)

    # Set default values in case the parameter values are null
    if up_factor is None: 
        up_factor = 1.25
    if down_factor is None: 
        down_factor = 0.80

    # Calculate the modified travel time cost based on slope
    factor = 1
    if slope < -0.05:  # Steep downhill
        factor = down_factor
    elif slope > 0.075: # Steep uphill
        factor = up_factor
    modified_cost = factor * time_cost

    return modified_cost
```

### Example 5

```python
Value:
is_closed_for_event("MarketIntersection", "MarketEvent")

Code Block:
def is_closed_for_event(is_conditionally_open_attr_name, event_closure_bool_param_name):
    is_affected_by_event = Junction.AttributeValueByName(is_conditionally_open_attr_name)
    is_closed_for_event_param = ParameterValueByName(event_closure_bool_param_name)
    return is_affected_by_event and is_closed_for_event_param
```

### Example 6

```python
Value:
is_closed_for_event("MarketIntersection", "MarketEvent")

Code Block:
def is_closed_for_event(is_conditionally_open_attr_name, event_closure_bool_param_name):
    is_affected_by_event = Junction.AttributeValueByName(is_conditionally_open_attr_name)
    is_closed_for_event_param = ParameterValueByName(event_closure_bool_param_name)
    return is_affected_by_event and is_closed_for_event_param
```

### Example 7

```python
Value:
no_backwards_turn(Turn.Angle)

Code Block:
def no_backwards_turn(angle):
    if angle >= 135 and angle <= 225:
        # Restrict turns with sharp angles
        return True
    return False
```

### Example 8

```python
Value:
no_backwards_turn(Turn.Angle)

Code Block:
def no_backwards_turn(angle):
    if angle >= 135 and angle <= 225:
        # Restrict turns with sharp angles
        return True
    return False
```

---

## ArgStatistics function

## Code Samples

### Example 1

```python
i = ( (n-1) / 2 )
```

### Example 2

```python
i = ( (n-1) / 2 )
```

---

## Arithmetic function

## Code Samples

### Example 1

```python
output = Raster1 + Raster2
```

### Example 2

```python
output = Raster1 + Raster2
```

### Example 3

```python
output = Raster1 - Raster2
```

### Example 4

```python
output = Raster1 - Raster2
```

### Example 5

```python
output = Raster1 × Raster2
```

### Example 6

```python
output = Raster1 × Raster2
```

### Example 7

```python
output = Raster1 ÷ Raster2
```

### Example 8

```python
output = Raster1 ÷ Raster2
```

### Example 9

```python
output = Raster1Raster2
```

### Example 10

```python
output = Raster1Raster2
```

---

## ATan2 function

## Code Samples

### Example 1

```python
tanθ = y / x
```

### Example 2

```python
tanθ = y / x
```

---

## Band Arithmetic function

## Code Samples

### Example 1

```python
B1 + B2
b1 + (-b2)
(B1 + B2) / 2(B3 * B5)
```

### Example 2

```python
B1 + B2
b1 + (-b2)
(B1 + B2) / 2(B3 * B5)
```

### Example 3

```python
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 4

```python
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 5

```python
CIg = [(NIR / Green)-1]
```

### Example 6

```python
CIg = [(NIR / Green)-1]
```

### Example 7

```python
Clre = [(NIR / RedEdge)-1]
```

### Example 8

```python
Clre = [(NIR / RedEdge)-1]
```

### Example 9

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 10

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 11

```python
EVI = 2.5*(NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
```

### Example 12

```python
EVI = 2.5*(NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
```

### Example 13

```python
Ferrous Minerals Ratio = SWIR / NIR
```

### Example 14

```python
Ferrous Minerals Ratio = SWIR / NIR
```

### Example 15

```python
GEMI = eta*(1-0.25*eta)-((Red-0.125)/(1-Red))
```

### Example 16

```python
GEMI = eta*(1-0.25*eta)-((Red-0.125)/(1-Red))
```

### Example 17

```python
eta = (2*(NIR2-Red2)+1.5*NIR+0.5*Red)/(NIR+Red+0.5)
```

### Example 18

```python
eta = (2*(NIR2-Red2)+1.5*NIR+0.5*Red)/(NIR+Red+0.5)
```

### Example 19

```python
GNDVI = (NIR-Green)/(NIR+Green)
```

### Example 20

```python
GNDVI = (NIR-Green)/(NIR+Green)
```

### Example 21

```python
GVI=-0.2848*Band1-0.2435*Band2-0.5436*Band3+0.7243*Band4+0.0840*Band5-1.1800*Band7
```

### Example 22

```python
GVI=-0.2848*Band1-0.2435*Band2-0.5436*Band3+0.7243*Band4+0.0840*Band5-1.1800*Band7
```

### Example 23

```python
Iron Oxide Ratio = Red / Blue
```

### Example 24

```python
Iron Oxide Ratio = Red / Blue
```

### Example 25

```python
MNDWI = (Green - SWIR) / (Green + SWIR)
```

### Example 26

```python
MNDWI = (Green - SWIR) / (Green + SWIR)
```

### Example 27

```python
MSAVI2 = (1/2)*(2(NIR+1)-sqrt((2*NIR+1)2-8(NIR-Red)))
```

### Example 28

```python
MSAVI2 = (1/2)*(2(NIR+1)-sqrt((2*NIR+1)2-8(NIR-Red)))
```

### Example 29

```python
MTVI2 = [1.5(1.2(NIR-Green)-2.5(Red-Green))√((2NIR+1)²-(6NIR-5√(Red))-0.5)]
```

### Example 30

```python
MTVI2 = [1.5(1.2(NIR-Green)-2.5(Red-Green))√((2NIR+1)²-(6NIR-5√(Red))-0.5)]
```

### Example 31

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 32

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 33

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

### Example 34

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

### Example 35

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 36

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 37

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 38

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 39

```python
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 40

```python
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 41

```python
NDVIre = (NIR - RedEdge)/(NIR + RedEdge)
```

### Example 42

```python
NDVIre = (NIR - RedEdge)/(NIR + RedEdge)
```

### Example 43

```python
NDWI = (Green - NIR) / (Green + NIR)
```

### Example 44

```python
NDWI = (Green - NIR) / (Green + NIR)
```

### Example 45

```python
PVI = (NIR - a*Red - b) / (sqrt(1 + a2))
```

### Example 46

```python
PVI = (NIR - a*Red - b) / (sqrt(1 + a2))
```

### Example 47

```python
RTVICore = [100(NIR-RedEdge)-10(NIR-Green)]
```

### Example 48

```python
RTVICore = [100(NIR-RedEdge)-10(NIR-Green)]
```

### Example 49

```python
SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
```

### Example 50

```python
SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
```

### Example 51

```python
SR = NIR / Red
```

### Example 52

```python
SR = NIR / Red
```

### Example 53

```python
SRre = NIR / RedEdge
```

### Example 54

```python
SRre = NIR / RedEdge
```

### Example 55

```python
Band 1 = (Band5 / Band7) x 100
Band 2 = (Band5 / Band1) x 100
Band 3 = (Band3 / Band4) x (Band5 / Band4) x 100
```

### Example 56

```python
Band 1 = (Band5 / Band7) x 100
Band 2 = (Band5 / Band1) x 100
Band 3 = (Band3 / Band4) x (Band5 / Band4) x 100
```

### Example 57

```python
TSAVI = (s * (NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 58

```python
TSAVI = (s * (NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 59

```python
VARI = (Green - Red)/ (Green + Red - Blue)
```

### Example 60

```python
VARI = (Green - Red)/ (Green + Red - Blue)
```

### Example 61

```python
WNDWI = [Green – α * NIR – (1 – α) * SWIR ] / [Green + α * NIR + (1 – α) * SWIR]
```

### Example 62

```python
WNDWI = [Green – α * NIR – (1 – α) * SWIR ] / [Green + α * NIR + (1 – α) * SWIR]
```

---

## Colormap function

## Code Samples

### Example 1

```python
1 255 0 0
2 100 0 100
3 50 200 10
4 45 60 100
```

### Example 2

```python
1 255 0 0
2 100 0 100
3 50 200 10
4 45 60 100
```

---

## Compute Change function

## Code Samples

### Example 1

```python
To Raster - From Raster
```

### Example 2

```python
To Raster - From Raster
```

### Example 3

```python
(To Raster - From Raster)/max(From Raster, To Raster)
```

### Example 4

```python
(To Raster - From Raster)/max(From Raster, To Raster)
```

---

## Convolution function

## Code Samples

### Example 1

```python
1  0 -1
 2  0 -2
 1  0 -1
```

### Example 2

```python
-1 -2 -1
  0  0  0
  1  2  1
```

### Example 3

```python
0 -1 -2
 1  0 -1
 2  1  0
```

### Example 4

```python
-2 -1  0
 -1  0  1
  0  1  2
```

### Example 5

```python
1  2  1
  0  0  0 
 -1 -2 -1
```

### Example 6

```python
-1  0  1
 -2  0  2
 -1  0  1
```

### Example 7

```python
0 -1  0
-1  4 -1
 0 -1  0
```

### Example 8

```python
0  0 -1  0  0 
 0 -1 -2 -1  0
-1 -2 17 -2 -1
 0 -1 -2 -1  0
 0  0 -1  0  0
```

### Example 9

```python
-1 -1 -1
 2  2  2 
-1 -1 -1
```

### Example 10

```python
2 -1 -1
-1  2 -1
-1 -1  2
```

### Example 11

```python
-1 -1  2 
-1  2 -1
 2 -1 -1
```

### Example 12

```python
-1  0 -1 
-1  2 -1 
-1  2 -1
```

### Example 13

```python
-1 -2 -1
 0  0  0
 1  2  1
```

### Example 14

```python
-1  0  1 
-2  0  2 
-1  0  1
```

### Example 15

```python
0    -0.25    0
-0.25    2    -0.25
  0    -0.25    0
```

### Example 16

```python
-0.25 -0.25 -0.25 
-0.25  3    -0.25 
-0.25 -0.25 -0.25
```

### Example 17

```python
-1 -1 -1 
-1  9 -1 
-1 -1 -1
```

### Example 18

```python
-1 -3 -4 -3 -1 
-3  0  6  0 -3 
-4  6 21  6 -4 
-3  0  6  0 -3
-1 -3 -4 -3 -1
```

### Example 19

```python
0.111  0.111  0.111
0.111  0.111  0.111
0.111  0.111  0.111
```

### Example 20

```python
1  2  1
2  4  2
1  2  1
```

### Example 21

```python
1  1  1  1  1 
1  4  4  4  1 
1  4 12  4  1 
1  4  4  4  1 
1  1  1  1  1
```

### Example 22

```python
-0.627  0.352 -0.627
 0.352  2.923  0.352
-0.627  0.352 -0.627
```

---

## Distance Accumulation function

## Code Samples

### Example 1

```python
Keyword                   Zero    Low    High   Slope  Power  Cos    Sec
                          factor  cut    cut                  power  power
                                  angle  angle                             
------------------------  ------  -----  -----  -----  -----  -----  -----
Binary                    1.0     -30    30     ~      ~      ~      ~
Linear                    1.0     -90    90      1/90  ~      ~      ~
Symmetric linear          1.0     -90    90      1/90  ~      ~      ~
Inverse linear            1.0     -45    45     -1/45  ~      ~      ~
Symmetric inverse linear  1.0     -45    45     -1/45  ~      ~      ~
Cos                       ~       -90    90     ~      1.0    ~      ~
Sec                       ~       -90    90     ~      1.0    ~      ~
Cos_sec                   ~       -90    90     ~      ~      1.0    1.0
Sec_cos                   ~       -90    90     ~      ~      1.0    1.0
Hiking time               ~       -70    70     ~      ~      ~      ~
Bidirectional hiking time ~       -70    70     ~      ~      ~      ~
```

### Example 2

```python
Keywords         Zero factor   Cut angle     Slope   Side value
--------------   -----------   -----------   -----   ---------
Binary           1.0            45           ~       ~
Forward          0.5            45 (fixed)   ~       1.0
Linear           0.5           181            1/90   ~
Inverse linear   2.0           180           -1/90   ~
```

---

## Distance Allocation function

## Code Samples

### Example 1

```python
Keyword                   Zero    Low    High   Slope  Power  Cos    Sec
                          factor  cut    cut                  power  power
                                  angle  angle                             
------------------------  ------  -----  -----  -----  -----  -----  -----
Binary                    1.0     -30    30     ~      ~      ~      ~
Linear                    1.0     -90    90      1/90  ~      ~      ~
Symmetric linear          1.0     -90    90      1/90  ~      ~      ~
Inverse linear            1.0     -45    45     -1/45  ~      ~      ~
Symmetric inverse linear  1.0     -45    45     -1/45  ~      ~      ~
Cos                       ~       -90    90     ~      1.0    ~      ~
Sec                       ~       -90    90     ~      1.0    ~      ~
Cos_sec                   ~       -90    90     ~      ~      1.0    1.0
Sec_cos                   ~       -90    90     ~      ~      1.0    1.0
Hiking time               ~       -70    70     ~      ~      ~      ~
Bidirectional hiking time ~       -70    70     ~      ~      ~      ~
```

### Example 2

```python
Keywords         Zero factor   Cut angle     Slope   Side value
--------------   -----------   -----------   -----   ---------
Binary           1.0            45           ~       ~
Forward          0.5            45 (fixed)   ~       1.0
Linear           0.5           181            1/90   ~
Inverse linear   2.0           180           -1/90   ~
```

---

## Fundamentals of pan sharpening

## Code Samples

### Example 1

```python
Red_out = Red_in / [(blue_in + green_in + red_in) * Pan]
```

### Example 2

```python
Red_out = Red_in / [(blue_in + green_in + red_in) * Pan]
```

### Example 3

```python
DNF = (P - IW * I) / (RW * R + GW * G + BW * B)
Red_out = R * DNF
Green_out = G * DNF
Blue_out = B * DNF
Infrared_out = I * DNF
```

### Example 4

```python
DNF = (P - IW * I) / (RW * R + GW * G + BW * B)
Red_out = R * DNF
Green_out = G * DNF
Blue_out = B * DNF
Infrared_out = I * DNF
```

### Example 5

```python
P = panchromatic image
R = red band
G = green band
B = blue band
I = near infrared
W = weight
```

### Example 6

```python
P = panchromatic image
R = red band
G = green band
B = blue band
I = near infrared
W = weight
```

### Example 7

```python
ADJ = pan image - WA
Red_out = R + ADJ
Green_out = G + ADJ
Blue_out = B + ADJ
Near_Infrared_out = I + ADJ
```

### Example 8

```python
ADJ = pan image - WA
Red_out = R + ADJ
Green_out = G + ADJ
Blue_out = B + ADJ
Near_Infrared_out = I + ADJ
```

### Example 9

```python
Intensity = P - I * IW
```

### Example 10

```python
Intensity = P - I * IW
```

### Example 11

```python
Red_out= 0.5 * (Red_in + Pan_in)
Green_out = 0.5 * (Green_in + Pan_in)
Blue_out= 0.5 * (Blue_in + Pan_in)
```

### Example 12

```python
Red_out= 0.5 * (Red_in + Pan_in)
Green_out = 0.5 * (Green_in + Pan_in)
Blue_out= 0.5 * (Blue_in + Pan_in)
```

---

## Gradient function

## Code Samples

### Example 1

```python
(right pixel - current pixel) / Denominator Unit
```

### Example 2

```python
(right pixel - current pixel) / Denominator Unit
```

### Example 3

```python
(lower pixel - current pixel) / Denominator Unit
```

### Example 4

```python
(lower pixel - current pixel) / Denominator Unit
```

### Example 5

```python
(next slice - current slice) / Denominator Unit
```

### Example 6

```python
(next slice - current slice) / Denominator Unit
```

---

## Grayscale function

## Code Samples

### Example 1

```python
Output_temp = Band1*Weight1+Band2*Weight2+Band3*Weight3+...
```

### Example 2

```python
Output_temp = Band1*Weight1+Band2*Weight2+Band3*Weight3+...
```

### Example 3

```python
Output = Output_temp/(Sum of all Weights)
```

### Example 4

```python
Output = Output_temp/(Sum of all Weights)
```

---

## Heat Index function

## Code Samples

### Example 1

```python
Heat Index = (-42.379 + (2.04901523 * T) + (10.14333127 * R) - (0.22475541 * TR)  - (6.83783e-3 * TT) - (5.481717e-2 * RR) + (1.22874e-3 * TTR) + (8.5282e-4 * TRR) - (1.99e-6 * TTRR))
```

### Example 2

```python
Heat Index = (-42.379 + (2.04901523 * T) + (10.14333127 * R) - (0.22475541 * TR)  - (6.83783e-3 * TT) - (5.481717e-2 * RR) + (1.22874e-3 * TTR) + (8.5282e-4 * TRR) - (1.99e-6 * TTRR))
```

---

## Hillshade function

## Code Samples

### Example 1

```python
Adjusted Z-Factor = (Z Factor) + (Pixel Size)(Pixel Size Power) × (Pixel Size Factor)
```

### Example 2

```python
Adjusted Z-Factor = (Z Factor) + (Pixel Size)(Pixel Size Power) × (Pixel Size Factor)
```

---

## Key Metadata function

## Code Samples

### Example 1

```python
{
     "CloudCover": 4,
     "BandProperties":[
          {
               "BandName": "Blue",
               "WavelengthMin": 445,
               "WavelengthMax": 516
         },
         {
              "BandName": "Green",
              "WavelengthMin": 506,
              "WavelengthMax": 595
         },

    ]
}
```

### Example 2

```python
{
     "CloudCover": 4,
     "BandProperties":[
          {
               "BandName": "Blue",
               "WavelengthMin": 445,
               "WavelengthMax": 516
         },
         {
              "BandName": "Green",
              "WavelengthMin": 506,
              "WavelengthMax": 595
         },

    ]
}
```

---

## NDVI function

## Code Samples

### Example 1

```python
NDVI = ((IR - R)/(IR + R)) * 100 + 100
```

### Example 2

```python
NDVI = ((IR - R)/(IR + R)) * 100 + 100
```

### Example 3

```python
NDVI = ((IR - R)/(IR + R))
```

### Example 4

```python
NDVI = ((IR - R)/(IR + R))
```

---

## Path Distance Allocation function

## Code Samples

### Example 1

```python
Keywords         Zero factor   Cut angle     Slope   Side value
--------------   -----------   -----------   -----   ---------
Binary           1.0            45           ~       ~
Forward          0.5            45 (fixed)   ~       1.0
Linear           0.5           181            1/90   ~
Inverse linear   2.0           180           -1/90   ~
```

### Example 2

```python
Keyword                   Zero    Low    High   Slope  Power  Cos    Sec
                          factor  cut    cut                  power  power
                                  angle  angle                             
------------------------  ------  -----  -----  -----  -----  -----  -----
Binary                    1.0     -30    30     ~      ~      ~      ~
Linear                    1.0     -90    90      1/90  ~      ~      ~
Symmetric linear          1.0     -90    90      1/90  ~      ~      ~
Inverse linear            1.0     -45    45     -1/45  ~      ~      ~
Symmetric inverse linear  1.0     -45    45     -1/45  ~      ~      ~
Cos                       ~       -90    90     ~      1.0    ~      ~
Sec                       ~       -90    90     ~      1.0    ~      ~
Cos_sec                   ~       -90    90     ~      ~      1.0    1.0
Sec_cos                   ~       -90    90     ~      ~      1.0    1.0
Hiking time               ~       -70    70     ~      ~      ~      ~
Bidirectional hiking time ~       -70    70     ~      ~      ~      ~
```

---

## Path Distance Back Link function

## Code Samples

### Example 1

```python
Keywords         Zero factor   Cut angle     Slope   Side value
--------------   -----------   -----------   -----   ---------
Binary           1.0            45           ~       ~
Forward          0.5            45 (fixed)   ~       1.0
Linear           0.5           181            1/90   ~
Inverse linear   2.0           180           -1/90   ~
```

### Example 2

```python
Keyword                   Zero    Low    High   Slope  Power  Cos    Sec
                          factor  cut    cut                  power  power
                                  angle  angle                             
------------------------  ------  -----  -----  -----  -----  -----  -----
Binary                    1.0     -30    30     ~      ~      ~      ~
Linear                    1.0     -90    90      1/90  ~      ~      ~
Symmetric linear          1.0     -90    90      1/90  ~      ~      ~
Inverse linear            1.0     -45    45     -1/45  ~      ~      ~
Symmetric inverse linear  1.0     -45    45     -1/45  ~      ~      ~
Cos                       ~       -90    90     ~      1.0    ~      ~
Sec                       ~       -90    90     ~      1.0    ~      ~
Cos_sec                   ~       -90    90     ~      ~      1.0    1.0
Sec_cos                   ~       -90    90     ~      ~      1.0    1.0
Hiking time               ~       -70    70     ~      ~      ~      ~
Bidirectional hiking time ~       -70    70     ~      ~      ~      ~
```

---

## Path Distance function

## Code Samples

### Example 1

```python
Keywords         Zero factor   Cut angle     Slope   Side value
--------------   -----------   -----------   -----   ---------
Binary           1.0            45           ~       ~
Forward          0.5            45 (fixed)   ~       1.0
Linear           0.5           181            1/90   ~
Inverse linear   2.0           180           -1/90   ~
```

### Example 2

```python
Keyword                   Zero    Low    High   Slope  Power  Cos    Sec
                          factor  cut    cut                  power  power
                                  angle  angle                             
------------------------  ------  -----  -----  -----  -----  -----  -----
Binary                    1.0     -30    30     ~      ~      ~      ~
Linear                    1.0     -90    90      1/90  ~      ~      ~
Symmetric linear          1.0     -90    90      1/90  ~      ~      ~
Inverse linear            1.0     -45    45     -1/45  ~      ~      ~
Symmetric inverse linear  1.0     -45    45     -1/45  ~      ~      ~
Cos                       ~       -90    90     ~      1.0    ~      ~
Sec                       ~       -90    90     ~      1.0    ~      ~
Cos_sec                   ~       -90    90     ~      ~      1.0    1.0
Sec_cos                   ~       -90    90     ~      ~      1.0    1.0
Hiking time               ~       -70    70     ~      ~      ~      ~
Bidirectional hiking time ~       -70    70     ~      ~      ~      ~
```

---

## Round Down function

## Code Samples

### Example 1

```python
Input   Output
     5.3     5.0
     4.9     4.0
     3.0     3.0
     6.5     6.0
    -0.2    -1.0
    -2.8    -3.0
```

---

## Round Up function

## Code Samples

### Example 1

```python
Input   Output
    5.3     6.0
    4.9     5.0
    3.0     3.0
    6.5     7.0
   -0.2     0.0
   -2.8    -2.0
```

---

## Slope function

## Code Samples

### Example 1

```python
Adjusted Z Factor = (Z Factor) + (Pixel Size)PSP × PSF)
```

### Example 2

```python
Adjusted Z Factor = (Z Factor) + (Pixel Size)PSP × PSF)
```

---

## Spectral Conversion function

## Code Samples

### Example 1

```python
Output Band_R = Weight_P * Band_C
```

### Example 2

```python
Output Band_R = Weight_P * Band_C
```

### Example 3

```python
Output Band_R = Weight_P * Band_C
```

### Example 4

```python
Output Band_R = Weight_P * Band_C
```

### Example 5

```python
0.1 0.9 0.0 
0.3 0.0 0.7 
0.1 0.1 0.8
```

---

## Vector Field function

## Code Samples

### Example 1

```python
u = m * cos (pi *d / 180)
```

### Example 2

```python
u = m * cos (pi *d / 180)
```

### Example 3

```python
v = m * sin (pi * d /180)
```

### Example 4

```python
v = m * sin (pi * d /180)
```

### Example 5

```python
m = sqrt (u * u + v * v)
```

### Example 6

```python
m = sqrt (u * u + v * v)
```

### Example 7

```python
d = atan2 (v / u) * 180 / p
```

### Example 8

```python
d = atan2 (v / u) * 180 / p
```

---

## Wind Chill function

## Code Samples

### Example 1

```python
WS16 = np.pwer(WS, 0.16)
Wind Chill = 35.74 + (0.6215 * T) - (35.75 * WS16) + (0.4275 * T * WS16)
```

### Example 2

```python
WS16 = np.pwer(WS, 0.16)
Wind Chill = 35.74 + (0.6215 * T) - (35.75 * WS16) + (0.4275 * T * WS16)
```

---

## Map algebra in Spatial Analyst

## Code Samples

### Example 1

```python
from arcpy.sa import *
outShade = Hillshade("inelevation.tif", 99, 33)
```

### Example 2

```python
from arcpy.sa import *
outShade = Hillshade("inelevation.tif", 99, 33)
```

### Example 3

```python
# Name: Slope
# Description: Identifies the rate of maximum change
#               in z-value from each cell.
# Requirements: Spatial Analyst Extension


# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outMeasurement = "DEGREE"
zFactor = 0.3043

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run Slope
outSlope = Slope(inRaster, outMeasurement, zFactor)

# Save the output
outSlope.save("C:/output/outslope02")
```

### Example 4

```python
# Name: Slope
# Description: Identifies the rate of maximum change
#               in z-value from each cell.
# Requirements: Spatial Analyst Extension


# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outMeasurement = "DEGREE"
zFactor = 0.3043

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run Slope
outSlope = Slope(inRaster, outMeasurement, zFactor)

# Save the output
outSlope.save("C:/output/outslope02")
```

### Example 5

```python
# In the following statement, indem is either  
#   in the TOC or in the current workspace
outRas = Aspect("indem")

# In the following statement the full path is specified
outRas2 = Aspect("C:/Data/indem2.tif")
```

### Example 6

```python
# In the following statement, indem is either  
#   in the TOC or in the current workspace
outRas = Aspect("indem")

# In the following statement the full path is specified
outRas2 = Aspect("C:/Data/indem2.tif")
```

### Example 7

```python
outRas = Select("inras.tif", "Value > 105")

# outRas is variable defined by the previous statement and is not quoted
outdist = EucDistance(outRas)
```

### Example 8

```python
outRas = Select("inras.tif", "Value > 105")

# outRas is variable defined by the previous statement and is not quoted
outdist = EucDistance(outRas)
```

### Example 9

```python
# set outVar to 14 using the Python + operator
outVar = 5 + 9
```

### Example 10

```python
# set outVar to 14 using the Python + operator
outVar = 5 + 9
```

### Example 11

```python
outRas = Raster("inras1.tif") + Raster("inras2.tif")
```

### Example 12

```python
outRas = Raster("inras1.tif") + Raster("inras2.tif")
```

### Example 13

```python
outRas = Raster("inras1.tif") + 8
```

### Example 14

```python
outRas = Raster("inras1.tif") + 8
```

### Example 15

```python
outRas = Slope("indem" * 2) / 57
outdist = EucDistance(ExtractByAttributes("inras", "Value > 105"))
```

### Example 16

```python
outRas = Slope("indem" * 2) / 57
outdist = EucDistance(ExtractByAttributes("inras", "Value > 105"))
```

### Example 17

```python
outRas1 = (Raster("inras1") + Raster("inras2")) / Raster("inras3")
```

### Example 18

```python
outRas1 = (Raster("inras1") + Raster("inras2")) / Raster("inras3")
```

### Example 19

```python
outRas2 = Raster("inras1") + Raster("inras2") / Raster("inras3")
```

### Example 20

```python
outRas2 = Raster("inras1") + Raster("inras2") / Raster("inras3")
```

### Example 21

```python
outRas = (Raster("a") > 2) & (Raster("a") < 5)
```

### Example 22

```python
outRas = (Raster("a") > 2) & (Raster("a") < 5)
```

### Example 23

```python
outRas = FocalStatistics("inRaster", NbrCircle(5, "CELL"), "SUM")
```

### Example 24

```python
outRas = FocalStatistics("inRaster", NbrCircle(5, "CELL"), "SUM")
```

### Example 25

```python
outReclass = Reclassify("inRaster", "VALUE", RemapRange([[0, 1], [3, 10], [4, 8]]))
```

### Example 26

```python
outReclass = Reclassify("inRaster", "VALUE", RemapRange([[0, 1], [3, 10], [4, 8]]))
```

### Example 27

```python
indem = "C:/Data/indem"
contourInterval = 100
Contour(indem, "C:/output/outcontours", contourInterval)
```

### Example 28

```python
indem = "C:/Data/indem"
contourInterval = 100
Contour(indem, "C:/output/outcontours", contourInterval)
```

### Example 29

```python
import arcpy 
from arcpy import env 
from arcpy.sa import *

env.workspace = "C:/sapyexamples/data" 

outHillshade = Hillshade("elevation", 180, 75, "SHADOWS", 1)

outHillshade.save("outhillshd01")
```

### Example 30

```python
import arcpy 
from arcpy import env 
from arcpy.sa import *

env.workspace = "C:/sapyexamples/data" 

outHillshade = Hillshade("elevation", 180, 75, "SHADOWS", 1)

outHillshade.save("outhillshd01")
```

### Example 31

```python
import arcpy 
from arcpy import env
from arcpy.sa import *

env.workspace = "C:/sapyexamples/data" 
myRemapRange = RemapRange([[-3, 0, 0], [0, 1.75, 25], [1.75, 3.5, 50], 
                           [3.5, 5.25, 75], [5.25, 7, 100]]) 

outReclassRR = Reclassify("inreclass", "VALUE", myRemapRange)

outReclassRR.save("rclassremran")
```

### Example 32

```python
import arcpy 
from arcpy import env
from arcpy.sa import *

env.workspace = "C:/sapyexamples/data" 
myRemapRange = RemapRange([[-3, 0, 0], [0, 1.75, 25], [1.75, 3.5, 50], 
                           [3.5, 5.25, 75], [5.25, 7, 100]]) 

outReclassRR = Reclassify("inreclass", "VALUE", myRemapRange)

outReclassRR.save("rclassremran")
```

---

## Map algebra syntax and components

## Code Samples

### Example 1

```python
Output_Name = Action
```

### Example 2

```python
Output_Name = Action
```

### Example 3

```python
outRas = Aspect("C:/Data/inraster.tif")
```

### Example 4

```python
outRas = Aspect("C:/Data/inraster.tif")
```

### Example 5

```python
outRas = Raster("inraster1.tif") + Raster("inraster2.tif")
```

### Example 6

```python
outRas = Raster("inraster1.tif") + Raster("inraster2.tif")
```

### Example 7

```python
# In the following statement outVar will be set to 15
outVar = 6 + 9
```

### Example 8

```python
# In the following statement outVar will be set to 15
outVar = 6 + 9
```

### Example 9

```python
outRas = Sin("inraster.tif")
```

### Example 10

```python
outRas = Sin("inraster.tif")
```

### Example 11

```python
outRas = Slope("inraster.tif", "PERCENT_RISE")
```

### Example 12

```python
outRas = Slope("inraster.tif", "PERCENT_RISE")
```

### Example 13

```python
outRas = Slope("inraster.tif")
```

### Example 14

```python
outRas = Slope("inraster.tif")
```

### Example 15

```python
# The following statement takes the slope of the input elevation in degrees.
outRas = Slope("elevation.tif", "DEGREE", 0.3043)
```

### Example 16

```python
# The following statement takes the slope of the input elevation in degrees.
outRas = Slope("elevation.tif", "DEGREE", 0.3043)
```

---

## Spatial Analyst classes

## Code Samples

### Example 1

```python
Neighborhood = NbrRectangle(5, 5, "MAP")
outRas = FocalStatistics("inRas", Neighborhood, "MEAN")
```

### Example 2

```python
Neighborhood = NbrRectangle(5, 5, "MAP")
outRas = FocalStatistics("inRas", Neighborhood, "MEAN")
```

### Example 3

```python
outRas = FocalStatistics("inRas", NbrRectangle(5, 5, "MAP"), "MEAN")
```

### Example 4

```python
outRas = FocalStatistics("inRas", NbrRectangle(5, 5, "MAP"), "MEAN")
```

### Example 5

```python
Neighborhood = NbrCircle(5, "MAP")
outRas = FocalStatistics("inRas", Neighborhood, "MAXIMUM")
```

### Example 6

```python
Neighborhood = NbrCircle(5, "MAP")
outRas = FocalStatistics("inRas", Neighborhood, "MAXIMUM")
```

### Example 7

```python
inBoundary = TopoBoundary(["inBound1.shp", "inBound2.shp"])
```

### Example 8

```python
inBoundary = TopoBoundary(["inBound1.shp", "inBound2.shp"])
```

### Example 9

```python
# Usage: RemapRange([[startValue, endValue, newValue],...])
myRemapRange = RemapRange([[-3, -1.75, 1], [-1.75, -0.5, 2], [-0.5, 0.75, 3], 
                           [0.75, 2, 4], [2, 3.25, 5], [3.25, 4.5, 6],
                           [4.5, 5.75, 7], [5.75, 7, 8]])
outReclassRR = Reclassify("inRas", "VALUE", myRemapRange)
```

### Example 10

```python
# Usage: RemapRange([[startValue, endValue, newValue],...])
myRemapRange = RemapRange([[-3, -1.75, 1], [-1.75, -0.5, 2], [-0.5, 0.75, 3], 
                           [0.75, 2, 4], [2, 3.25, 5], [3.25, 4.5, 6],
                           [4.5, 5.75, 7], [5.75, 7, 8]])
outReclassRR = Reclassify("inRas", "VALUE", myRemapRange)
```

---

## Complex statements

## Code Samples

### Example 1

```python
outRaster = Raster("inras1") + Raster("inras2") / Raster("inras3")
```

### Example 2

```python
outRaster = Raster("inras1") + Raster("inras2") / Raster("inras3")
```

### Example 3

```python
outRas = Raster("inras1") / (Raster("inras2") + Raster("inras3"))
```

### Example 4

```python
outRas = Raster("inras1") / (Raster("inras2") + Raster("inras3"))
```

### Example 5

```python
outRas = (Raster("a") > 2 ) & ( Raster("a") < 5)
```

### Example 6

```python
outRas = (Raster("a") > 2 ) & ( Raster("a") < 5)
```

### Example 7

```python
outRas = Sin("inras1") + Raster("inras2") + 8
```

### Example 8

```python
outRas = Sin("inras1") + Raster("inras2") + 8
```

### Example 9

```python
const = 10
outRas = Raster("inras1") + 2 * const
```

### Example 10

```python
const = 10
outRas = Raster("inras1") + 2 * const
```

### Example 11

```python
num = 10
outRas = (ZonalStatistics((Raster("inras2") + Raster("inras3")),
                         "Value", "valueras", "MAXIMUM") - num ) / 8
```

### Example 12

```python
num = 10
outRas = (ZonalStatistics((Raster("inras2") + Raster("inras3")),
                         "Value", "valueras", "MAXIMUM") - num ) / 8
```

### Example 13

```python
outAdd = Raster("inras1") + Raster("inras2")
outRas = FocalStatistics(outAdd, NbrCircle(5, "Map"), "MEAN")
```

### Example 14

```python
outAdd = Raster("inras1") + Raster("inras2")
outRas = FocalStatistics(outAdd, NbrCircle(5, "Map"), "MEAN")
```

### Example 15

```python
outdistance = EucDistance(ContourList("elevation", "#", [1500]))
```

### Example 16

```python
outdistance = EucDistance(ContourList("elevation", "#", [1500]))
```

### Example 17

```python
dist = EucDistance(arcpy.Select_analysis("schools", "#", "Pop>2000"))
```

### Example 18

```python
dist = EucDistance(arcpy.Select_analysis("schools", "#", "Pop>2000"))
```

### Example 19

```python
costDist = CostDistance("source", "in_cost", 15000, "out_bklink") 
costOut = CostPath("dest", costDist, "out_bklink")
```

### Example 20

```python
costDist = CostDistance("source", "in_cost", 15000, "out_bklink") 
costOut = CostPath("dest", costDist, "out_bklink")
```

### Example 21

```python
bklink = "C:/results/out_bklink"
costDist = CostDistance("source", "in_cost", 15000, bklink) 
costOut = CostPath("dest", costDist, bklink)
```

### Example 22

```python
bklink = "C:/results/out_bklink"
costDist = CostDistance("source", "in_cost", 15000, bklink) 
costOut = CostPath("dest", costDist, bklink)
```

---

## Change arguments in classes

## Code Samples

### Example 1

```python
neighborhood = NbrCircle(5, "MAP")

# The neighborhood object can be changed from a circle to a rectangle
neighborhood = NbrRectangle(3, 3, "MAP")
```

### Example 2

```python
neighborhood = NbrCircle(5, "MAP")

# The neighborhood object can be changed from a circle to a rectangle
neighborhood = NbrRectangle(3, 3, "MAP")
```

### Example 3

```python
>>> neighborhood = NbrCircle(5, "MAP")
>>> # The following statements change the radius to 7 and the units to CELL
>>> neighborhood.radius = 7 
>>> neighborhood.units = "CELL"

>>> print(neighborhood)
CIRCLE 7 CELL
```

### Example 4

```python
>>> neighborhood = NbrCircle(5, "MAP")
>>> # The following statements change the radius to 7 and the units to CELL
>>> neighborhood.radius = 7 
>>> neighborhood.units = "CELL"

>>> print(neighborhood)
CIRCLE 7 CELL
```

### Example 5

```python
circle = NbrCircle(5, "CELL")

# The following statement changes the radius to 5.5
circle.radius = circle.radius * 1.1
```

### Example 6

```python
circle = NbrCircle(5, "CELL")

# The following statement changes the radius to 5.5
circle.radius = circle.radius * 1.1
```

### Example 7

```python
# The following statement changes the radius to 5.5
circle.radius *= 1.1
```

### Example 8

```python
# The following statement changes the radius to 5.5
circle.radius *= 1.1
```

### Example 9

```python
>>> arguments = TopoStream(["features1", "features2"]) 

>>> arguments.inFeatures.append("features3")
>>> arguments.inFeatures += ["features4", "features5"]

>>> print(arguments.inFeatures)
['features1', 'features2', 'features3', 'features4', 'features5']
```

### Example 10

```python
>>> arguments = TopoStream(["features1", "features2"]) 

>>> arguments.inFeatures.append("features3")
>>> arguments.inFeatures += ["features4", "features5"]

>>> print(arguments.inFeatures)
['features1', 'features2', 'features3', 'features4', 'features5']
```

### Example 11

```python
>>> arguments = TopoStream(["features1", "features2", "features3", "features4", "features5"])
>>> del arguments.inFeatures[2]

>>> print(arguments.inFeatures)
['features1', 'features2', 'features4', 'features5']
```

### Example 12

```python
>>> arguments = TopoStream(["features1", "features2", "features3", "features4", "features5"])
>>> del arguments.inFeatures[2]

>>> print(arguments.inFeatures)
['features1', 'features2', 'features4', 'features5']
```

### Example 13

```python
>>> arguments = TopoStream(["features1", "features2"]) 
>>> arguments.inFeatures[1] = "lake2"

>>> print(arguments.inFeatures)
['features1', 'lake2']
```

### Example 14

```python
>>> arguments = TopoStream(["features1", "features2"]) 
>>> arguments.inFeatures[1] = "lake2"

>>> print(arguments.inFeatures)
['features1', 'lake2']
```

### Example 15

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])

>>> # Change the newValue 12 in the second reclassification to a 10
>>> remap.remapTable[1][1] = 10

>>> print(remap.remapTable)
[[1, 11], [2, 10], [3, 13]]
```

### Example 16

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])

>>> # Change the newValue 12 in the second reclassification to a 10
>>> remap.remapTable[1][1] = 10

>>> print(remap.remapTable)
[[1, 11], [2, 10], [3, 13]]
```

### Example 17

```python
remap = RemapRange([[1, 10, 5], [10, 20, 8], [20, 30, 10]])

# The following statement increases the endValue 20 by 5 percent
remap.remapTable[1][1] *= 1.05 

# Another implementation of increasing an entry by 5 percent
remap.remapTable[1][1] = remapTable.table[1][1] * 1.05
```

### Example 18

```python
remap = RemapRange([[1, 10, 5], [10, 20, 8], [20, 30, 10]])

# The following statement increases the endValue 20 by 5 percent
remap.remapTable[1][1] *= 1.05 

# Another implementation of increasing an entry by 5 percent
remap.remapTable[1][1] = remapTable.table[1][1] * 1.05
```

### Example 19

```python
>>> remap = RemapValue([[1, 11], [2, 12], [4, 13]])

>>> # Change the second reclassification [2, 12] to [3,10]
>>> remap.table[1] = [3, 10]
  
>>> print(remap.remapTable)
[[1, 11], [3, 10], [4, 13]]
```

### Example 20

```python
>>> remap = RemapValue([[1, 11], [2, 12], [4, 13]])

>>> # Change the second reclassification [2, 12] to [3,10]
>>> remap.table[1] = [3, 10]
  
>>> print(remap.remapTable)
[[1, 11], [3, 10], [4, 13]]
```

### Example 21

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])

>>> # Add a forth reclassification, [4, 14] to the end
>>> remap.remapTable.append([4, 14]) 

>>> # Another approach for adding a row
>>> remap.remapTable += [[5, 15]] 

>>> print(remap.remapTable)
[[1, 11], [2, 12], [3, 13], [4, 14], [5, 15]]
```

### Example 22

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])

>>> # Add a forth reclassification, [4, 14] to the end
>>> remap.remapTable.append([4, 14]) 

>>> # Another approach for adding a row
>>> remap.remapTable += [[5, 15]] 

>>> print(remap.remapTable)
[[1, 11], [2, 12], [3, 13], [4, 14], [5, 15]]
```

### Example 23

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13], [4, 14], [5, 15]])

>>> # Delete the entire second reclassification
>>> del remap.remapTable[1]

>>> print(remap.remapTable)
[[1, 11], [3, 13], [4, 14], [5, 15]]
```

### Example 24

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13], [4, 14], [5, 15]])

>>> # Delete the entire second reclassification
>>> del remap.remapTable[1]

>>> print(remap.remapTable)
[[1, 11], [3, 13], [4, 14], [5, 15]]
```

### Example 25

```python
>>> points = [Point(0, 5), Point(15, 175)]

>>> # Change the X value of the second input to 25
>>> points[1].X = 25 

>>> print(points)
[<Point (0.0, 5.0, #, #)>, <Point (25.0, 175.0, #, #)>]
```

### Example 26

```python
>>> points = [Point(0, 5), Point(15, 175)]

>>> # Change the X value of the second input to 25
>>> points[1].X = 25 

>>> print(points)
[<Point (0.0, 5.0, #, #)>, <Point (25.0, 175.0, #, #)>]
```

---

## Create classes

## Code Samples

### Example 1

```python
# Creating a neighborhood class and assigning it to a variable
neighborhood = NbrRectangle(10, 10, "CELL") 

outFocalStats = FocalStatistics(inRas, neighborhood, "MINORITY")
```

### Example 2

```python
# Creating a neighborhood class and assigning it to a variable
neighborhood = NbrRectangle(10, 10, "CELL") 

outFocalStats = FocalStatistics(inRas, neighborhood, "MINORITY")
```

### Example 3

```python
# Creating the Kriging model to be used
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", 2000, 2.6, 542, 0)

# Creating a radius class and assigning it to a variable
kRadius = RadiusFixed(20000, 1) 

outKriging = Kriging(inFeatures, field, kModelOrdinary, cellSize, 
                     kRadius, outVarRaster)
```

### Example 4

```python
# Creating the Kriging model to be used
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", 2000, 2.6, 542, 0)

# Creating a radius class and assigning it to a variable
kRadius = RadiusFixed(20000, 1) 

outKriging = Kriging(inFeatures, field, kModelOrdinary, cellSize, 
                     kRadius, outVarRaster)
```

### Example 5

```python
# Create classes as input for TopoToRaster
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], 
                                   ["spots2.shp", "elev"]]) 
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"]) 
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]]) 
myTopoStream = TopoStream(["streams.shp"])

# Applying the tool
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, 
                                myTopoLake, myTopoSink, myTopoStream])
```

### Example 6

```python
# Create classes as input for TopoToRaster
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], 
                                   ["spots2.shp", "elev"]]) 
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"]) 
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]]) 
myTopoStream = TopoStream(["streams.shp"])

# Applying the tool
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, 
                                myTopoLake, myTopoSink, myTopoStream])
```

### Example 7

```python
# The RemapValue class has a usage of: 
#   RemapRange(startValue, endValue, newValue)
RemapTable = RemapValue([[1, 5], [2, 8], [3, 1], [4, 10]])

# Run the tool 
outReclass = Reclassify("inRas", RemapTable)
```

### Example 8

```python
# The RemapValue class has a usage of: 
#   RemapRange(startValue, endValue, newValue)
RemapTable = RemapValue([[1, 5], [2, 8], [3, 1], [4, 10]])

# Run the tool 
outReclass = Reclassify("inRas", RemapTable)
```

### Example 9

```python
# Identify the points to be extracted by creating a list
#   of Point objects.
PointsToExtract = [Point(0, 5), Point(15, 175), Point(225, 450)] 

# Run the tool
Outraster = ExtractByPoints(PointsToExtract)
```

### Example 10

```python
# Identify the points to be extracted by creating a list
#   of Point objects.
PointsToExtract = [Point(0, 5), Point(15, 175), Point(225, 450)] 

# Run the tool
Outraster = ExtractByPoints(PointsToExtract)
```

### Example 11

```python
NbrWedge({radius}, {startAngle}, {endAngle}, {units})
```

### Example 12

```python
NbrWedge({radius}, {startAngle}, {endAngle}, {units})
```

### Example 13

```python
# The circle neighborhood will default to
#   a radius of 3 and units of CELL
circle = NbrCircle()
```

### Example 14

```python
# The circle neighborhood will default to
#   a radius of 3 and units of CELL
circle = NbrCircle()
```

---

## Create output

## Code Samples

### Example 1

```python
outSlope = Slope("indem")
```

### Example 2

```python
outSlope = Slope("indem")
```

### Example 3

```python
outDirection = FlowDirection("inelevation")
outAccumulation = FlowAccumulation(outDirection)
```

### Example 4

```python
outDirection = FlowDirection("inelevation")
outAccumulation = FlowAccumulation(outDirection)
```

### Example 5

```python
outSlope = Slope("indem")
outSlope.save("sloperaster")
```

### Example 6

```python
outSlope = Slope("indem")
outSlope.save("sloperaster")
```

### Example 7

```python
# An empty string, "", indicates the use of a default value for the parameter.
# In the following statement the defaults are taken for maximum_distance and 
# cell_size parameters. outdirection will be a a permanent raster stored in the 
# current workspace.
outDistance = EucDistance("input", "", "", "outdirection")
```

### Example 8

```python
# An empty string, "", indicates the use of a default value for the parameter.
# In the following statement the defaults are taken for maximum_distance and 
# cell_size parameters. outdirection will be a a permanent raster stored in the 
# current workspace.
outDistance = EucDistance("input", "", "", "outdirection")
```

### Example 9

```python
Contour("elevation", "C:/sapyexamples/output/outcontours.shp", 200, 0)
```

### Example 10

```python
Contour("elevation", "C:/sapyexamples/output/outcontours.shp", 200, 0)
```

---

## Run tools in map algebra

## Code Samples

### Example 1

```python
outRas = Slope("elevation.tif", "PERCENT_RISE", 3)
```

### Example 2

```python
outRas = Slope("elevation.tif", "PERCENT_RISE", 3)
```

### Example 3

```python
outRas = ZonalStatistics("inzoneraster.tif", "Value", 
                         "invalueraster.tif", "MEAN")
```

### Example 4

```python
outRas = ZonalStatistics("inzoneraster.tif", "Value", 
                         "invalueraster.tif", "MEAN")
```

### Example 5

```python
# The following tools have correct capitalization
#  and spelling, and are valid.
outRas = Square("inraster.tif")
outRas2 = GreaterThan("inraster.tif", "inraster2.tif")
```

### Example 6

```python
# The following tools have correct capitalization
#  and spelling, and are valid.
outRas = Square("inraster.tif")
outRas2 = GreaterThan("inraster.tif", "inraster2.tif")
```

### Example 7

```python
# The following is invalid because the tool name starts with a capital letter.
outRas = square("inraster")

# The following is invalid because the tool name is capitalized incorrectly.
outRas2 = Greaterthan("inraster", "inraster2")
```

### Example 8

```python
# The following is invalid because the tool name starts with a capital letter.
outRas = square("inraster")

# The following is invalid because the tool name is capitalized incorrectly.
outRas2 = Greaterthan("inraster", "inraster2")
```

### Example 9

```python
# Complex expression using two Spatial Analyst tools
outRas = Slice(Slope("C:/Data/elevation.tif"), 10)
```

### Example 10

```python
# Complex expression using two Spatial Analyst tools
outRas = Slice(Slope("C:/Data/elevation.tif"), 10)
```

### Example 11

```python
# The Result object output from the Buffer tool
#  is used as the zone input for the Zonal Statistics tool  
outRas = ZonalStatistics(arcpy.Buffer_analysis("C:/Data/schools.shp", "#", 500),
                         "OBJECTID", "C:/Data/pop1990.tif", "SUM")
```

### Example 12

```python
# The Result object output from the Buffer tool
#  is used as the zone input for the Zonal Statistics tool  
outRas = ZonalStatistics(arcpy.Buffer_analysis("C:/Data/schools.shp", "#", 500),
                         "OBJECTID", "C:/Data/pop1990.tif", "SUM")
```

---

## Import the Spatial Analyst module

## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
```

### Example 3

```python
env.workspace = "c:/base/data.gdb"
```

### Example 4

```python
env.workspace = "c:/base/data.gdb"
```

### Example 5

```python
arcpy.Buffer_analysis("infeatures", "outbuffer", 5000)
```

### Example 6

```python
arcpy.Buffer_analysis("infeatures", "outbuffer", 5000)
```

### Example 7

```python
outRas = Sin("inraster1") + Raster("inraster2") + 8
```

### Example 8

```python
outRas = Sin("inraster1") + Raster("inraster2") + 8
```

### Example 9

```python
# Check out the ArcGIS Spatial Analyst
# extension license
arcpy.CheckOutExtension("Spatial")
```

### Example 10

```python
# Check out the ArcGIS Spatial Analyst
# extension license
arcpy.CheckOutExtension("Spatial")
```

### Example 11

```python
# File: pythonstartup.py
# Description: Used to customize the state of the Python startup environment 
#   upon startup of ArcGIS application
#   Can specify module imports, variables, messages
# Requirements: Spatial Analyst Extension

# Print to screen
print("import os\nimport sys\nimport arcpy\nfrom arcpy import env\nfrom arcpy.sa import *")

# Imports
import os
import sys
import arcpy
from arcpy import env
from arcpy.sa import *
```

### Example 12

```python
# File: pythonstartup.py
# Description: Used to customize the state of the Python startup environment 
#   upon startup of ArcGIS application
#   Can specify module imports, variables, messages
# Requirements: Spatial Analyst Extension

# Print to screen
print("import os\nimport sys\nimport arcpy\nfrom arcpy import env\nfrom arcpy.sa import *")

# Imports
import os
import sys
import arcpy
from arcpy import env
from arcpy.sa import *
```

---

## Output from tools in map algebra

## Code Samples

### Example 1

```python
outraster = Slope("C:/Data/elevation") 
outraster.save("C:/output/sloperaster")
```

### Example 2

```python
outraster = Slope("C:/Data/elevation") 
outraster.save("C:/output/sloperaster")
```

### Example 3

```python
outraster.save()
```

### Example 4

```python
outraster.save()
```

### Example 5

```python
outraster.save("C:/output/file_gdb.gdb/sloperaster")
outraster.save("C:/output/sloperaster.tif")
```

### Example 6

```python
outraster.save("C:/output/file_gdb.gdb/sloperaster")
outraster.save("C:/output/sloperaster.tif")
```

---

## Query classes

## Code Samples

### Example 1

```python
circle = NbrCircle(5, "CELL")

# varRadius will be assigned the radius property (which is 5)
varRadius = circle.radius
```

### Example 2

```python
circle = NbrCircle(5, "CELL")

# varRadius will be assigned the radius property (which is 5)
varRadius = circle.radius
```

### Example 3

```python
>>> circle = NbrCircle(5, "CELL")
>>> print(circle)
Circle 5 Cell
>>> print(circle.radius)
5
```

### Example 4

```python
>>> circle = NbrCircle(5, "CELL")
>>> print(circle)
Circle 5 Cell
>>> print(circle.radius)
5
```

### Example 5

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])
>>> print(remap)
1 11; 2 12; 3 13
>>> print(remap.remapTable)
[[1, 11], [2, 12], [3, 13]]
```

### Example 6

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])
>>> print(remap)
1 11; 2 12; 3 13
>>> print(remap.remapTable)
[[1, 11], [2, 12], [3, 13]]
```

### Example 7

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])
>>> print(remap.remapTable[1][1])
12
```

### Example 8

```python
>>> remap = RemapValue([[1, 11], [2, 12], [3, 13]])
>>> print(remap.remapTable[1][1])
12
```

### Example 9

```python
>>> points = [Point(0, 5), Point(15, 175), Point(225, 450)]
>>> # The following statement queries the x value of the second input point
>>> xvalue = points[1].X
>>> print(xvalue)
15.0
```

### Example 10

```python
>>> points = [Point(0, 5), Point(15, 175), Point(225, 450)]
>>> # The following statement queries the x value of the second input point
>>> xvalue = points[1].X
>>> print(xvalue)
15.0
```

### Example 11

```python
>>> neighborhood = NbrCircle(5, "CELL")
>>> neighType = type(neighborhood)
>>> print(neighType)
<class 'arcpy.sa.ParameterClasses.NbrCircle'>
```

### Example 12

```python
>>> neighborhood = NbrCircle(5, "CELL")
>>> neighType = type(neighborhood)
>>> print(neighType)
<class 'arcpy.sa.ParameterClasses.NbrCircle'>
```

### Example 13

```python
circle = NbrCircle(5, "CELL")

# The general format is: isinstance(AnyObject, AnyClass)
# In the following statement, val will be assigned True
val = isinstance(circle, NbrCircle) 

# In the following statement, val will be assigned False
val = isinstance(circle, NbrRectangle)
```

### Example 14

```python
circle = NbrCircle(5, "CELL")

# The general format is: isinstance(AnyObject, AnyClass)
# In the following statement, val will be assigned True
val = isinstance(circle, NbrCircle) 

# In the following statement, val will be assigned False
val = isinstance(circle, NbrRectangle)
```

---

## Input data specification

## Code Samples

### Example 1

```python
# The full path and name of the dataset is used
outRas = Slope("C:/Data/elevation")

# If the layer is in the Contents or in your workspace,
#  then just the quoted name is needed
outRas2 = Slope("elevation")
```

### Example 2

```python
# The full path and name of the dataset is used
outRas = Slope("C:/Data/elevation")

# If the layer is in the Contents or in your workspace,
#  then just the quoted name is needed
outRas2 = Slope("elevation")
```

### Example 3

```python
# In the following statement Population is a field name
outRas2 = KernelDensity("inpoints", "Population")
```

### Example 4

```python
# In the following statement Population is a field name
outRas2 = KernelDensity("inpoints", "Population")
```

### Example 5

```python
inputElevation = "C:/Data/dem"
outRas = Slope(inputElevation)
```

### Example 6

```python
inputElevation = "C:/Data/dem"
outRas = Slope(inputElevation)
```

### Example 7

```python
outSource = ExtractByAttributes("inraster", "Value > 3000")

# The output of ExtractByAttributes is used as input to EucDistance
outDistance = EucDistance(outSource)
```

### Example 8

```python
outSource = ExtractByAttributes("inraster", "Value > 3000")

# The output of ExtractByAttributes is used as input to EucDistance
outDistance = EucDistance(outSource)
```

### Example 9

```python
# Buffer returns a Result object, which is used here as 
#   input to EucDistance
dist = EucDistance(arcpy.Select_analysis("schools", "#", "Pop>2000"))
```

### Example 10

```python
# Buffer returns a Result object, which is used here as 
#   input to EucDistance
dist = EucDistance(arcpy.Select_analysis("schools", "#", "Pop>2000"))
```

### Example 11

```python
outStats = CellStatistics(["inraster1", "inraster2", "inraster3"], "MEAN")
```

### Example 12

```python
outStats = CellStatistics(["inraster1", "inraster2", "inraster3"], "MEAN")
```

---

## Raster object interaction

## Code Samples

### Example 1

```python
>>> outRas = Slope("elevation")
>>> print outRas(isTemporary)
True
```

### Example 2

```python
>>> outRas = Slope("elevation")
>>> print outRas(isTemporary)
True
```

### Example 3

```python
>>> outRas = Raster("C:/Data/elevation")
>>> print outRas(isTemporary)
False
```

### Example 4

```python
>>> outRas = Raster("C:/Data/elevation")
>>> print outRas(isTemporary)
False
```

### Example 5

```python
outRas = Slope("inRas1") 
outRas = Aspect("inRas2")
```

### Example 6

```python
outRas = Slope("inRas1") 
outRas = Aspect("inRas2")
```

### Example 7

```python
outRas = Slope("C:/Data/elevation") 
del outRas
```

### Example 8

```python
outRas = Slope("C:/Data/elevation") 
del outRas
```

### Example 9

```python
outRas1 = Slope("elevation")

# Assigns Raster object to a new Raster object and save the raster dataset
outRas2 = outRas1
outRas2.save("C:/output/outslope")
```

### Example 10

```python
outRas1 = Slope("elevation")

# Assigns Raster object to a new Raster object and save the raster dataset
outRas2 = outRas1
outRas2.save("C:/output/outslope")
```

---

## Tool parameters in map algebra

## Code Samples

### Example 1

```python
# Usage: Slope(in_raster, {output_measurement}, {z_factor})

# DEGREE will be used as the default output measurement in the 
#  following statement
outRas = Slope("elevation", "DEGREE")
```

### Example 2

```python
# Usage: Slope(in_raster, {output_measurement}, {z_factor})

# DEGREE will be used as the default output measurement in the 
#  following statement
outRas = Slope("elevation", "DEGREE")
```

### Example 3

```python
# In the following statement, 4 is the zfactor parameter value
outRas = Slope("inraster", "DEGREE", 4)
```

### Example 4

```python
# In the following statement, 4 is the zfactor parameter value
outRas = Slope("inraster", "DEGREE", 4)
```

### Example 5

```python
outRas = FocalStatistics("inraster", NbrAnnulus(1, 3, "MAP"), "VARIETY")
```

### Example 6

```python
outRas = FocalStatistics("inraster", NbrAnnulus(1, 3, "MAP"), "VARIETY")
```

### Example 7

```python
# In the following statement the slope calculations will 
#  default to DEGREE; 4 is the z value
outRas = Slope("inraster", "", 4)
```

### Example 8

```python
# In the following statement the slope calculations will 
#  default to DEGREE; 4 is the z value
outRas = Slope("inraster", "", 4)
```

---

## Introduction to map algebra

## Code Samples

### Example 1

```python
from arcpy.sa import *
outRas = Slope("indem")
```

### Example 2

```python
from arcpy.sa import *
outRas = Slope("indem")
```

### Example 3

```python
from arcpy.ia import *
outRas = Slope("indem")
```

### Example 4

```python
from arcpy.ia import *
outRas = Slope("indem")
```

---

## Work with operators in map algebra

## Code Samples

### Example 1

```python
# outVar will be assigned 10
outVar = 3 + 7
```

### Example 2

```python
# outVar will be assigned 10
outVar = 3 + 7
```

### Example 3

```python
outRas = Raster("inraster1") + Raster("inraster2")
```

### Example 4

```python
outRas = Raster("inraster1") + Raster("inraster2")
```

### Example 5

```python
# In the following statement, 4 is added to each cell value in inraster1
outRas = Raster("inraster1") + 4
outRas2 = Raster("inraster") + math.pi
```

### Example 6

```python
# In the following statement, 4 is added to each cell value in inraster1
outRas = Raster("inraster1") + 4
outRas2 = Raster("inraster") + math.pi
```

### Example 7

```python
outRas = -Raster("inraster")
```

### Example 8

```python
outRas = -Raster("inraster")
```

### Example 9

```python
# In the following statement, 100 is added to each cell in 
# each slice of in_multidem_raster
out_multidem_raster = in_multidem_raster + 100
```

### Example 10

```python
# In the following statement, 100 is added to each cell in 
# each slice of in_multidem_raster
out_multidem_raster = in_multidem_raster + 100
```

### Example 11

```python
# In the following statement, the cell values from in_raster are added to 
# the cell values in each slice of in_multidem_raster.
out_multidem_raster = in_multidem_raster + in_raster
```

### Example 12

```python
# In the following statement, the cell values from in_raster are added to 
# the cell values in each slice of in_multidem_raster.
out_multidem_raster = in_multidem_raster + in_raster
```

### Example 13

```python
# In the following statement, the cell values in each slice from in_multidem_raster1
# are added to the cell values in each slice from in_multidem_raster2, only where variables and 
# dimensionality overlap.
out_multidem_raster = in_multidem_raster1 + in_multidem_raster2
```

### Example 14

```python
# In the following statement, the cell values in each slice from in_multidem_raster1
# are added to the cell values in each slice from in_multidem_raster2, only where variables and 
# dimensionality overlap.
out_multidem_raster = in_multidem_raster1 + in_multidem_raster2
```

---

## Work with Raster objects

## Code Samples

### Example 1

```python
rasObject = Raster("C:/Data/elevation")
```

### Example 2

```python
rasObject = Raster("C:/Data/elevation")
```

### Example 3

```python
# rasObject is a Raster object pointing to a temporary 
#   raster dataset
rasObject = Slope("C:/Data/elevation")
```

### Example 4

```python
# rasObject is a Raster object pointing to a temporary 
#   raster dataset
rasObject = Slope("C:/Data/elevation")
```

### Example 5

```python
outraster = Slope("C:/Data/elevation")
outraster.save("C:/output/sloperaster")
```

### Example 6

```python
outraster = Slope("C:/Data/elevation")
outraster.save("C:/output/sloperaster")
```

### Example 7

```python
outraster.save()
```

### Example 8

```python
outraster.save()
```

### Example 9

```python
outraster.save("C:/output/file_gdb.gdb/sloperaster")
outraster.save("C:/output/sloperaster.tif")
```

### Example 10

```python
outraster.save("C:/output/file_gdb.gdb/sloperaster")
outraster.save("C:/output/sloperaster.tif")
```

### Example 11

```python
from arcpy import env
from arcpy.sa import *
outraster = Raster("C:/Data/studyarea")
myextent = outraster.extent

# Modify myextent as necessary for your workflow and use it to set the extent environment
env.extent = myextent
```

### Example 12

```python
from arcpy import env
from arcpy.sa import *
outraster = Raster("C:/Data/studyarea")
myextent = outraster.extent

# Modify myextent as necessary for your workflow and use it to set the extent environment
env.extent = myextent
```

---

## Multidimensional raster types

## Code Samples

### Example 1

```python
153 is the code
CONVfract  is the variable name
The text after the variable name is the long name
7 is the data center
12 is the data subcenter
130 is the table version
```

### Example 2

```python
153 is the code
CONVfract  is the variable name
The text after the variable name is the long name
7 is the data center
12 is the data subcenter
130 is the table version
```

---

## Field names in Spatial Analyst

## Code Samples

### Example 1

```python
+   *   /   !   ^   %
(   )   [   ]   {   }
,   ~   '   "   :   ;
>   <   &   |   \   =
@   #   $
```

### Example 2

```python
AND      BEGIN    BREAK    BRK      CAND     COR      CXOR
DIFF     DIV      DO       DOCELL   EQ       ELSE     END
ENDIF    GE       GT       IF       IN       LE       LT
MAXOF    MINOF    MOD      NE       NOT      OFF      ON
OR       OVER     THEN     WHILE    XOR
```

---

## Output raster formats and names

## Code Samples

### Example 1

```python
' '  (space)            (   (open parenthesis)
 \   (backslash)        )   (close parenthesis)
 ,   (comma)            {   (open brace)
 ~   (tilde)            }   (close brace)
 '   (single quote)     [   (open bracket)
 "   (double quote)     ]   (close bracket)
```

---

## What is the Raster Cell Iterator?

## Code Samples

### Example 1

```python
from arcpy.sa import *
myRas = Raster("myras")
for i, j in myRas:
    print(i, j, myRas[i, j])
```

### Example 2

```python
from arcpy.sa import *
myRas = Raster("myras")
for i, j in myRas:
    print(i, j, myRas[i, j])
```

---
