# Spatial Analyst ArcPy Functions

*Consolidated from 156 individual documentation files*

---

## Anomaly

## Summary

Creates a raster object that contains the anomaly pixel values of the input multidimensional raster based on a time-dimension interval and the anomaly calculation method.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input multidimensional raster. | Raster |
| dimension_name | The dimension name which the anomaly definition will be performed along.(The default value is StdTime) | String |
| anomaly_type | Specifies the method used to calculate the anomaly.DIFFERENCE_FROM_MEAN—Calculates the difference between a pixel value and the mean of that pixel's values across slices defined by the interval. This is the default.PERCENT_DIFFERENCE_FROM_MEAN—Calculates the percent difference between a pixel value and the mean of that pixel's values across slices defined by the interval.PERCENT_OF_MEAN—Calculates the percent of the mean.(The default value is DIFFERENCE_FROM_MEAN) | String |
| temporal_interval | Specifies the temporal interval to use to calculate the average.None—Calculates the average across all slices for each pixel. This is the default.HOURLY—Calculates the hourly average for each pixel.DAILY—Calculates the daily average for each pixel.WEEKLY—Calculates the weekly average for each pixel.MONTHLY—Calculates the monthly average for each pixel.YEARLY—Calculates the yearly average for each pixel.(The default value is None) | String |
| ignore_nodata | Specifies whether NoData values are ignored in the analysis. True—The analysis will include all valid pixels along a given dimension and ignore any NoData pixels. This is the default.False—The analysis will result in NoData if there are any NoData values for the pixel along the given dimension.(The default value is True) | Boolean |

## Code Samples

### Example 1

```python
Anomaly (in_raster, {dimension_name}, {anomaly_type}, {temporal_interval}, {ignore_nodata})
```

### Example 2

```python
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
 
in_raster = Raster("C:/sapyexamples/data/ClimateData_Daily.nc", True)
 
# Choose the precipitation variable 
prcp_raster = Subset(in_raster, variables = 'prcp')
 
# Calculate percent of mean anomalies, 
# where the mean_value is the mean of all slices 
prcp_anomaly = Anomaly(prcp_raster, anomaly_type = 'PERCENT_OF_MEAN') 
 
# Calculate the difference from mean,
# where the mean_value is the mean of each year 
prcp_monthly_anomaly = Anomaly(prcp_raster, temporal_interval = 'YEARLY')
```

### Example 3

```python
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")
 
in_raster = Raster("C:/sapyexamples/data/ClimateData_Daily.nc", True)
 
# Choose the precipitation variable 
prcp_raster = Subset(in_raster, variables = 'prcp')
 
# Calculate percent of mean anomalies, 
# where the mean_value is the mean of all slices 
prcp_anomaly = Anomaly(prcp_raster, anomaly_type = 'PERCENT_OF_MEAN') 
 
# Calculate the difference from mean,
# where the mean_value is the mean of each year 
prcp_monthly_anomaly = Anomaly(prcp_raster, temporal_interval = 'YEARLY')
```

---

## Apply

## Summary

Creates a raster object by applying a raster function or function chain to one or more input rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster[in_raster,...] | The input raster dataset or datasets. The input can include the following: A single raster—For raster functions that require one raster input, and the raster function argument name for the raster input is Raster. For example, to apply the NDVI raster function to a raster object, the input would be raster_object.A collection of rasters in a tuple—For raster functions that require two or more raster inputs, and the raster function argument names for the raster inputs are Raster, Raster2, Raster3, etc. For example, to apply the Arithmetic raster function to perform a mathematical operation on two rasters, the input would be (raster_object_1,raster_object_2).An array of rasters in a list—For raster functions that require an array of raster inputs, and the raster function argument name for the inputs is Rasters. For example, to apply the Composite Bands raster function to combine three rasters into a single raster, the input would be [raster_object_1,raster_object_2,raster_object_3].A dictionary with names and rasters—For raster functions that require a set of names raster inputs. For example, to apply the Heat Index raster function to calculate apparent temperature, the input would be ['temperature': raster_object_1,'rh': raster_object_2]. | Raster |
| raster_function | The name of a raster function or the path to a custom raster function (.rft.xml file) to apply to the input. | String |
| raster_function_arguments | The parameters and values associated with the raster function or function chain. If not specified, and if applicable, default values will be used.For example, the Tasseled Cap raster function does not require any arguments; the input is a single raster, so there is no need to specify arguments.The Arithmetic raster function, however, requires 5 input parameters: Raster, Raster2, Operation, Cellsize Type and Extent Type. To use Arithmetic with the Apply function, Raster and Raster2 are defined in the in_raster parameter, and the remaining parameters have default values, so if nothing is specified for those parameters, the default values will be used.For information about the function arguments for each raster function, see Raster function objects. | Dictionary |

## Code Samples

### Example 1

```python
Apply (in_raster, raster_function, {raster_function_arguments})
```

### Example 2

```python
# Apply NDVI, Arithmetic, and Composite Bands functions to one or more raster datasets.

# Import system modules
import arcpy
from arcpy.sa import *
from arcpy import env

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set input raster for NDVI
Landsat = Raster("Landsat") 

# Apply NDVI raster function to a single raster
out_NDVI_raster = Apply(Landsat, "NDVI", {'VisibleBandID':4,'InfraredBandID':5})

# Set input rasters for Arithmetic
DEM = Raster("DEM.tif")
Buildings = Raster("BuildingHeights.tif") 

# Apply Arithmetic raster function to add building height to ground elevation
out_Arithmetic_raster = Apply((DEM, Buildings),'Arithmetic',{'operation':1})

# Set input rasters for Composite Bands
Band1 = Raster("blue.tif") 
Band2 = Raster("green.tif") 
Band3 = Raster("red.tif") 

# Apply Composite Bands function to combine three bands into a single raster
out_composite_rasters = Apply([Band1, Band2, Band3], 'CompositeBand')
```

### Example 3

```python
# Apply NDVI, Arithmetic, and Composite Bands functions to one or more raster datasets.

# Import system modules
import arcpy
from arcpy.sa import *
from arcpy import env

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set input raster for NDVI
Landsat = Raster("Landsat") 

# Apply NDVI raster function to a single raster
out_NDVI_raster = Apply(Landsat, "NDVI", {'VisibleBandID':4,'InfraredBandID':5})

# Set input rasters for Arithmetic
DEM = Raster("DEM.tif")
Buildings = Raster("BuildingHeights.tif") 

# Apply Arithmetic raster function to add building height to ground elevation
out_Arithmetic_raster = Apply((DEM, Buildings),'Arithmetic',{'operation':1})

# Set input rasters for Composite Bands
Band1 = Raster("blue.tif") 
Band2 = Raster("green.tif") 
Band3 = Raster("red.tif") 

# Apply Composite Bands function to combine three bands into a single raster
out_composite_rasters = Apply([Band1, Band2, Band3], 'CompositeBand')
```

### Example 4

```python
# Apply Heat Index function to multidimensional raster objects

# Import system modules
import arcpy
from arcpy.sa import *

# Set input multidimensional raster dataset
in_raster = Raster("C:/sapyexamples/data/ClimateData.nc", True)

# Select the relative humidity variable
RH = Subset(in_raster, variables = 'rh')

# Select the temperature variable
Temp = Subset(in_raster, variables = 't')

# Apply the Heat Index function to the two multidimensional raster subsets
# The output is a multidimensional raster where each slice is the heat index for the slice's time
heat_index_raster = Apply({'temperature': Temp, 'rh': RH}, 'HeatIndex', {'units':'Kelvin', 'outUnits':'Fahrenheit'})

# Save the output as crf
heat_index_raster = ("C:/sapyexamples/output/HeatIndexRaster.crf")
```

### Example 5

```python
# Apply Heat Index function to multidimensional raster objects

# Import system modules
import arcpy
from arcpy.sa import *

# Set input multidimensional raster dataset
in_raster = Raster("C:/sapyexamples/data/ClimateData.nc", True)

# Select the relative humidity variable
RH = Subset(in_raster, variables = 'rh')

# Select the temperature variable
Temp = Subset(in_raster, variables = 't')

# Apply the Heat Index function to the two multidimensional raster subsets
# The output is a multidimensional raster where each slice is the heat index for the slice's time
heat_index_raster = Apply({'temperature': Temp, 'rh': RH}, 'HeatIndex', {'units':'Kelvin', 'outUnits':'Fahrenheit'})

# Save the output as crf
heat_index_raster = ("C:/sapyexamples/output/HeatIndexRaster.crf")
```

---

## ApplyEnvironment

## Summary

Creates a new raster that is a copy of the input raster with the current environment settings being applied.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input raster dataset. | Raster |

## Code Samples

### Example 1

```python
ApplyEnvironment (in_raster)
```

### Example 2

```python
import arcpy
from arcpy import env

#convert raster form meter to feet
elevMeter = Raster('C:/data/dem10') * 0.3048
env.cellSize = '30'
env.mask = 'C:/data/studyarea'

#create a new clipped raster based on the cellsize and mask environment settings
elevRasterClip = ApplyEnvironment(elevMeter)
elevRasterClip.save("C:/output/fgdb.gdb/dem30_m")
```

### Example 3

```python
import arcpy
from arcpy import env

#convert raster form meter to feet
elevMeter = Raster('C:/data/dem10') * 0.3048
env.cellSize = '30'
env.mask = 'C:/data/studyarea'

#create a new clipped raster based on the cellsize and mask environment settings
elevRasterClip = ApplyEnvironment(elevMeter)
elevRasterClip.save("C:/output/fgdb.gdb/dem30_m")
```

---

## ArgStatistics

## Summary

Creates a raster object in which each pixel contains the band index at which that pixel reached the statistical argument. If the input raster is multidimensional, the output raster object will contain dimension values instead of band indices.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The input raster or list of rasters. | Raster |
| stat_type | Specifies the statistical argument to extract.MAX— The band index or dimension value at which the maximum pixel value is reached will be extracted.MIN— The band index or dimension value at which the minimum pixel value is reached will be extracted.MEDIAN— The band index or dimension value at which the median pixel value is reached will be extracted.DURATION— The longest dimension duration for which the pixel values fall between the minimum and maximum values.(The default value is None) | String |
| min_value | The minimum pixel value to be used to extract the duration. This argument is required when the stat_type argument is set to DURATION.(The default value is None) | Double |
| max_value | The maximum pixel value to be used to extract the duration. This argument is required when the stat_type argument is set to DURATION.(The default value is None) | Double |
| multiple_occurrence_value | The pixel value to use to indicate that a given argument statistic was reached more than once in the input raster dataset. This argument is required when the stat_type argument is set to MIN or MAX.(The default value is 100) | Integer |
| ignore_nodata | Specifies whether to ignore NoData values in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is True) | Boolean |

## Code Samples

### Example 1

```python
ArgStatistics (rasters, {stat_type}, {min_value}, {max_value}, {multiple_occurrence_value}, {ignore_nodata})
```

### Example 2

```python
import arcpy

argstat_raster = arcpy.sa.ArgStatistics("Temperature_30_years.crf", "MAX","","", 9999)
```

### Example 3

```python
import arcpy

argstat_raster = arcpy.sa.ArgStatistics("Temperature_30_years.crf", "MAX","","", 9999)
```

---

## / (Division) operator

## Summary

Divides the values of two rasters on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/sapyexamples/output/outdivide")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/sapyexamples/output/outdivide")
```

### Example 3

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/sapyexamples/output/outdivide2")
```

### Example 4

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/sapyexamples/output/outdivide2")
```

---

## // (Integer Division) operator

## Summary

Performs an integer divide on the values of two rasters on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outDivide = Raster("degs") // Raster("negs")
outDivide.save("C:/sapyexamples/output/outdivide")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outDivide = Raster("degs") // Raster("negs")
outDivide.save("C:/sapyexamples/output/outdivide")
```

### Example 3

```python
# Name: Op_IntegerDivide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Integer Divide
outDivide = inRaster01 // inRaster02

# Save the output 
outDivide.save("C:/sapyexamples/output/outdivide2")
```

### Example 4

```python
# Name: Op_IntegerDivide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Integer Divide
outDivide = inRaster01 // inRaster02

# Save the output 
outDivide.save("C:/sapyexamples/output/outdivide2")
```

---

## - (Subtract) operator

## Summary

Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outMinus = Raster("degs") - Raster("negs")
outMinus.save("C:/sapyexamples/output/outminus")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outMinus = Raster("degs") - Raster("negs")
outMinus.save("C:/sapyexamples/output/outminus")
```

### Example 3

```python
# Name: Op_Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Minus
outMinus = inRaster1 - inRaster2

# Save the output 
outMinus.save("C:/sapyexamples/output/outminus.tif")
```

### Example 4

```python
# Name: Op_Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Minus
outMinus = inRaster1 - inRaster2

# Save the output 
outMinus.save("C:/sapyexamples/output/outminus.tif")
```

---

## % (Modulo) operator

## Summary

Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outMod = Raster("degs") % Raster("negs")
outMod.save("C:/sapyexamples/output/outmod.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outMod = Raster("degs") % Raster("negs")
outMod.save("C:/sapyexamples/output/outmod.tif")
```

### Example 3

```python
# Name: Op_Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Mod
outMod = inRaster1 % inRaster2

# Save the output 
outMod.save("C:/sapyexamples/output/outmod")
```

### Example 4

```python
# Name: Op_Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Mod
outMod = inRaster1 % inRaster2

# Save the output 
outMod.save("C:/sapyexamples/output/outmod")
```

---

## - (Negate) operator

## Summary

Changes the sign of the cell values (multiplies by -1) of the input raster on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNegate = - Raster("degs")
outNegate.save("C:/sapyexamples/output/outneg")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNegate = - Raster("degs")
outNegate.save("C:/sapyexamples/output/outneg")
```

### Example 3

```python
# Name: Op_Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a cell-by-cell basis 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outNegate = -(inRaster)

# Save the output 
outNegate.save("C:/sapyexamples/output/outnegate")
```

### Example 4

```python
# Name: Op_Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a cell-by-cell basis 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outNegate = -(inRaster)

# Save the output 
outNegate.save("C:/sapyexamples/output/outnegate")
```

---

## + (Addition) operator

## Summary

Adds (sums) the values of two rasters on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outPlus = Raster("degs") + Raster("negs")
outPlus.save("C:/sapyexamples/output/outplus.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outPlus = Raster("degs") + Raster("negs")
outPlus.save("C:/sapyexamples/output/outplus.img")
```

### Example 3

```python
# Name: Op_Plus_Ex_02.py
# Description: Adds the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("cost")
inRaster2 = Raster("degs")

# Execute Plus
outPlus = inRaster1 + inRaster2

# Save the output 
outPlus.save("C:/sapyexamples/output/outplus")
```

### Example 4

```python
# Name: Op_Plus_Ex_02.py
# Description: Adds the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("cost")
inRaster2 = Raster("degs")

# Execute Plus
outPlus = inRaster1 + inRaster2

# Save the output 
outPlus.save("C:/sapyexamples/output/outplus")
```

---

## ** (Power) operator

## Summary

