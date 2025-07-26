# Network Analyst Complete Reference

*Consolidated from 33 individual documentation files*

---

## Access analysis outputs

## Code Samples

### Example 1

```python
# Solve the analysis
result = route.solve()

# Save results to disk using the export method
output_feature_class = "C:/data/io.gdb/Routes"
result.export(arcpy.nax.RouteOutputDataType.Routes, output_feature_class)
```

### Example 2

```python
# Solve the analysis
result = route.solve()

# Save results to disk using the export method
output_feature_class = "C:/data/io.gdb/Routes"
result.export(arcpy.nax.RouteOutputDataType.Routes, output_feature_class)
```

### Example 3

```python
# Solve the analysis
result = route.solve()

# Retrieve specific fields of interest using a searchCursor
for row in result.searchCursor(arcpy.nax.RouteOutputDataType.Routes, ["Name", "Total_Miles"]):
    # Retrieve the name and mileage for each route
    route_name = row[0]
    route_miles = row[1]
    # Print the route's name if the route's total mileage is greater than 10 miles
    if route_miles > 10:
        print(route_name)
```

### Example 4

```python
# Solve the analysis
result = route.solve()

# Retrieve specific fields of interest using a searchCursor
for row in result.searchCursor(arcpy.nax.RouteOutputDataType.Routes, ["Name", "Total_Miles"]):
    # Retrieve the name and mileage for each route
    route_name = row[0]
    route_miles = row[1]
    # Print the route's name if the route's total mileage is greater than 10 miles
    if route_miles > 10:
        print(route_name)
```

### Example 5

```python
import pandas as pd

# Solve the analysis
result = route.solve()

# Read the results into a pandas dataframe
fields = ["Name", "Total_Miles"]
with result.searchCursor(arcpy.nax.RouteOutputDataType.Routes, fields) as cur:
    df = pd.DataFrame(cur, columns=fields)
# Do some further analysis...
```

### Example 6

```python
import pandas as pd

# Solve the analysis
result = route.solve()

# Read the results into a pandas dataframe
fields = ["Name", "Total_Miles"]
with result.searchCursor(arcpy.nax.RouteOutputDataType.Routes, fields) as cur:
    df = pd.DataFrame(cur, columns=fields)
# Do some further analysis...
```

### Example 7

```python
# Solve the analysis
result = od_matrix.solve()

# Retrieve the Arrow table using the toArrowTable method
arrow_table = result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID"]
)

# Count the number of destinations reached by each origin.
# The result is a pyarrow structured array.
counts = arrow_table["OriginOID"].value_counts()

# If desired, you can convert the Arrow table to a pandas dataframe
# or many other supported formats.
df = arrow_table.to_pandas(split_blocks=True, zero_copy_only=True)
```

### Example 8

```python
# Solve the analysis
result = od_matrix.solve()

# Retrieve the Arrow table using the toArrowTable method
arrow_table = result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID"]
)

# Count the number of destinations reached by each origin.
# The result is a pyarrow structured array.
counts = arrow_table["OriginOID"].value_counts()

# If desired, you can convert the Arrow table to a pandas dataframe
# or many other supported formats.
df = arrow_table.to_pandas(split_blocks=True, zero_copy_only=True)
```

### Example 9

```python
# Solve the analysis
result = od_matrix.solve()

# Using the toArrowTable method to save the OD Cost Matrix result permanently to a file.
result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID", "DestinationOID", "Total_Time", "Total_Distance"],
    os.path.join(output_folder, "ODLines.arrow")
)
```

### Example 10

```python
# Solve the analysis
result = od_matrix.solve()

# Using the toArrowTable method to save the OD Cost Matrix result permanently to a file.
result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID", "DestinationOID", "Total_Time", "Total_Distance"],
    os.path.join(output_folder, "ODLines.arrow")
)
```

### Example 11

```python
import pyarrow

# Read the data from the file
with pyarrow.memory_map(os.path.join(output_folder, "ODLines.arrow"), 'r') as source:
    batch_reader = pyarrow.ipc.RecordBatchFileReader(source)
    table_from_file = batch_reader.read_all()

# Create a pandas dataframe using the records from the memory-mapped file using zero copy
df = table_from_file.to_pandas(split_blocks=True, zero_copy_only=True)
# Do some further analysis...
```

### Example 12

```python
import pyarrow

# Read the data from the file
with pyarrow.memory_map(os.path.join(output_folder, "ODLines.arrow"), 'r') as source:
    batch_reader = pyarrow.ipc.RecordBatchFileReader(source)
    table_from_file = batch_reader.read_all()

# Create a pandas dataframe using the records from the memory-mapped file using zero copy
df = table_from_file.to_pandas(split_blocks=True, zero_copy_only=True)
# Do some further analysis...
```

### Example 13

```python
# Solve the analysis
result = od_matrix.solve()

# Using the toArrowTable method to save the OD Cost Matrix result permanently to a file.
# Use max_batch_size to prevent memory errors.
out_arrow_file = os.path.join(output_folder, "ODLines.arrow")
arrow_table = result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID", "DestinationOID", "Total_Time", "Total_Distance"],
    out_arrow_file,
    max_batch_size=1000000  # Limit the output batches to one million records
)
```

### Example 14

```python
# Solve the analysis
result = od_matrix.solve()

# Using the toArrowTable method to save the OD Cost Matrix result permanently to a file.
# Use max_batch_size to prevent memory errors.
out_arrow_file = os.path.join(output_folder, "ODLines.arrow")
arrow_table = result.toArrowTable(
    arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines,
    ["OriginOID", "DestinationOID", "Total_Time", "Total_Distance"],
    out_arrow_file,
    max_batch_size=1000000  # Limit the output batches to one million records
)
```

### Example 15

```python
import pyarrow

# Process the OD Cost Matrix results in batches
with pyarrow.memory_map(os.path.join(output_folder, "ODLines.arrow"), 'r') as source:
    batch_reader = pyarrow.ipc.RecordBatchFileReader(source)
    for i in range(batch_reader.num_record_batches):
        rb = batch_reader.get_batch(i)
        # Convert this record batch to a pandas dataframe using zero copy
        df = rb.to_pandas(split_blocks=True, zero_copy_only=True)
        # Do some further analysis...
```

### Example 16

```python
import pyarrow

# Process the OD Cost Matrix results in batches
with pyarrow.memory_map(os.path.join(output_folder, "ODLines.arrow"), 'r') as source:
    batch_reader = pyarrow.ipc.RecordBatchFileReader(source)
    for i in range(batch_reader.num_record_batches):
        rb = batch_reader.get_batch(i)
        # Convert this record batch to a pandas dataframe using zero copy
        df = rb.to_pandas(split_blocks=True, zero_copy_only=True)
        # Do some further analysis...
```

### Example 17

```python
# Solve the analysis
result = route.solve()

# Export the results to a route data .zip file
out_zip = "C:/data/RouteData.zip"
result.saveRouteData(out_zip)

# Share the route data zip file as route layers to your portal
arcpy.nax.ShareAsRouteLayers(
    out_zip,
    summary='Tuesday restaurant inspection routes', 
    tags='Tuesday',
    route_name_prefix='TuesdayRestaurants', 
    portal_folder_name='RouteLayers',
    share_with='MYGROUPS',
    groups='Drivers'
)
```

### Example 18

```python
# Solve the analysis
result = route.solve()

# Export the results to a route data .zip file
out_zip = "C:/data/RouteData.zip"
result.saveRouteData(out_zip)

# Share the route data zip file as route layers to your portal
arcpy.nax.ShareAsRouteLayers(
    out_zip,
    summary='Tuesday restaurant inspection routes', 
    tags='Tuesday',
    route_name_prefix='TuesdayRestaurants', 
    portal_folder_name='RouteLayers',
    share_with='MYGROUPS',
    groups='Drivers'
)
```

### Example 19

```python
# Solve the analysis
result = route.solve()

# Save the results to a layer package for debugging purposes
out_lpkx = "C:/data/RouteAnalysis.lpkx"
result.saveAsLayerFile(out_lpkx)
```

### Example 20

```python
# Solve the analysis
result = route.solve()

# Save the results to a layer package for debugging purposes
out_lpkx = "C:/data/RouteAnalysis.lpkx"
result.saveAsLayerFile(out_lpkx)
```

---

## DistanceUnits

## Summary

Enumeration to select the desired distance units for reporting distance-based costs in the output of the analysis. Regardless of the units of the cost attributes in the network dataset, the outputs will be transformed to and reported in the units set in using this property.

---

## GetNASublayer

## Summary

Returns a Layer or Table object for the designated sublayer or subtable of the specified network analysis layer. This object can be used as input for further analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| network_analyst_layer | A network analysis layer from which you want to retrieve a sublayer, referenced as a layer object or by its layer name. | Layer |
| naclass_name | The class name for the sublayer or subtable to retrieve.The following table lists the class names for each network analysis layer type:Closest FacilityFacilities—FacilitiesIncidents—IncidentsCFRoutes—RoutesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersLocation-AllocationFacilities—FacilitiesDemandPoints—Demand PointsLALines—LinesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersOrigin Destination Cost MatrixOrigins—OriginsDestinations—DestinationsODLines—LinesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersRouteStops—StopsRoutes—RoutesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersService AreaFacilities—FacilitiesSAPolygons—PolygonsSALines—LinesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersVehicle Routing ProblemOrders—OrdersDepots—DepotsRoutes—RoutesBreaks—BreaksDepotVisits—Depot VisitsRouteZones—Route ZonesOrderPairs—Order PairsRouteRenewals—Route RenewalsOrderSpecialties—Order SpecialtiesRouteSpecialties—Route SpecialtiesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon BarriersLast Mile DeliveryOrders—OrdersDepots—DepotsRoutes—RoutesDepotVisits—Depot VisitsZones—ZonesOrderSpecialties—Order SpecialtiesRouteSpecialties—Route SpecialtiesBarriers—Point BarriersPolylineBarriers—Line BarriersPolygonBarriers—Polygon Barriers | Closest Facility |

## Code Samples

### Example 1

```python
GetNASublayer (network_analyst_layer, naclass_name)
```

### Example 2

```python
tuesday = datetime.datetime(1900, 1, 2)
layer_name = "Tuesday deliveries"
vrp_layer_object = arcpy.na.MakeVehicleRoutingProblemAnalysisLayer(
    "Streets_ND", layer_name, "Driving Time", 
    default_date=tuesday).getOutput(0)
route_specialties_table = arcpy.na.GetNASublayer(layer_name, "RouteSpecialties")
```

### Example 3

```python
tuesday = datetime.datetime(1900, 1, 2)
layer_name = "Tuesday deliveries"
vrp_layer_object = arcpy.na.MakeVehicleRoutingProblemAnalysisLayer(
    "Streets_ND", layer_name, "Driving Time", 
    default_date=tuesday).getOutput(0)
route_specialties_table = arcpy.na.GetNASublayer(layer_name, "RouteSpecialties")
```

### Example 4

```python
# Name: MakeODCostMatrixAnalysisLayer_Workflow2.py
# Description: Find the travel time to the closest hospital from each census
#               tract and join the travel time and hospital name to the input
#               tracts.
# Requirements: Network Analyst Extension

# Import system modules
import datetime
import os
import arcpy

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    # Set environment settings
    output_dir = "C:/Data"
    #The NA layer's data will be saved to the workspace specified here
    arcpy.env.workspace = os.path.join(output_dir, "Output.gdb")
    arcpy.env.overwriteOutput = True

    # Set inputs and outputs
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    origins = os.path.join(input_gdb, "Analysis", "TractCentroids")
    destinations = os.path.join(input_gdb, "Analysis", "Hospitals")
    output_features = "TractCentroids_withOD"

    # Define some OD cost matrix analysis settings
    layer_name = "HospitalsOD"
    # User settings for driving
    travel_mode = "Driving Time"
    # Calculate the total distance, even though the analysis is optimizing time
    accumulate_attributes = ["Meters"]
    # Find only the closest hospital
    num_hospitals_to_find = 1
    # Set the time of day for the analysis to 6PM on a generic Monday.
    start_time = datetime.datetime(1900, 1, 1, 18, 0, 0)
    # Don't output line shapes (output Lines will still list travel times)
    out_lines = "NO_LINES"

    # Create a new OD cost matrix layer.
    result_object = arcpy.na.MakeODCostMatrixAnalysisLayer(network, layer_name,
                    travel_mode,
                    number_of_destinations_to_find=num_hospitals_to_find,
                    time_of_day=start_time, line_shape=out_lines, 
                    accumulate_attributes=accumulate_attributes)

    # Get the layer object from the result object. The OD layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the OD layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Store the layer names for later use
    origins_layer_name = sublayer_names["Origins"]
    destinations_layer_name = sublayer_names["Destinations"]

    # The input census tract data has a unique ID field that can be transferred
    # to the analysis layer. Add the field, and then use field mapping to
    # transfer the values.
    arcpy.na.AddFieldToAnalysisLayer(layer_object, origins_layer_name,
                                                        "Tract_ID", "TEXT")
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                            origins_layer_name)
    field_mappings["Tract_ID"].mappedFieldName = "ID"

    # Load the census tracts as origins.
    arcpy.na.AddLocations(layer_object, origins_layer_name, origins,
                            field_mappings, "")

    # Map the input hospital NAME field to a new Hospital_Name field in
    # Destinations
    arcpy.na.AddFieldToAnalysisLayer(layer_object, destinations_layer_name,
                                                        "Hospital_Name", "TEXT")
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                        destinations_layer_name)
    field_mappings["Hospital_Name"].mappedFieldName = "NAME"

    # Load the hospitals as desinations.
    arcpy.na.AddLocations(layer_object, destinations_layer_name, destinations,
                            field_mappings, "")

    # Solve the OD layer
    arcpy.na.Solve(layer_object)

    # Get sublayers
    origins_sublayer = arcpy.na.GetNASublayer(layer_object, "Origins")
    destinations_sublayer = arcpy.na.GetNASublayer(layer_object, "Destinations")
    lines_sublayer = arcpy.na.GetNASublayer(layer_object, "ODLines")

    # Use the JoinField tool to transfer OD Cost Matrix information to the
    # output feature class
    # Transfer the tract ID from the input Origins to the output Lines
    arcpy.management.JoinField(lines_sublayer, "OriginID",
                                    origins_sublayer, "ObjectID", "Tract_ID")
    # Transfer the hospital name from the input Destinations to the output Lines
    arcpy.management.JoinField(lines_sublayer, "DestinationID",
                            destinations_sublayer, "ObjectID", "Hospital_Name")
    # Transfer fields of interest (hospital name, impedance attribute, and other
    # accumulated costs) from the output Lines to a copy of the input census
    # tracts feature class using the Tract_ID field
    # Determine the impedance attribute
    solver_props = arcpy.na.GetSolverProperties(layer_object)
    impedance = solver_props.impedance
    output_impedance_fieldname = "Total_" + impedance
    fields_to_transfer = ["Hospital_Name", output_impedance_fieldname]
    for field in accumulate_attributes:
        fields_to_transfer.append("Total_" + field)
    arcpy.management.CopyFeatures(origins, output_features)
    arcpy.management.JoinField(output_features, "ID",
                                lines_sublayer, "Tract_ID", fields_to_transfer)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))
```

### Example 5

```python
# Name: MakeODCostMatrixAnalysisLayer_Workflow2.py
# Description: Find the travel time to the closest hospital from each census
#               tract and join the travel time and hospital name to the input
#               tracts.
# Requirements: Network Analyst Extension

# Import system modules
import datetime
import os
import arcpy

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    # Set environment settings
    output_dir = "C:/Data"
    #The NA layer's data will be saved to the workspace specified here
    arcpy.env.workspace = os.path.join(output_dir, "Output.gdb")
    arcpy.env.overwriteOutput = True

    # Set inputs and outputs
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    origins = os.path.join(input_gdb, "Analysis", "TractCentroids")
    destinations = os.path.join(input_gdb, "Analysis", "Hospitals")
    output_features = "TractCentroids_withOD"

    # Define some OD cost matrix analysis settings
    layer_name = "HospitalsOD"
    # User settings for driving
    travel_mode = "Driving Time"
    # Calculate the total distance, even though the analysis is optimizing time
    accumulate_attributes = ["Meters"]
    # Find only the closest hospital
    num_hospitals_to_find = 1
    # Set the time of day for the analysis to 6PM on a generic Monday.
    start_time = datetime.datetime(1900, 1, 1, 18, 0, 0)
    # Don't output line shapes (output Lines will still list travel times)
    out_lines = "NO_LINES"

    # Create a new OD cost matrix layer.
    result_object = arcpy.na.MakeODCostMatrixAnalysisLayer(network, layer_name,
                    travel_mode,
                    number_of_destinations_to_find=num_hospitals_to_find,
                    time_of_day=start_time, line_shape=out_lines, 
                    accumulate_attributes=accumulate_attributes)

    # Get the layer object from the result object. The OD layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the OD layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Store the layer names for later use
    origins_layer_name = sublayer_names["Origins"]
    destinations_layer_name = sublayer_names["Destinations"]

    # The input census tract data has a unique ID field that can be transferred
    # to the analysis layer. Add the field, and then use field mapping to
    # transfer the values.
    arcpy.na.AddFieldToAnalysisLayer(layer_object, origins_layer_name,
                                                        "Tract_ID", "TEXT")
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                            origins_layer_name)
    field_mappings["Tract_ID"].mappedFieldName = "ID"

    # Load the census tracts as origins.
    arcpy.na.AddLocations(layer_object, origins_layer_name, origins,
                            field_mappings, "")

    # Map the input hospital NAME field to a new Hospital_Name field in
    # Destinations
    arcpy.na.AddFieldToAnalysisLayer(layer_object, destinations_layer_name,
                                                        "Hospital_Name", "TEXT")
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                        destinations_layer_name)
    field_mappings["Hospital_Name"].mappedFieldName = "NAME"

    # Load the hospitals as desinations.
    arcpy.na.AddLocations(layer_object, destinations_layer_name, destinations,
                            field_mappings, "")

    # Solve the OD layer
    arcpy.na.Solve(layer_object)

    # Get sublayers
    origins_sublayer = arcpy.na.GetNASublayer(layer_object, "Origins")
    destinations_sublayer = arcpy.na.GetNASublayer(layer_object, "Destinations")
    lines_sublayer = arcpy.na.GetNASublayer(layer_object, "ODLines")

    # Use the JoinField tool to transfer OD Cost Matrix information to the
    # output feature class
    # Transfer the tract ID from the input Origins to the output Lines
    arcpy.management.JoinField(lines_sublayer, "OriginID",
                                    origins_sublayer, "ObjectID", "Tract_ID")
    # Transfer the hospital name from the input Destinations to the output Lines
    arcpy.management.JoinField(lines_sublayer, "DestinationID",
                            destinations_sublayer, "ObjectID", "Hospital_Name")
    # Transfer fields of interest (hospital name, impedance attribute, and other
    # accumulated costs) from the output Lines to a copy of the input census
    # tracts feature class using the Tract_ID field
    # Determine the impedance attribute
    solver_props = arcpy.na.GetSolverProperties(layer_object)
    impedance = solver_props.impedance
    output_impedance_fieldname = "Total_" + impedance
    fields_to_transfer = ["Hospital_Name", output_impedance_fieldname]
    for field in accumulate_attributes:
        fields_to_transfer.append("Total_" + field)
    arcpy.management.CopyFeatures(origins, output_features)
    arcpy.management.JoinField(output_features, "ID",
                                lines_sublayer, "Tract_ID", fields_to_transfer)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))
```

