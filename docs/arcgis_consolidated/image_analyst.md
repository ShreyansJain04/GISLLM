# Image Analyst Complete Reference

*Consolidated from 138 individual documentation files*

---

## Aggregate

## Summary

Creates a raster object by combining slices from the input multidimensional raster based on a dimension interval and an aggregation method.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input multidimensional raster to be aggregated. | Raster |
| dimension_name | The aggregation dimension. This is the dimension along which the variables will be aggregated. | String |
| raster_function | The name of a raster function as a string or the path to a custom raster function (.rft.xml file) that will be used to compute the aggregated pixel values. The following are the supported raster functions as strings: Majority—The pixel value that occurs most frequently will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension.MajorityContinueOnNoData—The pixel value that occurs most frequently will be calculated across all slices in the interval, and NoData pixels will be ignored.Max—The maximum value of a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension.MaxContinueOnNoData—The maximum value of a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored.Mean—The mean of a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. MeanContinueOnNoData—The mean of a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Med—The median of a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. MedContinueOnNoData—The median of a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Min—The minimum of a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. MinContinueOnNoData—The minimum of a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Minority—The pixel value that occurs least frequently will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. MinorityContinueOnNoData—The pixel value that occurs least frequently will be calculated across all slices in the interval, and NoData pixels will be ignored.Percentile—The percentile of values for a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension.PercentileContinueOnNoData—The percentile of values for a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Range—The range of values for a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. RangeContinueOnNoData—The range of values for a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Std—The standard deviation of a pixel will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. StdContinueOnNoData—The standard deviation of a pixel will be calculated across all slices in the interval, and NoData pixels will be ignored. Sum—The sum of a pixel's values will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension. SumContinueOnNoData—The sum of a pixel's values will be calculated across all slices in the interval, and NoData pixels will be ignored.Variety—The number of unique pixel values will be calculated across all slices in the interval, and NoData will be returned if there are any NoData pixels along the dimension.VarietyContinueOnNoData—The number of unique pixel values will be calculated across all slices in the interval, and NoData pixels will be ignored. | String |
| raster_function_arguments | The parameters and values associated with the raster function or function chain. If not specified, default values will be used.(The default value is None) | Dictionary |
| aggregation_definition | The dimension interval for which the data will be aggregated. The key-value pairs must follow one of the following formats:'interval':<interval_keyword>Use the interval keyword only when dimension_name is a time dimension. Interval keywords include HOURLY, DAILY, WEEKLY, MONTHLY, QUARTERLY, and YEARLY. For example, use this option to aggregate daily temperature data into monthly temperature data for each year. The output will include no more than 12 slices for each year.'recurrent_interval':<recurrent_interval_keyword>Use the recurrent interval keyword only when dimension_name is a time dimension. Recurrent interval keywords include DAILY, WEEKLY, MONTHLY, and QUARTERLY. For example, use this option to calculate the average temperature value for each month across all the years in the dataset. The output will include no more than 12 slices (one slice for each month of the year).'interval_value':<value>, 'interval_unit':<unit>Use the interval value to define recurring intervals. The interval unit is required when dimension_name is a time dimension. Interval unit keywords include HOUR, DAY, WEEK, MONTH, QUARTER, and YEAR. For example, use this option to aggregate daily temperature into temperature every 10 days.'interval_ranges':[(min, max),(min, max), ...]Use the interval ranges option to define custom intervals for aggregation. For example, use this option to aggregate daily temperature into temperature across specific seasonal dates.If not specified, all slices across the dimension will be aggregated.(The default value is None) | Dictionary |
| dimensionless | Specifies whether the output will be a dimensionless raster. This is only possible when the output has a single slice.True—The layer will not have dimension values.False—The layer will have dimension values.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Aggregate (in_raster, dimension_name, raster_function, {raster_function_arguments}, {aggregation_definition}, {dimensionless})
```

### Example 2

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

in_raster = Raster('ClimateData_Daily.nc', True)

# Choose the precipitation variable
prcp_raster = Subset(in_raster, variables = 'prcp')

# Calculate the average precipitation across the whole time period
avg_prcp = Aggregate(prcp_raster, 'StdTime', 'Mean')

# Calculate the monthly mean precipitation 
monthly_avg_prcp = Aggregate(prcp_raster, 'StdTime', 
	'Mean', {'interval': 'monthly'})

# Calculate the minimum precipitation every 10 days
min_precip_10day = Aggregate(prcp_raster, 'StdTime', 'Min', 
	{'interval_value' : 10, 'interval_unit': 'day'})

# Calculate the maximum precipitation in two separate time ranges
max_prcp_range = Aggregate(prcp_raster, 'StdTime', 'Max', 
	{'interval_ranges':  [('2001-01-01T00:00:00', '2001-02-01T00:00:00'), 
	('2001-12-01T00:00:00', '2001-12-24T00:00:00')]})
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

in_raster = Raster('ClimateData_Daily.nc', True)

# Choose the precipitation variable
prcp_raster = Subset(in_raster, variables = 'prcp')

# Calculate the average precipitation across the whole time period
avg_prcp = Aggregate(prcp_raster, 'StdTime', 'Mean')

# Calculate the monthly mean precipitation 
monthly_avg_prcp = Aggregate(prcp_raster, 'StdTime', 
	'Mean', {'interval': 'monthly'})

# Calculate the minimum precipitation every 10 days
min_precip_10day = Aggregate(prcp_raster, 'StdTime', 'Min', 
	{'interval_value' : 10, 'interval_unit': 'day'})

# Calculate the maximum precipitation in two separate time ranges
max_prcp_range = Aggregate(prcp_raster, 'StdTime', 'Max', 
	{'interval_ranges':  [('2001-01-01T00:00:00', '2001-02-01T00:00:00'), 
	('2001-12-01T00:00:00', '2001-12-24T00:00:00')]})
```

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
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")
 
in_raster = Raster('ClimateData_Daily.nc', True)
 
# Choose the precipitation variable 
prcp_raster = Subset(in_raster, variables = 'prcp')
 
# Calculate percent of mean anomalies, 
# where the mean_value is the mean of all slices 
prcp_anomaly = Anomaly(prcp_raster, anomaly_type = 'PERCENT_OF_MEAN') 
 
# Calculate the difference from mean,
# where the mean_value is the mean of each year 
prcp_monthly_anomaly = Anomaly(
	prcp_raster, temporal_interval = 'YEARLY')
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")
 
in_raster = Raster('ClimateData_Daily.nc', True)
 
# Choose the precipitation variable 
prcp_raster = Subset(in_raster, variables = 'prcp')
 
# Calculate percent of mean anomalies, 
# where the mean_value is the mean of all slices 
prcp_anomaly = Anomaly(prcp_raster, anomaly_type = 'PERCENT_OF_MEAN') 
 
# Calculate the difference from mean,
# where the mean_value is the mean of each year 
prcp_monthly_anomaly = Anomaly(
	prcp_raster, temporal_interval = 'YEARLY')
```

---

## ApparentReflectance

## Summary

Calibrates the digital number (DN) values of imagery from some satellite sensors. The calibration uses sun elevation, acquisition date, sensor gain, and bias for each band to derive Top of Atmosphere reflectance, and sun angle correction.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| radiance_gain_values[radiance_gain_values,...] | The list of radiance gain values, in order of bands.(The default value is None) | Double |
| radiance_bias_values[radiance_bias_values,...] | The list of radiance bias values.(The default value is None) | Double |
| reflectance_gain_values[reflectance_gain_values,...] | The list of reflectance gain values.(The default value is None) | Double |
| reflectance_bias_values[reflectance_bias_values,...] | The list of reflectance bias values.(The default value is None) | Double |
| sun_elevation | The sun elevation angle, in degrees.(The default value is None) | Double |
| albedo | Specifies whether to provide the apparent reflectance values as albedo, which is the fractional value of the available energy that is reflected by the planetary surface. It is expressed as a dimensionless floating-point number between 0 and 1.True—The function returns 32-bit floating-point values, expressed in the range of 0.0 to 1.0.False—The function returns apparent reflectance values.(The default value is False) | Boolean |
| scale_factor | The multiplier for the albedo to convert all floating-point values into integer values.(The default value is None) | Integer |
| offset | The offset for the scaled albedo value.For 16-bit unsigned data types, the default scale offset is 5000.For 8-bit unsigned data types, the default scale offset is 0.(The default value is None) | Integer |

## Code Samples

### Example 1

```python
ApparentReflectance (raster, {radiance_gain_values}, {radiance_bias_values}, {reflectance_gain_values}, {reflectance_bias_values}, {sun_elevation}, {albedo}, {scale_factor}, {offset})
```

### Example 2

```python
# Import system modulesimport arcpy
import arcpy
from arcpy.ia import *

# Set the local variables
in_raster = "C:/data/Landsat.tif"
radiance_gain_values = [0.762824, 1.442510, 1.039880]
radiance_bias_values = [-1.52, -2.84, -1.17]
reflectance_gain_values = None
reflectance_bias_values = None
sun_elevation = 51.71
albedo = False
scale_factor = 255
offset = None

# Apply ApparentReflectance function
reflectance_raster = arcpy.ia.ApparentReflectance(in_raster, radiance_gain_values,
		      radiance_bias_values, reflectance_gain_values, reflectance_bias_values,
                      sun_elevation, albedo, scale_factor, offset)

# Save the output

reflectance_raster.save("C:/arcpyExamples/outputs/Landsat8_reflectance.crf")
```

### Example 3

```python
# Import system modulesimport arcpy
import arcpy
from arcpy.ia import *

# Set the local variables
in_raster = "C:/data/Landsat.tif"
radiance_gain_values = [0.762824, 1.442510, 1.039880]
radiance_bias_values = [-1.52, -2.84, -1.17]
reflectance_gain_values = None
reflectance_bias_values = None
sun_elevation = 51.71
albedo = False
scale_factor = 255
offset = None

# Apply ApparentReflectance function
reflectance_raster = arcpy.ia.ApparentReflectance(in_raster, radiance_gain_values,
		      radiance_bias_values, reflectance_gain_values, reflectance_bias_values,
                      sun_elevation, albedo, scale_factor, offset)

# Save the output

reflectance_raster.save("C:/arcpyExamples/outputs/Landsat8_reflectance.crf")
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

import arcpy
from arcpy.ia import *

# Set input raster for NDVI
Landsat = Raster("Landsat8_1_12_18.tif") 

# Apply NDVI raster function to a single raster
out_NDVI_raster = Apply(Landsat, "NDVI", {'VisibleBandID':4,'InfraredBandID':5}) 

# Set input rasters for Arithmetic
DEM = Raster("DEM.tif")
Buildings = Raster("BuildingHeights.tif") 

# Apply Arithmetic raster function to add building height to ground elevation
out_Arithmetic_raster = Apply((DEM, Buildings),'Plus')

# Set input rasters for Composite Bands
Band1 = Raster("L8_MSB1.tif") 
Band2 = Raster("L8_MSB2.tif") 
Band3 = Raster("L8_MSB3.tif") 

# Apply Composite Bands function to combine three bands into a single raster
out_composite_rasters = Apply([Band1, Band2, Band3], 'CompositeBand')
```

### Example 3

```python
# Apply NDVI, Arithmetic, and Composite Bands functions to one or more raster datasets.

import arcpy
from arcpy.ia import *

# Set input raster for NDVI
Landsat = Raster("Landsat8_1_12_18.tif") 

# Apply NDVI raster function to a single raster
out_NDVI_raster = Apply(Landsat, "NDVI", {'VisibleBandID':4,'InfraredBandID':5}) 

# Set input rasters for Arithmetic
DEM = Raster("DEM.tif")
Buildings = Raster("BuildingHeights.tif") 

# Apply Arithmetic raster function to add building height to ground elevation
out_Arithmetic_raster = Apply((DEM, Buildings),'Plus')

# Set input rasters for Composite Bands
Band1 = Raster("L8_MSB1.tif") 
Band2 = Raster("L8_MSB2.tif") 
Band3 = Raster("L8_MSB3.tif") 

# Apply Composite Bands function to combine three bands into a single raster
out_composite_rasters = Apply([Band1, Band2, Band3], 'CompositeBand')
```

### Example 4

```python
# Apply Heat Index function to multidimensional raster objects

import arcpy
from arcpy.ia import *

# Set input multidimensional raster dataset
in_raster = Raster("C:\\test.gdb\ClimateData", True) 

# Select the relative humidity variable
RH = Subset(ClimateData, variables = 'rh')

# Select the temperature variable
Temp = Subset(ClimateData, variables = 't')

# Apply the Heat Index function to the two multidimensional raster subsets
# The output is a multidimensional raster where each slice is the heat index for the slice's time
heat_index_raster= Apply({'temperature': Temp, 'rh': RH}, 'HeatIndex', {'units':'Kelvin', 'outUnits':'Fahrenheit'})
```

### Example 5

```python
# Apply Heat Index function to multidimensional raster objects

import arcpy
from arcpy.ia import *

# Set input multidimensional raster dataset
in_raster = Raster("C:\\test.gdb\ClimateData", True) 

# Select the relative humidity variable
RH = Subset(ClimateData, variables = 'rh')

# Select the temperature variable
Temp = Subset(ClimateData, variables = 't')

# Apply the Heat Index function to the two multidimensional raster subsets
# The output is a multidimensional raster where each slice is the heat index for the slice's time
heat_index_raster= Apply({'temperature': Temp, 'rh': RH}, 'HeatIndex', {'units':'Kelvin', 'outUnits':'Fahrenheit'})
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
elevRasterClip = arcpy.ia.ApplyEnvironment(elevMeter)
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
elevRasterClip = arcpy.ia.ApplyEnvironment(elevMeter)
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

argstat_raster = arcpy.ia.ArgStatistics("Temperature_30_years.crf", "MAX","","", 9999)
```

### Example 3

```python
import arcpy

argstat_raster = arcpy.ia.ArgStatistics("Temperature_30_years.crf", "MAX","","", 9999)
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/iapyexamples/output/outdivide")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/iapyexamples/output/outdivide")
```

### Example 3

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/iapyexamples/output/outdivide2")
```

### Example 4

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/iapyexamples/output/outdivide2")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/iapyexamples/output/outdivide")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outDivide = Raster("degs") / Raster("negs")
outDivide.save("C:/iapyexamples/output/outdivide")
```

### Example 3

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/iapyexamples/output/outdivide2")
```

### Example 4

```python
# Name: Op_Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster01 = Raster("elevation")
inRaster02 = Raster("landuse")

# Execute Divide
outDivide = inRaster01 / inRaster02

# Save the output 
outDivide.save("C:/iapyexamples/output/outdivide2")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outMinus = Raster("degs") - Raster("negs")
outMinus.save("C:/iapyexamples/output/outminus")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outMinus = Raster("degs") - Raster("negs")
outMinus.save("C:/iapyexamples/output/outminus")
```

### Example 3

```python
# Name: Op_Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Minus
outMinus = inRaster1 - inRaster2

# Save the output 
outMinus.save("C:/iapyexamples/output/outminus.tif")
```

### Example 4

```python
# Name: Op_Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Minus
outMinus = inRaster1 - inRaster2

# Save the output 
outMinus.save("C:/iapyexamples/output/outminus.tif")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outMod = Raster("degs") % Raster("negs")
outMod.save("C:/iapyexamples/output/outmod.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outMod = Raster("degs") % Raster("negs")
outMod.save("C:/iapyexamples/output/outmod.tif")
```

### Example 3

```python
# Name: Op_Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Mod
outMod = inRaster1 % inRaster2

# Save the output 
outMod.save("C:/iapyexamples/output/outmod")
```

### Example 4

```python
# Name: Op_Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute Mod
outMod = inRaster1 % inRaster2

# Save the output 
outMod.save("C:/iapyexamples/output/outmod")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outNegate = - Raster("degs")
outNegate.save("C:/iapyexamples/output/outneg")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outNegate = - Raster("degs")
outNegate.save("C:/iapyexamples/output/outneg")
```

### Example 3

```python
# Name: Op_Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a cell-by-cell basis 
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outNegate = -(inRaster)

# Save the output 
outNegate.save("C:/iapyexamples/output/outnegate")
```

### Example 4

```python
# Name: Op_Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a cell-by-cell basis 
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outNegate = -(inRaster)

# Save the output 
outNegate.save("C:/iapyexamples/output/outnegate")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outPlus = Raster("degs") + Raster("negs")
outPlus.save("C:/iapyexamples/output/outplus.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outPlus = Raster("degs") + Raster("negs")
outPlus.save("C:/iapyexamples/output/outplus.img")
```

### Example 3

```python
# Name: Op_Plus_Ex_02.py
# Description: Adds the values of two rasters on a cell-by-cell basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("cost")
inRaster2 = Raster("degs")

# Execute Plus
outPlus = inRaster1 + inRaster2

# Save the output 
outPlus.save("C:/iapyexamples/output/outplus")
```

### Example 4

```python
# Name: Op_Plus_Ex_02.py
# Description: Adds the values of two rasters on a cell-by-cell basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("cost")
inRaster2 = Raster("degs")

# Execute Plus
outPlus = inRaster1 + inRaster2

# Save the output 
outPlus.save("C:/iapyexamples/output/outplus")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outPower = Raster("degs") ** Raster("cost")
outPower.save("C:/iapyexamples/output/outpower.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outPower = Raster("degs") ** Raster("cost")
outPower.save("C:/iapyexamples/output/outpower.img")
```

### Example 3

```python
# Name: Op_Power_Ex_02.py
# Description: Raises the cells in a raster to the power of the values
#              found in another raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("cost")

# Execute Power
outPower = inRaster1 ** inRaster2

# Save the output 
outPower.save("C:/iapyexamples/output/outpower")
```

### Example 4

```python
# Name: Op_Power_Ex_02.py
# Description: Raises the cells in a raster to the power of the values
#              found in another raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("cost")

# Execute Power
outPower = inRaster1 ** inRaster2

# Save the output 
outPower.save("C:/iapyexamples/output/outpower")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outTimes = Raster("elevation") * 0.3048
outTimes.save("C:/iapyexamples/output/outtimes")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outTimes = Raster("elevation") * 0.3048
outTimes.save("C:/iapyexamples/output/outtimes")
```

### Example 3

```python
# Name: Op_Times_Ex_02.py
# Description: Multiplies the values of two rasters on a cell-by-cell basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("elevation")
inConstant = 0.3048

# Execute Times
outTimes = inRaster * inConstant

# Save the output 
outTimes.save("C:/iapyexamples/output/timesout")
```

### Example 4

```python
# Name: Op_Times_Ex_02.py
# Description: Multiplies the values of two rasters on a cell-by-cell basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("elevation")
inConstant = 0.3048

# Execute Times
outTimes = inRaster * inConstant

# Save the output 
outTimes.save("C:/iapyexamples/output/timesout")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outUnaryPlus = + Raster("degs")
outUnaryPlus.save("C:/iapyexamples/output/outdeg")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outUnaryPlus = + Raster("degs")
outUnaryPlus.save("C:/iapyexamples/output/outdeg")
```

### Example 3

```python
# Name: Op_UnaryPlus_Ex_02.py
# Description: Returns the cell valuesof the input raster on a cell-by-cell 
#    basis. 
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outUnaryPlus = +(inRaster)

# Save the output 
outUnaryPlus.save("C:/iapyexamples/output/outunplus")
```

### Example 4

```python
# Name: Op_UnaryPlus_Ex_02.py
# Description: Returns the cell valuesof the input raster on a cell-by-cell 
#    basis. 
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute Negate
outUnaryPlus = +(inRaster)

# Save the output 
outUnaryPlus.save("C:/iapyexamples/output/outunplus")
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

new_raster = arcpy.ia.Arithmetic("Raster1.tif","Raster2.tif", "Multiply", "UnionOf", "FirstOf")
```

### Example 3

```python
import arcpy

new_raster = arcpy.ia.Arithmetic("Raster1.tif","Raster2.tif", "Multiply", "UnionOf", "FirstOf")
```

---

## Aspect

## Summary

Identifies the downslope direction of the maximum rate of change in value from each cell to its neighbors.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |

## Code Samples

### Example 1

```python
Aspect (raster)
```

### Example 2

```python
from arcpy.ia import *
out_aspect_raster = Aspect("elevation.tif")
out_aspect_raster.save("C:/arcpyExamples/outputs/aspect.tif")
```

### Example 3

```python
from arcpy.ia import *
out_aspect_raster = Aspect("elevation.tif")
out_aspect_raster.save("C:/arcpyExamples/outputs/aspect.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "elevation.tif"

# Execute Aspect function
out_aspect_raster = Aspect(in_raster)

# Save the output
out_aspect_raster.save("C:/arcpyExamples/outputs/aspect.tif")
```

### Example 5

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "elevation.tif"

# Execute Aspect function
out_aspect_raster = Aspect(in_raster)

# Save the output
out_aspect_raster.save("C:/arcpyExamples/outputs/aspect.tif")
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
from arcpy.ia import *
out_aspectslope_raster = AspectSlope("elevation.tif", 3)
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

### Example 3

```python
from arcpy.ia import *
out_aspectslope_raster = AspectSlope("elevation.tif", 3)
out_aspectslope_raster.save("C:/arcpyExamples/outputs/aspectslope.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
import arcpy

BAI_raster = arcpy.ia.BAI("Landsat8_SurfaceReflectance.tif", red_band_id = 4, nir_band_id = 5)
```

### Example 5

```python
import arcpy

BAI_raster = arcpy.ia.BAI("Landsat8_SurfaceReflectance.tif", red_band_id = 4, nir_band_id = 5)
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

SimpleRatio = arcpy.ia.BandArithmetic("Landsat8.tif","5 4", 11)
```

### Example 3

```python
import arcpy

SimpleRatio = arcpy.ia.BandArithmetic("Landsat8.tif","5 4", 11)
```

### Example 4

```python
import arcpy

BandAddition_raster = arcpy.ia.BandArithmetic("Landsat8.tif","B2+B3", 0)
```

### Example 5

```python
import arcpy

BandAddition_raster = arcpy.ia.BandArithmetic("Landsat8.tif","B2+B3", 0)
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBitwiseLS = Raster("degs") << Raster("negs")
outBitwiseLS.save("C:/iapyexamples/output/outbitls.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBitwiseLS = Raster("degs") << Raster("negs")
outBitwiseLS.save("C:/iapyexamples/output/outbitls.tif")
```

### Example 3

```python
# Name: Op_BitwiseLeftShift_Ex_02.py
# Description: Performs a Bitwise Left Shift operation on the binary
#     values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseLeftShift
outBitwiseLShift = inRaster1 << inRaster2

# Save the output 
outBitwiseLShift.save("C:/iapyexamples/output/outlshift")
```

### Example 4

```python
# Name: Op_BitwiseLeftShift_Ex_02.py
# Description: Performs a Bitwise Left Shift operation on the binary
#     values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseLeftShift
outBitwiseLShift = inRaster1 << inRaster2

# Save the output 
outBitwiseLShift.save("C:/iapyexamples/output/outlshift")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBitwiseRShift = Raster("degs") >> Raster("negs")
outBitwiseRShift.save("C:/iapyexamples/output/outbitrs")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBitwiseRShift = Raster("degs") >> Raster("negs")
outBitwiseRShift.save("C:/iapyexamples/output/outbitrs")
```

### Example 3