Raises the cell values in a raster to the power of the values found in another raster.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outPower = Raster("degs") ** Raster("cost")
outPower.save("C:/sapyexamples/output/outpower.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outPower = Raster("degs") ** Raster("cost")
outPower.save("C:/sapyexamples/output/outpower.img")
```

### Example 3

```python
# Name: Op_Power_Ex_02.py
# Description: Raises the cells in a raster to the power of the values
#              found in another raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("cost")

# Execute Power
outPower = inRaster1 ** inRaster2

# Save the output 
outPower.save("C:/sapyexamples/output/outpower")
```

### Example 4

```python
# Name: Op_Power_Ex_02.py
# Description: Raises the cells in a raster to the power of the values
#              found in another raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("cost")

# Execute Power
outPower = inRaster1 ** inRaster2

# Save the output 
outPower.save("C:/sapyexamples/output/outpower")
```

---

## * (Multiplication) operator

## Summary

Multiplies the values of two rasters on a cell-by-cell basis.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outTimes = Raster("elevation") * 0.3048
outTimes.save("C:/sapyexamples/output/outtimes")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outTimes = Raster("elevation") * 0.3048
outTimes.save("C:/sapyexamples/output/outtimes")
```

### Example 3

```python
# Name: Op_Times_Ex_02.py
# Description: Multiplies the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("elevation")
inConstant = 0.3048

# Execute Times
outTimes = inRaster * inConstant

# Save the output 
outTimes.save("C:/sapyexamples/output/timesout")
```

### Example 4

```python
# Name: Op_Times_Ex_02.py
# Description: Multiplies the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("elevation")
inConstant = 0.3048

# Execute Times
outTimes = inRaster * inConstant

# Save the output 
outTimes.save("C:/sapyexamples/output/timesout")
```

---

## + (Unary Plus) operator

## Summary

Multiplies each cell value of the input raster on a cell-by-cell basis by 1.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outUnaryPlus = + Raster("degs")
outUnaryPlus.save("C:/sapyexamples/output/outdeg")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outUnaryPlus = + Raster("degs")
outUnaryPlus.save("C:/sapyexamples/output/outdeg")
```

### Example 3

```python
# Name: Op_UnaryPlus_Ex_02.py
# Description: Returns the cell valuesof the input raster on a cell-by-cell 
#    basis. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outUnaryPlus = +(inRaster)

# Save the output 
outUnaryPlus.save("C:/sapyexamples/output/outunplus")
```

### Example 4

```python
# Name: Op_UnaryPlus_Ex_02.py
# Description: Returns the cell valuesof the input raster on a cell-by-cell 
#    basis. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outUnaryPlus = +(inRaster)

# Save the output 
outUnaryPlus.save("C:/sapyexamples/output/outunplus")
```

---

## Arithmetic

## Summary

Performs an arithmetic operation between two rasters or between a raster and a scalar and returns a raster object with the operation applied.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster1 | The first input raster. This can be a scalar raster where all pixels have the same value. | Raster |
| raster2 | The second input raster. This can be a scalar raster where all pixels have the same value. | Raster |
| operation_type | The arithmetic operation to apply between the two input rasters.Divide—Outputs the divisible result between the corresponding pixel values for each raster.Minus—Outputs the difference between the corresponding pixel values for each raster. This operation can be used to calculate change detection.Mode—Outputs the pixel value of all overlapping pixels that occurs the most. For example, if there are six bands in a raster, there will be six overlapping pixels. For the values 4, 5, 6, 4, 7, 9, the mode value is 4.Multiply—Outputs the product of the corresponding pixel values for each raster. This operation can be used to perform some cost functions.Plus—Outputs the sum of all the corresponding pixel values for each raster.Power—Outputs the product of the corresponding pixel values raised to the power of the input raster or scalar.(The default value is Plus) | String |
| extent_type | The method to use to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent is defined using the extent of the first input raster.LastOf—The output extent is defined using the extent of the last input raster.IntersectionOf—The output extent is defined as the intersecting area of the input rasters.UnionOf—The output extent is defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method to use to compute the cell size of the output when the input rasters have different cell sizes. FirstOf—The output cell size is defined using the cell size of the first input raster.LastOf—The output cell size is defined using the cell size of the last input raster.MaxOf—The output cell size is defined using the maximum cell size of the input rasters.MeanOf—The output cell size is defined using the mean of both input rasters.MinOf—The output cell size is defined using the minimum cell size of the input rasters.(The default value is FirstOf) | String |

## Code Samples

### Example 1

```python
Arithmetic (raster1, raster2, {operation_type}, {extent_type}, {cellsize_type})
```

### Example 2

```python
import arcpy

new_raster = arcpy.sa.Arithmetic("Raster1.tif","Raster2.tif", "Multiply", "UnionOf", "FirstOf")
```

### Example 3

```python
import arcpy

new_raster = arcpy.sa.Arithmetic("Raster1.tif","Raster2.tif", "Multiply", "UnionOf", "FirstOf")
```

---

## AspectSlope

## Summary

Creates a raster object that simultaneously displays the aspect and slope of a surface.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input elevation raster. | Raster |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |

## Code Samples

### Example 1

```python
AspectSlope (raster, {z_factor})
```

### Example 2

```python
from arcpy.sa import *
out_aspectslope_raster = AspectSlope("elevation.tif", 3)
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

### Example 3

```python
from arcpy.sa import *
out_aspectslope_raster = AspectSlope("elevation.tif", 3)
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "elevation.tif"

# Execute the AspectSlope function
out_aspectslope_raster = AspectSlope(in_raster, 3)

# Save the output
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

### Example 5

```python
# Import the system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "elevation.tif"

# Execute the AspectSlope function
out_aspectslope_raster = AspectSlope(in_raster, 3)

# Save the output
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

---

## BAI

## Summary

Calculates the Burn Area Index (BAI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |

## Code Samples

### Example 1

```python
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 2

```python
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 3

```python
BAI (raster, {red_band_id}, {nir_band_id})
```

### Example 4

```python
from arcpy.sa import *
out_bai_raster = BAI("landsat8.tif", 3, 4)
out_bai_raster.save("C:/arcpyExamples/outputs/BAI.tif")
```

### Example 5

```python
from arcpy.sa import *
out_bai_raster = BAI("landsat8.tif", 3, 4)
out_bai_raster.save("C:/arcpyExamples/outputs/BAI.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute BAI function
out_bai_raster = BAI(in_raster, 3, 4)

# Save the output
out_bai_raster.save("C:/arcpyExamples/outputs/BAI.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute BAI function
out_bai_raster = BAI(in_raster, 3, 4)

# Save the output
out_bai_raster.save("C:/arcpyExamples/outputs/BAI.tif")
```

---

## BandArithmetic

## Summary

Performs an arithmetic operation on the bands of a multiband raster object and returns a raster object with the operation applied.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| band_ids | The band IDs to use in the arithmetic operation, separated by a space. Band IDs are indexed using one-based indexing, so that the first band in a list of bands in a multiband raster object has an index of 1.The bands should be provided in the order that is required by the arithmetic method. For information about the order of bands needed for each method, see Band Arithmetic. | String |
| method | The arithmetic operation to apply to the bands.A custom operation can also be defined.1— NDVI2—SAVI3— TSAVI4—MSAVI5—GEMI6—PVI7—GVITM8—Sultan9—VARI10—GNDVI11—SR12—NDVIre13—SRre14—MTVI215—RTVICore16—CIre17—CIg18—NDWI19—EVI20—Iron oxide21—Ferrous minerals22—Clay minerals23—WNDWI(The default value is 1) | Integer |

## Code Samples

### Example 1

```python
BandArithmetic (raster, band_ids, {method})
```

### Example 2

```python
import arcpy

SimpleRatio = arcpy.sa.BandArithmetic("Landsat8.tif","5 4", 11)
```

### Example 3

```python
import arcpy

SimpleRatio = arcpy.sa.BandArithmetic("Landsat8.tif","5 4", 11)
```

### Example 4

```python
import arcpy

BandAddition_raster = arcpy.sa.BandArithmetic("Landsat8.tif","B2+B3", 0)
```

### Example 5

```python
import arcpy

BandAddition_raster = arcpy.sa.BandArithmetic("Landsat8.tif","B2+B3", 0)
```

---

## << (Bitwise Left Shift) operator

## Summary

Performs a Bitwise Left Shift operation on the binary values of two input rasters.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBitwiseLS = Raster("degs") << Raster("negs")
outBitwiseLS.save("C:/sapyexamples/output/outbitls.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBitwiseLS = Raster("degs") << Raster("negs")
outBitwiseLS.save("C:/sapyexamples/output/outbitls.tif")
```

### Example 3

```python
# Name: Op_BitwiseLeftShift_Ex_02.py
# Description: Performs a Bitwise Left Shift operation on the binary
#     values of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseLeftShift
outBitwiseLShift = inRaster1 << inRaster2

# Save the output 
outBitwiseLShift.save("C:/sapyexamples/output/outlshift")
```

### Example 4

```python
# Name: Op_BitwiseLeftShift_Ex_02.py
# Description: Performs a Bitwise Left Shift operation on the binary
#     values of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseLeftShift
outBitwiseLShift = inRaster1 << inRaster2

# Save the output 
outBitwiseLShift.save("C:/sapyexamples/output/outlshift")
```

---

## >> (Bitwise Right Shift) operator

## Summary

Performs a Bitwise Right Shift operation on the binary values of two input rasters.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBitwiseRShift = Raster("degs") >> Raster("negs")
outBitwiseRShift.save("C:/sapyexamples/output/outbitrs")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBitwiseRShift = Raster("degs") >> Raster("negs")
outBitwiseRShift.save("C:/sapyexamples/output/outbitrs")
```

### Example 3

```python
# Name: Op_BitwiseRightShift_Ex_02.py
# Description: Performs a Bitwise Right Shift operation on the binary
#              values of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseRightShift
outBitwiseRShift = inRaster1 >> inRaster2

# Save the output 
outBitwiseRShift.save("C:/sapyexamples/output/outbitrshift.img")
```

### Example 4

```python
# Name: Op_BitwiseRightShift_Ex_02.py
# Description: Performs a Bitwise Right Shift operation on the binary
#              values of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseRightShift
outBitwiseRShift = inRaster1 >> inRaster2

# Save the output 
outBitwiseRShift.save("C:/sapyexamples/output/outbitrshift.img")
```

---

## & (Boolean And) operator

## Summary

Performs a Boolean And operation on the cell values of two input rasters.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanAnd = Raster("degs") & Raster("negs")
outBooleanAnd.save("C:/sapyexamples/output/outbooland.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanAnd = Raster("degs") & Raster("negs")
outBooleanAnd.save("C:/sapyexamples/output/outbooland.img")
```

### Example 3

```python
# Name: Op_BooleanAnd_Ex_02.py
# Description: Performs a Boolean And operation on the cell values
#              of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanAnd
outBooleanAnd = inRaster1 & inRaster2

# Save the output 
outBooleanAnd.save("C:/sapyexamples/output/outbooland")
```

### Example 4

```python
# Name: Op_BooleanAnd_Ex_02.py
# Description: Performs a Boolean And operation on the cell values
#              of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanAnd
outBooleanAnd = inRaster1 & inRaster2

# Save the output 
outBooleanAnd.save("C:/sapyexamples/output/outbooland")
```

---

## ~ (Boolean Not) operator

## Summary

Performs a Boolean-complement (Not) operation on the cell values of the input raster.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanNot = ~ Raster("degs")
outBooleanNot.save("C:/sapyexamples/output/outboolnot.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanNot = ~ Raster("degs")
outBooleanNot.save("C:/sapyexamples/output/outboolnot.tif")
```

### Example 3

```python
# Name: Op_BooleanNot_Ex_02.py
# Description: Performs a Boolean complement (NOT) operation on the
#              cell values of an input raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute BooleanNot
outBooleanNot = ~ inRaster

# Save the output 
outBooleanNot.save("C:/sapyexamples/output/outboolnot")
```

### Example 4

```python
# Name: Op_BooleanNot_Ex_02.py
# Description: Performs a Boolean complement (NOT) operation on the
#              cell values of an input raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute BooleanNot
outBooleanNot = ~ inRaster

# Save the output 
outBooleanNot.save("C:/sapyexamples/output/outboolnot")
```

---

## | (Boolean Or) operator

## Summary

Performs a Boolean Or operation on the cell values of two input rasters.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanOr = Raster("degs") | Raster("negs")
outBooleanOr.save("C:/sapyexamples/output/outboolor2")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanOr = Raster("degs") | Raster("negs")
outBooleanOr.save("C:/sapyexamples/output/outboolor2")
```

### Example 3

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/sapyexamples/output/outboolor")
```

### Example 4

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/sapyexamples/output/outboolor")
```

---

## ^ (Boolean XOr) operator

## Summary

Performs a Boolean Exclusive Or operation on the cell values of two input rasters.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanXOr = Raster("degs") ^ Raster("negs")
outBooleanXOr.save("C:/sapyexamples/output/outboolxor.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outBooleanXOr = Raster("degs") ^ Raster("negs")
outBooleanXOr.save("C:/sapyexamples/output/outboolxor.tif")
```

### Example 3

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/sapyexamples/output/outboolor")
```

### Example 4

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/sapyexamples/output/outboolor")
```

---

## CIg

## Summary

Calculates the Green Chlorophyll Index (CIg) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
CIg = (NIR / Green)-1
```

### Example 2

```python
CIg = (NIR / Green)-1
```

### Example 3

```python
CIg (raster, {nir_band_id}, {green_band_id})
```

### Example 4

```python
import arcpy

CIg_raster = arcpy.sa.CIg("Landsat8.tif", 5, 3)
```

### Example 5

```python
import arcpy

CIg_raster = arcpy.sa.CIg("Landsat8.tif", 5, 3)
```

---

## CIre

## Summary

Calculates the Red-Edge Chlorophyll Index (CIre) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| redEdge_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
Clre = ((NIR / RedEdge) - 1)
```

### Example 2

```python
Clre = ((NIR / RedEdge) - 1)
```

### Example 3

```python
CIre (raster, {nir_band_id}, {redEdge_band_id})
```

### Example 4

```python
import arcpy

CIre_raster = arcpy.sa.CIre("Sentinel2.tif", 8, 5)
```

### Example 5

```python
import arcpy

CIre_raster = arcpy.sa.CIre("Sentinel2.tif", 8, 5)
```

---

## Classify

## Summary

Classifies a raster dataset based on an Esriclassifier definition file (.ecd) and raster dataset inputs.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster1 | The input raster to be classified. | Raster |
| raster2 | An optional raster dataset to incorporate into the classifier, such as a segmented image, multispectral image, or elevation data, used to generate a more robust classification definition for your dataset.The raster dataset for this parameter must match the one used to create the input Esri Classifier Definition file. | Raster |
| classifier_definition | The path to the Esri Classifier Definition file (.ecd) that contains the statistics and other classification information for the specific dataset, classifier, and chosen attributes.(The default value is None) | String |

## Code Samples

### Example 1

```python
Classify (raster1, {raster2}, classifier_definition)
```

### Example 2

```python
from arcpy.sa import *
out_classify_raster = Classify("NAIP.tif",None,
                               "C:/arcpyExamples/data/vegetation_class.ecd")
out_classify_raster.save("C:/arcpyexamples/outputs/classify_output.tif")
```

### Example 3

```python
from arcpy.sa import *
out_classify_raster = Classify("NAIP.tif",None,
                               "C:/arcpyExamples/data/vegetation_class.ecd")
out_classify_raster.save("C:/arcpyexamples/outputs/classify_output.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster1 = "QuickBird_4bands.tif"
raster2 = None
classifier_definition = "C:/arcpyExamples/data/tree_crown_classification_training_2classes_4b16b_ntree50.ecd"


# Apply Classify function
classified_raster = Classify(raster1, raster2, classifier_definition)

# Save the output
classified_raster.save("C:/arcpyExamples/outputs/Vegetation_landcover.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster1 = "QuickBird_4bands.tif"
raster2 = None
classifier_definition = "C:/arcpyExamples/data/tree_crown_classification_training_2classes_4b16b_ntree50.ecd"


# Apply Classify function
classified_raster = Classify(raster1, raster2, classifier_definition)

# Save the output
classified_raster.save("C:/arcpyExamples/outputs/Vegetation_landcover.crf")
```

---

## ClayMinerals

## Summary

Calculates the Clay Minerals (CM) ratio from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| swir1_band_id | The band ID of the shortwave infrared 1 (SWIR1) band.The band ID index uses one-based indexing.(The default value is 6) | Integer |
| swir2_band_id | The band ID of the shortwave infrared 2 (SWIR2) band.The band ID index uses one-based indexing.(The default value is 7) | Integer |

## Code Samples

### Example 1

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 2

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 3

```python
ClayMinerals (raster, {swir1_band_id}, {swir2_band_id})
```

### Example 4

```python
import arcpy

ClayMinerals_raster = arcpy.sa.ClayMinerals("Sentinel2.tif", 11, 12)
```

### Example 5

```python
import arcpy

ClayMinerals_raster = arcpy.sa.ClayMinerals("Sentinel2.tif", 11, 12)
```

---

## ColormapToRGB

## Summary

Converts a single-band raster with a color map to a three-band (red, green, and blue) raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input color map raster. | Raster |

## Code Samples

### Example 1

```python
ColormapToRGB (raster)
```

### Example 2

```python
from arcpy.sa import *
out_slope_with_colormap = ColormapToRGB("elevation_raster.tif")
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/elevtion_rgb_3bands.tif")
```

### Example 3

```python
from arcpy.sa import *
out_slope_with_colormap = ColormapToRGB("elevation_raster.tif")
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/elevtion_rgb_3bands.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "slope_raster.tif"

# convert the raster with colormap to a RGB 3bands raster
out_slope_rgb_3bands = ColormapToRGB(in_raster)

# save the output
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/slope_rgb_3bands.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "slope_raster.tif"

# convert the raster with colormap to a RGB 3bands raster
out_slope_rgb_3bands = ColormapToRGB(in_raster)

# save the output
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/slope_rgb_3bands.tif")
```

---

## Colormap

## Summary

Transforms the pixel values to display the raster data as either a grayscale or an RGB color image based on a color scheme or specific colors in a color map file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| Colormap | The following default color maps are available:None—No color map. This is the default.Elevation—A color map that gradually changes from cyan to purple to black.Gray—A color map that gradually changes from black to white.NDVI—A color map to visualize vegetation. Values near zero are blue. Low values are brown. Then the colors gradually change from red, to orange, to yellow, to green, and to black as the vegetation index goes from low to high.NDVI2—A color map to visualize vegetation. Low values range from white to green. Then the colors range from gray, to purple, to violet, to dark blue, and to black as the vegetation index goes from low to high. NDVI3—A color map to visualize vegetation. Values near zero are blue. Then the colors gradually change from red, to orange, and to green as the vegetation index goes from low to high.Random—A random color map.(The default value is None) | String |
| Color Ramp | Choose a pre-existing color ramp or create your own color scheme.Can be a string specifying color ramp name such as Black To White, Yellow To Red, Slope, or other color ramp names supported in ArcGIS ProFor more information about color ramp objects, see Color ramp objects.(The default value is None) | String |

## Code Samples

### Example 1

```python
Colormap (raster, {Colormap}, {Color Ramp})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the local variables
raster = "C:/arcpyExamples/data/land_cover.tif"
# pixels with value = 1 will be red, pixels with value = 2 will be green, pixels
# with value = 3 will be blue 
customized_colormap = {"values": [1, 2, 3], "colors": ['red','green','blue']}
#or customized_colormap = [[1, 255, 0, 0], [2, 0, 255, 0], [3, 0, 0, 255]]
# it is same with the one above

# Execute Colormap function
out_land_cover_with_colormap = Colormap(raster, colormap = customized_colormap)

# Display in notebook
out_land_cover_with_colormap
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the local variables
raster = "C:/arcpyExamples/data/land_cover.tif"
# pixels with value = 1 will be red, pixels with value = 2 will be green, pixels
# with value = 3 will be blue 
customized_colormap = {"values": [1, 2, 3], "colors": ['red','green','blue']}
#or customized_colormap = [[1, 255, 0, 0], [2, 0, 255, 0], [3, 0, 0, 255]]
# it is same with the one above

# Execute Colormap function
out_land_cover_with_colormap = Colormap(raster, colormap = customized_colormap)

# Display in notebook
out_land_cover_with_colormap
```

---

## ColorspaceConversion

## Summary

Converts the color model of a three-band unsigned 8-bit image from the hue, saturation, and value (HSV) to red, green, and blue (RGB) or vice versa.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | An unsigned 8-bit pixel type input raster. | Raster |
| conversion_type | The color conversion type to perform.rgb_to_hsv—RGB to HSVhsv_to_rgb—HSV to RGB(The default value is rgb_to_hsv) | String |

## Code Samples

### Example 1

```python
ColorspaceConversion (raster, {conversion_type})
```

### Example 2

```python
from arcpy.sa import *
out_hsv_3bands = ColorspaceConversion("slope_rgb_3bands.tif", "rgb_to_hsv")
out_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

### Example 3

```python
from arcpy.sa import *
out_hsv_3bands = ColorspaceConversion("slope_rgb_3bands.tif", "rgb_to_hsv")
out_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
# the pixeltype of the input raster must be unsigned 8-bit, otherwise,
# the function would fail
in_raster = "slope_rgb_3bands.tif"

# Execute ColorspaceConversion function
slope_hsv_3bands = ColorspaceConversion(in_raster, "rgb_to_hsv")

# Save the output
slope_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
# the pixeltype of the input raster must be unsigned 8-bit, otherwise,
# the function would fail
in_raster = "slope_rgb_3bands.tif"

# Execute ColorspaceConversion function
slope_hsv_3bands = ColorspaceConversion(in_raster, "rgb_to_hsv")

# Save the output
slope_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

---

## Complex

## Summary

Computes the magnitude from complex values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |

## Code Samples

### Example 1

```python
Complex (raster)
```

### Example 2

```python
from arcpy.sa import *
out_magnitude_raster = Complex("itemgrd")
out_magnitude_raster.save("C:/arcpyexamples/outputs/out_magnitude_radar.crf")
```

### Example 3

```python
from arcpy.sa import *
out_magnitude_raster = Complex("itemgrd")
out_magnitude_raster.save("C:/arcpyexamples/outputs/out_magnitude_radar.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "Radar_stage4"

# Execute Complex function
out_magnitude_raster = Complex(in_raster)

# Save output
out_magnitude_raster.save("C:/arcpyExamples/outputs/out_magnitude_radar.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "Radar_stage4"

# Execute Complex function
out_magnitude_raster = Complex(in_raster)

# Save output
out_magnitude_raster.save("C:/arcpyExamples/outputs/out_magnitude_radar.crf")
```

---

## CompositeBand

## Summary

Creates a raster object by combining multiple rasters to form a multiband image.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster[raster,...] | The input raster or list of rasters. | Raster |

## Code Samples

### Example 1

```python
CompositeBand (raster)
```

### Example 2

```python
import arcpy

compband_raster = arcpy.sa.CompositeBand(["Band1.TIF", "Band2.TIF", "Band3.TIF"])
```

### Example 3

```python
import arcpy

compband_raster = arcpy.sa.CompositeBand(["Band1.TIF", "Band2.TIF", "Band3.TIF"])
```

---

## ContrastBrightness

## Summary

Creates an enhanced image by improving the contrast and brightness of the source image.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| contrast_offset | Specify the contrast offset value. Value can range from -100 through 100.(The default value is 0) | Double |
| brightness_offset | Specify the contrast offset value. Value can range from -100 through 100. (The default value is 0) | Double |

## Code Samples

### Example 1

```python
ContrastBrightness (raster, {contrast_offset}, {brightness_offset})
```

### Example 2

```python
import arcpy

ContrastBrightness_raster = arcpy.sa.ContrastBrightness(in_raster1, -50, 100)
```

### Example 3

```python
import arcpy

ContrastBrightness_raster = arcpy.sa.ContrastBrightness(in_raster1, -50, 100)
```

---

## Convolution

## Summary

Performs filtering on the pixel values in an image, which can be used for sharpening an image, blurring an image, detecting edges within an image, or other kernel-based enhancements.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| kernel[kernel,...] | Specify the filtering method.0—Enhance an image with a LINE_DETECTION_HORIZONTAL filter.1—Enhance an image with a Line Detection Vertical filter.2—Enhance an image with a Line Detection Left Diagonal filter.3—Enhance an image with a Line Detection Right Diagonal filter.4—Enhance an image with a Gradient North filter.5— Enhance an image with a Gradient West filter.6— Enhance an image with a Gradient East filter.7—Enhance an image with a Gradient South filter.8— Enhance an image with a Gradient Northeast filter.9— Enhance an image with a Gradient Northwest filter.10— Enhance an image with a Smooth Arithmetic Mean filter.11— Enhance an image with a Smoothing_3X3 filter.12—Enhance an image with a Smoothing_5X5 filter.13— Enhance an image with a Sharpening_3X3 filter.14— Enhance an image with a Sharpening_5X5 filter.15—Enhance an image with a Laplacian_3X3 filter.16—Enhance an image with a Laplacian_5X5 filter.17— Enhance an image with a Sobel Horizontal filter.18—Enhance an image with a Sobel Vertical filter.19—Enhance an image with a Sharpen filter.20—Enhance an image with a Sharpen2 filter.21—Enhance an image with a Point Spread filter.(The default value is None) | String |

## Code Samples

### Example 1

```python
Convolution (raster, kernel)
```

### Example 2

```python
import arcpy

Convolution_raster = arcpy.sa.Convolution(imagePath1, 15)
```

### Example 3

```python
import arcpy

Convolution_raster = arcpy.sa.Convolution(imagePath1, 15)
```

---

## ElevationVoidFill

## Summary

Creates pixels on a raster object where holes exist in the elevation.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input elevation raster. | Raster |
| max_void_width | The maximum void width value is used to specify the largest size of a void to be filled. If the width or height of the bounding box around the void is larger than the maximum void width value, the void is not filled. The units of this parameter are the same as the units used in the data's spatial reference system.If this parameter is blank or has a value of 0, no maximum width will be used, and all voids will be filled. A value of -1 means that no void filling will occur.(The default value is 0) | Integer |

## Code Samples

### Example 1

```python
ElevationVoidFill (raster, max_void_width)
```

### Example 2

```python
from arcpy.sa import *
out_evf_raster = ElevationVoidFill("elevation.tif", 0)
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

### Example 3

```python
from arcpy.sa import *
out_evf_raster = ElevationVoidFill("elevation.tif", 0)
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Define input parameters
in_raster = "elevation.tif"
max_void_width = 0

# Execute the ElevationVoidFill function
out_evf_raster = ElevationVoidFill(in_raster, max_void_width)

# Save output
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Define input parameters
in_raster = "elevation.tif"
max_void_width = 0

# Execute the ElevationVoidFill function
out_evf_raster = ElevationVoidFill(in_raster, max_void_width)

# Save output
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

---

## EVI

## Summary

Calculates the Enhanced Vegetation Index (EVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| blue_band_id | The band ID of the blue band. The ID index uses one-based indexing.(The default value is 2) | Integer |

## Code Samples

### Example 1

```python
EVI = 2.5*(NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
```

### Example 2

```python
EVI = 2.5*(NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
```

### Example 3

```python
EVI (raster, {nir_band_id}, {red_band_id}, {blue_band_id})
```

### Example 4

```python
import arcpy

EVI_raster = arcpy.sa.EVI("Landsat8.tif", 5, 4, 2)
```

### Example 5

```python
import arcpy

EVI_raster = arcpy.sa.EVI("Landsat8.tif", 5, 4, 2)
```

---

## ExtractBand

## Summary

Creates a raster object by extracting one or more bands from, or reordering the bands in, a multiband raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| band_ids[band_ids,...] | Extracts bands using the band ID.(The default value is None) | Integer |
| band_names[band_names,...] | Extracts bands using the name of the bands.(The default value is None) | String |
| band_wavelengths[band_wavelengths,...] | Extracts bands using the band wavelengths.(The default value is None) | Double |
| missing_band_action | Specifies the action that will occur when a band within the extract band list is not available.BestMatch—This option will try to find the best available band to use in place of the missing one, so that the function will not fail.Fail—Any mosaic dataset item that is missing a specified band will fail, since the extract band was invalid.(The default value is BestMatch) | Integer |
| wavelength_match_tolerance | Specifies the margin of error when extracting bands using the band_wavelengths method.(The default value is None) | Double |

## Code Samples

### Example 1

```python
ExtractBand (raster, {band_ids}, {band_names}, {band_wavelengths}, {missing_band_action}, {wavelength_match_tolerance})
```

### Example 2

```python
import arcpy

out_bands_raster = arcpy.sa.ExtractBand("in_raster.tif", [1, 2])
```

### Example 3

```python
import arcpy

out_bands_raster = arcpy.sa.ExtractBand("in_raster.tif", [1, 2])
```

### Example 4

```python
import arcpy

out_bands_raster = arcpy.sa.ExtractBand("in_raster.tif", band_wavelengths=[500.00])
```

### Example 5

```python
import arcpy

out_bands_raster = arcpy.sa.ExtractBand("in_raster.tif", band_wavelengths=[500.00])
```

---

## FerrousMinerals

## Summary

Calculates the Ferrous Minerals (FM) ratio from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| swir_band_id | The band ID of the shortwave infrared (SWIR) band.The band ID index uses one-based indexing.(The default value is 6) | Integer |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |

## Code Samples

### Example 1

```python
Ferrous Minerals Ratio = SWIR / NIR
```

### Example 2

```python
Ferrous Minerals Ratio = SWIR / NIR
```

### Example 3

```python
FerrousMinerals (raster, {swir_band_id}, {nir_band_id})
```

### Example 4

```python
import arcpy

FerrousMinerals_raster = arcpy.sa.FerrousMinerals("Sentinel2.tif", 11, 8)
```

### Example 5

```python
import arcpy

FerrousMinerals_raster = arcpy.sa.FerrousMinerals("Sentinel2.tif", 11, 8)
```

---

## Foreach

## Summary

Creates a raster object by applying a raster function or a customized function template to every slice in the input multidimensional raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input multidimensional raster dataset. | Raster |
| raster_function | The name of a raster function or the path to a custom raster function (.rft.xml file) to apply to every slice in the input multidimensional raster. | String |
| raster_function_arguments | The parameters and values associated with the raster function or function chain. If not specified, default values will be used.For example, the Tasseled Cap raster function does not require any arguments; the input is a single raster, so there is no need to specify arguments.The Arithmetic raster function, however, requires 5 input parameters: Raster, Raster2, Operation, Cellsize Type and Extent Type. To use Arithmetic with the Apply function, Raster and Raster2 are defined in the in_raster parameter, and the remaining parameters have default values, so if nothing is specified for those parameters, the default values will be used.For information about the function arguments for each raster function, see Raster function objects. | Dictionary |

## Code Samples

### Example 1

```python
Foreach (in_raster, raster_function, {raster_function_arguments})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create multidimensional raster object from 
# Landsat7 time series data in a mosaic dataset
in_raster = Raster("Landsat7", True)

# Calculate NDVI for each scene in the time series
out_NDVI_raster = Foreach(
	in_raster, "NDVI", {'VisibleBandID':3,'InfraredBandID':4})
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create multidimensional raster object from 
# Landsat7 time series data in a mosaic dataset
in_raster = Raster("Landsat7", True)

# Calculate NDVI for each scene in the time series
out_NDVI_raster = Foreach(
	in_raster, "NDVI", {'VisibleBandID':3,'InfraredBandID':4})
```

---

## FuzzyGaussian

## Summary

Defines a fuzzy membership function through a Gaussian or normal distribution based around a user-specified midpoint (which is assigned a membership of 1) with a defined spread decreasing to zero.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value with a fuzzy membership of 1.The default is the midpoint of the range of values of the input raster. | Double |
| spread | Defines the spread of the Gaussian function. The spread generally ranges from 0.01 to 1, with the larger the value results in a steeper distribution around the midpoint.(The default value is 0.1) | Double |

## Code Samples

### Example 1

```python
FuzzyGaussian (midpoint, spread)
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyGaussian(12, 0.1))
outFzyMember.save("c:/sapyexamples/fzymemb")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyGaussian(12, 0.1))
outFzyMember.save("c:/sapyexamples/fzymemb")
```

### Example 4

```python
# Name: FuzzyGaussian_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyGaussian algorithm object
midpoint = 10
spread = 0.2
myFuzzyAlgorithm = FuzzyGaussian(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzygauss")
```

### Example 5

```python
# Name: FuzzyGaussian_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyGaussian algorithm object
midpoint = 10
spread = 0.2
myFuzzyAlgorithm = FuzzyGaussian(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzygauss")
```

---

## FuzzyLarge

## Summary

Defines a fuzzy membership function where the larger input values have membership closer to 1. The function is defined by a user-specified midpoint (which is assigned a membership of 0.5) with a defined spread.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value with a fuzzy membership of 0.5.The default is the midpoint of the range of values of the input raster. | Double |
| spread | Defines the spread of the Large function. The spread generally ranges from 1 to 10, with the larger the value results in a steeper distribution from the midpoint.(The default value is 5) | Double |

## Code Samples

### Example 1

```python
FuzzyLarge (midpoint, spread)
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyLarge(12, 5))
outFzyMember.save("c:/sapyexamples/fzymemb")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyLarge(12, 5))
outFzyMember.save("c:/sapyexamples/fzymemb")
```

### Example 4

```python
# Name: FuzzyLarge_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyLarge algorithm object
midpoint = 15
spread = 5
myFuzzyAlgorithm = FuzzyLarge(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzylarge")
```

### Example 5

```python
# Name: FuzzyLarge_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyLarge algorithm object
midpoint = 15
spread = 5
myFuzzyAlgorithm = FuzzyLarge(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzylarge")
```

---

## FuzzyLinear

## Summary

Defines a fuzzy membership function through a linear transformation between the user-specified minimum value, a membership of 0, to the user-defined maximum value, which is assigned a membership of 1.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| minimum | The value that will have a membership of 0. If the minimum value is less than the maximum, the linear function will have a positive slope. If the minimum value is greater than the maximum, the linear function will have a negative slope.(The default value is Minimum of the input) | Double |
| maximum | The value that will have a membership of 1. If the maximum value is greater than the minimum, the linear function will have a positive slope. If the maximum value is less than the minimum, the linear function will have a negative slope.(The default value is Maximum of the input) | Double |

## Code Samples

### Example 1

```python
FuzzyLinear (minimum, maximum)
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyLinear(12, 16))
outFzyMember.save("c:/sapyexamples/fzyline")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyLinear(12, 16))
outFzyMember.save("c:/sapyexamples/fzyline")
```

### Example 4

```python
# Name: FuzzyLinear_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyLinear algorithm object
min = 19
max = 22
myFuzzyAlgorithm = FuzzyLinear(min, max)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzyline2")
```

### Example 5

```python
# Name: FuzzyLinear_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyLinear algorithm object
min = 19
max = 22
myFuzzyAlgorithm = FuzzyLinear(min, max)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzyline2")
```

---

## FuzzyMSLarge

## Summary

Defines a fuzzy membership through a function based on the mean and standard deviation, with the larger values having a membership closer to 1.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| meanMultiplier | The multiplier for the mean of the input values in the MSLarge function equation.(The default value is 1) | Double |
| STDMultiplier | The multiplier for the standard deviation of the input values in the MSLarge function equation.(The default value is 1) | Double |

## Code Samples

### Example 1

```python
u(x) = 1 - (b * s) / (x - (a * m) + (b * s))
```

### Example 2

```python
u(x) = 1 - (b * s) / (x - (a * m) + (b * s))
```

### Example 3

```python
FuzzyMSLarge (meanMultiplier, STDMultiplier)
```

### Example 4

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyMSLarge(1, 1.8))
outFzyMember.save("c:/sapyexamples/fzymslrg")
```

### Example 5

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyMSLarge(1, 1.8))
outFzyMember.save("c:/sapyexamples/fzymslrg")
```

### Example 6

```python
# Name: FuzzyMSLarge_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyMSLarge algorithm object
meanMultiply = 1.5
stdMultiply = 2.2
myFuzzyAlgorithm = FuzzyMSLarge(meanMultiply, stdMultiply)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzymslrg2")
```

### Example 7

```python
# Name: FuzzyMSLarge_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyMSLarge algorithm object
meanMultiply = 1.5
stdMultiply = 2.2
myFuzzyAlgorithm = FuzzyMSLarge(meanMultiply, stdMultiply)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzymslrg2")
```

---

## FuzzyMSSmall

## Summary

Defines a fuzzy membership through a function based on the mean and standard deviation, with the smaller values having a membership closer to 1.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| meanMultiplier | The multiplier for the mean of the input values in the MSLarge function equation.(The default value is 1) | Double |
| STDMultiplier | The multiplier for the standard deviation of the input values in the MSLarge function equation.(The default value is 1) | Double |

## Code Samples

### Example 1

```python
u(x) = (b * s) / (x - (a * m) + (b * s))
```

### Example 2

```python
u(x) = (b * s) / (x - (a * m) + (b * s))
```

### Example 3

```python
FuzzyMSSmall (meanMultiplier, STDMultiplier)
```

### Example 4

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyMSSmall(1.2, 3.2))
outFzyMember.save("c:/sapyexamples/fzymssml")
```

### Example 5

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyMSSmall(1.2, 3.2))
outFzyMember.save("c:/sapyexamples/fzymssml")
```

### Example 6

```python
# Name: FuzzyMSSmall_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyMSSmall algorithm object
meanMultiply = 1.5
stdMultiply = 1
myFuzzyAlgorithm = FuzzyMSSmall(meanMultiply, stdMultiply)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzymssml2")
```

### Example 7

```python
# Name: FuzzyMSSmall_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyMSSmall algorithm object
meanMultiply = 1.5
stdMultiply = 1
myFuzzyAlgorithm = FuzzyMSSmall(meanMultiply, stdMultiply)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzymssml2")
```

---

## FuzzyNear

## Summary

Defines a fuzzy membership function around a specific value which is defined by a user-defined midpoint (which is assigned a membership of 1), with a defined spread decreasing to zero.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value with a fuzzy membership of 1.The default is the midpoint of the range of values of the input raster. | Double |
| spread | Defines the spread of the Near function. The spread generally ranges from 0.001 to 1 with the larger the value results in a steeper distribution from the midpoint.(The default value is 0.1) | Double |

## Code Samples

### Example 1

```python
FuzzyNear (midpoint, spread)
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyGaussian(9, 0.1))
outFzyMember.save("c:/sapyexamples/fzynear")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzyGaussian(9, 0.1))
outFzyMember.save("c:/sapyexamples/fzynear")
```

### Example 4

```python
# Name: FuzzyNear_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyNear algorithm object
midpoint = 11
spread = 0.2
myFuzzyAlgorithm = FuzzyNear(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzynear2")
```

### Example 5

```python
# Name: FuzzyNear_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzyNear algorithm object
midpoint = 11
spread = 0.2
myFuzzyAlgorithm = FuzzyNear(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzynear2")
```

---

## FuzzySmall

## Summary

Defines a fuzzy membership function with the smaller input values having membership closer to 1. The function is defined by a user-specified midpoint (which is assigned a membership of 0.5) with a defined spread.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value with a fuzzy membership of 0.5.The default is the midpoint of the range of values of the input raster. | Double |
| spread | Defines the spread of the Small function. The spread generally ranges from 1 to 10, with the larger the value results in a steeper distribution from the midpoint.(The default value is 5) | Double |

## Code Samples

### Example 1

```python
FuzzySmall (midpoint, spread)
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzySmall(19, 8))
outFzyMember.save("c:/sapyexamples/fzysml")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outFzyMember = FuzzyMembership("as_std", FuzzySmall(19, 8))
outFzyMember.save("c:/sapyexamples/fzysml")
```

### Example 4

```python
# Name: FuzzySmall_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzySmall algorithm object
midpoint = 12
spread = 8
myFuzzyAlgorithm = FuzzySmall(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzysml2")
```

### Example 5

```python
# Name: FuzzySmall_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "as_std"

# Create the FuzzySmall algorithm object
midpoint = 12
spread = 8
myFuzzyAlgorithm = FuzzySmall(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzysml2")
```

---

## GEMI

## Summary

Calculates the Global Environmental Monitoring Index (GEMI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
GEMI = eta * (1 - 0.25 * eta) - ((Red - 0.125)/(1 - Red))
```

### Example 2

```python
GEMI = eta * (1 - 0.25 * eta) - ((Red - 0.125)/(1 - Red))
```

### Example 3

```python
eta = (2 * (NIR2 - Red2) + 1.5 * NIR + 0.5 * Red)/(NIR + Red + 0.5)
```

### Example 4

```python
eta = (2 * (NIR2 - Red2) + 1.5 * NIR + 0.5 * Red)/(NIR + Red + 0.5)
```

### Example 5

```python
GEMI (raster, {nir_band_id}, {red_band_id})
```

### Example 6

```python
import arcpy

GEMI_raster = arcpy.sa.GEMI("Landsat8.tif", 5, 4)
```

### Example 7

```python
import arcpy

GEMI_raster = arcpy.sa.GEMI("Landsat8.tif", 5, 4)
```

---

## GNDVI

## Summary

Calculates the Green Normalized Difference Vegetation Index (GNDVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 2) | Integer |

## Code Samples

### Example 1

```python
GNDVI = (NIR - Green)/(NIR + Green)
```

### Example 2

```python
GNDVI = (NIR - Green)/(NIR + Green)
```

### Example 3

```python
GNDVI (raster, {nir_band_id}, {green_band_id})
```

### Example 4

```python
import arcpy

GNDVI_raster = arcpy.sa.GNDVI("Landsat8.tif", 5, 3)
```

### Example 5

```python
import arcpy

GNDVI_raster = arcpy.sa.GNDVI("Landsat8.tif", 5, 3)
```

---

## Grayscale

## Summary

Converts a multiband image to a single-band grayscale image. Specified weights are applied to each of the input bands, and a normalization is applied for output.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| conversion_parameters | The weights for each of the bands comprising the input raster.(The default value is None) | List |

## Code Samples

### Example 1

```python
Grayscale (raster, {conversion_parameters})
```

### Example 2

```python
from arcpy.sa import *
out_grayscale_raster = Grayscale("imagery.tif")
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

### Example 3

```python
from arcpy.sa import *
out_grayscale_raster = Grayscale("imagery.tif")
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "imagery.tif"

# Execute the Grayscale function
out_grayscale_raster = Grayscale(in_raster)

# Save the output
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

### Example 5

```python
# Import the system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "imagery.tif"

# Execute the Grayscale function
out_grayscale_raster = Grayscale(in_raster)

# Save the output
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

---

## GVITM

## Summary

Calculates the Green Vegetation Index for Landsat TM (GVITM) from a Landsat TM image and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| band1_id | The band index of Band 1 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 1) | Integer |
| band2_id | The band index of Band 2 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 2) | Integer |
| band3_id | The band index of Band 3 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 3) | Integer |
| band4_id | The band index of Band 4 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 4) | Integer |
| band5_id | The band index of Band 5 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 5) | Integer |
| band7_id | The band index of Band 7 from the Landsat TM image.The band ID index uses one-based indexing.(The default value is 7) | Integer |