---

## GetTravelModes

## Summary

Returns a dictionary of travel mode objects that are available with the network data source. The dictionary keys are the names of the travel modes, and the dictionary values are the travel mode objects.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| network_dataset_path | The network dataset or service from which to retrieve travel modes. The argument can be specified using one of the following options:The catalog path to the network datasetA network dataset layer objectThe string name of the network dataset layerThe URL for ArcGIS Online or an ArcGIS Enterprise portal with routing servicesA dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site | String |

## Code Samples

### Example 1

```python
GetTravelModes (network_dataset_path)
```

### Example 2

```python
import arcpy

nds = 'C:/Data/SanDiego.gdb/Transportation/Streets_ND'
travel_modes = arcpy.nax.GetTravelModes(nds)
print(travel_modes['Walking Time'])
```

### Example 3

```python
import arcpy

nds = 'C:/Data/SanDiego.gdb/Transportation/Streets_ND'
travel_modes = arcpy.nax.GetTravelModes(nds)
print(travel_modes['Walking Time'])
```

### Example 4

```python
import arcpy

travel_modes = arcpy.nax.GetTravelModes("https://www.arcgis.com/")
travel_mode_names = [travel_modes[mode].name for mode in travel_modes]
```

### Example 5

```python
import arcpy

travel_modes = arcpy.nax.GetTravelModes("https://www.arcgis.com/")
travel_mode_names = [travel_modes[mode].name for mode in travel_modes]
```

### Example 6

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 7

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 8

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.nax.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when constructing an OD cost matrix analysis
od_object = arcpy.nax.OriginDestinationCostMatrix(network)
od_object.travelMode = new_travel_mode
```

### Example 9

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.nax.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when constructing an OD cost matrix analysis
od_object = arcpy.nax.OriginDestinationCostMatrix(network)
od_object.travelMode = new_travel_mode
```

### Example 10

```python
travel_modes = arcpy.nax.GetTravelModes(
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

### Example 11

```python
travel_modes = arcpy.nax.GetTravelModes(
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

---

## GetTravelModes

## Summary

Returns a dictionary of travel mode objects that are available with the network data source. The dictionary keys are the names of the travel modes, and the dictionary values are the travel mode objects. The travel mode objects can be used to update a solver properties object (RouteSolverProperties, ClosestFacilitySolverProperties, ServiceAreaSolverProperties, ODCostMatrixSolverProperties, VehicleRoutingProblemSolverProperties, or LocationAllocationSolverProperties) before solving a particular analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| network_dataset_path | The network dataset or service from which to retrieve travel modes. The argument can be specified using one of the following options:The catalog path to the network datasetA network dataset layer objectThe string name of the network dataset layerThe URL for ArcGIS Online or an ArcGIS Enterprise portal with routing servicesA dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site | String |

## Code Samples

### Example 1

```python
GetTravelModes (network_dataset_path)
```

### Example 2

```python
import arcpy

nds = 'C:/Data/SanDiego.gdb/Transportation/Streets_ND'
travel_modes = arcpy.na.GetTravelModes(nds)
print(travel_modes['Walking Time'])
```

### Example 3

```python
import arcpy

nds = 'C:/Data/SanDiego.gdb/Transportation/Streets_ND'
travel_modes = arcpy.na.GetTravelModes(nds)
print(travel_modes['Walking Time'])
```

### Example 4

```python
import arcpy

travel_modes = arcpy.na.GetTravelModes("https://www.arcgis.com/")
travel_mode_names = [travel_modes[mode].name for mode in travel_modes]
```

### Example 5

```python
import arcpy

travel_modes = arcpy.na.GetTravelModes("https://www.arcgis.com/")
travel_mode_names = [travel_modes[mode].name for mode in travel_modes]
```

### Example 6

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 7

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 8

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when creating an OD cost matrix analysis layer
arcpy.na.MakeODCostMatrixAnalysisLayer(network, "OD Cost Matrix", new_travel_mode)
```

### Example 9

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when creating an OD cost matrix analysis layer
arcpy.na.MakeODCostMatrixAnalysisLayer(network, "OD Cost Matrix", new_travel_mode)
```

### Example 10

```python
travel_modes = arcpy.na.GetTravelModes(
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

### Example 11

```python
travel_modes = arcpy.na.GetTravelModes(
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

---

## GetWebToolInfo

## Summary

Returns the description of the network dataset used for the analysis and the run limits for a tool in the routing utility services registered with your portal or stand-alone ArcGIS Server site.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| service_name | The name of the service containing the web tool. Valid values are as follows:asyncClosestFacilityasyncFleetRoutingasyncLocationAllocationasyncODCostMatrixasyncRouteasyncServiceAreaasyncVRPsyncVRP The values are case sensitive. A ValueError occurs if the service_name value is not in the list of supported values. | String |
| tool_name | The name of the web tool. Valid values are as follows:EditVehicleRoutingProblemFindClosestFacilitiesFindRoutesGenerateOriginDestinationCostMatrixGenerateServiceAreasSolveLastMileDeliverySolveLocationAllocationSolveVehicleRoutingProblem The values are case sensitive. A ValueError occurs if the tool_name value is not in the list of supported values. | String |
| portal_url | The URL of the portal containing the service or a dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site.If no value is provided, the active portal URL will be used.(The default value is None) | String |

## Code Samples

### Example 1

```python
GetWebToolInfo (service_name, tool_name, {portal_url})
```

### Example 2

```python
# The following code sample shows how to get the maximum number of facilities supported by the Service Area utility
# service from your active portal.

import arcpy

# Get the active portal url
portal_url = arcpy.GetActivePortalURL()
print(f"Active portal: {portal_url}")

# Get the tool limits for the tool from the active portal
tool_info = arcpy.nax.GetWebToolInfo("asyncServiceArea", "GenerateServiceAreas")
max_facilities = tool_info["serviceLimits"]["maximumFacilities"]
print(f"Maximum facilities: {max_facilities}")
```

### Example 3

```python
# The following code sample shows how to get the maximum number of facilities supported by the Service Area utility
# service from your active portal.

import arcpy

# Get the active portal url
portal_url = arcpy.GetActivePortalURL()
print(f"Active portal: {portal_url}")

# Get the tool limits for the tool from the active portal
tool_info = arcpy.nax.GetWebToolInfo("asyncServiceArea", "GenerateServiceAreas")
max_facilities = tool_info["serviceLimits"]["maximumFacilities"]
print(f"Maximum facilities: {max_facilities}")
```

### Example 4

```python
# The following code sample shows how to print the traffic support type for all
# the cost attributes from the arcgis.com routing service.

import arcpy

tool_info = arcpy.nax.GetWebToolInfo(
    "asyncRoute", "FindRoutes", "https://www.arcgis.com/")
nd_info = tool_info["networkDataset"]
for attribute in nd_info["networkAttributes"]:
    if attribute["usageType"] == "Cost":
        print(f"{attribute['name']}: {attribute['trafficSupport']}")
```

### Example 5

```python
# The following code sample shows how to print the traffic support type for all
# the cost attributes from the arcgis.com routing service.

import arcpy

tool_info = arcpy.nax.GetWebToolInfo(
    "asyncRoute", "FindRoutes", "https://www.arcgis.com/")
nd_info = tool_info["networkDataset"]
for attribute in nd_info["networkAttributes"]:
    if attribute["usageType"] == "Cost":
        print(f"{attribute['name']}: {attribute['trafficSupport']}")
```

### Example 6

```python
tool_info = arcpy.nax.GetWebToolInfo(
    "asyncODCostMatrix", "GenerateOriginDestinationCostMatrix",
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

### Example 7

```python
tool_info = arcpy.nax.GetWebToolInfo(
    "asyncODCostMatrix", "GenerateOriginDestinationCostMatrix",
    {
        "utilityUrl": f"https://mysite.mydomain.com/:6443/arcgis/rest/services/MyRouting/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

---

## LastMileDelivery

## Summary

An ArcPy class for performing a last mile delivery analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_network | The network dataset or service that will be used for the network analysis. The argument can be specified using one of the following:The catalog path to the network datasetA network dataset layer objectThe string name of the network dataset layerA NetworkDataset objectThe URL for ArcGIS Online or an ArcGIS Enterprise portal with routing servicesA dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site The network must have at least one travel mode, one cost attribute with time units, and one cost attribute with distance units, as well as a time zone attribute.To use a portal URL, you must be signed in to the portal with an account that has routing privileges. When using ArcGIS Online or an ArcGIS Enterprise portal whose routing services are configured using ArcGIS Online as the in_network value, solving the analysis will consume credits and will be subject to certain limits, such as the number of allowed inputs. Learn more about credit consumption and analysis limits in network analysis | String |
| input_type | The type of input to which the fields will be added.Set this parameter using the LastMileDeliveryInputDataType enumeration. | Object |
| field_description[field_description,...] | The fields and their properties that will be added to the input class. The value will be constructed as a list of lists with each row containing the following items: Field name—The name of the field that will be added to the input class.Field type—The type of the new field. Field alias—The alternate display name for the field name.Field length—The length of the field being added. This sets the maximum number of allowable characters for each record of the field. This option is only applicable to fields of type text. The default length is 255.Default value—The default value of the field.Available field types are as follows: Field typeDescriptionTEXTThe field type will be text. Text fields support a string of characters.FLOATThe field type will be float. Float fields support fractional numbers between -3.4E38 and 1.2E38.DOUBLEThe field type will be double. Double fields support fractional numbers between -2.2E308 and 1.8E308.SHORTThe field type will be short. Short fields support whole numbers between -32,768 and 32,767.LONGThe field type will be long. Long fields support whole numbers between -2,147,483,648 and 2,147,483,647.DATEThe field type will be date. Date fields support date and time values. GUIDThe field type will be GUID. GUID fields store registry-style strings consisting of 36 characters enclosed in curly brackets.BIGINTEGERThe field type will be big integer. Big integer fields support whole numbers between -(253) and 253.TIMEONLYThe field type will be time only. Time only fields support time values with no date values.DATEONLYThe field type will be date only. Date only fields support date values with no time values.TIMESTAMPOFFSETThe field type will be timestamp offset. Timestamp offset fields support a date, time, and offset from a UTC value. Only the field name and type are required. Use None as a place holder for any of the other parameters to accept the default or if the parameter does not apply to the specified field type.The method will return an error if the field already exists in the table or if any of the field properties are invalid.Legacy:The GUID, BIGINTEGER, TIMEONLY, DATEONLY, and TIMESTAMPOFFSET field types are not supported when the network data source is a portal running ArcGIS Enterprise 11.1.x or earlier. | TEXT |
| input_type | The type of input features to count. Set this parameter using the LastMileDeliveryInputDataType enumeration. | Object |
| input_type | The type of input for which the field mappings will be returned.Set this parameter using the LastMileDeliveryInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Specifies whether network location fields will be included in the returned field mappings dictionary. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned field mappings dictionary will include network location fields. The default is False, which means the field mapping dictionary will not include network location fields.(The default value is False) | Boolean |
| list_candidate_fields[list_candidate_fields,...] | Use this parameter to map additional, nondefault fields from the input data to the analysis inputs. For example, if the input feature class contains a field named MyField, and you want it to be included in the analysis inputs, pass the MyField field object to the list_candidate_fields parameter. MyField will be included in the returned field mapping dictionary and automatically mapped. When you call the load method using these field mappings, MyField will be included in the analysis inputs along with all the default fields. In many cases, these extra fields will be passed to the analysis output as well.Specify this parameter as a list of arcpy.Field objects, which can be obtained from a specified feature class or table using the arcpy.ListFields function.Learn more about best practices for setting up analysis inputsLegacy:If the network data source is an ArcGIS Enterprise portal, the method will return an error if any of the fields specified are of a type that is not supported by the portal version.(The default value is None) | Field |
| input_type | The type of input for which the supported field names are returned.Set this parameter using the LastMileDeliveryInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Indicates whether network location fields will be included in the returned list of field names. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how your analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned list of field names will contain network location fields. The default is False; the list of field names will not include network location fields.(The default value is False) | Boolean |
| input_type | The type of input into which the cursor can be used to insert rows. Set this parameter using the LastMileDeliveryInputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the input type whose values you want to set when inserting rows using the cursor. You can get the names of the fields supported by an input type using the fieldNames method.See descriptions of the fields available for each input typeIn addition to regular fields, you can also set the geometry of the input using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid x,y coordinates.SHAPE@XYZ—A tuple of the feature's centroid x,y,z coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based input types. When using the SHAPE@XY and SHAPE@XYZ tokens, specify the x-, y-, and z-values in the spatial reference of the network data source being used in the analysis. | String |
| append | Specifies whether the features being inserted will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended; the existing features will be preserved. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features being inserted.(The default value is True) | Boolean |
| input_type | The type of input feature that will be loaded.Set this parameter using the LastMileDeliveryInputDataType enumeration. | Object |
| features | The input features that will be loaded. This parameter accepts the following input types:The catalog path to a feature class or a tableA Layer objectThe string representing the name of a layerA FeatureSet or RecordSet objectFor layer inputs, only selected features will be loaded. If a layer has a definition query, only the subset of features visible with the definition query will be loaded. The method also honors the Extent geoprocessing environment; only features in the specified extent will be loaded. | String |
| field_mappings | An NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects representing the mapping of fields from the input features. Valid input for this parameter can be constructed using the fieldMappings method.If no field mappings are specified, all fields from the input features that have the same name as the supported fields for the input type will be mapped.See descriptions of the fields available for each input type(The default value is None) | Dictionary |
| append | Specifies whether the features being loaded will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended, and existing features will be preserved. This is useful when loading inputs from multiple feature classes or tables to use in a single analysis. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features currently being loaded.(The default value is True) | Boolean |
| max_features | The maximum number of features that can be loaded into the input type. This is useful if you are creating a tool or service and want an error returned if the size of the input exceeds the available resources. The load method will return an arcpy.nax.LimitError if the number of input features exceeds the max_features limit.If no value is provided, no limit will be enforced for the count of the input features.(The default value is None) | Integer |
| input_type | The type of input for which to override default locate settings.Set this parameter using the LastMileDeliveryInputDataType enumeration. | Object |
| search_sources[[Source, Expression],...] | The list of network sources to be used when locating inputs of the designated type on the network, and, optionally, a query to restrict the search to a subset of the features within a source feature class.See the documentation for the searchSources property for examples of proper syntax for this parameter.Specifying a value for this parameter overrides the default searchSources property value for the designated input type.If this parameter is not specified or is set to None, the searchSources value will be used for this input type.The method returns an error if this parameter is used and the network data source is ArcGIS Online. | String |
| allow_auto_relocate | Specifies whether inputs of the designated type with existing network location fields can be automatically relocated at solve time to ensure valid, routable location fields for the analysis. If the value is True, points located on restricted network elements and points affected by barriers will be relocated to the closest routable location. If the value is False, network location fields will be used as is, even if the points are unreachable, and this may cause the solve to fail. Even if the value is False, inputs with no location fields or incomplete location fields will be located at solve time.Specifying a value for this parameter overrides the default allowAutoRelocate property value for the designated input type.If this parameter is not specified or is set to None, the allowAutoRelocate value will be used for this input type.The method returns an error if the network data source is ArcGIS Online.The method returns an error if the network data source is an ArcGIS Enterprise portal that does not support using network location fields. | Boolean |
| search_tolerance | The maximum search distance to use when locating inputs of the designated type on the network.Specifying a value for this parameter overrides the default searchTolerance property value for the designated input type.If this parameter is not specified or is set to None, the searchTolerance value will be used for this input type.The units of this parameter value are set using the search_tolerance_units parameter; however, if no value is set for that parameter, the search_tolerance value will be interpreted in the units specified in the searchToleranceUnits property.This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |
| search_tolerance_units | The units of the maximum search distance when locating inputs of the designated type of the network. The parameter is specified using a member of the DistanceUnits enumeration.Specifying a value for this parameter overrides the default searchToleranceUnits property value for the designated input type.If this parameter is not specified or is set to None, the searchToleranceUnits will be used for this input type.The value specified using the search_tolerance parameter is interpreted using these units. If that parameter is not specified, the value of the searchTolerance property will be interpreted using these units for the designated input type only. This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |

## Methods

### addFields (input_type, field_description)

Adds custom fields to the designated input class. These fields will be included in the field mapping dictionary created by the fieldMappings method and will also be available for use with the insertCursor method.Learn more about using custom fields in analysis inputs

### count (input_type)

Returns the number of rows added for an input type.

### fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})

Generates an NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects that allow you to map fields from the input data to the properties of the solver. The dictionary can be used as input to the field_mappings argument of the load method.Learn more about how to use field mappings when loading inputs

### fieldNames (input_type, {use_location_fields})

Get a list of field names supported by the specified input type.

### insertCursor (input_type, field_names, {append})

Establishes a write cursor on the specified input type. This cursor can be used to add rows directly to the input.Learn more about how to insert inputs

### load (input_type, features, {field_mappings}, {append}, {max_features})

Sets input features to use for the analysis.Learn more about how to load inputs

### setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})

Set locate settings for a designated input class, overriding the default locate settings specified for the analysis. This is useful if you want to use different rules to locate different inputs. For example, in an OD cost matrix analysis, you can use a search query that applies to the input origins only, if that query should not apply to the input destinations and barriers.Using this method, you can override the values of the searchSources, allowAutoRelocate, searchTolerance, and searchToleranceUnits properties for the designated input class.Learn more about locating inputs on the network

### solve ()

Perform the last mile delivery analysis using the properties set on the LastMileDelivery object and the loaded inputs.

## Code Samples

### Example 1

```python
LastMileDelivery (in_network)
```

### Example 2

```python
addFields (input_type, field_description)
```

### Example 3

```python
count (input_type)
```

### Example 4

```python
fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})
```

### Example 5

```python
fieldNames (input_type, {use_location_fields})
```

### Example 6

```python
insertCursor (input_type, field_names, {append})
```

### Example 7

```python
load (input_type, features, {field_mappings}, {append}, {max_features})
```

### Example 8

```python
setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})
```

### Example 9

```python
# An example showing how to perform last mile delivery analysis using inputs
# from feature classes and tables.
import datetime
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_orders = "C:/data/io.gdb/Orders"
input_depots = "C:/data/io.gdb/Depots"
input_routes = "C:/data/io.gdb/Vehicles"
output_orders = "C:/data/io.gdb/OutputOrders"
output_routes = "C:/data/io.gdb/OutputRoutes"
output_direction_points = "C:/data/io.gdb/OutputDirectionPoints"
output_direction_lines = "C:/data/io.gdb/OutputDirectionLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a LastMileDelivery solver object
last_mile = arcpy.nax.LastMileDelivery(nd_layer_name)
# Set properties
last_mile.travelMode = travel_mode
last_mile.earliestRouteStartDate = datetime.date(2024, 6, 3)
last_mile.earliestRouteStartTime = datetime.time(8, 0, 0)
last_mile.timeUnits = arcpy.nax.TimeUnits.Hours
last_mile.maxRouteTotalTime = 8  # hours
last_mile.returnDirections = True
# Load inputs
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Orders, input_orders)
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Depots, input_depots)
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Routes, input_routes)
# Solve the analysis
result = last_mile.solve()

# Export the results to feature classes
if result.solveSucceeded:
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.Orders, output_orders)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.Routes, output_routes)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.DirectionPoints, output_direction_points)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.DirectionLines, output_direction_lines)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 10

```python
# An example showing how to perform last mile delivery analysis using inputs
# from feature classes and tables.
import datetime
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_orders = "C:/data/io.gdb/Orders"
input_depots = "C:/data/io.gdb/Depots"
input_routes = "C:/data/io.gdb/Vehicles"
output_orders = "C:/data/io.gdb/OutputOrders"
output_routes = "C:/data/io.gdb/OutputRoutes"
output_direction_points = "C:/data/io.gdb/OutputDirectionPoints"
output_direction_lines = "C:/data/io.gdb/OutputDirectionLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a LastMileDelivery solver object
last_mile = arcpy.nax.LastMileDelivery(nd_layer_name)
# Set properties
last_mile.travelMode = travel_mode
last_mile.earliestRouteStartDate = datetime.date(2024, 6, 3)
last_mile.earliestRouteStartTime = datetime.time(8, 0, 0)
last_mile.timeUnits = arcpy.nax.TimeUnits.Hours
last_mile.maxRouteTotalTime = 8  # hours
last_mile.returnDirections = True
# Load inputs
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Orders, input_orders)
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Depots, input_depots)
last_mile.load(arcpy.nax.LastMileDeliveryInputDataType.Routes, input_routes)
# Solve the analysis
result = last_mile.solve()

# Export the results to feature classes
if result.solveSucceeded:
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.Orders, output_orders)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.Routes, output_routes)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.DirectionPoints, output_direction_points)
    result.export(arcpy.nax.LastMileDeliveryOutputDataType.DirectionLines, output_direction_lines)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## MessageSeverity