```python
# Name: Op_BitwiseRightShift_Ex_02.py
# Description: Performs a Bitwise Right Shift operation on the binary
#              values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseRightShift
outBitwiseRShift = inRaster1 >> inRaster2

# Save the output 
outBitwiseRShift.save("C:/iapyexamples/output/outbitrshift.img")
```

### Example 4

```python
# Name: Op_BitwiseRightShift_Ex_02.py
# Description: Performs a Bitwise Right Shift operation on the binary
#              values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BitwiseRightShift
outBitwiseRShift = inRaster1 >> inRaster2

# Save the output 
outBitwiseRShift.save("C:/iapyexamples/output/outbitrshift.img")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanAnd = Raster("degs") & Raster("negs")
outBooleanAnd.save("C:/iapyexamples/output/outbooland.img")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanAnd = Raster("degs") & Raster("negs")
outBooleanAnd.save("C:/iapyexamples/output/outbooland.img")
```

### Example 3

```python
# Name: Op_BooleanAnd_Ex_02.py
# Description: Performs a Boolean And operation on the cell values
#              of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanAnd
outBooleanAnd = inRaster1 & inRaster2

# Save the output 
outBooleanAnd.save("C:/iapyexamples/output/outbooland")
```

### Example 4

```python
# Name: Op_BooleanAnd_Ex_02.py
# Description: Performs a Boolean And operation on the cell values
#              of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanAnd
outBooleanAnd = inRaster1 & inRaster2

# Save the output 
outBooleanAnd.save("C:/iapyexamples/output/outbooland")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"outBooleanNot = ~ Raster("degs")
outBooleanNot.save("C:/iapyexamples/output/outboolnot.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"outBooleanNot = ~ Raster("degs")
outBooleanNot.save("C:/iapyexamples/output/outboolnot.tif")
```

### Example 3

```python
# Name: Op_BooleanNot_Ex_02.py
# Description: Performs a Boolean complement (NOT) operation on the
#              cell values of an input raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute BooleanNot
outBooleanNot = ~ inRaster

# Save the output 
outBooleanNot.save("C:/iapyexamples/output/outboolnot")
```

### Example 4

```python
# Name: Op_BooleanNot_Ex_02.py
# Description: Performs a Boolean complement (NOT) operation on the
#              cell values of an input raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = Raster("degs")

# Execute BooleanNot
outBooleanNot = ~ inRaster

# Save the output 
outBooleanNot.save("C:/iapyexamples/output/outboolnot")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanOr = Raster("degs") | Raster("negs")
outBooleanOr.save("C:/iapyexamples/output/outboolor2")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanOr = Raster("degs") | Raster("negs")
outBooleanOr.save("C:/iapyexamples/output/outboolor2")
```

### Example 3

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/iapyexamples/output/outboolor")
```

### Example 4

```python
# Name: Op_BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanOr
outBooleanOr = inRaster1 | inRaster2