## Code Samples

### Example 1

```python
GVI=-0.2848 * Band1 - 0.2435 * Band2 - 0.5436 * Band3 + 0.7243 * Band4 + 0.084 * Band5 - 1.18 * Band7
```

### Example 2

```python
GVI=-0.2848 * Band1 - 0.2435 * Band2 - 0.5436 * Band3 + 0.7243 * Band4 + 0.084 * Band5 - 1.18 * Band7
```

### Example 3

```python
GVITM (raster, {band1_id}, {band2_id}, {band3_id}, {band4_id}, {band5_id}, {band7_id})
```

### Example 4

```python
import arcpy

GVITM_raster = arcpy.sa.GVITM("LandsatTM.tif", 1, 2, 3, 4, 5, 7)
```

### Example 5

```python
import arcpy

GVITM_raster = arcpy.sa.GVITM("LandsatTM.tif", 1, 2, 3, 4, 5, 7)
```

---

## HeatIndex

## Summary

Calculates apparent temperature based on ambient temperature and relative humidity. The apparent temperature is often described as how hot it feels to the human body.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| temperature_raster | A single-band raster where pixel values represent ambient air temperature. | Raster |
| relative_humidity_raster | A single-band raster where pixel values represent relative humidity as a percentage value between 0 and 100. | Raster |
| temperature_unit | The unit of measurement associated with the input temperature raster. Available input units are Celsius, Fahrenheit, and Kelvin.(The default value is Fahrenheit) | String |
| heat_index_unit | The unit of measurement associated with the output raster. Available output units are Celsius, Fahrenheit, and Kelvin.(The default value is Fahrenheit) | String |

## Code Samples

### Example 1

```python
Heat Index = ( -42.379 + (2.04901523 * T) + (10.14333127 * R) 
              - (0.22475541 * TR) - (6.83783e-3 * TT) - (5.481717e-2 * RR) 
              + (1.22874e-3 * TTR) + (8.5282e-4 * TRR) - (1.99e-6 * TTRR) )
```

### Example 2

```python
Heat Index = ( -42.379 + (2.04901523 * T) + (10.14333127 * R) 
              - (0.22475541 * TR) - (6.83783e-3 * TT) - (5.481717e-2 * RR) 
              + (1.22874e-3 * TTR) + (8.5282e-4 * TRR) - (1.99e-6 * TTRR) )
```

### Example 3

```python
HeatIndex (temperature_raster, relative_humidity_raster, {temperature_unit}, {heat_index_unit})
```

### Example 4

```python
from arcpy.sa import *
out_heatindex_raster = HeatIndex("temperature", "relative_humidity", "Celsius", "Kelvin")
out_heatindex_raster.save("C:/arcpyExamples/outputs/heat_index_K.tif")
```

### Example 5

```python
from arcpy.sa import *
out_heatindex_raster = HeatIndex("temperature", "relative_humidity", "Celsius", "Kelvin")
out_heatindex_raster.save("C:/arcpyExamples/outputs/heat_index_K.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_temperature_raster = "temperature.tif"
in_relative_humidity_raster  = "relativehumid.tif"

# Execute the HeatIndex function
out_heat_index_raster = HeatIndex(in_temperature_raster, in_relative_humidity_raster, "", "Celsius")

# Save the output
out_heat_index_raster.save("C:/arcpyExamples/outputs/heat_index_C.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_temperature_raster = "temperature.tif"
in_relative_humidity_raster  = "relativehumid.tif"

# Execute the HeatIndex function
out_heat_index_raster = HeatIndex(in_temperature_raster, in_relative_humidity_raster, "", "Celsius")

# Save the output
out_heat_index_raster.save("C:/arcpyExamples/outputs/heat_index_C.tif")
```

---

## HfBinary

## Summary

Defines the relationship between the horizontal cost factor and the horizontal relative moving angle through a binary function. If the horizontal relative moving angle is less than the cut angle, the horizontal factor is set to the value associated with the zero factor; otherwise it is infinity.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the binary function. (The zeroFactor is assigned as the horizontal factor when HRMA is less then the cutAngle.)(The default value is 1.0) | Double |
| cutAngle | The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity. (When the HRMA is less than the cutAngle the horizontal factor is assigned to the zeroFactor; when the HRMA is greater than the cutAngle the horizontal factor is assigned infinity.)(The default value is 45) | Double |

## Code Samples

### Example 1

```python
HfBinary ({zeroFactor}, {cutAngle})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHfBinary = HfBinary(1.5, 45.5)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHfBinary)
outDistAccum.save("C:/sapyexamples/output/distaccumhfb")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHfBinary = HfBinary(1.5, 45.5)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHfBinary)
outDistAccum.save("C:/sapyexamples/output/distaccumhfb")
```

### Example 4

```python
# Name: HfBinary_Ex_02.py
# Description: Uses the HFBinary object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfBinary Object
zeroFactor = 1.0
cutAngle = 45.0
myHorizFactor = HfBinary(zeroFactor, cutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute 
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfb2")
```

### Example 5

```python
# Name: HfBinary_Ex_02.py
# Description: Uses the HFBinary object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfBinary Object
zeroFactor = 1.0
cutAngle = 45.0
myHorizFactor = HfBinary(zeroFactor, cutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute 
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfb2")
```

---

## HfForward

## Summary

Defines the relationship between the horizontal cost factor and the horizontal relative moving angle through a forward function. The function establishes that only forward movement is allowed.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the forward function.(The default value is 0.5) | Double |
| sideValue | Identifies the HF value that will be assigned for HRMAs that are equal to or less than 45 degrees and less than 90 degrees. In the diagram above, the sideValue is assigned 1.(The default value is 1.0) | Double |

## Code Samples

### Example 1

```python
HfForward ({zeroFactor}, {sideValue})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfForward(0.5, 1.0)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhff")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfForward(0.5, 1.0)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhff")
```

### Example 4

```python
# Name: HfForward_Ex_02.py
# Description: Uses the HfForward object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfForward Object
zeroFactor = 0.5
sideValue = 1.0
myHorizFactor = HfForward(zeroFactor, sideValue)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfF2")
```

### Example 5

```python
# Name: HfForward_Ex_02.py
# Description: Uses the HfForward object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfForward Object
zeroFactor = 0.5
sideValue = 1.0
myHorizFactor = HfForward(zeroFactor, sideValue)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfF2")
```

---

## HfInverseLinear

## Summary

Defines the relationship between the horizontal cost factor and the horizontal relative moving angle through an inverse linear function. The function specifies that the horizontal factor is an inverse linear function of the horizontal relative moving angle.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the inverse linear function.(The default value is 2.0) | Double |
| cutAngle | The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity.(The default value is 180.0) | Double |
| slope | Identifies the slope of the straight line in the HRMA-HF coordinate system. Slope is specified as the rise over the run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 HF on the y axis / 30 degrees on the x axis).(The default value is -0.011111) | Double |

## Code Samples

### Example 1

```python
HfInverseLinear ({zeroFactor}, {cutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfInverseLinear(2.0, 181.0, -0.01111)
outPathDist = PathDistance("source.shp", "costraster", "", "", myHorizFactor)
outPathDist.save("C:/sapyexamples/output/pathdisthfil")

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfInverseLinear(2.0, 181.0, -0.01111)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhfil")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfInverseLinear(2.0, 181.0, -0.01111)
outPathDist = PathDistance("source.shp", "costraster", "", "", myHorizFactor)
outPathDist.save("C:/sapyexamples/output/pathdisthfil")

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfInverseLinear(2.0, 181.0, -0.01111)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhfil")
```

### Example 4

```python
# Name: HfInverseLinear_Ex_02.py
# Description: Uses the HfInverseLinear object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfInverseLinear Object
zeroFactor = 2.0
cutAngle = 181.0
slope = -0.01111
myHorizFactor = HfInverseLinear(zeroFactor, cutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfil2")
```

### Example 5

```python
# Name: HfInverseLinear_Ex_02.py
# Description: Uses the HfInverseLinear object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfInverseLinear Object
zeroFactor = 2.0
cutAngle = 181.0
slope = -0.01111
myHorizFactor = HfInverseLinear(zeroFactor, cutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfil2")
```

---

## HfLinear

## Summary

Defines the relationship between the horizontal cost factor and the horizontal relative moving angle through a linear function. The function specifies that the horizontal factor has a linear relationship with the horizontal relative moving angle.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the linear function.(The default value is 0.5) | Double |
| cutAngle | The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity.(The default value is 181.0) | Double |
| slope | Identifies the slope of the straight line in the HRMA-HF coordinate system. Slope is specified as the rise over the run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 HF on the y axis / 30 degrees on the x axis).(The default value is 0.011111) | Double |

## Code Samples

### Example 1

```python
HfLinear ({zeroFactor}, {cutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfLinear(0.5, 181.0, 0.01111)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhfL")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfLinear(0.5, 181.0, 0.01111)
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhfL")
```

### Example 4

```python
# Name: HfLinear_Ex_02.py
# Description: Uses the HfLinear object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfLinear Object
zeroFactor = 0.5
cutAngle = 181.0
slope = 0.01111
myHorizFactor = HfLinear(zeroFactor, cutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfl2")
```

### Example 5

```python
# Name: HfLinear_Ex_02.py
# Description: Uses the HfLinear object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfLinear Object
zeroFactor = 0.5
cutAngle = 181.0
slope = 0.01111
myHorizFactor = HfLinear(zeroFactor, cutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhfl2")
```

---

## HfTable

## Summary

Defines the relationship between the horizontal cost factor and the horizontal relative moving angle through a specified table file. The table file identifies the horizontal factor graph used to determine the horizontal factors.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inTable | The inTable is an ASCII file with two columns on each line. The first column identifies the HRMA in degrees, and the second, the HF. Each line specifies a point. Two consecutive points produce a line segment in the HRMA-HF coordinate system. The angles must be input in ascending order. The HF factor for any HRMA angle less than the first (lowest) input value or larger than the last (largest) input value will be set to infinity. An infinite HF is represented by -1 in the ASCII file. | File |

## Code Samples

### Example 1

```python
HfTable (inTable)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfTable("hffile.txt")
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhft")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myHorizFactor = HfTable("hffile.txt")
outDistAccum = DistanceAccumulation("source.shp", "barrier.tif",
                                    "elev.tif", "", "", "",
                                    "horizontalRas.tif", myHorizFactor)
outDistAccum.save("C:/sapyexamples/output/distaccumhft")
```

### Example 4

```python
# Name: HfTable_Ex_02.py
# Description: Uses the HfTable object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfTable Object
inTable = "hffile.txt"
myHorizFactor = HfTable(inTable)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhft2")
```

### Example 5

```python
# Name: HfTable_Ex_02.py
# Description: Uses the HfTable object to run the
#              DistanceAccumulation tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "sourcepts.shp"
inSurfaceRaster = "elevation.tif"
inHorizontalRaster = "horizontalRas.tif"

# Create the HfTable Object
inTable = "hffile.txt"
myHorizFactor = HfTable(inTable)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData,"", inSurfaceRaster,"","",
                                    "", inHorizontalRaster, myHorizFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumhft2")
```

---

## IronOxide

## Summary

Calculates the Iron Oxide (IO) ratio from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| blue_band_id | The band ID of the blue band. The ID index uses one-based indexing.(The default value is 2) | Integer |

## Code Samples

### Example 1

```python
Iron Oxide Ratio = Red / Blue
```

### Example 2

```python
Iron Oxide Ratio = Red / Blue
```

### Example 3

```python
IronOxide (raster, {red_band_id}, {blue_band_id})
```

### Example 4

```python
import arcpy

IronOxide_raster = arcpy.sa.IronOxide("Sentinel2.tif", 4, 2)
```

### Example 5

```python
import arcpy

IronOxide_raster = arcpy.sa.IronOxide("Sentinel2.tif", 4, 2)
```

---

## KrigingModelOrdinary

## Summary

Defines the Ordinary Kriging model. The available model types are Spherical, Circular, Exponential, Gaussian, and Linear.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| semivariogramType | Semivariogram model to be used.SPHERICAL—Spherical semivariogram model.CIRCULAR— Circular semivariogram model.EXPONENTIAL— Exponential semivariogram model.GAUSSIAN— Gaussian (or normal distribution) semivariogram model.LINEAR—Linear semivariogram model with a sill.(The default value is SPHERICAL) | String |
| lagSize | The lag size to be used in model creation. The default is the output raster cell size. | Double |
| majorRange | Represents a distance beyond which there is little or no correlation. | Double |
| partialSill | The difference between the nugget and the sill. | Double |
| nugget | Represents the error and variation at spatial scales too fine to detect. The nugget effect is seen as a discontinuity at the origin. | Double |

## Code Samples

### Example 1

```python
Z(s) = µ + ε(s)
```

### Example 2

```python
Z(s) = µ + ε(s)
```

### Example 3

```python
KrigingModelOrdinary ({semivariogramType}, {lagSize}, {majorRange}, {partialSill}, {nugget})
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", 70000, 250000, 180000, 34000)
outKrigingOrd1 = Kriging("ca_ozone_pts.shp", "ELEVATION", kModelOrdinary, 2000, RadiusVariable(),"")
outKrigingOrd1.save("C:/sapyexamples/output/kordinary1")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", 70000, 250000, 180000, 34000)
outKrigingOrd1 = Kriging("ca_ozone_pts.shp", "ELEVATION", kModelOrdinary, 2000, RadiusVariable(),"")
outKrigingOrd1.save("C:/sapyexamples/output/kordinary1")
```

### Example 6

```python
# Name: KrigingModelOrdinary_Ex_02.py
# Description: Uses the KrigingModelOrdinary object to execute the Kriging tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeature = "ca_ozone_pts.shp"
outVarRaster = "C:/sapyexamples/output/ovariance2"

# Create KrigingModelOrdinary Object
lagSize = 70000
majorRange = 250000
partialSill = 180000
nugget = 34000
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", lagSize, majorRange,
                                         partialSill, nugget)

# Execute Kriging
outKrigingOrd2 = Kriging(inPointFeature, "ELEVATION", kModelOrdinary, 2000,
                     RadiusFixed(200000, 10), outVarRaster)

# Save the output 
outKrigingOrd2.save("C:/sapyexamples/output/kordinary2")
```

### Example 7

```python
# Name: KrigingModelOrdinary_Ex_02.py
# Description: Uses the KrigingModelOrdinary object to execute the Kriging tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeature = "ca_ozone_pts.shp"
outVarRaster = "C:/sapyexamples/output/ovariance2"

# Create KrigingModelOrdinary Object
lagSize = 70000
majorRange = 250000
partialSill = 180000
nugget = 34000
kModelOrdinary = KrigingModelOrdinary("CIRCULAR", lagSize, majorRange,
                                         partialSill, nugget)

# Execute Kriging
outKrigingOrd2 = Kriging(inPointFeature, "ELEVATION", kModelOrdinary, 2000,
                     RadiusFixed(200000, 10), outVarRaster)

# Save the output 
outKrigingOrd2.save("C:/sapyexamples/output/kordinary2")
```

---

## KrigingModelUniversal

## Summary

Defines the Universal Kriging model. The available model types are Linear with linear drift and Linear with quadratic drift.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| semivariogramType | Semivariogram model to be used.LINEARDRIFT—Universal Kriging with linear drift.QUADRATICDRIFT— Universal Kriging with quadratic drift.(The default value is LINEARDRIFT) | String |
| lagSize | The lag size to be used in model creation. The default is the output raster cell size. | Double |
| majorRange | Represents a distance beyond which there is little or no correlation. | Double |
| partialSill | The difference between the nugget and the sill. | Double |
| nugget | Represents the error and variation at spatial scales too fine to detect. The nugget effect is seen as a discontinuity at the origin. | Double |

## Code Samples

### Example 1

```python
Z(s) = µ(s) + ε(s)
```

### Example 2

```python
Z(s) = µ(s) + ε(s)
```

### Example 3

```python
KrigingModelUniversal ({semivariogramType}, {lagSize}, {majorRange}, {partialSill}, {nugget})
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
kModelUniversal = KrigingModelUniversal("LINEARDRIFT", 70000, 250000, 180000, 34000)
outKrigingUni1 = Kriging("ca_ozone_pts.shp", "ELEVATION", kModelUniversal, 2000, RadiusVariable(),"")
outKrigingUni1.save("C:/sapyexamples/output/kuniversal1")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
kModelUniversal = KrigingModelUniversal("LINEARDRIFT", 70000, 250000, 180000, 34000)
outKrigingUni1 = Kriging("ca_ozone_pts.shp", "ELEVATION", kModelUniversal, 2000, RadiusVariable(),"")
outKrigingUni1.save("C:/sapyexamples/output/kuniversal1")
```

### Example 6

```python
# Name: KrigingModelUniversal_Ex_02.py
# Description: Uses the KrigingModelUniversal object to execute the Kriging tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeature = "ca_ozone_pts.shp"
outVarRaster = "C:/sapyexamples/output/uvariance2"

# Create KrigingModelUniversal Object
lagSize = 70000
majorRange = 250000
partialSill = 180000
nugget = 34000
kModelUniversalObj = KrigingModelUniversal("LINEARDRIFT", lagSize, majorRange,
                                           partialSill, nugget)

# Execute 
outKrigingUni2 = Kriging(inPointFeature, "ELEVATION", kModelUniversalObj, 2000,
                           RadiusFixed(200000, 10), outVarRaster)

# Save the output 
outKrigingUni2.save("C:/sapyexamples/output/kuniversal2")
```

### Example 7

```python
# Name: KrigingModelUniversal_Ex_02.py
# Description: Uses the KrigingModelUniversal object to execute the Kriging tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeature = "ca_ozone_pts.shp"
outVarRaster = "C:/sapyexamples/output/uvariance2"

# Create KrigingModelUniversal Object
lagSize = 70000
majorRange = 250000
partialSill = 180000
nugget = 34000
kModelUniversalObj = KrigingModelUniversal("LINEARDRIFT", lagSize, majorRange,
                                           partialSill, nugget)

# Execute 
outKrigingUni2 = Kriging(inPointFeature, "ELEVATION", kModelUniversalObj, 2000,
                           RadiusFixed(200000, 10), outVarRaster)

# Save the output 
outKrigingUni2.save("C:/sapyexamples/output/kuniversal2")
```

---

## LinearUnmixing

## Summary

Performs subpixel classification and calculates the fractional abundance of land-cover types for individual pixels.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input raster. | Raster |
| in_spectral_profile_file | The path to the spectral profile for the various land cover classes.This can be provided as a polygon feature class, a classifier definition file (.ecd) generated from the Train Maximum Likelihood Classifier tool, or a JSON file (.json) that contains the class spectral profiles. | String |
| value_option | Specifies how the output pixel values will be defined.SUM_TO_ONE—Class values for each pixel will be provided in decimal format with the sum of all classes equal to 1; for example, Class1 = 0.16; Class2 = 0.24; Class3 = 0.60.NON_NEGATIVE—There will be no negative output values. Both options can be specified by delimiting with a semicolon: "SUM_TO_ONE;NON_NEGATIVE". | String |

## Code Samples

### Example 1

```python
LinearUnmixing (in_raster, in_spectral_profile_file, {value_option})
```

### Example 2

```python
from arcpy.sa import *
out_linearunmixing_raster = LinearUnmixing(
    "Landsat8.tif","C:/arcpyExamples/data/training_feature.ecd")
out_linearunmixing_raster.save(
    "C:/arcpyexamples/outputs/linearunmix_output.tif")
```

### Example 3

```python
from arcpy.sa import *
out_linearunmixing_raster = LinearUnmixing(
    "Landsat8.tif","C:/arcpyExamples/data/training_feature.ecd")
out_linearunmixing_raster.save(
    "C:/arcpyexamples/outputs/linearunmix_output.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "Landsat_8.tif"
in_spectral_profile = "C:/data/training_features.ecd"
value_options = "SUM_TO_ONE;NON_NEGATIVE" 

# Apply LinearSpectralUnmixing function
unmixing_outputs = LinearUnmixing(in_raster, in_spectral_profile, value_options)

# Save the output
unmixing_outputs.save("C:/arcpyExamples/outputs/unmixing_results.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "Landsat_8.tif"
in_spectral_profile = "C:/data/training_features.ecd"
value_options = "SUM_TO_ONE;NON_NEGATIVE" 

# Apply LinearSpectralUnmixing function
unmixing_outputs = LinearUnmixing(in_raster, in_spectral_profile, value_options)

# Save the output
unmixing_outputs.save("C:/arcpyExamples/outputs/unmixing_results.tif")
```

---

## Mask

## Summary

Creates a raster object by specifying one or more NoData values or a range of valid pixel values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| no_data_values[no_data_values,...] | The NoData value or list of values. Values can be type Double or Integer.(The default value is None) | Double |
| included_ranges[included_ranges,...] | The range of valid pixel values to be included in the output raster. Values can be type Double or Integer. (The default value is None) | Double |
| no_data_interpretation | Specifies how the NoData values will be displayed in the output raster. 0—All—The NoData values you specify for each band must occur in the same cell for the output image to contain the NoData cell.1—Any—If the NoData value you specify occurs for a cell in a specified band, that cell in the output image will be NoData.(The default value is None) | Integer |

## Code Samples

### Example 1

```python
Mask (raster, {no_data_values}, {included_ranges}, {no_data_interpretation})
```

### Example 2

```python
import arcpy

out_Mask_raster = arcpy.sa.Mask("Landsat8.tif", no_data_values = 6, included_ranges = [3,9])
```

### Example 3

```python
import arcpy

out_Mask_raster = arcpy.sa.Mask("Landsat8.tif", no_data_values = 6, included_ranges = [3,9])
```

---

## MSAVI

## Summary

Calculates the Modified Soil Adjusted Vegetation Index (MSAVI2) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
MSAVI2 = (1/2)*(2(NIR+1)-sqrt((2*NIR+1)2-8(NIR-Red)))
```

### Example 2

```python
MSAVI2 = (1/2)*(2(NIR+1)-sqrt((2*NIR+1)2-8(NIR-Red)))
```

### Example 3

```python
MSAVI (raster, {nir_band_id}, {red_band_id})
```

### Example 4

```python
import arcpy

MSAVI_raster = arcpy.sa.MSAVI("Landsat8.tif", 5, 4)
```

### Example 5

```python
import arcpy

MSAVI_raster = arcpy.sa.MSAVI("Landsat8.tif", 5, 4)
```

---

## MTVI2

## Summary

Calculates the Modified Triangular Vegetation Index (MTVI2) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
MTVI2 = 1.5*(1.2 * (NIR - Green) - 2.5 * (Red - Green))√((2 * NIR + 1)²-(6 * NIR - 5√(Red)) - 0.5)
```

### Example 2

```python
MTVI2 = 1.5*(1.2 * (NIR - Green) - 2.5 * (Red - Green))√((2 * NIR + 1)²-(6 * NIR - 5√(Red)) - 0.5)
```

### Example 3

```python
MTVI2 (raster, {nir_band_id}, {red_band_id}, {green_band_id})
```

### Example 4

```python
import arcpy

MTVI2_raster = arcpy.sa.MTVI2("Landsat8.tif", 5, 4, 3)
```

### Example 5

```python
import arcpy

MTVI2_raster = arcpy.sa.MTVI2("Landsat8.tif", 5, 4, 3)
```

---

## NBR

## Summary

Calculates the Normalized Burn Ratio (NBR) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| swir_band_id | The band ID of the shortwave infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |

## Code Samples

### Example 1

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 2

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 3

```python
NBR (raster, {swir_band_id}, {nir_band_id})
```

### Example 4

```python
from arcpy.sa import *
out_nbr_raster = NBR("landsat8.tif", 7, 5)
out_nbr_raster.save("C:/arcpyExamples/outputs/NBR.tif")
```

### Example 5

```python
from arcpy.sa import *
out_nbr_raster = NBR("landsat8.tif", 7, 5)
out_nbr_raster.save("C:/arcpyExamples/outputs/NBR.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NBR function
out_nbr_raster = NBR(in_raster, 7, 5)

# Save the output
out_nbr_raster.save("C:/arcpyExamples/outputs/NBR.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NBR function
out_nbr_raster = NBR(in_raster, 7, 5)

# Save the output
out_nbr_raster.save("C:/arcpyExamples/outputs/NBR.tif")
```

---

## NbrAnnulus

## Summary

Defines an annulus neighborhood which is created by specifying an inner and outer circles' radii in either map units or number of cells.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| innerRadius | The inner radius of an annulus neighborhood.(The default value is 1) | Double |
| outerRadius | The outer radius of an annulus neighborhood.(The default value is 3) | Double |
| units | Defines the units of the neighborhood.CELL—The unit of measurement is in cells.MAP—The units are in map coordinates.(The default value is CELL) | String |

## Code Samples

### Example 1

```python
NbrAnnulus ({innerRadius}, {outerRadius}, {units})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrA = BlockStatistics("block", NbrAnnulus(1, 2, "CELL"))
outNbrA.save("C:/sapyexamples/output/blstatnbra2")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrA = BlockStatistics("block", NbrAnnulus(1, 2, "CELL"))
outNbrA.save("C:/sapyexamples/output/blstatnbra2")
```

### Example 4

```python
# Name: NbrAnnulus_Ex_02.py
# Description: Uses the NbrAnnulus object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
innerRadius = 1
outerRadius = 3
myNbrAnnulus = NbrAnnulus(innerRadius, outerRadius, "MAP")

# Execute BlockStatistics
outBlkStats =  BlockStatistics(inRaster, myNbrAnnulus, "MINIMUM", "DATA")

# Save the output 
outBlkStats.save("C:/sapyexamples/output/blstat_Ann3")
```

### Example 5

```python
# Name: NbrAnnulus_Ex_02.py
# Description: Uses the NbrAnnulus object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
innerRadius = 1
outerRadius = 3
myNbrAnnulus = NbrAnnulus(innerRadius, outerRadius, "MAP")

# Execute BlockStatistics
outBlkStats =  BlockStatistics(inRaster, myNbrAnnulus, "MINIMUM", "DATA")

# Save the output 
outBlkStats.save("C:/sapyexamples/output/blstat_Ann3")
```

---

## NbrCircle

## Summary

Defines a circle neighborhood which is created by specifying the radius in either map units or number of cells.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| radius | The radius of the circle neighborhood.(The default value is 3) | Double |
| units | Defines the units of the neighborhood.CELL—The unit of measurement is in cells.MAP—The units are in map coordinates.(The default value is CELL) | String |

## Code Samples

### Example 1

```python
NbrCircle ({radius}, {units})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrC = BlockStatistics("block", NbrCircle(2, "MAP"))
outNbrC.save("C:/sapyexamples/output/blstatsnbrc2")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrC = BlockStatistics("block", NbrCircle(2, "MAP"))
outNbrC.save("C:/sapyexamples/output/blstatsnbrc2")
```

### Example 4

```python
# Name: NbrCircle_Ex_02.py
# Description: Uses the NbrCircle object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
radius = 2
myNbrCirc = NbrCircle(radius, "MAP")

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrCirc, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_cir3")
```

### Example 5

```python
# Name: NbrCircle_Ex_02.py
# Description: Uses the NbrCircle object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
radius = 2
myNbrCirc = NbrCircle(radius, "MAP")

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrCirc, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_cir3")
```

---

## NbrIrregular

## Summary

Defines an irregular neighborhood which is created by a kernel file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inKernelFile | The irregular inKernelFile is an ASCII text file that defines the shape of an irregular neighborhood. A value of 0 for a cell position indicates that the cell is not a member of the neighborhood, and a nonzero number at a corresponding cell's position indicates that the cell value be included as a member of the neighborhood. | File |

## Code Samples

### Example 1

```python
x = (width + 1)/2
y = (height + 1)/2
```

### Example 2