## Summary

Enumeration for the severity level of solver messages to retrieve using the solverMessages method of each solver object.

---

## NAClassFieldMap

## Summary

Provides the ability to map field names or set default values for the properties of a network analysis input class. The properties of the network analysis class are used as inputs by the solvers while performing the network analyses.

## Code Samples

### Example 1

```python
# An example showing how to perform origin destination cost matrix analysis using inputs from feature classes.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"
output_lines = "C:/data/io.gdb/ODCostMatrixLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Pre-calculate network location fields on the inputs to speed up analysis later
search_tolerance = "5000 Meters"
search_criteria = [["Streets", "SHAPE"], ["Streets_ND_Junctions", "NONE"]]
arcpy.nax.CalculateLocations(input_origins, nds, search_tolerance, search_criteria, travel_mode=travel_mode)
arcpy.nax.CalculateLocations(input_destinations, nds, search_tolerance, search_criteria, travel_mode=travel_mode)

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine

# Load inputs using field mappings, including the pre-calculated location fields
field_mappings_origins = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, True)
# Map the "Nombre" field in the input data to the "Name" property of the Origins class
field_mappings_origins["Name"].mappedFieldName = "Nombre"
# If the "Nombre" field is blank, set the default name to "Origen"
field_mappings_origins["Name"].defaultValue = "Origen"
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins, field_mappings_origins)
# Load destinations
field_mappings_destinations = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, True)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations, field_mappings_destinations)

# Solve the analysis
result = odcm.solve()
# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, output_lines)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 2

```python
# An example showing how to perform origin destination cost matrix analysis using inputs from feature classes.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"
output_lines = "C:/data/io.gdb/ODCostMatrixLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Pre-calculate network location fields on the inputs to speed up analysis later
search_tolerance = "5000 Meters"
search_criteria = [["Streets", "SHAPE"], ["Streets_ND_Junctions", "NONE"]]
arcpy.nax.CalculateLocations(input_origins, nds, search_tolerance, search_criteria, travel_mode=travel_mode)
arcpy.nax.CalculateLocations(input_destinations, nds, search_tolerance, search_criteria, travel_mode=travel_mode)

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine

# Load inputs using field mappings, including the pre-calculated location fields
field_mappings_origins = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, True)
# Map the "Nombre" field in the input data to the "Name" property of the Origins class
field_mappings_origins["Name"].mappedFieldName = "Nombre"
# If the "Nombre" field is blank, set the default name to "Origen"
field_mappings_origins["Name"].defaultValue = "Origen"
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins, field_mappings_origins)
# Load destinations
field_mappings_destinations = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, True)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations, field_mappings_destinations)

# Solve the analysis
result = odcm.solve()
# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, output_lines)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## NAClassFieldMappings

## Summary

Provides a dictionary of NAClassFieldMap objects that are used to map field names or set default values for the properties of a network analysis input class. The dictionary keys are the network analysis class property names, and the values are the NAClassFieldMap objects.

## Code Samples

### Example 1

```python
# An example showing how to perform origin destination cost matrix analysis using inputs from feature classes.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"
output_lines = "C:/data/io.gdb/ODCostMatrixLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Pre-calculate network location fields on the inputs to speed up analysis later
search_tolerance = "5000 Meters"
search_criteria = [["Streets", "SHAPE"], ["Streets_ND_Junctions", "NONE"]]
arcpy.nax.CalculateLocations(input_origins, nds, search_tolerance, search_criteria, travel_mode=travel_mode)
arcpy.nax.CalculateLocations(input_destinations, nds, search_tolerance, search_criteria, travel_mode=travel_mode)

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine

# Load inputs using field mappings, including the pre-calculated location fields
field_mappings_origins = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, True)
# Map the "Nombre" field in the input data to the "Name" property of the Origins class
field_mappings_origins["Name"].mappedFieldName = "Nombre"
# If the "Nombre" field is blank, set the default name to "Origen"
field_mappings_origins["Name"].defaultValue = "Origen"
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins, field_mappings_origins)
# Load destinations
field_mappings_destinations = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, True)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations, field_mappings_destinations)

# Solve the analysis
result = odcm.solve()
# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, output_lines)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 2

```python
# An example showing how to perform origin destination cost matrix analysis using inputs from feature classes.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"
output_lines = "C:/data/io.gdb/ODCostMatrixLines"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.na.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.na.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Pre-calculate network location fields on the inputs to speed up analysis later
search_tolerance = "5000 Meters"
search_criteria = [["Streets", "SHAPE"], ["Streets_ND_Junctions", "NONE"]]
arcpy.nax.CalculateLocations(input_origins, nds, search_tolerance, search_criteria, travel_mode=travel_mode)
arcpy.nax.CalculateLocations(input_destinations, nds, search_tolerance, search_criteria, travel_mode=travel_mode)

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine

# Load inputs using field mappings, including the pre-calculated location fields
field_mappings_origins = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, True)
# Map the "Nombre" field in the input data to the "Name" property of the Origins class
field_mappings_origins["Name"].mappedFieldName = "Nombre"
# If the "Nombre" field is blank, set the default name to "Origen"
field_mappings_origins["Name"].defaultValue = "Origen"
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins, field_mappings_origins)
# Load destinations
field_mappings_destinations = odcm.fieldMappings(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, True)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations, field_mappings_destinations)

# Solve the analysis
result = odcm.solve()
# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, output_lines)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## NetworkDataset

## Summary

Provides access to the properties of a network dataset. You can use this class to retrieve the properties and attribute values for network dataset edges, junctions, and turns, as well as other properties of the network dataset.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_network | The network dataset whose properties you want to retrieve. The argument can be specified using the catalog path to the network dataset, a network dataset layer object, or the string name of the network dataset layer. | String |
| feature_layer | A Layer object containing the features that intersect the network edge sources. Any selection set or definition query present on the layer object is honored and can be used to specify only a subset of features. | Layer |
| cutoff | The maximum number of intersecting features. | Integer |
| edge_properties[edge_properties,...] | A list of strings representing the network edge properties to retrieve. For a single property, you can use a string instead of a list of strings. The available properties include the following: EID—The ID of the edge.SOURCEID— The ID of the source feature class of the edge.SOURCEOID— The ObjectID of the feature within the source feature class from which this network edge is derived.FROMPOSITION— The distance along the source feature where this network edge starts. A network edge can represent a partial feature in the source feature class.TOPOSITION— The distance along the source feature where this network edge ends.DIRECTION— A Boolean value indicating whether the edge's direction is along the direction of digitization of the source feature. A value of True means that the edge's direction is along the direction of digitization, and a value of False means that the edge's direction is against the direction of digitization.FROMJUNCTION— The EID of the junction feature at the beginning of the edge.TOJUNCTION— The EID of the junction feature at the end of the edge.ISRESTRICTED—A Boolean value indicating whether the edge is restricted for the specified travel mode.COST—The cost to traverse the edge for the specified travel mode.TIME—The time cost to traverse the edge for the specified travel mode.DISTANCE—The distance cost incurred by traversing the edge for the specified travel mode.To request the ISRESTRICTED, COST, TIME, and DISTANCE properties, you must specify a value for the travel_mode parameter. | String |
| attribute_names[attribute_names,...] | The list of network dataset attribute names, such as costs or restrictions, for which to retrieve the value for each network element. If the value is time dependent, you can specify the time of day using the time_of_day parameter. For a single attribute, you can use a string instead of a list of strings. | String |
| time_of_day | The time of day for which to retrieve time-dependent attribute values for this network element. When no time of day value is passed, the time-neutral value will be returned. | DateTime |
| eids[eids,...] | A list of EID values to include in the cursor. This allows you to return only a subset of all network elements. If no value is passed for this parameter, all network elements are returned.The eids and area_of_interest parameters cannot be used simultaneously. | Integer |
| travel_mode | The travel mode to apply when requesting edge properties and attribute values. The travel mode settings may impact the returned property and attribute values, particularly if the travel mode uses nondefault values for any attribute parameters.When no travel mode is specified, all values requested from attribute_names use their default attribute parameter values, and the ISRESTRICTED, COST, TIME, and DISTANCE properties are not available.The travel mode should be specified as a TravelMode object. You can use one of the network's travel modes obtained using the NetworkDataset object's travelModes property or use a custom TravelMode object. | Object |
| area_of_interest | The spatial filter to apply when requesting edge properties and attribute values. This allows you to return only the subset of edges that intersect the specified area of interest.The parameter should be specified as an Extent object or a Polygon object. If an Extent object is used, all edges intersecting the rectangular extent are returned. If a Polygon object is used, all edges intersecting the polygon's shape are returned. The Polygon option can be used to filter edges by country or state boundaries, for example. If a 3D polygon is used, all edges intersecting the 2D projection of the polygon are returned. The eids and area_of_interest parameters cannot be used simultaneously. | Object |
| source_id | The network source ID for which the corresponding source feature class's catalog path will be retrieved. | Integer |
| junction_properties[junction_properties,...] | A list of strings representing the network junction properties to retrieve. For a single property, you can use a string instead of a list of strings. The available properties include the following: EID—The ID of the junction.SOURCEID— The ID of the source feature class of the junction.SOURCEOID— The ObjectID of the feature within the source feature class from which this network junction is derived.ISRESTRICTED—A Boolean value indicating whether the junction is restricted for the specified travel mode.COST—The cost to traverse the junction for the specified travel mode.TIME—The time cost to traverse the junction for the specified travel mode.DISTANCE—The distance cost incurred by traversing the junction for the specified travel mode.To request the ISRESTRICTED, COST, TIME, and DISTANCE properties, you must specify a value for the travel_mode parameter. | String |
| attribute_names[attribute_names,...] | The list of network dataset attribute names, such as costs or restrictions, for which the value of each network element will be retrieved. If the value is time dependent, you can specify the time of day using the time_of_day parameter. For a single attribute, you can use a string instead of a list of strings. | String |
| time_of_day | The time of day that time-dependent attribute values for this network element will be retrieved. When no time of day value is passed, the time-neutral value will be returned. | DateTime |
| eids[eids,...] | A list of EID values to include in the cursor. This allows you to return only a subset of all network elements. If no value is passed for this parameter, all network elements are returned.The eids and area_of_interest parameters cannot be used simultaneously. | Integer |
| travel_mode | The travel mode to apply when requesting junction properties and attribute values. The travel mode settings may impact the returned property and attribute values, particularly if the travel mode uses nondefault values for any attribute parameters.When no travel mode is specified, all values requested from attribute_names use their default attribute parameter values, and the ISRESTRICTED, COST, TIME, and DISTANCE properties are not available.The travel mode should be specified as a TravelMode object. You can use one of the network's travel modes obtained using the NetworkDataset object's travelModes property or use a custom TravelMode object. | Object |
| area_of_interest | The spatial filter to apply when requesting junction properties and attribute values. This allows you to return only the subset of junctions that intersect the specified area of interest.The parameter should be specified as an Extent object or a Polygon object. If an Extent object is used, all junctions intersecting the rectangular extent are returned. If a Polygon object is used, all junctions intersecting the polygon's shape are returned. The Polygon option can be used to filter junctions by country or state boundaries, for example. If a 3D polygon is used, all junctions intersecting the 2D projection of the polygon are returned. The eids and area_of_interest parameters cannot be used simultaneously. | Object |
| turn_properties[turn_properties,...] | A list of strings representing the network turn properties to retrieve. For a single property, you can use a string instead of a list of strings. The available properties include the following: EID—The ID of the turn.SOURCEID— The ID of the source feature class of the turn.SOURCEOID— The ObjectID of the feature within the source feature class from which this network turn is derived.EDGEEIDS— An ordered list of EID values of network edges that participate in this turn.ISRESTRICTED—A Boolean value indicating whether the turn is restricted for the specified travel mode.COST—The cost to traverse the turn for the specified travel mode.TIME—The time cost to traverse the turn for the specified travel mode.DISTANCE—The distance cost incurred by traversing the turn for the specified travel mode.To request the ISRESTRICTED, COST, TIME, and DISTANCE properties, you must specify a value for the travel_mode parameter. | String |
| attribute_names[attribute_names,...] | The list of network dataset attribute names, such as costs or restrictions, for which to retrieve the value for each network element. For a single attribute, you can use a string instead of a list of strings. | String |
| eids[eids,...] | A list of EID values to include in the cursor. This allows you to return only a subset of all network elements. If no value is passed for this parameter, all network elements are returned.The eids and area_of_interest parameters cannot be used simultaneously. | Integer |
| travel_mode | The travel mode to apply when requesting turn properties and attribute values. The travel mode settings may impact the returned property and attribute values, particularly if the travel mode uses nondefault values for any attribute parameters.When no travel mode is specified, all values requested from attribute_names use their default attribute parameter values, and the ISRESTRICTED, COST, TIME, and DISTANCE properties are not available.The travel mode should be specified as a TravelMode object. You can use one of the network's travel modes obtained using the NetworkDataset object's travelModes property or use a custom TravelMode object. | Object |
| area_of_interest | The spatial filter to apply when requesting turn properties and attribute values. This allows you to return only the subset of turns that intersect the specified area of interest.The parameter should be specified as an Extent object or a Polygon object. If an Extent object is used, all turns intersecting the rectangular extent are returned. If a Polygon object is used, all turns intersecting the polygon's shape are returned. The Polygon option can be used to filter turns by country or state boundaries, for example. If a 3D polygon is used, all turns intersecting the 2D projection of the polygon are returned. The eids and area_of_interest parameters cannot be used simultaneously. | Object |
| custom_evaluators | A dictionary that describes the custom evaluators that will be associated with the network dataset.Learn more about custom evaluatorsThe dictionary keys are the network attribute names that the custom evaluator will be applied to. The values are a dictionary with a class key and an optional sourceNames key. The class key value describes how to import the custom evaluator class from the active ArcGIS Pro Python environment's site-packages directory using a dot notation to specify the package, module, and class. The sourceNames key value is a list of network source names specifying the sources the custom evaluator applies to. If this key is not included in the dictionary, the custom evaluator will apply to all sources.This code snippet shows a dictionary with the correct structure to update the network dataset's Minutes attribute with a custom evaluator whose code is defined in a class named CostCustomizer in a Python file named custom_eval.py in a folder Python na_customization in the Python environment's site-packages directory.ce_description = { "Minutes": { "class": "na_customization.custom_eval.CostCustomizer", "sourceNames": ["Streets"] } } nd.updateNetworkDatasetSchema(custom_evaluators=ce_description)Only include a given network attribute in the dictionary once. You can only associate one custom evaluator with a given attribute.To remove a reference to existing custom evaluators from the network dataset schema, use a value of None when calling this method.nd.updateNetworkDatasetSchema(custom_evaluators=None)Caution:Positional arguments are not supported with this method. To associate a custom evaluator with the network, you must use the named argument custom_evaluators when calling this method. | Dictionary |
| custom_directions | A dictionary that describes the directions customization classes that will be associated with the network dataset.Learn more about custom directionsThe dictionary must have a key named class. The value describes how to import the custom evaluator class from the active ArcGIS Pro Python environment's site-packages directory using a dot notation to specify the package, module, and class.This code snippet shows a dictionary with the correct structure to update the network dataset schema with a custom directions class named DirectionsCustomizer in a Python file named custom_directions.py in a folder named na_customization in the Python environment's site-packages directory.cd_description = {"class": "na_customization.custom_directions.DirectionsCustomizer"} nd.updateNetworkDatasetSchema(custom_directions=cd_description)To remove a reference to existing custom directions classes from the network dataset schema, use a value of None when calling this method.nd.updateNetworkDatasetSchema(custom_directions=None)Caution:Positional arguments are not supported with this method. To associate a custom directions class with the network, you must use the named argument custom_directions when calling this method. | Dictionary |