# Save the output 
outBooleanOr.save("C:/iapyexamples/output/outboolor")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanXOr = Raster("degs") ^ Raster("negs")
outBooleanXOr.save("C:/iapyexamples/output/outboolxor.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outBooleanXOr = Raster("degs") ^ Raster("negs")
outBooleanXOr.save("C:/iapyexamples/output/outboolxor.tif")
```

### Example 3

```python
# Name: Op_BooleanXOr_Ex_02.py
# Description: Performs a Boolean Exclusive Or operation on the
#              cell values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanXOr
outBooleanXOr = inRaster1 ^ inRaster2

# Save the output 
outBooleanXOr.save("C:/iapyexamples/output/outboolxor")
```

### Example 4

```python
# Name: Op_BooleanXOr_Ex_02.py
# Description: Performs a Boolean Exclusive Or operation on the
#              cell values of two input rasters
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute BooleanXOr
outBooleanXOr = inRaster1 ^ inRaster2

# Save the output 
outBooleanXOr.save("C:/iapyexamples/output/outboolxor")
```

---

## Buffered

## Summary

Stores the pixel block of the input raster in memory to optimize performance when the raster is used multiple times in an expression.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |

## Code Samples

### Example 1

```python
NewRaster = (Raster1+Raster2)/Raster1
```

### Example 2

```python
NewRaster = (Raster1+Raster2)/Raster1
```

### Example 3

```python
Buffered (raster)
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
Raster1 = arcpy.Raster("Band_3")
Raster2 = arcpy.Raster("Band_4")

# Execute Buffered function
Raster1buff = arcpy.ia.Buffered(Raster1)
Raster2buff = arcpy.ia.Buffered(Raster2)

# Run complex expression
Output = (Raster1buff+Raster2buff)/(Raster1buff+Raster2buff)

# Save output
Output.save("C:/arcpyExamples/outputs/expressionOutput.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
Raster1 = arcpy.Raster("Band_3")
Raster2 = arcpy.Raster("Band_4")

# Execute Buffered function
Raster1buff = arcpy.ia.Buffered(Raster1)
Raster2buff = arcpy.ia.Buffered(Raster2)

# Run complex expression
Output = (Raster1buff+Raster2buff)/(Raster1buff+Raster2buff)

# Save output
Output.save("C:/arcpyExamples/outputs/expressionOutput.tif")
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

CIg_raster = arcpy.ia.CIg("Landsat8.tif", 5, 3)
```

### Example 5

```python
import arcpy

CIg_raster = arcpy.ia.CIg("Landsat8.tif", 5, 3)
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

CIre_raster = arcpy.ia.CIre("Sentinel2.tif", 8, 5)
```

### Example 5

```python
import arcpy

CIre_raster = arcpy.ia.CIre("Sentinel2.tif", 8, 5)
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
from arcpy.ia import *
out_classify_raster = Classify("NAIP.tif",None,
                               "C:/arcpyExamples/data/vegetation_class.ecd")
out_classify_raster.save("C:/arcpyexamples/outputs/classify_output.tif")
```

### Example 3

```python
from arcpy.ia import *
out_classify_raster = Classify("NAIP.tif",None,
                               "C:/arcpyExamples/data/vegetation_class.ecd")
out_classify_raster.save("C:/arcpyexamples/outputs/classify_output.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster1 = "C:/data/NAIP.tif"
raster2 = None
classifier_definition = "C:/data/vegetation_class.ecd"


# Apply Classify function
classified_raster = arcpy.ia.classify(raster1, raster2, classifier_definition)

# Save the output
classified_raster.save("C:/arcpyExamples/outputs/Vegetation_landcover.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster1 = "C:/data/NAIP.tif"
raster2 = None
classifier_definition = "C:/data/vegetation_class.ecd"


# Apply Classify function
classified_raster = arcpy.ia.classify(raster1, raster2, classifier_definition)

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

ClayMinerals_raster = arcpy.ia.ClayMinerals("Sentinel2.tif", 11, 12)
```

### Example 5

```python
import arcpy

ClayMinerals_raster = arcpy.ia.ClayMinerals("Sentinel2.tif", 11, 12)
```

---

## Clip

## Summary

Creates a raster object that is clipped according to the extent of an input raster dataset or the shape of an input polygon feature class.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input raster. | Raster |
| aoi | Defines the area of interest (AOI), or clipping extent, used to clip the raster. Supported AOI options include Raster, Extent, and Polygon geometry. | Extent |

## Code Samples

### Example 1

```python
Clip (in_raster, aoi)
```

### Example 2

```python
import arcpy
from arcpy.ia import *


# Set input raster
in_raster = arcpy.Raster("USA_Landcover.tif")

# Clip the raster using a feature extent
clip_raster = arcpy.ia.Clip(in_raster, aoi = "C:\Data\California_State.shp")
clip_raster.save("California_Landcover.tif")
```

### Example 3

```python
import arcpy
from arcpy.ia import *


# Set input raster
in_raster = arcpy.Raster("USA_Landcover.tif")

# Clip the raster using a feature extent
clip_raster = arcpy.ia.Clip(in_raster, aoi = "C:\Data\California_State.shp")
clip_raster.save("California_Landcover.tif")
```

### Example 4

```python
import arcpy
from arcpy.ia import *

# Set input raster
in_raster = arcpy.Raster("us_landcover.tif")

# Create a polygon geometry object using the array object
coordinates = [[-102.78838, 42.9953], [-104.0594, 43.8529], 
	[-104.0489, 45.942993], [-102.78838, 42.9953]]
array = arcpy.Array([arcpy.Point(x, y) for x, y in coordinates])
polygon_geometry=arcpy.Polygon(array, arcpy.SpatialReference(4326))

# Clip the raster using the polygon geometry
clip_raster = arcpy.ia.Clip(in_raster, aoi = polygon_geometry)
clip_raster.save("landcover_clipped_by_polygon_geometry.tif")
```

### Example 5

```python
import arcpy
from arcpy.ia import *

# Set input raster
in_raster = arcpy.Raster("us_landcover.tif")

# Create a polygon geometry object using the array object
coordinates = [[-102.78838, 42.9953], [-104.0594, 43.8529], 
	[-104.0489, 45.942993], [-102.78838, 42.9953]]
array = arcpy.Array([arcpy.Point(x, y) for x, y in coordinates])
polygon_geometry=arcpy.Polygon(array, arcpy.SpatialReference(4326))

# Clip the raster using the polygon geometry
clip_raster = arcpy.ia.Clip(in_raster, aoi = polygon_geometry)
clip_raster.save("landcover_clipped_by_polygon_geometry.tif")
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
from arcpy.ia import *
out_slope_with_colormap = ColormapToRGB("elevation_raster.tif")
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/elevtion_rgb_3bands.tif")
```

### Example 3

```python
from arcpy.ia import *
out_slope_with_colormap = ColormapToRGB("elevation_raster.tif")
out_slope_rgb_3bands.save("C:/arcpyExamples/outputs/elevtion_rgb_3bands.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *
out_hsv_3bands = ColorspaceConversion("slope_rgb_3bands.tif", "rgb_to_hsv")
out_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

### Example 3

```python
from arcpy.ia import *
out_hsv_3bands = ColorspaceConversion("slope_rgb_3bands.tif", "rgb_to_hsv")
out_hsv_3bands.save("C:/arcpyExamples/outputs/slope_hsv_3bands.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *
out_magnitude_raster = Complex("itemgrd")
out_magnitude_raster.save("C:/arcpyexamples/outputs/out_magnitude_radar.crf")
```

### Example 3

```python
from arcpy.ia import *
out_magnitude_raster = Complex("itemgrd")
out_magnitude_raster.save("C:/arcpyexamples/outputs/out_magnitude_radar.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

compband_raster = arcpy.ia.CompositeBand(["Band1.TIF", "Band2.TIF", "Band3.TIF"])
```

### Example 3

```python
import arcpy

compband_raster = arcpy.ia.CompositeBand(["Band1.TIF", "Band2.TIF", "Band3.TIF"])
```

---

## ComputeChange

## Summary

Creates a raster object that contains the difference between two categorical or continuous rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster1 | The first raster to be used in the computation. To evaluate change from time 1 (earlier) to time 2 (later), enter the time 1 raster here. | Raster |
| raster2 | The second raster to be used in the computation. To evaluate change from time 1 (earlier) to time 2 (later), enter the time 2 raster here. | Raster |
| method | Specifies the method to use to compute the difference between the two rasters.DIFFERENCE—The mathematical difference, or subtraction, between the pixel values in the input rasters will be calculated. This is the default.RELATIVE_DIFFERENCE—The difference in pixel values, accounting for the magnitudes of the values being compared, will be calculated.CATEGORICAL_DIFFERENCE—The difference between two categorical or thematic rasters will be calculated, where the output contains class transitions that occurred between the two rasters.(The default value is DIFFERENCE) | String |
| from_class_values[from_class_values,...] | The list of class values from raster1 to include in the computation, if method is set to CATEGORICAL_DIFFERENCE. For example, if you want to identify the areas that changed from Forest to Urban, enter the class value for the Forest class here.If no value is provided, all classes are included. | Integer |
| to_class_values[to_class_values,...] | The list of class values from raster2 to include in the computation, if method is set to CATEGORICAL_DIFFERENCE. For example, if you want to identify the areas that changed from Forest to Urban, enter the class value for the Urban class here.If no value is provided, all classes are included. | Integer |
| filter_method | Specifies the pixels to categorize in the output raster object, if method is set to CATEGORICAL_DIFFERENCE.ALL—All pixels will be categorized in the output. For example, pixels that changed from Forest to Urban will be categorized in a transition class named Forest>Urban. Pixels that started as Forest and remained Forest will be categorized in a class named Forest.CHANGED_PIXELS_ONLY—Only the pixels that changed from one class type to a different class type will be categorized in transitional classes. Pixels that did not change will be grouped in a class named Other. This is the default.UNCHANGED_PIXELS_ONLY—Only the pixels that did not change classes will be categorized. Pixels that did change will be grouped in a class named Other.(The default value is CHANGE_PIXELS_ONLY) | String |
| define_transition_colors | Specifies the color to use to symbolize class transition categories, if method is set to CATEGORICAL_DIFFERENCE and filter_method is set to either CHANGED_PIXELS_ONLY or ALL.AVERAGE—Transition classes will be given the color that is the average of the from and to class colors. For example, pixels in the Forest>Urban class will have a color that is the average of the Forest class in raster1 and the Urban class in raster2.This is the default.FROM_COLOR—Transition classes will be given the color of the original class from raster1.TO_COLOR—Transition classes will be given the color of the final class from raster2.(The default value is AVERAGE) | String |
| extent_type | Specifies the spatial extent used to create the output raster.FirstOf—The extent of the first raster variableIntersectionOf—The minimum area common to all input rastersUnionOf—The combined extent of all input rastersLastOf—The extent of the last raster variable(The default value is IntersectionOf) | String |
| cellsize_type | Specifies the cell size used to create the output raster.FirstOf—The cell size of the first raster variableMinOf—The minimum cell size of the input rastersMaxOf—The maximum cell size of the input rastersMeanOf—The average cell size of the input rastersLastOf—The cell size of the last raster variable(The default value is MaxOf) | String |

## Code Samples

### Example 1

```python
ComputeChange (raster1, raster2, {method}, {from_class_values}, {to_class_values}, {filter_method}, {define_transition_colors}, {extent_type}, {cellsize_type})
```

### Example 2

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

raster1 = arcpy.Raster('Landcover_2000.tif')
raster2 = arcpy.Raster('Landcover_2020.tif')

# Compute only the change that occured in land cover between 2000 and 2020
changed_landcover = arcpy.ia.ComputeChange(raster1, raster2,
	"CATEGORICAL_DIFFERENCE",[41,42,43],[21,22,23],"CHANGED_PIXELS_ONLY",
	"AVERAGE","IntersectionOf","MaxOf")
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

raster1 = arcpy.Raster('Landcover_2000.tif')
raster2 = arcpy.Raster('Landcover_2020.tif')

# Compute only the change that occured in land cover between 2000 and 2020
changed_landcover = arcpy.ia.ComputeChange(raster1, raster2,
	"CATEGORICAL_DIFFERENCE",[41,42,43],[21,22,23],"CHANGED_PIXELS_ONLY",
	"AVERAGE","IntersectionOf","MaxOf")
```

---

## Contour

## Summary

Creates a raster object for contour lines by joining points with the same value from a raster dataset. The contours are isolines created as rasters for visualization.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| adaptive_smoothing | The amount of smoothing to apply to the contour line. A lower value produces a contour line with more granularity and less smoothing, while a higher value produces a contour line with more smoothing that appears less jagged. (The default value is 2.5) | Double |
| contour_type | The type of contour to be created.contour lines— Joins points of equal elevation to create a line representing constant elevation.contour fill— Fills the area between every contour line with the quantized elevation value.smooth surface only— Smooths the input elevation layer but does not produce contours.(The default value is contour lines) | String |
| z_base | The base contour value. Contours are generated above and below this value as needed to cover the entire value range of the input raster.A value of 0 often represents mean sea level, depending on the source elevation dataset.(The default value is 0) | Double |
| number_of_contours | The number of contours to be generated. This dynamically adjusts the contour interval to fit the terrain in the display while maintaining standardized intervals such as 1, 5, 10, and so on.(The default value is 0) | Integer |
| contour_interval | The difference in altitude between contour lines.A small contour interval is used in relatively flat areas, while larger contour intervals are used in variable or mountainous terrain.(The default value is 100) | Double |
| nth_contour_line_in_bold | The index contour, which is represented as a bold line.(The default value is 5) | Integer |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |

## Code Samples

### Example 1

```python
Contour (raster, {adaptive_smoothing}, {contour_type}, {z_base}, {number_of_contours}, {contour_interval}, {nth_contour_line_in_bold}, {z_factor})
```

### Example 2

```python
from arcpy.ia import *
out_contour_raster = Contour("contour_input.tif", "", "smooth surface only", "", "", 150, 10, 2)
out_contour_raster.save("C:/arcpyexamples/outputs/contour_surface.tif")
```

### Example 3

```python
from arcpy.ia import *
out_contour_raster = Contour("contour_input.tif", "", "smooth surface only", "", "", 150, 10, 2)
out_contour_raster.save("C:/arcpyexamples/outputs/contour_surface.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "contour_input.tif"

# Execute Contour function
out_contour_raster = Contour(in_raster, 3, "contour fill", 10, 20, 10, 3)

# Save the output
out_contour_raster.save("C:/arcpyExamples/outputs/contour_fill.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "contour_input.tif"

# Execute Contour function
out_contour_raster = Contour(in_raster, 3, "contour fill", 10, 20, 10, 3)

# Save the output
out_contour_raster.save("C:/arcpyExamples/outputs/contour_fill.tif")
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

ContrastBrightness_raster = arcpy.ia.ContrastBrightness(in_raster1, -50, 100)
```

### Example 3

```python
import arcpy

ContrastBrightness_raster = arcpy.ia.ContrastBrightness(in_raster1, -50, 100)
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

Convolution_raster = arcpy.ia.Convolution(imagePath1, 15)
```

### Example 3

```python
import arcpy

Convolution_raster = arcpy.ia.Convolution(imagePath1, 15)
```

---

## Curvature

## Summary

Displays the shape or curvature of the slope, which can be concave or convex and can be understood from the curvature value. The curvature is calculated by computing the second derivative of the surface.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster dataset. | Raster |
| curvature_type | The curvature type accentuates different aspects of the slope.standard—Combines the profile and planform curvatures.planform—Is perpendicular to the direction of the maximum slope. It affects the convergence and divergence of flow across a surface.profile— Is parallel to the slope and indicates the direction of maximum slope. It affects the acceleration and deceleration of flow across the surface.(The default value is standard) | String |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |

## Code Samples

### Example 1

```python
Curvature (raster, curvature_type, {z_factor})
```

### Example 2

```python
from arcpy.ia import *
out_curvature_raster = Curvature("curvature_input.tif", "profile", 2)
out_curvature_raster.save("C:/arcpyExamples/outputs/curv_profile.tif")
```

### Example 3

```python
from arcpy.ia import *
out_curvature_raster = Curvature("curvature_input.tif", "profile", 2)
out_curvature_raster.save("C:/arcpyExamples/outputs/curv_profile.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "curvature_input.tif"

# Execute Curvature function
out_curvature_raster = Curvature(in_raster, "planform", 3)

# Save the output
out_curvature_raster.save("C:/arcpyExamples/outputs/cur_planform.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "curvature_input.tif"

# Execute Curvature function
out_curvature_raster = Curvature(in_raster, "planform", 3)

# Save the output
out_curvature_raster.save("C:/arcpyExamples/outputs/cur_planform.tif")
```

---

## DetectChangeUsingChangeAnalysis

## Summary

Uses a change analysis raster to create a raster object containing date-of-change information.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input change analysis raster generated with the Analyze Changes Using CCDC tool or the Analyze Changes Using LandTrendr tool. | Raster |
| change_type | Specifies the type of change to be extracted from the change analysis raster.TIME_OF_LATEST_CHANGE—Each pixel will contain the date of the most recent change for that pixel in the time series. This is the default.TIME_OF_EARLIEST_CHANGE—Each pixel will contain the date of the earliest change for that pixel in the time series.TIME_OF_LARGEST_CHANGE—Each pixel will contain the date of the most significant change for that pixel in the time series.NUM_OF_CHANGES—Each pixel will contain the total number of times the pixel changed in the time series.TIME_OF_LONGEST_CHANGE—Each pixel contains the date of change at the beginning or end of the longest transition segment in the time series.TIME_OF_SHORTEST_CHANGE—Each pixel contains the date of change at the beginning or end of the shortest transition segment in the time series.TIME_OF_FASTEST_CHANGE—Each pixel contains the date of change at the beginning or end of the transition that occurred most quickly.TIME_OF_SLOWEST_CHANGE—Each pixel contains the date of change at the beginning or end of the transition that occurred most slowly.(The default value is TIME_OF_LATEST_CHANGE) | String |
| max_number_of_changes | The maximum number of changes per pixel to be calculated. This number corresponds to the number of bands in the output raster. The default is 1, meaning only one change date will be calculated, and the output raster will contain only one band. This parameter is not available when the change_type parameter is set to NUM_OF_CHANGES.(The default value is 1) | Integer |
| segment_date | Specifies whether to extract the date at the beginning of a change segment, or the end.This parameter is available only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr tool.BEGINNING_OF_SEGMENT—Extract the date at the beginning of a change segment. This is the default.END_OF_SEGMENT—Extract the date at the end of a change segment. (The default value is BEGINNING_OF_SEGMENT) | String |
| change_direction | Specifies the direction of change to be included in the analysis.This parameter is available only when the input change analysis raster is the output from the Analyze Changes Using LandTrendr tool.ALL—All change directions are included in the output. This is the default.INCREASE—Only change in the positive or increasing direction is included in the output.DECREASE—Only change in the negative or decreasing direction is included in the output.(The default value is ALL) | String |
| filter_by_year | Specifies whether to filter by a range of years. True—Filter results so that only changes that occurred within a specific range of years are included in the output.False—Do not filter results by year. This is the default.(The default value is False) | Boolean |
| min_year | The earliest year to use to filter results. This parameter is required if the filter_by_year parameter is set to True.(The default value is 1970) | Double |
| max_year | The latest year to use to filter results. This parameter is required if the filter_by_year parameter is set to True.(The default value is 2020) | Double |
| filter_by_duration | Specifies whether to filter by the duration of a change event. True—Filter results by duration so that only the changes that lasted a given amount of time are included in the output.False—Do not filter results by duration. This is the default.(The default value is False) | Boolean |
| min_duration | The minimum number of consecutive years to include in the results. This parameter is required if the filter_by_duration parameter is set to True.(The default value is 0) | Double |
| min_duration | The maximum number of consecutive years to include in the results. This parameter is required if the filter_by_duration parameter is set to True.(The default value is 50) | Double |
| filter_by_magnitude | Specifies whether to filter by the magnitude of change.True—Filter results by magnitude so that only the changes of a given magnitude are included in the output.False—Do not filter results by magnitude. This is the default.(The default value is False) | Boolean |
| min_magnitude | The minimum change magnitude to include in the results. This parameter is required if the filter_by_magnitude parameter is set to True.(The default value is -50) | Double |
| max_magnitude | The maximum change magnitude to include in the results. This parameter is required if the filter_by_magnitude parameter is set to True.(The default value is 50) | Double |

## Code Samples

### Example 1

```python
DetectChangeUsingChangeAnalysis (raster, {change_type}, {max_number_of_changes}, {segment_date}, {change_direction}, {filter_by_year}, {min_year}, {max_year}, {filter_by_duration}, {min_duration}, {min_duration}, {filter_by_magnitude}, {min_magnitude}, {max_magnitude})
```

### Example 2

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

change_analysis_raster = arcpy.Raster('Landsat_CCDC.crf', True)

# Detect the dates of the three largest changes in pixel values over time
largest_change = arcpy.ia.DetectChangeUsingChangeAnalysis(
	change_analysis_raster, "TIME_OF_LARGEST_CHANGE", 3)
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

change_analysis_raster = arcpy.Raster('Landsat_CCDC.crf', True)

# Detect the dates of the three largest changes in pixel values over time
largest_change = arcpy.ia.DetectChangeUsingChangeAnalysis(
	change_analysis_raster, "TIME_OF_LARGEST_CHANGE", 3)
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
from arcpy.ia import *
out_evf_raster = ElevationVoidFill("elevation.tif", 0)
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

### Example 3

```python
from arcpy.ia import *
out_evf_raster = ElevationVoidFill("elevation.tif", 0)
out_evf_raster.save("C:/arcpyExamples/outputs/raster_evf.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

## EqualToFrequency

## Summary

Creates a raster object in which each pixel contains the number of times the values in a set of rasters are equal to another raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| value_raster | A value raster that will be referenced by the set of input rasters. | Raster |
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
EqualToFrequency (value_raster, rasters, {extent_type}, {cellsize_type}, {process_as_multiband})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
EqualTo_raster = EqualToFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
EqualTo_raster = EqualToFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
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

EVI_raster = arcpy.ia.EVI("Landsat8.tif", 5, 4, 2)
```

### Example 5

```python
import arcpy

EVI_raster = arcpy.ia.EVI("Landsat8.tif", 5, 4, 2)
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

out_bands_raster = arcpy.ia.ExtractBand("in_raster.tif", [1, 2])
```

### Example 3

```python
import arcpy

out_bands_raster = arcpy.ia.ExtractBand("in_raster.tif", [1, 2])
```

### Example 4

```python
import arcpy

out_bands_raster = arcpy.ia.ExtractBand("in_raster.tif", band_wavelengths=[500.00])
```

### Example 5

```python
import arcpy

out_bands_raster = arcpy.ia.ExtractBand("in_raster.tif", band_wavelengths=[500.00])
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

FerrousMinerals_raster = arcpy.ia.FerrousMinerals("Sentinel2.tif", 11, 8)
```

### Example 5

```python
import arcpy

FerrousMinerals_raster = arcpy.ia.FerrousMinerals("Sentinel2.tif", 11, 8)
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
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Create multidimensional raster object from 
# Landsat7 time series data in a mosaic dataset
in_raster = Raster('C:\\test.gdb\\Landsat7', True) 

# Calculate NDVI for each scene in the time series
out_NDVI_raster = Foreach(
	in_raster, "NDVI", {'VisibleBandID':3,'InfraredBandID':4})
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Create multidimensional raster object from 
# Landsat7 time series data in a mosaic dataset
in_raster = Raster('C:\\test.gdb\\Landsat7', True) 

# Calculate NDVI for each scene in the time series
out_NDVI_raster = Foreach(
	in_raster, "NDVI", {'VisibleBandID':3,'InfraredBandID':4})
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

GEMI_raster = arcpy.ia.GEMI("Landsat8.tif", 5, 4)
```

### Example 7

```python
import arcpy

GEMI_raster = arcpy.ia.GEMI("Landsat8.tif", 5, 4)
```

---

## GenerateTrend

## Summary

Estimates the trend for each pixel along a dimension for one or more variables in a multidimensional raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input multidimensional raster. | Raster |
| dimension_name | The name of the dimension along which a trend will be extracted for the variable or variables selected in the analysis. | String |
| regression_type | Specifies the type of line to be used to fit to the pixel values along a dimension.LINEAR—Variable pixel values will be fitted along a linear trend line. This is the default.HARMONIC—Variable pixel values will be fitted along a harmonic trend line.POLYNOMIAL—Variable pixel values will be fitted along a second-order polynomial trend line.MANN-KENDALL—Variable pixel values will be evaluated for monotonic trend using the Mann-Kendall trend test.SEASONAL-KENDALL—Variable pixel values will be evaluated for monotonic trend using the Seasonal-Kendall trend test.(The default value is LINEAR) | String |
| cycle_length | The length of periodic variation to model. This argument is required when regression_type is set to HARMONIC. For example, leaf greenness often has one strong cycle of variation in a single year, so cycle_length is 1 year. Hourly temperature data has one strong cycle of variation throughout a single day, so the cycle_length is 1 day. The default value is 1.(The default value is 1) | Integer |
| cycle_unit | Specifies the time unit to be used for the length of a harmonic cycle.DAYS—The unit for the length of the harmonic cycle is days.YEARS—The unit for the length of the harmonic cycle is years. This is the default.(The default value is YEARS) | String |
| harmonic_frequency | The number of models to use in the trend fitting when the regression_type is HARMONIC. The default is 1, or one harmonic cycle per year.This argument is only included in the trend analysis when the dimension being analyzed is time.(The default value is 1) | Integer |
| polynomial_order | The polynomial order number to use in the trend fitting when the regression_type is POLYNOMIAL. The default is 2, or second-order polynomial.This argument is only included in the trend analysis when the dimension being analyzed is time.(The default value is 2) | Integer |
| ignore_nodata | Specifies whether NoData values are ignored in the analysis.True—The analysis will include all valid pixels along a given dimension and ignore any NoData pixels. This is the default.False—The analysis will result in NoData if there are any NoData values for the pixels along the given dimension.(The default value is True) | Boolean |
| rmse | Specifies whether the root mean square error (RMSE) of the trend fit line will be calculated.True—The RMSE will be calculated. This is the default.False—The RMSE will not be calculated.(The default value is True) | Boolean |
| r2 | Specifies whether the R-squared goodness-of-fit statistic for the trend fit line will be calculated.True—The R-squared value will be calculated.False—The R-squared value will not be calculated. This is the default.(The default value is False) | Boolean |
| slope_p_value | Specifies whether the p-value statistic for the slope coefficient of the trend line will be calculated.True—The p-value will be calculated.False—The p-value will not be calculated. This is the default.(The default value is False) | Boolean |
| seasonal_period | Specifies the unit to use for seasonal period. This is required when the regression_type argument is set to SEASONAL-KENDALL.DAYS—The unit for the length of the seasonal period is days. This is the default.MONTHS—The unit for the length of the seasonal period is months.(The default value is DAYS) | String |

## Code Samples

### Example 1

```python
GenerateTrend (raster, dimension_name, {regression_type}, {cycle_length}, {cycle_unit}, {harmonic_frequency}, {polynomial_order}, {ignore_nodata}, {rmse}, {r2}, {slope_p_value}, {seasonal_period})
```

### Example 2

```python
# Import system modulesimport arcpy
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_multidimensional_raster = "C:/data/ndvi_time_series.crf"
dimension_name = "StdTime"
regression_type = "HARMONIC"
cycle_length = 1
cycle_unit = "YEARS"
harmonic_frequency = 1
polynomial_order = None
ignore_nodata = True

rmse = True
r2 = False
slope_p_value = False
seasonal_period = None

# Apply GenerateTrendRaster function
trend_raster = arcpy.ia.GenerateTrend(in_multidimensional_raster,
                dimension_name, regression_type, cycle_length, cycle_unit, 
				harmonic_frequency, polynomial_order, ignore_nodata, rmse,
				r2, slope_p_value, seasonal_period)

# Save the output
trend_raster.save("C:/arcpyExamples/outputs/ndvi_trend_raster.crf")
```

### Example 3

```python
# Import system modulesimport arcpy
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_multidimensional_raster = "C:/data/ndvi_time_series.crf"
dimension_name = "StdTime"
regression_type = "HARMONIC"
cycle_length = 1
cycle_unit = "YEARS"
harmonic_frequency = 1
polynomial_order = None
ignore_nodata = True

rmse = True
r2 = False
slope_p_value = False
seasonal_period = None

# Apply GenerateTrendRaster function
trend_raster = arcpy.ia.GenerateTrend(in_multidimensional_raster,
                dimension_name, regression_type, cycle_length, cycle_unit, 
				harmonic_frequency, polynomial_order, ignore_nodata, rmse,
				r2, slope_p_value, seasonal_period)

# Save the output
trend_raster.save("C:/arcpyExamples/outputs/ndvi_trend_raster.crf")
```

---

## Geometric

## Summary

Creates a raster object by producing an orthorectified image using a sensor definition and terrain model.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| geodata_transforms | The transformation method for the geometric function. Transformation methods include Polynomial, Projective, or Identity.(The default value is None) | String |
| append_geodata_xform | Specifies whether to append the geodata transform to the input raster.True—The geodata transform will be appended to the input raster.False—The geodata transform will not be appended to the input raster.(The default value is False) | Boolean |
| z_factor | The z-factor value to rescale to meters, if the input elevation dataset uses vertical units other than meters.(The default value is None) | Double |
| z_offset | The base value to be added to the elevation values in the DEM. Use this argument to offset elevation values that do not start at sea level.(The default value is None) | Double |
| constant_z | A constant elevation value to use for the function.(The default value is None) | Double |
| correct_geoid | The geoid correction converts orthometric heights using a geoid before applying an orthorectification to your imagery.Most elevation datasets, such as USGS NED or ArcGIS Online World elevation, use orthometric heights, so it is necessary to select the Geoid correction for compatibility with satellite RPCs, which require ellipsoidal heights.True—Apply the geoid (EGM96) correction to the z-values.False—Do not apply the geoid correction to the z-values.(The default value is False) | Boolean |
| tolerance | The maximum tolerable error in the geometric function, given in number of pixels.(The default value is None) | Double |
| dem | The DEM used to orthorectify the raster dataset.(The default value is None) | Raster |

## Code Samples

### Example 1

```python
Geometric (raster, {geodata_transforms}, {append_geodata_xform}, {z_factor}, {z_offset}, {constant_z}, {correct_geoid}, {tolerance}, {dem})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the local variables
raster = "C:/data/Image.JPG"
geodata_transforms = "Polynomial"
append_geodata_xform = True
z_factor = None
z_offset = None
constant_z = None 
correct_geoid = False 
tolerance = 2
dem = "C:/data/DEM.tif"


# Apply RegionGrow function
Orthorectified_raster = arcpy.ia.Geometric(raster, geodata_transforms, append_geodata_xform,
                   z_factor, z_offset, constant_z, correct_geoid,
                    tolerance, dem)

# Save the output
Orthorectified_raster.save("C:/arcpyExamples/outputs/Image_ortho.JPG")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the local variables
raster = "C:/data/Image.JPG"
geodata_transforms = "Polynomial"
append_geodata_xform = True
z_factor = None
z_offset = None
constant_z = None 
correct_geoid = False 
tolerance = 2
dem = "C:/data/DEM.tif"


# Apply RegionGrow function
Orthorectified_raster = arcpy.ia.Geometric(raster, geodata_transforms, append_geodata_xform,
                   z_factor, z_offset, constant_z, correct_geoid,
                    tolerance, dem)

# Save the output
Orthorectified_raster.save("C:/arcpyExamples/outputs/Image_ortho.JPG")
```

---

## GeometricMedian

## Summary

Calculates the geometric median across pixels in a time series of multiband imagery.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The input multiband rasters. | List |
| epsilon | The convergence value between two consecutive iterations. When epsilon is less than or equal to the specified value, the iteration will stop, and the result of the last iteration will be used.(The default value is 0.001) | Double |
| max_iteration | The maximum number of iterations to complete. The computation will end once this value is reached, regardless of the epsilon setting.(The default value is 10) | Integer |
| extent_type | Specifies the processing extent for the output raster.FirstOf—Use the extent of the first input raster to determine the processing extent.IntersectionOf—Use the extent of the overlapping pixels to determine the processing extent. This is the default.UnionOf—Use the extent of all the rasters to determine the processing extent.LastOf—Use the extent of the last input raster to determine the processing extent.(The default value is IntersectionOf) | String |
| cellsize_type | Specifies the cell size to use in the output raster.FirstOf—Use the first cell size of the input rasters. This is the default.MinOf—Use the smallest cell size of all the input rasters.MaxOf—Use the largest cell size of all the input rasters. This is the default.MeanOf—Use the mean cell size of all the input rasters.LastOf—Use the last cell size of the input rasters.(The default value is MaxOf) | String |

## Code Samples

### Example 1

```python
GeometricMedian (rasters, epsilon, {max_iteration}, {extent_type}, {cellsize_type})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

#Execute
geomedian = arcpy.ia.GeometricMedian(rc, {"epsilon": 0.001, "max_iteration": 5, "extent_type":"UnionOf", "CellsizeType": "FirstOf"})

# Save the output
geomedian.save("C:/arcpyExamples/outputs/geomedian_raster.crf")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

#Execute
geomedian = arcpy.ia.GeometricMedian(rc, {"epsilon": 0.001, "max_iteration": 5, "extent_type":"UnionOf", "CellsizeType": "FirstOf"})

# Save the output
geomedian.save("C:/arcpyExamples/outputs/geomedian_raster.crf")
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

GNDVI_raster = arcpy.ia.GNDVI("Landsat8.tif", 5, 3)
```

### Example 5

```python
import arcpy

GNDVI_raster = arcpy.ia.GNDVI("Landsat8.tif", 5, 3)
```

---

## Gradient

## Summary

Calculates the gradient along x, y, x,y, or a given dimension.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster[raster,...] | The input raster or list of rasters. | Raster |
| gradient_dimension | The available dimensions for which the gradient will be calculated.For nonmultidimensional input, available dimension options are X, Y, and XY.For multidimensional input, available dimension options are X, Y, XY, and all dimensions available in the data, including time (StdTime). If there are two or more dimensions, the gradient will be calculated on the gradient dimension for all slices in the available dimensions.The XY option outputs a 2-band raster in which band 1 represents the gradient along the x-dimension, and band 2 represents the gradient along the y-dimension.(The default value is X) | String |
| denominator_unit | The unit of the gradient denominator. The unit depends on the gradient_dimension argument value.The following options are available for X, Y, and XY:DEFAULT—The output will be the difference between adjacent cells. This is the default.CELLSIZE—The output will be the difference between adjacent cells divided by the cell size of the input. The output unit will be the same as the unit of the x,y coordinates of the input. If the data is in a geographic coordinate system, it will be converted to meters.The following options are available for StdTime:DEFAULT—The output will be the difference between adjacent slices. This is the default.PER_HOUR—The output will be the difference between adjacent slices divided by the difference between the time values and converted to the per-hour rate.PER_DAY—The output will be the difference between adjacent slices divided by the difference between their time values and converted to the per-day rate. PER_MONTH—The output will be the difference between adjacent slices divided by the difference between their time values and converted to the per-month rate.PER_YEAR—The output will be the difference between adjacent slices divided by the difference between their time values and converted to the per-year rate.PER_DECADE—The output will be the difference between adjacent slices divided by the difference between their time values and converted to the per-decade rate.The following options are available for dimensions other than time dimensions:DEFAULT—The output will be the difference between adjacent slices. This is the default.DIMENSION_INTERVAL—The output will be the difference between adjacent slices divided by the difference between their dimension values.(The default value is DEFAULT) | String |

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

### Example 7

```python
Gradient (raster, {gradient_dimension}, {denominator_unit})
```

### Example 8

```python
# Import system modules
import arcpy
from arcpy.ia import *
arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")
# Set local variables
input_raster = in_multidimensional_raster = "C:/data/landsat.crf"
gradient_dimension = “XY”
denominator_unit = “Cellsize”
# Apply Gradient function
gradient_raster = arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Save the output
gradient _raster.save("C:/output/landsat_xy_gradient.crf")
```

### Example 9

```python
# Import system modules
import arcpy
from arcpy.ia import *
arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")
# Set local variables
input_raster = in_multidimensional_raster = "C:/data/landsat.crf"
gradient_dimension = “XY”
denominator_unit = “Cellsize”
# Apply Gradient function
gradient_raster = arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Save the output
gradient _raster.save("C:/output/landsat_xy_gradient.crf")
```

### Example 10

```python
# Import system modules
import arcpy
from arcpy.ia import *
arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")
# Set local variables
input_raster = in_multidimensional_raster = "C:/data/ndvi_time_series.crf"
gradient_dimension = “StdTime”
denominator_unit = “Per Year”
# Apply Gradient function
gradient_raster = arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Save the output
gradient _raster.save("C:/output/ndvi_stdtime_gradient.crf")
```

### Example 11

```python
# Import system modules
import arcpy
from arcpy.ia import *
arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")
# Set local variables
input_raster = in_multidimensional_raster = "C:/data/ndvi_time_series.crf"
gradient_dimension = “StdTime”
denominator_unit = “Per Year”
# Apply Gradient function
gradient_raster = arcpy.ia.Gradient (raster, gradient_dimension, denominator_unit)
# Save the output
gradient _raster.save("C:/output/ndvi_stdtime_gradient.crf")
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
from arcpy.ia import *
out_grayscale_raster = Grayscale("imagery.tif")
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

### Example 3

```python
from arcpy.ia import *
out_grayscale_raster = Grayscale("imagery.tif")
out_grayscale_raster.save("C:/arcpyExamples/outputs/grayscale.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

## GreaterThanFrequency

## Summary

Creates a raster object in which each pixel contains the number of times a set of rasters is greater than another raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| value_raster | A value raster that will be referenced by the list of input rasters. | Raster |
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
GreaterThanFrequency (value_raster, rasters, {extent_type}, {cellsize_type}, {process_as_multiband})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
GreaterThan_raster = GreaterThanFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
GreaterThan_raster = GreaterThanFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
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

GVITM_raster = arcpy.ia.GVITM("LandsatTM.tif", 1, 2, 3, 4, 5, 7)
```

### Example 5

```python
import arcpy

GVITM_raster = arcpy.ia.GVITM("LandsatTM.tif", 1, 2, 3, 4, 5, 7)
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
from arcpy.ia import *
out_heatindex_raster = HeatIndex("temperature", "relative_humidity", "Celsius", "Kelvin")
out_heatindex_raster.save("C:/arcpyExamples/outputs/heat_index_K.tif")
```

### Example 5

```python
from arcpy.ia import *
out_heatindex_raster = HeatIndex("temperature", "relative_humidity", "Celsius", "Kelvin")
out_heatindex_raster.save("C:/arcpyExamples/outputs/heat_index_K.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

## HighestPosition

## Summary

Creates a raster object in which each pixel contains the position of the raster with the maximum value in a set of rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | None |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |

## Code Samples

### Example 1

```python
HighestPosition (rasters, {extent_type}, {cellsize_type})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
Highest_raster = HighestPosition(rasters, "UnionOf", "FirstOf")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
Highest_raster = HighestPosition(rasters, "UnionOf", "FirstOf")
```

---

## Hillshade

## Summary

Creates a raster object of a grayscale 3D representation of a surface by considering the illumination source location and shadows.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dem | The input elevation raster. | Raster |
| azimuth | Azimuth is the sun's relative position along the horizon (in degrees). This position is indicated by the angle of the sun measured clockwise from due north. An azimuth of 0 degrees indicates north, east is 90 degrees, south is 180 degrees, and west is 270 degrees.This parameter is only valid when the hillshade_type argument is set to TRADITIONAL. The default is 315 degrees, which is from the northwest.(The default value is 315) | Double |
| altitude | Altitude is the sun's angle of elevation above the horizon and ranges from 0 to 90 degrees. A value of 0 degrees indicates that the sun is on the horizon, that is, on the same horizontal plane as the frame of reference. A value of 90 degrees indicates that the sun is directly overhead.This parameter is only valid when the hillshade_type argument is set to TRADITIONAL. (The default value is 45) | Double |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |
| slope_type | The inclination of slope can be output as either a value in degrees or percent rise. Specify one of the following: DEGREE, PERCENTRISE, or SCALED. For more information, see Slope function. | Integer |
| ps_power | Accounts for the altitude changes (or scale) as the viewer zooms in and out on the map display. It is the exponent applied to the pixel size term in the equation that controls the rate at which the z-factor changes to avoid significant loss of relief.This parameter is only valid when slope_type is SCALED.(The default value is 0.664) | Double |
| psz_factor | Accounts for changes in scale as the viewer zooms in and out on the map display. The value controls the rate at which the z-factor changes.This parameter is only valid when slope_type is SCALED.(The default value is 0.024) | Double |
| remove_edge_effect | Using this option will avoid any resampling of artifacts that may occur along the edges of a raster. The output pixels along the edge of a raster or next to pixels without a value will be populated with NoData. It is recommended that you use this option only when there are other rasters with overlapping pixels available. When overlapping pixels are available, these areas of NoData will display the overlapping pixel values instead of being blank.False—Bilinear resampling will be applied uniformly to resample the output.True—Bilinear resampling will be used to resample the output, except along the edges of the rasters or next to pixels of NoData. These pixels will be populated with NoData. This will reduce any sharp edge effects that may otherwise occur.(The default value is False) | Boolean |
| hillshade_type | Controls the illumination source for the hillshade.0—Calculates hillshade from a single illumination direction. You can set the azimuth and altitude arguments to control the location of the light source.1—Combines light from multiple sources to represent an enhanced visualization of the terrain.(The default value is 0) | Integer |

## Code Samples

### Example 1

```python
Hillshade (dem, {azimuth}, {altitude}, {z_factor}, {slope_type}, {ps_power}, {psz_factor}, {remove_edge_effect}, {hillshade_type})
```

### Example 2

```python
from arcpy.ia import *
out_hillshade_raster = Hillshade("elevation.tif", 180, 75, 0.3048)
out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")
```

### Example 3

```python
from arcpy.ia import *
out_hillshade_raster = Hillshade("elevation.tif", 180, 75, 0.3048)
out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_dem = "elevation.tif"

# Execute the Hillshade function
out_hillshade_raster = Hillshade(in_dem, 180, 75, 0.3048)

# Save the output
out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")
```

### Example 5

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_dem = "elevation.tif"

# Execute the Hillshade function
out_hillshade_raster = Hillshade(in_dem, 180, 75, 0.3048)

# Save the output
out_hillshade_raster.save("C:/arcpyExamples/outputs/hillshade.tif")
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

IronOxide_raster = arcpy.ia.IronOxide("Sentinel2.tif", 4, 2)
```

### Example 5

```python
import arcpy

IronOxide_raster = arcpy.ia.IronOxide("Sentinel2.tif", 4, 2)
```

---

## LessThanFrequency

## Summary

Creates a raster object in which each pixel contains the number of times a set of rasters is less than another raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| value_raster | A value raster that will be referenced by the list of input rasters. | Raster |
| rasters | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
LessThanFrequency (value_raster, rasters, {extent_type}, {cellsize_type}, {process_as_multiband})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
LessThan_raster = LessThanFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
value_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
LessThan_raster = LessThanFrequency(value_raster, rasters, "UnionOf", "FirstOf", True)
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
from arcpy.ia import *
out_linearunmixing_raster = LinearUnmixing(
    "Landsat8.tif","C:/arcpyExamples/data/training_feature.ecd")
out_linearunmixing_raster.save(
    "C:/arcpyexamples/outputs/linearunmix_output.tif")
```

### Example 3

```python
from arcpy.ia import *
out_linearunmixing_raster = LinearUnmixing(
    "Landsat8.tif","C:/arcpyExamples/data/training_feature.ecd")
out_linearunmixing_raster.save(
    "C:/arcpyexamples/outputs/linearunmix_output.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_raster = "C:/data/Landsat_8.tif"
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
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_raster = "C:/data/Landsat_8.tif"
in_spectral_profile = "C:/data/training_features.ecd"
value_options = "SUM_TO_ONE;NON_NEGATIVE" 

# Apply LinearSpectralUnmixing function
unmixing_outputs = LinearUnmixing(in_raster, in_spectral_profile, value_options)

# Save the output
unmixing_outputs.save("C:/arcpyExamples/outputs/unmixing_results.tif")
```

---

## Lookup

## Summary

Creates a raster object by looking up values found in another field in the table of the input raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster that contains a field from which to create a raster. It can be either integer or floating-point type. | Raster |
| field | Field containing the desired values for the new raster. | String |

## Code Samples

### Example 1

```python
Lookup (raster, {field})
```

### Example 2

```python
from arcpy.ia import *
out_lookup_raster = Lookup("itemgrd", "bin")
out_lookup_raster.save("C:/arcpyExamples/outputs/output.tif")
```

### Example 3

```python
from arcpy.ia import *
out_lookup_raster = Lookup("itemgrd", "bin")
out_lookup_raster.save("C:/arcpyExamples/outputs/output.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "itemgrd"
in_field = "String"

# Execute Lookup function
out_lookup_raster = Lookup(in_raster, in_field)

# Save the output
out_lookup_raster.save("C:/arcpyExamples/outputs/output.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_raster = "itemgrd"
in_field = "String"

# Execute Lookup function
out_lookup_raster = Lookup(in_raster, in_field)

# Save the output
out_lookup_raster.save("C:/arcpyExamples/outputs/output.tif")
```

---

## LowestPosition

## Summary

Creates a raster object in which each pixel contains the position of the raster with the minimum value in a set of rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |

## Code Samples

### Example 1

```python
LowestPosition (rasters, {extent_type}, {cellsize_type})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
Lowest_raster = LowestPosition(rasters, "UnionOf", "FirstOf")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
Lowest_raster = LowestPosition(rasters, "UnionOf", "FirstOf")
```

---

## Majority

## Summary

Creates a raster object in which each pixel contains the value that occurs most often across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Majority (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

majority_raster = Majority(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

majority_raster = Majority(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
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

out_Mask_raster = arcpy.ia.Mask("Landsat8.tif", no_data_values = 6, included_ranges = [3,9])
```

### Example 3

```python
import arcpy

out_Mask_raster = arcpy.ia.Mask("Landsat8.tif", no_data_values = 6, included_ranges = [3,9])
```

---

## Max

## Summary

Creates a raster object in which each pixel contains the largest value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Max (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

max_raster = Max(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

max_raster = Max(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## Mean

## Summary

Creates a raster object in which each pixel contains the average value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Mean (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

mean_raster = Mean(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

mean_raster = Mean(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## Median

## Summary

Creates a raster object in which each pixel contains the median value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Median (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

mean_raster = Median(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

mean_raster = Median(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## Mensuration

## Summary

Performs measurements on an image with a sensor model, which includes the geometric sensor model and the appropriate metadata (Image Support Data) that is supplied with the image. The supported types of measurements include point, distance or length, area, and feature height.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | A raster object created with the Raster class, or the path to a raster dataset. | Raster |
| polygon | The input polygon. The polygon can be specified as a Polygon object, a list of Point objects, or a list of coordinate pairs in tuples.If specified as a list of tuples, the x- and y-coordinate values must be in the image coordinate system (column, row). If other spatial reference systems are preferred, use Polygon or Point objects with a spatial reference system defined. | Polygon |
| from_point | The input coordinates of the origin point. The point can be specified as a Point object, a PointGeometry object, or a coordinate pair in a tuple.If specified as a tuple, the x- and y-coordinate values must be in an image coordinate system (column, row). If other spatial reference systems are preferred, use the Point or PointGeometry objects with a spatial reference system defined. | Point |
| to_point | The input coordinates of the destination point. The point can be specified as a Point object, a PointGeometry object, or a coordinate pair in a tuple.If specified as a tuple, the x-and y-coordinate values must be in the image coordinate system (column, row). If other spatial reference systems are preferred, use Point or PointGeometry objects with a spatial reference system defined. | Point |
| base_point | The input coordinates of the base of the feature to measure. This can be specified as a Point object, a PointGeometry object, or a coordinate pair in a tuple.If specified as a tuple, the x- and y-coordinate values should be in the image coordinate system (column, row). If other spatial reference systems are preferred, use PointGeometry or Point objects with a spatial reference system defined. | Point |
| top_point | The input coordinates of the top of the feature to measure. The point can be specified as a Point object, a PointGeometry object, or a coordinate pair in a tuple.If specified as a tuple, the x- and y-coordinate values should be in the image coordinate system (column, row). If other spatial reference systems are preferred, use PointGeometry or Point objects with a spatial reference system defined. | Point |
| height_type | Height measurements of an object can be obtained when a sensor model exists for an image. Sun angle information is required to make measurements using shadows. The height of an object is calculated between two points, based on a sensor model. Three types of height measurements are supported:base_to_top—Calculates the height of a ground feature by measuring from the base of the object to the top of the object.base_to_shadow—Calculates the height of a feature by measuring from the base of the object to the top of the object's shadow on the ground.top_to_shadow—Calculates the height of a feature by measuring from the top of the object to the top of the object's shadow on the ground. | Integer |
| point | The input coordinates to measure. The point can be specified as a Point object, a PointGeometry object, or a coordinate pair in a tuple.If specified as a tuple, the x- and y-coordinate values must be in the image coordinate system (column, row). If other spatial reference systems are preferred, use Point or PointGeometry objects with a spatial reference system defined. | Point |

## Methods

### area (polygon)

Calculates the area of a polygon in an image, based on a sensor model.

### distance (from_point, to_point)

Calculates the geographic distance between two points in an image, based on a sensor model.

### height (base_point, top_point, height_type)

Calculate the vertical height of an object.

### point (point)

Calculates the geographic coordinate based on sensor model.

## Code Samples

### Example 1

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.point((raster.width/2, raster.height/2))
print(f"Center: ({result.lat}, {result.lon})")
```

### Example 2

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.point((raster.width/2, raster.height/2))
print(f"Center: ({result.lat}, {result.lon})")
```

### Example 3

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.distance((0, 0), (raster.width, 0))
print(f"Image Width: {result.distance} m")
```

### Example 4

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.distance((0, 0), (raster.width, 0))
print(f"Image Width: {result.distance} m")
```

### Example 5

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.area([(0, 0), (raster.width, 0),
                    (raster.width, raster.height), (0, raster.height)])
print(f"Image Size: {result.area} m^2")
```

### Example 6

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.area([(0, 0), (raster.width, 0),
                    (raster.width, raster.height), (0, raster.height)])
print(f"Image Size: {result.area} m^2")
```

### Example 7

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.height((base_x, base_y),
                     (top_x, top_y),
                      Mensuration.base_to_top)
print (f"Height: {result.height} m")
```

### Example 8

```python
import arcpy
raster = arcpy.sa.Raster(raster_path)
mens = arcpy.ia.Mensuration(raster)
result = mens.height((base_x, base_y),
                     (top_x, top_y),
                      Mensuration.base_to_top)
print (f"Height: {result.height} m")
```

### Example 9

```python
Mensuration
 (raster)
```

### Example 10

```python
area (polygon)
```

### Example 11

```python
import arcpy
in_raster = arcpy.sa.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.area([(0, 0), (in_raster.width, 0), (in_raster.width, in_raster.height), (0, in_raster.height)])
print(f"Image Size: {result.area} m^2")
```

### Example 12

```python
import arcpy
in_raster = arcpy.sa.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.area([(0, 0), (in_raster.width, 0), (in_raster.width, in_raster.height), (0, in_raster.height)])
print(f"Image Size: {result.area} m^2")
```

### Example 13

```python
distance (from_point, to_point)
```

### Example 14

```python
import arcpy
in_raster = arcpy.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.distance((0, 0),( raster.width, 0))
print(f"Image Width: {result.distance} m")
```

### Example 15

```python
import arcpy
in_raster = arcpy.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.distance((0, 0),( raster.width, 0))
print(f"Image Width: {result.distance} m")
```

### Example 16

```python
height (base_point, top_point, height_type)
```

### Example 17

```python
import arcpy
in_raster = arcpy.sa.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.height((base_x, base_y), (top_x, top_y), Mensuration.base_to_top)
print(f"Height: {result.height} m")
```

### Example 18

```python
import arcpy
in_raster = arcpy.sa.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.height((base_x, base_y), (top_x, top_y), Mensuration.base_to_top)
print(f"Height: {result.height} m")
```

### Example 19

```python
point (point)
```

### Example 20

```python
import arcpy
in_raster = arcpy.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.point((in_raster.width/2, in_raster.height/2))
print(f"Center: ({result.lat}, {result.lon})")
```

### Example 21

```python
import arcpy
in_raster = arcpy.Raster('Charlotte_multiband.tif')
mensuration = arcpy.ia.Mensuration(in_raster)
result = mensuration.point((in_raster.width/2, in_raster.height/2))
print(f"Center: ({result.lat}, {result.lon})")
```

---

## Merge

## Summary

Creates a raster object by merging a list of rasters spatially or across dimensions.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| resolve_overlap | The method used to handle overlapping pixels when merging rasters spatially or dimensionally.FIRST—The pixel value will be determined by the raster that appears first in the list of rasters. This is the default.LAST—The pixel value will be determined by the raster that appears last in the list of rasters.MIN—The pixel value will be determined by the lowest pixel value in the overlapping rasters.MAX—The pixel value will be determined by the highest pixel value in the overlapping rasters.MEAN—The pixel value will be determined by the average of the overlapping pixel values.SUM—The pixel value will be determined by the sum of the overlapping pixel values.(The default value is FIRST) | String |

## Code Samples

### Example 1

```python
Merge (rasters, {resolve_overlap})
```

### Example 2

```python
import arcpy
from arcpy.ia import *


# Set input rasters
in_raster1 = arcpy.Raster("Canada_landcover.tif")
in_raster2 = arcpy.Raster("USA_landcover.tif")
in_raster3 = arcpy.Raster("Mexico_landcover.tif")

# Merge the three rasters
NorthAmericaLC = arcpy.ia.Merge([in_raster1, in_raster2, in_raster3], "FIRST")
NorthAmericaLC.save("NorthAmerica_landcover.tif")
```

### Example 3

```python
import arcpy
from arcpy.ia import *


# Set input rasters
in_raster1 = arcpy.Raster("Canada_landcover.tif")
in_raster2 = arcpy.Raster("USA_landcover.tif")
in_raster3 = arcpy.Raster("Mexico_landcover.tif")

# Merge the three rasters
NorthAmericaLC = arcpy.ia.Merge([in_raster1, in_raster2, in_raster3], "FIRST")
NorthAmericaLC.save("NorthAmerica_landcover.tif")
```

### Example 4

```python
import arcpy
from arcpy.ia import *


# Set input multidimensional rasters
# multidim_1 contains a precipitation variable, measured daily in 2018
# multidim_2 contains a temperature variable, measured daily in 2018
multidim_1 = arcpy.Raster("prcp_daily_2018.nc", True)
multidim_2 = arcpy.Raster("temp_daily_2018.nc", True)

# Merge the two multidimensional rasters
multidim_precip_temp = arcpy.ia.Merge([multidim_1, multidim_2])

# The result contains both daily variables for the year 2018
multidim_precip_temp.save("prcp_and_temp_2018.crf")
```

### Example 5

```python
import arcpy
from arcpy.ia import *


# Set input multidimensional rasters
# multidim_1 contains a precipitation variable, measured daily in 2018
# multidim_2 contains a temperature variable, measured daily in 2018
multidim_1 = arcpy.Raster("prcp_daily_2018.nc", True)
multidim_2 = arcpy.Raster("temp_daily_2018.nc", True)

# Merge the two multidimensional rasters
multidim_precip_temp = arcpy.ia.Merge([multidim_1, multidim_2])

# The result contains both daily variables for the year 2018
multidim_precip_temp.save("prcp_and_temp_2018.crf")
```

### Example 6

```python
import arcpy
from arcpy.ia import *


# Set input multidimensional rasters
# multidim_1 contains a precipitation variable, measured daily in 2017
# multidim_2 contains a temperature variable, measured daily in 2018
multidim_1 = arcpy.Raster("precip_daily_2017.nc", True)
multidim_2 = arcpy.Raster("precip_daily_2018.nc", True)

# Merge the two multidimensional rasters
multidim_precip_17_18 = arcpy.ia.Merge([multidim_1, multidim_2])

# The result contains precipitation variables for the years 2017 and 2018
multidim_precip_17_18.save("prcp_2017_and_2018.crf")
```

### Example 7

```python
import arcpy
from arcpy.ia import *


# Set input multidimensional rasters
# multidim_1 contains a precipitation variable, measured daily in 2017
# multidim_2 contains a temperature variable, measured daily in 2018
multidim_1 = arcpy.Raster("precip_daily_2017.nc", True)
multidim_2 = arcpy.Raster("precip_daily_2018.nc", True)

# Merge the two multidimensional rasters
multidim_precip_17_18 = arcpy.ia.Merge([multidim_1, multidim_2])

# The result contains precipitation variables for the years 2017 and 2018
multidim_precip_17_18.save("prcp_2017_and_2018.crf")
```

---

## Min

## Summary

Creates a raster object in which each pixel contains the minimum value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Min (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

min_raster = Min(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

min_raster = Min(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## Minority

## Summary

Creates a raster object in which each pixel contains the value that occurs least often across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Minority (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

minority_raster = Minority(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

minority_raster = Minority(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## MLClassify

## Summary

Performs a supervised classification using the maximum likelihood classification algorithm.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster[raster,...] | The input raster to classify using the maximum likelihood classification algorithm. | Raster |
| signature[signature,...] | The .gsg signature file. | String |

## Code Samples

### Example 1

```python
MLClassify (raster, signature)
```

### Example 2

```python
from arcpy.ia import *
out_mlclassify_raster = MLClassify("northerncincy.tif", "C:/arcpyExamples/data/cincinnati1234.gsg")
out_mlclassify_raster.save("C:/arcpyExamples/outputs/outputs_mlclassify.tif")
```

### Example 3

```python
from arcpy.ia import *
out_mlclassify_raster = MLClassify("northerncincy.tif", "C:/arcpyExamples/data/cincinnati1234.gsg")
out_mlclassify_raster.save("C:/arcpyExamples/outputs/outputs_mlclassify.tif")
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

MSAVI_raster = arcpy.ia.MSAVI("Landsat8.tif", 5, 4)
```

### Example 5

```python
import arcpy

MSAVI_raster = arcpy.ia.MSAVI("Landsat8.tif", 5, 4)
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

MTVI2_raster = arcpy.ia.MTVI2("Landsat8.tif", 5, 4, 3)
```

### Example 5

```python
import arcpy

MTVI2_raster = arcpy.ia.MTVI2("Landsat8.tif", 5, 4, 3)
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
import arcpy

NBR_raster = arcpy.ia.NBR("Landsat8.tif", swir_band_id = 7, nir_band_id = 5)
```

### Example 5

```python
import arcpy

NBR_raster = arcpy.ia.NBR("Landsat8.tif", swir_band_id = 7, nir_band_id = 5)
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
import arcpy

NDBI_raster = arcpy.ia.NDBI("Landsat8.tif", swir_band_id = 6, nir_band_id = 5)
```

### Example 5

```python
import arcpy

NDBI_raster = arcpy.ia.NDBI("Landsat8.tif", swir_band_id = 6, nir_band_id = 5)
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
import arcpy

NDMI_raster = arcpy.ia.NDMI("Landsat8.tif", nir_band_id = 5, swir1_band_id = 6)
```

### Example 5

```python
import arcpy

NDMI_raster = arcpy.ia.NDMI("Landsat8.tif", nir_band_id = 5, swir1_band_id = 6)
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
import arcpy

NDSI_raster = arcpy.ia.NDSI("Landsat8.tif", green_band_id = 4, swir_band_id = 6)
```

### Example 5

```python
import arcpy

NDSI_raster = arcpy.ia.NDSI("Landsat8.tif", green_band_id = 4, swir_band_id = 6)
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

NDVI_raster = arcpy.ia.NDVI("Landsat8.tif", 5, 4)
```

### Example 5

```python
import arcpy

NDVI_raster = arcpy.ia.NDVI("Landsat8.tif", 5, 4)
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

NDVIre_raster = arcpy.ia.NDVIre("Sentinel2.tif", 8, 5)
```

### Example 5

```python
import arcpy

NDVIre_raster = arcpy.ia.NDVIre("Sentinel2.tif", 8, 5)
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

NDWI_raster = arcpy.ia.NDWI("Sentinel2.tif", 8, 3)
```

### Example 5

```python
import arcpy

NDWI_raster = arcpy.ia.NDWI("Sentinel2.tif", 8, 3)
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

Pansharpen_raster = arcpy.ia.Pansharpen(imagePath1, imagePath2, None, True, [0.166, 0.167, 0.167, 0.5], "Gram-Schmidt", None
```

### Example 3

```python
import arcpy

Pansharpen_raster = arcpy.ia.Pansharpen(imagePath1, imagePath2, None, True, [0.166, 0.167, 0.167, 0.5], "Gram-Schmidt", None
```

---

## Percentile

## Summary

Creates a raster object in which each pixel contains the specified percentile value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| percentile_value | The percentile value to calculate.(The default value is 90) | Double |
| percentile_interpolation_type | The interpolation method used when the specified percentile value lies between two input cell values.AUTO_DETECT—If the input raster collection is integer type, the NEAREST method is used. If the input raster collection is floating point type, the LINEAR method is used.NEAREST—The nearest available value to the specified percentile is used. The output pixel type will match the input.LINEAR—The weighted average of the two surrounding percentile values is used. The output pixel type is floating point.(The default value is AUTO_DETECT) | String |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Percentile (rasters, {percentile_value}, {percentile_interpolation_type}, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

percentile_raster = Percentile(rc, percentile_value = 90, percentile_interpolation_type = "AUTO_DETECT", extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

percentile_raster = Percentile(rc, percentile_value = 90, percentile_interpolation_type = "AUTO_DETECT", extent_type = "UnionOf", cellsize_type = "MinOf", 
		ignore_nodata = True, process_as_multiband = True)
```

---

## PixelBlock

## Summary

Defines a group or block of pixels to include for raster processing. The PixelBlockCollection object is made up of one or more PixelBlock objects.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| data | A NumPy array containing the pixel values for the pixel block. If the raster is not multidimensional, the shape of the array should be (rows, columns, bands). If the raster is multidimensional, the shape of the array should be (slices, rows, columns, bands). | NumPyArray |
| extent | The spatial extent of the pixel block. | Extent |

## Methods

### getData ()

Returns the NumPy array within the pixel block.

## Code Samples

### Example 1

```python
PixelBlock
 (data, extent)
```

### Example 2

```python
import arcpy 

# Specify the input raster
in_raster = arcpy.Raster("landcover.tif")  

# Create a PixelBlockCollection

blockCollection = arcpy.ia.PixelBlockCollection(
	in_raster, pixel_block_size = (512, 512), nodata_to_values = -1) 
forest_cell_count = 0 

# Iterate through each PixelBlock 

try: 
    while True: 
        pixelblock = next(blockCollection) 
        np_array = pixelblock.getData() 
        forest_cell_count+= np.count_nonzero(np_array == 1) # value = 1 is forest class 
except StopIteration: 
    pass 
print ("total forest pixels : " + str(forest_cell_count))
```

### Example 3

```python
import arcpy 

# Specify the input raster
in_raster = arcpy.Raster("landcover.tif")  

# Create a PixelBlockCollection

blockCollection = arcpy.ia.PixelBlockCollection(
	in_raster, pixel_block_size = (512, 512), nodata_to_values = -1) 
forest_cell_count = 0 

# Iterate through each PixelBlock 

try: 
    while True: 
        pixelblock = next(blockCollection) 
        np_array = pixelblock.getData() 
        forest_cell_count+= np.count_nonzero(np_array == 1) # value = 1 is forest class 
except StopIteration: 
    pass 
print ("total forest pixels : " + str(forest_cell_count))
```

---

## PixelBlockCollection

## Summary

Establishes read-only access to all pixel blocks from a raster or list of rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_rasters[in_rasters,...] | The input raster object or a list of raster objects. If you're using a list of raster objects, the rasters must all have the same cell size and spatial reference. | Raster |
| pixel_block_size | A tuple with two values describing the block size (number of rows, number of columns).(The default value is (512, 512)) | tuple |
| stride | A tuple with two integers specifying the stride or increment along the rows and columns for processing.If no value is specified, the pixel block size will be used, and adjacent pixel blocks will have no overlap.(The default value is None) | tuple |
| overlay_type | Specifies the overlay type when input rasters have different extents. INTERSECTION—Pixel blocks will only cover the area of intersection between rasters.UNION—Pixel blocks will cover the extent of all rasters.(The default value is INTERSECTION) | String |
| nodata_to_values[nodata_to_values,...] | The value to assign to NoData values from the input rasters in the resulting NumPy array. This can be a single value or a list of values, one for each raster. | Integer |

## Methods

### reset ()

Resets the pixel block collection iterator to the beginning of the collection.

### shuffle ()

Shuffles the pixel blocks in the pixel block collection. This is useful when feeding image samples into a deep learning model.

## Code Samples

### Example 1

```python
pixelblockcoll = PixelBlockCollection(in_raster)
numpy_array = pixelblockcoll[0][0].getData()
```

### Example 2

```python
pixelblockcoll = PixelBlockCollection(in_raster)
numpy_array = pixelblockcoll[0][0].getData()
```

### Example 3

```python
pixelblockcoll = PixelBlockCollection(in_raster1, in_raster2)
numpy_array = pixelblockcoll[0][0][1].getData()
```

### Example 4

```python
pixelblockcoll = PixelBlockCollection(in_raster1, in_raster2)
numpy_array = pixelblockcoll[0][0][1].getData()
```

### Example 5

```python
PixelBlockCollection
 (in_rasters, pixel_block_size, stride, overlay_type, nodata_to_values)
```

### Example 6

```python
import arcpy 

# Specify the input raster
in_raster1 = arcpy.Raster("landcover.tif")  
 
# Create a PixelBlockCollection 
blockCollection = arcpy.ia.PixelBlockCollection(
	in_raster1, pixel_block_size = (512, 512), nodata_to_values = -1) 

# Check the number of pixelblocks along x and y direction 
number_blocks_y, number_blocks_x= blockCollection.size 

urban_cell_count=0 

# Iterate through each PixelBlock 
for i in range(number_blocks_y):
    for j in range(number_blocks_x):
        pixelblock = blockCollection[i,j] 
	np_array = pixelblock.getData()
	urban_cell_count+= np.count_nonzero(np_array == 3) 
	# value = 3 is urban class 

urban_area = urban_cell_count * in_raster1.meanCellWidth*in_raster1.meanCellHeight 
print("Total urban area : " + str(urban_area))
```

### Example 7

```python
import arcpy 

# Specify the input raster
in_raster1 = arcpy.Raster("landcover.tif")  
 
# Create a PixelBlockCollection 
blockCollection = arcpy.ia.PixelBlockCollection(
	in_raster1, pixel_block_size = (512, 512), nodata_to_values = -1) 

# Check the number of pixelblocks along x and y direction 
number_blocks_y, number_blocks_x= blockCollection.size 

urban_cell_count=0 

# Iterate through each PixelBlock 
for i in range(number_blocks_y):
    for j in range(number_blocks_x):
        pixelblock = blockCollection[i,j] 
	np_array = pixelblock.getData()
	urban_cell_count+= np.count_nonzero(np_array == 3) 
	# value = 3 is urban class 

urban_area = urban_cell_count * in_raster1.meanCellWidth*in_raster1.meanCellHeight 
print("Total urban area : " + str(urban_area))
```

### Example 8

```python
import arcpy 
from arcpy.ia import *

# Specify the input rasters
in_raster1 = arcpy.Raster("C:/iapyexamples/data/landcover_2006.tif")  
in_raster2 = arcpy.Raster("C:/iapyexamples/data/landcover_2016.tif")  
 
# Create a PixelBlockCollection 
blockCollection = arcpy.ia.PixelBlockCollection(
	[in_raster1, in_raster2], pixel_block_size = (256, 256), nodata_to_values = -1) 

# Check the number of pixelblocks along x and y direction 
number_blocks_y, number_blocks_x= pixelblocks.size 

forest_to_urban_cell_count = 0 

# Iterate through each PixelBlock

for i in range(number_blocks_y): 
    for j in range(number_blocks_x): 
        pixelblocklist = blockCollection[i][j]
        # get the array from pixelblock in the 1st raster
        array_in_raster1 = pixelblocklist[0].getData()  
        # get the array from pixelblock in the 2nd raster
        array_ in_raster2 = pixelblocklist[1].getData()  

        forest_in_raster1= array_in_raster1[array_in_raster1==1] # value = 1 is forest class 
        urban_in_raster2= array_in_raster2[array_in_raster2==3] # value = 3 is urban class 
        res= forest_in_raster1+ urban_in_raster2  
        forest_to_urban_cell_count+= np.count_nonzero(res == 4) # value = 4 is forest in in_raster1 and urban in in_raster2 

forest_to_urban_area= forest_to_urban_cell_count * in_raster1.meanCellWidth*in_raster1.meanCellHeight 
print("total area from forest in 2006 to urban in 2016 : " + str(forest_to_urban_area))
```

### Example 9

```python
import arcpy 
from arcpy.ia import *

# Specify the input rasters
in_raster1 = arcpy.Raster("C:/iapyexamples/data/landcover_2006.tif")  
in_raster2 = arcpy.Raster("C:/iapyexamples/data/landcover_2016.tif")  
 
# Create a PixelBlockCollection 
blockCollection = arcpy.ia.PixelBlockCollection(
	[in_raster1, in_raster2], pixel_block_size = (256, 256), nodata_to_values = -1) 

# Check the number of pixelblocks along x and y direction 
number_blocks_y, number_blocks_x= pixelblocks.size 

forest_to_urban_cell_count = 0 

# Iterate through each PixelBlock

for i in range(number_blocks_y): 
    for j in range(number_blocks_x): 
        pixelblocklist = blockCollection[i][j]
        # get the array from pixelblock in the 1st raster
        array_in_raster1 = pixelblocklist[0].getData()  
        # get the array from pixelblock in the 2nd raster
        array_ in_raster2 = pixelblocklist[1].getData()  

        forest_in_raster1= array_in_raster1[array_in_raster1==1] # value = 1 is forest class 
        urban_in_raster2= array_in_raster2[array_in_raster2==3] # value = 3 is urban class 
        res= forest_in_raster1+ urban_in_raster2  
        forest_to_urban_cell_count+= np.count_nonzero(res == 4) # value = 4 is forest in in_raster1 and urban in in_raster2 

forest_to_urban_area= forest_to_urban_cell_count * in_raster1.meanCellWidth*in_raster1.meanCellHeight 
print("total area from forest in 2006 to urban in 2016 : " + str(forest_to_urban_area))
```

---

## Popularity

## Summary

Creates a raster object in which each pixel contains the value in an argument list that is at a certain level of popularity.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| popularity_raster | The input raster that defines the popularity position to be returned. | Raster |
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Popularity (popularity_raster, rasters, {extent_type}, {cellsize_type}, {process_as_multiband})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
popularity_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
output_raster = Popularity(popularity_raster, rasters, "UnionOf", "FirstOf", True)
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
popularity_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
output_raster = Popularity(popularity_raster, rasters, "UnionOf", "FirstOf", True)
```

---

## PredictUsingTrend

## Summary

Computes a forecasted multidimensional raster object using the output trend raster from the GenerateTrend function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input trend raster from the GenerateTrend function. | Raster |
| dimension_definition_type | Specifies the method to be used to provide prediction dimension values.BY_VALUE—The prediction will be calculated for a single dimension value or a list of dimension values defined by the dimension_values argument. This is the default.BY_INTERVAL—The prediction will be calculated for an interval of the dimension defined by the start and end arguments.(The default value is BY_VALUE) | String |
| dimension_values[dimension_values,...] | The dimension value or list of values to be used in the prediction. The format of the value must match the format of the dimension in the input multidimensional raster. If the trend raster was generated for the StdTime dimension, the format will be YYYY-MM-DDTHH:MM:SS, for example, 2050-01-01T12:00:00.This argument is required when the dimension_def parameter is set to BY_VALUE.(The default value is None) | String |
| start | The start date, height, or depth of the dimension interval to be used in the prediction. The format of the value must match the format of the dimension in the input multidimensional raster.(The default value is None) | String |
| end | The end date, height, or depth of the dimension interval to be used in the prediction. The format of the value must match the format of the dimension in the input multidimensional raster.(The default value is None) | String |
| interval_value | The number of steps between two dimension values to be included in the prediction. The default value is 1.(The default value is 1) | Double |
| interval_unit | Specifies the unit that will be used for the interval_value argument. This only applies when the dimension of analysis is a time dimension.HOURS—The prediction will be calculated for each hour in the range of time described by the start, end, and interval_value arguments.DAYS—The prediction will be calculated for each day in the range of time described by the start, end, and interval_value arguments.WEEKS—The prediction will be calculated for each week in the range of time described by the start, end, and interval_value arguments.MONTHS—The prediction will be calculated for each month in the range of time described by the start, end, and interval_value arguments.YEARS—The prediction will be calculated for each year in the range of time described by the start, end, and interval_value arguments.(The default value is HOURS) | String |

## Code Samples

### Example 1

```python
PredictUsingTrend (raster, {dimension_definition_type}, {dimension_values}, {start}, {end}, {interval_value}, {interval_unit})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_raster = "C:/Data/NDVI_Trend.crf"
dimension_def = "BY_INTERVAL"
dimension_values = "None"
start = "2025-01-01T00:00:00"
end = "2025-12-31T00:00:00"
interval_value = 1
interval_unit = "MONTHS"

# Apply PredictUsingTrendRaster function
predicted_raster = arcpy.ia.PredictusingTrend(in_raster, dimension_def, 
                        dimension_values , start, end, interval_value, interval_unit)
	
# Save the output
predicted_raster.save("C:/arcpyExamples/outputs/predicted_NDVI.crf")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
in_raster = "C:/Data/NDVI_Trend.crf"
dimension_def = "BY_INTERVAL"
dimension_values = "None"
start = "2025-01-01T00:00:00"
end = "2025-12-31T00:00:00"
interval_value = 1
interval_unit = "MONTHS"

# Apply PredictUsingTrendRaster function
predicted_raster = arcpy.ia.PredictusingTrend(in_raster, dimension_def, 
                        dimension_values , start, end, interval_value, interval_unit)
	
# Save the output
predicted_raster.save("C:/arcpyExamples/outputs/predicted_NDVI.crf")
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

PVI_raster = arcpy.ia.PVI("Landsat8.tif", 5, 4, 0.3, 0.5)
```

### Example 5

```python
import arcpy

PVI_raster = arcpy.ia.PVI("Landsat8.tif", 5, 4, 0.3, 0.5)
```

---

## Range

## Summary

Creates a raster object in which each pixel contains the difference between the largest and smallest values across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Range (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Range(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Range(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
```

---

## Rank

## Summary

Creates a raster object in which each pixel contains values from a set of input rasters based on the value of the rank input raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rank_raster | The input raster that defines the rank position to be returned. | Raster |
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Rank (rank_raster, rasters, {extent_type}, {cellsize_type}, {process_as_multiband})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rank_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
output_raster = Rank(rank_raster, rasters, "UnionOf", "FirstOf", True)
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

#Set the local variables
rank_raster = r"c:\temp\value_raster.tif"

rasters = [r"c:\temp\raster1.tif", r"c:\temp\raster2.tif", r"c:\temp\raster3.tif"] 

#Execute
output_raster = Rank(rank_raster, rasters, "UnionOf", "FirstOf", True)
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
from arcpy.ia import *
out_rc_multi_raster = RasterCalculator(["raster1.tif", "raster2.tif"],
                                       ["x", "y"], "x*y")
out_rc_multi_raster.save("C:/arcpyExamples/raster_rc_multi.tif")
```

### Example 3

```python
from arcpy.ia import *
out_rc_multi_raster = RasterCalculator(["raster1.tif", "raster2.tif"],
                                       ["x", "y"], "x*y")
out_rc_multi_raster.save("C:/arcpyExamples/raster_rc_multi.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

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
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

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

## RasterCollection

## Summary

Defines the group of input rasters and attributes to include in a collection that will be used for processing.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The input raster datasets. Supported inputs include a list of rasters, a mosaic dataset, a multidimensional raster in Cloud Raster Format, a NetCDF file, or an image service. If you're using a list of raster datasets, all rasters must have the same cell size and spatial reference. | List |
| attribute_dict | A Python dictionary that contains attribute information to be added to each raster, when the input is a list of rasters. For each key-value pair, the key is the attribute name and the value is a list of values that represent the attribute value for each raster. For example, to add a name field to a list of three rasters, use {"name": ["Landsat8_Jan", "Landsat8_Feb", "Landsat8_Mar"]}.(The default value is None) | Dictionary |
| field_name | The name of the field to be added. | String |
| field_values[field_values,...] | The list of values associated with the field name. The length of the list should match the number of items in the raster collection. | List |
| where_clause | An expression that limits the records returned. For more information on WHERE clauses and SQL statements, see SQL reference for query expressions used in ArcGIS. (The default value is None) | String |
| query_geometry_or_extent | An object that filters the items such that only those that intersect with the object will be returned. This can be specified with a Geometry object, Extent object, Raster object, or a path to a feature class.(The default value is None) | Geometry |
| field_name | The field name to use in the filter. | String |
| operator | The keyword to filter the attributes. Keywords include the following:CONTAINS—The attribute in the field contains the specified string, list, or number.ENDS_WITH—The attribute ends with the specified string or number.EQUALS—The attribute equals the specified string, list, or number.GREATER_THAN—The attribute is greater than the specified number. IN—The attribute is one of the items in the specified list.LESS_THAN—The attribute is less than the specified number.NOT_CONTAINS—The attribute does not contain the specified string, list, or number.NOT_ENDS_WITH—The attribute does not end with the specified string or number.NOT_EQUALS—The attribute does not equal the specified string, list, or number.NOT_GREATER_THAN—The attribute is not greater than the specified number. NOT_IN—The attribute is not one of the items in the specified list.NOT_LESS_THAN—The attribute is not less than the specified number.NOT_STARTS_WITH—The attribute does not start with the specified string or number.STARTS_WITH—The attribute starts with the specified string or number. | String |
| field_values[field_values,...] | The attribute value or values against which to compare. This can be specified as a string, a list, or a number. | String |
| calendar_field | The name of the calendar field. Specify one of the following: HOUR, DAY_OF_WEEK, DAY_OF_MONTH, DAY_OF_YEAR, WEEK_OF_YEAR, MONTH, YEAR, or QUARTER. | String |
| start | The start value of the calendar_field. For example, to filter all items that were collected in January, filtered_rc = rc.filterByCalendarRange(calendar_field="MONTH", start=1). | Integer |
| end | The end value of the calendar_field. For example, to filter all items that were collected in the first five days of each year, filtered_rc = rc.filterByCalendarRange(calendar_field="DAY_OF_YEAR", start=1, end=5). | Integer |
| time_field_name | The name of the field that contains the time attribute for each item in the collection. The default is StdTime. | String |
| date_time_format | The time format of the values in the time field. For example, if the input date and time value is "1990-01-31T00:00:00", the date_time_format is "%Y-%m-%dT%H:%M:%S". If only the date value is required, date_time_format can be specified as "%Y-%m-%d". | String |
| query_geometry_or_extent | An object that filters the items such that only those that intersect with the object will be returned. This can be specified with a Geometry object, Extent object, Raster object, or a path to a feature class. | Geometry |
| property_name | The name of the property to use in the filter. | String |
| operator | The operator to filter the property.CONTAINS—The property contains the specified string, list, or number.ENDS_WITH—The property ends with the specified string or number.EQUALS—The property equals the specified string, list, or number.GREATER_THAN—The property is greater than the specified number. IN—The property is one of the items in the specified list.LESS_THAN—The property is less than the specified number.NOT_CONTAINS—The property does not contain the specified string, list, or number.NOT_ENDS_WITH—The property does not end with the specified string or number.NOT_EQUALS—The property does not equal the specified string, list, or number.NOT_GREATER_THAN—The property is not greater than the specified number. NOT_IN—The property is not one of the items in the specified list.NOT_LESS_THAN—The property is not less than the specified number.NOT_STARTS_WITH—The property does not start with the specified string or number.STARTS_WITH—The property starts with the specified string or number. | String |
| property_values[property_values,...] | The property value or values against which to compare. This can be specified as a string, a list, or a number. | String |
| start_time | A string that specifies the start time. The string should be formatted to match the date format of the input raster collections, for example, "1990-01-01T13:30:00". If not specified, the end time must be specified, and only the items that have a time value that is earlier than or equal to the end time will be returned.(The default value is None) | String |
| end_time | A string that specifies the end time. The string should be formatted to match the date format of the input raster collections, for example, "1991-01-01T13:30:00". If not specified, the start time must be specified, and only the items that have a time value that is later than or equal to the start time will be returned. (The default value is None) | String |
| time_field_name | The name of the field that contains the time attribute for each item in the collection.(The default value is StdTime) | String |
| date_time_format | The format of the start_time and end_time values. For example, if the provided start_time value is "1990-01-31", the date_time_format is "%Y-%m-%d." For dates that include a time component, such as "1990-01-31T00:00:00", the default format is "%Y-%m-%dT%H:%M:%S". | String |
| stac_api | The URL of the STAC API root endpoint. This is the STAC API where the search will be performed, for example, "https://planetarycomputer.microsoft.com/api/stac/v1". The following STAC APIs are supported: https://planetarycomputer.microsoft.com/api/stac/v1—The following collections are supported: daymet-annual-pr, daymet-daily-hi, 3dep-seamless, 3dep-lidar-dsm, sentinel-1-rtc, gridmet, daymet-annual-na, daymet-monthly-na, daymet-annual-hi, daymet-monthly-hi, daymet-monthly-pr, hgb, cop-dem-glo-30, cop-dem-glo-90, terraclimate, gnatsgo-rasters, 3dep-lidar-hag, 3dep-lidar-intensity, 3dep-lidar-pointsourceid, mtbs, noaa-c-cap, alos-fnf-mosaic, 3dep-lidar-returns, mobi, landsat-c2-l2, chloris-biomass, daymet-daily-pr, 3dep-lidar-dtm-native, 3dep-lidar-classification, 3dep-lidar-dtm, gap, alos-dem, jrc-gsw, hrea, sentinel-2-l2a, daymet-daily-na, nrcan-landcover, ecmwf-forecast, noaa-mrms-qpe-24h-pass2, sentinel-1-grd, nasadem, io-lulc, landsat-c2-l1, drcog-lulc, chesapeake-lc-7, chesapeake-lc-13, chesapeake-lu, noaa-mrms-qpe-1h-pass1, noaa-mrms-qpe-1h-pass2, noaa-nclimgrid-monthly, usda-cdl, esa-cci-lc, esa-cci-lc-netcdf, noaa-climate-normals-netcdf, noaa-climate-normals-gridded, io-lulc-9-class, io-biodiversity, naip, noaa-cdr-sea-surface-temperature-whoi, noaa-cdr-ocean-heat-content, noaa-cdr-sea-surface-temperature-whoi-netcdf, sentinel-3-olci-wfr-l2-netcdf, noaa-cdr-ocean-heat-content-netcdf, sentinel-3-synergy-v10-l2-netcdf, sentinel-3-olci-lfr-l2-netcdf, sentinel-3-slstr-lst-l2-netcdf, sentinel-3-slstr-wst-l2-netcdf, sentinel-3-synergy-syn-l2-netcdf, sentinel-3-synergy-vgp-l2-netcdf, sentinel-3-synergy-vg1-l2-netcdf, esa-worldcover, modis-64A1-061, modis-17A2H-061, modis-11A2-061, modis-17A2HGF-061, modis-17A3HGF-061, modis-09A1-061, modis-16A3GF-061, modis-21A2-061, modis-43A4-061, modis-09Q1-061, modis-14A1-061, modis-13Q1-061, modis-14A2-061, modis-15A2H-061, modis-11A1-061, modis-15A3H-061, modis-13A1-061, modis-10A2-061, modis-10A1-061, and aster-l1t. https://earth-search.aws.element84.com/v0—All collections are supported. https://earth-search.aws.element84.com/v1—All collections are supported. https://services.sentinel-hub.com/api/v1/catalog—All collections are supported.https://landsatlook.usgs.gov/stac-server—All collections are supported.https://geoportalstac.azurewebsites.net/stac—All collections are supported.https://gpt.geocloud.com/sentinel/stac—All collections are supported. | String |
| query | The GET or POST request query dictionary that will be used to query a STAC API search endpoint. The key-value pairs depend on the specification of the stac_api value and the request_method value.{ "collections": ["sentinel-2-l2a"], "bbox": [-110, 39.5, -105, 40.5], "query": {"eo:cloud_cover": {"lt": 0.5}}, "datetime": "2020-10-05T00:00:00Z/2020-10-10T12:31:12Z", "limit": 100 } For the bbox key, Extent and Polygon objects are also accepted (in any spatial reference). | Dictionary |
| attribute_dict | The attribute information that will be added to each STAC item raster returned from the query. For each key-value pair, the key is the attribute name, and the value is a list of values that represent the attribute value for each raster. Attribute values can also be collected from the STAC items automatically using the STAC item metadata information. To do this, specify the STAC item property name for the attribute of interest as key-value pairs (attribute display name: STAC item property name).{ "Name": "id", "Sensor": "platform", "StdTime": "datetime", "Cloud Cover": "eo:cloud_cover", "Spatial Reference": "proj:epsg", "Extent": "bbox" }Note:If no Geometry key is specified, it will be automatically added for each raster in the RasterCollection object based on its STAC item's geometry property and will be in "Spatial Reference": {"wkid": 4326}. | Dictionary |
| request_method | Specifies the HTTP request method that will be used with the STAC API for the search.GET—A GET request will be sent to the STAC API.POST—A POST request will be sent to the STAC API.Example: "POST"(The default value is POST) | String |
| request_params | The parameters of the STAC API search request. Specify the requests.post() or requests.get() method parameters and values in dictionary format.{ "verify": False, "headers": {"Authorization": "Bearer access_token_string"} } | Dictionary |
| context | Additional properties that will be used to control the creation of the object. The dictionary supports the assetManagement and processingTemplate keys.The assetManagement key specifies how to manage and select assets for the RasterCollection object. If multiple assets are selected, the collection will be composed of multiband rasters from those selected asset types. The value can be a list, string, or dictionary.When working with individual assets, the asset key can be specified directly, for example, "B02" or {"key": "B02"}, or as a list. Each item in the list represents an asset key or identifier. Items in the list can be strings representing the asset key directly, or dictionaries providing additional details for locating the asset. If the value of the assetManagement key is a dictionary, the following keys are supported:key—A string representing the unique identifier for an asset, for example, "red".path—A list representing the hierarchy of keys to navigate to the asset, for example, ["alternate", "s3"].hrefKey—A string representing the key to access the asset URL, for example, "msft:https-url". If this value is different from the default href key, specify it here.Examples:{ "assetManagement": [ "red", "blue" ] }{ "assetManagement": { "key": "tasmin", "hrefKey": "msft:https-url" } }{ "assetManagement": [ {"key": "TRAD", "path": ["alternate", "s3"]}, {"key": "DRAD", "path": ["alternate", "s3"]} ] }The processingTemplate key specifies the processing template that will be applied to the individual rasters in the collection. This is supported for selected collections and raster types. For more information about collections and raster types, see Satellite sensor raster types. The default for supported raster types is "Multiband"; otherwise, it's None.Example:{ "processingTemplate": "Surface Reflectance" } | Dictionary |
| stac_catalog | The URL of the STAC item, a pystac.Catalog object, or a pystac.Collection object. If a URL is provided, the value must be a static STAC item URL or a STAC API item URL, for example, "https://maxar-opendata.s3.amazonaws.com/events/India-Floods-Oct-2023/collection.json". The following static catalogs (and their underlying child catalogs) are supported:https://capella-open-data.s3.us-west-2.amazonaws.com/stac/catalog.json—The GEO, GEC, and SICD product types are supported.https://maxar-opendata.s3.amazonaws.com/events/catalog.jsonhttps://storage.googleapis.com/cfo-public/catalog.jsonhttps://nz-imagery.s3-ap-southeast-2.amazonaws.com/catalog.jsonhttps://raw.githubusercontent.com/m-mohr/oam-example/main/catalog.jsonhttps://dop-stac.opengeodata.lgln.niedersachsen.de/catalog.json https://pta.data.lit.fmi.fi/stac/root.jsonhttps://datacloud.icgc.cat/stac-catalog/catalog.jsonhttps://bdc-sentinel-2.s3.us-west-2.amazonaws.com/catalog.json | String |
| attribute_dict | The attribute information that will be added to each STAC item raster returned from the query. For each key-value pair, the key is the attribute name, and the value is a list of values that represent the attribute value for each raster. Attribute values can also be collected from the STAC items automatically using the STAC item metadata information. To do this, specify the STAC item property name for the attribute of interest as key-value pairs (attribute display name: STAC item property name).{ "Name": "id", "Sensor": "platform", "StdTime": "datetime", "Cloud Cover": "eo:cloud_cover", "Spatial Reference": "proj:epsg", "Extent": "bbox" }Note:If no Geometry key is specified, it will be automatically added for each raster in the RasterCollection object based on its STAC item's geometry property and will use a spatial reference as follows: "Spatial Reference": {"wkid": 4326}. | Dictionary |
| request_params | The parameters of the STAC catalog or item request. Specify the requests.post() or requests.get() method parameters and values in dictionary format.{ "verify": False, "headers": {"Authorization": "Bearer access_token_string"} } | Dictionary |
| context | Additional properties that will be used to control the creation of the object.The dictionary supports the assetManagement and processingTemplate keys.The assetManagement key specifies how to manage and select assets for the RasterCollection object. If multiple assets are selected, the collection will be composed of multiband rasters from those selected asset types. The value can be a list, string, or dictionary.When working with individual assets, the asset key can be specified directly, for example, "B02" or {"key": "B02"}, or as a list. Each item in the list represents an asset key or identifier. Items in the list can be strings representing the asset key directly, or dictionaries providing additional details for locating the asset. If the value of the assetManagement key is a dictionary, the following keys are supported:key—A string representing the unique identifier for an asset, for example, "red".path—A list representing the hierarchy of keys to navigate to the asset, for example, ["alternate", "s3"].hrefKey—A string representing the key to access the asset URL, for example, "msft:https-url". If this value is different from the default href key, specify it here.Examples:{ "assetManagement": [ "red", "blue" ] }{ "assetManagement": { "key": "tasmin", "hrefKey": "msft:https-url" } }{ "assetManagement": [ {"key": "TRAD", "path": ["alternate", "s3"]}, {"key": "DRAD", "path": ["alternate", "s3"]} ] }The processingTemplate key specifies the processing template that will be applied to the individual rasters in the collection. This is supported for selected collections and raster types. For more information about collections and raster types, see Satellite sensor raster types. The default for supported raster types is "Multiband"; otherwise, it's None.Example:{ "processingTemplate": "Surface Reflectance" } | Dictionary |
| field_name | The name of the field from which to extract values. | String |
| max_count | An integer that specifies the maximum number of field values to be returned. The values will be returned in the order that the raster items are ordered in the collection. If no value is specified, all the field values for the given field will be returned.(The default value is None) | Integer |
| field_name | The name of the field. Items with the same field values will be grouped together. | String |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| func | The Python function to map over the raster collection. The return value of the function must be a dictionary in which one of the keys is raster. For example, {"raster": output_raster_object, "name": input_item_name["name"]}. def NDVI(item): """Define a Python function to calculate NDVI""" # Create the raster object from the item raster_obj = item['Raster'] # Create raster objects for the red and NIR bands red, nir = raster_obj.getRasterBands(["red", "nir"]) # Compute NDVI ndvi = (nir-red)/(nir+red) return {"raster": ndvi, "name": item['Name'], "stdTime": item['AcquisitionDate']} ndvi_rc = rc.map(NDVI) | Function |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent using the extent of the last input raster.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the total extent of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| collection2 | The raster collection to be merged. | RasterCollection |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| mosaic_method | The method that will be used for overlapping areas between adjacent raster items. Mosaic method options include the following:FIRST—The pixel value from the first raster that is overlapping will be determined.LAST—The pixel value from the last raster that is overlapping will be determined.MEAN—The average pixel value from the two rasters that are overlapping will be determined.MINIMUM—The lower pixel value from the two raster datasets that are overlapping will be determined.MAXIMUM—The higher pixel value from the two raster datasets that are overlapping will be determined.SUM—The sum of pixel values from the two rasters that are overlapping will be determined.For more information about mosaic methods, see Displaying overlapping imagery.(The default value is First) | String |
| quality_rc_or_list | The raster collection or list of rasters to be used as quality indicators. For example, Landsat 8's Band 1 is the Coastal/Aerosol band, which can be used to estimate the concentration of fine aerosol particles such as smoke and haze in the atmosphere. For a collection of Landsat 8 images, use the selectBands method to return a RasterCollection object containing only Band 1 from each raster item. The number of raster items in the quality_rc_or_list must match the number of raster items in the raster collection to be mosaicked. | RasterCollection |
| statistic_type | The statistic used to compare the input collection or list of quality rasters.MAX—The highest pixel value in the input quality rasters will be the pixel value in the output raster. This is the default.MEDIAN—The median pixel value in the input quality rasters will be the pixel value in the output raster.MIN—The minimum pixel value in the input quality rasters will be the pixel value in the output raster.For example, to mosaic the input raster collection such that those with the lowest aerosol content are on top, use the MIN statistic type. | String |
| func[func,...] | The function used to reduce the raster collection. This argument also accepts a custom reducer function.(The default value is None) | String |
| func_args | A dictionary that contains additional parameters for the reducer function.rc = RasterCollection("<data path>") max_raster = rc.reduce(func=Max, func_args={'extent_type': 'UnionOf', 'cellsize_type': 'MinOf', 'ignore_nodata': True, 'process_as_multiband': True})(The default value is None) | Dictionary |
| band_ids_or_names[band_ids_or_names,...] | The names or index numbers of bands to be included in the returned raster items. This can be specified with a single string, integer, or a list of strings or integers. | Object |
| field_name | The name of the field to use for sorting. | String |
| ascending | Specifies whether to sort in ascending or descending order. (The default value is True) | Boolean |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the total extent of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster.(The default value is FirstOf) | String |
| ignore_nodata[ignore_nodata,...] | Specifies whether NoData values are ignored.(The default value is True) | Boolean |
| extent_type | Computes the extent of the output raster object when the input rasters have different extents.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster. | String |
| cellsize_type | Computes the cell size of the output raster object when the input rasters have different cell sizes.FirstOf—Defines the output extent using the extent of the first input raster.IntersectionOf—Defines the output extent as the intersecting area of the input rasters.UnionOf—Defines the output extent as the total extent of the input rasters.LastOf—Defines the output extent using the extent of the last input raster. | String |
| field_name | The field name to summarize. | String |
| summary_type[summary_type,...] | The summary methods to calculate for the selected field. One or more methods can be specified.COUNT—Calculates the number of non-null values of the selected field.COUNT_DISTINCT—Calculates the number of distinct values of the selected field.FIRST—Calculates the field value of the first object in the collection. HISTOGRAM—Calculates a histogram of the selected field.MAX—Calculates the maximum of the values of the selected field.MEAN—Calculates the mean of the selected field.MIN—Calculates the minimum of the values of the selected field.PRODUCT—Calculates the product of the values of the selected field.SAMPLE_SD—Calculates the sample standard deviation of the values of the selected field.SAMPLE_VAR—Calculates the sample variance of the values of the selected field.SUM—Calculates the sum of the values of the selected field. TOTAL_SD—Calculates the total standard deviation of the values of the selected field.TOTAL_VAR—Calculates the total variance of the values of the selected field.ALL—Calculates all the above statistics of the selected field.(The default value is ALL) | String |
| variable_field_name | The name of the field that contains the variable names. | String |
| dimension_field_names[dimension_field_names,...] | The name of the field or fields that contains the dimension names. This can be specified as a single string or a list of strings.For time-related dimensions, the field name must match one of the following to be recognized as a time field: StdTime, Date, Time, or AcquisitionDate. For nontime-related dimensions, the values in those fields must be type Double. If there are two or more dimensions, use a comma to separate the fields (for example, dimension_field_names = ["Time", "Depth"]). | String |

## Methods

### addField (field_name, field_values)

Adds a new field to the raster collection and populates it with values.

### filter ({where_clause}, {query_geometry_or_extent})

Filters the collection of raster items by attributes or geometry and returns a raster collection containing only the items that satisfy the filter. If no arguments are provided, all raster items from the raster collection will be returned in a new raster collection.

### filterByAttribute (field_name, operator, field_values)

Filters the collection of raster items by an attribute query and returns a raster collection containing only the items that satisfy the query. To query the raster collection based on a time field, use the filterByTime method.

### filterByCalendarRange (calendar_field, start, {end}, time_field_name, date_time_format)

Filters the collection of raster items based on the range of a calendar field and returns a raster collection containing only the items that satisfy the filter. If no arguments are provided, all raster items from the raster collection will be returned in a new raster collection.

### filterByGeometry (query_geometry_or_extent)

Filters the collection of raster items so that only those that intersect with the geometry will be returned.

### filterByRasterProperty (property_name, operator, property_values)

Filters the collection of raster items by a raster property query and returns a raster collection containing only the items that satisfy the query.

### filterByTime ({start_time}, {end_time}, {time_field_name}, {date_time_format})

Filters the collection of raster items by a time range and returns a raster collection containing only the items that satisfy the filter.

### fromSTACAPI (stac_api, {query}, {attribute_dict}, {request_method}, {request_params}, {context})

Creates a RasterCollection object from a SpatioTemporal Asset Catalog (STAC) API search query.

### fromSTACCatalog (stac_catalog, {attribute_dict}, {request_params}, {context})

Creates a RasterCollection object from a static SpatioTemporal Asset Catalog (STAC).

### getFieldValues (field_name, {max_count})

Returns the values of a specified field from the raster collection.

### groupBy (field_name)

Groups a raster collection based on a field. Each grouped raster collection can be accessed by the field value.

### majority ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the pixel value that occurs most frequently for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the majority method will determine the pixel value that occurs most frequently across all raster items for band 1, for band 2, for band 3, and for band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### map (func)

Maps a Python function over a raster collection.

### max ({ignore_nodata}, extent_type, cellsize_type)

Returns a raster object in which each band contains the maximum pixel values for that band across all rasters in the raster collection. For example, if there are 10 raster items in the raster collection, each with four bands, the max method will calculate the maximum pixel value that occurs across all raster items for band 1, band 2, band 3, and band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### mean ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the average pixel values for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the mean method will calculate the mean pixel value that occurs across all raster items for band 1, band 2, band 3, and band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### median ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the median pixel values for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the median method will calculate the median pixel value that occurs across all raster items for band 1, band 2, band 3, and band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### merge (collection2)

Returns a merged raster collection that includes all rasters from two raster collections.

### min ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the lowest pixel values for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the min method will calculate the minimum pixel value that occurs across all raster items for band 1, band 2, band 3, and band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### mosaic ({mosaic_method})

Returns a raster dataset in which all items in a raster collection have been mosaicked into a single raster.

### qualityMosaic (quality_rc_or_list, {statistic_type})

Returns a raster dataset in which all items in a raster collection have been mosaicked into a single raster based on a quality requirement.

### reduce (func, {func_args})

Returns a raster object where all images in the collection are combined into a single image based on a reducer function.For example, if there are ten raster items in the raster collection, each with four bands, the Min method can be specified as the reducer function. This will return a four-band raster, with each band containing the minimum values across all ten rasters.

### selectBands (band_ids_or_names)

Selects a list of bands from every raster item in a raster collection and returns a raster collection that contains raster items with only the selected bands.

### sort (field_name, {ascending})

Sorts the collection of rasters by a field name and returns a raster collection that is in the order specified.

### std ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the standard deviation pixel values for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the std method will calculate the standard deviation pixel value that occurs across all raster items for bands 1, 2, 3, and 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### sum ({ignore_nodata}, {extent_type}, {cellsize_type})

Returns a raster object in which each band contains the sum of pixel values for that band across all rasters in the raster collection.For example, if there are 10 raster items in the raster collection, each with four bands, the sum method will calculate the sum of pixel values for each pixel that occurs across all raster items for band 1, band 2, band 3, and band 4; a four-band raster is returned. Band numbers are matched between raster items using the band index, so the items in the raster collection must follow the same band order.

### summarizeField (field_name, {summary_type})

Summarizes the objects in a given field for a raster collection.

### toMultidimensionalRaster (variable_field_name, dimension_field_names)

Returns a multidimensional raster dataset, in which each item in the raster collection is a slice in the multidimensional raster.

## Code Samples

### Example 1

```python
RasterCollection (rasters, {attribute_dict})
```

### Example 2

```python
addField (field_name, field_values)
```

### Example 3

```python
filter ({where_clause}, {query_geometry_or_extent})
```

### Example 4

```python
filterByAttribute (field_name, operator, field_values)
```

### Example 5

```python
filterByCalendarRange (calendar_field, start, {end}, time_field_name, date_time_format)
```

### Example 6

```python
filterByGeometry (query_geometry_or_extent)
```

### Example 7

```python
filterByRasterProperty (property_name, operator, property_values)
```

### Example 8

```python
filterByTime ({start_time}, {end_time}, {time_field_name}, {date_time_format})
```

### Example 9

```python
fromSTACAPI (stac_api, {query}, {attribute_dict}, {request_method}, {request_params}, {context})
```

### Example 10

```python
{
"collections": ["sentinel-2-l2a"],
"bbox": [-110, 39.5, -105, 40.5],
"query": {"eo:cloud_cover": {"lt": 0.5}},
"datetime": "2020-10-05T00:00:00Z/2020-10-10T12:31:12Z",
"limit": 100
}
```

### Example 11

```python
{
"collections": ["sentinel-2-l2a"],
"bbox": [-110, 39.5, -105, 40.5],
"query": {"eo:cloud_cover": {"lt": 0.5}},
"datetime": "2020-10-05T00:00:00Z/2020-10-10T12:31:12Z",
"limit": 100
}
```

### Example 12

```python
{
"Name": "id",
"Sensor": "platform",
"StdTime": "datetime",
"Cloud Cover": "eo:cloud_cover",
"Spatial Reference": "proj:epsg",
"Extent": "bbox"
}
```

### Example 13

```python
{
"Name": "id",
"Sensor": "platform",
"StdTime": "datetime",
"Cloud Cover": "eo:cloud_cover",
"Spatial Reference": "proj:epsg",
"Extent": "bbox"
}
```

### Example 14

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 15

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 16

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 17

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 18

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 19

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 20

```python
{
    "assetManagement": [
       {"key": "TRAD",
        "path": ["alternate", "s3"]},
       {"key": "DRAD", 
        "path": ["alternate", "s3"]}
    ]
}
```

### Example 21

```python
{
    "assetManagement": [
       {"key": "TRAD",
        "path": ["alternate", "s3"]},
       {"key": "DRAD", 
        "path": ["alternate", "s3"]}
    ]
}
```

### Example 22

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 23

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 24

```python
fromSTACCatalog (stac_catalog, {attribute_dict}, {request_params}, {context})
```

### Example 25

```python
{
"Name": "id",
"Sensor": "platform",
"StdTime": "datetime",
"Cloud Cover": "eo:cloud_cover",
"Spatial Reference": "proj:epsg",
"Extent": "bbox"
}
```

### Example 26

```python
{
"Name": "id",
"Sensor": "platform",
"StdTime": "datetime",
"Cloud Cover": "eo:cloud_cover",
"Spatial Reference": "proj:epsg",
"Extent": "bbox"
}
```

### Example 27

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 28

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 29

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 30

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 31

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 32

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 33

```python
{
    "assetManagement": [
       {"key": "TRAD",
        "path": ["alternate", "s3"]},
       {"key": "DRAD", 
        "path": ["alternate", "s3"]}
    ]
}
```

### Example 34

```python
{
    "assetManagement": [
       {"key": "TRAD",
        "path": ["alternate", "s3"]},
       {"key": "DRAD", 
        "path": ["alternate", "s3"]}
    ]
}
```

### Example 35

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 36

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 37

```python
getFieldValues (field_name, {max_count})
```

### Example 38

```python
groupBy (field_name)
```

### Example 39

```python
majority ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 40

```python
def NDVI(item):
    """Define a Python function to calculate NDVI"""

    # Create the raster object from the item
    raster_obj = item['Raster']
    # Create raster objects for the red and NIR bands
		  red, nir = raster_obj.getRasterBands(["red", "nir"])
    # Compute NDVI
    ndvi = (nir-red)/(nir+red)
    return {"raster": ndvi, "name": item['Name'], "stdTime": item['AcquisitionDate']}

ndvi_rc = rc.map(NDVI)
```

### Example 41

```python
def NDVI(item):
    """Define a Python function to calculate NDVI"""

    # Create the raster object from the item
    raster_obj = item['Raster']
    # Create raster objects for the red and NIR bands
		  red, nir = raster_obj.getRasterBands(["red", "nir"])
    # Compute NDVI
    ndvi = (nir-red)/(nir+red)
    return {"raster": ndvi, "name": item['Name'], "stdTime": item['AcquisitionDate']}

ndvi_rc = rc.map(NDVI)
```

### Example 42

```python
max ({ignore_nodata}, extent_type, cellsize_type)
```

### Example 43

```python
mean ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 44

```python
median ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 45

```python
merge (collection2)
```

### Example 46

```python
min ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 47

```python
mosaic ({mosaic_method})
```

### Example 48

```python
qualityMosaic (quality_rc_or_list, {statistic_type})
```

### Example 49

```python
reduce (func, {func_args})
```

### Example 50

```python
rc = RasterCollection("<data path>")
max_raster = rc.reduce(func=Max, func_args={'extent_type': 'UnionOf', 
                                            'cellsize_type': 'MinOf', 
                                            'ignore_nodata': True, 
                                            'process_as_multiband': True})
```

### Example 51

```python
rc = RasterCollection("<data path>")
max_raster = rc.reduce(func=Max, func_args={'extent_type': 'UnionOf', 
                                            'cellsize_type': 'MinOf', 
                                            'ignore_nodata': True, 
                                            'process_as_multiband': True})
```

### Example 52

```python
selectBands (band_ids_or_names)
```

### Example 53

```python
sort (field_name, {ascending})
```

### Example 54

```python
std ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 55

```python
sum ({ignore_nodata}, {extent_type}, {cellsize_type})
```

### Example 56

```python
summarizeField (field_name, {summary_type})
```

### Example 57

```python
toMultidimensionalRaster (variable_field_name, dimension_field_names)
```

### Example 58

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

# Filter the collection to extract all images before year 2009
filtered_rc = rc.filterByTime(end_time = '2009-01-01T00:00:00', 
	time_field_name = 'AcquisitionDate')

# Return the dates in the filtered collection
dates = filtered_rc.getFieldValues('AcquisitionDate')
```

### Example 59

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

# Filter the collection to extract all images before year 2009
filtered_rc = rc.filterByTime(end_time = '2009-01-01T00:00:00', 
	time_field_name = 'AcquisitionDate')

# Return the dates in the filtered collection
dates = filtered_rc.getFieldValues('AcquisitionDate')
```

### Example 60

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

# Define line geometry 
line = arcpy.Polyline(arcpy.Array([arcpy.Point(54.9243963, 23.9279934), 
	arcpy.Point(55.29, 25.6)]),arcpy.SpatialReference(4326))

# Filter the collection to extract images that intersect with line geometry
filtered_rc = rc.filterByGeometry(line)

# Return the total number of items in the filtered collection
count = filtered_rc.count
```

### Example 61

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\data.gdb\time_series_landsat_images')

# Define line geometry 
line = arcpy.Polyline(arcpy.Array([arcpy.Point(54.9243963, 23.9279934), 
	arcpy.Point(55.29, 25.6)]),arcpy.SpatialReference(4326))

# Filter the collection to extract images that intersect with line geometry
filtered_rc = rc.filterByGeometry(line)

# Return the total number of items in the filtered collection
count = filtered_rc.count
```

### Example 62

```python
# Name: RasterCollection_Ex_03.py
# Description: Generates a raster collection from a mosaic dataset and
#	filters by an attribute field
# Requirements: ArcGIS Image Analyst 

# Import system modules
import arcpy
from arcpy.ia import *

# Define arguments
mosaic_dataset = r'C:\data.gdb\time_series_landsat_images'

# Construct a collection from a mosaic dataset
rc = RasterCollection(mosaic_dataset)

# Filter the collection to extract only images from Landsat 7
Landsat7_rc = rc.filterByAttribute("SensorName", "contain", "Landsat7")

# Return the names of the sensors in the filtered collection to double confirm
sensors= Landsat7_rc.getFieldValues(field_name)
```

### Example 63

```python
# Name: RasterCollection_Ex_03.py
# Description: Generates a raster collection from a mosaic dataset and
#	filters by an attribute field
# Requirements: ArcGIS Image Analyst 

# Import system modules
import arcpy
from arcpy.ia import *

# Define arguments
mosaic_dataset = r'C:\data.gdb\time_series_landsat_images'

# Construct a collection from a mosaic dataset
rc = RasterCollection(mosaic_dataset)

# Filter the collection to extract only images from Landsat 7
Landsat7_rc = rc.filterByAttribute("SensorName", "contain", "Landsat7")

# Return the names of the sensors in the filtered collection to double confirm
sensors= Landsat7_rc.getFieldValues(field_name)
```

### Example 64

```python
# Import system modules
import arcpy
from arcpy.ia import *
from arcpy import env

# Set workspace
arcpy.env.workspace = "C:/Data/NDVI"

# Get the list of tiff files from the workspace
NDVI_tiff_list = arcpy.ListRasters("*", "TIF")

# Generate a list of raster file names without the .tif extension 
name_list = []
for NDVI in NDVI_tiff_list:
    name_list.append(NDVI.replace(".tif","")

# Construct a collection from the list of raster file names
rc = RasterCollection(NDVI_tiff_list, {'name':name_list})

# Return a raster object where every pixel contains the 
# maximum value of that pixel over the entired NDVI raster collection
max_NDVI_rc = rc.max()

# Save the new raster object
max_NDVI_rc.save(r'C:\output\max_NDVI_raster.tif')
```

### Example 65

```python
# Import system modules
import arcpy
from arcpy.ia import *
from arcpy import env

# Set workspace
arcpy.env.workspace = "C:/Data/NDVI"

# Get the list of tiff files from the workspace
NDVI_tiff_list = arcpy.ListRasters("*", "TIF")

# Generate a list of raster file names without the .tif extension 
name_list = []
for NDVI in NDVI_tiff_list:
    name_list.append(NDVI.replace(".tif","")

# Construct a collection from the list of raster file names
rc = RasterCollection(NDVI_tiff_list, {'name':name_list})

# Return a raster object where every pixel contains the 
# maximum value of that pixel over the entired NDVI raster collection
max_NDVI_rc = rc.max()

# Save the new raster object
max_NDVI_rc.save(r'C:\output\max_NDVI_raster.tif')
```

### Example 66

```python
# Import system modules
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\Data.gdb\Landsat8_TimeSeries')

# Define a Python function to calculate the Soil Adjusted Vegetation Index (SAVI) 
def SAVI(item):
	# Get the raster object from the item
	raster = item['Raster']
	# Get the raster objects for the NIR and Red bands
	Red_band, NIR_band = raster.getRasterBands(["red","nir"])
	# Compute the index
	savi_index = ((1.5 * (NIR_band - Red_band))/(NIR_band + Red_band + 0.5))
	return{"raster": savi_index, "name": "Soil_Adjusted_Vegetation_Index", "StdTime":item['AcquisitionDate']}
	
# Run the Python function over the raster collection and generate a new collection
SAVI_rc = rc.map(SAVI)

# save it as a multidimensional raster
mdim_raster = SAVI_rc.toMultidimensionalRaster(variable_field_name = "name", dimension_field_names = "StdTime")
mdim_raster.save(r'C:\output\time_series_SAVI_raster.crf')
```

### Example 67

```python
# Import system modules
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Construct a collection from a mosaic dataset
rc = RasterCollection(r'C:\Data.gdb\Landsat8_TimeSeries')

# Define a Python function to calculate the Soil Adjusted Vegetation Index (SAVI) 
def SAVI(item):
	# Get the raster object from the item
	raster = item['Raster']
	# Get the raster objects for the NIR and Red bands
	Red_band, NIR_band = raster.getRasterBands(["red","nir"])
	# Compute the index
	savi_index = ((1.5 * (NIR_band - Red_band))/(NIR_band + Red_band + 0.5))
	return{"raster": savi_index, "name": "Soil_Adjusted_Vegetation_Index", "StdTime":item['AcquisitionDate']}
	
# Run the Python function over the raster collection and generate a new collection
SAVI_rc = rc.map(SAVI)

# save it as a multidimensional raster
mdim_raster = SAVI_rc.toMultidimensionalRaster(variable_field_name = "name", dimension_field_names = "StdTime")
mdim_raster.save(r'C:\output\time_series_SAVI_raster.crf')
```

### Example 68

```python
# Import system modules
from arcpy.ia import *
from arcpy import AIO

# 1) Creates a raster collection from Earth Search STAC API

# Defining query parameters
query_params = {
    "collections": ["sentinel-2-l2a"],
    "bbox": [-110, 39.5, -105, 40.5],
    "query": {"eo:cloud_cover": {"lt": 10}},
    "datetime": "2020-10-05T00:00:00Z/2020-10-10T12:31:12Z",
    "limit": 5,
}
 
# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "Platform": "platform",
    "StdTime": "datetime",
    "Cloud Cover": "eo:cloud_cover",
    "Spatial Reference": "proj:epsg",
    "Extent": "bbox",
}
 
# Construct a collection from the Sentinel-2 L2A data accesible through Earth Search STAC API

sentinel_2_rc = RasterCollection.fromSTACAPI(
    stac_api="https://earth-search.aws.element84.com/v1",
    query=query_params,
    attribute_dict=attribute_dict,
)

# Filter the collection further to work with data only from the Sentinel-2A satellite
filtered_rc = sentinel_2_rc.filterByAttribute("Platform", "EQUALS", "sentinel-2a")

# 2) Creates a raster collection from Planetray computer STAC API

# Defining query parameters
query_params = {
    "collections": ["naip"],
    "bbox": [-122.2751, 47.5469, -121.9613, 47.7458],
    "datetime": "2018-12-01/2020-12-31",
    "limit": 5,
}
 
# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "GSD": "gsd",
    "StdTime": "datetime",
    "State": "naip:state",
    "Spatial Reference": "proj:epsg",
    "Extent": "bbox",
}
 
# Construct a collection from the NAIP data accesible through Planetary Computer STAC API
naip_rc = RasterCollection.fromSTACAPI(
    stac_api="https://planetarycomputer.microsoft.com/api/stac/v1",
    query=query_params,
    attribute_dict=attribute_dict,
)
 
# Define a Python function to map grayscale raster function to the whole collection
def grayscale(item):
    # Get the raster object from the item
    raster = item["Raster"]
    # Get the raster objects for the NIR and Red bands
    gray_raster = Grayscale(raster)
    # Compute the index
    return {
        "raster": gray_raster,
        "name": f"gray_{item['Name']}",
        "StdTime": item["StdTime"],
    }
 
# apply grayscale function to each raster item in the raster collection using the map function
gray_rc = naip_rc.map(grayscale)
 
# work with the first raster in the grayscale collection
gray_raster_1 = gray_rc[0]["Raster"]

# 3) Creates a raster collection from the Landsat-9 C2-L2 data accesible through

# Digital Earth Africa STAC API (with custom asset selection) - Requires acs (AIO object).

landsat_dea_acs = AIO(r"C:\acsfiles\s3_dea_landsat.acs")

landsat_dea_rc = RasterCollection.fromSTACAPI(
      stac_api="https://explorer.digitalearth.africa/stac",
      query={
	"collections": ["ls9_sr"],
	"bbox": [
	        25.982987096443583,
	        29.249912751222965,
	        28.30879111403085,
	        31.348538968581714,
	      ],
	     "datetime": "2023-12-25/2023-12-31",
	},
	attribute_dict={
	    "Name": "id",
	    "Sensor": "platform",
	    "Cloud Cover": "eo:cloud_cover",
	    "Row": "landsat:wrs_row",
	    "Path": "landsat:wrs_path",
	},
	context={"assetManagement": ["SR_B4", "SR_B3", "SR_B2"]}, # rgb
)
```

### Example 69

```python
# Import system modules
from arcpy.ia import *
from arcpy import AIO

# 1) Creates a raster collection from Earth Search STAC API

# Defining query parameters
query_params = {
    "collections": ["sentinel-2-l2a"],
    "bbox": [-110, 39.5, -105, 40.5],
    "query": {"eo:cloud_cover": {"lt": 10}},
    "datetime": "2020-10-05T00:00:00Z/2020-10-10T12:31:12Z",
    "limit": 5,
}
 
# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "Platform": "platform",
    "StdTime": "datetime",
    "Cloud Cover": "eo:cloud_cover",
    "Spatial Reference": "proj:epsg",
    "Extent": "bbox",
}
 
# Construct a collection from the Sentinel-2 L2A data accesible through Earth Search STAC API

sentinel_2_rc = RasterCollection.fromSTACAPI(
    stac_api="https://earth-search.aws.element84.com/v1",
    query=query_params,
    attribute_dict=attribute_dict,
)

# Filter the collection further to work with data only from the Sentinel-2A satellite
filtered_rc = sentinel_2_rc.filterByAttribute("Platform", "EQUALS", "sentinel-2a")

# 2) Creates a raster collection from Planetray computer STAC API

# Defining query parameters
query_params = {
    "collections": ["naip"],
    "bbox": [-122.2751, 47.5469, -121.9613, 47.7458],
    "datetime": "2018-12-01/2020-12-31",
    "limit": 5,
}
 
# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "GSD": "gsd",
    "StdTime": "datetime",
    "State": "naip:state",
    "Spatial Reference": "proj:epsg",
    "Extent": "bbox",
}
 
# Construct a collection from the NAIP data accesible through Planetary Computer STAC API
naip_rc = RasterCollection.fromSTACAPI(
    stac_api="https://planetarycomputer.microsoft.com/api/stac/v1",
    query=query_params,
    attribute_dict=attribute_dict,
)
 
# Define a Python function to map grayscale raster function to the whole collection
def grayscale(item):
    # Get the raster object from the item
    raster = item["Raster"]
    # Get the raster objects for the NIR and Red bands
    gray_raster = Grayscale(raster)
    # Compute the index
    return {
        "raster": gray_raster,
        "name": f"gray_{item['Name']}",
        "StdTime": item["StdTime"],
    }
 
# apply grayscale function to each raster item in the raster collection using the map function
gray_rc = naip_rc.map(grayscale)
 
# work with the first raster in the grayscale collection
gray_raster_1 = gray_rc[0]["Raster"]

# 3) Creates a raster collection from the Landsat-9 C2-L2 data accesible through

# Digital Earth Africa STAC API (with custom asset selection) - Requires acs (AIO object).

landsat_dea_acs = AIO(r"C:\acsfiles\s3_dea_landsat.acs")

landsat_dea_rc = RasterCollection.fromSTACAPI(
      stac_api="https://explorer.digitalearth.africa/stac",
      query={
	"collections": ["ls9_sr"],
	"bbox": [
	        25.982987096443583,
	        29.249912751222965,
	        28.30879111403085,
	        31.348538968581714,
	      ],
	     "datetime": "2023-12-25/2023-12-31",
	},
	attribute_dict={
	    "Name": "id",
	    "Sensor": "platform",
	    "Cloud Cover": "eo:cloud_cover",
	    "Row": "landsat:wrs_row",
	    "Path": "landsat:wrs_path",
	},
	context={"assetManagement": ["SR_B4", "SR_B3", "SR_B2"]}, # rgb
)
```

### Example 70

```python
# Import system modules
from arcpy.ia import *

# 1) Creates a raster collection from Maxar STAC (Static Catalog)

# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "Platform": "platform",
    "StdTime": "datetime",
    "Data Area": "tile:data_area",
    "Clouds Percent": "tile:clouds_percent",
    "Spatial Reference": "proj:epsg",
}

# Construct a collection from Maxar STAC

     maxar_rc = RasterCollection.fromSTACCatalog(
     stac_catalog="https://maxar-opendata.s3.amazonaws.com/events/Emilia-Romagna-Italy-flooding-may23/ard/acquisition_collections/103005009DF96A00_collection.json",
     attribute_dict=attribute_dict,
)

# Filter the collection further to only work with data that has tile area less than 15 square kilometer

filtered_rc =maxar_rc.filterByAttribute("Data Area", "LESS_THAN", 15)

# 2) Creates a raster collection from New Zealand Imagery STAC (Static Catalog)

# Define attribute dictionary using the STAC Item properties
attribute_dict = {
   "Name": "id",
   "Start StdTime": "start_datetime",
   "End StdTime": "end_datetime",
   "Extent": "bbox",
}

# Construct a collection from New Zealand Imagery STAC

     nz_rc = RasterCollection.fromSTACCatalog(
     stac_catalog="https://nz-imagery.s3-ap-southeast-2.amazonaws.com/tasman/tasman_snc30002_2002_0.75m/rgb/2193/collection.json",
     attribute_dict=attribute_dict,
)

# Define a Python function to map grayscale raster function to the whole collection

def grayscale(item):
	# Get the raster object from the item
	raster = item["Raster"]

	# Get the raster objects for the NIR and Red bands
	gray_raster = Grayscale(raster)

	# Compute the index
	return {
		"raster": gray_raster,
		"name": f"gray_{item['Name']}",
		"StdTime": item["Start StdTime"],
		}

# apply grayscale function to each raster item in the raster collection using the map function

gray_rc = nz_rc.map(grayscale)

# work with the first raster in the grayscale collection

gray_raster_1 = gray_rc[8]["Raster"]

#3) Creates a raster collection from UMBRA STAC (with custom asset selection)

umbra_rc = RasterCollection.fromSTACCatalog(
stac_catalog="https://s3.us-west-2.amazonaws.com/umbra-open-data-catalog/stac/2024/2024-02/2024-02-19/catalog.json",
       attribute_dict={
	"Name": "id",
	"Sensor": "platform",
	"StdTime": "datetime",
	"Polarizations": "sar:polarizations",
	"Extent": "bbox",
	},
	context={"assetManagement": ["GEC"]},
	)
```

### Example 71

```python
# Import system modules
from arcpy.ia import *

# 1) Creates a raster collection from Maxar STAC (Static Catalog)

# Define attribute dictionary using the STAC Item properties
attribute_dict = {
    "Name": "id",
    "Platform": "platform",
    "StdTime": "datetime",
    "Data Area": "tile:data_area",
    "Clouds Percent": "tile:clouds_percent",
    "Spatial Reference": "proj:epsg",
}

# Construct a collection from Maxar STAC

     maxar_rc = RasterCollection.fromSTACCatalog(
     stac_catalog="https://maxar-opendata.s3.amazonaws.com/events/Emilia-Romagna-Italy-flooding-may23/ard/acquisition_collections/103005009DF96A00_collection.json",
     attribute_dict=attribute_dict,
)

# Filter the collection further to only work with data that has tile area less than 15 square kilometer

filtered_rc =maxar_rc.filterByAttribute("Data Area", "LESS_THAN", 15)

# 2) Creates a raster collection from New Zealand Imagery STAC (Static Catalog)

# Define attribute dictionary using the STAC Item properties
attribute_dict = {
   "Name": "id",
   "Start StdTime": "start_datetime",
   "End StdTime": "end_datetime",
   "Extent": "bbox",
}

# Construct a collection from New Zealand Imagery STAC

     nz_rc = RasterCollection.fromSTACCatalog(
     stac_catalog="https://nz-imagery.s3-ap-southeast-2.amazonaws.com/tasman/tasman_snc30002_2002_0.75m/rgb/2193/collection.json",
     attribute_dict=attribute_dict,
)

# Define a Python function to map grayscale raster function to the whole collection

def grayscale(item):
	# Get the raster object from the item
	raster = item["Raster"]

	# Get the raster objects for the NIR and Red bands
	gray_raster = Grayscale(raster)

	# Compute the index
	return {
		"raster": gray_raster,
		"name": f"gray_{item['Name']}",
		"StdTime": item["Start StdTime"],
		}

# apply grayscale function to each raster item in the raster collection using the map function

gray_rc = nz_rc.map(grayscale)

# work with the first raster in the grayscale collection

gray_raster_1 = gray_rc[8]["Raster"]

#3) Creates a raster collection from UMBRA STAC (with custom asset selection)

umbra_rc = RasterCollection.fromSTACCatalog(
stac_catalog="https://s3.us-west-2.amazonaws.com/umbra-open-data-catalog/stac/2024/2024-02/2024-02-19/catalog.json",
       attribute_dict={
	"Name": "id",
	"Sensor": "platform",
	"StdTime": "datetime",
	"Polarizations": "sar:polarizations",
	"Extent": "bbox",
	},
	context={"assetManagement": ["GEC"]},
	)
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
from arcpy.ia import *
rasterized_polygons = arcpy.ia.RasterizeFeatures("sample.tif",
	"ParkPolygons", "CarbonQuantity", "SMALLEST")
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 3

```python
from arcpy.ia import *
rasterized_polygons = arcpy.ia.RasterizeFeatures("sample.tif",
	"ParkPolygons", "CarbonQuantity", "SMALLEST")
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# convert regional park features to raster with carbon quantity field
rasterized_polygons = arcpy.ia.RasterizeFeatures(sample_raster,
	"C:/data/MyData.gdb/ParkPolygons", "CarbonQuantity", "SMALLEST")

# save the output
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# convert regional park features to raster with carbon quantity field
rasterized_polygons = arcpy.ia.RasterizeFeatures(sample_raster,
	"C:/data/MyData.gdb/ParkPolygons", "CarbonQuantity", "SMALLEST")

# save the output
rasterized_polygons.save("C:/arcpyExamples/outputs/ParkRaster.tif")
```

---

## RasterToXarray

## Summary

Converts a multidimensional raster to an xarray.Dataset containing labeled arrays (data array objects) with aligned dimensions.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input multidimensional raster to convert to an xarray. It can be a Raster object, a file path to a multidimensional raster dataset, or a netCDF file. | Raster |

## Code Samples

### Example 1

```python
RasterToXarray (in_raster)
```

### Example 2

```python
import arcpy
import xarray

# Get input Raster multidimensional information
inRas = arcpy.Raster('C:/data/temperature_3hour.crf', True)
inRas.mdinfo

# Convert Raster to Xarray Dataset
xrr = arcpy.ia.RasterToXarray(inRas)

# Upsample the data from originally 3 hour to hourly time interval
newXrr = xrr.resample(StdTime='1H').nearest(tolerance="1H")

#Convert Xarray dataset back to raster 
newRaster = arcpy.ia.XarrayToRaster(newXrr)
newRaster.save("C:/output/temperature_hourly.crf")
```

### Example 3

```python
import arcpy
import xarray

# Get input Raster multidimensional information
inRas = arcpy.Raster('C:/data/temperature_3hour.crf', True)
inRas.mdinfo

# Convert Raster to Xarray Dataset
xrr = arcpy.ia.RasterToXarray(inRas)

# Upsample the data from originally 3 hour to hourly time interval
newXrr = xrr.resample(StdTime='1H').nearest(tolerance="1H")

#Convert Xarray dataset back to raster 
newRaster = arcpy.ia.XarrayToRaster(newXrr)
newRaster.save("C:/output/temperature_hourly.crf")
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
from arcpy.ia import *
out_regiongrow_raster = RegionGrow("mlc.tif", "seeds.shp",
                                   "radius", "similarity")
out_regiongrow_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

### Example 3

```python
from arcpy.ia import *
out_regiongrow_raster = RegionGrow("mlc.tif", "seeds.shp",
                                   "radius", "similarity")
out_regiongrow_raster.save(
    "C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

### Example 4

```python
# Import system modules
import arcpy

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster = "C:/data/Multispectral_Landsat.tif"
seed_points = "C:/data/seed_point.shp"
max_growth_radius_field = "radius"
similarity_threshold_field = "similarity"
fill_value_field = "fill"

# Apply RegionGrow function
classified_raster = arcpy.ia.RegionGrow(raster, seed_points, max_growth_radius_field, similarity_threshold_field, fill_value_field)

# Save the output
classified_raster.save("C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

### Example 5

```python
# Import system modules
import arcpy

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster = "C:/data/Multispectral_Landsat.tif"
seed_points = "C:/data/seed_point.shp"
max_growth_radius_field = "radius"
similarity_threshold_field = "similarity"
fill_value_field = "fill"

# Apply RegionGrow function
classified_raster = arcpy.ia.RegionGrow(raster, seed_points, max_growth_radius_field, similarity_threshold_field, fill_value_field)

# Save the output
classified_raster.save("C:/arcpyExamples/outputs/Multispectral_Landsat_grow.crf")
```

---

## RegionPixelCount

## Summary

Groups connected regions with the same pixel value and calculates the number of pixels in each region.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| maximum_region_size | The maximum number of pixels a region can contain.(The default value is 100) | Integer |
| pixel_neighborhood | The number of neighborhoods used to assess pixel connectivity. Valid values are 4 and 8.(The default value is 4) | Integer |

## Code Samples

### Example 1

```python
RegionPixelCount (raster, {maximum_region_size}, {pixel_neighborhood})
```

### Example 2

```python
from arcpy.ia import *

pixel_count_raster = RegionPixelCount('C:/arcpyExamples/ndvi_threshold.tif', 1000, 4)

pixel_count_raster.save('C:/temp/ndvi_mask.tif')
```

### Example 3

```python
from arcpy.ia import *

pixel_count_raster = RegionPixelCount('C:/arcpyExamples/ndvi_threshold.tif', 1000, 4)

pixel_count_raster.save('C:/temp/ndvi_mask.tif')
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outEqualTo = Raster("degs") == Raster("negs")
outEqualTo.save("C:/iapyexamples/output/outequalto.tif")
```

### Example 2

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outEqualTo = Raster("degs") == Raster("negs")
outEqualTo.save("C:/iapyexamples/output/outequalto.tif")
```

### Example 3

```python
# Name: Op_EqualTo_Ex_02.py
# Description: Performs a relational equal-to operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute EqualTo
outEqualTo = inRaster1 == inRaster2

# Save the output 
outEqualTo.save("C:/iapyexamples/output/outequalto")
```

### Example 4

```python
# Name: Op_EqualTo_Ex_02.py
# Description: Performs a relational equal-to operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute EqualTo
outEqualTo = inRaster1 == inRaster2

# Save the output 
outEqualTo.save("C:/iapyexamples/output/outequalto")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outGTE = Raster("degs") >= Raster("negs")
outGTE.save("C:/iapyexamples/output/outgte.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outGTE = Raster("degs") >= Raster("negs")
outGTE.save("C:/iapyexamples/output/outgte.tif")
```

### Example 4

```python
# Name: Op_GreaterThanEqual_Ex_02.py
# Description: Performs a relational greater-than-equal operation on
#              two inputs on a cell-by-cell basis within the Analysis
#              window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThanEqual
outGTE = inRaster1 >= inRaster2

# Save the output 
outGTE.save("C:/iapyexamples/output/outgte")
```

### Example 5

```python
# Name: Op_GreaterThanEqual_Ex_02.py
# Description: Performs a relational greater-than-equal operation on
#              two inputs on a cell-by-cell basis within the Analysis
#              window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThanEqual
outGTE = inRaster1 >= inRaster2

# Save the output 
outGTE.save("C:/iapyexamples/output/outgte")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outGreaterThan = Raster("degs") > Raster("negs")
outGreaterThan.save("C:/iapyexamples/output/outgt.img")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outGreaterThan = Raster("degs") > Raster("negs")
outGreaterThan.save("C:/iapyexamples/output/outgt.img")
```

### Example 4

```python
# Name: Op_GreaterThan_Ex_02.py
# Description: Performs a relational greater-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThan
outGreaterThan = inRaster1 > inRaster2

# Save the output 
outGreaterThan.save("C:/iapyexamples/output/outgt")
```

### Example 5

```python
# Name: Op_GreaterThan_Ex_02.py
# Description: Performs a relational greater-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute GreaterThan
outGreaterThan = inRaster1 > inRaster2

# Save the output 
outGreaterThan.save("C:/iapyexamples/output/outgt")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outLTE = Raster("degs") <= Raster("negs")
outLTE.save("C:/iapyexamples/output/outlte.img")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outLTE = Raster("degs") <= Raster("negs")
outLTE.save("C:/iapyexamples/output/outlte.img")
```

### Example 4

```python
# Name: Op_LessThanEqual_Ex_02.py
# Description: Performs a relational less-than-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThanEqual
outLTE = inRaster1 <= inRaster2

# Save the output 
outLTE.save("C:/iapyexamples/output/outlte")
```

### Example 5

```python
# Name: Op_LessThanEqual_Ex_02.py
# Description: Performs a relational less-than-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThanEqual
outLTE = inRaster1 <= inRaster2

# Save the output 
outLTE.save("C:/iapyexamples/output/outlte")
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
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outLessThan = Raster("degs") < Raster("negs")
outLessThan.save("C:/iapyexamples/output/outlt.tif")
```

### Example 3

```python
import arcpy
from arcpy import env
from arcpy.ia import *
env.workspace = "C:/iapyexamples/data"
outLessThan = Raster("degs") < Raster("negs")
outLessThan.save("C:/iapyexamples/output/outlt.tif")
```

### Example 4

```python
# Name: Op_LessThan_Ex_02.py
# Description: Performs a relational less-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThan
outLessThan = inRaster1 < inRaster2

# Save the output 
outLessThan.save("C:/iapyexamples/output/outlt")
```

### Example 5

```python
# Name: Op_LessThan_Ex_02.py
# Description: Performs a relational less-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute LessThan
outLessThan = inRaster1 < inRaster2

# Save the output 
outLessThan.save("C:/iapyexamples/output/outlt")
```

---

## != (Relational Not Equal) operator

## Summary

Returns 1 for cells where the first raster is not equal to the second raster and 0 for cells where it is equal.

## Usage


## Code Samples

### Example 1

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/iapyexamples/output/outnotequal")
```

### Example 2

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/iapyexamples/output/outnotequal")
```

### Example 3

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/iapyexamples/output/outnotequal")
```

### Example 4

```python
# Name: Op_NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = Raster("degs")
inRaster2 = Raster("negs")

# Execute NotEqual
outNotEqual = inRaster1 != inRaster2

# Save the output 
outNotEqual.save("C:/iapyexamples/output/outnotequal")
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
from arcpy.ia import *
out_remap_raster = Remap("NomalRaster.tif")
out_remap_raster.save("C:/arcpyExamples/raster_remap.tif")
```

### Example 3

```python
from arcpy.ia import *
out_remap_raster = Remap("NomalRaster.tif")
out_remap_raster.save("C:/arcpyExamples/raster_remap.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 3

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 4

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 5

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 6

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.ia.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 7

```python
import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.ia.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 8

```python
import arcpy
from arcpy.ia import *

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

### Example 9

```python
import arcpy
from arcpy.ia import *

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.ia.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

---

## Reproject

## Summary

Creates a raster object by modifying the projection of the input raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| spatial_reference | The coordinate system used to reproject the data. This value is provided as a Python dictionary with the well-known ID (wkid). Optionally, you can include the latest well-known ID (latestWkid), or the current wkid value associated with the same spatial reference. For example, the WGS 1984 Web Mercator Auxiliary Sphere projection has a wkid of 102100 and a latestWKid of 3857. To reproject the input raster object into Web Mercator, use {"wkid" : 102100} or {"wkid" : 102100, "latestWkid" : 3857}.(The default value is None) | Dictionary |
| x_cell_size | The cell size in the x-dimension to use if resampling the data. If no value is provided or the value is 0, the output envelope (extent and cell sizes) is calculated from the input raster.(The default value is 0) | Integer |
| y_cell_size | The cell size in the y-dimension to use if resampling the data. If no value is provided or the value is 0, the output envelope (extent and cell sizes) is calculated from the input raster.(The default value is 0) | Integer |
| x_registration_point | The x-coordinate used to define the upper left corner of the dataset. The coordinate must be in the units of the new spatial reference. If both x_cell_size and y_cell_size are defined and greater than 0, they are used along with the x_registration_point and y_registration_point arguments to define the output envelope.(The default value is 0) | Double |
| y_registration_point | The y-coordinate used to define the upper left corner of the dataset. The coordinate must be in the units of the new spatial reference. If both x_cell_size and y_cell_size are defined and greater than 0, they are used along with the x_registration_point and y_registration_point arguments to define the output envelope.(The default value is 0) | Double |

## Code Samples

### Example 1

```python
Reproject (raster, {spatial_reference}, {x_cell_size}, {y_cell_size}, {x_registration_point}, {y_registration_point})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

input_raster = arcpy.Raster("LasVegas_LandCover.tif")

# reproject the input raster to WGS 1984 UTM Zone 11N 
reprojected_raster = arcpy.ia.Reproject(input_raster, {"wkid" : 32611})

# verify the new coordinate system
prj = print(arcpy.Describe(reprojected_raster).spatialReference.name)

# save the output
reprojected_raster.save("C:/arcpyExamples/outputs/LasVegas_LandCover_UTM11N.tif")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

input_raster = arcpy.Raster("LasVegas_LandCover.tif")

# reproject the input raster to WGS 1984 UTM Zone 11N 
reprojected_raster = arcpy.ia.Reproject(input_raster, {"wkid" : 32611})

# verify the new coordinate system
prj = print(arcpy.Describe(reprojected_raster).spatialReference.name)

# save the output
reprojected_raster.save("C:/arcpyExamples/outputs/LasVegas_LandCover_UTM11N.tif")
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

resampled_raster = arcpy.ia.Resample("NAIP_1_meter.tif", "NearestNeighbor", 1, 3)
```

### Example 3

```python
Import arcpy

resampled_raster = arcpy.ia.Resample("NAIP_1_meter.tif", "NearestNeighbor", 1, 3)
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

RTVICore_raster = arcpy.ia.RTVICore("Sentinel2.tif",8,5,3)
```

### Example 5

```python
import arcpy

RTVICore_raster = arcpy.ia.RTVICore("Sentinel2.tif",8,5,3)
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

SAVI_raster = arcpy.ia.SAVI("Landsat8.tif",5,4,0.5)
```

### Example 5

```python
import arcpy

SAVI_raster = arcpy.ia.SAVI("Landsat8.tif",5,4,0.5)
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
from arcpy.ia import *
out_segmented_raster = SegMeanShift("Multispectral_Landsat.tif")
out_segmented_raster.save("C:/arcpyExamples/outputs/segmeanshift_out.crf")
```

### Example 3

```python
from arcpy.ia import *
out_segmented_raster = SegMeanShift("Multispectral_Landsat.tif")
out_segmented_raster.save("C:/arcpyExamples/outputs/segmeanshift_out.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster = "C:/data/Multispectral_Landsat.tif"
spectral_detail= 15.5
spatial_detail= 15
spectral_radius=None
spatial_radius=None
min_num_pixels_per_segment= 20

# Apply RegionGrow function
arcpy.ia.SegMeanShift(raster, spectral_detail, spatial_detail, spectral_radius, spatial_radius, min_num_pixels_per_segment)

# Save the output
segmented_raster.save("C:/arcpyExamples/outputs/Multispectral_Landsat_seg.crf")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the local variables
raster = "C:/data/Multispectral_Landsat.tif"
spectral_detail= 15.5
spatial_detail= 15
spectral_radius=None
spatial_radius=None
min_num_pixels_per_segment= 20

# Apply RegionGrow function
arcpy.ia.SegMeanShift(raster, spectral_detail, spatial_detail, spectral_radius, spatial_radius, min_num_pixels_per_segment)

# Save the output
segmented_raster.save("C:/arcpyExamples/outputs/Multispectral_Landsat_seg.crf")
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
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# use built-in colorramp slope
colorramp_name = "Slope"

# Execute arcpy.ia.ShadedRelief
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colorramp=colorramp_name, slope_type = "SCALED",
                            ps_power=0.664, psz_factor=0.024, remove_edge_effect=False)
shadedRelief.save("C:/output/shadedrelief_output2.tif")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/data"

# input raster
inRasters= = "input_raster.tif"

# use built-in colorramp slope
colorramp_name = "Slope"

# Execute arcpy.ia.ShadedRelief
shadedRelief = ShadedRelief(imagePath1, azimuth=315, altitude=45, z_factor=1, colorramp=colorramp_name, slope_type = "SCALED",
                            ps_power=0.664, psz_factor=0.024, remove_edge_effect=False)
shadedRelief.save("C:/output/shadedrelief_output2.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *
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
from arcpy.ia import *
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

## Slope

## Summary

Represents the rate of change of elevation for each pixel.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dem | The input elevation raster. | Raster |
| z_factor | The z-factor is a scaling factor used to convert the elevation values for the following purposes: Convert the elevation units (such as meters or feet) to the horizontal coordinate units of the dataset, which may be feet, meters, or degrees.Add vertical exaggeration for visual effect. If the x,y units and z units are in the same units of measure, the z-factor should be set to 1. The z-values of the input surface are multiplied by the z-factor when calculating the final output surface.(The default value is 1) | Double |
| slope_type | The inclination of slope can be output as either a value in degrees or percent rise. Specify one of the following: DEGREE, PERCENTRISE, or SCALED. For more information, see Slope function.(The default value is DEGREE) | String |
| ps_power | Accounts for the altitude changes (or scale) as the viewer zooms in and out on the map display. It is the exponent applied to the pixel size term in the equation that controls the rate at which the z-factor changes to avoid significant loss of relief.This parameter is only valid when slope_type is SCALED.(The default value is 0.664) | Double |
| psz_factor | Accounts for changes in scale as the viewer zooms in and out on the map display. The value controls the rate at which the z-factor changes.This parameter is only valid when slope_type is SCALED.(The default value is 0.024) | Double |
| remove_edge_effect | Using this option will avoid any resampling of artifacts that may occur along the edges of a raster. The output pixels along the edge of a raster or next to pixels without a value will be populated with NoData. It is recommended that you use this option only when there are other rasters with overlapping pixels available. When overlapping pixels are available, these areas of NoData will display the overlapping pixel values instead of being blank.False—Bilinear resampling will be applied uniformly to resample the output.True—Bilinear resampling will be used to resample the output, except along the edges of the rasters or next to pixels of NoData. These pixels will be populated with NoData. This will reduce any sharp edge effects that may otherwise occur.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Slope (dem, {z_factor}, {slope_type}, {ps_power}, {psz_factor}, {remove_edge_effect})
```

### Example 2

```python
from arcpy.ia import *
out_slope_raster = Slope("elevation.tif")
out_slope_raster.save("C:/arcpyExamples/outputs/slope.tif")
```

### Example 3

```python
from arcpy.ia import *
out_slope_raster = Slope("elevation.tif")
out_slope_raster.save("C:/arcpyExamples/outputs/slope.tif")
```

### Example 4

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_dem = "elevation.tif"

# Execute the Slope function
out_slope_raster = Slope(in_raster)

# Save the output
out_slope_raster.save("C:/arcpyExamples/outputs/slope.tif")
```

### Example 5

```python
# Import the system modules
import arcpy
from arcpy.ia import *

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_dem = "elevation.tif"

# Execute the Slope function
out_slope_raster = Slope(in_raster)

# Save the output
out_slope_raster.save("C:/arcpyExamples/outputs/slope.tif")
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
from arcpy.ia import *
out_raster = SpectralConversion("3bands_raster",
                                [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8])
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

### Example 5

```python
from arcpy.ia import *
out_raster = SpectralConversion("3bands_raster",
                                [0.1, 0.9, 0, 0.3, 0, 0.7, 0.1, 0.1, 0.8])
out_raster.save("C:/arcpyExamples/outputs/out_spectralconversion_raster.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

## SR

## Summary

Calculates the Simple Ratio (SR) from a multiband raster object and returns a raster object with the index values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input raster. | Raster |
| nir_band_id | The band ID of the near-infrared band. The ID index uses one-based indexing.(The default value is 5) | Integer |
| red_band_id | The band ID of the red band. The ID index uses one-based indexing.(The default value is 4) | Integer |

## Code Samples

### Example 1

```python
SR = NIR / Red
```

### Example 2

```python
SR = NIR / Red
```

### Example 3

```python
SR (raster, {nir_band_id}, {red_band_id})
```

### Example 4

```python
import arcpy

SR_raster = arcpy.ia.SR("MSimage.tif",5,4)
```

### Example 5

```python
import arcpy

SR_raster = arcpy.ia.SR("MSimage.tif",5,4)
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

SRre_raster = arcpy.ia.SRre("Sentinel2.tif",8,6)
```

### Example 5

```python
import arcpy

SRre_raster = arcpy.ia.SRre("Sentinel2.tif",8,6)
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
from arcpy.ia import *
LandCover_filled = arcpy.ia.Statistics("LandCover.tif", 5, 5, "majority", True)
LandCover_filles.save("LandCover_majority_5_by_5.tif")
```

### Example 3

```python
from arcpy.ia import *
LandCover_filled = arcpy.ia.Statistics("LandCover.tif", 5, 5, "majority", True)
LandCover_filles.save("LandCover_majority_5_by_5.tif")
```

### Example 4

```python
import arcpy
from arcpy import env
from arcpy.ia import *

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
from arcpy.ia import *

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

StatisticsHistogram_raster = arcpy.ia.StatisticsHistogram(imagePath1, [-4.514, 4.338, 0.0043, 1.0], None)
```

### Example 5

```python
import arcpy

StatisticsHistogram_raster = arcpy.ia.StatisticsHistogram(imagePath1, [-4.514, 4.338, 0.0043, 1.0], None)
```

---

## StdDev

## Summary

Creates a raster object in which each pixel contains the standard deviation value across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
StdDev (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = StdDev(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = StdDev(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
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

Stretch_raster = arcpy.ia.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
```

### Example 3

```python
import arcpy

Stretch_raster = arcpy.ia.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
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
import arcpy
from arcpy.ia import *

in_raster = Raster('ClimateData_Daily.nc', True)

# Select two variables: precipitation and water temperature 
out_subset_raster1 = Subset(in_raster, variables = ['precip', 'water_temp'])
print(out_subset_raster1.variables)

# Filter variables that have the Depth dimension and where depth=0.
# For variables that do not have dimension depth, all slices are selected.
out_subset_raster2 = Subset(in_raster, dimension_definitions = {'depth' : 0})   
print(out_subset_raster2.variables)

# Select water temperature data on the 1st of every January
out_subset_raster3 = Subset(in_raster, variables = 'water_temp', 
	dimension_definitions = {'time': 
	('1980-01-01T12:00:00', None, 1, 'year')})   
print(out_subset_raster3.variables)

# Select water temperature data for the first three months of every year
out_subset_raster4 = Subset(in_raster, variables = 'water_temp',
	dimension_definitions = {'time':('1980-01-01T00:00:00', 
	'1980-03-31T00:00:00', 1, 'year')})   

# Select both variables for January in 5 year increments: 1980, 1985, 1990, etc.
out_subset_raster5 = Subset(in_raster, variables = ['precip', 'water_temp']), 
	dimension_definitions = {'time':
	('1980-01-01T00:00:00', '1980-01-31T00:00:00', 5, 'year')})   

# Select surface water temperature in January 1980
out_subset_raster6 = Subset(in_raster, variables = 'water_temp', 
	dimension_definitions  = {'time': 
	('1980-01-01T12:00:00', '1980-01-31T12:00:00'), 'depth': 0})
print(out_subset_raster4.mdinfo)

# Save the water temperature in January 1980
out_subset_raster6.save("c:/output/Jan1980_watertemp.crf")
```

### Example 3

```python
import arcpy
from arcpy.ia import *

in_raster = Raster('ClimateData_Daily.nc', True)

# Select two variables: precipitation and water temperature 
out_subset_raster1 = Subset(in_raster, variables = ['precip', 'water_temp'])
print(out_subset_raster1.variables)

# Filter variables that have the Depth dimension and where depth=0.
# For variables that do not have dimension depth, all slices are selected.
out_subset_raster2 = Subset(in_raster, dimension_definitions = {'depth' : 0})   
print(out_subset_raster2.variables)

# Select water temperature data on the 1st of every January
out_subset_raster3 = Subset(in_raster, variables = 'water_temp', 
	dimension_definitions = {'time': 
	('1980-01-01T12:00:00', None, 1, 'year')})   
print(out_subset_raster3.variables)

# Select water temperature data for the first three months of every year
out_subset_raster4 = Subset(in_raster, variables = 'water_temp',
	dimension_definitions = {'time':('1980-01-01T00:00:00', 
	'1980-03-31T00:00:00', 1, 'year')})   

# Select both variables for January in 5 year increments: 1980, 1985, 1990, etc.
out_subset_raster5 = Subset(in_raster, variables = ['precip', 'water_temp']), 
	dimension_definitions = {'time':
	('1980-01-01T00:00:00', '1980-01-31T00:00:00', 5, 'year')})   

# Select surface water temperature in January 1980
out_subset_raster6 = Subset(in_raster, variables = 'water_temp', 
	dimension_definitions  = {'time': 
	('1980-01-01T12:00:00', '1980-01-31T12:00:00'), 'depth': 0})
print(out_subset_raster4.mdinfo)

# Save the water temperature in January 1980
out_subset_raster6.save("c:/output/Jan1980_watertemp.crf")
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

Sultan_raster = arcpy.ia.Sultan("LandsatETM.tif",1,3,4,5,6)
```

### Example 9

```python
import arcpy

Sultan_raster = arcpy.ia.Sultan("LandsatETM.tif",1,3,4,5,6)
```

---

## Sum

## Summary

Creates a raster object in which each pixel contains the sum of values across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Sum (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Sum(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Sum(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
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

TasseledCap_raster = arcpy.ia.TasseledCap("Worldview2.tif")
```

### Example 3

```python
import arcpy

TasseledCap_raster = arcpy.ia.TasseledCap("Worldview2.tif")
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

Binary_raster = arcpy.ia.Threshold("Landsat8.TIF")
```

### Example 3

```python
import arcpy

Binary_raster = arcpy.ia.Threshold("Landsat8.TIF")
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

transpose_raster = arcpy.ia.TransposeBits("Landsat_8.tif",[4, 5],[0, 1], 0, None)
```

### Example 3

```python
import acrpy

transpose_raster = arcpy.ia.TransposeBits("Landsat_8.tif",[4, 5],[0, 1], 0, None)
```

---

## TrendToRGB

## Summary

Converts a trend raster to a three-band (red, green, and blue) raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster | The input trend raster. | Raster |
| model_type | The trend model type information to be converted to RGB.LINEAR—Linear trend information will be converted to RGB. This is the default.HARMONIC—Harmonic trend model information will be converted to RGB.(The default value is LINEAR) | String |

## Code Samples

### Example 1

```python
TrendToRGB (raster, {model_type})
```

### Example 2

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
trend_raster = "precip_trend.tif"
model_type = "HARMONIC"

# convert the trend raster to a RGB raster
precipTrend_rgb = TrendToRGB(trend_raster,model_type)

# save the output
precipTrend_rgb.save("C:/arcpyExamples/outputs/precipTrend_rgb.tif")
```

### Example 3

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
trend_raster = "precip_trend.tif"
model_type = "HARMONIC"

# convert the trend raster to a RGB raster
precipTrend_rgb = TrendToRGB(trend_raster,model_type)

# save the output
precipTrend_rgb.save("C:/arcpyExamples/outputs/precipTrend_rgb.tif")
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

TSAVI_raster = arcpy.ia.TSAVI("Landsat8.tif",5,4,0.33,0.5,1.5)
```

### Example 5

```python
import arcpy

TSAVI_raster = arcpy.ia.TSAVI("Landsat8.tif",5,4,0.33,0.5,1.5)
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
from arcpy.ia import *
out_unit_raster = UnitConversion("wind_speed_meter_per_second.tif",
                                 "MetersPerSecond'", "KilometersPerHour")
out_unit_raster.save("C:/arcpyExamples/outputs/wind_speed_km_per_hour.tif")
```

### Example 3

```python
from arcpy.ia import *
out_unit_raster = UnitConversion("wind_speed_meter_per_second.tif",
                                 "MetersPerSecond'", "KilometersPerHour")
out_unit_raster.save("C:/arcpyExamples/outputs/wind_speed_km_per_hour.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

VARI_raster = arcpy.ia.VARI("Landsat8.tif",4,3,2)
```

### Example 5

```python
import arcpy

VARI_raster = arcpy.ia.VARI("Landsat8.tif",4,3,2)
```

---

## Variety

## Summary

Creates a raster object in which each pixel contains the number of unique values across multiple rasters.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| rasters[rasters,...] | The list of input rasters. | Raster |
| extent_type | The method that will be used to compute the extent of the output when the input rasters have different extents.FirstOf—The output extent will be defined using the extent of the first input raster.LastOf—The output extent will be defined using the extent of the last input raster.IntersectionOf—The output extent will be defined as the intersecting area of the input rasters.UnionOf—The output extent will be defined as the total extent of the input rasters.(The default value is FirstOf) | String |
| cellsize_type | The method that will be used to compute the pixel size of the output when the input rasters have different pixel sizes.FirstOf—The output pixel size will be defined using the pixel size of the first input raster.LastOf—The output pixel size will be defined using the pixel size of the last input raster.MaxOf—The output pixel size will be defined using the maximum pixel size of the input rasters.MeanOf—The output pixel size will be defined using the mean of both input rasters.MinOf—The output pixel size will be defined using the minimum pixel size of the input rasters.(The default value is FirstOf) | String |
| ignore_nodata | Specifies whether NoData values will be ignored in the calculation.True—The analysis will include all valid pixels in the input rasters and ignore any NoData pixels.False—The analysis will result in NoData if there are any NoData values for the pixels in the input rasters.(The default value is False) | Boolean |
| process_as_multiband | Specifies how the bands of the input rasters will be processed.True—Each multiband raster will be processed as a multiband raster. The operation will be performed for each band from one input using the corresponding band number from other inputs.False—Each band from a multiband raster input will be processed separately as a single-band raster.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
Variety (rasters, {extent_type}, {cellsize_type}, {ignore_nodata}, {process_as_multiband})
```

### Example 2

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Variety(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
```

### Example 3

```python
from arcpy.ia import * 

rc = RasterCollection([landsat_1, landsat_2, landsat_3]) 

range_raster = Variety(rc, extent_type = "UnionOf", cellsize_type = "MinOf", 
	ignore_nodata = True, process_as_multiband = True)
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

Stretch_raster = arcpy.ia.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
```

### Example 3

```python
import arcpy

Stretch_raster = arcpy.ia.Stretch(imagePath1, "PercentClip", None, None, None, None, True, 0.25, 0.75, None, None, None)
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
from arcpy.ia import *
out_vectorfield_raster = VectorField("magnitude", "direction", "Vector-MagDir",
                                 None, "Vector-UV)
out_vectorfield_raster.save("C:/arcpyExamples/outputs/vector_field_UV.crf")
```

### Example 3

```python
from arcpy.ia import *
out_vectorfield_raster = VectorField("magnitude", "direction", "Vector-MagDir",
                                 None, "Vector-UV)
out_vectorfield_raster.save("C:/arcpyExamples/outputs/vector_field_UV.crf")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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
from arcpy.ia import *
out_windchill_raster = WindChill("temperature.tif", "windspeed.tif", "",
                                 "km/h", "Celsius")
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_C.tif")
```

### Example 5

```python
from arcpy.ia import *
out_windchill_raster = WindChill("temperature.tif", "windspeed.tif", "",
                                 "km/h", "Celsius")
out_windchill_raster.save("C:/arcpyExamples/outputs/wind_chill_C.tif")
```

### Example 6

```python
# Import system modules
import arcpy
from arcpy.ia import *

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
from arcpy.ia import *

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

## XarrayToRaster

## Summary

Converts an xarray.Dataset to a multidimensional raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_xarray | The input xarray.Dataset object to convert to a multidimensional raster. | xarray.Dataset |

## Code Samples

### Example 1

```python
XarrayToRaster (in_xarray)
```

### Example 2

```python
import arcpy
import xarray

# Get input Raster multidimensional information
inRas = arcpy.Raster('C:/data/temperature_3hour.crf', True)
inRas.mdinfo

# Convert Raster to Xarray Dataset
xrr = arcpy.ia.RasterToXarray(inRas)

# Upsample the data from originally 3 hour to hourly time interval
newXrr = xrr.resample(StdTime='1H').nearest(tolerance="1H")

#Convert Xarray dataset back to raster 
newRaster = arcpy.ia.XarrayToRaster(newXrr)
newRaster.save("C:/output/temperature_hourly.crf")
```

### Example 3

```python
import arcpy
import xarray

# Get input Raster multidimensional information
inRas = arcpy.Raster('C:/data/temperature_3hour.crf', True)
inRas.mdinfo

# Convert Raster to Xarray Dataset
xrr = arcpy.ia.RasterToXarray(inRas)

# Upsample the data from originally 3 hour to hourly time interval
newXrr = xrr.resample(StdTime='1H').nearest(tolerance="1H")

#Convert Xarray dataset back to raster 
newRaster = arcpy.ia.XarrayToRaster(newXrr)
newRaster.save("C:/output/temperature_hourly.crf")
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
from arcpy.ia import *
out_zonalremap_raster = ZonalRemap("cloudceilings.tif","zonal.csv", "zone.tif")
out_zonalremap_raster.save("C:/arcpyExamples/outputs/Zonal_remap.tif")
```

### Example 3

```python
from arcpy.ia import *
out_zonalremap_raster = ZonalRemap("cloudceilings.tif","zonal.csv", "zone.tif")
out_zonalremap_raster.save("C:/arcpyExamples/outputs/Zonal_remap.tif")
```

### Example 4

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the local variables
in_raster = "C:/data/NDVI.tif"
zonal_attribute_table = "C:/data/Features.gdb/remapValues"
zone_raster = "C:/data/neighborhoods.tif"

# Apply ZonalRemap function
zonal_remap_raster = arcpy.ia.ZonalRemap(in_raster, zonal_attribute_table, zone_raster)

# Save the output
zonal_remap_raster.save("C:/arcpyExamples/outputs/neighborhood_NDVI.tiff")
```

### Example 5

```python
# Import system modules
import arcpy
from arcpy.ia import *

# Set the local variables
in_raster = "C:/data/NDVI.tif"
zonal_attribute_table = "C:/data/Features.gdb/remapValues"
zone_raster = "C:/data/neighborhoods.tif"

# Apply ZonalRemap function
zonal_remap_raster = arcpy.ia.ZonalRemap(in_raster, zonal_attribute_table, zone_raster)

# Save the output
zonal_remap_raster.save("C:/arcpyExamples/outputs/neighborhood_NDVI.tiff")
```

---