```python
x = (width + 1)/2
y = (height + 1)/2
```

### Example 3

```python
NbrIrregular (inKernelFile)
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrKF = BlockStatistics("block", NbrIrregular("irreg.txt"))
outNbrKF.save("C:/sapyexamples/output/blstatsnbri2")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrKF = BlockStatistics("block", NbrIrregular("irreg.txt"))
outNbrKF.save("C:/sapyexamples/output/blstatsnbri2")
```

### Example 6

```python
# Name: NbrIrregular_Ex_02.py
# Description: Uses the NbrIrregular object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
inKernelFile = "C:/data/irreg.txt"
myNbrIrreg = NbrIrregular(inKernelFile)

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrIrreg, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_irr3")
```

### Example 7

```python
# Name: NbrIrregular_Ex_02.py
# Description: Uses the NbrIrregular object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
inKernelFile = "C:/data/irreg.txt"
myNbrIrreg = NbrIrregular(inKernelFile)

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrIrreg, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_irr3")
```

---

## NbrRectangle

## Summary

Defines a rectangle neighborhood which is created by specifying the height and the width in either map units or number of cells.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| width | The width of the rectangle neighborhood.If only the width is specified, the resulting neighborhood is a square.(The default value is 3) | Double |
| height | The height of the rectangle neighborhood.If only the height is specified, the resulting neighborhood is a square.(The default value is 3) | Double |
| units | Defines the units of the neighborhood.CELL—The unit of measurement is in cells.MAP—The units are in map coordinates.(The default value is CELL) | String |

## Code Samples

### Example 1

```python
x = (width of the neighborhood + 1)/2
y = (height of the neighborhood + 1)/2
```

### Example 2

```python
x = (width of the neighborhood + 1)/2
y = (height of the neighborhood + 1)/2
```

### Example 3

```python
NbrRectangle ({width}, {height}, {units})
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrRec = BlockStatistics("block", NbrRectangle(4, 5, "MAP"))
outNbrRec.save("C:/sapyexamples/output/blstatsnbrr2")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrRec = BlockStatistics("block", NbrRectangle(4, 5, "MAP"))
outNbrRec.save("C:/sapyexamples/output/blstatsnbrr2")
```

### Example 6

```python
# Name: NbrRectangle_Ex_02.py
# Description: Uses the NbrRectangle object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
width = 5
height = 6
myNbrRec = NbrRectangle(width, height, "MAP")

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrRec, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_rec3")
```

### Example 7

```python
# Name: NbrRectangle_Ex_02.py
# Description: Uses the NbrRectangle object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
width = 5
height = 6
myNbrRec = NbrRectangle(width, height, "MAP")

# Execute BlockStatistics
outBlkStat =  BlockStatistics(inRaster, myNbrRec, "MINIMUM", "DATA")

# Save the output 
outBlkStat.save("C:/sapyexamples/output/blstat_rec3")
```

---

## NbrWedge

## Summary

Defines a wedge neighborhood which is created by specifying a radius and two angles in either map units or number of cells.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| radius | The radius is the distance from the corner of the wedge to the outer limit of the wedge. The radius is an integer or floating-point value.(The default value is 3) | Double |
| startAngle | The startAngle is an integer or floating-point value from 0 to 360.The start angle is measured counterclockwise from the positive x-axis (3:00 on a clock) to the closest edge of the wedge.(The default value is 0) | Double |
| endAngle | The endAngle is an integer or floating-point value from 0 to 360.The end angle is measured counterclockwise from the positive x-axis (3:00 on a clock) to the outer edge of the wedge.(The default value is 90) | Double |
| units | Defines the units of the neighborhood.CELL—The unit of measurement is in cells.MAP—The units are in map coordinates.(The default value is CELL) | String |

## Code Samples

### Example 1

```python
NbrWedge ({radius}, {startAngle}, {endAngle}, {units})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrWedge = BlockStatistics("block", NbrWedge(5, 10.5, 40, "MAP"))
outNbrWedge.save("C:/sapyexamples/output/blstatsnbrw2")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrWedge = BlockStatistics("block", NbrWedge(5, 10.5, 40, "MAP"))
outNbrWedge.save("C:/sapyexamples/output/blstatsnbrw2")
```

### Example 4

```python
# Name: NbrWedge_Ex_02.py
# Description: Uses the NbrWedge object to execute BlockStatistics tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
radius = 5
startAngle = 5
endAngle = 10

myNbrWedge = NbrWedge(radius, startAngle, endAngle, "")

# Execute BlockStatistics
outBlkStats =  BlockStatistics(inRaster, myNbrWedge, "MINIMUM", "DATA")

# Save the output 
outBlkStats.save("C:/sapyexamples/output/blkst_wedge4")
```

### Example 5

```python
# Name: NbrWedge_Ex_02.py
# Description: Uses the NbrWedge object to execute BlockStatistics tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
radius = 5
startAngle = 5
endAngle = 10

myNbrWedge = NbrWedge(radius, startAngle, endAngle, "")

# Execute BlockStatistics
outBlkStats =  BlockStatistics(inRaster, myNbrWedge, "MINIMUM", "DATA")

# Save the output 
outBlkStats.save("C:/sapyexamples/output/blkst_wedge4")
```

---

## NbrWeight

## Summary

Defines a weight neighborhood which is created using a kernel file specifying the values to multiply the cell by that are within the neighborhood.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inKernelFile | An ASCII text file that defines the shape of the neighborhood and the weight of each cell in that neighborhood. A value of 0 for a cell position indicates that the cell is not a member of the neighborhood, and a number at a corresponding cell's position indicates that the cell value be included as a member of the neighborhood. The nonzero value will also serve as the weight to multiply the corresponding cell value. | File |

## Code Samples

### Example 1

```python
x = (width + 1)/2
y = (height + 1)/2
```

### Example 2

```python
x = (width + 1)/2
y = (height + 1)/2
```

### Example 3

```python
NbrWeight (inKernelFile)
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrWF = BlockStatistics("block", NbrWeight("weight.txt"))
outNbrWF.save("C:/sapyexamples/output/blstatsnbrwf2")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNbrWF = BlockStatistics("block", NbrWeight("weight.txt"))
outNbrWF.save("C:/sapyexamples/output/blstatsnbrwf2")
```

### Example 6

```python
# Name: NbrWeight_Ex_02.py
# Description: Uses the NbrWeight object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
inWeightFile = "C:/data/weight.txt"
myNbrWeight = NbrWeight(inWeightFile)

# Execute BlockStatistics
outBlStats =  BlockStatistics(inRaster, myNbrWeight, "MINIMUM", "DATA")

# Save the output 
outBlStats.save("C:/sapyexamples/output/blstat_wght3")
```

### Example 7

```python
# Name: NbrWeight_Ex_02.py
# Description: Uses the NbrWeight object to execute BlockStatistics tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"

# Create the Neighborhood Object
inWeightFile = "C:/data/weight.txt"
myNbrWeight = NbrWeight(inWeightFile)

# Execute BlockStatistics
outBlStats =  BlockStatistics(inRaster, myNbrWeight, "MINIMUM", "DATA")

# Save the output 
outBlStats.save("C:/sapyexamples/output/blstat_wght3")
```

---

## NDBI

## Summary