## Methods

### checkIntersectingFeatures (feature_layer, cutoff)

Returns a Boolean value indicating whether the number of edge source features from the specified network dataset that are intersected by the features within the specified feature layer is less than or equal to the specified cutoff. This is useful for restricting the number of features that can be loaded as line or polygon barriers into a network analysis problem.This method is similar to the CheckIntersectingFeatures function.

### describe ()

Returns a Describe object that contains additional properties of the network dataset. This is equivalent to using arcpy.Describe on the network dataset.

### edges ({edge_properties}, {attribute_names}, {time_of_day}, {eids}, {travel_mode}, {area_of_interest})

Returns an iterator of network dataset edge elements you can use to access the value of specific edge properties and network attributes at the time of day specified.

### getDataSourceFromSourceID (source_id)

Returns the catalog path of the network dataset source feature class identified by the given source ID.Tip:This method is effectively instantaneous because it reads a cached value. Your code can call this method repeatedly with minimal performance impact.

### junctions ({junction_properties}, {attribute_names}, {time_of_day}, {eids}, {travel_mode}, {area_of_interest})

Returns an iterator of network dataset junction elements that you can use to access the value of specific junction properties and network attributes at the time of day specified.

### turns ({turn_properties}, {attribute_names}, {eids}, {travel_mode}, {area_of_interest})

Returns an iterator of network dataset turn elements you can use to access the value of specific turn properties and network attributes.

### updateNetworkDatasetSchema ({custom_evaluators}, {custom_directions})

Updates the network dataset to associate a custom evaluator or directions Python class with the network.

## Code Samples

### Example 1

```python
NetworkDataset (in_network)
```

### Example 2

```python
checkIntersectingFeatures (feature_layer, cutoff)
```

### Example 3

```python
describe ()
```

### Example 4

```python
edges ({edge_properties}, {attribute_names}, {time_of_day}, {eids}, {travel_mode}, {area_of_interest})
```

### Example 5

```python
getDataSourceFromSourceID (source_id)
```

### Example 6

```python
junctions ({junction_properties}, {attribute_names}, {time_of_day}, {eids}, {travel_mode}, {area_of_interest})
```

### Example 7

```python
turns ({turn_properties}, {attribute_names}, {eids}, {travel_mode}, {area_of_interest})
```

### Example 8

```python
updateNetworkDatasetSchema ({custom_evaluators}, {custom_directions})
```

### Example 9

```python
ce_description = {
    "Minutes": {
        "class": "na_customization.custom_eval.CostCustomizer",
        "sourceNames": ["Streets"]
    }
}
nd.updateNetworkDatasetSchema(custom_evaluators=ce_description)
```

### Example 10

```python
ce_description = {
    "Minutes": {
        "class": "na_customization.custom_eval.CostCustomizer",
        "sourceNames": ["Streets"]
    }
}
nd.updateNetworkDatasetSchema(custom_evaluators=ce_description)
```

### Example 11

```python
nd.updateNetworkDatasetSchema(custom_evaluators=None)
```

### Example 12

```python
nd.updateNetworkDatasetSchema(custom_evaluators=None)
```

### Example 13

```python
cd_description = {"class": "na_customization.custom_directions.DirectionsCustomizer"}
nd.updateNetworkDatasetSchema(custom_directions=cd_description)
```

### Example 14

```python
cd_description = {"class": "na_customization.custom_directions.DirectionsCustomizer"}
nd.updateNetworkDatasetSchema(custom_directions=cd_description)
```

### Example 15

```python
nd.updateNetworkDatasetSchema(custom_directions=None)
```

### Example 16

```python
nd.updateNetworkDatasetSchema(custom_directions=None)
```

### Example 17

```python
# Print the travel time for each edge in the network that is not restricted to automobiles
import datetime
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Print network dataset build information
print(f"Network dataset is built: {nds.isBuilt}")
print(f"Most recent build time: {nds.buildTimestamp}")

# Iterate through all the edges in the network and get the TravelTime cost attribute
# value for a specific time of day. Only print the value if the edge is not restricted
# to automobiles
edges = nds.edges("EID", ["TravelTime", "Driving an Automobile"], datetime.datetime(2019, 4, 19, 8, 0, 0))
for edge in edges:
    if not edge[2]:
        print(f"TravelTime for EID {edge[0]}: {edge[1]}")
```

### Example 18

```python
# Print the travel time for each edge in the network that is not restricted to automobiles
import datetime
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Print network dataset build information
print(f"Network dataset is built: {nds.isBuilt}")
print(f"Most recent build time: {nds.buildTimestamp}")

# Iterate through all the edges in the network and get the TravelTime cost attribute
# value for a specific time of day. Only print the value if the edge is not restricted
# to automobiles
edges = nds.edges("EID", ["TravelTime", "Driving an Automobile"], datetime.datetime(2019, 4, 19, 8, 0, 0))
for edge in edges:
    if not edge[2]:
        print(f"TravelTime for EID {edge[0]}: {edge[1]}")
```

### Example 19

```python
# Retrieve the ObjectIDs of all junctions for all edges that participate in turns
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through all turns in the network and get the edges that participate
turns = nds.turns(["SOURCEOID", "EDGEEIDS"])
for turn in turns:
    # For the edges in the turn, get the from and to junctions
    edges = nds.edges(["SOURCEOID", "FROMJUNCTION", "TOJUNCTION"], eids=turn[1])
    for edge in edges:
        # For the from and to junction, get the SOURCEOID
        junctions = nds.junctions("SOURCEOID", eids=[edge[1], edge[2]])
        junctionOIDs = [j[0] for j in junctions]
```

### Example 20

```python
# Retrieve the ObjectIDs of all junctions for all edges that participate in turns
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through all turns in the network and get the edges that participate
turns = nds.turns(["SOURCEOID", "EDGEEIDS"])
for turn in turns:
    # For the edges in the turn, get the from and to junctions
    edges = nds.edges(["SOURCEOID", "FROMJUNCTION", "TOJUNCTION"], eids=turn[1])
    for edge in edges:
        # For the from and to junction, get the SOURCEOID
        junctions = nds.junctions("SOURCEOID", eids=[edge[1], edge[2]])
        junctionOIDs = [j[0] for j in junctions]
```

### Example 21

```python
# Retrieve the cost and restricted status for all network edges for the Walking Time travel mode
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through all the edges in the network and print the cost to traverse it with the Walking Time travel mode and
# whether or not the edge is restricted.
for edge in nds.edges(["EID", "COST", "ISRESTRICTED"], travel_mode=nds.travelModes["Walking Time"]):
    print(f"EID {edge[0]} -- COST: {edge[1]}; RESTRICTED: {edge[2]}")
```

### Example 22

```python
# Retrieve the cost and restricted status for all network edges for the Walking Time travel mode
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through all the edges in the network and print the cost to traverse it with the Walking Time travel mode and
# whether or not the edge is restricted.
for edge in nds.edges(["EID", "COST", "ISRESTRICTED"], travel_mode=nds.travelModes["Walking Time"]):
    print(f"EID {edge[0]} -- COST: {edge[1]}; RESTRICTED: {edge[2]}")
```

### Example 23

```python
# Retrieve the ObjectID values for junctions within a specified extent
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"
extent_fc = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Analysis\AnalysisExtent"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Get the extent from the feature class
extent = arcpy.Describe(extent_fc).extent

# Retrieve the junctions that fall within the designated extent
for junction in nds.junctions(["SOURCEOID"], area_of_interest=extent):
    print(junction)
```

### Example 24

```python
# Retrieve the ObjectID values for junctions within a specified extent
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"
extent_fc = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Analysis\AnalysisExtent"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Get the extent from the feature class
extent = arcpy.Describe(extent_fc).extent

# Retrieve the junctions that fall within the designated extent
for junction in nds.junctions(["SOURCEOID"], area_of_interest=extent):
    print(junction)
```

### Example 25

```python
# Retrieve the ObjectID values for junctions within specified territories
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"
territories = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Analysis\Territories"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through the polygons in the Territories feature class and retrieve
# the junctions that fall within each territory's boundary.
for row in arcpy.da.SearchCursor(territories, ["Name", "SHAPE@"]):
    print(f"Junctions in territory {row[0]}:")
    for junction in nds.junctions(["SOURCEOID"], area_of_interest=row[1]):
        print(junction[0])
```

### Example 26

```python
# Retrieve the ObjectID values for junctions within specified territories
import arcpy
arcpy.CheckOutExtension("network")

nds_path = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Transportation\Streets_ND"
territories = r"E:\TutorialData\Network Analyst\Tutorial\SanDiego.gdb\Analysis\Territories"

# Initialize the NetworkDataset object
nds = arcpy.nax.NetworkDataset(nds_path)

# Iterate through the polygons in the Territories feature class and retrieve
# the junctions that fall within each territory's boundary.
for row in arcpy.da.SearchCursor(territories, ["Name", "SHAPE@"]):
    print(f"Junctions in territory {row[0]}:")
    for junction in nds.junctions(["SOURCEOID"], area_of_interest=row[1]):
        print(junction[0])
```

---

## OriginDestinationCostMatrixResult

## Summary

An object containing the results of an origin destination cost matrix analysis that can be used to access outputs and solver messages.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| output_type | The type of output features to count.Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration. | Object |
| output_type | The type of output to export. Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| output_features | The catalog path to the output feature class or table that will contain the exported features. | String |
| output_type | The type of output features for which to get the extent.Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration.If you do not specify a value, or you specify a value of None, the extent for the combined analysis outputs is returned. | Object |
| output_type | The type of output for which to return a list of field names.Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| file_name | The catalog path of the output layer file (.lyr) or layer package (.lpkx) to write.Caution:Layer files with an .lyr extension cannot be saved if the solver object uses a service URL as its network data source. The method returns a RuntimeError exception in this case. | String |
| output_type | The type of output that will be read. Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the output type whose values will be returned by the cursor. You can get the names of the fields that are supported by an output type using the fieldNames method.See descriptions of the fields included in each output typeIn addition to regular fields, you can also access the geometry of the output using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid's x- and y-coordinates.SHAPE@XYZ—A tuple of the feature's centroid's x-, y-, and z-coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based output types. The x-, y-, and z-values returned when using the SHAPE@XY and SHAPE@XYZ tokens are in the spatial reference reported by the solver result object's spatialReference property, and this is typically the same as the spatial reference of the network data source used for the analysis.Tip:Retrieving geometry for the Lines output type can be slow. For best performance, do not request geometry using any of the geometry tokens. | String |
| where_clause | An optional expression that limits the records returned. For more information on WHERE clauses and SQL statements, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| severity | The type of messages to be returned.The parameter should be specified using the MessageSeverity enumeration. | Object |
| output_type | The type of output that will be read. Set this parameter using the OriginDestinationCostMatrixOutputDataType enumeration.Caution:Only the Lines output type is currently supported. The method returns a RuntimeError exception if a different output type is specified. | Object |
| field_names[field_names,...] | A list of field names of the output type to include in the Arrow table.See descriptions of the fields included in each output typeCaution:For the Lines output type, the Shape, OriginName, and DestinationName fields are not supported. | String |
| file_name | The file path to use to save the analysis results permanently. The file will contain one or more Arrow record batches and can be opened in any package or library that supports the Arrow format.This parameter is optional. If it is not specified, the Arrow table returned by the method can be used within the current Python operation but will not be stored permanently. | String |
| max_batch_size | The maximum number of records to include in a single record batch in the output Arrow table. When no value or None is specified, a value of 2,147,483,647 is used. If the total number of records is smaller than the specified max_batch_size, the output Arrow table and file will contain only one record batch.For very large analyses, writing the output in batches prevents out-of-memory errors. The method always returns a single Arrow table and output file (if the file_name parameter is specified), but the presence of multiple record batches in the output may influence how you handle it in subsequent code. When an Arrow table or file containing multiple record batches is converted to another format, such as a Pandas DataFrame, you may not be able to do a zero-copy read of the entire table or file. In a zero-copy read, the data can be accessed without additional serialization overhead to load it in RAM. To achieve this zero-copy read behavior, your code may need to handle one record batch at a time.For the Lines output type, for most applications, it is important to keep all records associated with the same origin together in the same batch. This ensures that you can do a zero-copy read of all records for that origin for post-processing or further analysis. If the number of records associated with a given origin exceeds the specified max_batch_size, the method will override the max_batch_size value, and the resulting record batches will increase to the minimum size needed to store all records associated with the origin. The value for max_batch_size cannot exceed 2,147,483,647. | Integer |

## Methods

### count (output_type)

Returns the number of rows for an output type.

### export (output_type, output_features)

Exports the analysis results to a feature class or table.The output features will be created in the spatial reference of the network dataset used for the analysis. If the arcpy.env.outputCoordinateSystem environment is set, the output features will be created with the specified coordinate system instead.

### extent ({output_type})

Returns the extent of the analysis output.The method returns a RuntimeError exception if the analysis solve failed.

### fieldNames (output_type)

Returns a list of field names supported by a specified output type.

### saveAsLayerFile (file_name)

Save the analysis result and settings to a layer file or layer package. The layer file or package can be opened in ArcGIS Pro as a record of the analysis settings or to visualize the results. A layer file can also be opened in ArcGIS Desktop.The method returns a RuntimeError exception if the allowSaveLayerFile property on the solver object is set to False.Legacy:Routing services based on portals running versions of ArcGIS Enterprise older than 10.9 do not support saving layer packages. The method returns a RuntimeError exception if this is the case.

### searchCursor (output_type, field_names, {where_clause})

Establishes a search cursor on the specified output type. This cursor can be used to read rows directly from the output.

### solverMessages (severity)

Get error, warning, and informational messages returned by the solver.

### toArrowTable (output_type, field_names, {file_name}, {max_batch_size})

Returns the OD Cost Matrix result in Apache Arrow format.Note:Arrow output is not available if the solver object uses a service URL as its network data source. The method returns a RuntimeError exception in this case.

## Code Samples

### Example 1

```python
count (output_type)
```

### Example 2

```python
export (output_type, output_features)
```

### Example 3

```python
extent ({output_type})
```

### Example 4

```python
fieldNames (output_type)
```

### Example 5

```python
saveAsLayerFile (file_name)
```

### Example 6

```python
searchCursor (output_type, field_names, {where_clause})
```

### Example 7

```python
solverMessages (severity)
```

### Example 8

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

### Example 9

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

### Example 10

```python
toArrowTable (output_type, field_names, {file_name}, {max_batch_size})
```

---

## Network analysis

## Code Samples

### Example 1

```python
import arcpy
nd_path = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "NorthAmerica"

# Create a network dataset layer. The layer will be referenced using its name.
arcpy.nax.MakeNetworkDatasetLayer(nd_path, nd_layer_name)

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea(nd_layer_name)
```

### Example 2

```python
import arcpy
nd_path = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "NorthAmerica"

# Create a network dataset layer. The layer will be referenced using its name.
arcpy.nax.MakeNetworkDatasetLayer(nd_path, nd_layer_name)

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea(nd_layer_name)
```

### Example 3

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea("https://www.arcgis.com/")
```

### Example 4

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea("https://www.arcgis.com/")
```

### Example 5

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea("https://myportal.mysite.com/portal/")
```

### Example 6

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea("https://myportal.mysite.com/portal/")
```