Calculates the Normalized Difference Built-up Index (NDBI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| swir_band_id | The band ID of the shortwave infrared band. The ID index uses one-based indexing.(The default value is 6) | Integer |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |

## Code Samples

### Example 1

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

### Example 2

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

### Example 3

```python
NDBI (raster, {swir_band_id}, {nir_band_id})
```

### Example 4

```python
from arcpy.sa import *
out_ndbi_raster = NDBI("landsat8.tif", 6, 5)
out_ndbi_raster.save("C:/arcpyExamples/outputs/NDBI.tif")
```

### Example 5

```python
from arcpy.sa import *
out_ndbi_raster = NDBI("landsat8.tif", 6, 5)
out_ndbi_raster.save("C:/arcpyExamples/outputs/NDBI.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDBI function
out_ndbi_raster = NDBI(in_raster, 6, 5)

# Save the output
out_ndbi_raster.save("C:/arcpyExamples/outputs/NDBI.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDBI function
out_ndbi_raster = NDBI(in_raster, 6, 5)

# Save the output
out_ndbi_raster.save("C:/arcpyExamples/outputs/NDBI.tif")
```

---

## NDMI

## Summary

Calculates the Normalized Difference Moisture Index (NDMI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| swir1_band_id | The band ID of the shortwave infrared band. The ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 2

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 3

```python
NDMI (raster, {nir_band_id}, {swir1_band_id})
```

### Example 4

```python
from arcpy.sa import *
out_ndmi_raster = NDMI("landsat8.tif", 5, 6)
out_ndmi_raster.save("C:/arcpyExamples/outputs/NDMI.tif")
```

### Example 5

```python
from arcpy.sa import *
out_ndmi_raster = NDMI("landsat8.tif", 5, 6)
out_ndmi_raster.save("C:/arcpyExamples/outputs/NDMI.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDMI function
out_ndmi_raster = NDMI(in_raster, 5, 6)

# Save the output
out_ndmi_raster.save("C:/arcpyExamples/outputs/NDMI.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDMI function
out_ndmi_raster = NDMI(in_raster, 5, 6)

# Save the output
out_ndmi_raster.save("C:/arcpyExamples/outputs/NDMI.tif")
```

---

## NDSI

## Summary

Calculates the Normalized Difference Snow Index (NDSI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| swir_band_id | The band ID of the shortwave infrared band. The ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 2

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 3

```python
NDSI (raster, {green_band_id}, {swir_band_id})
```

### Example 4

```python
from arcpy.sa import *
out_ndsi_raster = NDSI("landsat8.tif", 4, 6)
out_ndsi_raster.save("C:/arcpyExamples/outputs/NDSI.tif")
```

### Example 5

```python
from arcpy.sa import *
out_ndsi_raster = NDSI("landsat8.tif", 4, 6)
out_ndsi_raster.save("C:/arcpyExamples/outputs/NDSI.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDSI function
out_ndsi_raster = NDSI(in_raster, 4, 6)

# Save the output
out_ndsi_raster.save("C:/arcpyExamples/outputs/NDSI.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "landsat8.tif"

# Execute NDSI function
out_ndsi_raster = NDSI(in_raster, 4, 6)

# Save the output
out_ndsi_raster.save("C:/arcpyExamples/outputs/NDSI.tif")
```

---

## NDVI

## Summary

Calculates the Normalized Difference Vegetation Index (NDVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 2

```python
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 3

```python
NDVI (raster, {nir_band_id}, {red_band_id})
```

### Example 4

```python
import arcpy

NDVI_raster = arcpy.sa.NDVI("Landsat8.tif", 5, 4)
```

### Example 5

```python
import arcpy

NDVI_raster = arcpy.sa.NDVI("Landsat8.tif", 5, 4)
```

---

## NDVIre

## Summary

Calculates the Red-Edge Normalized Difference Vegetation Index (NDVIre) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| redEdge_band_id | The band ID of the red-edge band. The band ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
NDVIre = (NIR - RedEdge)/(NIR + RedEdge)
```

### Example 2

```python
NDVIre = (NIR - RedEdge)/(NIR + RedEdge)
```

### Example 3

```python
NDVIre (raster, {nir_band_id}, {redEdge_band_id})
```

### Example 4

```python
import arcpy

NDVIre_raster = arcpy.sa.NDVIre("Landsat8.tif", 5, 6)
```

### Example 5

```python
import arcpy

NDVIre_raster = arcpy.sa.NDVIre("Landsat8.tif", 5, 6)
```

---

## NDWI

## Summary

Calculates the Normalized Difference Water Index (NDWI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
NDWI = (Green - NIR) / (Green + NIR)
```

### Example 2

```python
NDWI = (Green - NIR) / (Green + NIR)
```

### Example 3

```python
NDWI (raster, {nir_band_id}, {green_band_id})
```

### Example 4

```python
import arcpy

NDWI_raster = arcpy.sa.NDWI("Sentinel2.tif", 8, 3)
```

### Example 5

```python
import arcpy

NDWI_raster = arcpy.sa.NDWI("Sentinel2.tif", 8, 3)
```

---

## Pansharpen

## Summary

Creates a higher-resolution multiband image by fusing a lower-resolution multispectral image and a higher-resolution panchromatic image.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| pan_raster | The input panchromatic raster. | Raster |
| ms_raster | The input multispectral raster. | Raster |
| ir_raster | Specify the path to a single-band image containing the near-infrared band. (The default value is None) | Raster |
| fourth_band_of_ms_is_ir | Specify that the fourth band of the input multispectral raster (ms_raster) is an infrared band.True—The fourth band of the input multispectral raster is an IR band.False—The multispectral raster contains an IR band.(The default value is True) | Boolean |
| weights | Specify weights applied to Red, Green, Blue, Near-Infrared bands. Sum of the weights is 1. For example, the weights for QuickBird imagery are [0.166, 0.167, 0.167, 0.5].(The default value is [0.166, 0.167, 0.167, 0.5]) | String |
| type[type,...] | Specify the Pansharpening method.IHS—Uses Intensity, Hue, and Saturation color space for data fusion.Brovey—Uses the Brovey algorithm based on spectral modeling for data fusion.ESRI—Uses the Esri algorithm based on spectral modeling for data fusion. This is the default.SimpleMean—Uses the averaged value between the red, green, and blue values and the panchromatic pixel value.Gram-Schmidt—Uses the Gram-Schmidt spectral-sharpening algorithm to sharpen multispectral data.(The default value is ESRI) | String |
| sensor[sensor,...] | Specify the sensor name of the input imagery when the pansharpening method is Gram-Schmidt. Supported raster data types include DubaiSat-2, GeoEye-1, GF-1 PMS, GF-2 PMS, IKONOS, Jilin-1, KOMPSAT-2, KOMPSAT-3, Landsat 1-5 MSS, Landsat 7 ETM+, Landsat 8, Pleiades-1, QuickBird, SkySat, SPOT 5, SPOT 6 SPOT 7, TH-01, UltraCam, WorldView-2, WorldView-3, WorldView-4, ZY1-02C PMS, ZY3-CRESDA, ZY3-SASMAC, and UNKNOWN.(The default value is None) | String |

## Code Samples

### Example 1

```python
Pansharpen (pan_raster, ms_raster, {ir_raster}, {fourth_band_of_ms_is_ir}, {weights}, {type}, {sensor})
```

### Example 2

```python
import arcpy

Pansharpen_raster = arcpy.sa.Pansharpen(imagePath1, imagePath2, None, True, [0.166, 0.167, 0.167, 0.5], "Gram-Schmidt", None
```

### Example 3

```python
import arcpy

Pansharpen_raster = arcpy.sa.Pansharpen(imagePath1, imagePath2, None, True, [0.166, 0.167, 0.167, 0.5], "Gram-Schmidt", None
```

---

## PVI

## Summary

Calculates the Perpendicular Vegetation Index (PVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |
| a | The slope of the soil line.(The default value is 0.3) | Double |
| b | The gradient of the soil line.(The default value is 0.5) | Double |

## Code Samples

### Example 1

```python
PVI = (NIR - a * Red - b) / (√(1 + a2))
```

### Example 2

```python
PVI = (NIR - a * Red - b) / (√(1 + a2))
```

### Example 3

```python
PVI (raster, {nir_band_id}, {red_band_id}, {a}, {b})
```

### Example 4

```python
import arcpy

PVI_raster = arcpy.sa.PVI("Landsat8.tif", 5, 4, 0.3, 0.5)
```

### Example 5

```python
import arcpy

PVI_raster = arcpy.sa.PVI("Landsat8.tif", 5, 4, 0.3, 0.5)
```

---

## RadiusFixed

## Summary

Defines a fixed search radius by specifying a distance and a minimum number of points required for analysis. If the required number of points is not found within the specified distance, the search radius will be increased until the specified minimum number of points is found.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| distance | The distance specifies the distance as a radius within which input sample points will be used to perform the interpolation. The value of the radius is expressed in map units. The default radius is five times the cell size of the output raster. | Double |
| minNumberOfPoints | The minNumberOfPoints is an integer defining the minimum number of points to be used to perform the interpolation. If the required number of points is not found within the specified distance, the search distance will be increased until the specified minimum number of points is found.When the search radius needs to be increased, it is done so until the minNumberOfPoints fall within that radius, or the extent of the radius crosses the lower (southern) and/or upper (northern) extent of the output raster. NoData is assigned to all locations that do not satisfy the above condition.(The default value is 0) | Long |

## Code Samples

### Example 1

```python
RadiusFixed ({distance}, {minNumberOfPoints})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRadius = RadiusFixed(80000)
outKriging = Kriging("ca_ozone_pts.shp", "ELEVATION", "SPHERICAL", "", myRadius)
outKriging.save("C:/sapyexamples/output/krigradfix")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRadius = RadiusFixed(80000)
outKriging = Kriging("ca_ozone_pts.shp", "ELEVATION", "SPHERICAL", "", myRadius)
outKriging.save("C:/sapyexamples/output/krigradfix")
```

### Example 4

```python
# Name: RadiusFixed_Ex_02.py
# Description: Uses the RadiusFixed object to execute IDW tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeature = "ca_ozone_pts.shp"

# Create the Radius Object
distance = 15000
minNumPoints = 3
searchRadius = RadiusFixed(distance, minNumPoints)

# Execute IDW
outRadFix = Idw(inFeature, "elevation", 2000, 2, searchRadius)

# Save the output 
outRadFix.save("C:/sapyexamples/output/idwradfix")
```

### Example 5

```python
# Name: RadiusFixed_Ex_02.py
# Description: Uses the RadiusFixed object to execute IDW tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeature = "ca_ozone_pts.shp"

# Create the Radius Object
distance = 15000
minNumPoints = 3
searchRadius = RadiusFixed(distance, minNumPoints)

# Execute IDW
outRadFix = Idw(inFeature, "elevation", 2000, 2, searchRadius)

# Save the output 
outRadFix.save("C:/sapyexamples/output/idwradfix")
```

---

## RadiusVariable

## Summary

Defines a variable search radius by specifing a maximum distance and the number of points for analysis. If the number of points cannot be satisfied within that maximum distance, a smaller number of points will be used.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| numberOfPoints | The numberOfPoints is an integer value specifying the number of nearest input sample points to be used to perform the interpolation. (The default value is 12) | Long |
| maxDistance | The maxDistance specifies the distance, in map units, by which to limit the search for the nearest input sample points. The default value is the length of the extent's diagonal. If the number of points cannot be satisfied within that distance, a smaller number of points will be used. | Double |

## Code Samples

### Example 1

```python
RadiusVariable ({numberOfPoints}, {maxDistance})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRadius = RadiusVariable(12)
outKriging = Kriging("ca_ozone_pts.shp", "ELEVATION", "SPHERICAL", 2000, myRadius, "C:/sapyexamples/output/krigvpradiusv")
outKriging.save("C:/sapyexamples/output/krigradvar")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRadius = RadiusVariable(12)
outKriging = Kriging("ca_ozone_pts.shp", "ELEVATION", "SPHERICAL", 2000, myRadius, "C:/sapyexamples/output/krigvpradiusv")
outKriging.save("C:/sapyexamples/output/krigradvar")
```

### Example 4

```python
# Name: RadiusVariable_Ex_02.py
# Description: Uses the RadiusVariable object to execute IDW tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeature = "ca_ozone_pts.shp"

# Create the Radius Variable
numberOfPoints = 5
maxDistance = 200000
searchRadius = RadiusVariable(numberOfPoints, maxDistance)

# Execute IDW
outIDWRadVar = Idw(inFeature, "elevation", 2000, 3, searchRadius)

# Save the output 
outIDWRadVar.save("C:/sapyexamples/output/idwradvar")
```

### Example 5

```python
# Name: RadiusVariable_Ex_02.py
# Description: Uses the RadiusVariable object to execute IDW tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFeature = "ca_ozone_pts.shp"

# Create the Radius Variable
numberOfPoints = 5
maxDistance = 200000
searchRadius = RadiusVariable(numberOfPoints, maxDistance)

# Execute IDW
outIDWRadVar = Idw(inFeature, "elevation", 2000, 3, searchRadius)

# Save the output 
outIDWRadVar.save("C:/sapyexamples/output/idwradvar")
```

---

## RasterCalculator

## Summary

Provides access to all existing math functions and returns a raster object with the mathematical operation applied.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| input_names[input_names,...] | The user-defined variable names. | String |
| expression | Build an algebraic expression to perform spatial analysis on the input raster. | String |
| extent_type | The spatial extent used to create the output raster.FirstOf—The extent of the first raster variableIntersectionOf—The minimum area common to all input rastersUnionOf—The combined extent of all input rastersLastOf—The extent of the last raster variable(The default value is FirstOf) | String |
| cellsize_type | The cell size used to create the output raster.FirstOf—The cell size of the first raster variableMinOf—The minimum cell size of the input rastersMaxOf—The maximum cell size of the input rastersMeanOf—The average cell size of the input rastersLastOf—The cell size of the last raster variable(The default value is FirstOf) | String |

## Code Samples

### Example 1

```python
RasterCalculator (rasters, input_names, expression, {extent_type}, {cellsize_type})
```

### Example 2

```python
from arcpy.sa import *
out_rc_multi_raster = RasterCalculator(["raster1.tif", "raster2.tif"],
                                       ["x", "y"], "x*y")
out_rc_multi_raster.save("C:/arcpyExamples/raster_rc_multi.tif")
```

### Example 3

```python
from arcpy.sa import *
out_rc_multi_raster = RasterCalculator(["raster1.tif", "raster2.tif"],
                                       ["x", "y"], "x*y")
out_rc_multi_raster.save("C:/arcpyExamples/raster_rc_multi.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set local variables
in_raster1 = "raster1.tif"
in_raster2 = "raster2.tif"

# Excuate RasterCalculator(Minus) function
out_rc_minus_raster = RasterCalculator([in_raster1, in_raster2], ["x", "y"],
                                       "x-y", "", "FirstOf")

# Save the output
out_rc_minus_raster.save("C:/arcpyExamples/raster_rc_minus.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set local variables
in_raster1 = "raster1.tif"
in_raster2 = "raster2.tif"

# Excuate RasterCalculator(Minus) function
out_rc_minus_raster = RasterCalculator([in_raster1, in_raster2], ["x", "y"],
                                       "x-y", "", "FirstOf")

# Save the output
out_rc_minus_raster.save("C:/arcpyExamples/raster_rc_minus.tif")
```

---

## RasterCellIterator

## Summary

Defines an iterator object to iterate through the cells of one or more rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| *args | A dictionary that defines rasters and padding in the following format: {'rasters': [in_rasterobj1, in_rasterobj2, ...], 'padding': padding_factor, 'skipNoData': [in_rasterobj1, in_rasterobj2, ...]}The rasters key is expressed as a list of Raster objects. Each Raster object must be an instance of the arcpy.Raster class.The optional padding key is expressed as an integer. The padding factor expands the internal pixel block size of the raster objects by the value specified. The optional skipNoData key is expressed as a list of rasters specifying cells to be skipped by the iterator. For any given cell, if one or more rasters in this list has a NoData value, that cell would be skipped by the iterator.The rasters in the skipNoData list must be a subset of, or equal to, the rasters list. | Dictionary |

## Code Samples

### Example 1

```python
RasterCellIterator (*args)
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create inRaster raster object
inRaster = arcpy.Raster("C:/arcpyExamples/inputs/elevation.tif")

# Get the raster info object from inRaster
rasInfo = inRaster.getRasterInfo()
# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# The following code shifts inRaster by one cell and writes to outRaster
with arcpy.sa.RasterCellIterator({"rasters":[inRaster, outRaster], "padding":1}) as rci:
    for r, c in rci:
        # Read cell value from inRaster (at upper left corner of the current location)
        v = inRaster[r-1, c-1]
        # Check for NoData
        if math.isnan(v):
            # Write NoData to outRaster
            outRaster[r, c] = math.nan
        else:
            # Write v to outRaster
            outRaster[r, c] = v 

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras01.tif")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create inRaster raster object
inRaster = arcpy.Raster("C:/arcpyExamples/inputs/elevation.tif")

# Get the raster info object from inRaster
rasInfo = inRaster.getRasterInfo()
# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# The following code shifts inRaster by one cell and writes to outRaster
with arcpy.sa.RasterCellIterator({"rasters":[inRaster, outRaster], "padding":1}) as rci:
    for r, c in rci:
        # Read cell value from inRaster (at upper left corner of the current location)
        v = inRaster[r-1, c-1]
        # Check for NoData
        if math.isnan(v):
            # Write NoData to outRaster
            outRaster[r, c] = math.nan
        else:
            # Write v to outRaster
            outRaster[r, c] = v 

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras01.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create a raster info object
rasInfo = arcpy.RasterInfo()

# Create a spatial reference object
spRef = arcpy.SpatialReference(32145)
# Create an extent object
ext = arcpy.Extent(471090.082572495, 208342.353396819, 494670.082572495, 231352.353396819, 0, 0, 0, 0, spRef)

# Initialize raster info object properties
# Set the spatial reference property
rasInfo.setSpatialReference(spRef)
# Set the extent property
rasInfo.setExtent(ext)
# Set the cell size property
rasInfo.setCellSize((30, 30))
# Set the pixel type property
rasInfo.setPixelType("S32")

# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# The following code will create a row (or column) raster
with RasterCellIterator({"rasters":[outRaster], "padding":1}) as rci:
    for r, c in rci:
        # Assign 'r' to outRaster will result in a row raster
        # Assign 'c' to outRaster will result in a column raster.
        outRaster[r, c] = r

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras02.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create a raster info object
rasInfo = arcpy.RasterInfo()

# Create a spatial reference object
spRef = arcpy.SpatialReference(32145)
# Create an extent object
ext = arcpy.Extent(471090.082572495, 208342.353396819, 494670.082572495, 231352.353396819, 0, 0, 0, 0, spRef)

# Initialize raster info object properties
# Set the spatial reference property
rasInfo.setSpatialReference(spRef)
# Set the extent property
rasInfo.setExtent(ext)
# Set the cell size property
rasInfo.setCellSize((30, 30))
# Set the pixel type property
rasInfo.setPixelType("S32")

# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# The following code will create a row (or column) raster
with RasterCellIterator({"rasters":[outRaster], "padding":1}) as rci:
    for r, c in rci:
        # Assign 'r' to outRaster will result in a row raster
        # Assign 'c' to outRaster will result in a column raster.
        outRaster[r, c] = r

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras02.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create inRaster raster object
inStreamRas = arcpy.Raster("C:/arcpyExamples/inputs/streamras.tif")
inFlowDirRas = arcpy.Raster("C:/arcpyExamples/inputs/flowdir.tif")

# Get the raster info object from inRaster
rasInfo = inFlowDirRas.getRasterInfo()
# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# Get flow directions along a stream network
with arcpy.sa.RasterCellIterator({"rasters":[inStreamRas, inFlowDirRas, outRaster], "padding":1, "skipNoData":[inStreamRas]}) as rci:
    for r, c in rci:        
        v = inFlowDirRas[r, c]
        outRaster[r, c] = v 

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras03.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Create inRaster raster object
inStreamRas = arcpy.Raster("C:/arcpyExamples/inputs/streamras.tif")
inFlowDirRas = arcpy.Raster("C:/arcpyExamples/inputs/flowdir.tif")

# Get the raster info object from inRaster
rasInfo = inFlowDirRas.getRasterInfo()
# Create a new raster dataset 
outRaster = arcpy.Raster(rasInfo)

# Get flow directions along a stream network
with arcpy.sa.RasterCellIterator({"rasters":[inStreamRas, inFlowDirRas, outRaster], "padding":1, "skipNoData":[inStreamRas]}) as rci:
    for r, c in rci:        
        v = inFlowDirRas[r, c]
        outRaster[r, c] = v 

# Save the output
outRaster.save("C:/arcpyExamples/outputs/outras03.tif")
```

---

## RasterizeFeatures

## Summary

Converts a polygon, polyline, or point feature class to a raster object.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The raster used to define the cell size and extent for the feature conversion. | Raster |
| feature_class | The point, line, or polygon feature class to convert to a raster object. Supported options include the path to the feature class or a FeatureSet. | String |
| class_index_field | The feature class field to assign values to pixels in the rasterized output. If no field is provided, pixel values will be assigned using the feature class's OBJECTID field. (The default value is None) | String |
| resolve_overlap_method | Specifies the method to assign pixel values in areas where features are overlapping.FIRST—Overlapping areas will be assigned a value from the overlapping feature that is listed first in the feature class table. This is the default.LAST—Overlapping areas will be assigned a value from the overlapping feature that is listed last in the feature class table.SMALLEST—Overlapping areas will be assigned the smallest value from the overlapping features.LARGEST—Overlapping areas will be assigned the largest value from the overlapping features.(The default value is FIRST) | String |

## Code Samples

### Example 1

```python
RasterizeFeatures (raster, feature_class, {class_index_field}, {resolve_overlap_method})
```

### Example 2

```python
from arcpy.sa import *
rasterized_polygons = arcpy.sa.RasterizeFeatures("sample.tif",
	"ParkPolygons", "CarbonQuantity", "SMALLEST")
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 3

```python
from arcpy.sa import *
rasterized_polygons = arcpy.sa.RasterizeFeatures("sample.tif",
	"ParkPolygons", "CarbonQuantity", "SMALLEST")
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# convert regional park features to raster with carbon quantity field
rasterized_polygons = arcpy.sa.RasterizeFeatures(sample_raster,
	"C:/data/MyData.gdb/ParkPolygons", "CarbonQuantity", "SMALLEST")

# save the output
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# convert regional park features to raster with carbon quantity field
rasterized_polygons = arcpy.sa.RasterizeFeatures(sample_raster,
	"C:/data/MyData.gdb/ParkPolygons", "CarbonQuantity", "SMALLEST")

# save the output
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

---

## RegionGrow

## Summary

Groups adjacent pixels depending on the specified radius from the seed point.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| seed_points | The point feature class, serving as the initial seeds for the algorithm.Each seed point corresponds to one entry in the attribute table, which includes values for the maximum growth radius, similarity threshold, and an optional fill value. | String |
| max_growth_radius_field | The field in the attribute table that defines the maximum growth radius, in the image's spatial reference units. | String |
| similarity_threshold_field | The field that defines the similarity threshold, as Euclidean distance in spectral space. | String |
| fill_value_field | The field that defines the fill value for the group of pixels formed from each seed point. In a multiband image, all bands will be assigned this value.(The default value is None) | String |

## Code Samples

### Example 1

```python
RegionGrow (raster, seed_points, max_growth_radius_field, similarity_threshold_field, {fill_value_field})
```

### Example 2

```python
from arcpy.sa import *
out_regiongrow_raster = RegionGrow("mlc.tif", "seeds.shp",
                                   "radius", "similarity")
out_regiongrow_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

### Example 3

```python
from arcpy.sa import *
out_regiongrow_raster = RegionGrow("mlc.tif", "seeds.shp",
                                   "radius", "similarity")
out_regiongrow_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster = "Multispectral_Landsat.tif"
seed_points = "seed_point.shp"
max_growth_radius_field = "radius"
similarity_threshold_field = "similarity"
fill_value_field = "None"

# Apply RegionGrow function
out_regiongrow_raster = RegionGrow(raster, seed_points, max_growth_radius_field,
                                   similarity_threshold_field, fill_value_field)

# Save the output
out_regiongrow_raster.save("C:/arcpyExamples/outputs/Mul_spec_RegionGrow.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster = "Multispectral_Landsat.tif"
seed_points = "seed_point.shp"
max_growth_radius_field = "radius"
similarity_threshold_field = "similarity"
fill_value_field = "None"

# Apply RegionGrow function
out_regiongrow_raster = RegionGrow(raster, seed_points, max_growth_radius_field,
                                   similarity_threshold_field, fill_value_field)

# Save the output
out_regiongrow_raster.save("C:/arcpyExamples/outputs/Mul_spec_RegionGrow.crf")
```

---

## == (Relational Equal To) operator

## Summary

Performs a relational equal-to operation on two inputs on a cell-by-cell basis within the Analysis window.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outEqualTo = Raster("degs") == Raster("negs")
outEqualTo.save("C:/sapyexamples/output/outequalto.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outEqualTo = Raster("degs") == Raster("negs")
outEqualTo.save("C:/sapyexamples/output/outequalto.tif")
```

### Example 3

```python
# Name: Op_EqualTo_Ex_02.py
# Description: Performs a relational equal-to operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute EqualTo
outEqualTo = inRaster1 == inRaster2

# Save the output 
outEqualTo.save("C:/sapyexamples/output/outequalto")
```

### Example 4

```python
# Name: Op_EqualTo_Ex_02.py
# Description: Performs a relational equal-to operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute EqualTo
outEqualTo = inRaster1 == inRaster2

# Save the output 
outEqualTo.save("C:/sapyexamples/output/outequalto")
```

---

## >= (Relational Greater Than Equal To) operator

## Summary

Returns 1 for cells where the first raster is greater than or equal to the second raster and 0 if it is not.

## Usage


## Code Samples

### Example 1

```python
Input1 > Input2, Output = 1
    Input1 = Input2, Output = 0
    Input1 < Input2, Output = 0
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outGTE = Raster("degs") >= Raster("negs")
outGTE.save("C:/sapyexamples/output/outgte.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outGTE = Raster("degs") >= Raster("negs")
outGTE.save("C:/sapyexamples/output/outgte.tif")
```

### Example 4

```python
# Name: Op_GreaterThanEqual_Ex_02.py
# Description: Performs a relational greater-than-equal operation on
#              two inputs on a cell-by-cell basis within the Analysis
#              window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThanEqual
outGTE = inRaster1 >= inRaster2

# Save the output 
outGTE.save("C:/sapyexamples/output/outgte")
```

### Example 5

```python
# Name: Op_GreaterThanEqual_Ex_02.py
# Description: Performs a relational greater-than-equal operation on
#              two inputs on a cell-by-cell basis within the Analysis
#              window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThanEqual
outGTE = inRaster1 >= inRaster2

# Save the output 
outGTE.save("C:/sapyexamples/output/outgte")
```

---

## > (Relational Greater Than) operator

## Summary

Returns 1 for cells where the first raster is greater than the second raster and 0 for cells if it is not.

## Usage


## Code Samples

### Example 1

```python
Input1 > Input2, Output = 1
    Input1 = Input2, Output = 0
    Input1 < Input2, Output = 0
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outGreaterThan = Raster("degs") > Raster("negs")
outGreaterThan.save("C:/sapyexamples/output/outgt.img")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outGreaterThan = Raster("degs") > Raster("negs")
outGreaterThan.save("C:/sapyexamples/output/outgt.img")
```

### Example 4

```python
# Name: Op_GreaterThan_Ex_02.py
# Description: Performs a relational greater-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThan
outGreaterThan = inRaster1 > inRaster2

# Save the output 
outGreaterThan.save("C:/sapyexamples/output/outgt")
```

### Example 5

```python
# Name: Op_GreaterThan_Ex_02.py
# Description: Performs a relational greater-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThan
outGreaterThan = inRaster1 > inRaster2

# Save the output 
outGreaterThan.save("C:/sapyexamples/output/outgt")
```

---

## <= (Relational Less Than Equal To) operator

## Summary

Returns 1 for cells where the first raster is less than or equal to the second raster and 0 where it is not.

## Usage


## Code Samples

### Example 1

```python
Input1 < Input2, Output = 1
    Input1 = Input2, Output = 1
    Input1 > Input2, Output = 0
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outLTE = Raster("degs") <= Raster("negs")
outLTE.save("C:/sapyexamples/output/outlte.img")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outLTE = Raster("degs") <= Raster("negs")
outLTE.save("C:/sapyexamples/output/outlte.img")
```

### Example 4

```python
# Name: Op_LessThanEqual_Ex_02.py
# Description: Performs a relational less-than-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThanEqual
outLTE = inRaster1 <= inRaster2

# Save the output 
outLTE.save("C:/sapyexamples/output/outlte")
```

### Example 5

```python
# Name: Op_LessThanEqual_Ex_02.py
# Description: Performs a relational less-than-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThanEqual
outLTE = inRaster1 <= inRaster2

# Save the output 
outLTE.save("C:/sapyexamples/output/outlte")
```

---

## < (Relational Less Than) operator

## Summary

Returns 1 for cells where the first raster is less than the second raster and 0 if it is not.

## Usage


## Code Samples

### Example 1

```python
Input1 < Input2, Output = 1
    Input1 = Input2, Output = 0
    Input1 > Input2, Output = 0
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outLessThan = Raster("degs") < Raster("negs")
outLessThan.save("C:/sapyexamples/output/outlt.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outLessThan = Raster("degs") < Raster("negs")
outLessThan.save("C:/sapyexamples/output/outlt.tif")
```

### Example 4

```python
# Name: Op_LessThan_Ex_02.py
# Description: Performs a relational less-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThan
outLessThan = inRaster1 < inRaster2

# Save the output 
outLessThan.save("C:/sapyexamples/output/outlt")
```

### Example 5

```python
# Name: Op_LessThan_Ex_02.py
# Description: Performs a relational less-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThan
outLessThan = inRaster1 < inRaster2

# Save the output 
outLessThan.save("C:/sapyexamples/output/outlt")
```

---

## != (Relational Not Equal) operator

## Summary

Returns 1 for cells where the first raster is not equal to the second raster and 0 for cells where it is equal.

## Usage


## Code Samples

### Example 1

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNotEqual = Raster("degs") != Raster("negs")
outNotEqual.save("C:/sapyexamples/output/outne")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outNotEqual = Raster("degs") != Raster("negs")
outNotEqual.save("C:/sapyexamples/output/outne")
```

### Example 3

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/sapyexamples/output/outnotequal")
```

### Example 4

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/sapyexamples/output/outnotequal")
```

---

## Remap

## Summary

Categorizes the pixel values of a raster object into groups with specific values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| input_ranges | Input ranges are specified in pairs: from (inclusive) and to (exclusive). (The default value is None) | Double |
| output_values | The output values of the corresponding input_ranges parameter value.(The default value is None) | Double |
| no_data_ranges | NoData ranges are specified in pairs: from (inclusive) and to (exclusive).(The default value is None) | Double |
| allow_unmatched | Missing values in the reclass table can retain their value or be remapped to NoData or to a replacement value.True—Any pixel from the input raster that is not reclassed in a remap table will retain its value and be written for its location to the output raster.False—Any pixel from the input raster that is not reclassed in a remap table will have its value remapped to NoData or to a replacement value for its location to the output raster. (The default value is True) | Boolean |
| replacement_value | The value that will replace missing or unmatched values in the output when the allow_unmatched parameter is set to False.(The default value is None) | Double |

## Code Samples

### Example 1

```python
Remap (raster, {input_ranges}, {output_values}, {no_data_ranges}, {allow_unmatched}, {replacement_value})
```

### Example 2

```python
from arcpy.sa import *
out_remap_raster = Remap("NomalRaster.tif")
out_remap_raster.save("C:/arcpyExamples/raster_remap.tif")
```

### Example 3

```python
from arcpy.sa import *
out_remap_raster = Remap("NomalRaster.tif")
out_remap_raster.save("C:/arcpyExamples/raster_remap.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set Local Variables
in_raster = "raster.tif"

# Excute Remap function
out_remap_raster = Remap(in_raster, [-5, 0, 0, 5], [-1, 1])

# Save output
out_remap_raster.save("C:/arcpyExamples/outputs/raster_remap.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set Local Variables
in_raster = "raster.tif"

# Excute Remap function
out_remap_raster = Remap(in_raster, [-5, 0, 0, 5], [-1, 1])

# Save output
out_remap_raster.save("C:/arcpyExamples/outputs/raster_remap.tif")
```

---

## RemapValue

## Summary

A list identifying what the individual input values should be reclassified to in an output raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| remapTable[[oldValue, newValue],...] | The remap table to be used to remap the old values to new values. It defines a list to be used to remap the input values. It is a list of lists, with the inner lists being composed of two components. The components are:oldValue—Represents an original value from the base raster (data type: double, long, string).newValue—Is the new reclassified value (data type: long). The oldValue can be numeric or string. The newValue must be integer. | List |

## Code Samples

### Example 1

```python
RemapValue (remapTable)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRemapValue = RemapValue([["Water", 0], ["Wetlands", 0], ["Barrenland", 1], ["Brushtransitional", 2], ["Builtup",3]])
outReclassRV = Reclassify("landuse", "LANDUSE2", myRemapValue)
outReclassRV.save("C:/sapyexamples/output/reclassrv")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myRemapValue = RemapValue([["Water", 0], ["Wetlands", 0], ["Barrenland", 1], ["Brushtransitional", 2], ["Builtup",3]])
outReclassRV = Reclassify("landuse", "LANDUSE2", myRemapValue)
outReclassRV.save("C:/sapyexamples/output/reclassrv")
```

### Example 4

```python
# Name: RemapValue_Ex_02.py
# Description: Uses the RemapValue object to execute Reclassify tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "negs"

# Define the RemapValue Object
myRemapVal = RemapValue([[-3,9],[0,1],[3,-4],[4,5],[5,6],[6,4],[7,-7]])

# Execute Reclassify
outReclassRV = Reclassify(inRaster, "VALUE", myRemapVal, "")

# Save the output 
outReclassRV.save("C:/sapyexamples/output/reclassrevar2")
```

### Example 5

```python
# Name: RemapValue_Ex_02.py
# Description: Uses the RemapValue object to execute Reclassify tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "negs"

# Define the RemapValue Object
myRemapVal = RemapValue([[-3,9],[0,1],[3,-4],[4,5],[5,6],[6,4],[7,-7]])

# Execute Reclassify
outReclassRV = Reclassify(inRaster, "VALUE", myRemapVal, "")

# Save the output 
outReclassRV.save("C:/sapyexamples/output/reclassrevar2")
```

---

## Render

## Summary

Creates a rendered raster object by applying symbology to the referenced raster dataset. This function is useful when displaying data in a Jupyter notebook.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input raster dataset. | Raster |
| rendering_rule | The rendering rules to apply to the input raster. If a color map is not specified, a rendering rule must be specified.The rendering rules can use one or more of the following formats: bands—A list of band indexes to be mapped to an RGB display.For example, to create a natural color composite for Landsat 8 imagery, where band 4 is displayed as red, band 3 as green, and band 2 as blue, use {'bands': [4, 3, 2]}.min and max—A range of values to use to perform a linear stretch on the raster. The minimum and maximum values are used as endpoints for the histogram stretch, and they can be single inputs or a list of values, one pair per band.For example, to perform a linear stretch from pixel value 0 to 100 for a single-band raster, use {'min': 0, 'max': 100}. To perform a linear stretch on a three-band image where each will stretch from a pixel value of 0 to different maximum pixel values, use {'min': 0, 'max': [220,210,180]}.numberOfStandardDeviations—A single value that describes the number of standard deviations to use for a linear stretch. The stretch will be applied between minimum and maximum pixel values defined by the number of standard deviations from the mean.For example, to perform a linear stretch that removes any pixel values beyond two standard deviations from the mean, use {'numberOfStandardDeviations': 2}.gamma—A single value or a list of values (one per band) that defines the amount of gamma correction to apply to control the overall brightness of the raster display. Gamma can also impact the ratios of red to green to blue in the display.For example, to perform a gamma stretch of 0.5, use {'gamma': 0.5}. To perform various gamma stretches on a three-band raster, use {'gamma': [0.5, 2, 1.5]}.rft—A path to a raster function template (.rft.xml) where the stretch is defined by a raster function chain; for example, {'rft': r"C:\StretchFunctions\Remap_and_Stretch.rft.xml"}. | Dictionary |
| colormap | Defines the colors to use for rendering. If a rendering rule is not specified, a color map must be specified.The parameter must use one of the following formats: The name of a color map or color scheme that is supported in ArcGIS Pro; for example, colormap="Red to Green". For a full list of supported color schemes, download the ArcGIS_Pro_ColorSchemes.pdf PDF document.A list of hex color codes, named colors, or both. There are 16 supported named colors: aquablackbluefuchsiagraygreenlimemaroonnavyolivepurpleredsilvertealwhiteyellowFor example, ["#B0C4DE", "blue", "navy"].A dictionary with the following key value pairs: "values": [<pixel_value1>, <pixel_value2>, ... ]"colors": ["<color1>", "<color2", ... ]"labels": ["<label1>", "<label2>", ... ]For example, {"values": [11, 21, 30], "colors": ["#B0C4DE", "green", "gray"], "labels": ["water", "vegetation", "urban"]} | String |

## Code Samples

### Example 1

```python
Render (in_raster, {rendering_rule}, {colormap})
```

### Example 2

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 3

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 4

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 5

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 6

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.sa.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 7

```python
import arcpy
from arcpy.sa import *

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.sa.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 8

```python
import arcpy
from arcpy.sa import *

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

### Example 9

```python
import arcpy
from arcpy.sa import *

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.sa.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

---

## Resample

## Summary

Creates a raster object by changing the spatial resolution of the input raster and sets rules for aggregating or interpolating values across the new pixel sizes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| resampling_type | The method used to change the spatial resolution of the input raster.NearestNeighbor—Performs a nearest neighbor assignment and is the fastest of the interpolation methods. It is used primarily for discrete data, such as a land-use classification, since it will not change the values of the cells. The maximum spatial error will be one-half the cell size.Bilinear—Performs a bilinear interpolation and determines the new value of a cell based on a weighted distance average of the four nearest input cell centers. It is useful for continuous data and will cause some smoothing of the data.Cubic—Performs a cubic convolution and determines the new value of a cell based on fitting a smooth curve through the 16 nearest input cell centers. It is appropriate for continuous data, although it may result in the output raster containing values outside the range of the input raster.Majority—Performs a majority algorithm and determines the new value of the cell based on the most popular values within the filter window. It is mainly used with discrete data, just as the nearest neighbor method; Majority tends to give a smoother result than Nearest. The majority resampling method will find corresponding 4 by 4 cells in the input space that are closest to the center of the output cell and use the majority of the 4 by 4 neighbors.BilinearInterpolationPlus—Uses Bilinear, except the pixels along the edges are defined as NoData (since there are no surrounding pixels for an accurate calculation).BilinearGaussBlur—Applies a Gaussian convolution to the source raster and calculates pixel value using the distance-weighted value of four nearest pixels from the blurred raster.BilinearGaussBlurPlus—Uses BilinearGaussBlur, except the pixels along the edges are defined as NoData (since there are no surrounding pixels for an accurate calculation).Average—Calculates pixel values using the average value of all involved pixels, where the source pixels are covered by the target pixel.Minimum—Calculates pixel value using the minimum value of all involved pixels. If no source pixel exists, no new pixel can be created in the output.Maximum—Calculates pixel value using the maximum value of all involved pixels. If no source pixel exists, no new pixel can be created in the output.VectorAverage—Calculates vector average of magnitude-direction using all involved pixels. This method is only applicable for two band rasters that represent magnitude and direction. It first converts magnitude-direction into U-V, and then it takes the arithmetic average across all involved pixels to get the U-V of the target pixel and converts it back to magnitude-direction.(The default value is None) | String |
| input_cellsize | The cell size of the input raster.(The default value is None) | Double |
| output_cellsize | The cell size of the output raster.(The default value is None) | Double |

## Code Samples

### Example 1

```python
Resample (raster, {resampling_type}, {input_cellsize}, {output_cellsize})
```

### Example 2

```python
Import arcpy

resampled_raster = arcpy.sa.Resample("NAIP_1_meter.tif", "NearestNeighbor", 1, 3)
```

### Example 3

```python
Import arcpy

resampled_raster = arcpy.sa.Resample("NAIP_1_meter.tif", "NearestNeighbor", 1, 3)
```

---

## RTVICore

## Summary

Calculates the Red-Edge Triangulated Vegetation Index (RTVICore) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| redEdge_band_id | The band ID of the red-edge band. The band ID index uses one-based indexing.(The default value is 6) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 3) | Integer |

## Code Samples

### Example 1

```python
RTVICore = (100*(NIR - RedEdge) - 10*(NIR - Green))
```

### Example 2

```python
RTVICore = (100*(NIR - RedEdge) - 10*(NIR - Green))
```

### Example 3

```python
RTVICore (raster, {nir_band_id}, {redEdge_band_id}, {green_band_id})
```

### Example 4

```python
import arcpy

RTVICore_raster = arcpy.sa.RTVICore("Sentinel2.tif",8,5,3)
```

### Example 5

```python
import arcpy

RTVICore_raster = arcpy.sa.RTVICore("Sentinel2.tif",8,5,3)
```

---

## SAVI

## Summary

Calculates the Soil Adjusted Vegetation Index (SAVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| red_band_id | The band ID of the red-edge band. The band ID index uses one-based indexing.(The default value is 6) | Integer |
| l | The amount of green vegetative cover.(The default value is 0.33) | Double |

## Code Samples

### Example 1

```python
SAVI = ((NIR - Red)/(NIR + Red + L)) * (1 + L)
```

### Example 2

```python
SAVI = ((NIR - Red)/(NIR + Red + L)) * (1 + L)
```

### Example 3

```python
SAVI (raster, {nir_band_id}, {red_band_id}, {l})
```

### Example 4

```python
import arcpy

SAVI_raster = arcpy.sa.SAVI("Landsat8.tif",5,4,0.5)
```

### Example 5

```python
import arcpy

SAVI_raster = arcpy.sa.SAVI("Landsat8.tif",5,4,0.5)
```

---

## SegMeanShift

## Summary

Groups adjacent pixels that have similar spectral and spatial characteristics.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| spectral_detail | The relative importance of separating objects based on color characteristics. Valid values range from 0 to 21. Smaller values result in broad classes and more smoothing. A higher value is appropriate when you want to discriminate between features having somewhat similar spectral characteristics.(The default value is None) | Double |
| spatial_detail | The relative importance of separating objects based on spatial characteristics.Valid integer values range from 0 to 21. Smaller values result in broad classes and more smoothing. A higher value is appropriate for discriminating between features that are spatially small and clustered together.(The default value is None) | Integer |
| spectral_radius | The relative importance of separating objects based on color characteristics.Valid values range from 0 to 21. Larger values result in broad classes and more smoothing. A lower value is appropriate when you want to discriminate between features having somewhat similar spectral characteristics.(The default value is None) | Double |
| spatial_radius | The relative importance of separating objects based on spatial characteristics.Valid integer values range from 0 to 21. Larger values result in broad classes and more smoothing. A lower value is appropriate for discriminating between features that are spatially small and clustered together.(The default value is None) | Integer |
| min_num_pixels_per_segment | The minimum segment size, measured in pixels. This value is related to your minimum mapping unit, and will filter out smaller blocks of pixels.(The default value is None) | Integer |
| astype | The output pixel type.(The default value is None) | Double |

## Code Samples

### Example 1

```python
SegMeanShift (raster, spectral_detail, spatial_detail, {spectral_radius}, {spatial_radius}, min_num_pixels_per_segment, {astype})
```

### Example 2

```python
from arcpy.sa import *
out_segmented_raster = SegMeanShift("Multispectral_Landsat.tif")
out_segmented_raster.save("C:/arcpyExamples/outputs/segmeanshift_out.crf")
```

### Example 3

```python
from arcpy.sa import *
out_segmented_raster = SegMeanShift("Multispectral_Landsat.tif")
out_segmented_raster.save("C:/arcpyExamples/outputs/segmeanshift_out.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster = "Multispectral_Landsat.tif"
spectral_detail = 15.5
spatial_detail = 15
spectral_radius = None
spatial_radius = None
min_num_pixels_per_segment = 20

# Apply SegMeanShift function
out_segmented_raster = SegMeanShift(raster, spectral_detail, spatial_detail,
                                    spectral_radius, spatial_radius,
                                    min_num_pixels_per_segment)

# Save the output
out_segmented_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_seg.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
raster = "Multispectral_Landsat.tif"
spectral_detail = 15.5
spatial_detail = 15
spectral_radius = None
spatial_radius = None
min_num_pixels_per_segment = 20

# Apply SegMeanShift function
out_segmented_raster = SegMeanShift(raster, spectral_detail, spatial_detail,
                                    spectral_radius, spatial_radius,
                                    min_num_pixels_per_segment)

# Save the output
out_segmented_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_seg.crf")
```

---

## ShadedRelief

## Summary

Creates a color 3D representation of the terrain by merging the images from the elevation-coded and hillshade methods.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input DEM. | Raster |
| azimuth | Azimuth is the sun's relative position along the horizon (in degrees). This position is indicated by the angle of the sun measured clockwise from due north. An azimuth of 0 degrees indicates north, east is 90 degrees, south is 180 degrees, and west is 270 degrees.(The default value is 315) | Double |
| altitude | Altitude is the sun's angle of elevation above the horizon and ranges from 0 to 90 degrees. A value of 0 degrees indicates that the sun is on the horizon, that is, on the same horizontal plane as the frame of reference. A value of 90 degrees indicates that the sun is directly overhead.(The default value is 45) | Double |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |
| colormap[colormap,...] | The color map used to render the raster. This can be provided as a list or dictionary.(The default value is None) | List |
| colorramp | The name of the color ramp. This can be provided as a string specifying a color ramp name supported in ArcGIS Pro, such as Yellow to Red, or Slope. This can also be provided as a dictionary. For more information, see Color ramp objects.(The default value is Elevation #1) | String |
| slope_type | The inclination of slope can be output as either a value in degrees or percent rise. Specify one of the following: DEGREE, PERCENTRISE, or SCALED. For more information, see Slope function.(The default value is DEGREE) | String |
| ps_power | Accounts for the altitude changes (or scale) as the viewer zooms in and out on the map display. It is the exponent applied to the pixel size term in the equation that controls the rate at which the z-factor changes to avoid significant loss of relief.This parameter is only valid when slope_type is SCALED.(The default value is 0.664) | Double |
| psz_factor | Accounts for changes in scale as the viewer zooms in and out on the map display. The value controls the rate at which the z-factor changes.This parameter is only valid when slope_type is SCALED.(The default value is 0.024) | Double |
| remove_edge_effect | Using this option will avoid any resampling of artifacts that may occur along the edges of a raster. The output pixels along the edge of a raster or next to pixels without a value will be populated with NoData. It is recommended that you use this option only when there are other rasters with overlapping pixels available. When overlapping pixels are available, these areas of NoData will display the overlapping pixel values instead of being blank.False—Bilinear resampling will be applied uniformly to resample the output.True—Bilinear resampling will be used to resample the output, except along the edges of the rasters or next to pixels of NoData. These pixels will be populated with NoData. This will reduce any sharp edge effects that may otherwise occur.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
ShadedRelief (raster, azimuth, altitude, {z_factor}, {colormap}, {colorramp}, {slope_type}, {ps_power}, {psz_factor}, {remove_edge_effect})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# use built-in colorramp slope
colorramp_name = "Slope"

# Execute arcpy.sa.ShadedRelief
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colorramp=colorramp_name, slope_type = "SCALED",
                            ps_power=0.664, psz_factor=0.024, remove_edge_effect=False)
shadedRelief.save("C:/output/shadedrelief_output2.tif")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# use built-in colorramp slope
colorramp_name = "Slope"

# Execute arcpy.sa.ShadedRelief
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colorramp=colorramp_name, slope_type = "SCALED",
                            ps_power=0.664, psz_factor=0.024, remove_edge_effect=False)
shadedRelief.save("C:/output/shadedrelief_output2.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *
import random

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# generate a color map list
color_map = []
for i in range(1, 255):
    # generate random color
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    value = i
    color_map.append([value, red, green, blue])

# Execute Sample
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colormap=315, slope_type = "DEGREE")
shadedRelief.save("C:/output/shadedrelief_output.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *
import random

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# generate a color map list
color_map = []
for i in range(1, 255):
    # generate random color
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    value = i
    color_map.append([value, red, green, blue])

# Execute Sample
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colormap=315, slope_type = "DEGREE")
shadedRelief.save("C:/output/shadedrelief_output.tif")
```

---

## Speckle

## Summary

Creates a raster object by removing speckle and smoothing out noise in radar datasets, while retaining edges and sharp features in the image.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| filter_type | Specifies the filter type that will be used in the smoothing algorithm to remove speckle noise. Lee—The Lee filter will be used, which reduces the speckle noise by applying a spatial filter to each pixel in an image and filters the data based on local statistics calculated within a square window.EnhancedLee—The EnhancedLee filter will be used, which is a refined version of the Lee filter that reduces the speckle noise effectively by preserving image sharpness and detail. This filter requires the damp_factor and nlooks arguments to be set.Frost—The Frost filter will be used, which reduces speckle noise and preserves important image features at the edges with an exponentially damped circularly symmetric filter that uses local statistics within individual filter windows. This filter requires the damp_factor argument to be set. Kuan—The Kuan filter will be used, which follows a similar filtering process to the Lee filter in reducing speckle noise. This filter also applies a spatial filter to each pixel in an image, filtering the data based on local statistics of the centered pixel value that is calculated using the neighboring pixels. The Kuan filter requires the nlooks argument to be set, which controls image smoothing and estimates noise variance. Gamma MAP—A Bayesian analysis and gamma distribution filter will be used to reduce the speckle noise. This filter is useful for reducing speckle while preserving edges.Refined Lee—A spatial filter will be applied to selected pixels, based on local statistics, to reduce the speckle noise. This filter uses a nonsquare filter window to match the direction of edges. It is useful for reducing speckle while preserving edges.(The default value is Lee) | String |
| filter_size | Specifies the size of the filter window in pixels.3x3—The pixel size of the filter window is 3 by 3.5x5—The pixel size of the filter window is 5 by 5.7x7—The pixel size of the filter window is 7 by 7.9x9—The pixel size of the filter window is 9 by 9.11x11—The pixel size of the filter window is 11 by 11.(The default value is 3x3) | String |
| noise_model | Specifies the type of noise that is reducing the quality of the radar image. This argument is only valid when the filter_type argument is set to Lee.Multiplicative—Random signal noise that is multiplied into the relevant signal during capture or transmission is reducing the quality of the image.Additive—Random signal noise that is added into the relevant signal during capture or transmission is reducing the quality of the image.AdditiveAndMultiplicative—A combination of both noise models is reducing the quality of the image.(The default value is Multiplicative) | String |
| noise_var | The noise variance of the radar image.This argument is only valid when the filter_type argument is set to Lee and the noise_model argument is set to Additive or AdditiveAndMultiplicative. (The default value is None) | Double |
| additive_noise_mean | The mean value of additive noise. A larger noise mean value will produce less smoothing, while a smaller value results in more smoothing.This argument is only valid when the filter_type argument is set to Lee and the noise_model argument is set to Additive or AdditiveAndMultiplicative. (The default value is None) | Double |
| multiplicative_noise_mean | The mean value of multiplicative noise. A larger noise mean value will produce less smoothing, while a smaller value results in more smoothing.This argument is only valid when the filter_type argument is set to Lee and the noise_model argument is set to Multiplicative or AdditiveAndMultiplicative.(The default value is 1) | Double |
| nlooks | The number of looks of the image, which controls image smoothing and estimates noise variance. A smaller value results in more smoothing, while a larger value retains more image features.This argument is only valid when the filter_type argument is set to Lee and the noise_model argument is set to Multiplicative, or when the filter_type argument is set to Kuan.(The default value is 1) | Integer |
| damp_factor | The extent of exponential damping effect on filtering. A larger damping value preserves edges better but smooths less, while a smaller value produces more smoothing. This parameter is only valid when the filter_type argument is set to EnhancedLee or Frost.(The default value is None) | Double |

## Code Samples

### Example 1

```python
Speckle (raster, {filter_type}, {filter_size}, {noise_model}, {noise_var}, {additive_noise_mean}, {multiplicative_noise_mean}, {nlooks}, {damp_factor})
```

### Example 2

```python
import arcpy

out_speckle_raster = arcpy.sa.Speckle("Sentinel_1.tif", filter_type="Lee", filter_size="3x3",
                                              noise_model="AdditiveAndMultiplicative", noise_var=0.25,
                                              additive_noise_mean=0, multiplicative_noise_mean=1)
```

### Example 3

```python
import arcpy

out_speckle_raster = arcpy.sa.Speckle("Sentinel_1.tif", filter_type="Lee", filter_size="3x3",
                                              noise_model="AdditiveAndMultiplicative", noise_var=0.25,
                                              additive_noise_mean=0, multiplicative_noise_mean=1)
```

---

## SpectralConversion

## Summary

Applies a matrix to a multiband image to affect the color values of the output.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster.This can be a raster dataset within a mosaic dataset or raster catalog, or a raster dataset outside the mosaic dataset. | Raster |
| conversion_matrix | The matrix used to convert the input raster.The equation used to perform this conversion is as follows:Output Band_R = Weight_P * Band_Cwhere:Band_R is an output band, where R is a number from 1 to the number of output bands.Weight_P is a comma-delimited list of weights, 1 for each input band. The sum of the weights for each band should equal 1.Band_C is the input image, where C is a number from 1 to the number of bands of the input image. | Raster |

## Code Samples

### Example 1

```python
SpectralConversion (raster, conversion_matrix)
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
from arcpy.sa import *
out_raster = SpectralConversion("3bands_raster",
                                [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8])
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

### Example 5

```python
from arcpy.sa import *
out_raster = SpectralConversion("3bands_raster",
                                [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8])
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "3bands_raster"
in_conversion_matrix =  [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8]

# Execute SpectralConversion function
out_raster = SpectralConversion(in_raster, in_conversion_matrix)
#Output band 1 = (0.1 * InputBand1) + (0.9 * InputBand2) +(0 * InputBand3)
#Output band 2 = (0.3 * InputBand1) + (0 * InputBand2) +(0.7 * InputBand3)
#Output band 3 = (0.1 * InputBand1) + (0.1 * InputBand2) +(0.8 * InputBand3)

# Save output
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "3bands_raster"
in_conversion_matrix =  [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8]

# Execute SpectralConversion function
out_raster = SpectralConversion(in_raster, in_conversion_matrix)
#Output band 1 = (0.1 * InputBand1) + (0.9 * InputBand2) +(0 * InputBand3)
#Output band 2 = (0.3 * InputBand1) + (0 * InputBand2) +(0.7 * InputBand3)
#Output band 3 = (0.1 * InputBand1) + (0.1 * InputBand2) +(0.8 * InputBand3)

# Save output
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

---

## SRre

## Summary

Calculates the Red-Edge Simple Ratio (SRre) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 7) | Integer |
| redEdge_band_id | The band ID of the red-edge band. The band ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
SRre = NIR / RedEdge
```

### Example 2

```python
SRre = NIR / RedEdge
```

### Example 3

```python
SRre (raster, {nir_band_id}, {redEdge_band_id})
```

### Example 4

```python
import arcpy

SRre_raster = arcpy.sa.SRre("Sentinel2.tif",8,6)
```

### Example 5

```python
import arcpy

SRre_raster = arcpy.sa.SRre("Sentinel2.tif",8,6)
```

---

## Statistics

## Summary

Calculates statistics for each cell of an image based on a defined focal neighborhood.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster on which to perform focal statistics. | Raster |
| kernel_columns | The number of pixel columns to use in your focal neighborhood dimension.(The default value is 3) | Integer |
| kernel_rows | The number of pixel rows to use in your focal neighborhood dimension.(The default value is 3) | Integer |
| stat_type | Specify the type of statistics to calculate.max— Calculates the maximum value of the pixels within the neighborhood.mean— Calculates the average value of the pixels within the neighborhood. This is the default.min— Calculates the minimum value of the pixels within the neighborhood.standarddeviation—Calculates the standard deviation value of the pixels within the neighborhood.median—Calculates the median value of the pixels within the neighborhood.majority— Calculates the majority value, or the value that occurs most frequently, of the pixels within the neighborhood.minority— Calculates the minority value, or the value that occurs least frequently, of the pixels within the neighborhood.(The default value is None) | String |
| fill_no_data_only | Specify whether NoData values are ignored in the analysis. True—Fills NoData pixels only. This is the default.False—NoData pixels will not be filled.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Statistics (raster, kernel_columns, kernel_rows, stat_type, {fill_no_data_only})
```

### Example 2

```python
from arcpy.sa import *
LandCover_filled = arcpy.sa.Statistics("LandCover.tif", 5, 5, "majority", True)
LandCover_filles.save("LandCover_majority_5_by_5.tif")
```

### Example 3

```python
from arcpy.sa import *
LandCover_filled = arcpy.sa.Statistics("LandCover.tif", 5, 5, "majority", True)
LandCover_filles.save("LandCover_majority_5_by_5.tif")
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/statistics_example/data"

# Set local variables
inRaster = "elevation.tif"
kernel_columns=3
kernel_rows=3
stat_type="Mean"
fill_no_data_only = False

# for each pixel, calculate the average value of pixels within its neighborhood. the neighborhood size is 5x5
output = Statistics(imagePath1, kernel_columns, kernel_rows, stat_type, fill_no_data_only)
output.save("statistics_mean_5_by_5.tif")
```

### Example 5

```python
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/statistics_example/data"

# Set local variables
inRaster = "elevation.tif"
kernel_columns=3
kernel_rows=3
stat_type="Mean"
fill_no_data_only = False

# for each pixel, calculate the average value of pixels within its neighborhood. the neighborhood size is 5x5
output = Statistics(imagePath1, kernel_columns, kernel_rows, stat_type, fill_no_data_only)
output.save("statistics_mean_5_by_5.tif")
```

---

## StatisticsHistogram

## Summary

Computes the statistics and histogram of a raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| statistics | List of statistical information, based on predefined statistics for each band. Statistics specified for a single-band raster are, for example: statistics = [{"min": 0, "max": 23.06, mean": 4.547517, "standardDeviation": 2.6870, "count": 10000, "median": 5, "mode": 6}].Statistics specified for a three-band raster are, for example: statistics = [{"min": 0, "max": 23.06, "mean": 4.547517, "standardDeviation": 2.6870, "count": 10000, "median": 5, "mode": 6}, {"min":2, "max": 25, "mean": 5.32, "standardDeviation": 3.42, "count": 10000, "median": 6, "mode": 6}, {"min": 5, "max": 53.06, "mean": 35.23, "standardDeviation": 6.3270, "count": 10000, "median": 36, "mode": 6}]. | List |
| histogram | Dictionary of histogram information, based on predefined histogram for each band.Enter the dictionary of histogram information using the example below:{ "rasterFunction": "StatisticsHistogram", "rasterFunctionArguments": { "histograms": [{ "size": 256, "min": 0, "max": 23.064547032777931, "counts": [559, 172, 217, ... //256 elements for each of the bins in this example ] }] | Dictionary |

## Code Samples

### Example 1

```python
StatisticsHistogram (raster, statistics, histogram)
```

### Example 2

```python
{
  "rasterFunction": "StatisticsHistogram",
  "rasterFunctionArguments": {
    "histograms": [{
      "size": 256,
      "min": 0,
      "max": 23.064547032777931,
      "counts": [559,
        172,
        217,
        ... //256 elements for each of the bins in this example
     ]
   }]
```

### Example 3

```python
{
  "rasterFunction": "StatisticsHistogram",
  "rasterFunctionArguments": {
    "histograms": [{
      "size": 256,
      "min": 0,
      "max": 23.064547032777931,
      "counts": [559,
        172,
        217,
        ... //256 elements for each of the bins in this example
     ]
   }]
```

### Example 4

```python
import arcpy

StatisticsHistogram_raster = arcpy.sa.StatisticsHistogram(imagePath1, [-4.514, 4.338, 0.0043, 1.0], None)
```

### Example 5

```python
import arcpy

StatisticsHistogram_raster = arcpy.sa.StatisticsHistogram(imagePath1, [-4.514, 4.338, 0.0043, 1.0], None)
```

---

## Stretch

## Summary

Enhances an image by changing properties such as brightness, contrast, and gamma through multiple stretch types based on statistics.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| stretch_type[stretch_type,...] | Specify the type of stretch to apply to the image.None—No stretch method will be applied, even if statistics exist.StdDev—Uses the Brovey algorithm based on spectral modeling for data fusion. Requires the number of standard deviations (num_stddev) to be specified, statistics to be computed, or DRA (dra) set to True.Histogram—Apply a histogram equalization stretch. Requires the source dataset to have histograms computed, or DRA set to True.MinMax—Applies a linear stretch based on the output minimum and output maximum pixel values, which are used as the endpoints for the histogram. Requires statistics to be computed, or DRA (dra) to be set to True.PercentClip—Applies a linear stretch between the defined percent clip minimum and percent clip maximum pixel values.Sigmoid—Places all of the pixels in the image along a sigmoid function (an S-shaped curve). (The default value is 0) | String |
| min | Set the lowest pixel value for the output histogram.The output minimum (min) and output maximum (max) will set the range of values that will then be stretched.(The default value is None) | Double |
| max | Set the highest pixel value for the output histogram.The output maximum (max) and output minimum (min) will set the range of values that will then be stretched.(The default value is None) | Double |
| num_stddev | Specify the n value for the number of standard deviations to use. This method is used to emphasize how much feature values vary from the mean value; it is best when used on normally distributed data. (The default value is None) | Double |
| statistics[statistics,...] | By default, the statistics used are retrieved from the data; however, any statistic values you enter in this parameter will be used instead.Statistics are specified as: [[<min>, <max>, <mean>, <standardDeviation>] [<min>, <max>, <mean>, <standardDeviation>] [<min>, <max>, <mean>, <standardDeviation>]] (The default value is None) | Double |
| dra | Calculate statistics from only the pixels displayed on your screen. The statistics parameter is ignored when DRA is True.True—Dynamic Range Adjustment (dra) will be computed.False—Dynamic Range Adjustment (dra) will not be computed.(The default value is None) | Boolean |
| min_percent | Specify the percentage of the low values to exclude when the PercentClip stretch is specified.Valid values range from 0 through 99.(The default value is None) | Double |
| max_percent | Specify the percentage of the high values to exclude when the PercentClip stretch is specified.Valid values range from 0 through 99.(The default value is None) | Double |
| gamma | Specify gamma values for each band to apply to the image.For example, a three-band image would have three values, such as [<gamma1>, <gamma2>, <gamma3>].(The default value is None) | Double |
| compute_gamma | Calculates the best gamma value to render the exported image based on an empirical model.True—Gamma values for the image are computed.False—Gamma values for the image are not computed.(The default value is None) | Boolean |
| sigmoid_strength_level | Determines how much of the sigmoidal function will be used in the stretch. A low value such as 1 will only use the middle portion of the curve, which tends to produce dull and faint colors. A high value such as 6 will use the entire curve, which tends to produce bold and sharp colors. The valid range is 1 through 6.(The default value is None) | Integer |

## Code Samples

### Example 1

```python
Stretch (raster, stretch_type, min, max, num_stddev, statistics, dra, {min_percent}, max_percent, {gamma}, {compute_gamma}, sigmoid_strength_level)
```

### Example 2

```python
import arcpy

Stretch_raster = arcpy.sa.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
```

### Example 3

```python
import arcpy

Stretch_raster = arcpy.sa.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
```

---

## Subset

## Summary

Creates a raster object that is a subset of the input multidimensional raster based on selected variables and dimension intervals.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input multidimensional raster dataset. | Raster |
| variables[variables,...] | A variable name or a list of variable names to be included in the output raster. If not specified, all variables will be included. | String |
| dimension_definitions | The dimension interval used to subset the multidimensional raster. This parameter is passed as a dictionary in which the key:value pairs are described as dimension_name:dimension interval. The key is the name of the dimension along which you wish to subset, and the value is the dimension interval. The dimension interval must use one of the following formats: A single dimension input.For example, to subset variables only at the depth of 0, use {"depth": 0 }.A tuple containing the minimum and maximum dimension values.For example, to subset variables from a depth of 0 to 100, use {"depth": (-100,0)}. A tuple containing minimum and maximum dimension values, an increment size and an increment unit.For example, to subset variables from the year 1980 until the end of the time series, extracting the first day of every year, use {"StdTime": ('1980-01-01T12:00:00', None, 1, 'year')}.To subset variables with the time dimension 1980 to 2000, extracting January of every year, use {"StdTime": ('1980-01-01T12:00:00', 1980-31-01T12:00:00', 1, 'year')}.A list containing any of the above. You can include multiple single-dimension inputs and multiple minimum and maximum ranges.For example, to subset variables at depths of 0, 50, and 200, use {"depth": [0, -50, -200]}.For example, to subset variables from a depth of 0 to 100 and also at a depth of 500, use {"depth": [-500, (-100, 0)]}. | Dictionary |

## Code Samples

### Example 1

```python
Subset (in_raster, {variables}, {dimension_definitions})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.sa import *

in_raster = Raster('C:/sapyexamples/data/ClimateData_Daily.nc', True)

# Select two variables: precipitation and water temperature 
out_subset_raster1 = Subset(in_raster, variables = ['precip', 'water_temp'])
print(out_subset_raster1.variables)

# Filter variables that have the Depth dimension and where depth=0.
# For variables that do not have dimension depth, all slices are selected.
out_subset_raster2 = Subset(in_raster, dimension_definitions = {'depth' : 0})   
print(out_subset_raster2.variables)

# Select water temperature data on the 1st of every January
out_subset_raster3 = Subset(
	in_raster, variables = 'water_temp', 
	dimension_definitions = {'time': 
	('1980-01-01T12:00:00', None, 1, 'year')})   
print(out_subset_raster3.variables)

# Select surface water temperature in January 1980
out_subset_raster4 = Subset(
	in_raster, variables = 'water_temp', 
	dimension_definitions  = {'StdTime': 
	('1980-01-01T12:00:00', '1980-01-31T12:00:00'), 'depth': 0})
print(out_subset_raster4.mdinfo)

# Save the water temperature in January 1980
out_subset_raster4.save("C:/sapyexamples/output/Jan1980_watertemp.crf")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.sa import *

in_raster = Raster('C:/sapyexamples/data/ClimateData_Daily.nc', True)

# Select two variables: precipitation and water temperature 
out_subset_raster1 = Subset(in_raster, variables = ['precip', 'water_temp'])
print(out_subset_raster1.variables)

# Filter variables that have the Depth dimension and where depth=0.
# For variables that do not have dimension depth, all slices are selected.
out_subset_raster2 = Subset(in_raster, dimension_definitions = {'depth' : 0})   
print(out_subset_raster2.variables)

# Select water temperature data on the 1st of every January
out_subset_raster3 = Subset(
	in_raster, variables = 'water_temp', 
	dimension_definitions = {'time': 
	('1980-01-01T12:00:00', None, 1, 'year')})   
print(out_subset_raster3.variables)

# Select surface water temperature in January 1980
out_subset_raster4 = Subset(
	in_raster, variables = 'water_temp', 
	dimension_definitions  = {'StdTime': 
	('1980-01-01T12:00:00', '1980-01-31T12:00:00'), 'depth': 0})
print(out_subset_raster4.mdinfo)

# Save the water temperature in January 1980
out_subset_raster4.save("C:/sapyexamples/output/Jan1980_watertemp.crf")
```

---

## Sultan

## Summary

Calculates Sultan's formula from a six-band 8-bit raster object and returns a three-band 8-bit raster object.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| band1_id | The band index of Band 1.The band ID index uses one-based indexing.(The default value is 1) | Integer |
| band3_id | The band index of Band 3.The band ID index uses one-based indexing.(The default value is 3) | Integer |
| band4_id | The band index of Band 4.The band ID index uses one-based indexing.(The default value is 4) | Integer |
| band5_id | The band index of Band 5.The band ID index uses one-based indexing.(The default value is 5) | Integer |
| band6_id | The band index of Band 6.The band ID index uses one-based indexing.(The default value is 6) | Integer |

## Code Samples

### Example 1

```python
Band 1 = (Band5 / Band6) x 100
```

### Example 2

```python
Band 1 = (Band5 / Band6) x 100
```

### Example 3

```python
Band 2 = (Band5 / Band1) x 100
```

### Example 4

```python
Band 2 = (Band5 / Band1) x 100
```

### Example 5

```python
Band 3 = (Band3 / Band4) x (Band5 / Band4) x 100
```

### Example 6

```python
Band 3 = (Band3 / Band4) x (Band5 / Band4) x 100
```

### Example 7

```python
Sultan (raster, {band1_id}, {band3_id}, {band4_id}, {band5_id}, {band6_id})
```

### Example 8

```python
import arcpy

Sultan_raster = arcpy.sa.Sultan("LandsatETM.tif",1,3,4,5,6)
```

### Example 9

```python
import arcpy

Sultan_raster = arcpy.sa.Sultan("LandsatETM.tif",1,3,4,5,6)
```

---

## TasseledCap

## Summary

Creates a raster object by applying a tasseled cap transformation on an input raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |

## Code Samples

### Example 1

```python
TasseledCap (raster)
```

### Example 2

```python
import arcpy

TasseledCap_raster = arcpy.sa.TasseledCap("Worldview2.tif")
```

### Example 3

```python
import arcpy

TasseledCap_raster = arcpy.sa.TasseledCap("Worldview2.tif")
```

---

## TfExponential

## Summary

Defines an Exponential transformation function which is determined from the shift and base factor shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| shift | Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.The shift can be positive or negative.(The default value is None) | Double |
| baseFactor | A multiplier that controls how steep the Exponential function increases. The larger the multiplier, the steeper the curve will be at the larger input values. There is a close connection between the base factor and the base of the Exponential function. A baseFactor of 1 equals the natural exponential (ex).(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfExponential ({shift}, {baseFactor}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfExponential(30, 0.00035, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfex1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfExponential(30, 0.00035, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfex1")
```

### Example 4

```python
# Name: TfExponential_Ex_02.py
# Description: Rescales input raster data using an Exponential function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfExponential object
shift = 30
basefactor = 0.00035
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfExponential(shift, basefactor, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfex2")
```

### Example 5

```python
# Name: TfExponential_Ex_02.py
# Description: Rescales input raster data using an Exponential function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfExponential object
shift = 30
basefactor = 0.00035
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfExponential(shift, basefactor, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfex2")
```

---

## TfGaussian

## Summary

Defines a Gaussian transformation function which is determined from the midpoint and spread shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value that defines the highest point of the Gaussian transformation function curve. If the midpoint value is between the lower and upper threshold, input cell locations with the corresponding value will receive the toScale evaluation scale value on the output raster.(The default value is None) | Double |
| spread | Defines the spread of the Gaussian function that controls the steepness of the decay of the function from the midpoint. The spread generally ranges from 0.01 to 1; the larger the value results in a steeper decay from the midpoint.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfGaussian ({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("solar", TfGaussian(180, 0.0004, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfga1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("solar", TfGaussian(180, 0.0004, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfga1")
```

### Example 4

```python
# Name: TfGaussian_Ex_02.py
# Description: Rescales input raster data using a Gaussian function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar"

# Create the TfGaussian object
midpoint = 180
spread = 0.0004
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfGaussian(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfga2")
```

### Example 5

```python
# Name: TfGaussian_Ex_02.py
# Description: Rescales input raster data using a Gaussian function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar"

# Create the TfGaussian object
midpoint = 180
spread = 0.0004
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfGaussian(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfga2")
```

---

## TfLarge

## Summary

Defines a Large transformation function which is determined from the midpoint and spread shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | Defines the transition point of the transformation function where the curve becomes more convex for the values lesser than the midpoint and more concave for values greater than the midpoint. Shifting the midpoint less than the midpoint of the input data alters the transition point, resulting in an increase in the range of the larger values above the midpoint being more preferred, with the preference increasing at a faster rate.The midpoint cannot equal 0.(The default value is None) | Double |
| spread | Defines the spread of the Large transformation function that controls how quickly the function values increase and decrease from the midpoint. The spread generally ranges from 1 to 10; the larger the value results in a steeper distribution around the midpoint.The spread must be > 0.(The default value is 5) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfLarge ({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfLarge(4075, 4.5, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfla1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfLarge(4075, 4.5, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfla1")
```

### Example 4

```python
# Name: TfLarge_Ex_02.py
# Description: Rescales input raster data using a Large function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfLarge object
midpoint = 4075
spread = 4.5
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLarge(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfla2")
```

### Example 5

```python
# Name: TfLarge_Ex_02.py
# Description: Rescales input raster data using a Large function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfLarge object
midpoint = 4075
spread = 4.5
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLarge(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfla2")
```

---

## TfLinear

## Summary

Defines a Linear transformation function which is determined from the minimum and maximum shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| minimum | One of two points the Linear transformation function must pass through. If the minimum value is less than the maximum, the linear function will have a positive slope. If the minimum value is greater than the maximum, the linear function will have a negative slope. The minimum cannot equal the maximum.(The default value is None) | Double |
| maximum | One of two points the Linear function must pass through. If the maximum value is greater than the minimum, the linear function will have a positive slope. If the maximum value is less than the minimum, the linear function will have a negative slope.The minimum cannot equal the maximum.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfLinear ({minimum}, {maximum}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLinear(421, 4450, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfli1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLinear(421, 4450, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfli1")
```

### Example 4

```python
# Name: TfLinear_Ex_02.py
# Description: Rescales input raster data using a Linear function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLinear object
minimum = 421
maximum = 4450
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLinear(minimum, maximum, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfli2")
```

### Example 5

```python
# Name: TfLinear_Ex_02.py
# Description: Rescales input raster data using a Linear function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLinear object
minimum = 421
maximum = 4450
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLinear(minimum, maximum, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfli2")
```

---

## TfLogarithm

## Summary

Defines a Logarithm transformation function which is determined from the shift and factor shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| shift | Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.By default, the shift adjusts the function so it begins at the lowerThreshold (or very close). As a result, the function will be applied to 0 (the shifted input value) with the function being constrained between the lower and upper thresholds. A shift can be applied so the low input values do not dramatically increase the range of the function values; therefore, the final output evaluation scale maintains the general function shape.The shift can be positive or negative.(The default value is None) | Double |
| factor | The multiplier to apply to the shifted input values. The factor alters the rise of the Logarithm curve.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfLogarithm ({shift}, {factor}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLogarithm(450, 6.25, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletflo1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLogarithm(450, 6.25, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletflo1")
```

### Example 4

```python
# Name: TfLogarithm_Ex_02.py
# Description: Rescales input raster data using an Logarithm function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLogarithm object
shift = 450
factor = 6.25
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogarithm(shift, factor, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletflg2")
```

### Example 5

```python
# Name: TfLogarithm_Ex_02.py
# Description: Rescales input raster data using an Logarithm function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLogarithm object
shift = 450
factor = 6.25
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogarithm(shift, factor, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletflg2")
```

---

## TfLogisticDecay

## Summary

Defines a Logistic Decay transformation function which is determined from the minimum, maximum, and y intercept percent shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| minimum | The starting point for the LogisticDecay transformation function.The minimum must be less than the maximum.(The default value is None) | Double |
| maximum | The ending point for the LogisticDecay transformation function.The minimum must be less than the maximum.(The default value is None) | Double |
| yInterceptPercent | Determines the value range in the decreasing portion of the logistic decay curve. The greater the yInterceptPercent, the smaller the input value range will be in the decay section of the curve; however, the preference for the values will decrease at a faster rate. A larger yInterceptPercent results in a more pronounced logistic decay curve.The yInterceptPercent must be between 50 and 100.(The default value is 99.0) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfLogisticDecay ({minimum}, {maximum}, {yInterceptPercent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLogisticDecay(421, 4450, 75, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfld1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfLogisticDecay(421, 4450, 75, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfld1")
```

### Example 4

```python
# Name: TfLogisticDecay_Ex_02.py
# Description: Rescales input raster data using a LogisticDecay function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLogisticDecay object
minimum = 421
maximum = 4450
yintercept = 75
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogisticDecay(minimum, maximum, yintercept, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfld2")
```

### Example 5

```python
# Name: TfLogisticDecay_Ex_02.py
# Description: Rescales input raster data using a LogisticDecay function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfLogisticDecay object
minimum = 421
maximum = 4450
yintercept = 75
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogisticDecay(minimum, maximum, yintercept, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfld2")
```

---

## TfLogisticGrowth

## Summary

Defines a Logistic Growth transformation function which is determined from the minimum, maximum, and y intercept percent shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| minimum | The starting point for the LogisticGrowth transformation function.The minimum must be less than the maximum.(The default value is None) | Double |
| maximum | The ending point for the LogisticGrowth transformation function. The minimum must be less than the maximum.(The default value is None) | Double |
| yInterceptPercent | Determines the value range in the increasing portion of the logistic growth curve. The smaller the yInterceptPercent, the smaller the input value range will be in the growth section of the curve; however, the preference for the values will increase at a faster rate. A smaller yInterceptPercent results in a more pronounced logistic growth curve.The yInterceptPercent must be between 0 and 50.(The default value is 1.0) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting. (The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfLogisticGrowth ({minimum}, {maximum}, {yInterceptPercent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("biomass", TfLogisticGrowth(30, 412000, 15, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletflg1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("biomass", TfLogisticGrowth(30, 412000, 15, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletflg1")
```

### Example 4

```python
# Name: TfLogisticGrowth_Ex_02.py
# Description: Rescales input raster data using a LogisticGrowth function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "biomass"

# Create the TfLogisticGrowth object
minimum = 30
maximum = 412000
yintercept = 15
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogisticGrowth(minimum, maximum, yintercept, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletflg2")
```

### Example 5

```python
# Name: TfLogisticGrowth_Ex_02.py
# Description: Rescales input raster data using a LogisticGrowth function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "biomass"

# Create the TfLogisticGrowth object
minimum = 30
maximum = 412000
yintercept = 15
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfLogisticGrowth(minimum, maximum, yintercept, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletflg2")
```

---

## TfMSLarge

## Summary

Defines an MSLarge transformation function which is determined from the mean multiplier and standard deviation multiplier shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| meanMultiplier | The multiplier for the mean of the input values in the MSLarge function equation.The meanMultiplier must be greater than 0.(The default value is 1.0) | Double |
| STDMultiplier | The multiplier for the standard deviation of the input values in the MSLarge function equation.The STDMultiplier must be greater than 0.(The default value is 1.0) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
f(x) = 1 - (b * s) / (x - (a * m) + (b * s))
```

### Example 2

```python
f(x) = 1 - (b * s) / (x - (a * m) + (b * s))
```

### Example 3

```python
TfMSLarge (meanMultiplier, STDMultiplier, lowerThreshold, valueBelowThreshold, upperThreshold, valueAboveThreshold)
```

### Example 4

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("biomass", TfMSLarge(1.2, 1.25, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfml1")
```

### Example 5

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("biomass", TfMSLarge(1.2, 1.25, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfml1")
```

### Example 6

```python
# Name: TfMSLarge_Ex_02.py
# Description: Rescales input raster data using a MSLarge function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "biomass"

# Create the TfMSLarge object
meanmult = 1.2
stdmult = 1.25
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfMSLarge(meanmult, stdmult, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfml2")
```

### Example 7

```python
# Name: TfMSLarge_Ex_02.py
# Description: Rescales input raster data using a MSLarge function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "biomass"

# Create the TfMSLarge object
meanmult = 1.2
stdmult = 1.25
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfMSLarge(meanmult, stdmult, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfml2")
```

---

## TfMSSmall

## Summary

Defines an MSSmall transformation function which is determined from the mean multiplier and standard deviation multiplier shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| meanMultiplier | The multiplier for the mean of the input values in the MSSmall function equation.The meanMultiplier must be greater than 0.(The default value is 1.0) | Double |
| STDMultiplier | The multiplier for the standard deviation of the input values in the MSSmall function equation.The STDMultiplier must be greater than 0.(The default value is 1.0) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
f(x) = (b * s) / (x - (a * m) + (b * s))
```

### Example 2

```python
f(x) = (b * s) / (x - (a * m) + (b * s))
```

### Example 3

```python
TfMSSmall ({meanMultiplier}, {STDMultiplier}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 4

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfMSSmall(1.5, 1.75, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfms1")
```

### Example 5

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfMSSmall(1.5, 1.75, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfms1")
```

### Example 6

```python
# Name: TfMSSmall_Ex_02.py
# Description: Rescales input raster data using a MSSmall function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfMSSmall object
meanmult = 1.5
stdmult = 1.75
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfMSSmall(meanmult, stdmult, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfms2")
```

### Example 7

```python
# Name: TfMSSmall_Ex_02.py
# Description: Rescales input raster data using a MSSmall function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfMSSmall object
meanmult = 1.5
stdmult = 1.75
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfMSSmall(meanmult, stdmult, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfms2")
```

---

## TfNear

## Summary

Defines a Near transformation function which is determined from the midpoint and spread shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | The user-defined value that defines the highest point of the Near transformation function curve. If the midpoint value is between the lower and upper threshold, input cell locations with the corresponding value will receive the toScale evaluation scale value on the output raster.(The default value is None) | Double |
| spread | Defines the spread of the Near function that controls the steepness of the decay of the function from the midpoint. The spread generally ranges from 0.001 to 1; the larger the value results in a steeper decay from the midpoint.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfNear ({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("solar", TfNear(180, 0.002, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfne1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("solar", TfNear(180, 0.002, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfne1")
```

### Example 4

```python
# Name: TfNear_Ex_02.py
# Description: Rescales input raster data using a Near function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar"

# Create the TfNear object
midpoint = 180
spread = 0.002
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfNear(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfne2")
```

### Example 5

```python
# Name: TfNear_Ex_02.py
# Description: Rescales input raster data using a Near function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar"

# Create the TfNear object
midpoint = 180
spread = 0.002
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfNear(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfne2")
```

---

## TfPower

## Summary

Defines a Power transformation function which is determined from the shift and exponent shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| shift | Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.By default, the shift adjusts the function so it begins at the lowerThreshold (or very close). As a result, the function will be applied to 0 (the shifted input value) with the function being constrained between the lower and upper thresholds. The shift can be positive or negative.(The default value is None) | Double |
| exponent | The power to raise the input values in the transformation function. As the exponent increases, the preference for the larger input values increases more rapidly.The exponent cannot equal 0 or 1.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfPower ({shift}, {exponent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfPower(-2, 0.27, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfpo1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfPower(-2, 0.27, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfpo1")
```

### Example 4

```python
# Name: TfPower_Ex_02.py
# Description: Rescales input raster data using an Power function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfPower object
shift = -2
exponent = 0.27
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfPower(shift, exponent, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfpo2")
```

### Example 5

```python
# Name: TfPower_Ex_02.py
# Description: Rescales input raster data using an Power function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfPower object
shift = -2
exponent = 0.27
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfPower(shift, exponent, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfpo2")
```

---

## TfSmall

## Summary

Defines a Small transformation function which is determined from the midpoint and spread shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| midpoint | Defines the transition point of the transformation function where the curve becomes more concave for the values lesser than the midpoint and more convex for values greater than the midpoint. Shifting the midpoint greater than the midpoint of the input data alters the transition point, resulting in an increase in the range of the smaller values below the midpoint being more preferred, with the preference increasing at a slower rate.The midpoint value cannot equal 0.(The default value is None) | Double |
| spread | Defines the spread of the Small transformation function that controls how quickly the function values increase and decrease from the midpoint. The spread generally ranges from 1 to 10; the larger the value results in a steeper distribution around the midpoint.The spread value must be greater than 0.(The default value is 5.0) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfSmall ({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfSmall(2475, 4.5, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfsm1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("elevation", TfSmall(2475, 4.5, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfsm1")
```

### Example 4

```python
# Name: TfSmall_Ex_02.py
# Description: Rescales input raster data using a Small function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfSmall object
midpoint = 2475
spread = 4.5
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfSmall(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfsm2")
```

### Example 5

```python
# Name: TfSmall_Ex_02.py
# Description: Rescales input raster data using a Small function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfSmall object
midpoint = 2475
spread = 4.5
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfSmall(midpoint, spread, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfsm2")
```

---

## TfSymmetricLinear

## Summary

Defines a Symmetric Linear transformation function which is determined from the minimum and maximum shape–controlling parameters as well as the lower and upper threshold that identify the range within which to apply the function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| minimum | The starting point for the Symmetric Linear transformation function. The point of inflection to mirror the function is determined by the midpoint of the minimum and maximum. If the minimum value is less than the maximum, the linear function will have a positive slope. If the minimum value is greater than the maximum, the linear function will be a negative slope.The minimum cannot equal the maximum.(The default value is None) | Double |
| maximum | The ending point for the Symmetric Linear transformation function. The point of inflection to mirror the function is determined by the midpoint of the minimum and maximum. If the minimum value is less than the maximum, the linear function will have a positive slope. If the minimum value is greater than the maximum, the linear function will have a negative slope.The minimum cannot equal the maximum.(The default value is None) | Double |
| lowerThreshold | Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueBelowThreshold | A user-specified value to assign output cell locations with input values below the lowerThreshold. The value for valueBelowThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |
| upperThreshold | Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.The lowerThreshold must be less than the upperThreshold.(The default value is None) | Double |
| valueAboveThreshold | A user-specified value to assign output cell locations with input values above the upperThreshold. The value for valueAboveThreshold can be float, integer, or NoData. In the tool dialog box, no quotation marks are used around NoData; however, quotation marks are required around "NoData" when scripting.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
TfSymmetricLinear ({minimum}, {maximum}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})
```

### Example 2

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfSymmetricLinear(30, 8500, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfli1")
```

### Example 3

```python
import arcpy
from arcpy.sa import *
from arcpy import env
env.workspace = "c:/sapyexamples/data"
outRescale = RescaleByFunction("distroads", TfSymmetricLinear(30, 8500, "#", "#", "#", "#"), 1, 10)
outRescale.save("c:/sapyexamples/rescaletfli1")
```

### Example 4

```python
# Name: TfSymmetricLinear_Ex_02.py
# Description: Rescales input raster data using a SymmetricLinear function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfSymmetricLinear object
minimum = 30
maximum = 8500
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfSymmetricLinear(minimum, maximum, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfsl2")
```

### Example 5

```python
# Name: TfSymmetricLinear_Ex_02.py
# Description: Rescales input raster data using a SymmetricLinear function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "distroads"

# Create the TfSymmetricLinear object
minimum = 30
maximum = 8500
lowerthresh = "#"
valbelowthresh = "#"
upperthresh = "#"
valabovethresh = "#"
myTfFunction = TfSymmetricLinear(minimum, maximum, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfsl2")
```

---

## Threshold

## Summary

Creates a raster object by dividing an input raster into two distinct classes in which a high-value class is displayed with light pixels and a low-value class is displayed with dark pixels.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |

## Code Samples

### Example 1

```python
Threshold (raster)
```

### Example 2

```python
import arcpy

Binary_raster = arcpy.sa.Threshold("Landsat8.TIF")
```

### Example 3

```python
import arcpy

Binary_raster = arcpy.sa.Threshold("Landsat8.TIF")
```

---

## TimeMultipleDays

## Summary

Defines a multiple day time period within a given year to perform solar calculations. A year, start day, and end day are specified.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| year | The Julian year.(The default value is the current Julian year) | Long |
| startDay | The startDay is the first Julian day in the analysis.(The default value is 5, which is January 5th) | Long |
| endDay | The endDay is the last Julian day in the analysis.(The default value is 160, which is June 9th or 10th, depending if the year is a leap year) | Long |

## Code Samples

### Example 1

```python
TimeMultipleDays ({year}, {startDay}, {endDay})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTimeMultiDay = TimeMultipleDays(1980, 216, 244) 
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", myTimeMultiDay)
outAreaSolar.save("C:/temp/solarouttmd")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTimeMultiDay = TimeMultipleDays(1980, 216, 244) 
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", myTimeMultiDay)
outAreaSolar.save("C:/temp/solarouttmd")
```

### Example 4

```python
# Name: TimeMultipleDays_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeMultipleDays object.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeMultipleDays Object
year = 2004
startDay = 5
endDay = 6
myTimeMultiDay = TimeMultipleDays(year, startDay, endDay)

# Execute AreaSolarRadiation using TimeMultipleDays Object
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeMultiDay, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)


# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartmd2")
```

### Example 5

```python
# Name: TimeMultipleDays_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeMultipleDays object.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeMultipleDays Object
year = 2004
startDay = 5
endDay = 6
myTimeMultiDay = TimeMultipleDays(year, startDay, endDay)

# Execute AreaSolarRadiation using TimeMultipleDays Object
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeMultiDay, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)


# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartmd2")
```

---

## TimeSpecialDays

## Summary

Defines the summer solstice/equinox/winter solstice days as the time period to perform solar calculations.

## Code Samples

### Example 1

```python
TimeSpecialDays ()
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outAreaSolar = AreaSolarRadiation("solar_dem", "", 200, TimeSpecialDays())
outAreaSolar.save("C:/sapyexamples/output/areasolartsd")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outAreaSolar = AreaSolarRadiation("solar_dem", "", 200, TimeSpecialDays())
outAreaSolar.save("C:/sapyexamples/output/areasolartsd")
```

### Example 4

```python
# Name: TimeSpecialDays_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeSpecialDays object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeSpecialDays Object
myTimeSpecialDay = TimeSpecialDays()

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeSpecialDay, 14,
                                  0.5, "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)


# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartsd2")
```

### Example 5

```python
# Name: TimeSpecialDays_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeSpecialDays object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeSpecialDays Object
myTimeSpecialDay = TimeSpecialDays()

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeSpecialDay, 14,
                                  0.5, "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)


# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartsd2")
```

---

## TimeWholeYear

## Summary

Defines a year, using monthly intervals, to perform solar calculations.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| year | The Julian year.(The default value is the current Julian year) | Long |

## Code Samples

### Example 1

```python
TimeWholeYear ({year})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", TimeWholeYear(2008))
outAreaSolar.save("C:/sapyexamples/output/areasolartwy")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", TimeWholeYear(2008))
outAreaSolar.save("C:/sapyexamples/output/areasolartwy")
```

### Example 4

```python
# Name: TimeWholeYear_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeWholeYear object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create a TimeWholeYear Object
year = 2004
myTimeWholeYear = TimeWholeYear(year)

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeWholeYear, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)

# Save the output 
outAreaSolar.save("C:/sapyexamples/output/mysolarout")
```

### Example 5

```python
# Name: TimeWholeYear_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeWholeYear object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create a TimeWholeYear Object
year = 2004
myTimeWholeYear = TimeWholeYear(year)

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeWholeYear, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)

# Save the output 
outAreaSolar.save("C:/sapyexamples/output/mysolarout")
```

---

## TimeWithinDay

## Summary

Defines a time period within one day to perform solar calculations. A Julian Day, start time, and end time are specified.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| day | The day is a Julian day value from 1 to 365.(The default value is 183) | Long |
| startTime | The startTime is the first hour to be used in the analysis. The hour is represented with a number from 0 to 24.(The default value is 0) | Double |
| endTime | The endTime is the last hour to be used in the analysis. The hour is represented with a number from 0 to 24.(The default value is 24) | Double |

## Code Samples

### Example 1

```python
TimeWithinDay ({day}, {startTime}, {endTime})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTimeWithinDay = TimeWithinDay(264, 11, 14)
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", myTimeWithinDay)
outAreaSolar.save("C:/sapyexamples/output/areasolartwd")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTimeWithinDay = TimeWithinDay(264, 11, 14)
outAreaSolar = AreaSolarRadiation("solar_dem", "", "", myTimeWithinDay)
outAreaSolar.save("C:/sapyexamples/output/areasolartwd")
```

### Example 4

```python
# Name: TimeWithinDay_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeWithinDay object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeWithinDay Object
day = 100
startTime = 0 
endTime = 24
myTimeWithinDay = TimeWithinDay(day, startTime, endTime)

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeWithinDay, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)

# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartwd2")
```

### Example 5

```python
# Name: TimeWithinDay_Ex_02.py
# Description: Execute AreaSolarRadiation using the TimeWithinDay object
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "solar_dem"

# Create TimeWithinDay Object
day = 100
startTime = 0 
endTime = 24
myTimeWithinDay = TimeWithinDay(day, startTime, endTime)

# Execute AreaSolarRadiation
outAreaSolar = AreaSolarRadiation(inRaster, "", 200, myTimeWithinDay, 14, 0.5,
                                  "NOINTERVAL", 1, "FROM_DEM", 32, 8, 8,
                                  "UNIFORM_SKY", 0.3, 0.5)

# Save the output 
outAreaSolar.save("C:/sapyexamples/output/areasolartwd2")
```

---

## TopoBoundary

## Summary

Defines a list of feature classes containing polygons that represent the outer boundary of the output raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoBoundary (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoCliff

## Summary

Defines a list of line feature classes of cliff locations.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoCliff (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoCoast

## Summary

Defines a list of feature classes containing polygons that represent the coastal boundary.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoCoast (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoContour

## Summary

Defines a list of line feature classes that represent contours and the fields identifying their elevation values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[[inFeature, {field}],...] | The input line feature datasets. Optionally, you can supply the name of a field that stores the elevation values to use for the input lines. | List |

## Code Samples

### Example 1

```python
TopoContour (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoExclusion

## Summary

Defines a list of feature classes containing polygons that represent areas of data that will be excluded.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoExclusion (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoLake

## Summary

Defines a list of polygon feature classes that specify the location of lakes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoLake (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoPointElevation

## Summary

Defines a list of point feature classes representing surface elevations and the fields identifying their elevation values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[[inFeature, {field}],...] | The input point feature datasets. Optionally, you can supply the name of a field that stores the elevation values to use for the input points. | List |

## Code Samples

### Example 1

```python
TopoPointElevation (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoSink

## Summary

Defines a list of point feature classes that represent the locations and magnitude of known topographic depressions and the fields identifying their elevation values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[[inFeature, {field}],...] | The input point feature datasets. Optionally, you can supply the name of a field that stores the elevation values to use for the input points. The field used should be one that stores the elevation of the legitimate sink. If NONE is selected, only the location of the sink is used. | List |

## Code Samples

### Example 1

```python
TopoSink (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TopoStream

## Summary

Defines a list of line feature classes of stream locations.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inFeatures[inFeature,...] | The input feature datasets. | String |

## Code Samples

### Example 1

```python
TopoStream (inFeatures)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
myTopoCliff = TopoCliff(["cliff.shp"])
myTopoCoast = TopoCoast(["coast.shp"])
myTopoExclusion = TopoExclusion(["ignore.shp"])
outTopoToRaster1 = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream, myTopoCliff, myTopoCoast, myTopoExclusion])
outTopoToRaster1.save("C:/sapyexamples/output/ttraster1")
```

### Example 4

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

### Example 5

```python
# Name: TopoBoundary_Ex_02.py
# Description: Execute TopoToRaster using all the supported objects.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Create all the supported Objects
 
myTopoPtElev = TopoPointElevation([["spots.shp", "spot_meter"], ["spots2.shp", "elev"]])
myTopoContour = TopoContour([["contours.shp", "spot_meter"]]) 
myTopoBoundary = TopoBoundary(["boundary.shp"])
myTopoLake = TopoLake(["lakes.shp"])
myTopoSink = TopoSink([["sink1.shp", "elevation"], ["sink2.shp", "NONE"]])
myTopoStream = TopoStream(["streams.shp"])
# Execute TopoToRaster
outTopoToRaster = TopoToRaster([myTopoPtElev, myTopoContour, myTopoBoundary, myTopoLake, myTopoSink, myTopoStream])
# Save the output 
outTopoToRaster.save("C:/sapyexamples/output/ttraster2")
```

---

## TransposeBits

## Summary

Creates a raster object by unpacking the bits of the input pixel and mapping them to specified bits in the output pixel. The purpose of this function is to manipulate bits from a couple of inputs, such as the Landsat 8 quality band products.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster to unpack and remap. | Raster |
| input_bit_positions[input_bit_positions,...] | The list of input bits.(The default value is [12, 13]) | Integer |
| output_bit_positions[output_bit_positions,...] | The list of output bits.(The default value is [0, 1]) | Integer |
| constant_fill_value | An integer used to fill in all bits that are not involved in the transpose.(The default value is 0) | Integer |
| fill_raster | A raster used to fill in all bits that are not involved in the transpose.(The default value is None) | Raster |

## Code Samples

### Example 1

```python
TransposeBits (raster, {input_bit_positions}, {output_bit_positions}, {constant_fill_value}, {fill_raster})
```

### Example 2

```python
import acrpy

transpose_raster = arcpy.sa.TransposeBits("Landsat_8.tif",[4, 5],[0, 1], 0, None)
```

### Example 3

```python
import acrpy

transpose_raster = arcpy.sa.TransposeBits("Landsat_8.tif",[4, 5],[0, 1], 0, None)
```

---

## TSAVI

## Summary

Calculates the Transformed Soil Adjusted Vegetation Index (TSAVI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 4) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 3) | Integer |
| s | The slope of the soil line.(The default value is 0.33) | Double |
| a | The soil line intercept.(The default value is 0.5) | Double |
| X | The adjustment factor that is set to minimize soil noise.(The default value is 1.5) | Double |

## Code Samples

### Example 1

```python
TSAVI = (s *(NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 2

```python
TSAVI = (s *(NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 3

```python
TSAVI (raster, {nir_band_id}, {red_band_id}, {s}, {a}, {X})
```

### Example 4

```python
import arcpy

TSAVI_raster = arcpy.sa.TSAVI("Landsat8.tif",5,4,0.33,0.5,1.5)
```

### Example 5

```python
import arcpy

TSAVI_raster = arcpy.sa.TSAVI("Landsat8.tif",5,4,0.33,0.5,1.5)
```

---

## UnitConversion

## Summary

Converts pixels from one unit to another. It supports conversion of distance, speed, and temperature.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster that will contain the converted units. | Raster |
| from_unit | The original unit type of the pixels.MetersPerSecond—Meters per secondKilometersPerHour—Kilometers per hourKnots—KnotsFeetPerSecond—Feet per secondMilesPerHour—Miles per hourCelsius—CelsiusFahrenheit—FahrenheitKelvin—Kelvininches—InchesFeet—FeetYards—YardsMiles—MilesNauticalMiles—Nautical milesMillimeters—MillimetersCentimeters—CentimetersMeters—Meters(The default value is None) | String |
| to_unit | The converted unit type of the pixels.MetersPerSecond—Meters per secondKilometersPerHour—Kilometers per hourKnots—KnotsFeetPerSecond—Feet per secondMilesPerHour—Miles per hourCelsius—CelsiusFahrenheit—FahrenheitKelvin—Kelvininches—InchesFeet—FeetYards—YardsMiles—MilesNauticalMiles—Nautical milesMillimeters—MillimetersCentimeters—CentimetersMeters—Meters(The default value is None) | String |

## Code Samples

### Example 1

```python
UnitConversion (raster, {from_unit}, {to_unit})
```

### Example 2

```python
from arcpy.sa import *
out_unit_raster = UnitConversion("wind_speed_meter_per_second.tif",
                                 "MetersPerSecond'", "KilometersPerHour")
out_unit_raster.save("C:/arcpyExamples/outputs/wind_speed_km_per_hour.tif")
```

### Example 3

```python
from arcpy.sa import *
out_unit_raster = UnitConversion("wind_speed_meter_per_second.tif",
                                 "MetersPerSecond'", "KilometersPerHour")
out_unit_raster.save("C:/arcpyExamples/outputs/wind_speed_km_per_hour.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
inRaster_File = "temperature_celcius.tif"
from_unit = 'Celsius'
to_unit = 'Kelvin'

# Execute UnitConversion function
out_unit_raster = UnitConversion(inRaster_File, from_unit, to_unit)

# Save the output
out_unit_raster.save("C:/arcpyExamples/outputs/temperature_kelvin.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
inRaster_File = "temperature_celcius.tif"
from_unit = 'Celsius'
to_unit = 'Kelvin'

# Execute UnitConversion function
out_unit_raster = UnitConversion(inRaster_File, from_unit, to_unit)

# Save the output
out_unit_raster.save("C:/arcpyExamples/outputs/temperature_kelvin.tif")
```

---

## VARI

## Summary

Calculates the Visible Atmospherically Resistant Index (VARI) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| red_band_id | The band ID of the red-edge band. The band ID index uses one-based indexing.(The default value is 3) | Integer |
| green_band_id | The band ID of the green band. The ID index uses one-based indexing.(The default value is 2) | Integer |
| blue_band_id | The band ID of the blue band. The ID index uses one-based indexing.(The default value is 1) | Integer |

## Code Samples

### Example 1

```python
VARI = (Green - Red) / (Green + Red – Blue)
```

### Example 2

```python
VARI = (Green - Red) / (Green + Red – Blue)
```

### Example 3

```python
VARI (raster, {red_band_id}, {green_band_id}, {blue_band_id})
```

### Example 4

```python
import arcpy

VARI_raster = arcpy.sa.VARI("Landsat8.tif",4,3,2)
```

### Example 5

```python
import arcpy

VARI_raster = arcpy.sa.VARI("Landsat8.tif",4,3,2)
```

---

## VectorFieldRenderer

## Summary

Visualizes flow direction and magnitude information in a raster with vector symbols.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| is_uv_components | Specifies whether the input components represent U-V, or magnitude and direction.True—The input data represents U-V components.False—The input data represents magnitude and direction components. This is the default.(The default value is None) | Boolean |
| reference_system | Specifies how the direction component is measured.1—Direction is measured in arithmetic coordinates. 0° points due east, and 90° points due north.2—Direction is measured in geographic coordinates. 0° points due north, and 90° points due east. (The default value is 2) | Integer |
| mass_flow_angle_representation | Specifies the angle of mass flow.0—From—The mass is flowing along the angle and moving toward the origin of the reference system. This is sometimes referred to as the meteorological convention.1—To—The mass is flowing along the angle and moving away from the origin of the reference system. This is sometimes referred to as the oceanographic convention.(The default value is From) | Integer |
| calculation_method[calculation_method,...] | Specifies the thinning method to be used to calculate the magnitude and direction value of a tile.Vector Average—The following calculation occurs for each pixel: convert direction and magnitude to U and V components, calculate the averages of U and V for all pixels in a tile, and then convert the average U and average V back to direction and magnitude.Nearest neighbor—Uses the value from the pixels closest to the center of the tile.Bilinear—Bilinear resampling will be performed on the tile.Cubic—Cubic convolution resampling will be performed on the tile.Minimum—The minimum pixel value of the tile.Maximum—The maximum pixel value of the tile.(The default value is Vector Average) | String |
| symbology_name[symbology_name,...] | Specifies the name of the symbol depicting direction and magnitude.Single Arrow—A single arrow depicting direction and magnitude.Wind Barb—Wind barbs indicating wind direction and magnitude.Ocean Current—Ocean current symbol indicating current and magnitude.(The default value is Single Arrow) | String |

## Code Samples

### Example 1

```python
VectorFieldRenderer (raster, {is_uv_components}, {reference_system}, {mass_flow_angle_representation}, {calculation_method}, {symbology_name})
```

### Example 2

```python
import arcpy

VectorFieldRenderer_raster = arcpy.sa.VectorFieldRenderer(out_vector_field_raster, 
           is_uv_components=False, reference_system='Geographic',
           mass_flow_angle_representation='from')
```

### Example 3

```python
import arcpy

VectorFieldRenderer_raster = arcpy.sa.VectorFieldRenderer(out_vector_field_raster, 
           is_uv_components=False, reference_system='Geographic',
           mass_flow_angle_representation='from')
```

---

## VectorField

## Summary

Visualizes flow direction and magnitude information in a raster with vector symbols.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster_u_mag | The first input raster, which is either the U value or the magnitude. | Raster |
| raster_v_dir | The second input raster, which is either the V value or the direction. | Raster |
| input_data_type | The type of vector field your inputs represent.Unknown—It is unknown whether the inputs represent U-V or Magnitude-Direction.Vector-UV—Input data represents U and V components.Vector-MagDir— Input data represents magnitude and direction.(The default value is Vector-UV) | String |
| angle_reference_system | Specifies how the direction component was measured. Geographic—0° points due north, and 90° points due east.Arithmetic— 0° points due east, and 90° points due north.(The default value is Geographic) | String |
| output_data_type | Specifies the type of vector field your output will represent.Vector-UV—Output data represents U and V components.Vector-MagDir—Output data represents magnitude and direction.(The default value is Vector-UV) | String |

## Code Samples

### Example 1

```python
VectorField (raster_u_mag, raster_v_dir, {input_data_type}, {angle_reference_system}, {output_data_type})
```

### Example 2

```python
from arcpy.sa import *
out_vectorfield_raster = VectorField("magnitude", "direction", "Vector-MagDir",
                                 None, "Vector-UV)
out_vectorfield_raster.save("C:/arcpyExamples/outputs/vector_field_UV.crf")
```

### Example 3

```python
from arcpy.sa import *
out_vectorfield_raster = VectorField("magnitude", "direction", "Vector-MagDir",
                                 None, "Vector-UV)
out_vectorfield_raster.save("C:/arcpyExamples/outputs/vector_field_UV.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
# create a multidimensional raster object from hycom.nc that
# contains 2 variables water_u and water_v
hycom_raster = arcpy.Raster("C:/data/hycom.nc", True)

# choose the 2 variables from hycom_raster as 2 multidimensional raster
in_raster_u_mag = Subset(hycom_raster, variables = "water_u")
in_raster_v_dir = Subset(hycom_raster, variables = "water_v")

# Execute VectorField function
out_vectorField_raster = VectorField(in_raster_u_mag, in_raster_v_dir,
                                     "Vector-UV", "Geographic", "Vector-MagDir")

# Save the output
out_vectorField_raster.save("C:/arcpyExamples/vector_field_magdir.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
# create a multidimensional raster object from hycom.nc that
# contains 2 variables water_u and water_v
hycom_raster = arcpy.Raster("C:/data/hycom.nc", True)

# choose the 2 variables from hycom_raster as 2 multidimensional raster
in_raster_u_mag = Subset(hycom_raster, variables = "water_u")
in_raster_v_dir = Subset(hycom_raster, variables = "water_v")

# Execute VectorField function
out_vectorField_raster = VectorField(in_raster_u_mag, in_raster_v_dir,
                                     "Vector-UV", "Geographic", "Vector-MagDir")

# Save the output
out_vectorField_raster.save("C:/arcpyExamples/vector_field_magdir.crf")
```

---

## VfBidirHikingTime

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through a bidirectional hiking function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -70.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 70.0) | Double |

## Code Samples

### Example 1

```python
VfBidirHikingTime ({lowCutAngle}, {highCutAngle})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfBidirHikingTime(-30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfBH.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfBidirHikingTime(-30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfBH.tif")
```

### Example 4

```python
# Name: VfBidirHikingTime_Ex_02.py
# Description: Uses the VfBidirHikingTime object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfBidirHikingTime Object
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfBidirHikingTime(lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfBH2.tif")
```

### Example 5

```python
# Name: VfBidirHikingTime_Ex_02.py
# Description: Uses the VfBidirHikingTime object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfBidirHikingTime Object
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfBidirHikingTime(lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfBH2.tif")
```

---

## VfBinary

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through a binary function. If the vertical relative moving angle is greater than the low-cut angle and less than the high-cut angle, the vertical factor is set to the value associated with the zero factor; otherwise it is infinity.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the binary function.(The default value is 1.0) | Double |
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -30.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 30.0) | Double |

## Code Samples

### Example 1

```python
VfBinary ({zeroFactor}, {lowCutAngle}, {highCutAngle})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfBinary(1.0, -30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfB.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfBinary(1.0, -30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfB.tif")
```

### Example 4

```python
# Name: VfBinary_Ex_02.py
# Description: Uses the VfBinary object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfBinary Object
zeroFactor = 1.0
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfBinary(zeroFactor, lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfB2.tif")
```

### Example 5

```python
# Name: VfBinary_Ex_02.py
# Description: Uses the VfBinary object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfBinary Object
zeroFactor = 1.0
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfBinary(zeroFactor, lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfB2.tif")
```

---

## VfCos

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through a cosine function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| cosPower | The power to which the values in the cosine VRMA function will be raised. The VF is determined by: VF = cos(VRMA)power (The default value is 1.0) | Double |

## Code Samples

### Example 1

```python
VfCos ({lowCutAngle}, highCutAngle, {cosPower})
```

### Example 2

```python
VF = cos(VRMA)power
```

### Example 3

```python
VF = cos(VRMA)power
```

### Example 4

```python
VF = cos(VRMA)power
```

### Example 5

```python
VF = cos(VRMA)power
```

### Example 6

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfCos(-15, 15, 1.5)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfC.tif")
```

### Example 7

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfCos(-15, 15, 1.5)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfC.tif")
```

### Example 8

```python
# Name: VfCos_Ex_02.py
# Description: Uses the VfCos object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfCos Object
lowCutAngle = -15
highCutAngle = 45
cosPower = 2
myVerticalFactor = VfCos(lowCutAngle, highCutAngle, cosPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfC2.tif")
```

### Example 9

```python
# Name: VfCos_Ex_02.py
# Description: Uses the VfCos object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfCos Object
lowCutAngle = -15
highCutAngle = 45
cosPower = 2
myVerticalFactor = VfCos(lowCutAngle, highCutAngle, cosPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfC2.tif")
```

---

## VfCosSec

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA) through a cosine/secant function. If the VRMA is negative the vertical factor is defined by a cosine function, and if the VRMA is nonnegative the vertical factor is defined by a secant function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| cosPower | The power to which the values in the cosine VRMA function will be raised. The VF is determined by: VF = cos(VRMA)power(The default value is 1.0) | Double |
| secPower | The power to which the values in the secant VRMA function will be raised. The VF is determined by: VF = sec(VRMA)power (The default value is 1.0) | Double |

## Code Samples

### Example 1

```python
VfCosSec ({lowCutAngle}, {highCutAngle}, {cosPower}, {secPower})
```

### Example 2

```python
VF = cos(VRMA)power
```

### Example 3

```python
VF = cos(VRMA)power
```

### Example 4

```python
VF = sec(VRMA)power
```

### Example 5

```python
VF = sec(VRMA)power
```

### Example 6

```python
VF = cos(VRMA)power
```

### Example 7

```python
VF = cos(VRMA)power
```

### Example 8

```python
VF = sec(VRMA)power
```

### Example 9

```python
VF = sec(VRMA)power
```

### Example 10

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfCosSec(-90, 90, 1, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfCS.tif")
```

### Example 11

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfCosSec(-90, 90, 1, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfCS.tif")
```

### Example 12

```python
# Name: VfCosSec_Ex_02.py
# Description: Uses the VfCosSec object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"


# Create the VfCosSec Object
lowCutAngle = -90
highCutAngle = 90
cosPower = 1
secPower = 1
myVerticalFactor = VfCosSec(lowCutAngle, highCutAngle, cosPower, secPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfCS2.tif")
```

### Example 13

```python
# Name: VfCosSec_Ex_02.py
# Description: Uses the VfCosSec object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"


# Create the VfCosSec Object
lowCutAngle = -90
highCutAngle = 90
cosPower = 1
secPower = 1
myVerticalFactor = VfCosSec(lowCutAngle, highCutAngle, cosPower, secPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfCS2.tif")
```

---

## VfHikingTime

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through the reciprocal of Tobler's function, which results in hiking time in hours.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -70.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 70.0) | Double |

## Code Samples

### Example 1

```python
VfHikingTime ({lowCutAngle}, {highCutAngle})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfHikingTime(-30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfH.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfHikingTime(-30, 30)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfH.tif")
```

### Example 4

```python
# Name: VfHikingTime_Ex_02.py
# Description: Uses the VfHikingTime object to run the
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfHikingTime Object
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfHikingTime(lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfH2.tif")
```

### Example 5

```python
# Name: VfHikingTime_Ex_02.py
# Description: Uses the VfHikingTime object to run the
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfHikingTime Object
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfHikingTime(lowCutAngle, highCutAngle)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run DistanceAccumulation
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfH2.tif")
```

---

## VfInverseLinear

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through an inverse linear function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the inverse linear function.(The default value is 1.0) | Double |
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -45.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 45.0) | Double |
| slope | Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a -45-degree slope as -0.02222.(The default value is -0.022222) | Double |

## Code Samples

### Example 1

```python
VfInverseLinear ({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfInverseLinear(1.0, -45, 45, -0.02222)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfIL.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfInverseLinear(1.0, -45, 45, -0.02222)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfIL.tif")
```

### Example 4

```python
# Name: VfInverseLinear_Ex_02.py
# Description: Uses the VfInverseLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfInverseLinear Object
zeroFactor = 1.0
lowCutAngle = -45
highCutAngle = 45
slope = -0.02222
myVerticalFactor = VfInverseLinear(zeroFactor, lowCutAngle, highCutAngle,
                                    slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfIL2.tif")
```

### Example 5

```python
# Name: VfInverseLinear_Ex_02.py
# Description: Uses the VfInverseLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfInverseLinear Object
zeroFactor = 1.0
lowCutAngle = -45
highCutAngle = 45
slope = -0.02222
myVerticalFactor = VfInverseLinear(zeroFactor, lowCutAngle, highCutAngle,
                                    slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfIL2.tif")
```

---

## VfLinear

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through a linear function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the linear function.(The default value is 1.0) | Double |
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| slope | Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a 90-degree slope as 0.011111.(The default value is 0.011111) | Double |

## Code Samples

### Example 1

```python
VfLinear ({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfLinear(1.0, -90.0, 90.0, 0.01111)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfL.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfLinear(1.0, -90.0, 90.0, 0.01111)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfL.tif")
```

### Example 4

```python
# Name: VfLinear_Ex_02.py
# Description: Uses the VfLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfLinear Object
zeroFactor = 1.0
lowCutAngle = -90
highCutAngle = 90
slope = 0.01111
myVerticalFactor = VfLinear(zeroFactor, lowCutAngle, highCutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfL2.tif")
```

### Example 5

```python
# Name: VfLinear_Ex_02.py
# Description: Uses the VfLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfLinear Object
zeroFactor = 1.0
lowCutAngle = -90
highCutAngle = 90
slope = 0.01111
myVerticalFactor = VfLinear(zeroFactor, lowCutAngle, highCutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfL2.tif")
```

---

## VfSec

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle through a secant function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| secPower | The power to which the values in the secant VRMA function will be raised. The VF is determined by: VF = sec(VRMA)power(The default value is 1.0) | Double |

## Code Samples

### Example 1

```python
VfSec ({lowCutAngle}, {highCutAngle}, {secPower})
```

### Example 2

```python
VF = sec(VRMA)power
```

### Example 3

```python
VF = sec(VRMA)power
```

### Example 4

```python
VF = sec(VRMA)power
```

### Example 5

```python
VF = sec(VRMA)power
```

### Example 6

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSec(-90, 90, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfS.tif")
```

### Example 7

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSec(-90, 90, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfS.tif")
```

### Example 8

```python
# Name: VfSec_Ex_02.py
# Description: Uses the VfSec object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSec Object
lowCutAngle = -90
highCutAngle = 90
secPower = 1
myVerticalFactor = VfSec(lowCutAngle, highCutAngle, secPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfS2.tif")
```

### Example 9

```python
# Name: VfSec_Ex_02.py
# Description: Uses the VfSec object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSec Object
lowCutAngle = -90
highCutAngle = 90
secPower = 1
myVerticalFactor = VfSec(lowCutAngle, highCutAngle, secPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfS2.tif")
```

---

## VfSecCos

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA) through a secant/cosine function. If the VRMA is negative the vertical factor is defined by a secant function, and if the VRMA is nonnegative the vertical factor is defined by a cosine function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity (The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| secPower | The power to which the values in the secant VRMA function will be raised. The VF is determined by: VF = sec(VRMA)power(The default value is 1.0) | Double |
| cosPower | The power to which the values in the cosine VRMA function will be raised. The VF is determined by: VF = cos(VRMA)power(The default value is 1.0) | Double |

## Code Samples

### Example 1

```python
VfSecCos ({lowCutAngle}, {highCutAngle}, {secPower}, {cosPower})
```

### Example 2

```python
VF = sec(VRMA)power
```

### Example 3

```python
VF = sec(VRMA)power
```

### Example 4

```python
VF = cos(VRMA)power
```

### Example 5

```python
VF = cos(VRMA)power
```

### Example 6

```python
VF = sec(VRMA)power
```

### Example 7

```python
VF = sec(VRMA)power
```

### Example 8

```python
VF = cos(VRMA)power
```

### Example 9

```python
VF = cos(VRMA)power
```

### Example 10

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSecCos(-90, 90, 1, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVSC.tif")
```

### Example 11

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSecCos(-90, 90, 1, 1)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVSC.tif")
```

### Example 12

```python
# Name: VfSecCos_Ex_02.py
# Description: Uses the VfSecCos object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSecCos Object
lowCutAngle = -90
highCutAngle = 90
secPower = 1
cosPower = 1
myVerticalFactor = VfSecCos(lowCutAngle, highCutAngle, secPower, cosPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfSC2.tif")
```

### Example 13

```python
# Name: VfSecCos_Ex_02.py
# Description: Uses the VfSecCos object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSecCos Object
lowCutAngle = -90
highCutAngle = 90
secPower = 1
cosPower = 1
myVerticalFactor = VfSecCos(lowCutAngle, highCutAngle, secPower, cosPower)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfSC2.tif")
```

---

## VfSymInverseLinear

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA) through a symmetrical inverse linear function in either the negative or positive side of the VRMA, respectively. The two linear functions are symmetrical with respect to the VF (y) axis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the symmetric inverse linear function.(The default value is 1.0) | Double |
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -45.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 45.0) | Double |
| slope | Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a -45-degree slope as -0.022222.(The default value is -0.022222) | Double |

## Code Samples

### Example 1

```python
VfSymInverseLinear ({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSymInverseLinear(1.0, -45, 45, -0.02222)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfIL.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSymInverseLinear(1.0, -45, 45, -0.02222)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfIL.tif")
```

### Example 4

```python
# Name: VfSymInverseLinear_Ex_02.py
# Description: ses the VfSymInverseLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSymInverseLinear Object
zeroFactor = 1.0
lowCutAngle = -45
highCutAngle = 45
slope = -0.02222
myVerticalFactor = VfSymInverseLinear(zeroFactor, lowCutAngle, highCutAngle,
                                      slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfIL2.tif")
```

### Example 5

```python
# Name: VfSymInverseLinear_Ex_02.py
# Description: ses the VfSymInverseLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSymInverseLinear Object
zeroFactor = 1.0
lowCutAngle = -45
highCutAngle = 45
slope = -0.02222
myVerticalFactor = VfSymInverseLinear(zeroFactor, lowCutAngle, highCutAngle,
                                      slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfIL2.tif")
```

---

## VfSymLinear

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA) through a symmetrical linear function in either the negative or positive side of the VRMA, respectively. The two linear functions are symmetrical with respect to the VF (y) axis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| zeroFactor | The zeroFactor will be used to position the y-intercept of the symmetric linear function.(The default value is 1.0) | Double |
| lowCutAngle | The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.(The default value is -90.0) | Double |
| highCutAngle | The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.(The default value is 90.0) | Double |
| slope | Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a 90-degree slope as 0.011111.(The default value is 0.011111) | Double |

## Code Samples

### Example 1

```python
VfSymLinear ({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSymLinear(1.0, -90, 90, -0.01111)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfSL.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfSymLinear(1.0, -90, 90, -0.01111)
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfSL.tif")
```

### Example 4

```python
# Name: VfSymLinear_Ex_02.py
# Description: Uses the VfSymLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSymLinear Object
zeroFactor = 1.0
lowCutAngle = -90
highCutAngle = 90
slope = -0.01111
myVerticalFactor = VfSymLinear(zeroFactor, lowCutAngle, highCutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfSL2.tif")
```

### Example 5

```python
# Name: VfSymLinear_Ex_02.py
# Description: Uses the VfSymLinear object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfSymLinear Object
zeroFactor = 1.0
lowCutAngle = -90
highCutAngle = 90
slope = -0.01111
myVerticalFactor = VfSymLinear(zeroFactor, lowCutAngle, highCutAngle, slope)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfSL2.tif")
```

---

## VfTable

## Summary

Defines the relationship between the vertical cost factor and the vertical relative moving angle with a vertical-factor graph identifying the vertical factor specified by a table file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inTable | The inTable is an ASCII file with two columns on each line. The first column identifies the VRMA in degrees, and the second, the VF. Each line specifies a point. Two consecutive points produce a line segment in the VRMA-VF coordinate system.The VRMAs must be input in ascending order. The VF factor for any VRMA less than the first (lowest) input value or larger than the final (largest) input will be set to infinity. An infinite VF is represented by a negative value in the ASCII table. | File |

## Code Samples

### Example 1

```python
VfTable (inTable)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfTable("vffile.txt")
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfT.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myVerticalFactor = VfTable("vffile.txt")
outDistAccum = DistanceAccumulation("Source.shp", "", "elev.tif",
                                   "cost.tif", "elev.tif",
                                    myVerticalFactor)
outDistAccum.save("C:/sapyexamples/output/distAccumVfT.tif")
```

### Example 4

```python
# Name: VfTable_Ex_02.py
# Description: Uses the VfTable object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfTable Object
inTable = "vffile.txt"
myVerticalFactor = VfTable(inTable)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfT2.tif")
```

### Example 5

```python
# Name: VfTable_Ex_02.py
# Description: Uses the VfTable object to run the 
#              DistanceAccumulation tool
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSourceData = "source.shp"
inCostRaster = "costraster.tif"
inElevation = "elev.tif"

# Create the VfTable Object
inTable = "vffile.txt"
myVerticalFactor = VfTable(inTable)

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute PathDistance
outDistAccum = DistanceAccumulation(inSourceData, "", inElevation,
                                    inCostRaster, inElevation,
                                    myVerticalFactor)

# Save the output 
outDistAccum.save("C:/sapyexamples/output/distaccumvfT2.tif")
```

---

## WindChill

## Summary

Identifies dangerous winter conditions that, depending on exposure times to the elements, can result in frostbite or hypothermia.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| temperature_raster[temperature_raster,...] | A single-band raster where pixel values represent ambient air temperature. | Raster |
| wind_speed_raster[wind_speed_raster,...] | A single-band raster where pixel values represent wind speed. | Raster |
| temperature_units | The unit of measurement associated with the input temperature raster. Available input units are Celsius, Fahrenheit, and Kelvin.(The default value is Fahrenheit) | String |
| wind_speed_units | Defines the unit of measurement for the wind-speed raster: mph—Miles per hourkm/h—Kilometers per hourm/s—Meters per secondft/s—Feet per secondkn—Knots(The default value is mph) | String |
| wind_chill_units | The unit of measurement associated with the output raster. Available output units are Celsius, Fahrenheit, and Kelvin.(The default value is Fahrenheit) | String |

## Code Samples

### Example 1

```python
Wind Chill = 35.74 + (0.6215 * T) - (35.75 * WS^0.16) + (0.4275 * T * WS^0.16)
```

### Example 2

```python
Wind Chill = 35.74 + (0.6215 * T) - (35.75 * WS^0.16) + (0.4275 * T * WS^0.16)
```

### Example 3

```python
WindChill (temperature_raster, wind_speed_raster, {temperature_units}, {wind_speed_units}, {wind_chill_units})
```

### Example 4

```python
from arcpy.sa import *
out_windchill_raster = WindChill("temperature.tif", "windspeed.tif", "",
                                 "km/h", "Celsius")
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_C.tif")
```

### Example 5

```python
from arcpy.sa import *
out_windchill_raster = WindChill("temperature.tif", "windspeed.tif", "",
                                 "km/h", "Celsius")
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_C.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_temperature_raster = "temperature.tif"
in_wind_speed_raster  = "windspeed.tif"

# Execute WindChill function
out_windchill_raster = WindChill(in_temperature_raster, in_wind_speed_raster,
                                 "", "knots", "Kelvin")
# Save the output
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_K.tif")
```

### Example 7

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_temperature_raster = "temperature.tif"
in_wind_speed_raster  = "windspeed.tif"

# Execute WindChill function
out_windchill_raster = WindChill(in_temperature_raster, in_wind_speed_raster,
                                 "", "knots", "Kelvin")
# Save the output
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_K.tif")
```

---

## WOTable

## Summary

Defines the input rasters, the field identifying the input values, the remap of their values, the weight of each raster, and the evaluation scale to use in the Weighted Overlay tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| weightedOverlayTable[[inRaster, influence, field, Remap],...] | The table specifying the input rasters, their influence, the field to use, and the remap table identifying what the old values should be remapped to.inRaster—The input raster criteria being weighted.influence—The influence of the raster compared to the other criteria (data type: double).field—The field of the criteria raster to use for weighting (data type: string).Remap—The Remap object identifies the scaled weights for the input criterion. In addition to numerical values for the scaled weights in the remap table, the following options are available: RESTRICTED—Assigns the restricted value to cells in the output, regardless of whether other input rasters have a different scale value set for that cell.NODATA—Assigns NoData to cells in the output, regardless of whether other input rasters have a different scale value set for that cell. | List |
| evaluationScale[from, to, by] | The range and interval for the new values in which to remap the old values. The parameter is required for both the dialog box and scripting but it has no effect in scripting. from—Is the lowest value to use for the new values (data type: double).to—Is the highest value to use for the new values (data type: double). by—Is the interval between the new remap values (data type: double). | List |

## Code Samples

### Example 1

```python
WOTable (weightedOverlayTable, evaluationScale)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myWOTable = WOTable([["snow", 50, "VALUE", RemapValue([[0, 1], [1, 1], [5, 5],
                    [6, 6], [7, 7], [8, 8], [9, 9], ["NODATA", "NODATA"]])],
                    ["land", 20, "VALUE", RemapValue([[0, 1], [1, 1], [5, 5],
                    [6, 6],[7, 7], [8, 8], [9, 9], ["NODATA", "NODATA"]])],
                    ["soil", 30, "VALUE", RemapValue([[0, 1], [1, 1], [2, 2],
                    [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9],
                    ["NODATA", "NODATA"]])]], [1, 9, 1])
outWeightedOverlay = WeightedOverlay(myWOTable)
outWeightedOverlay.save("C:/sapyexamples/output/woverlaytbl")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myWOTable = WOTable([["snow", 50, "VALUE", RemapValue([[0, 1], [1, 1], [5, 5],
                    [6, 6], [7, 7], [8, 8], [9, 9], ["NODATA", "NODATA"]])],
                    ["land", 20, "VALUE", RemapValue([[0, 1], [1, 1], [5, 5],
                    [6, 6],[7, 7], [8, 8], [9, 9], ["NODATA", "NODATA"]])],
                    ["soil", 30, "VALUE", RemapValue([[0, 1], [1, 1], [2, 2],
                    [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9],
                    ["NODATA", "NODATA"]])]], [1, 9, 1])
outWeightedOverlay = WeightedOverlay(myWOTable)
outWeightedOverlay.save("C:/sapyexamples/output/woverlaytbl")
```

### Example 4

```python
# Name: WOTable_Ex_02.py
# Description: Uses the WOTable object to execute WeightedOverlay tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "snow"
inRaster2 = "land"
inRaster3 = "soil"

# Define WOTable 
myWOTable = WOTable([[inRaster1, 50, "VALUE", RemapValue([[1, 1], [5, 5],
                    [6, 5], [7, 5], [8, 9], [9, 9], ["NODATA", "NODATA"]])],
                    [inRaster2, 20, "VALUE", RemapValue([[1, 1], [5, 5],
                    [6, 5], [7, 5], [8, 9], [9, 9], ["NODATA", "NODATA"]])],
                    [inRaster3, 30, "VALUE", RemapValue([[1, 1], [2, 1],
                    [3, 1], [4, 5], [5, 5], [6, 5], [7, 9], [8, 9], [9, 9],
                    ["NODATA", "NODATA"]])]], [1, 9, 1])
 
# Execute WeightedOverlay
outWeightedOverlay = WeightedOverlay(myWOTable)

# Save the output 
outWeightedOverlay.save("C:/sapyexamples/output/woverlaytbl2")
```

### Example 5

```python
# Name: WOTable_Ex_02.py
# Description: Uses the WOTable object to execute WeightedOverlay tool.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "snow"
inRaster2 = "land"
inRaster3 = "soil"

# Define WOTable 
myWOTable = WOTable([[inRaster1, 50, "VALUE", RemapValue([[1, 1], [5, 5],
                    [6, 5], [7, 5], [8, 9], [9, 9], ["NODATA", "NODATA"]])],
                    [inRaster2, 20, "VALUE", RemapValue([[1, 1], [5, 5],
                    [6, 5], [7, 5], [8, 9], [9, 9], ["NODATA", "NODATA"]])],
                    [inRaster3, 30, "VALUE", RemapValue([[1, 1], [2, 1],
                    [3, 1], [4, 5], [5, 5], [6, 5], [7, 9], [8, 9], [9, 9],
                    ["NODATA", "NODATA"]])]], [1, 9, 1])
 
# Execute WeightedOverlay
outWeightedOverlay = WeightedOverlay(myWOTable)

# Save the output 
outWeightedOverlay.save("C:/sapyexamples/output/woverlaytbl2")
```

---

## WSTable

## Summary

Defines the input rasters and their weights which will be added together in the Weighted Sum tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| weightedSumTable[[inRaster, field, weight],...] | The table specifying the input rasters, the fields to use for the values for each raster, and the weight by which to multiply each raster.InRaster—Is the raster being weighted (data type: string).field—The field in the raster to use for the input values (data type: string).weight—The weight value by which to multiple the raster (data type: double). | List |

## Code Samples

### Example 1

```python
WSTable (weightedSumTable)
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myWSumTable = WSTable([["snow", "VALUE", 0.2], ["land", "VALUE", 0.3], ["soil",
                    "VALUE", 0.5]])
outWSumT = WeightedSum(myWSumTable)
outWSumT.save("C:/sapyexamples/output/wsumtable")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
myWSumTable = WSTable([["snow", "VALUE", 0.2], ["land", "VALUE", 0.3], ["soil",
                    "VALUE", 0.5]])
outWSumT = WeightedSum(myWSumTable)
outWSumT.save("C:/sapyexamples/output/wsumtable")
```

### Example 4

```python
# Name: WSTable_Ex_02.py
# Description: Demonstrate executing WeightedSum using the WSTable object.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = "snow"
field01 = "VALUE"
weight01 = 0.25
inRaster02 = "land"
field02 = "VALUE"
weight02 = 0.25
inRaster03 = "soil"
field03 = "VALUE"
weight03 = 0.5

# Define WSTable 
myWSumTable = WSTable([[inRaster01, field01, weight01], [inRaster02, field02,
                        weight02], [inRaster03, field03, weight03]])

# Execute WeightedSum
outWSumT = WeightedSum(myWSumTable)

# Save the output 
outWSumT.save("C:/sapyexamples/output/wsumtable2")
```

### Example 5

```python
# Name: WSTable_Ex_02.py
# Description: Demonstrate executing WeightedSum using the WSTable object.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = "snow"
field01 = "VALUE"
weight01 = 0.25
inRaster02 = "land"
field02 = "VALUE"
weight02 = 0.25
inRaster03 = "soil"
field03 = "VALUE"
weight03 = 0.5

# Define WSTable 
myWSumTable = WSTable([[inRaster01, field01, weight01], [inRaster02, field02,
                        weight02], [inRaster03, field03, weight03]])

# Execute WeightedSum
outWSumT = WeightedSum(myWSumTable)

# Save the output 
outWSumT.save("C:/sapyexamples/output/wsumtable2")
```

---

## ZonalRemap

## Summary

Categorizes the pixel values of a raster object into groups based on zones defined in another raster and zone-dependent value mapping defined in a table.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | A single-band raster input containing pixel values to remap. | Raster |
| zonal_attribute_table | A table containing at least three fields. The table must have a minimum threshold value, a maximum threshold value, and a target value. The target value is the name of the field that will contain the remapped value. The format of the input can be a feature class, feature service, or any table type that ArcGIS supports. | String |
| zone_raster | A single-band raster, where each pixel defines zones associated with a particular location. A zone is defined as all areas in the input that have the same value. The areas do not have to be contiguous.(The default value is None) | RasterCollection |
| zone_field | The field name in the zonal_attribute_table that contains the zone ID values. The zone ID values are directly tied to the zone IDs in your zonal raster. The zone ID values provide another level of filtering while remapping. If there is no zone ID associated with a particular record in the table, it will not participate in the remapping.(The default value is 'ZoneID') | String |
| min_value_field_name | The field name containing the minimum value above which an input pixel is remapped. If left unspecified, or if the field value is null, pixel values are not tested for minimum.(The default value is 'ZoneMin') | String |
| max_value_field_name | The field name containing the maximum value below which an input pixel is remapped. If left unspecified, or if the field value is null, pixel values are not tested for maximum.(The default value is 'ZoneMax') | String |
| output_value_field_name | The field name containing the target value to which an input pixel is remapped. If left unspecified, or if the field value is null, remapped pixel values are set to default_output_value.(The default value is 'ZoneValue') | String |
| background_value | The initial pixel value of the output raster, before input pixels are remapped.(The default value is 0) | String |
| default_output_value | The value that will be assigned to a pixel that does not satisfy any of the conditions set in the zonal_attribute_table. This value will also be the value of the output pixel if either the output_value_field_name parameter is left unspecified or the output value of the corresponding zonal threshold is left unspecified in the zonal_attribute_table.(The default value is 255) | String |
| where_clause | A query applied to the zonal_attribute_table.(The default value is None) | String |

## Code Samples

### Example 1

```python
ZonalRemap (raster, zonal_attribute_table, {zone_raster}, {zone_field}, {min_value_field_name}, {max_value_field_name}, {output_value_field_name}, {background_value}, {default_output_value}, {where_clause})
```

### Example 2

```python
from arcpy.sa import *
out_zonalremap_raster = ZonalRemap("cloudceilings.tif","zonal.csv", "zone.tif")
out_zonalremap_raster.save("C:/arcpyExamples/outputs/Zonal_remap.tif")
```

### Example 3

```python
from arcpy.sa import *
out_zonalremap_raster = ZonalRemap("cloudceilings.tif","zonal.csv", "zone.tif")
out_zonalremap_raster.save("C:/arcpyExamples/outputs/Zonal_remap.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "NDVI.tif"
zonal_attribute_table = "zonal.csv"
zone_raster = "neighborhoods.tif"

# Apply ZonalRemap function
zonal_remap_raster = ZonalRemap(in_raster, zonal_attribute_table, zone_raster)

# Save the output
zonal_remap_raster.save("C:/arcpyExamples/outputs/NDVI.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "NDVI.tif"
zonal_attribute_table = "zonal.csv"
zone_raster = "neighborhoods.tif"

# Apply ZonalRemap function
zonal_remap_raster = ZonalRemap(in_raster, zonal_attribute_table, zone_raster)

# Save the output
zonal_remap_raster.save("C:/arcpyExamples/outputs/NDVI.tif")
```

---