### Example 7

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea(
    {
        "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
        "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

### Example 8

```python
import arcpy

# Instantiate a ServiceArea analysis object.
service_area = arcpy.nax.ServiceArea(
    {
        "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
        "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
        "authenticationInfo": {
            "username": "my_username",
            "password": "my_password"
        }
    }
)
```

### Example 9

```python
# Get the desired travel mode for the analysis.
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Set properties.
service_area.timeUnits = arcpy.nax.TimeUnits.Minutes
service_area.defaultImpedanceCutoffs = [5, 10, 15]
service_area.travelMode = travel_mode
service_area.outputType = arcpy.nax.ServiceAreaOutputType.Polygons
service_area.geometryAtOverlap = arcpy.nax.ServiceAreaOverlapGeometry.Split
```

### Example 10

```python
# Get the desired travel mode for the analysis.
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Set properties.
service_area.timeUnits = arcpy.nax.TimeUnits.Minutes
service_area.defaultImpedanceCutoffs = [5, 10, 15]
service_area.travelMode = travel_mode
service_area.outputType = arcpy.nax.ServiceAreaOutputType.Polygons
service_area.geometryAtOverlap = arcpy.nax.ServiceAreaOverlapGeometry.Split
```

### Example 11

```python
# Check out the Network Analyst extension license.
arcpy.CheckOutExtension("network")

# Solve the analysis.
result = service_area.solve()
```

### Example 12

```python
# Check out the Network Analyst extension license.
arcpy.CheckOutExtension("network")

# Solve the analysis.
result = service_area.solve()
```

### Example 13

```python
# Solve the analysis.
result = service_area.solve()

# Export the results to a feature class. If the analysis failed, print all the 
# messages.
if result.solveSucceeded:
    result.export(arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
else:
    arcpy.AddError("Analysis failed")
    # Print all the warning messages.
    for message in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
        arcpy.AddWarning(message[-1])
    # Print all the error messages.
    for message in result.solverMessages(arcpy.nax.MessageSeverity.Error):
        arcpy.AddError(message[-1])
```

### Example 14

```python
# Solve the analysis.
result = service_area.solve()

# Export the results to a feature class. If the analysis failed, print all the 
# messages.
if result.solveSucceeded:
    result.export(arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
else:
    arcpy.AddError("Analysis failed")
    # Print all the warning messages.
    for message in result.solverMessages(arcpy.nax.MessageSeverity.Warning):
        arcpy.AddWarning(message[-1])
    # Print all the error messages.
    for message in result.solverMessages(arcpy.nax.MessageSeverity.Error):
        arcpy.AddError(message[-1])
```

---

## Route

## Summary

An ArcPy class for performing a route analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_network | The network dataset or service that will be used for the network analysis. The argument can be specified using one of the following:The catalog path to the network datasetA network dataset layer objectThe string name of the network dataset layerA NetworkDataset objectThe URL for ArcGIS Online or an ArcGIS Enterprise portal with routing servicesA dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site To use a network dataset, the network must have at least one travel mode.To use a portal URL, you must be signed in to the portal with an account that has routing privileges. Learn how to sign in to a portal in Python When using ArcGIS Online or an ArcGIS Enterprise portal whose routing services are configured using ArcGIS Online as the in_network value, solving the analysis will consume credits and will be subject to certain limits, such as the number of allowed inputs. Learn more about credit consumption and analysis limits in network analysis | String |
| input_type | The type of input to which the fields will be added.Set this parameter using the RouteInputDataType enumeration. | Object |
| field_description[field_description,...] | The fields and their properties that will be added to the input class. The value will be constructed as a list of lists with each row containing the following items: Field name—The name of the field that will be added to the input class.Field type—The type of the new field. Field alias—The alternate display name for the field name.Field length—The length of the field being added. This sets the maximum number of allowable characters for each record of the field. This option is only applicable to fields of type text. The default length is 255.Default value—The default value of the field.Available field types are as follows: Field typeDescriptionTEXTThe field type will be text. Text fields support a string of characters.FLOATThe field type will be float. Float fields support fractional numbers between -3.4E38 and 1.2E38.DOUBLEThe field type will be double. Double fields support fractional numbers between -2.2E308 and 1.8E308.SHORTThe field type will be short. Short fields support whole numbers between -32,768 and 32,767.LONGThe field type will be long. Long fields support whole numbers between -2,147,483,648 and 2,147,483,647.DATEThe field type will be date. Date fields support date and time values. GUIDThe field type will be GUID. GUID fields store registry-style strings consisting of 36 characters enclosed in curly brackets.BIGINTEGERThe field type will be big integer. Big integer fields support whole numbers between -(253) and 253.TIMEONLYThe field type will be time only. Time only fields support time values with no date values.DATEONLYThe field type will be date only. Date only fields support date values with no time values.TIMESTAMPOFFSETThe field type will be timestamp offset. Timestamp offset fields support a date, time, and offset from a UTC value. Only the field name and type are required. Use None as a place holder for any of the other parameters to accept the default or if the parameter does not apply to the specified field type.The method will return an error if the field already exists in the table or if any of the field properties are invalid.Legacy:The GUID, BIGINTEGER, TIMEONLY, DATEONLY, and TIMESTAMPOFFSET field types are not supported when the network data source is a portal running ArcGIS Enterprise 11.1.x or earlier. | TEXT |
| input_type | The type of input features to count.Set this parameter using the RouteInputDataType enumeration. | Object |
| input_type | The type of input for which the field mappings will be returned.Set this parameter using the RouteInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Specifies whether network location fields will be included in the returned field mappings dictionary. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned field mappings dictionary will include network location fields. The default is False, which means the field mapping dictionary will not include network location fields.(The default value is False) | Boolean |
| list_candidate_fields[list_candidate_fields,...] | Use this parameter to map additional, nondefault fields from the input data to the analysis inputs. For example, if the input feature class contains a field named MyField, and you want it to be included in the analysis inputs, pass the MyField field object to the list_candidate_fields parameter. MyField will be included in the returned field mapping dictionary and automatically mapped. When you call the load method using these field mappings, MyField will be included in the analysis inputs along with all the default fields. In many cases, these extra fields will be passed to the analysis output as well.Specify this parameter as a list of arcpy.Field objects, which can be obtained from a specified feature class or table using the arcpy.ListFields function.Learn more about best practices for setting up analysis inputsLegacy:If the network data source is an ArcGIS Enterprise portal, the method will return an error if any of the fields specified are of a type that is not supported by the portal version.(The default value is None) | Field |
| input_type | The type of input for which the supported field names are returned.Set this parameter using the RouteInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Indicates whether network location fields will be included in the returned list of field names. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how your analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned list of field names will contain network location fields. The default is False; the list of field names will not include network location fields.(The default value is False) | Boolean |
| input_type | The type of input into which the cursor can be used to insert rows. Set this parameter using the RouteInputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the input type whose values you want to set when inserting rows using the cursor. You can get the names of the fields supported by an input type using the fieldNames method.See descriptions of the fields available for each input typeIn addition to regular fields, you can also set the geometry of the input using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid x,y coordinates.SHAPE@XYZ—A tuple of the feature's centroid x,y,z coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based input types. When using the SHAPE@XY and SHAPE@XYZ tokens, specify the x-, y-, and z-values in the spatial reference of the network data source being used in the analysis. | String |
| append | Specifies whether the features being inserted will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended; the existing features will be preserved. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features being inserted.(The default value is True) | Boolean |
| input_type | The type of input feature that will be loaded.Set this parameter using the RouteInputDataType enumeration. | Object |
| features | The input features that will be loaded. This parameter accepts the following input types:The catalog path to a feature class or a tableA Layer objectThe string representing the name of a layerA FeatureSet or RecordSet objectFor layer inputs, only selected features will be loaded. If a layer has a definition query, only the subset of features visible with the definition query will be loaded. The method also honors the Extent geoprocessing environment; only features in the specified extent will be loaded. | String |
| field_mappings | An NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects representing the mapping of fields from the input features. Valid input for this parameter can be constructed using the fieldMappings method.If no field mappings are specified, all fields from the input features that have the same name as the supported fields for the input type will be mapped.See descriptions of the fields available for each input type(The default value is None) | Dictionary |
| append | Specifies whether the features being loaded will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended, and existing features will be preserved. This is useful when loading inputs from multiple feature classes or tables to use in a single analysis. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features currently being loaded.(The default value is True) | Boolean |
| max_features | The maximum number of features that can be loaded into the input type. This is useful if you are creating a tool or service and want an error returned if the size of the input exceeds the available resources. The load method will return an arcpy.nax.LimitError if the number of input features exceeds the max_features limit.If no value is provided, no limit will be enforced for the count of the input features.(The default value is None) | Integer |
| input_type | The type of input for which to override default locate settings.Set this parameter using the RouteInputDataType enumeration. | Object |
| search_sources[[Source, Expression],...] | The list of network sources to be used when locating inputs of the designated type on the network, and, optionally, a query to restrict the search to a subset of the features within a source feature class.See the documentation for the searchSources property for examples of proper syntax for this parameter.Specifying a value for this parameter overrides the default searchSources property value for the designated input type.If this parameter is not specified or is set to None, the searchSources value will be used for this input type.The method returns an error if this parameter is used and the network data source is ArcGIS Online. | String |
| allow_auto_relocate | Specifies whether inputs of the designated type with existing network location fields can be automatically relocated at solve time to ensure valid, routable location fields for the analysis. If the value is True, points located on restricted network elements and points affected by barriers will be relocated to the closest routable location. If the value is False, network location fields will be used as is, even if the points are unreachable, and this may cause the solve to fail. Even if the value is False, inputs with no location fields or incomplete location fields will be located at solve time.Specifying a value for this parameter overrides the default allowAutoRelocate property value for the designated input type.If this parameter is not specified or is set to None, the allowAutoRelocate value will be used for this input type.The method returns an error if the network data source is ArcGIS Online.The method returns an error if the network data source is an ArcGIS Enterprise portal that does not support using network location fields. | Boolean |
| search_tolerance | The maximum search distance to use when locating inputs of the designated type on the network.Specifying a value for this parameter overrides the default searchTolerance property value for the designated input type.If this parameter is not specified or is set to None, the searchTolerance value will be used for this input type.The units of this parameter value are set using the search_tolerance_units parameter; however, if no value is set for that parameter, the search_tolerance value will be interpreted in the units specified in the searchToleranceUnits property.This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |
| search_tolerance_units | The units of the maximum search distance when locating inputs of the designated type of the network. The parameter is specified using a member of the DistanceUnits enumeration.Specifying a value for this parameter overrides the default searchToleranceUnits property value for the designated input type.If this parameter is not specified or is set to None, the searchToleranceUnits will be used for this input type.The value specified using the search_tolerance parameter is interpreted using these units. If that parameter is not specified, the value of the searchTolerance property will be interpreted using these units for the designated input type only. This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |

## Methods

### addFields (input_type, field_description)

Adds custom fields to the designated input class. These fields will be included in the field mapping dictionary created by the fieldMappings method and will also be available for use with the insertCursor method.Learn more about using custom fields in analysis inputs

### count (input_type)

Returns the number of rows added for an input type.

### fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})

Generates an NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects that allow you to map fields from the input data to the properties of the solver. The dictionary can be used as input to the field_mappings argument of the load method. Learn more about how to use field mappings when loading inputs

### fieldNames (input_type, {use_location_fields})

Get a list of field names supported by the specified input type.

### insertCursor (input_type, field_names, {append})

Establishes a write cursor on the specified input type. This cursor can be used to add rows directly to the input.Learn more about how to insert inputs

### load (input_type, features, {field_mappings}, {append}, {max_features})

Sets input features to use for the analysis. Learn more about how to load inputs

### setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})

Set locate settings for a designated input class, overriding the default locate settings specified for the analysis. This is useful if you want to use different rules to locate different inputs. For example, in an OD cost matrix analysis, you can use a search query that applies to the input origins only, if that query should not apply to the input destinations and barriers.Using this method, you can override the values of the searchSources, allowAutoRelocate, searchTolerance, and searchToleranceUnits properties for the designated input class.Learn more about locating inputs on the network

### solve ()

Perform the route analysis using the properties set on the Route object and the loaded inputs.

## Code Samples

### Example 1

```python
Route (in_network)
```

### Example 2

```python
addFields (input_type, field_description)
```

### Example 3

```python
count (input_type)
```

### Example 4

```python
fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})
```

### Example 5

```python
fieldNames (input_type, {use_location_fields})
```

### Example 6

```python
insertCursor (input_type, field_names, {append})
```

### Example 7

```python
load (input_type, features, {field_mappings}, {append}, {max_features})
```

### Example 8

```python
setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})
```

### Example 9

```python
# An example showing how to perform route analysis using a feature class for input stops.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_stops = "C:/data/io.gdb/Stops"
output_routes = "C:/data/io.gdb/Routes"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a Route solver object
route = arcpy.nax.Route(nd_layer_name)
# Set properties
route.timeUnits = arcpy.nax.TimeUnits.Minutes
route.travelMode = travel_mode
route.routeShapeType = arcpy.nax.RouteShapeType.TrueShapeWithMeasures
# Load inputs
route.load(arcpy.nax.RouteInputDataType.Stops, input_stops)
# Solve the analysis
result = route.solve()

# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.RouteOutputDataType.Routes, output_routes)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 10

```python
# An example showing how to perform route analysis using a feature class for input stops.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_stops = "C:/data/io.gdb/Stops"
output_routes = "C:/data/io.gdb/Routes"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a Route solver object
route = arcpy.nax.Route(nd_layer_name)
# Set properties
route.timeUnits = arcpy.nax.TimeUnits.Minutes
route.travelMode = travel_mode
route.routeShapeType = arcpy.nax.RouteShapeType.TrueShapeWithMeasures
# Load inputs
route.load(arcpy.nax.RouteInputDataType.Stops, input_stops)
# Solve the analysis
result = route.solve()

# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.RouteOutputDataType.Routes, output_routes)
else:
    print("Solved failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## RouteResult

## Summary

An object containing the results of a route analysis that can be used to access outputs and solver messages.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| output_type | The type of output features to count.Set this parameter using the RouteOutputDataType enumeration. | Object |
| output_type | The type of output to export. Set this parameter using the RouteOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| output_features | The catalog path to the output feature class or table that will contain the exported features. | String |
| output_type | The type of output features for which to get the extent.Set this parameter using the RouteOutputDataType enumeration.If you do not specify a value, or you specify a value of None, the extent for the combined analysis outputs is returned. | Object |
| output_type | The type of output for which to return a list of field names.Set this parameter using the RouteOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| file_name | The catalog path of the output layer file (.lyr) or layer package (.lpkx) to write.Caution:Layer files with an .lyr extension cannot be saved if the solver object uses a service URL as its network data source. The method returns a RuntimeError exception in this case. | String |
| file_name | The full path of the output .zip file. | String |
| output_type | The type of output that will be read. Set this parameter using the RouteOutputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the output type whose values will be returned by the cursor. You can get the names of the fields that are supported by an output type using the fieldNames method.See descriptions of the fields included in each output typeIn addition to regular fields, you can also access the geometry of the output using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid's x- and y-coordinates.SHAPE@XYZ—A tuple of the feature's centroid's x-, y-, and z-coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based output types. The x-, y-, and z-values returned when using the SHAPE@XY and SHAPE@XYZ tokens are in the spatial reference reported by the solver result object's spatialReference property, and this is typically the same as the spatial reference of the network data source used for the analysis. | String |
| where_clause | An optional expression that limits the records returned. For more information on WHERE clauses and SQL statements, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| severity | The type of messages to be returned.The parameter should be specified using the MessageSeverity enumeration. | Object |

## Methods

### count (output_type)

Returns the number of rows for an output type.

### export (output_type, output_features)

Exports the analysis results to a feature class or table.The output features will be created in the spatial reference of the network dataset used for the analysis. If the arcpy.env.outputCoordinateSystem environment is set, the output features will be created with the specified coordinate system instead.

### extent ({output_type})

Returns the extent of the analysis output.The method returns a RuntimeError exception if the analysis solve failed.

### fieldNames (output_type)

Returns a list of field names supported by a specified output type.

### saveAsLayerFile (file_name)

Save the analysis result and settings to a layer file or layer package. The layer file or package can be opened in ArcGIS Pro as a record of the analysis settings or to visualize the results. A layer file can also be opened in ArcGIS Desktop.The method returns a RuntimeError exception if the allowSaveLayerFile property on the solver object is set to False.Legacy:Routing services based on portals running versions of ArcGIS Enterprise older than 10.9 do not support saving layer packages. The method returns a RuntimeError exception if this is the case.

### saveRouteData (file_name)

Save the outputs from the analysis to a .zip file. The .zip file can be used to share the routes from the analysis as route layer items in ArcGIS Online or ArcGIS Enterprise using the Share As Route Layers tool.A route layer item can be used by various applications, such as ArcGIS Navigator to provide route guidance for mobile workers, the Directions pane in Map Viewer Classic to further customize the route contained in the route layer, and ArcGIS Pro to create a route analysis layer from a route layer. The output features will be created in the spatial reference of the network dataset used for analysis. If the arcpy.env.outputCoordinateSystem environment has been set, the output will be created in that spatial reference instead.If the solve fails, saveRouteData returns a RuntimeError exception.The method returns a RuntimeError exception if the allowSaveRouteData property on the solver object is set to False.

### searchCursor (output_type, field_names, {where_clause})

Establishes a search cursor on the specified output type. This cursor can be used to read rows directly from the output.

### solverMessages (severity)

Get error, warning, and informational messages returned by the solver.

## Code Samples

### Example 1

```python
count (output_type)
```

### Example 2

```python
export (output_type, output_features)
```

### Example 3

```python
extent ({output_type})
```

### Example 4

```python
fieldNames (output_type)
```

### Example 5

```python
saveAsLayerFile (file_name)
```

### Example 6

```python
saveRouteData (file_name)
```

### Example 7

```python
searchCursor (output_type, field_names, {where_clause})
```

### Example 8

```python
solverMessages (severity)
```

### Example 9

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

### Example 10

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

---

## RouteSolverProperties

## Summary

Provides access to analysis properties from a route network analysis layer. The GetSolverProperties function is used to obtain a RouteSolverProperties object from a route network analysis layer.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| travel_mode | A variable that references a travel mode object derived from a network dataset. A list of travel mode objects can be obtained by calling the arcpy.na.GetTravelModes function. | Object |

## Methods

### applyTravelMode (travel_mode)

Updates the analysis properties of a network analyst layer based on a travel mode object. The updated network analyst layer can then be solved to complete the analysis.

## Code Samples

### Example 1

```python
solverProps.attributeParameters[('HeightRestriction', 'RestrictionUsage')] = "PROHIBITED"
```

### Example 2

```python
solverProps.attributeParameters[('HeightRestriction', 'RestrictionUsage')] = "PROHIBITED"
```

### Example 3

```python
params = solverProps.attributeParameters
params[('HeightRestriction', 'RestrictionUsage')] = "PROHIBITED"
solverProps.attributeParameters = params
```

### Example 4

```python
params = solverProps.attributeParameters
params[('HeightRestriction', 'RestrictionUsage')] = "PROHIBITED"
solverProps.attributeParameters = params
```

### Example 5

```python
applyTravelMode (travel_mode)
```

### Example 6

```python
# Name: RouteSolverProperties_workflow_01.py
# Description: Find the fastest route at two different times of day. The travel
#              time is different because of traffic conditions. Use the
#              RouteSolverProperties object to update an existing Route layer
#              before re-running the analysis.
# Requirements: Network Analyst Extension

# Import system modules
import arcpy
from arcpy import env
import os

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")

    # Set environment settings
    output_dir = "C:/Data"
    # The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    # Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    stops = os.path.join(input_gdb, "Analysis", "Stores")
    route_0830 = os.path.join(output_dir, "Output.gdb", "Route_MorningRush")
    route_1100 = os.path.join(output_dir, "Output.gdb", "Route_MidMorning")

    # Make a new route layer using travel time as impedance to determine fastest
    # route
    route_layer = arcpy.na.MakeRouteAnalysisLayer(network, "StoresRoute",
                                         "Driving Time",
                                         time_of_day="8:30 AM").getOutput(0)

    # Get the network analysis class names from the route layer
    na_classes = arcpy.na.GetNAClassNames(route_layer)

    # Load stops
    arcpy.na.AddLocations(route_layer, na_classes["Stops"], stops)

    # Solve the route layer
    arcpy.na.Solve(route_layer)

    # Get the routes sublayer from the route layer
    routes_sublayer = arcpy.na.GetNASublayer(route_layer, "Routes")

    # Save the resulting route as a feature class. This route was solved at 8:30
    # AM, morning rush hour.
    arcpy.management.CopyFeatures(routes_sublayer, route_0830)

    # Get the RouteSolverProperties object from the route layer to modify the
    # timeOfDay property of the route layer.
    solver_props = arcpy.na.GetSolverProperties(route_layer)

    # Set the impedance property to "Meters" to determine the shortest route.
    solver_props.timeOfDay = "11:00 AM"

    # Re-solve the route layer
    arcpy.na.Solve(route_layer)

    # Save the resulting route as a feature class. This route was solved at 11:00
    # AM, mid-morning when traffic is probably lighter.
    arcpy.management.CopyFeatures(routes_sublayer, route_1100)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occured on line %i" % tb.tb_lineno)
    print(str(e))
```

### Example 7

```python
# Name: RouteSolverProperties_workflow_01.py
# Description: Find the fastest route at two different times of day. The travel
#              time is different because of traffic conditions. Use the
#              RouteSolverProperties object to update an existing Route layer
#              before re-running the analysis.
# Requirements: Network Analyst Extension

# Import system modules
import arcpy
from arcpy import env
import os

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")

    # Set environment settings
    output_dir = "C:/Data"
    # The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    # Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    stops = os.path.join(input_gdb, "Analysis", "Stores")
    route_0830 = os.path.join(output_dir, "Output.gdb", "Route_MorningRush")
    route_1100 = os.path.join(output_dir, "Output.gdb", "Route_MidMorning")

    # Make a new route layer using travel time as impedance to determine fastest
    # route
    route_layer = arcpy.na.MakeRouteAnalysisLayer(network, "StoresRoute",
                                         "Driving Time",
                                         time_of_day="8:30 AM").getOutput(0)

    # Get the network analysis class names from the route layer
    na_classes = arcpy.na.GetNAClassNames(route_layer)

    # Load stops
    arcpy.na.AddLocations(route_layer, na_classes["Stops"], stops)

    # Solve the route layer
    arcpy.na.Solve(route_layer)

    # Get the routes sublayer from the route layer
    routes_sublayer = arcpy.na.GetNASublayer(route_layer, "Routes")

    # Save the resulting route as a feature class. This route was solved at 8:30
    # AM, morning rush hour.
    arcpy.management.CopyFeatures(routes_sublayer, route_0830)

    # Get the RouteSolverProperties object from the route layer to modify the
    # timeOfDay property of the route layer.
    solver_props = arcpy.na.GetSolverProperties(route_layer)

    # Set the impedance property to "Meters" to determine the shortest route.
    solver_props.timeOfDay = "11:00 AM"

    # Re-solve the route layer
    arcpy.na.Solve(route_layer)

    # Save the resulting route as a feature class. This route was solved at 11:00
    # AM, mid-morning when traffic is probably lighter.
    arcpy.management.CopyFeatures(routes_sublayer, route_1100)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occured on line %i" % tb.tb_lineno)
    print(str(e))
```

### Example 8

```python
#Get the route layer object from a layer named "Route" in the map
doc = arcpy.mp.ArcGISProject('current')
map_obj = doc.listMaps()[0]
route_layer = map_obj.listLayers('Route')[0]

#Get the Trucking Time travel mode from the network dataset
desc = arcpy.Describe(route_layer)
travel_modes = arcpy.na.GetTravelModes(desc.network.catalogPath)
trucking_mode = travel_modes["Trucking Time"]

#Apply the travel mode to the analysis layer
solver_properties = arcpy.na.GetSolverProperties(route_layer)
solver_properties.applyTravelMode(trucking_mode)
```

### Example 9

```python
#Get the route layer object from a layer named "Route" in the map
doc = arcpy.mp.ArcGISProject('current')
map_obj = doc.listMaps()[0]
route_layer = map_obj.listLayers('Route')[0]

#Get the Trucking Time travel mode from the network dataset
desc = arcpy.Describe(route_layer)
travel_modes = arcpy.na.GetTravelModes(desc.network.catalogPath)
trucking_mode = travel_modes["Trucking Time"]

#Apply the travel mode to the analysis layer
solver_properties = arcpy.na.GetSolverProperties(route_layer)
solver_properties.applyTravelMode(trucking_mode)
```

---

## ServiceArea

## Summary

An ArcPy class for performing a service area analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_network | The network dataset or service that will be used for the network analysis. The argument can be specified using one of the following:The catalog path to the network datasetA network dataset layer objectThe string name of the network dataset layerA NetworkDataset objectThe URL for ArcGIS Online or an ArcGIS Enterprise portal with routing servicesA dictionary specifying connection information for a routing service on a stand-alone ArcGIS Server site To use a network dataset, the network must have at least one travel mode.To use a portal URL, you must be signed in to the portal with an account that has routing privileges. Learn how to sign in to a portal in Python When using ArcGIS Online or an ArcGIS Enterprise portal whose routing services are configured using ArcGIS Online as the in_network value, solving the analysis will consume credits and will be subject to certain limits, such as the number of allowed inputs. Learn more about credit consumption and analysis limits in network analysis | String |
| input_type | The type of input to which the fields will be added.Set this parameter using the ServiceAreaInputDataType enumeration. | Object |
| field_description[field_description,...] | The fields and their properties that will be added to the input class. The value will be constructed as a list of lists with each row containing the following items: Field name—The name of the field that will be added to the input class.Field type—The type of the new field. Field alias—The alternate display name for the field name.Field length—The length of the field being added. This sets the maximum number of allowable characters for each record of the field. This option is only applicable to fields of type text. The default length is 255.Default value—The default value of the field.Available field types are as follows: Field typeDescriptionTEXTThe field type will be text. Text fields support a string of characters.FLOATThe field type will be float. Float fields support fractional numbers between -3.4E38 and 1.2E38.DOUBLEThe field type will be double. Double fields support fractional numbers between -2.2E308 and 1.8E308.SHORTThe field type will be short. Short fields support whole numbers between -32,768 and 32,767.LONGThe field type will be long. Long fields support whole numbers between -2,147,483,648 and 2,147,483,647.DATEThe field type will be date. Date fields support date and time values. GUIDThe field type will be GUID. GUID fields store registry-style strings consisting of 36 characters enclosed in curly brackets.BIGINTEGERThe field type will be big integer. Big integer fields support whole numbers between -(253) and 253.TIMEONLYThe field type will be time only. Time only fields support time values with no date values.DATEONLYThe field type will be date only. Date only fields support date values with no time values.TIMESTAMPOFFSETThe field type will be timestamp offset. Timestamp offset fields support a date, time, and offset from a UTC value. Only the field name and type are required. Use None as a place holder for any of the other parameters to accept the default or if the parameter does not apply to the specified field type.The method will return an error if the field already exists in the table or if any of the field properties are invalid.Legacy:The GUID, BIGINTEGER, TIMEONLY, DATEONLY, and TIMESTAMPOFFSET field types are not supported when the network data source is a portal running ArcGIS Enterprise 11.1.x or earlier. | TEXT |
| input_type | The type of input features to count.Set this parameter using the ServiceAreaInputDataType enumeration. | Object |
| input_type | The type of input for which the field mappings will be returned.Set this parameter using the ServiceAreaInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Specifies whether network location fields will be included in the returned field mappings dictionary. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned field mappings dictionary will include network location fields. The default is False, which means the field mapping dictionary will not include network location fields.(The default value is False) | Boolean |
| list_candidate_fields[list_candidate_fields,...] | Use this parameter to map additional, nondefault fields from the input data to the analysis inputs. For example, if the input feature class contains a field named MyField, and you want it to be included in the analysis inputs, pass the MyField field object to the list_candidate_fields parameter. MyField will be included in the returned field mapping dictionary and automatically mapped. When you call the load method using these field mappings, MyField will be included in the analysis inputs along with all the default fields. In many cases, these extra fields will be passed to the analysis output as well.Specify this parameter as a list of arcpy.Field objects, which can be obtained from a specified feature class or table using the arcpy.ListFields function.Learn more about best practices for setting up analysis inputsLegacy:If the network data source is an ArcGIS Enterprise portal, the method will return an error if any of the fields specified are of a type that is not supported by the portal version.(The default value is None) | Field |
| input_type | The type of input for which the supported field names are returned.Set this parameter using the ServiceAreaInputDataType enumeration.See descriptions of the fields available for each input type | Object |
| use_location_fields | Indicates whether network location fields will be included in the returned list of field names. Network location fields describe the point on the network where an object is located. You can use network location fields to more precisely control how your analysis inputs locate on the network and to save time when calling the solve method because the solver will not have to calculate the location fields from the geometry of the inputs. You can calculate location fields for a feature class using the Calculate Locations tool. Learn more about network location fields and how inputs are located on the networkWhen this argument is set to True, the returned list of field names will contain network location fields. The default is False; the list of field names will not include network location fields.(The default value is False) | Boolean |
| input_type | The type of input into which the cursor can be used to insert rows. Set this parameter using the ServiceAreaInputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the input type whose values you want to set when inserting rows using the cursor. You can get the names of the fields supported by an input type using the fieldNames method.See descriptions of the fields available for each input typeIn addition to regular fields, you can also set the geometry of the input using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid x,y coordinates.SHAPE@XYZ—A tuple of the feature's centroid x,y,z coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based input types. When using the SHAPE@XY and SHAPE@XYZ tokens, specify the x-, y-, and z-values in the spatial reference of the network data source being used in the analysis. | String |
| append | Specifies whether the features being inserted will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended; the existing features will be preserved. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features being inserted.(The default value is True) | Boolean |
| input_type | The type of input feature that will be loaded.Set this parameter using the ServiceAreaInputDataType enumeration. | Object |
| features | The input features that will be loaded. This parameter accepts the following input types:The catalog path to a feature class or a tableA Layer objectThe string representing the name of a layerA FeatureSet or RecordSet objectFor layer inputs, only selected features will be loaded. If a layer has a definition query, only the subset of features visible with the definition query will be loaded. The method also honors the Extent geoprocessing environment; only features in the specified extent will be loaded. | String |
| field_mappings | An NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects representing the mapping of fields from the input features. Valid input for this parameter can be constructed using the fieldMappings method.If no field mappings are specified, all fields from the input features that have the same name as the supported fields for the input type will be mapped.See descriptions of the fields available for each input type(The default value is None) | Dictionary |
| append | Specifies whether the features being loaded will be appended to the existing set of features for the input type. A value of True indicates that the new features will be appended, and existing features will be preserved. This is useful when loading inputs from multiple feature classes or tables to use in a single analysis. This is the default. A value of False indicates that any existing features for the input type will be deleted and replaced with the features currently being loaded.(The default value is True) | Boolean |
| max_features | The maximum number of features that can be loaded into the input type. This is useful if you are creating a tool or service and want an error returned if the size of the input exceeds the available resources. The load method will return an arcpy.nax.LimitError if the number of input features exceeds the max_features limit.If no value is provided, no limit will be enforced for the count of the input features.(The default value is None) | Integer |
| input_type | The type of input for which to override default locate settings.Set this parameter using the ServiceAreaInputDataType enumeration. | Object |
| search_sources[[Source, Expression],...] | The list of network sources to be used when locating inputs of the designated type on the network, and, optionally, a query to restrict the search to a subset of the features within a source feature class.See the documentation for the searchSources property for examples of proper syntax for this parameter.Specifying a value for this parameter overrides the default searchSources property value for the designated input type.If this parameter is not specified or is set to None, the searchSources value will be used for this input type.The method returns an error if this parameter is used and the network data source is ArcGIS Online. | String |
| allow_auto_relocate | Specifies whether inputs of the designated type with existing network location fields can be automatically relocated at solve time to ensure valid, routable location fields for the analysis. If the value is True, points located on restricted network elements and points affected by barriers will be relocated to the closest routable location. If the value is False, network location fields will be used as is, even if the points are unreachable, and this may cause the solve to fail. Even if the value is False, inputs with no location fields or incomplete location fields will be located at solve time.Specifying a value for this parameter overrides the default allowAutoRelocate property value for the designated input type.If this parameter is not specified or is set to None, the allowAutoRelocate value will be used for this input type.The method returns an error if the network data source is ArcGIS Online.The method returns an error if the network data source is an ArcGIS Enterprise portal that does not support using network location fields. | Boolean |
| search_tolerance | The maximum search distance to use when locating inputs of the designated type on the network.Specifying a value for this parameter overrides the default searchTolerance property value for the designated input type.If this parameter is not specified or is set to None, the searchTolerance value will be used for this input type.The units of this parameter value are set using the search_tolerance_units parameter; however, if no value is set for that parameter, the search_tolerance value will be interpreted in the units specified in the searchToleranceUnits property.This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |
| search_tolerance_units | The units of the maximum search distance when locating inputs of the designated type of the network. The parameter is specified using a member of the DistanceUnits enumeration.Specifying a value for this parameter overrides the default searchToleranceUnits property value for the designated input type.If this parameter is not specified or is set to None, the searchToleranceUnits will be used for this input type.The value specified using the search_tolerance parameter is interpreted using these units. If that parameter is not specified, the value of the searchTolerance property will be interpreted using these units for the designated input type only. This parameter does not apply to line and polygon barriers; the method will return an error if this parameter is specified when the input_type value is one of these barrier types. | Double |

## Methods

### addFields (input_type, field_description)

Adds custom fields to the designated input class. These fields will be included in the field mapping dictionary created by the fieldMappings method and will also be available for use with the insertCursor method.Learn more about using custom fields in analysis inputs

### count (input_type)

Returns the number of rows added for an input type.

### fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})

Generates an NAClassFieldMappings dictionary that maps the field names of the input type to arcpy.nax.NAClassFieldMap objects that allow you to map fields from the input data to the properties of the solver. The dictionary can be used as input to the field_mappings argument of the load method. Learn more about how to use field mappings when loading inputs

### fieldNames (input_type, {use_location_fields})

Get a list of field names supported by the specified input type.

### insertCursor (input_type, field_names, {append})

Establishes a write cursor on the specified input type. This cursor can be used to add rows directly to the input.Learn more about how to insert inputs

### load (input_type, features, {field_mappings}, {append}, {max_features})

Sets input features to use for the analysis. Learn more about how to load inputs

### setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})

Set locate settings for a designated input class, overriding the default locate settings specified for the analysis. This is useful if you want to use different rules to locate different inputs. For example, in an OD cost matrix analysis, you can use a search query that applies to the input origins only, if that query should not apply to the input destinations and barriers.Using this method, you can override the values of the searchSources, allowAutoRelocate, searchTolerance, and searchToleranceUnits properties for the designated input class.Learn more about locating inputs on the network

### solve ()

Perform the service area analysis using the properties set on the ServiceArea object and the loaded inputs.

## Code Samples

### Example 1

```python
ServiceArea (in_network)
```

### Example 2

```python
addFields (input_type, field_description)
```

### Example 3

```python
count (input_type)
```

### Example 4

```python
fieldMappings (input_type, {use_location_fields}, {list_candidate_fields})
```

### Example 5

```python
fieldNames (input_type, {use_location_fields})
```

### Example 6

```python
insertCursor (input_type, field_names, {append})
```

### Example 7

```python
load (input_type, features, {field_mappings}, {append}, {max_features})
```

### Example 8

```python
setLocateSettingsOverrides (input_type, {search_sources}, {allow_auto_relocate}, {search_tolerance}, {search_tolerance_units})
```

### Example 9

```python
# An example showing how to perform service area analysis using a feature class for input facilities.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_facilities = "C:/data/io.gdb/Facilities"
output_polygons = "C:/data/io.gdb/ServiceAreaPolygons"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a ServiceArea solver object
service_area = arcpy.nax.ServiceArea(nd_layer_name)
# Set properties
service_area.timeUnits = arcpy.nax.TimeUnits.Minutes
service_area.defaultImpedanceCutoffs = [5, 10, 15]
service_area.travelMode = travel_mode
service_area.outputType = arcpy.nax.ServiceAreaOutputType.Polygons
service_area.geometryAtOverlap = arcpy.nax.ServiceAreaOverlapGeometry.Split
# Load inputs
service_area.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
# Solve the analysis
result = service_area.solve()

# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 10

```python
# An example showing how to perform service area analysis using a feature class for input facilities.
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_facilities = "C:/data/io.gdb/Facilities"
output_polygons = "C:/data/io.gdb/ServiceAreaPolygons"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a ServiceArea solver object
service_area = arcpy.nax.ServiceArea(nd_layer_name)
# Set properties
service_area.timeUnits = arcpy.nax.TimeUnits.Minutes
service_area.defaultImpedanceCutoffs = [5, 10, 15]
service_area.travelMode = travel_mode
service_area.outputType = arcpy.nax.ServiceAreaOutputType.Polygons
service_area.geometryAtOverlap = arcpy.nax.ServiceAreaOverlapGeometry.Split
# Load inputs
service_area.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
# Solve the analysis
result = service_area.solve()

# Export the results to a feature class
if result.solveSucceeded:
    result.export(arcpy.nax.ServiceAreaOutputDataType.Polygons, output_polygons)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## ServiceAreaOutputType

## Summary

Enumeration of the output type to be generated for a ServiceArea analysis.

---

## ServiceAreaOverlapGeometry

## Summary

Enumeration specifying the desired behavior of the ServiceArea analysis output when multiple facilities are included in the input.

---

## ServiceAreaPolygonCutoffGeometry

## Summary

Enumeration specifying the desired behavior of the ServiceArea output polygons when multiple cutoffs are specified.

---

## ServiceAreaPolygonDetail

## Summary

Enumeration specifying the desired level of detail for the output polygons of a ServiceArea analysis.

---

## ServiceAreaResult

## Summary

An object containing the results of a service area analysis that can be used to access outputs and solver messages.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| output_type | The type of output features to count.Set this parameter using the ServiceAreaOutputDataType enumeration. | Object |
| output_type | The type of output to export. Set this parameter using the ServiceAreaOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| output_features | The catalog path to the output feature class or table that will contain the exported features. | String |
| output_type | The type of output features for which to get the extent.Set this parameter using the ServiceAreaOutputDataType enumeration.If you do not specify a value, or you specify a value of None, the extent for the combined analysis outputs is returned. | Object |
| output_type | The type of output for which to return a list of field names.Set this parameter using the ServiceAreaOutputDataType enumeration.See descriptions of the fields included in each output type | Object |
| file_name | The catalog path of the output layer file (.lyr) or layer package (.lpkx) to write.Caution:Layer files with an .lyr extension cannot be saved if the solver object uses a service URL as its network data source. The method returns a RuntimeError exception in this case. | String |
| output_type | The type of output that will be read. Set this parameter using the ServiceAreaOutputDataType enumeration. | Object |
| field_names[field_names,...] | A list of field names of the output type whose values will be returned by the cursor. You can get the names of the fields that are supported by an output type using the fieldNames method.See descriptions of the fields included in each output typeIn addition to regular fields, you can also access the geometry of the output using one of the following geometry tokens:SHAPE@XY—A tuple of the feature's centroid's x- and y-coordinates.SHAPE@XYZ—A tuple of the feature's centroid's x-, y-, and z-coordinates.SHAPE@JSON— The Esri JSON string representing the geometry.SHAPE@WKB—The well-known binary (WKB) representation for OGC geometry. It provides a portable representation of a geometry value as a contiguous stream of bytes. SHAPE@WKT—The well-known text (WKT) representation for OGC geometry. It provides a portable representation of a geometry value as a text string. SHAPE@—A geometry object for the feature.The SHAPE@XY and SHAPE@XYZ tokens are only supported for point-based output types. The x-, y-, and z-values returned when using the SHAPE@XY and SHAPE@XYZ tokens are in the spatial reference reported by the solver result object's spatialReference property, and this is typically the same as the spatial reference of the network data source used for the analysis. | String |
| where_clause | An optional expression that limits the records returned. For more information on WHERE clauses and SQL statements, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| severity | The type of messages to be returned.The parameter should be specified using the MessageSeverity enumeration. | Object |

## Methods

### count (output_type)

Returns the number of rows for an output type.

### export (output_type, output_features)

Exports the analysis results to a feature class or table.The output features will be created in the spatial reference of the network dataset used for the analysis. If the arcpy.env.outputCoordinateSystem environment is set, the output features will be created with the specified coordinate system instead.

### extent ({output_type})

Returns the extent of the analysis output.The method returns a RuntimeError exception if the analysis solve failed.

### fieldNames (output_type)

Returns a list of field names supported by a specified output type.

### saveAsLayerFile (file_name)

Save the analysis result and settings to a layer file or layer package. The layer file or package can be opened in ArcGIS Pro as a record of the analysis settings or to visualize the results. A layer file can also be opened in ArcGIS Desktop.The method returns a RuntimeError exception if the allowSaveLayerFile property on the solver object is set to False.Legacy:Routing services based on portals running versions of ArcGIS Enterprise older than 10.9 do not support saving layer packages. The method returns a RuntimeError exception if this is the case.

### searchCursor (output_type, field_names, {where_clause})

Establishes a search cursor on the specified output type. This cursor can be used to read rows directly from the output.

### solverMessages (severity)

Get error, warning, and informational messages returned by the solver.

## Code Samples

### Example 1

```python
count (output_type)
```

### Example 2

```python
export (output_type, output_features)
```

### Example 3

```python
extent ({output_type})
```

### Example 4

```python
fieldNames (output_type)
```

### Example 5

```python
saveAsLayerFile (file_name)
```

### Example 6

```python
searchCursor (output_type, field_names, {where_clause})
```

### Example 7

```python
solverMessages (severity)
```

### Example 8

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

### Example 9

```python
[[-2147200995, '0 location(s) in "Destinations" are valid.  Need at least 1 valid location(s).'],
 [30024, 'Solve returned a failure.'],
 [-2147200995, 'Insufficient number of valid locations in "Origins" or "Destinations".']]
```

---

## Set analysis inputs

## Code Samples

### Example 1

```python
input_facilities = "C:/data/io.gdb/FireStations"
service_area.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
```

### Example 2

```python
input_facilities = "C:/data/io.gdb/FireStations"
service_area.load(arcpy.nax.ServiceAreaInputDataType.Facilities, input_facilities)
```

### Example 3

```python
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object
field_mappings = service_area.fieldMappings(arcpy.nax.ServiceAreaInputDataType.Facilities)

# Map the TurnoutTime field from your input data to the Service Area Facilities
# class's AdditionalTime property
field_mappings["AdditionalTime"].mappedFieldName = "TurnoutTime"

# Set a default of one minute of additional time in case the TurnoutTime field
# has a null value
field_mappings["AdditionalTime"].defaultValue = 1

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 4

```python
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object
field_mappings = service_area.fieldMappings(arcpy.nax.ServiceAreaInputDataType.Facilities)

# Map the TurnoutTime field from your input data to the Service Area Facilities
# class's AdditionalTime property
field_mappings["AdditionalTime"].mappedFieldName = "TurnoutTime"

# Set a default of one minute of additional time in case the TurnoutTime field
# has a null value
field_mappings["AdditionalTime"].defaultValue = 1

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 5

```python
# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@XY"]

# Construct the insertCursor for the desired input type using the fields
# specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    # Insert rows. The lists of values inserted match the designated fields.
    cur.insertRow(["Fire Station 1", 1, (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Fire Station 2", 1, (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Fire Station 3", 2.5, (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Fire Station 4", 1.5, (-117.00762504, 32.70097640100005)])
```

### Example 6

```python
# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@XY"]

# Construct the insertCursor for the desired input type using the fields
# specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    # Insert rows. The lists of values inserted match the designated fields.
    cur.insertRow(["Fire Station 1", 1, (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Fire Station 2", 1, (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Fire Station 3", 2.5, (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Fire Station 4", 1.5, (-117.00762504, 32.70097640100005)])
```

### Example 7

```python
sr_wgs84 = arcpy.SpatialReference(4326)

# Input data with latitude and longitude values specified in WGS84 coordinates
input_data = [
    ["Fire Station 1", 1, -117.10191118199998, 32.634351493000054],
    ["Fire Station 2", 1, -116.97970607599996, 32.56210221400005],
    ["Fire Station 3", 2.5, -116.97141447099995, 32.654230331000065],
    ["Fire Station 4", 1.5, -117.00762504, 32.70097640100005]
]

# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@"]

# Construct the insertCursor for the desired input type using the fields
# specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    for input_pt in input_data:
        # Construct a PointGeometry object for the point using the
        # correct spatial reference
        pt_geom = arcpy.PointGeometry(
            arcpy.Point(input_pt[2], input_pt[3]), sr_wgs84)

        # Insert the data using its shape
        cur.insertRow([input_pt[0], input_pt[1], pt_geom])
```

### Example 8

```python
sr_wgs84 = arcpy.SpatialReference(4326)

# Input data with latitude and longitude values specified in WGS84 coordinates
input_data = [
    ["Fire Station 1", 1, -117.10191118199998, 32.634351493000054],
    ["Fire Station 2", 1, -116.97970607599996, 32.56210221400005],
    ["Fire Station 3", 2.5, -116.97141447099995, 32.654230331000065],
    ["Fire Station 4", 1.5, -117.00762504, 32.70097640100005]
]

# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@"]

# Construct the insertCursor for the desired input type using the fields
# specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    for input_pt in input_data:
        # Construct a PointGeometry object for the point using the
        # correct spatial reference
        pt_geom = arcpy.PointGeometry(
            arcpy.Point(input_pt[2], input_pt[3]), sr_wgs84)

        # Insert the data using its shape
        cur.insertRow([input_pt[0], input_pt[1], pt_geom])
```

### Example 9

```python
# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@XY"]

# Open the .csv file and construct a reader using the csv module
with open(in_csv, "r") as f:
    reader = csv.reader(f)
    # Read the headers and don't try to insert this row
    headers = next(reader)
    # Construct the insertCursor for the desired input type using the fields
    # specified
    with service_area.insertCursor(
        arcpy.nax.ServiceAreaInputDataType.Facilities,
        fields
    ) as cur:
        # Iterate through the CSV file's rows and insert them as facilities
        for row in reader:
            cur.insertRow(
                [row[0], float(row[1]), (float(row[2]), float(row[3]),)]
            )
```

### Example 10

```python
# Define fields to use with the insertCursor
fields = ["Name", "AdditionalTime", "SHAPE@XY"]

# Open the .csv file and construct a reader using the csv module
with open(in_csv, "r") as f:
    reader = csv.reader(f)
    # Read the headers and don't try to insert this row
    headers = next(reader)
    # Construct the insertCursor for the desired input type using the fields
    # specified
    with service_area.insertCursor(
        arcpy.nax.ServiceAreaInputDataType.Facilities,
        fields
    ) as cur:
        # Iterate through the CSV file's rows and insert them as facilities
        for row in reader:
            cur.insertRow(
                [row[0], float(row[1]), (float(row[2]), float(row[3]),)]
            )
```

### Example 11

```python
# Set default search tolerance and search sources for all analysis inputs
service_area.searchTolerance = 200
service_area.searchToleranceUnits = arcpy.nax.DistanceUnits.Feet
service_area.searchSources = [["Streets", ""], ["Streets_ND_Junctions", ""]]

# Set a search query for the input facilities only to prevent locating
# on highway ramps (designated, in this example, as ROAD_CLASS 3). This query
# will not apply to other inputs, such as barriers.
sources = [["Streets", "ROAD_CLASS <> 3"], ["Streets_ND_Junctions", ""]]
service_area.setLocateSettingsOverrides(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    search_sources=sources
)
```

### Example 12

```python
# Set default search tolerance and search sources for all analysis inputs
service_area.searchTolerance = 200
service_area.searchToleranceUnits = arcpy.nax.DistanceUnits.Feet
service_area.searchSources = [["Streets", ""], ["Streets_ND_Junctions", ""]]

# Set a search query for the input facilities only to prevent locating
# on highway ramps (designated, in this example, as ROAD_CLASS 3). This query
# will not apply to other inputs, such as barriers.
sources = [["Streets", "ROAD_CLASS <> 3"], ["Streets_ND_Junctions", ""]]
service_area.setLocateSettingsOverrides(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    search_sources=sources
)
```

### Example 13

```python
# Network locations have been precalculated for these inputs
# using the Calculate Locations tool. The feature class
# includes the network location fields:
# SourceID, SourceOID, PosAlong, SideOfEdge
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object with network location fields
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    use_location_fields=True
)

# Load your input data using the field mappings
# Location fields are included automatically because
# of the field mappings.
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 14

```python
# Network locations have been precalculated for these inputs
# using the Calculate Locations tool. The feature class
# includes the network location fields:
# SourceID, SourceOID, PosAlong, SideOfEdge
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object with network location fields
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    use_location_fields=True
)

# Load your input data using the field mappings
# Location fields are included automatically because
# of the field mappings.
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 15

```python
# Define fields to use with the insertCursor
fields = ["Name", "SHAPE@XY", "SourceID", "SourceOID", "PosAlong", "SideOfEdge"]

# Define input data with network location fields
# The latitude and longitude are not strictly necessary because the inputs
# have already been located on the network.
input_data = [
    ["Fire Station 1", (-117.10191118199998, 32.634351493000054), 1, 9533, 0.5, 2],
    ["Fire Station 2", (-116.97970607599996, 32.56210221400005), 1, 7629, 0.33, 1],
    ["Fire Station 3", (-116.97141447099995, 32.654230331000065), 1, 2309, 1.0, 1],
    ["Fire Station 4", (-117.00762504, 32.70097640100005), 1, 9016, 0.62, 1]
]

# Insert the facilities
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    for input_pt in input_data:
        cur.insertRow(input_pt)
```

### Example 16

```python
# Define fields to use with the insertCursor
fields = ["Name", "SHAPE@XY", "SourceID", "SourceOID", "PosAlong", "SideOfEdge"]

# Define input data with network location fields
# The latitude and longitude are not strictly necessary because the inputs
# have already been located on the network.
input_data = [
    ["Fire Station 1", (-117.10191118199998, 32.634351493000054), 1, 9533, 0.5, 2],
    ["Fire Station 2", (-116.97970607599996, 32.56210221400005), 1, 7629, 0.33, 1],
    ["Fire Station 3", (-116.97141447099995, 32.654230331000065), 1, 2309, 1.0, 1],
    ["Fire Station 4", (-117.00762504, 32.70097640100005), 1, 9016, 0.62, 1]
]

# Insert the facilities
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    for input_pt in input_data:
        cur.insertRow(input_pt)
```

### Example 17

```python
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object
# Use the list_candidate_fields parameter to include non-default custom fields
# from the input
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    list_candidate_fields=arcpy.ListFields(input_facilities)
)

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 18

```python
input_facilities = "C:/data/io.gdb/FireStations"

# Construct a field mapping object
# Use the list_candidate_fields parameter to include non-default custom fields
# from the input
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    list_candidate_fields=arcpy.ListFields(input_facilities)
)

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 19

```python
input_facilities = "C:/data/io.gdb/FireStations"
extra_fields = [f for f in arcpy.ListFields(input_facilities) if f.name == "NumTrucks"]

# Construct a field mapping object
# Use the list_candidate_fields parameter to include non-default custom fields 
# from the input
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    list_candidate_fields=extra_fields
)

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 20

```python
input_facilities = "C:/data/io.gdb/FireStations"
extra_fields = [f for f in arcpy.ListFields(input_facilities) if f.name == "NumTrucks"]

# Construct a field mapping object
# Use the list_candidate_fields parameter to include non-default custom fields 
# from the input
field_mappings = service_area.fieldMappings(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    list_candidate_fields=extra_fields
)

# Load your input data using the field mappings
service_area.load(
    arcpy.nax.ServiceAreaInputDataType.Facilities,
    input_facilities,
    field_mappings
)
```

### Example 21

```python
# Add a custom field called NumTrucks to the Service Area Facilities input class
field_definitions = [["NumTrucks", "SHORT"]]
service_area.addFields(arcpy.nax.ServiceAreaInputDataType.Facilities, field_definitions)

# Define fields to use with the insertCursor
fields = ["Name", "NumTrucks", "AdditionalTime", "SHAPE@XY"]
# Construct the insertCursor for the desired input type using the fields specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    # Insert rows. The lists of values inserted match the designated fields.
    cur.insertRow(["Fire Station 1", 1, 1, (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Fire Station 2", 2, 1, (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Fire Station 3", 4, 2.5, (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Fire Station 4", 2, 1.5, (-117.00762504, 32.70097640100005)])
```

### Example 22

```python
# Add a custom field called NumTrucks to the Service Area Facilities input class
field_definitions = [["NumTrucks", "SHORT"]]
service_area.addFields(arcpy.nax.ServiceAreaInputDataType.Facilities, field_definitions)

# Define fields to use with the insertCursor
fields = ["Name", "NumTrucks", "AdditionalTime", "SHAPE@XY"]
# Construct the insertCursor for the desired input type using the fields specified
with service_area.insertCursor(arcpy.nax.ServiceAreaInputDataType.Facilities, fields) as cur:
    # Insert rows. The lists of values inserted match the designated fields.
    cur.insertRow(["Fire Station 1", 1, 1, (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Fire Station 2", 2, 1, (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Fire Station 3", 4, 2.5, (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Fire Station 4", 2, 1.5, (-117.00762504, 32.70097640100005)])
```

---

## SolverInsertCursor

## Summary

A write cursor for a solver class, specific to an input type, that can be used to add rows directly to the input.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| row | The row to insert, represented as either a list or a tuple. The length of the list and the ordering and datatypes of the list items must match the list of field names specified in the field_names parameter of the insertCursor method used to instantiate the cursor. | List |

## Methods

### insertRow (row)

Insert a row into a network analysis solver input using a cursor.

## Code Samples

### Example 1

```python
insertRow (row)
```

### Example 2

```python
# An example showing how to use the insertCursor() method to set inputs for an analysis
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
output_routes = "C:/data/io.gdb/Routes"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a Route solver object
route = arcpy.nax.Route(nd_layer_name)
# Set properties
route.timeUnits = arcpy.nax.TimeUnits.Minutes
route.travelMode = travel_mode
route.routeShapeType = arcpy.nax.RouteShapeType.TrueShapeWithMeasures
# Set input stops using insertCursor()
fields = ["Name", "RouteName", "SHAPE@XY"]
with route.insertCursor(arcpy.nax.RouteInputDataType.Stops, fields) as cur:
    cur.insertRow(["Stop 1", "Route 1", (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Stop 2", "Route 1", (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Stop 1", "Route 2", (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Stop 2", "Route 2", (-117.00762504, 32.70097640100005)])
# Solve the analysis
result = route.solve()
```

### Example 3

```python
# An example showing how to use the insertCursor() method to set inputs for an analysis
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
output_routes = "C:/data/io.gdb/Routes"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a Route solver object
route = arcpy.nax.Route(nd_layer_name)
# Set properties
route.timeUnits = arcpy.nax.TimeUnits.Minutes
route.travelMode = travel_mode
route.routeShapeType = arcpy.nax.RouteShapeType.TrueShapeWithMeasures
# Set input stops using insertCursor()
fields = ["Name", "RouteName", "SHAPE@XY"]
with route.insertCursor(arcpy.nax.RouteInputDataType.Stops, fields) as cur:
    cur.insertRow(["Stop 1", "Route 1", (-117.10191118199998, 32.634351493000054)])
    cur.insertRow(["Stop 2", "Route 1", (-116.97970607599996, 32.56210221400005)])
    cur.insertRow(["Stop 1", "Route 2", (-116.97141447099995, 32.654230331000065)])
    cur.insertRow(["Stop 2", "Route 2", (-117.00762504, 32.70097640100005)])
# Solve the analysis
result = route.solve()
```

### Example 4

```python
# An example showing how to use the insertCursor() method to set inputs for an analysis
# Use ArcGIS Online as the network data source and PointGeometry objects as inputs
import arcpy

sr_wgs84 = arcpy.SpatialReference(4326)

# Instantiate a Route solver object using ArcGIS Online as the network data source
route = arcpy.nax.Route("https://www.arcgis.com/")

# Input data with latitude and longitude values specified in WGS84 coordinates
input_data = [
    ["Stop 1", "Route 1", -117.10191118199998, 32.634351493000054],
    ["Stop 2", "Route 1", -116.97970607599996, 32.56210221400005],
    ["Stop 1", "Route 2", -116.97141447099995, 32.654230331000065],
    ["Stop 2", "Route 2", -117.00762504, 32.70097640100005]
]

# Set input stops using insertCursor()
fields = ["Name", "RouteName", "SHAPE@"]
with route.insertCursor(arcpy.nax.RouteInputDataType.Stops, fields) as cur:
    for input_pt in input_data:
        # Construct a PointGeometry object for the point using the correct spatial reference
        pt_geom = arcpy.PointGeometry(arcpy.Point(input_pt[2], input_pt[3]), sr_wgs84)
        # Insert the data using its shape
        cur.insertRow([input_pt[0], input_pt[1], pt_geom])

# Solve the analysis
result = route.solve()
print(result.solveSucceeded)
```

### Example 5

```python
# An example showing how to use the insertCursor() method to set inputs for an analysis
# Use ArcGIS Online as the network data source and PointGeometry objects as inputs
import arcpy

sr_wgs84 = arcpy.SpatialReference(4326)

# Instantiate a Route solver object using ArcGIS Online as the network data source
route = arcpy.nax.Route("https://www.arcgis.com/")

# Input data with latitude and longitude values specified in WGS84 coordinates
input_data = [
    ["Stop 1", "Route 1", -117.10191118199998, 32.634351493000054],
    ["Stop 2", "Route 1", -116.97970607599996, 32.56210221400005],
    ["Stop 1", "Route 2", -116.97141447099995, 32.654230331000065],
    ["Stop 2", "Route 2", -117.00762504, 32.70097640100005]
]

# Set input stops using insertCursor()
fields = ["Name", "RouteName", "SHAPE@"]
with route.insertCursor(arcpy.nax.RouteInputDataType.Stops, fields) as cur:
    for input_pt in input_data:
        # Construct a PointGeometry object for the point using the correct spatial reference
        pt_geom = arcpy.PointGeometry(arcpy.Point(input_pt[2], input_pt[3]), sr_wgs84)
        # Insert the data using its shape
        cur.insertRow([input_pt[0], input_pt[1], pt_geom])

# Solve the analysis
result = route.solve()
print(result.solveSucceeded)
```

---

## SolverResultSearchCursor

## Summary

A read cursor for a solver result class, specific to an output type, that can be used to read rows directly from the output.

## Code Samples

### Example 1

```python
# An example showing how to use the searchCursor() method to access the output of an analysis
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.timeUnits = arcpy.nax.TimeUnits.Minutes
odcm.distanceUnits = arcpy.nax.DistanceUnits.Miles
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine
# Load inputs
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations)
# Solve the analysis
result = odcm.solve()

# Print the OD cost matrix results
if result.solveSucceeded:
    fields = ['OriginOID', 'DestinationOID', 'DestinationRank', 'Total_Time', 'Total_Distance']
    for row in result.searchCursor(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, fields):
        print(row)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

### Example 2

```python
# An example showing how to use the searchCursor() method to access the output of an analysis
import arcpy
arcpy.CheckOutExtension("network")

nds = "C:/data/NorthAmerica.gdb/Routing/Routing_ND"
nd_layer_name = "Routing_ND"
input_origins = "C:/data/io.gdb/Origins"
input_destinations = "C:/data/io.gdb/Destinations"

# Create a network dataset layer and get the desired travel mode for analysis
arcpy.nax.MakeNetworkDatasetLayer(nds, nd_layer_name)
nd_travel_modes = arcpy.nax.GetTravelModes(nd_layer_name)
travel_mode = nd_travel_modes["Driving Time"]

# Instantiate a OriginDestinationCostMatrix solver object
odcm = arcpy.nax.OriginDestinationCostMatrix(nd_layer_name)
# Set properties
odcm.travelMode = travel_mode
odcm.timeUnits = arcpy.nax.TimeUnits.Minutes
odcm.distanceUnits = arcpy.nax.DistanceUnits.Miles
odcm.lineShapeType = arcpy.nax.LineShapeType.NoLine
# Load inputs
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Origins, input_origins)
odcm.load(arcpy.nax.OriginDestinationCostMatrixInputDataType.Destinations, input_destinations)
# Solve the analysis
result = odcm.solve()

# Print the OD cost matrix results
if result.solveSucceeded:
    fields = ['OriginOID', 'DestinationOID', 'DestinationRank', 'Total_Time', 'Total_Distance']
    for row in result.searchCursor(arcpy.nax.OriginDestinationCostMatrixOutputDataType.Lines, fields):
        print(row)
else:
    print("Solve failed")
    print(result.solverMessages(arcpy.nax.MessageSeverity.All))
```

---

## StreetDirectionsProperties

## Summary

Provides read and write access to street directions properties, allowing you to customize the directions output from your network analysis layers. The StreetDirectionsProperties can be read from and set on a SolverProperties object obtained through the GetSolverProperties function.

## Code Samples

### Example 1

```python
# Name: StreetDirectionsProperties.py
# Description: Read a route layer from a layer file on disk, change the
#               directions properties, and generate directions features
# Requirements: Network Analyst Extension

#Import system modules
import arcpy

try:

    #Get the route layer object from a layer file on disk
    layer_object = arcpy.mp.LayerFile(r'C:\Data\Route.lyrx').listLayers()[0]

    #Get the solver properties of the layer.
    solver_props = arcpy.na.GetSolverProperties(layer_object)

    #Get the street directions properties
    directions_props = solver_props.streetDirectionsProperties

    #Set the lengthUnits to Kilometers
    directions_props.lengthUnits = "Kilometers"

    #Set the outputSpatialReference to web mercator
    sr = arcpy.SpatialReference(3785)
    directions_props.outputSpatialReference = sr

    #Generate directions features and save them to disk.
    arcpy.na.GenerateDirectionsFeatures(layer_object,
                                        r'C:\Data\Output.gdb\RouteDirections')

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occured on line %i" % tb.tb_lineno)
    print(str(e))
```

### Example 2

```python
# Name: StreetDirectionsProperties.py
# Description: Read a route layer from a layer file on disk, change the
#               directions properties, and generate directions features
# Requirements: Network Analyst Extension

#Import system modules
import arcpy

try:

    #Get the route layer object from a layer file on disk
    layer_object = arcpy.mp.LayerFile(r'C:\Data\Route.lyrx').listLayers()[0]

    #Get the solver properties of the layer.
    solver_props = arcpy.na.GetSolverProperties(layer_object)

    #Get the street directions properties
    directions_props = solver_props.streetDirectionsProperties

    #Set the lengthUnits to Kilometers
    directions_props.lengthUnits = "Kilometers"

    #Set the outputSpatialReference to web mercator
    sr = arcpy.SpatialReference(3785)
    directions_props.outputSpatialReference = sr

    #Generate directions features and save them to disk.
    arcpy.na.GenerateDirectionsFeatures(layer_object,
                                        r'C:\Data\Output.gdb\RouteDirections')

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occured on line %i" % tb.tb_lineno)
    print(str(e))
```

---

## TimeUnits

## Summary

Enumeration to select the desired time units for reporting time-based costs in the output of the analysis. Regardless of the units of the cost attributes in the network dataset, the outputs will be transformed to and reported in the units set in using this property.

---

## TimeZoneUsage

## Summary

Enumeration specifying how the time of day for the analysis should be interpreted.

---

## TravelDirection

## Summary

Enumeration to specify the direction of travel to or from the facilities in the network analysis.

---

## TravelMode

## Summary

Provides read and write access to the properties of a travel mode.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| template_travel_mode | An existing TravelMode object to use as a template for the one to be created. The new TravelMode object will be created with the same properties as the template object, except that the name property will be altered to include angle brackets indicating that the new travel mode is a copy. For example, if the template travel mode was named Driving Time, the new one will be named <Driving Time>.If a template is not specified or a value of None is used, a blank TravelMode object will be created, and the values of all properties must be explicitly set before using the travel mode in a network analysis. | Object |

## Code Samples

### Example 1

```python
TravelMode ({template_travel_mode})
```

### Example 2

```python
attr_params = travel_mode.attributeParameters
attr_params[('Height Restriction', 'Vehicle Height (feet)')] = 12
travel_mode.attributeParameters = attr_params
```

### Example 3

```python
attr_params = travel_mode.attributeParameters
attr_params[('Height Restriction', 'Vehicle Height (feet)')] = 12
travel_mode.attributeParameters = attr_params
```

### Example 4

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 5

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 6

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.nax.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when constructing an OD cost matrix analysis
od_object = arcpy.nax.OriginDestinationCostMatrix(network)
od_object.travelMode = new_travel_mode
```

### Example 7

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.nax.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.nax.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when constructing an OD cost matrix analysis
od_object = arcpy.nax.OriginDestinationCostMatrix(network)
od_object.travelMode = new_travel_mode
```

---

## TravelMode

## Summary

Provides read and write access to the properties of a travel mode.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| template_travel_mode | An existing TravelMode object to use as a template for the one to be created. The new TravelMode object will be created with the same properties as the template object, except that the name property will be altered to include angle brackets indicating that the new travel mode is a copy. For example, if the template travel mode was named Driving Time, the new one will be named <Driving Time>.If a template is not specified or a value of None is used, a blank TravelMode object will be created, and the values of all properties must be explicitly set before using the travel mode in a network analysis. | Object |

## Code Samples

### Example 1

```python
TravelMode ({template_travel_mode})
```

### Example 2

```python
attr_params = travel_mode.attributeParameters
attr_params[('Height Restriction', 'Vehicle Height (feet)')] = 12
travel_mode.attributeParameters = attr_params
```

### Example 3

```python
attr_params = travel_mode.attributeParameters
attr_params[('Height Restriction', 'Vehicle Height (feet)')] = 12
travel_mode.attributeParameters = attr_params
```

### Example 4

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 5

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)

# Print the impedance attribute and restrictions used for each travel mode
for travel_mode_name in travel_modes:
    travel_mode = travel_modes[travel_mode_name]
    print(travel_mode_name)
    print("Impedance:", travel_mode.impedance)
    print("Restrictions:", ", ".join(travel_mode.restrictions))
    print("")
```

### Example 6

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when creating an OD cost matrix analysis layer
arcpy.na.MakeODCostMatrixAnalysisLayer(network, "OD Cost Matrix", new_travel_mode)
```

### Example 7

```python
import arcpy

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)
# Construct a new TravelMode object from the existing Driving Time travel mode
new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
# Update the useHierarchy property to turn hierarchy off, and update the name
new_travel_mode.name = "Driving Time without Hierarchy"
new_travel_mode.useHierarchy = "NO_HIERARCHY"
# Use the new travel mode object when creating an OD cost matrix analysis layer
arcpy.na.MakeODCostMatrixAnalysisLayer(network, "OD Cost Matrix", new_travel_mode)
```

---

## Use routing services from a standalone ArcGIS Server site

## Code Samples

### Example 1

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer"
}
```

### Example 2

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer"
}
```

### Example 3

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
    "authenticationInfo": {
        "username": "my_username",
        "password": "my_password"
    }
}
```

### Example 4

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
    "authenticationInfo": {
        "username": "my_username",
        "password": "my_password"
    }
}
```

### Example 5

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
    "authenticationInfo": {
        "connectionFile": "C:\\data\\my_connection_file.ags"
    }
}
```

### Example 6

```python
{
    "url": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysis/GPServer",
    "utilityUrl": "https://webadaptorhost.domain.com/webadaptorname/rest/services/Routing/NetworkAnalysisUtilities/GPServer",
    "authenticationInfo": {
        "connectionFile": "C:\\data\\my_connection_file.ags"
    }
}
```

---

## VehicleRoutingProblemSchemaVersion

## Summary

Enumeration specifying the schema version to use for a VehicleRoutingProblem analysis.

---
