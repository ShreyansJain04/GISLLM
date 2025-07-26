# ArcPy Functions by Category

*Consolidated from 245 individual documentation files*

---

## AcceptConnections

## Summary

Allows an administrator to enable or disable the ability of nonadministrative users to make connections to an enterprise geodatabase.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| sde_workspace | The Enterprise geodatabase that will have its connection property altered.The connection properties specified in the Enterprise Geodatabase must be the geodatabase administrator. | String |
| accept_connections | Boolean value indicating if the geodatabase will accept connections (True) or will not accept connections (False). | Boolean |

## Code Samples

### Example 1

```python
AcceptConnections (sde_workspace, accept_connections)
```

### Example 2

```python
import arcpy

arcpy.AcceptConnections("C:\\MyProject\\admin.sde", False)
```

### Example 3

```python
import arcpy

arcpy.AcceptConnections("C:\\MyProject\\admin.sde", False)
```

### Example 4

```python
import arcpy

# Set Admin workspace variable
admin_workspace = "C:\\MyProject\\admin.sde"

# Block connections
arcpy.AcceptConnections(admin_workspace, False)

# Disconnect users
arcpy.DisconnectUser(admin_workspace, 'ALL')

# Reconcile/Post using default parameters.
arcpy.management.ReconcileVersions(admin_workspace, 'ALL_VERSIONS',
                                   'sde.DEFAULT', with_post='POST')

# Compress the geodatabase
arcpy.management.Compress(admin_workspace)

# Allow connections.
arcpy.AcceptConnections(admin_workspace, True)
```

### Example 5

```python
import arcpy

# Set Admin workspace variable
admin_workspace = "C:\\MyProject\\admin.sde"

# Block connections
arcpy.AcceptConnections(admin_workspace, False)

# Disconnect users
arcpy.DisconnectUser(admin_workspace, 'ALL')

# Reconcile/Post using default parameters.
arcpy.management.ReconcileVersions(admin_workspace, 'ALL_VERSIONS',
                                   'sde.DEFAULT', with_post='POST')

# Compress the geodatabase
arcpy.management.Compress(admin_workspace)

# Allow connections.
arcpy.AcceptConnections(admin_workspace, True)
```

---

## AddDataStoreItem

## Summary

Registers a folder or database with an ArcGIS Server site.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| connection_file | For a hosting server, provide the server URL or use the MY_HOSTED_SERVICES keyword. For a stand-alone server, an ArcGIS Server connection file (.ags) representing the server with which you want to register the data. | String |
| datastore_type | The type of data being registered.DATABASE—The data resides in an enterprise database.FOLDER—The data is file-based. | String |
| connection_name | A name for the folder or database that publishers or administrators will see when they view the server properties. | String |
| server_path | The path or connection to the data as identified by the server.If you're registering a DATABASE, this is either the path to a database connection file (.sde) or a string containing the database connection parameters.If you're registering a FOLDER, this is the path to the folder. | String |
| client_path | The path or connection to the data as identified by the publisher's machine, if different from the information used by the server. In some cases, the publisher and the server may be referencing physically distinct databases or folders. When you provide the publisher path and the server path, ArcGIS Server automatically corrects the paths at publish time when your map documents and other resources are transferred to the server.If you're registering a DATABASE, provide either the path to a database connection file (.sde) or a string containing the database connection parameters.If you're registering a FOLDER, provide the path to the folder.If you're registering an ArcGIS Server managed database, do not provide a path; instead, provide the string managed for this parameter. An ArcGIS Server managed database is an enterprise geodatabase you designate where data can be copied at publish time if a user attempts to publish a feature service from an unregistered data location. | String |
| hostname | The name of the publisher or client machine that will use the registered folder or database. If left blank, the name of the machine running the script will be used. | String |

## Code Samples

### Example 1

```python
AddDataStoreItem (connection_file, datastore_type, connection_name, server_path, {client_path}, {hostname})
```

### Example 2

```python
import arcpy

conn = "GIS Servers/MyConnection.ags"
path = "c:/temp"

arcpy.AddDataStoreItem(conn, "FOLDER", "My local data folder", path, path)
```

### Example 3

```python
import arcpy

conn = "GIS Servers/MyConnection.ags"
path = "c:/temp"

arcpy.AddDataStoreItem(conn, "FOLDER", "My local data folder", path, path)
```

### Example 4

```python
import arcpy

conn = "c:/connections/MYSERVER.ags"

arcpy.AddDataStoreItem(conn, "FOLDER", "Washington",
                       "//MYSERVER/mydata/Washington",
                       "c:/mydata/Washington", "MYPUBLISHER")
```

### Example 5

```python
import arcpy

conn = "c:/connections/MYSERVER.ags"

arcpy.AddDataStoreItem(conn, "FOLDER", "Washington",
                       "//MYSERVER/mydata/Washington",
                       "c:/mydata/Washington", "MYPUBLISHER")
```

### Example 6

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"
db_conn = "c:/connections/Connection to wilma.sde"

arcpy.AddDataStoreItem(server_conn, "DATABASE", "Wilma", db_conn, db_conn)
```

### Example 7

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"
db_conn = "c:/connections/Connection to wilma.sde"

arcpy.AddDataStoreItem(server_conn, "DATABASE", "Wilma", db_conn, db_conn)
```

### Example 8

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"
db_conn_serv = "c:/connections/Connection to wilma.sde"
db_conn_pub = "c:/connections/Connection to pebbles.sde"

arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "WilmaAndPebbles", db_conn_serv, db_conn_pub)
```

### Example 9

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"
db_conn_serv = "c:/connections/Connection to wilma.sde"
db_conn_pub = "c:/connections/Connection to pebbles.sde"

arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "WilmaAndPebbles", db_conn_serv, db_conn_pub)
```

### Example 10

```python
import arcpy

server_conn = "https://www.MYSERVER.com/server"
db_conn_serv = "c:/connections/Connection to wilma.sde"

arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "WilmaManaged", db_conn_serv, "managed")
```

### Example 11

```python
import arcpy

server_conn = "https://www.MYSERVER.com/server"
db_conn_serv = "c:/connections/Connection to wilma.sde"

arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "WilmaManaged", db_conn_serv, "managed")
```

### Example 12

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"

db_conn_string = u"PASSWORD=pwdX;SERVER=serverX;" + \
                 u"INSTANCE=sde:sqlserver:serverX;DBCLIENT=sqlserver;" + \
                 u"DB_CONNECTION_PROPERTIES=serverX;" + \
                 u"DATABASE=sde;USER=userX;AUTHENTICATION_MODE=DBMS"
                           
arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "ServerX", db_conn_string, db_conn_string)
```

### Example 13

```python
import arcpy

server_conn = "c:/connections/MYSERVER.ags"

db_conn_string = u"PASSWORD=pwdX;SERVER=serverX;" + \
                 u"INSTANCE=sde:sqlserver:serverX;DBCLIENT=sqlserver;" + \
                 u"DB_CONNECTION_PROPERTIES=serverX;" + \
                 u"DATABASE=sde;USER=userX;AUTHENTICATION_MODE=DBMS"
                           
arcpy.AddDataStoreItem(
    server_conn, "DATABASE", "ServerX", db_conn_string, db_conn_string)
```

---

## AddError

## Summary

Adds an error message (severity of 2) to the messages of a script tool or Python toolbox tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| message | The error message. | String |

## Code Samples

### Example 1

```python
AddError (message)
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from the GetCount tool's Result object
feature_count = int(arcpy.GetCount_management(fc)[0])

if feature_count == 0:
    arcpy.AddError("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from the GetCount tool's Result object
feature_count = int(arcpy.GetCount_management(fc)[0])

if feature_count == 0:
    arcpy.AddError("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

---

## AddFieldDelimiters

## Summary

Adds field delimiters to a field name for use in SQL queries.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| datasource | The data source used to determine the field delimiters. | String |
| field | The field name to which delimiters will be added. The field does not have to currently exist. | String |

## Code Samples

### Example 1

```python
AddFieldDelimiters (datasource, field)
```

### Example 2

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
arcpy.env.workspace = arcpy.GetParameterAsText(1)
in_features = arcpy.GetParameterAsText(2)
out_feat_class = arcpy.GetParameterAsText(3)
state_value = arcpy.GetParameterAsText(4)

# AddFieldDelimiters will return a field name with the proper
# field delimiters for the workspace specified.
sql_exp = """{0} = '{1}'""".format(
    arcpy.AddFieldDelimiters('c:/data', field_name),
    state_value)

# Use delimited field for Select tool SQL expression
arcpy.analysis.Select(in_features, out_feat_class, sql_exp)
```

### Example 3

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
arcpy.env.workspace = arcpy.GetParameterAsText(1)
in_features = arcpy.GetParameterAsText(2)
out_feat_class = arcpy.GetParameterAsText(3)
state_value = arcpy.GetParameterAsText(4)

# AddFieldDelimiters will return a field name with the proper
# field delimiters for the workspace specified.
sql_exp = """{0} = '{1}'""".format(
    arcpy.AddFieldDelimiters('c:/data', field_name),
    state_value)

# Use delimited field for Select tool SQL expression
arcpy.analysis.Select(in_features, out_feat_class, sql_exp)
```

---

## AddIDMessage

## Summary

Use system ID messages with a script tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| message_type | Specifies the message severity.ERROR—Adds an error message to the tool messagesINFORMATIVE—Adds an informative message to the tool messagesWARNING—Adds a warning message to the tool messages | String |
| message_ID | The message ID allows you to reference existing messages for your scripting errors and warnings. | Integer |
| add_argument1 | Depending on which message ID is used, an argument may be necessary to complete the message. Common examples include dataset or field names. Data type can be string, integer, or double. | Object |
| add_argument2 | Depending on which message ID is used, an argument may be necessary to complete the message. Common examples include dataset or field names. Data type can be string, integer, or double. | Object |

## Code Samples

### Example 1

```python
AddIDMessage (message_type, message_ID, {add_argument1}, {add_argument2})
```

### Example 2

```python
class overwriteError(Exception):
    pass

import arcpy

in_feature_class = arcpy.GetParameterAsText(0)
out_feature_class = arcpy.GetParameterAsText(1)

try:
    # If the output feature class already exists, raise an error
    if arcpy.Exists(in_feature_class):
        # Raise a custom exception
        raise overwriteError(out_feature_class)
    else:
        arcpy.CopyFeatures_management(in_feature_class, out_feature_class)

except overwriteError as err:
    # Use message ID 12, and provide the output feature class
    #    to complete the message.
    arcpy.AddIDMessage("Error", 12, str(err))
```

### Example 3

```python
class overwriteError(Exception):
    pass

import arcpy

in_feature_class = arcpy.GetParameterAsText(0)
out_feature_class = arcpy.GetParameterAsText(1)

try:
    # If the output feature class already exists, raise an error
    if arcpy.Exists(in_feature_class):
        # Raise a custom exception
        raise overwriteError(out_feature_class)
    else:
        arcpy.CopyFeatures_management(in_feature_class, out_feature_class)

except overwriteError as err:
    # Use message ID 12, and provide the output feature class
    #    to complete the message.
    arcpy.AddIDMessage("Error", 12, str(err))
```

---

## AddMessage

## Summary

Adds an informative message (severity of 0) to the messages of a script tool or Python toolbox tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| message | The informative message. | String |

## Code Samples

### Example 1

```python
AddMessage (message)
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from GetCount's Result object
feature_count = int(arcpy.GetCount_management(fc).getOutput(0))

if feature_count == 0:
    arcpy.AddError("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from GetCount's Result object
feature_count = int(arcpy.GetCount_management(fc).getOutput(0))

if feature_count == 0:
    arcpy.AddError("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

---

## AddReturnMessage

## Summary

Sets the return message of a script tool as an output message by index.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The message index. | Integer |

## Code Samples

### Example 1

```python
import arcpy
try:    
    result = arcpy.GetCount_management("c:/data/rivers.shp")

except:    
    # Return Geoprocessing tool specific errors
    #
    for msg in range(0, arcpy.GetMessageCount()):
        if arcpy.GetSeverity(msg) == 2:
            arcpy.AddReturnMessage(msg)
```

### Example 2

```python
import arcpy
try:    
    result = arcpy.GetCount_management("c:/data/rivers.shp")

except:    
    # Return Geoprocessing tool specific errors
    #
    for msg in range(0, arcpy.GetMessageCount()):
        if arcpy.GetSeverity(msg) == 2:
            arcpy.AddReturnMessage(msg)
```

### Example 3

```python
AddReturnMessage (index)
```

### Example 4

```python
import arcpy

# Set current workspace
arcpy.env.workspace = "c:/data/base.gdb"

arcpy.Buffer_analysis("roads", "roads_buffer_1000", "1000 feet")

# Return the resulting messages as script tool output messages
for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)
```

### Example 5

```python
import arcpy

# Set current workspace
arcpy.env.workspace = "c:/data/base.gdb"

arcpy.Buffer_analysis("roads", "roads_buffer_1000", "1000 feet")

# Return the resulting messages as script tool output messages
for i in range(0, arcpy.GetMessageCount()):
    arcpy.AddReturnMessage(i)
```

---

## AddToolbox

## Summary

Imports the specified toolbox into ArcPy, allowing for access to the toolbox's associated tools.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| input_file | The geoprocessing toolbox to be accessed from ArcPy. | String |
| module_name | If the toolbox does not have an alias, the module_name is required. When a tool is accessed through the ArcPy site package, the toolbox alias where the tool is contained is a required suffix (arcpy.<toolname>_<alias> or arcpy.<alias>.<toolname>). Since ArcPy depends on toolbox aliases to access and run the correct tool, aliases are important when importing custom toolboxes. It is recommended that you define a custom toolbox's alias; however, if the toolbox alias is not defined, a temporary alias can be set as the second parameter. | String |

## Code Samples

### Example 1

```python
import arcpy
tbx = "http://logistics.arcgis.com/arcgis/services;World/ServiceAreas;UseSSOIdentityIfPortalOwned"
arcpy.AddToolbox(tbx)
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 2

```python
import arcpy
tbx = "http://logistics.arcgis.com/arcgis/services;World/ServiceAreas;UseSSOIdentityIfPortalOwned"
arcpy.AddToolbox(tbx)
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 3

```python
import arcpy

token = 'sadsa213d2j32jsdw02dm2'
referrer = 'http://www.arcgis.com/'
tbx = 'http://logistics.arcgis.com/arcgis/services;' + \
      'World/ServiceAreas;token={};{}'.format(token, referrer)
arcpy.ImportToolbox(tbx)
result = arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 4

```python
import arcpy

token = 'sadsa213d2j32jsdw02dm2'
referrer = 'http://www.arcgis.com/'
tbx = 'http://logistics.arcgis.com/arcgis/services;' + \
      'World/ServiceAreas;token={};{}'.format(token, referrer)
arcpy.ImportToolbox(tbx)
result = arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 5

```python
AddToolbox (input_file, {module_name})
```

### Example 6

```python
import arcpy

# Import custom toolbox
arcpy.AddToolbox("c:/tools/My_Analysis_Tools.atbx")

try:
    # Run tool in the custom toolbox.  The tool is identified by the tool name
    # and the toolbox alias.
    arcpy.GetPoints_myanalysis("c:/data/forest.shp")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 7

```python
import arcpy

# Import custom toolbox
arcpy.AddToolbox("c:/tools/My_Analysis_Tools.atbx")

try:
    # Run tool in the custom toolbox.  The tool is identified by the tool name
    # and the toolbox alias.
    arcpy.GetPoints_myanalysis("c:/data/forest.shp")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## AddWarning

## Summary

Adds a warning message (severity of 1) to the messages of a script tool or Python toolbox tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| message | The warning message. | String |

## Code Samples

### Example 1

```python
AddWarning (message)
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from GetCount's Result object
feature_count = int(arcpy.GetCount_management(fc).getOutput(0))

if feature_count == 0:
    arcpy.AddWarning("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

# Get the count from GetCount's Result object
feature_count = int(arcpy.GetCount_management(fc).getOutput(0))

if feature_count == 0:
    arcpy.AddWarning("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("{0} has {1} features.".format(fc, feature_count))
```

---

## Aggregated Lines for SubnetLine properties

## Summary

The properties below are returned by the aggregatedLinesForSubnetLine object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Aggregated Lines for SubnetLine Properties        
        for al in tier.aggregatedLinesForSubnetLine:
            print(" -- Aggregated Lines for SubnetLine Properties -- ")
            print(f"Asset Group Code: {al.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in al.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Aggregated Lines for SubnetLine Properties        
        for al in tier.aggregatedLinesForSubnetLine:
            print(" -- Aggregated Lines for SubnetLine Properties -- ")
            print(f"Asset Group Code: {al.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in al.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")
```

---

## AIOFileOpen

## Summary

Opens a local or cloud file handle that supports context manager protocol.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| mode | Specifies the mode that will be used for opening a file.r—The file will be opened in read mode.w—The file will be opened in write moderb—The file will be opened in binary format for reading.wb—The file will be opened in binary format for writingNote:Only read mode honors the encoding parameter.(The default value is 'r') | String |
| encoding | Specifies the encoding that will be used to open a file.utf-8—UTF-8 encoding will be used. This is the default.utf-16—UTF-16 encoding will be used. ascii—ASCII encoding will be used.(The default value is 'utf-8') | String |
| mime | The Multipurpose Internet Mail Extensions (MIME) headers. For faster creation and setting of metadata, set MIME headers when creating the file.(The default value is None) | Dictionary |

## Code Samples

### Example 1

```python
AIOFileOpen (path, {mode}, {encoding}, {mime})
```

### Example 2

```python
# For opening a file in the cloud store
with AIOFileOpen(r"C:\data\datacloud.acs\datafile.txt", 'r') as rcsfile:
    rcsfile.seek(5)
    rcsfile.tell()
    print(rcsfile.read(4))
```

### Example 3

```python
# For opening a file in the cloud store
with AIOFileOpen(r"C:\data\datacloud.acs\datafile.txt", 'r') as rcsfile:
    rcsfile.seek(5)
    rcsfile.tell()
    print(rcsfile.read(4))
```

### Example 4

```python
# For opening a local file
with AIOFileOpen(r"C:\data\datafile.txt", 'r') as rcsfile:
    rcsfile.seek(5)
    rcsfile.tell()
    print(rcsfile.read(4))
```

### Example 5

```python
# For opening a local file
with AIOFileOpen(r"C:\data\datafile.txt", 'r') as rcsfile:
    rcsfile.seek(5)
    rcsfile.tell()
    print(rcsfile.read(4))
```

---

## AlterAliasName

## Summary

Updates the alias name for a table or feature class.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| table | Input table or feature class. | String |
| alias | The new alias name. | String |

## Code Samples

### Example 1

```python
AlterAliasName (table, alias)
```

### Example 2

```python
import arcpy

arcpy.CreateTable_management('c:/city/Boston.gdb', 'SnowReport')
arcpy.AlterAliasName('c:/city/Boston.gdb/SnowReport', 'Snow Report')
```

### Example 3

```python
import arcpy

arcpy.CreateTable_management('c:/city/Boston.gdb', 'SnowReport')
arcpy.AlterAliasName('c:/city/Boston.gdb/SnowReport', 'Snow Report')
```

---

## ArcInfo Workstation Item properties

## Summary

The Describe function returns the following properties for ArcInfo Workstation INFO table items. ArcInfo Workstation items are accessed from the itemSet property of the ArcInfo Workstation INFO Table property group.

## Code Samples

### Example 1

```python
import arcpy

# Create a list of Describe objects from the ArcInfo Table.
#
descList = arcpy.Describe("C:/data/crimefreq").itemSet

# Print properties about each item in the itemSet
#
for item in descList:
    print(item.name)
    print("%-22s %s" % ("  Alternate name:", item.alternateName))
    print("%-22s %s" % ("  Is indexed:", item.isIndexed))
    print("%-22s %s" % ("  Is pseudo:", item.isPseudo))
    print("%-22s %s" % ("  Is redefined:", item.isRedefined))
    print("%-22s %s" % ("  Item type:", item.itemType))
    print("%-22s %s" % ("  Number of decimals:", item.numberDecimals))
    print("%-22s %s" % ("  Output width:", item.outputWidth))
    print("%-22s %s" % ("  Start position:", item.startPosition))
    print("%-22s %s" % ("  Width:", item.width))
```

### Example 2

```python
import arcpy

# Create a list of Describe objects from the ArcInfo Table.
#
descList = arcpy.Describe("C:/data/crimefreq").itemSet

# Print properties about each item in the itemSet
#
for item in descList:
    print(item.name)
    print("%-22s %s" % ("  Alternate name:", item.alternateName))
    print("%-22s %s" % ("  Is indexed:", item.isIndexed))
    print("%-22s %s" % ("  Is pseudo:", item.isPseudo))
    print("%-22s %s" % ("  Is redefined:", item.isRedefined))
    print("%-22s %s" % ("  Item type:", item.itemType))
    print("%-22s %s" % ("  Number of decimals:", item.numberDecimals))
    print("%-22s %s" % ("  Output width:", item.outputWidth))
    print("%-22s %s" % ("  Start position:", item.startPosition))
    print("%-22s %s" % ("  Width:", item.width))
```

---

## ArcInfo Workstation Table properties

## Summary

The Describe function returns the following properties for ArcInfo Workstation INFO tables. The Table and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the ArcInfo Table.
#
desc = arcpy.Describe("C:/data/crimefreq")

# Print a Table property from the ArcInfo Table.
#
#print "HasOID:       " + desc.hasOID
print("%-11s %s" % ("HasOID:", desc.hasOID))


# Get the itemSet from the ArcInfo Table and
# print the name and item type of each item.
#
iSet = desc.itemSet
for item in iSet:
    print("%-12s %s" % ("\nName:", item.name))
    print("%-11s %s" % ("Item type:", item.itemType))
```

### Example 2

```python
import arcpy

# Create a Describe object from the ArcInfo Table.
#
desc = arcpy.Describe("C:/data/crimefreq")

# Print a Table property from the ArcInfo Table.
#
#print "HasOID:       " + desc.hasOID
print("%-11s %s" % ("HasOID:", desc.hasOID))


# Get the itemSet from the ArcInfo Table and
# print the name and item type of each item.
#
iSet = desc.itemSet
for item in iSet:
    print("%-12s %s" % ("\nName:", item.name))
    print("%-11s %s" % ("Item type:", item.itemType))
```

---

## ArealUnitConversionFactor

## Summary

Returns the factor for converting an area measurement to a different areal unit.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| from_unit | The original or source areal unit.SquareKilometers—Square kilometersHectares—HectaresAres—AresSquareMeters—Square metersSquareDecimeters—Square decimetersSquareCentimeters—Square centimetersSquareMillimeters—Square millimetersSquareMilesInt—Square statute milesAcresInt—International acresSquareYardsInt—Square international yardsSquareFeetInt—Square international feetSquareInchesInt—Square international inchesSquareMilesUS—Square US survey milesAcresUS—Square US survey acresSquareYardsUS—Square US survey yardsSquareFeetUS—Square US survey feetSquareInchesUS—Square US survey inches | String |
| to_unit | The destination areal unit.SquareKilometers—Square kilometersHectares—HectaresAres—AresSquareMeters—Square metersSquareDecimeters—Square decimetersSquareCentimeters—Square centimetersSquareMillimeters—Square millimetersSquareMilesInt—Square statute milesAcresInt—International acresSquareYardsInt—Square international yardsSquareFeetInt—Square international feetSquareInchesInt—Square international inchesSquareMilesUS—Square US survey milesAcresUS—Square US survey acresSquareYardsUS—Square US survey yardsSquareFeetUS—Square US survey feetSquareInchesUS—Square US survey inches | String |

## Code Samples

### Example 1

```python
ArealUnitConversionFactor (from_unit, to_unit)
```

### Example 2

```python
import arcpy

# Convert an area of 10000 Hectares to SquareKilometers 
area = 10000 * arcpy.ArealUnitConversionFactor(from_unit="Hectares", to_unit="SquareKilometers")

print(area)  # This will print a value of 100.0
```

### Example 3

```python
import arcpy

# Convert an area of 10000 Hectares to SquareKilometers 
area = 10000 * arcpy.ArealUnitConversionFactor(from_unit="Hectares", to_unit="SquareKilometers")

print(area)  # This will print a value of 100.0
```

### Example 4

```python
import locale
import sys

area = arcpy.GetParameter(n)  # Update n to the parameter index

area_value, area_unit = area.split(" ")  # For example, "10 Acres"

# Convert the area into "SquareMeters" as needed later in this script
try:
    conv_factor = arcpy.ArealUnitConversionFactor(area_unit, "SquareMeters")
except ValueError as e:
    # If fails, the likely area; unit is "Unknown"
    # Add code to either deal with it or produce an appropriateerror  as shown below.
    arcpy.AddError(arcpy.GetIDMessage('Invalid areal unit type.))
    sys.exit()

# Apply the conv_factor to the supplied value
# locale.atof is required for locales that don't use a period as the separator
area_square_m = locale.atof(area_value) * conv_factor
```

### Example 5

```python
import locale
import sys

area = arcpy.GetParameter(n)  # Update n to the parameter index

area_value, area_unit = area.split(" ")  # For example, "10 Acres"

# Convert the area into "SquareMeters" as needed later in this script
try:
    conv_factor = arcpy.ArealUnitConversionFactor(area_unit, "SquareMeters")
except ValueError as e:
    # If fails, the likely area; unit is "Unknown"
    # Add code to either deal with it or produce an appropriateerror  as shown below.
    arcpy.AddError(arcpy.GetIDMessage('Invalid areal unit type.))
    sys.exit()

# Apply the conv_factor to the supplied value
# locale.atof is required for locales that don't use a period as the separator
area_square_m = locale.atof(area_value) * conv_factor
```

---

## AsShape

## Summary

Converts Esri JSON or GeoJSON geometry to ArcPy geometry, and Esri JSON feature sets to ArcPy feature sets. GeoJSON is a geospatial data interchange format for encoding geographic data structures.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| geojson_struct | The geojson_struct includes type and coordinates. The following strings are included for type: Point, LineString, Polygon, MultiPoint, and MultiLineString. | Dictionary |
| esri_json | Specifies whether the input JSON is evaluated as Esri JSON or GeoJSON. If True, the input is evaluated as Esri JSON. (The default value is False) | Boolean |

## Code Samples

### Example 1

```python
AsShape (geojson_struct, {esri_json})
```

### Example 2

```python
import arcpy
geojson_point = {"type": "Point", "coordinates": [5.0, 5.0]}
point = arcpy.AsShape(geojson_point)
```

### Example 3

```python
import arcpy
geojson_point = {"type": "Point", "coordinates": [5.0, 5.0]}
point = arcpy.AsShape(geojson_point)
```

### Example 4

```python
import arcpy

geojson_point = {
    "type": "Point", 
    "coordinates": [5.0, 5.0]}
point = arcpy.AsShape(geojson_point)
```

### Example 5

```python
import arcpy

geojson_point = {
    "type": "Point", 
    "coordinates": [5.0, 5.0]}
point = arcpy.AsShape(geojson_point)
```

### Example 6

```python
import arcpy

esri_json = {
    "x": -122.65,
    "y": 45.53,
    "spatialReference": {
        "wkid": 4326}}
# Set the second parameter to True to use an esri JSON
point = arcpy.AsShape(esri_json, True)
```

### Example 7

```python
import arcpy

esri_json = {
    "x": -122.65,
    "y": 45.53,
    "spatialReference": {
        "wkid": 4326}}
# Set the second parameter to True to use an esri JSON
point = arcpy.AsShape(esri_json, True)
```

### Example 8

```python
import arcpy

geojson_multipoint = {
    "type": "MultiPoint",
    "coordinates": [[5.0, 4.0], [8.0, 7.0]]}
multipoint = arcpy.AsShape(geojson_multipoint)
```

### Example 9

```python
import arcpy

geojson_multipoint = {
    "type": "MultiPoint",
    "coordinates": [[5.0, 4.0], [8.0, 7.0]]}
multipoint = arcpy.AsShape(geojson_multipoint)
```

### Example 10

```python
import arcpy

esri_json = {
    "points" : [
        [-97.06138, 32.837],
        [-97.06133, 32.836],
        [-97.06124, 32.834],
        [-97.06127, 32.832]],
    "spatialReference" : {"wkid" : 4326}}
# Set the second parameter to True to use an esri JSON
multipoint = arcpy.AsShape(esri_json, True)
```

### Example 11

```python
import arcpy

esri_json = {
    "points" : [
        [-97.06138, 32.837],
        [-97.06133, 32.836],
        [-97.06124, 32.834],
        [-97.06127, 32.832]],
    "spatialReference" : {"wkid" : 4326}}
# Set the second parameter to True to use an esri JSON
multipoint = arcpy.AsShape(esri_json, True)
```

### Example 12

```python
import arcpy

geojson_linestring = {
    "type": "LineString",
    "coordinates": [[5.0, 4.0], [8.0, 7.0]]}
polyline = arcpy.AsShape(geojson_linestring)
```

### Example 13

```python
import arcpy

geojson_linestring = {
    "type": "LineString",
    "coordinates": [[5.0, 4.0], [8.0, 7.0]]}
polyline = arcpy.AsShape(geojson_linestring)
```

### Example 14

```python
import arcpy

esri_json = {
    "paths" : [
        [[-97.08, 32.8], [-97.05, 32.6], [-97.06, 32.7],
         [-97.07, 32.6]],
        [[-97.4, 32.5], [-97.2, 32.75]]],
    "spatialReference" : {"wkid" : 4326}}
# Set the second parameter to True to use an esri JSON
polyline = arcpy.AsShape(esri_json, True)
```

### Example 15

```python
import arcpy

esri_json = {
    "paths" : [
        [[-97.08, 32.8], [-97.05, 32.6], [-97.06, 32.7],
         [-97.07, 32.6]],
        [[-97.4, 32.5], [-97.2, 32.75]]],
    "spatialReference" : {"wkid" : 4326}}
# Set the second parameter to True to use an esri JSON
polyline = arcpy.AsShape(esri_json, True)
```

### Example 16

```python
import arcpy

geojson_multilinestring = {
    "type": "MultiLineString",
    "coordinates": [
        [[5.0, 4.0], [8.0, 7.0]],
        [[4.0, 5.0], [7.0, 8.0]]]}
polyline = arcpy.AsShape(geojson_multilinestring)
```

### Example 17

```python
import arcpy

geojson_multilinestring = {
    "type": "MultiLineString",
    "coordinates": [
        [[5.0, 4.0], [8.0, 7.0]],
        [[4.0, 5.0], [7.0, 8.0]]]}
polyline = arcpy.AsShape(geojson_multilinestring)
```

### Example 18

```python
import arcpy

geojson_polygon = {
    "type": "Polygon",
    "coordinates": [
        [[10.0, 0.0], [20.0, 0.0], [20.0, 10.0], [10.0, 10.0],
         [10.0, 0.0]]]}
polygon = arcpy.AsShape(geojson_polygon)
```

### Example 19

```python
import arcpy

geojson_polygon = {
    "type": "Polygon",
    "coordinates": [
        [[10.0, 0.0], [20.0, 0.0], [20.0, 10.0], [10.0, 10.0],
         [10.0, 0.0]]]}
polygon = arcpy.AsShape(geojson_polygon)
```

### Example 20

```python
import arcpy

geojson_polygon = {
    "type": "Polygon",
    "coordinates": [
        [[10.0, 0.0], [20.0, 0.0], [20.0, 10.0], [10.0, 10.0],
         [10.0, 0.0]],
        [[12.0, 2.0], [18.0, 2.0], [18.0,  8.0], [12.0,  8.0],
         [12.0, 2.0]]]}
polygon = arcpy.AsShape(geojson_polygon)
```

### Example 21

```python
import arcpy

geojson_polygon = {
    "type": "Polygon",
    "coordinates": [
        [[10.0, 0.0], [20.0, 0.0], [20.0, 10.0], [10.0, 10.0],
         [10.0, 0.0]],
        [[12.0, 2.0], [18.0, 2.0], [18.0,  8.0], [12.0,  8.0],
         [12.0, 2.0]]]}
polygon = arcpy.AsShape(geojson_polygon)
```

---

## Assignment properties

## Summary

The properties below are returned by the assignments object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes

for na in netattrs:
    print(f"Name: {na.name}")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")

    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes

for na in netattrs:
    print(f"Name: {na.name}")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")

    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

---

## Association Source properties

## Summary

The following properties are supported by the associationSource object in a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Association source properties
asources = d.associationSource
print("Association Sources properties")
print(f"Name: {asources.name}")
print(f"ID: {asources.sourceID}")
print(f"Type: {asources.sourceType} \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Association source properties
asources = d.associationSource
print("Association Sources properties")
print(f"Name: {asources.name}")
print(f"ID: {asources.sourceID}")
print(f"Type: {asources.sourceType} \n")
```

---

## Attribute Rule properties

## Summary

The Describe function returns the properties described below for datasets that have attribute rules added to them.

## Code Samples

### Example 1

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.Building"

# Print a report of the attribute rule properties
attRules = arcpy.Describe(fc).attributeRules
print("- Attribute Rule Properties -")

for ar in attRules:    
    if "Calculation" in ar.type:       
        print("- Calculation Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Field: {ar.fieldName}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is editable: {ar.userEditable}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Evaluation order: {ar.evaluationOrder}")
        print(f" Exclude from client evaluation: {ar.excludeFromClientEvaluation}")
        print(f" Triggering events: {ar.triggeringEvents}")
        print(f" Triggering fields: {ar.triggeringfields}\n")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Is flagged as a batch rule: {ar.batch}\n")
        print(f" Severity: {ar.severity}\n")
        print(f" Tags: {ar.tags}\n")
        

    elif "Constraint" in ar.type:       
        print("- Constraint Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is editable: {ar.userEditable}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Error number: {ar.errorNumber}")
        print(f" Error message: {ar.errorMessage}")
        print(f" Exclude from client evaluation: {ar.excludeFromClientEvaluation}")
        print(f" Triggering events: {ar.triggeringEvents}")
        print(f" Triggering fields: {ar.triggeringfields}\n")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Tags: {ar.tags}\n")


    elif "Validation" in ar.type:       
        print("- Validation Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Error number: {ar.errorNumber}")
        print(f" Error message: {ar.errorMessage}")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Is flagged as a batch rule: {ar.batch}\n")
        print(f" Severity: {ar.severity}\n")
        print(f" Tags: {ar.tags}\n")
```

### Example 2

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.Building"

# Print a report of the attribute rule properties
attRules = arcpy.Describe(fc).attributeRules
print("- Attribute Rule Properties -")

for ar in attRules:    
    if "Calculation" in ar.type:       
        print("- Calculation Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Field: {ar.fieldName}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is editable: {ar.userEditable}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Evaluation order: {ar.evaluationOrder}")
        print(f" Exclude from client evaluation: {ar.excludeFromClientEvaluation}")
        print(f" Triggering events: {ar.triggeringEvents}")
        print(f" Triggering fields: {ar.triggeringfields}\n")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Is flagged as a batch rule: {ar.batch}\n")
        print(f" Severity: {ar.severity}\n")
        print(f" Tags: {ar.tags}\n")
        

    elif "Constraint" in ar.type:       
        print("- Constraint Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is editable: {ar.userEditable}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Error number: {ar.errorNumber}")
        print(f" Error message: {ar.errorMessage}")
        print(f" Exclude from client evaluation: {ar.excludeFromClientEvaluation}")
        print(f" Triggering events: {ar.triggeringEvents}")
        print(f" Triggering fields: {ar.triggeringfields}\n")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Tags: {ar.tags}\n")


    elif "Validation" in ar.type:       
        print("- Validation Rule:")
        print(f" Name: {ar.name}")
        print(f" Creation time: {ar.creationTime}")
        print(f" Subtype code: {ar.subtypeCode}")
        print(f" Description: {ar.description}")
        print(f" Is enabled: {ar.isEnabled}")
        print(f" Error number: {ar.errorNumber}")
        print(f" Error message: {ar.errorMessage}")
        print(f" Script expression: {ar.scriptExpression}\n")
        print(f" Is flagged as a batch rule: {ar.batch}\n")
        print(f" Severity: {ar.severity}\n")
        print(f" Tags: {ar.tags}\n")
```

### Example 3

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.FacilitySite"

# Print a report of the checkParameter properties
attRules = arcpy.da.Describe(fc)['attributeRules']
for rule in range(len(attRules)):
    for key, value in attRules[rule]['checkParameters'].items():
        print(f"{key}: {value}")
```

### Example 4

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.FacilitySite"

# Print a report of the checkParameter properties
attRules = arcpy.da.Describe(fc)['attributeRules']
for rule in range(len(attRules)):
    for key, value in attRules[rule]['checkParameters'].items():
        print(f"{key}: {value}")
```

---

## BIM File Workspace properties

## Summary

The Describe function returns the following properties for a BIM file workspace. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy 

# Create a describe object # 
desc = arcpy.Describe("C:/data/project.ifc")

# Print BIM file Workspace properties
print(f"Is a Revit file: {desc.isRevit}")
print(f"Is an IFC file:  {desc.isIFC}")
print(f"Building Name:   {desc.buildingName}")
print(f"Client's Name:   {desc.client}")
```

### Example 2

```python
import arcpy 

# Create a describe object # 
desc = arcpy.Describe("C:/data/project.ifc")

# Print BIM file Workspace properties
print(f"Is a Revit file: {desc.isRevit}")
print(f"Is an IFC file:  {desc.isIFC}")
print(f"Building Name:   {desc.buildingName}")
print(f"Client's Name:   {desc.client}")
```

---

## CAD Drawing Dataset properties

## Summary

The Describe function returns the following properties for CAD drawing datasets. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy 

# Create a describe object 
# 
desc = arcpy.Describe("C:/data/arch.dgn")

# Print Cad Drawing Dataset properties 
# 
print("%-12s %s" % ("is2D:", desc.is2D))
print("%-12s %s" % ("is3D:", desc.is3D))
print("%-12s %s" % ("isAutoCAD:", desc.isAutoCAD))
print("%-12s %s" % ("isDGN:", desc.isDGN))
```

### Example 2

```python
import arcpy 

# Create a describe object 
# 
desc = arcpy.Describe("C:/data/arch.dgn")

# Print Cad Drawing Dataset properties 
# 
print("%-12s %s" % ("is2D:", desc.is2D))
print("%-12s %s" % ("is3D:", desc.is3D))
print("%-12s %s" % ("isAutoCAD:", desc.isAutoCAD))
print("%-12s %s" % ("isDGN:", desc.isDGN))
```

---

## CAD Feature Class properties

## Summary

The Describe function returns the Feature Class, Table, and Dataset property groups for CAD feature classes.

---

## Parcel Fabric For ArcMap properties

## Summary

The Describe function returns the following properties for ArcMap parcel fabrics. The Dataset property group is also supported.

---

## Category properties

## Summary

The properties below are returned by the categories object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Categories properties
categories = d.categories
for cat in categories:
    print("*** - Categories properties - ***")
    print(f"Category creation time: {cat.creationTime}")
    print(f"Category Name: {cat.name} \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Categories properties
categories = d.categories
for cat in categories:
    print("*** - Categories properties - ***")
    print(f"Category creation time: {cat.creationTime}")
    print(f"Category Name: {cat.name} \n")
```

---

## CheckExtension

## Summary

Checks to see if a license is available to be checked out for a specific type of extension.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| extension_code | Keyword for the extension product that is being checked.3D—ArcGIS 3D Analyst extensionAeronautical—ArcGIS Aviation ChartingAirports—ArcGIS Aviation AirportsArcScan—ArcScanBathymetry—ArcGIS BathymetryBusinessPrem—ArcGIS Business AnalystDataReviewer—ArcGIS Data ReviewerDataInteroperability—ArcGIS Data Interoperability extension for DesktopDefense—ArcGIS Defense MappingFoundation—ArcGIS Production MappingGeoStats—ArcGIS Geostatistical Analyst extensionIndoors—ArcGIS IndoorsImageAnalyst—Image AnalystJTX—ArcGIS Workflow Manager (Classic) DesktopLocationReferencing—ArcGIS Pipeline Referencing or ArcGIS Roads and HighwaysLocateXT—LocateXTNautical—ArcGIS MaritimeNetwork—ArcGIS Network Analyst extensionPublisher—ArcGIS PublisherSchematics—ArcGIS Schematics extensionSMPAsiaPacific—StreetMap Premium Asia PacificSMPEurope—StreetMap Premium EuropeSMPJapan—StreetMap Premium JapanSMPLatinAmerica—StreetMap Premium Latin AmericaSMPMiddleEastAfrica—StreetMap Premium Middle East AfricaSMPNorthAmerica—StreetMap Premium North AmericaSpatial—ArcGIS Spatial Analyst extensionTracking—ArcGIS Tracking Analyst extension | String |

## Code Samples

### Example 1

```python
CheckExtension (extension_code)
```

### Example 2

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## CheckInExtension

## Summary

Returns the license to the License Manager so other applications can use it.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| extension_code | Keyword for the extension product that is being checked. 3D—ArcGIS 3D Analyst extensionAeronautical—ArcGIS Aviation ChartingAirports—ArcGIS Aviation AirportsArcScan—ArcScanBathymetry—ArcGIS BathymetryBusinessPrem—ArcGIS Business AnalystDataReviewer—ArcGIS Data ReviewerDataInteroperability—ArcGIS Data Interoperability extension for DesktopDefense—ArcGIS Defense MappingFoundation—ArcGIS Production MappingGeoStats—ArcGIS Geostatistical Analyst extensionIndoors—ArcGIS IndoorsImageAnalyst—Image AnalystJTX—ArcGIS Workflow Manager (Classic) DesktopLocationReferencing—ArcGIS Pipeline Referencing or ArcGIS Roads and HighwaysLocateXT—LocateXTNautical—ArcGIS MaritimeNetwork—ArcGIS Network Analyst extensionPublisher—ArcGIS PublisherSchematics—ArcGIS Schematics extensionSMPAsiaPacific—StreetMap Premium Asia PacificSMPEurope—StreetMap Premium EuropeSMPJapan—StreetMap Premium JapanSMPLatinAmerica—StreetMap Premium Latin AmericaSMPMiddleEastAfrica—StreetMap Premium Middle East AfricaSMPNorthAmerica—StreetMap Premium North AmericaSpatial—ArcGIS Spatial Analyst extensionTracking—ArcGIS Tracking Analyst extensionLicensing and extensions | String |

## Code Samples

### Example 1

```python
CheckInExtension (extension_code)
```

### Example 2

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## CheckOutExtension

## Summary

Retrieves the license from the License Manager.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| extension_code | Specifies the extension product to be checked.3D—ArcGIS 3D Analyst extensionAeronautical—ArcGIS Aviation ChartingAirports—ArcGIS Aviation AirportsArcScan—ArcScanBathymetry—ArcGIS BathymetryBusinessPrem—ArcGIS Business AnalystDataReviewer—ArcGIS Data ReviewerDataInteroperability—ArcGIS Data Interoperability extension for DesktopDefense—ArcGIS Defense MappingFoundation—ArcGIS Production MappingGeoStats—ArcGIS Geostatistical Analyst extensionIndoors—ArcGIS IndoorsImageAnalyst—Image AnalystJTX—ArcGIS Workflow Manager (Classic) DesktopLocationReferencing—ArcGIS Pipeline Referencing or ArcGIS Roads and HighwaysLocateXT—LocateXTNautical—ArcGIS MaritimeNetwork—ArcGIS Network Analyst extensionPublisher—ArcGIS PublisherSchematics—ArcGIS Schematics extensionSMPAsiaPacific—StreetMap Premium Asia PacificSMPEurope—StreetMap Premium EuropeSMPJapan—StreetMap Premium JapanSMPLatinAmerica—StreetMap Premium Latin AmericaSMPMiddleEastAfrica—StreetMap Premium Middle East AfricaSMPNorthAmerica—StreetMap Premium North AmericaSpatial—ArcGIS Spatial Analyst extensionTracking—ArcGIS Tracking Analyst extensionLearn more about accessing licenses and extensions in Python | String |

## Code Samples

### Example 1

```python
CheckOutExtension (extension_code)
```

### Example 2

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## CheckProduct

## Summary

Checks to see if the requested license is available.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| product | Product code for the product being checked.arcview—ArcGIS Desktop Basic product codearceditor—ArcGIS Desktop Standard product codearcinfo—ArcGIS Desktop Advanced product codeengine—Engine Runtime product codeenginegeodb—Engine Geodatabase Update product codearcserver— Server product code | String |

## Code Samples

### Example 1

```python
CheckProduct (product)
```

### Example 2

```python
import sys
import arcpy

arcpy.env.workspace = "c:/data/world.gdb"

if arcpy.CheckProduct("ArcInfo") == "Available":
    arcpy.PolygonToLine_management("Lakes", "LakeLines")
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
```

### Example 3

```python
import sys
import arcpy

arcpy.env.workspace = "c:/data/world.gdb"

if arcpy.CheckProduct("ArcInfo") == "Available":
    arcpy.PolygonToLine_management("Lakes", "LakeLines")
else:
    msg = 'ArcGIS for Desktop Advanced license not available'
    print(msg)
    sys.exit(msg)
```

---

## ClearCredentials

## Summary

Removes ArcGIS Server credential information from a client machine to disable access to secured services.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| connections[connections,...] | A list of dictionaries with key-value pairs of credential information obtained from the arcpy.ImportCredentials function. | Dictionary |

## Code Samples

### Example 1

```python
ClearCredentials (connections)
```

### Example 2

```python
import arcpy

# import credentials
secured_credentials = arcpy.ImportCredentials([r"C:\Project\SecuredServices.ags"])
aprx = arcpy.mp.ArcGISProject(r"C:\Project\USA.aprx")
m = aprx.listMaps()[0]

# add secured service to map
m.addDataFromPath('http://SampleServer:6080/arcgis/rest/services/secured/ProjectArea/FeatureServer/0')

# clear credentials when finished
arcpy.ClearCredentials(secured_credentials)
```

### Example 3

```python
import arcpy

# import credentials
secured_credentials = arcpy.ImportCredentials([r"C:\Project\SecuredServices.ags"])
aprx = arcpy.mp.ArcGISProject(r"C:\Project\USA.aprx")
m = aprx.listMaps()[0]

# add secured service to map
m.addDataFromPath('http://SampleServer:6080/arcgis/rest/services/secured/ProjectArea/FeatureServer/0')

# clear credentials when finished
arcpy.ClearCredentials(secured_credentials)
```

---

## ClearEnvironment

## Summary

Resets a specific environment setting to its default.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| environment_name | The name of the environment setting that will be reset to its default setting. | String |

## Code Samples

### Example 1

```python
ClearEnvironment (environment_name)
```

### Example 2

```python
import arcpy

arcpy.env.workspace = "c:/data/world.gdb"

# Prints c:/data/world.gdb
print(arcpy.env.workspace)

arcpy.ClearEnvironment("workspace")

# Prints None
print(arcpy.env.workspace)
```

### Example 3

```python
import arcpy

arcpy.env.workspace = "c:/data/world.gdb"

# Prints c:/data/world.gdb
print(arcpy.env.workspace)

arcpy.ClearEnvironment("workspace")

# Prints None
print(arcpy.env.workspace)
```

---

## Closest Facility Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the closest facility solver.

---

## Command

## Summary

Runs a geoprocessing tool as a single string.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| command_line | The double-quoted string representing the tool to be run. | String |

## Code Samples

### Example 1

```python
Command (command_line)
```

### Example 2

```python
import arcpy

# Set current workspace and define command line command.
arcpy.env.workspace = "c:/data/florida.gdb"
command_string = "Clip_analysis Runways DadeCounty DadeRunways"

# Run command line string
arcpy.Command(command_string)
```

### Example 3

```python
import arcpy

# Set current workspace and define command line command.
arcpy.env.workspace = "c:/data/florida.gdb"
command_string = "Clip_analysis Runways DadeCounty DadeRunways"

# Run command line string
arcpy.Command(command_string)
```

---

## Condition Barrier properties

## Summary

The properties below are returned by the conditionBarriers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Condition Barrier Properties
        print(" - Condition Barrier Properties - ")
        for cb in ust.conditionBarriers:
            try:
                print(f"Name: {cb.name} ")
                print(f"Type: {cb.type} ")
                print(f"Operator: {cb.operator} ")
                print(f"Value: {cb.value} ")
                print(f"CombineUsingOr: {cb.combineUsingOr}")
                print(f"Is Specific Value: {cb.isSpecificValue} \n")
            except:
                print("Skipped condition barrier properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Condition Barrier Properties
        print(" - Condition Barrier Properties - ")
        for cb in ust.conditionBarriers:
            try:
                print(f"Name: {cb.name} ")
                print(f"Type: {cb.type} ")
                print(f"Operator: {cb.operator} ")
                print(f"Value: {cb.value} ")
                print(f"CombineUsingOr: {cb.combineUsingOr}")
                print(f"Is Specific Value: {cb.isSpecificValue} \n")
            except:
                print("Skipped condition barrier properties. \n")
```

---

## Condition properties

## Summary

The properties below are returned by the conditions object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")
```

---

## Connectivity Policies

## Summary

Provides information about connectivity policies used by the edge sources and junction sources. The properties with a "X" in their names are dynamic properties. The possible values of "X" depend upon another property. For example, for a given edge source, connSubtypeX, and connPolicyX are dynamic properties where X indicates a particular subtype. The range of possible values for X depends on the subTypeConnCount property. So if an edge source has two subtypes, then it will support connSubtype0, connSubtype1, connPolicy0, and connPolicy1 properties.

## Code Samples

### Example 1

```python
# Name: NDSConnectivityPolicies_ex01.py
# Description: Prints out the connectivity policy information about the
#              edge sources for a given network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Edge sources")

# Get all the edge sources for the network dataset
edgeSources = desc.edgeSources

#If there are no edge sources, quit
if not edgeSources:
    print("%*s" % (justify, "(No edge sources)"))
    sys.exit(0)

for edgeSource in edgeSources:
    print(" %*s: %s" % (justify, "Source Name" , edgeSource.name))
    print(" %*s: %s" % (justify, "Source ID" , str(edgeSource.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", edgeSource.sourceType))
    print(" %*s: %s" % (justify, "Element Type", edgeSource.elementType))
    print(" %*s: %s" % (justify, "From Elevation Field",
                        edgeSource.fromElevationFieldName))
    print(" %*s: %s" % (justify, "To Elevation Field",
                        edgeSource.toElevationFieldName))
    # Get connectivity information
    conn = edgeSource.connectivityPolicies
    # Check if subtypes are used for edge sources to define connectivity groups
    #and policies
    bUseSubtypes = conn.usesSubtypes
    print(" %*s: %s" % (justify, "Connectivity defined by subtype?",
                        str(conn.usesSubtypes)))

    #Print connectivity policy information depending on the use of subtypes
    if not bUseSubtypes:
        print("%*s: %s" %(justify,"Connectivity Policy",conn.classConnectivity))
    else:
        # Connectivity policy by subtype
        print(" %*s: %s" % (justify, "Number of subtypes",
                            str(conn.subtypeConnCount)))
        for i in range(0, conn.subtypeConnCount):
            subtypeCode = getattr(conn, "connSubtype" + str(i))
            policy = getattr(conn, "connPolicy" + str(i))
            print(" %*s: %s" %(justify, "Subtype Code",subtypeCode))
            print(" %*s: %s" % (justify, "... has connectivity policy", policy))

    # Print connectivity Group information depending on the use of subtypes
    if not bUseSubtypes:
        print("%*s: %s" % (justify,"Belongs to Connectivity Group",
                           conn.defaultGroup))
    else:
        # Connectivity group by subtype
        print(" %*s: %s" %(justify,"Number of subtypes for connectivity groups",
                          conn.groupCount))
        for i in range(0, conn.groupCount):
            subtypeCode = getattr(conn, "groupSubtype" + str(i))
            name = getattr(conn, "groupName" + str(i))
            print( "%*s: %s" %(justify,"Subtype Code", subtypeCode))
            print("%*s: %s" %(justify,"... belongs to connectivity group",name))
    print(" ")
```

### Example 2

```python
# Name: NDSConnectivityPolicies_ex01.py
# Description: Prints out the connectivity policy information about the
#              edge sources for a given network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Edge sources")

# Get all the edge sources for the network dataset
edgeSources = desc.edgeSources

#If there are no edge sources, quit
if not edgeSources:
    print("%*s" % (justify, "(No edge sources)"))
    sys.exit(0)

for edgeSource in edgeSources:
    print(" %*s: %s" % (justify, "Source Name" , edgeSource.name))
    print(" %*s: %s" % (justify, "Source ID" , str(edgeSource.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", edgeSource.sourceType))
    print(" %*s: %s" % (justify, "Element Type", edgeSource.elementType))
    print(" %*s: %s" % (justify, "From Elevation Field",
                        edgeSource.fromElevationFieldName))
    print(" %*s: %s" % (justify, "To Elevation Field",
                        edgeSource.toElevationFieldName))
    # Get connectivity information
    conn = edgeSource.connectivityPolicies
    # Check if subtypes are used for edge sources to define connectivity groups
    #and policies
    bUseSubtypes = conn.usesSubtypes
    print(" %*s: %s" % (justify, "Connectivity defined by subtype?",
                        str(conn.usesSubtypes)))

    #Print connectivity policy information depending on the use of subtypes
    if not bUseSubtypes:
        print("%*s: %s" %(justify,"Connectivity Policy",conn.classConnectivity))
    else:
        # Connectivity policy by subtype
        print(" %*s: %s" % (justify, "Number of subtypes",
                            str(conn.subtypeConnCount)))
        for i in range(0, conn.subtypeConnCount):
            subtypeCode = getattr(conn, "connSubtype" + str(i))
            policy = getattr(conn, "connPolicy" + str(i))
            print(" %*s: %s" %(justify, "Subtype Code",subtypeCode))
            print(" %*s: %s" % (justify, "... has connectivity policy", policy))

    # Print connectivity Group information depending on the use of subtypes
    if not bUseSubtypes:
        print("%*s: %s" % (justify,"Belongs to Connectivity Group",
                           conn.defaultGroup))
    else:
        # Connectivity group by subtype
        print(" %*s: %s" %(justify,"Number of subtypes for connectivity groups",
                          conn.groupCount))
        for i in range(0, conn.groupCount):
            subtypeCode = getattr(conn, "groupSubtype" + str(i))
            name = getattr(conn, "groupName" + str(i))
            print( "%*s: %s" %(justify,"Subtype Code", subtypeCode))
            print("%*s: %s" %(justify,"... belongs to connectivity group",name))
    print(" ")
```

### Example 3

```python
# Name: NDSConnectivityPolicies_ex02.py
# Description: Prints out the connectivity policy information about the
#              junction sources for a given network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Junction sources")

#Get all the junction sources for the network dataset
junctions = desc.junctionSources

#If there are no junction sources, quit
if not junctions:
    print(" %*s" % (justify, "(No junction sources)"))
    sys.exit(0)

for junction in junctions:
    print(" %*s: %s" % (justify, "Source Name" , junction.name))
    print(" %*s: %s" % (justify, "Source ID" , str(junction.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", junction.sourceType))
    print(" %*s: %s" % (justify, "Element Type", junction.elementType))
    print(" %*s: %s" % (justify, "Elevation Field",
                        junction.elevationFieldName))

    # system junctions do not support connectivity information
    sourcetype = junction.sourceType
    if sourcetype.lower() != "junctionfeature":
        continue
    #Get the connectivity policies
    conn = junction.connectivityPolicies
    if not conn:
        continue
    # Connectivity can be defined based on subtypes
    bUseSubtypes = conn.usesSubtypes
    print(" %*s: %s" % (justify + 5, "Connectivity defined by subtype?" ,
                         str(conn.usesSubtypes)))
    if not bUseSubtypes:
        print(" %*s: %s" % (justify + 5, "Connectivity policy" ,
                            conn.classConnectivity))
        outtext = "Belongs to %d different connectivity groups" % conn.defaultGroupsCount
        print(" %*s" % (justify + 5, outtext))
        defgrouplist = []
        for i in range(0,conn.defaultGroupsCount):
            defgrouplist.append(str(getattr(conn, "defaultGroupName" + str(i))))
        print("%*s: %s" % (justify + 5,"... belongs to connectivity group(s)",
                           " ".join(defgrouplist)))
    else:
        print(" %*s: %s" % (justify + 5, "Number of subtypes" ,
                            str(conn.subtypeConnCount)))
        for i in range(0, conn.subtypeConnCount):
            st = getattr(conn, "connSubtype" + str(i))
            policy = getattr(conn,"connPolicy" + str(i))
            print(" ")
            print(" %*s: %s" % (justify + 10, "Subtype value" , st))
            print(" %*s: %s" % (justify + 10, "...has connectivity policy" ,
                                 policy))

        print("")
        for i in range(0, conn.subtypeGroupCount):
            stGroup = getattr(conn, "subtypeGroup" + str(i))
            print(" %*s: %d" % (justify + 10, "Subtype value", stGroup))
            count = getattr(conn, "subtype" + str(i) + "GroupsCount")
            grouplist = []
            for j in range(0, count):
                key = getattr(conn,"subtype%dGroupName%d" % (i,j))
                grouplist.append(str(key))
            print(" %*s %s" % (justify + 10, "...belongs to connectivity group(s)",
                               " ".join(grouplist)))

            print("")
    print(" ")
```

### Example 4

```python
# Name: NDSConnectivityPolicies_ex02.py
# Description: Prints out the connectivity policy information about the
#              junction sources for a given network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Junction sources")

#Get all the junction sources for the network dataset
junctions = desc.junctionSources

#If there are no junction sources, quit
if not junctions:
    print(" %*s" % (justify, "(No junction sources)"))
    sys.exit(0)

for junction in junctions:
    print(" %*s: %s" % (justify, "Source Name" , junction.name))
    print(" %*s: %s" % (justify, "Source ID" , str(junction.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", junction.sourceType))
    print(" %*s: %s" % (justify, "Element Type", junction.elementType))
    print(" %*s: %s" % (justify, "Elevation Field",
                        junction.elevationFieldName))

    # system junctions do not support connectivity information
    sourcetype = junction.sourceType
    if sourcetype.lower() != "junctionfeature":
        continue
    #Get the connectivity policies
    conn = junction.connectivityPolicies
    if not conn:
        continue
    # Connectivity can be defined based on subtypes
    bUseSubtypes = conn.usesSubtypes
    print(" %*s: %s" % (justify + 5, "Connectivity defined by subtype?" ,
                         str(conn.usesSubtypes)))
    if not bUseSubtypes:
        print(" %*s: %s" % (justify + 5, "Connectivity policy" ,
                            conn.classConnectivity))
        outtext = "Belongs to %d different connectivity groups" % conn.defaultGroupsCount
        print(" %*s" % (justify + 5, outtext))
        defgrouplist = []
        for i in range(0,conn.defaultGroupsCount):
            defgrouplist.append(str(getattr(conn, "defaultGroupName" + str(i))))
        print("%*s: %s" % (justify + 5,"... belongs to connectivity group(s)",
                           " ".join(defgrouplist)))
    else:
        print(" %*s: %s" % (justify + 5, "Number of subtypes" ,
                            str(conn.subtypeConnCount)))
        for i in range(0, conn.subtypeConnCount):
            st = getattr(conn, "connSubtype" + str(i))
            policy = getattr(conn,"connPolicy" + str(i))
            print(" ")
            print(" %*s: %s" % (justify + 10, "Subtype value" , st))
            print(" %*s: %s" % (justify + 10, "...has connectivity policy" ,
                                 policy))

        print("")
        for i in range(0, conn.subtypeGroupCount):
            stGroup = getattr(conn, "subtypeGroup" + str(i))
            print(" %*s: %d" % (justify + 10, "Subtype value", stGroup))
            count = getattr(conn, "subtype" + str(i) + "GroupsCount")
            grouplist = []
            for j in range(0, count):
                key = getattr(conn,"subtype%dGroupName%d" % (i,j))
                grouplist.append(str(key))
            print(" %*s %s" % (justify + 10, "...belongs to connectivity group(s)",
                               " ".join(grouplist)))

            print("")
    print(" ")
```

---

## CopyParameter

## Summary

Copies the specified parameter by index or parameter name to another parameter in the script tool. The specified parameters must be of the same data type.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| from_param | The index position of the parameter, or the name of the parameter to be copied. | Integer |
| to_param | The index position of the parameter, or the name of the parameter that will be copied to. | Integer |

## Code Samples

### Example 1

```python
CopyParameter (from_param, to_param)
```

### Example 2

```python
import arcpy

# Copy the script tool's specified input parameter object
# to the script tool's specified output parameter.
arcpy.CopyParameter(0, 1)
```

### Example 3

```python
import arcpy

# Copy the script tool's specified input parameter object
# to the script tool's specified output parameter.
arcpy.CopyParameter(0, 1)
```

### Example 4

```python
import arcpy

# Copy the script tool's specified input parameter object
# to the script tool's specified output parameter.
arcpy.CopyParameter("param_a", "param_b")
```

### Example 5

```python
import arcpy

# Copy the script tool's specified input parameter object
# to the script tool's specified output parameter.
arcpy.CopyParameter("param_a", "param_b")
```

---

## Coverage Feature Class properties

## Summary

The Describe function returns the following properties for coverage feature classes. The Feature Class, Table, and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create describe object from a coverage feature class
#
desc = arcpy.Describe("C:/data/tongass1/polygon")

# Print coverage feature class properties
#
print("%-17s %s" % ("featureClassType:", desc.featureClassType))
print("%-17s %s" % ("hasFAT:", desc.hasFAT))
print("%-17s %s" % ("topology:", desc.topology))
```

### Example 2

```python
import arcpy

# Create describe object from a coverage feature class
#
desc = arcpy.Describe("C:/data/tongass1/polygon")

# Print coverage feature class properties
#
print("%-17s %s" % ("featureClassType:", desc.featureClassType))
print("%-17s %s" % ("hasFAT:", desc.hasFAT))
print("%-17s %s" % ("topology:", desc.topology))
```

---

## Coverage properties

## Summary

The Describe function returns the following properties for coverages. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a describe object from a coverage
desc = arcpy.Describe("C:/data/tongass1")

# Get the tolerances property set from the describe object
tolProps = desc.tolerances

# Print all eight tolerance properties
print("Tolerances")
print("==========")
print("%-10s %s" % ("fuzzy:", tolProps.fuzzy))
print("%-10s %s" % ("dangle:", tolProps.dangle))
print("%-10s %s" % ("ticMatch:", tolProps.ticMatch))
print("%-10s %s" % ("edit:", tolProps.edit))
print("%-10s %s" % ("nodeSnap:", tolProps.nodeSnap))
print("%-10s %s" % ("weed:", tolProps.weed))
print("%-10s %s" % ("grain:", tolProps.grain))
print("%-10s %s" % ("snap:", tolProps.snap))
```

### Example 2

```python
import arcpy

# Create a describe object from a coverage
desc = arcpy.Describe("C:/data/tongass1")

# Get the tolerances property set from the describe object
tolProps = desc.tolerances

# Print all eight tolerance properties
print("Tolerances")
print("==========")
print("%-10s %s" % ("fuzzy:", tolProps.fuzzy))
print("%-10s %s" % ("dangle:", tolProps.dangle))
print("%-10s %s" % ("ticMatch:", tolProps.ticMatch))
print("%-10s %s" % ("edit:", tolProps.edit))
print("%-10s %s" % ("nodeSnap:", tolProps.nodeSnap))
print("%-10s %s" % ("weed:", tolProps.weed))
print("%-10s %s" % ("grain:", tolProps.grain))
print("%-10s %s" % ("snap:", tolProps.snap))
```

---

## CreateGeocodeSDDraft

## Summary

Converts a locator to a Service Definition Draft file (.sddraft) that can be used to create a service definition for publishing a geocode service.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| loc_path | The catalog path to the locator files (.loc) in a file folder. | String |
| out_sddraft | The path and file name for the output Service Definition Draft file (.sddraft). | String |
| service_name | The name of the service. This is the name people will see and use to identify the service. The name can only contain alphanumeric characters and underscores. No spaces or special characters are allowed. The name cannot be more than 120 characters. | String |
| server_type | The server type. If a connection_file_path parameter value is not supplied, a server_type value must be provided. If a connection_file_path parameter value is supplied, the server_type value is taken from the connection file. In this case, you can choose FROM_CONNECTION_FILE or skip the parameter entirely.ARCGIS_SERVER—The ArcGIS Server server type.FROM_CONNECTION_FILE—Get the server_type value as specified by the connection_file_path parameter.(The default value is ARCGIS_SERVER) | String |
| connection_file_path | The path and file name to an ArcGIS Server connection file (.ags).To publish a geocoding service in ArcGIS Pro, you will need an .ags file that has been created with publisher or administrator credentials for ArcGIS Server 10.6 or later. You can create a connection file using ArcGIS Pro and use the path to that file when publishing in ArcGIS Pro. | String |
| copy_data_to_server | A Boolean that indicates whether the data referenced in the locator will be copied to the server. The copy_data_to_server parameter is only used if the server_type value is ARCGIS_SERVER and the connection_file_path value is not specified. If the connection_file_path value is specified, the server's registered data stores are used. For example, if the data in the locator is registered with the server, copy_data_to_server will always be False. Conversely, if the data in the locator is not registered with the server, copy_data_to_server will always be True.False—The data will not be copied to the server. This is the default.True—The data will be copied to the server.(The default value is False) | Boolean |
| folder_name | The folder name where the service definition will be published. If the folder does not exist, it will be created when the service definition is published as a service. The default folder is the server root level.(The default value is None) | String |
| summary | The Item Description Summary. Use this parameter to override the user interface summary or to provide a summary if one does not exist.(The default value is None) | String |
| tags | The Item Description Tags. Use this parameter to override the user interface tags or to provide tags if they do not exist. To specify multiple tags, separate each tag with a comma in the string.(The default value is None) | String |
| max_result_size | The maximum number of candidates returned by the service when geocoding a single address.(The default value is 500) | Integer |
| max_batch_size | The maximum number of records to be processed in each batch job when performing batch geocoding.(The default value is 1000) | Integer |
| suggested_batch_size | The recommended number of records to pass in each batch job when performing batch geocoding.(The default value is 1000) | Integer |
| supported_operations[supported_operations,...] | The built-in operations that will be supported by the service. The parameter should be specified as a list containing one or more of the following string keywords:GEOCODE—The service will allow geocoding operations.REVERSE_GEOCODE—The service will allow reverse geocoding operations.SUGGEST—The service will allow suggest operations.For example, to specify that the service will only support geocoding operations and will not allow reverse geocoding operations, specify the parameter as ["GEOCODE"].(The default value is [GEOCODE, REVERSE_GEOCODE, SUGGEST]) | String |
| overwrite_existing_service | Specifies whether an existing service on the server will be overwritten by a new service with the same service_name value. If the service_name value is unique, this parameter is not applicable. | Boolean |

## Code Samples

### Example 1

```python
CreateGeocodeSDDraft (loc_path, out_sddraft, service_name, {server_type}, {connection_file_path}, {copy_data_to_server}, {folder_name}, {summary}, {tags}, {max_result_size}, {max_batch_size}, {suggested_batch_size}, {supported_operations}, {overwrite_existing_service})
```

### Example 2

```python
import arcpy
import pprint

# Overwrite any existing outputs
arcpy.env.overwriteOutput = True

locator_path = "C:\\Data\\Locators\\Atlanta"
sddraft_file = "C:\\Output\\Atlanta.sddraft"
sd_file = "C:\\Output\\Atlanta.sd"
service_name = "Atlanta"
summary = "Address locator for the city of Atlanta"
tags = "address, locator, geocode"
# Create an AGS connection file to your standalone server
# in ArcGIS Pro
gis_server_connection_file = "C:\\Data\\server_connection"

# Create the sd draft file
analyze_messages = arcpy.CreateGeocodeSDDraft(locator_path, sddraft_file, service_name,
                        connection_file_path=gis_server_connection_file, 
                        copy_data_to_server=True,
                        summary=summary, tags=tags, max_result_size=20,
                        max_batch_size=500, suggested_batch_size=150, 
                        overwrite_existing_service=False)

# Stage and upload the service if the sddraft analysis did not contain errors
if analyze_messages['errors'] == {}:
    try:
        # Execute StageService to convert sddraft file to a service definition 
        # (sd) file 
        arcpy.server.StageService(sddraft_file, sd_file)

        # Execute UploadServiceDefinition to publish the service definition 
        # file as a service
        arcpy.server.UploadServiceDefinition(sd_file, gis_server_connection_file)
        print("The geocode service was successfully published")
    except arcpy.ExecuteError:
        print("An error occurred")
        print(arcpy.GetMessages(2))
else: 
    # If the sddraft analysis contained errors, display them
    print("Error were returned when creating service definition draft")
    pprint.pprint(analyze_messages['errors'], indent=2)
```

### Example 3

```python
import arcpy
import pprint

# Overwrite any existing outputs
arcpy.env.overwriteOutput = True

locator_path = "C:\\Data\\Locators\\Atlanta"
sddraft_file = "C:\\Output\\Atlanta.sddraft"
sd_file = "C:\\Output\\Atlanta.sd"
service_name = "Atlanta"
summary = "Address locator for the city of Atlanta"
tags = "address, locator, geocode"
# Create an AGS connection file to your standalone server
# in ArcGIS Pro
gis_server_connection_file = "C:\\Data\\server_connection"

# Create the sd draft file
analyze_messages = arcpy.CreateGeocodeSDDraft(locator_path, sddraft_file, service_name,
                        connection_file_path=gis_server_connection_file, 
                        copy_data_to_server=True,
                        summary=summary, tags=tags, max_result_size=20,
                        max_batch_size=500, suggested_batch_size=150, 
                        overwrite_existing_service=False)

# Stage and upload the service if the sddraft analysis did not contain errors
if analyze_messages['errors'] == {}:
    try:
        # Execute StageService to convert sddraft file to a service definition 
        # (sd) file 
        arcpy.server.StageService(sddraft_file, sd_file)

        # Execute UploadServiceDefinition to publish the service definition 
        # file as a service
        arcpy.server.UploadServiceDefinition(sd_file, gis_server_connection_file)
        print("The geocode service was successfully published")
    except arcpy.ExecuteError:
        print("An error occurred")
        print(arcpy.GetMessages(2))
else: 
    # If the sddraft analysis contained errors, display them
    print("Error were returned when creating service definition draft")
    pprint.pprint(analyze_messages['errors'], indent=2)
```

### Example 4

```python
import arcpy
import pprint

# Overwrite any existing outputs
arcpy.env.overwriteOutput = True

locator_path = "C:\\Data\\Locators\\Atlanta"
sddraft_file = "C:\\Output\\Atlanta.sddraft"
sd_file = "C:\\Output\\Atlanta.sd"
service_name = "Atlanta"
summary = "Address locator for the city of Atlanta"
tags = "address, locator, geocode"

# The URL of the federated server you are publishing to
in_server = "https://machinename.domainname.com/server"

# Create the sd draft file
analyze_messages = arcpy.CreateGeocodeSDDraft(locator_path, sddraft_file, service_name,
                        copy_data_to_server=True,
                        summary=summary, tags=tags, max_result_size=20,
                        max_batch_size=500, suggested_batch_size=150, 
                        overwrite_existing_service=False)

# Stage and upload the service if the sddraft analysis did not contain errors
if analyze_messages['errors'] == {}:
    try:
        # Execute StageService to convert sddraft file to a service definition 
        # (sd) file 
        arcpy.server.StageService(sddraft_file, sd_file)

        # Execute UploadServiceDefinition to publish the service definition 
        # file as a service
        arcpy.server.UploadServiceDefinition(sd_file, in_server)
        print("The geocode service was successfully published")
    except arcpy.ExecuteError:
        print("An error occurred")
        print(arcpy.GetMessages(2))
else: 
    # If the sddraft analysis contained errors, display them
    print("Error were returned when creating service definition draft")
    pprint.pprint(analyze_messages['errors'], indent=2)
```

### Example 5

```python
import arcpy
import pprint

# Overwrite any existing outputs
arcpy.env.overwriteOutput = True

locator_path = "C:\\Data\\Locators\\Atlanta"
sddraft_file = "C:\\Output\\Atlanta.sddraft"
sd_file = "C:\\Output\\Atlanta.sd"
service_name = "Atlanta"
summary = "Address locator for the city of Atlanta"
tags = "address, locator, geocode"

# The URL of the federated server you are publishing to
in_server = "https://machinename.domainname.com/server"

# Create the sd draft file
analyze_messages = arcpy.CreateGeocodeSDDraft(locator_path, sddraft_file, service_name,
                        copy_data_to_server=True,
                        summary=summary, tags=tags, max_result_size=20,
                        max_batch_size=500, suggested_batch_size=150, 
                        overwrite_existing_service=False)

# Stage and upload the service if the sddraft analysis did not contain errors
if analyze_messages['errors'] == {}:
    try:
        # Execute StageService to convert sddraft file to a service definition 
        # (sd) file 
        arcpy.server.StageService(sddraft_file, sd_file)

        # Execute UploadServiceDefinition to publish the service definition 
        # file as a service
        arcpy.server.UploadServiceDefinition(sd_file, in_server)
        print("The geocode service was successfully published")
    except arcpy.ExecuteError:
        print("An error occurred")
        print(arcpy.GetMessages(2))
else: 
    # If the sddraft analysis contained errors, display them
    print("Error were returned when creating service definition draft")
    pprint.pprint(analyze_messages['errors'], indent=2)
```

---

## CreateGPSDDraft

## Summary

Converts Result objects and result files (.rlt) to a service definition draft file (.sddraft).

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| result[result,...] | One or multiple Result objects or result files (.rlt). Multiple results must be supplied in a list format. The following example demonstrates multiple results as input to the CreateGPSDDraft function: import arcpy result1 = arcpy.analysis.Buffer("inPts", "output.shp", "100 Meters") result2 = arcpy.management.GetCount("FireStations") arcpy.CreateGPSDDraft([result1, result2], "output.sddraft", "myservice") | Result |
| out_sddraft | The path and file name for the output .sddraft file. | String |
| service_name | The name of the service. This is the name people will see and use to identify the service. The name can only contain alphanumeric characters and underscores. No spaces or special characters are allowed. The name cannot be more than 120 characters. | String |
| server_type | Specifies the server type. If a connection_file_path parameter value is not provided, a server_type value must be specified. If a connection_file_path parameter value is provided, the server_type value is taken from the connection file. In this case, you can specify FROM_CONNECTION_FILE or skip the parameter.Note:MY_HOSTED_SERVICES is only available when creating .sddraft files from ArcGIS Pro.ARCGIS_SERVER—The ArcGIS Server server type. This is the default.FROM_CONNECTION_FILE—The connection_file_path parameter value will be used.MY_HOSTED_SERVICES—An .sddraft file is created that will be published to the current portal.(The default value is ARCGIS_SERVER) | String |
| connection_file_path | The path and file name to the ArcGIS Server connection file (.ags). | String |
| copy_data_to_server | Specifies whether the data referenced in the result parameter will be copied to the server. This parameter is only used if the server_type value is ARCGIS_SERVER and the connection_file_path value isn't provided. If the connection_file_path value is provided, the server's registered data stores will be used. For example, if the data in the result parameter is registered with the server, copy_data_to_server will always be False. Conversely, if the data in the result parameter is not registered with the server, copy_data_to_server will always be True.False—The data will not be copied to the server. This is the default.True—The data will be copied to the server.(The default value is False) | Boolean |
| folder_name | The folder name where the service definition will be published. If the folder does not exist, it will be created. The default folder is the server root level. (The default value is None) | String |
| summary | The Item Description Summary text. Use this parameter to override the user interface summary or to provide a summary if one does not exist. The summary provided here will not be persisted in the map document.(The default value is None) | String |
| tags | The Item Description tags. Use this parameter to override the user interface tags or to provide tags if they do not exist. The tags provided here will not be persisted in the map document.(The default value is None) | String |
| executionType | Asynchronous and synchronous define how the client (the application using the task) interacts with the server and gets the result from the task. When a service is set to synchronous, the client waits for the task to finish. Typically, a synchronous task executes quickly—five seconds or less. An asynchronous task typically takes longer to execute, and the client must periodically ask the server if the task has finished and, if it has finished, get the result. A web application using an asynchronous task must have logic implemented to check the status of a task and handle the result once execution is finished. ArcGIS Desktop clients handle both execution types natively.(The default value is Asynchronous) | String |
| resultMapServer | Specifies whether the result of all tasks will be visualized with the service as a map (in addition to other results of the task) when publishing a geoprocessing service. The map is created on the server using a map service for transport back to the client as an image (a .jpeg file, for example). The symbology, labeling, transparency, and all other properties of the returned map are the same as the settings of the output layer. If you are creating result layers in the Python scripting environment (outside ArcGIS Pro), default symbology will be used. To maintain control over symbology, create the layer files with symbology and use them to modify the output symbology of the task.When True, a map service is automatically created on the server with the same name as the geoprocessing service. The default is False.(The default value is False) | Boolean |
| showMessages | Specifies the message level that will be used for the geoprocessing service. The following are the valid message levels the service will return to the client:None—No geoprocessing messages will be returned to the client except those stating whether the process succeeded or failed. This is the default.Error—Only tool messages that produce an error will be returned to the client. Warning—All tool error and warning messages will be returned to the client. Info—All tool messages from processing will be returned to the client. (The default value is None) | String |
| maximumRecords | The maximum number of results the service can return to a client. Setting this value to a large number means your GIS server can handle sending a lot of individual records or features to the client. If you don't want to return any features, set this value to 0 (zero). Typically, you set this value to zero only when you enable View result with a map service. (The default value is 1000) | Integer |
| minInstances | The minimum number of instances a service will start and make available for use. For heavily used services, you can increase this value.(The default value is 1) | Integer |
| maxInstances | The maximum number of instances a service can start and make available for use. For heavily used services, you can increase this value. Ensure that the server has adequate hardware to support the maximum number of instances indicated.(The default value is 2) | Integer |
| maxUsageTime | The maximum time, in seconds, that a service can be used. You may need to increase the default of 600 seconds (10 minutes) for long-running geoprocessing tasks. Alternatively, you may need to reduce this time to ensure a client will not abuse your services.(The default value is 600) | Integer |
| maxWaitTime | The maximum time, in seconds, that a client will wait to connect with an instance before timing out. When all instances are busy processing requests, subsequent requests are queued. If this time-out elapses before an instance becomes available, the task will fail. The default is 60 seconds (1 minute).(The default value is 60) | Integer |
| maxIdleTime | The maximum time, in seconds, that an instance will continue to be active before pool shrinking occurs. Any instances above the minimum number of instances that have not been used will be shut down once the idle maximum time value has elapsed.(The default value is 1800) | Integer |
| capabilities | Specifies the capabilities a service will support. Currently, only Uploads is supported.(The default value is None) | String |
| constantValues[constantValues,...] | A list of parameter names to be set as a constant. If multiple tools are included, parameter names must be qualified with the tool name, for example, ["toolX.parameterA", "toolY.parameterD"].(The default value is None) | String |
| choiceLists | Constrains values for any input parameter with a choice list input mode in the web tool or geoprocessing service.The choice list and its values must be created before using this property; you cannot use this property to add new values to the choice list. If you have a feature or raster input, you must create the layer for each value in the choice list first and use this property to constrain. The property uses a dictionary with the service task and parameter name as the key, and a list of the string values as the value, for example, {"ServiceTaskName.parameterName":["string1", "string2"]}.(The default value is None) | Dictionary |

## Code Samples

### Example 1

```python
import arcpy
result = arcpy.Buffer_analysis("inPts", "output.shp", "100 Meters")
```

### Example 2

```python
import arcpy
result = arcpy.Buffer_analysis("inPts", "output.shp", "100 Meters")
```

### Example 3

```python
CreateGPSDDraft (result, out_sddraft, service_name, {server_type}, {connection_file_path}, {copy_data_to_server}, {folder_name}, {summary}, {tags}, {executionType}, {resultMapServer}, {showMessages}, {maximumRecords}, {minInstances}, {maxInstances}, {maxUsageTime}, {maxWaitTime}, {maxIdleTime}, {capabilities}, {constantValues}, {choiceLists})
```

### Example 4

```python
import arcpy
result1 = arcpy.analysis.Buffer("inPts", "output.shp", "100 Meters")
result2 = arcpy.management.GetCount("FireStations")
arcpy.CreateGPSDDraft([result1, result2], "output.sddraft", "myservice")
```

### Example 5

```python
import arcpy
result1 = arcpy.analysis.Buffer("inPts", "output.shp", "100 Meters")
result2 = arcpy.management.GetCount("FireStations")
arcpy.CreateGPSDDraft([result1, result2], "output.sddraft", "myservice")
```

### Example 6

```python
import arcpy

toolbox = "c:/gis/gp/MyAnalysisTools.tbx"
sddraft = "c:/gis/gp/drafts/AnalysisReport.sddraft"
sd = "c:/gis/gp/sd/AnalysisReport.sd"
portalurl = "https://myportal.esri.com/portal"
portalusername = "username"
portalpassword = "password"
serverURL = "https://myserver.esri.com/server"
serviceName = "AnalysisReportService"

# Run the tool and set to a result object
arcpy.ImportToolbox(toolbox)
result = arcpy.reports.MyCustomAnalysis("c:/gis/data/parcels.gdb/taxlots",
                                        "40", "MyOutput.pdf")

# Sign in to Portal
arcpy.SignInToPortal(portalurl, portalusername, portalpassword)

# Create service definition draft and return analyzer messages
analyzeMessages = arcpy.CreateGPSDDraft(
    result, sddraft, serviceName, server_type="MY_HOSTED_SERVICES",
    copy_data_to_server=True, folder_name=None, 
    summary="Analysis Service", tags="gp", executionType="Synchronous",
    resultMapServer=False, showMessages="Info", maximumRecords=5000,
    minInstances=2, maxInstances=3, maxUsageTime=100, maxWaitTime=10,
    maxIdleTime=180)

# Stage and upload the service if the sddraft analysis did not
# contain errors
if analyzeMessages['errors'] == {}:
    # The following runs StageService for ArcGIS 11 Enterprise. If you're using version
    # 10.9.1 or earlier, you must provide the staging version. For example, 
    # the staging version for 10.9.1 server is 209.   
    arcpy.server.StageService(sddraft, sd)

    # Run UploadServiceDefinition
    # Use URL to a federated server
    arcpy.server.UploadServiceDefinition(sd, serverURL)
else:
    # If the sddraft analysis contained errors, display them
    print(analyzeMessages['errors'])
```

### Example 7

```python
import arcpy

toolbox = "c:/gis/gp/MyAnalysisTools.tbx"
sddraft = "c:/gis/gp/drafts/AnalysisReport.sddraft"
sd = "c:/gis/gp/sd/AnalysisReport.sd"
portalurl = "https://myportal.esri.com/portal"
portalusername = "username"
portalpassword = "password"
serverURL = "https://myserver.esri.com/server"
serviceName = "AnalysisReportService"

# Run the tool and set to a result object
arcpy.ImportToolbox(toolbox)
result = arcpy.reports.MyCustomAnalysis("c:/gis/data/parcels.gdb/taxlots",
                                        "40", "MyOutput.pdf")

# Sign in to Portal
arcpy.SignInToPortal(portalurl, portalusername, portalpassword)

# Create service definition draft and return analyzer messages
analyzeMessages = arcpy.CreateGPSDDraft(
    result, sddraft, serviceName, server_type="MY_HOSTED_SERVICES",
    copy_data_to_server=True, folder_name=None, 
    summary="Analysis Service", tags="gp", executionType="Synchronous",
    resultMapServer=False, showMessages="Info", maximumRecords=5000,
    minInstances=2, maxInstances=3, maxUsageTime=100, maxWaitTime=10,
    maxIdleTime=180)

# Stage and upload the service if the sddraft analysis did not
# contain errors
if analyzeMessages['errors'] == {}:
    # The following runs StageService for ArcGIS 11 Enterprise. If you're using version
    # 10.9.1 or earlier, you must provide the staging version. For example, 
    # the staging version for 10.9.1 server is 209.   
    arcpy.server.StageService(sddraft, sd)

    # Run UploadServiceDefinition
    # Use URL to a federated server
    arcpy.server.UploadServiceDefinition(sd, serverURL)
else:
    # If the sddraft analysis contained errors, display them
    print(analyzeMessages['errors'])
```

### Example 8

```python
import arcpy

toolbox = "c:/gis/gp/MyAnalysisTools.tbx"
sddraft = "c:/gis/gp/drafts/AnalysisReport.sddraft"
sd = "c:/gis/gp/sd/AnalysisReport.sd"

serverconnectionfile = "c:/gis/gp/myserver.ags"
serviceName = "AnalysisReportService"

# Run the tool and set to a result object
arcpy.ImportToolbox(toolbox)
result = arcpy.reports.MyCustomAnalysis("c:/gis/data/parcels.gdb/taxlots",
                                        "40", "MyOutput.pdf")

# Create service definition draft and returns analyzer messages
analyzeMessages = arcpy.CreateGPSDDraft(
    result, sddraft, serviceName, server_type="MY_HOSTED_SERVICES",  
    connection_file_path= serverconnectionfile,
    copy_data_to_server=True, folder_name=None, 
    summary="Analysis Service", tags="gp", executionType="Synchronous",
    resultMapServer=False, showMessages="Info", maximumRecords=5000,
    minInstances=2, maxInstances=3, maxUsageTime=100, maxWaitTime=10,
    maxIdleTime=180)

# Stage and upload the service if the sddraft analysis did not
# contain errors
if analyzeMessages['errors'] == {}:
    # The following runs StageService for ArcGIS 11 server. If you're using version 10.9.1 
    # or earlier, you must provide the staging version. For example, the staging 
    # version for 10.9.1 server is 209. 
    arcpy.server.StageService(sddraft, sd)

    # Run UploadServiceDefinition
    # Use URL to a federated server 
    arcpy.server.UploadServiceDefinition(sd, serverconnectionfile)
else:
    # If the sddraft analysis contained errors, display them
    print(analyzeMessages['errors'])
```

### Example 9

```python
import arcpy

toolbox = "c:/gis/gp/MyAnalysisTools.tbx"
sddraft = "c:/gis/gp/drafts/AnalysisReport.sddraft"
sd = "c:/gis/gp/sd/AnalysisReport.sd"

serverconnectionfile = "c:/gis/gp/myserver.ags"
serviceName = "AnalysisReportService"

# Run the tool and set to a result object
arcpy.ImportToolbox(toolbox)
result = arcpy.reports.MyCustomAnalysis("c:/gis/data/parcels.gdb/taxlots",
                                        "40", "MyOutput.pdf")

# Create service definition draft and returns analyzer messages
analyzeMessages = arcpy.CreateGPSDDraft(
    result, sddraft, serviceName, server_type="MY_HOSTED_SERVICES",  
    connection_file_path= serverconnectionfile,
    copy_data_to_server=True, folder_name=None, 
    summary="Analysis Service", tags="gp", executionType="Synchronous",
    resultMapServer=False, showMessages="Info", maximumRecords=5000,
    minInstances=2, maxInstances=3, maxUsageTime=100, maxWaitTime=10,
    maxIdleTime=180)

# Stage and upload the service if the sddraft analysis did not
# contain errors
if analyzeMessages['errors'] == {}:
    # The following runs StageService for ArcGIS 11 server. If you're using version 10.9.1 
    # or earlier, you must provide the staging version. For example, the staging 
    # version for 10.9.1 server is 209. 
    arcpy.server.StageService(sddraft, sd)

    # Run UploadServiceDefinition
    # Use URL to a federated server 
    arcpy.server.UploadServiceDefinition(sd, serverconnectionfile)
else:
    # If the sddraft analysis contained errors, display them
    print(analyzeMessages['errors'])
```

---

## CreateImageSDDraft

## Summary

Converts a raster or mosaic dataset to a Service Definition Draft file (.sddraft).

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| raster_or_mosaic_layer | The raster layer or mosaic layer that will be published. | String |
| out_sddraft | A string that represents the path and file name for the output Service Definition Draft file (.sddraft). | String |
| service_name | A string that represents the name of the service. This is the name people will see and use to identify the service. The name can only contain alphanumeric characters and underscores. No spaces or special characters are allowed. The name cannot be more than 120 characters. | String |
| server_type | A string representing the server type. If a connection_file_path parameter value is not supplied, a server_type value must be provided. If a connection_file_path parameter value is supplied, the server_type value is taken from the connection file. In this case, you can choose FROM_CONNECTION_FILE or skip the parameter entirely.ARCGIS_SERVER—The ArcGIS Server server type.FROM_CONNECTION_FILE—Get the server_type value as specified by the connection_file_path parameter. (The default value is ARCGIS_SERVER) | String |
| connection_file_path | A string that represents the path and file name to the ArcGIS Server connection file (.ags).(The default value is None) | String |
| copy_data_to_server | A Boolean that indicates whether the source data referenced by the mosaic dataset, the mosaic dataset itself, or the raster dataset published as an image service will be copied to the server.The copy_data_to_server parameter is only used if the server_type value is ARCGIS_SERVER and the connection_file_path value isn't specified. If the connection_file_path value is specified, the server's registered data stores are used. For example, if the workspace that contains the source data referenced by the mosaic dataset—the mosaic dataset or raster dataset is registered with the server—copy_data_to_server will always be False. Conversely, if the workspace that contains the source data referenced by the mosaic dataset—the mosaic dataset or raster dataset is not registered with the server—copy_data_to_server will always be True.False—The data will not be copied to the server. This is the default.True—The data will be copied to the server.(The default value is False) | Boolean |
| folder_name | A string that represents the folder name where the service definition will be published. If the folder does not exist, it will be created. The default folder is the server root level. (The default value is None) | String |
| summary | A string that represents the Item Description Summary.Use this parameter to override the user interface summary or to provide a summary if one does not exist.(The default value is None) | String |
| tags | A string that represents the Item Description Tags.Use this parameter to override the user interface tags or to provide tags if they do not exist.(The default value is None) | String |

## Code Samples

### Example 1

```python
CreateImageSDDraft (raster_or_mosaic_layer, out_sddraft, service_name, {server_type}, {connection_file_path}, {copy_data_to_server}, {folder_name}, {summary}, {tags})
```

### Example 2

```python
import arcpy

ws = "C:/workspace"
mdpath = os.path.join(ws, "fgdb.gdb/mdDEM")      
con = os.path.join(ws, "myserver_6080 (publisher).ags")
service = 'dem_service'
sddraft = os.path.join(ws, service + '.sddraft')

arcpy.CreateImageSDDraft(mdpath, sddraft, service, 'ARCGIS_SERVER', 
                         con, True, None, "Publish las MD", 
                         "las,image service")
```

### Example 3

```python
import arcpy

ws = "C:/workspace"
mdpath = os.path.join(ws, "fgdb.gdb/mdDEM")      
con = os.path.join(ws, "myserver_6080 (publisher).ags")
service = 'dem_service'
sddraft = os.path.join(ws, service + '.sddraft')

arcpy.CreateImageSDDraft(mdpath, sddraft, service, 'ARCGIS_SERVER', 
                         con, True, None, "Publish las MD", 
                         "las,image service")
```

---

## CreateObject

## Summary

Creates a geoprocessing object. The extra arguments can be used to specify additional requirements for the object creation such as the number of columns in the ValueTable object.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The name of the object to be created (ArcSDESQLExecute, Array, Extent, FeatureSet, Field, FieldInfo, FieldMap, FieldMappings, Geometry, NetCDFFileProperties, Point, RecordSet, Result, SpatialReference, and ValueTable). | String |
| options | Optional arguments depending on the object being created. | Object |

## Code Samples

### Example 1

```python
CreateObject (name, {options})
```

### Example 2

```python
import arcpy

# Set the workspace. List all of the feature classes in the dataset.
arcpy.env.workspace = "c:/data/landbase.gdb/wetlands"
fcs = arcpy.ListFeatureClasses()

# Create the value table for the Analysis Union tool with 2 columns.
vtab = arcpy.CreateObject("valuetable", 2)

# Iterate through the list of feature classes.
for fc in fcs:
    # Update the value table with a rank of 2 for each record, except
    #   for BigBog
    if fc.lower() != "bigbog":
        vtab.addRow(fc + " 2")
    else:
        vtab.addRow(fc + " 1")

# Union the wetlands feature classes with the land use feature class
# to create a single feature class with all of the wetlands and land
# use data.
vtab.addRow("c:/data/landbase.gdb/land_use 2")
arcpy.Union_analysis(vtab, "c:/data/landbase.gdb/wetlands_use")
```

### Example 3

```python
import arcpy

# Set the workspace. List all of the feature classes in the dataset.
arcpy.env.workspace = "c:/data/landbase.gdb/wetlands"
fcs = arcpy.ListFeatureClasses()

# Create the value table for the Analysis Union tool with 2 columns.
vtab = arcpy.CreateObject("valuetable", 2)

# Iterate through the list of feature classes.
for fc in fcs:
    # Update the value table with a rank of 2 for each record, except
    #   for BigBog
    if fc.lower() != "bigbog":
        vtab.addRow(fc + " 2")
    else:
        vtab.addRow(fc + " 1")

# Union the wetlands feature classes with the land use feature class
# to create a single feature class with all of the wetlands and land
# use data.
vtab.addRow("c:/data/landbase.gdb/land_use 2")
arcpy.Union_analysis(vtab, "c:/data/landbase.gdb/wetlands_use")
```

---

## CreateRandomValueGenerator

## Summary

Creates a new random number generator.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| seed | Initializes the random number generator. | Integer |
| distribution | The random generation algorithm.ACM599—ACM collected algorithm 599 MERSENNE_TWISTER—Mersenne Twister mt19937 STANDARD_C—Standard C Rand (The default value is ACM599) | String |

## Code Samples

### Example 1

```python
CreateRandomValueGenerator (seed, distribution)
```

---

## CreateScratchName

## Summary

Creates a unique scratch path name for the specified data type. If no workspace is given the current workspace is used.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| prefix | The prefix that is added to the scratchname. By default, a prefix of xx is used. (The default value is xx) | String |
| suffix | The suffix added to the scratchname. This can be an empty double-quoted string. | String |
| data_type | The data type which will be used to create the scratchname. Valid datatypes are:Coverage—Only valid Coverage names are returned.Dataset—Only valid Dataset names are returned.FeatureClass—Only valid FeatureClass names are returned.FeatureDataset—Only valid FeatureDataset names are returned.Folder—Only valid Folder names are returned.Geodataset—Only valid Geodataset names are returned.GeometricNetwork—Only valid Geometric Network names are returned.ArcInfoTable—Only valid ArcInfo Table names are returned.NetworkDataset—Only valid Network Dataset names are returned.RasterBand—Only valid Raster Band names are returned.RasterCatalog—Only valid Raster Catalog names are returned.RasterDataset—Only valid Raster Dataset names are returned.Shapefile—Only valid Shapefile names are returned.Terrain—Only valid Terrain names are returned.Workspace—Only valid Workspace scratchnames are returned. | String |
| workspace | The workspace used to determine the scratch name to be created. If not specified, the current workspace is used. | String |

## Code Samples

### Example 1

```python
CreateScratchName ({prefix}, {suffix}, {data_type}, {workspace})
```

### Example 2

```python
import arcpy

# Set workspace
#
arcpy.env.workspace = "C:/Data/Municipal.gdb"

# Create a scratch name for the Buffer tool output.
#   The scratch name created will be include 'temp0.shp',
#   If temp0.shp already exists, the number will be incremented
#   until the name is unique in the workspace.
#
scratch_name = arcpy.CreateScratchName("temp",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

# Execute Buffer tool, using scratch name for output
#
arcpy.Buffer_analysis("Roads", scratch_name, "1000 feet")

# Execute Clip tool, using scratch name for input
#
arcpy.Clip_analysis(scratch_name, "CityBoundary", "CityRoads")

# Delete scratch dataset
arcpy.Delete_management(scratch_name)
```

### Example 3

```python
import arcpy

# Set workspace
#
arcpy.env.workspace = "C:/Data/Municipal.gdb"

# Create a scratch name for the Buffer tool output.
#   The scratch name created will be include 'temp0.shp',
#   If temp0.shp already exists, the number will be incremented
#   until the name is unique in the workspace.
#
scratch_name = arcpy.CreateScratchName("temp",
                                       data_type="Shapefile",
                                       workspace=arcpy.env.scratchFolder)

# Execute Buffer tool, using scratch name for output
#
arcpy.Buffer_analysis("Roads", scratch_name, "1000 feet")

# Execute Clip tool, using scratch name for input
#
arcpy.Clip_analysis(scratch_name, "CityBoundary", "CityRoads")

# Delete scratch dataset
arcpy.Delete_management(scratch_name)
```

---

## CreateUniqueName

## Summary

Creates a unique name for the specified workspace by appending a number to the input name. This number is incremented until the name is unique. If no workspace is specified, the current workspace is used.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| base_name | The base name used to create the unique name. | String |
| workspace | The workspace used for creation of the unique name. | String |

## Code Samples

### Example 1

```python
CreateUniqueName (base_name, {workspace})
```

### Example 2

```python
import arcpy

# Set workspace
arcpy.env.workspace = "c:/data"

# Create a unique name for the Buffer tool's derived output.
unique_name = arcpy.CreateUniqueName("temp.shp")

# Use unique name for Buffer Tool output dataset name.
arcpy.Buffer_analysis("roads.shp", unique_name, "100 feet")

# Clip output from Buffer tool with County Boundary to obtain buffered roads
# in county.
arcpy.Clip_analysis(unique_name, "county.shp", "clipped_roads.shp")
```

### Example 3

```python
import arcpy

# Set workspace
arcpy.env.workspace = "c:/data"

# Create a unique name for the Buffer tool's derived output.
unique_name = arcpy.CreateUniqueName("temp.shp")

# Use unique name for Buffer Tool output dataset name.
arcpy.Buffer_analysis("roads.shp", unique_name, "100 feet")

# Clip output from Buffer tool with County Boundary to obtain buffered roads
# in county.
arcpy.Clip_analysis(unique_name, "county.shp", "clipped_roads.shp")
```

---

## Dataset properties

## Summary

The Describe function returns the dataset properties described below.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the shapefile
#
desc = arcpy.Describe("C:/temp/xy.shp")

# Print dataset properties
#
print(("Dataset Type: {0}".format(desc.datasetType)))
print(("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(
    desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax)))
print(("MExtent: {0}".format(desc.MExtent)))
print(("ZExtent: {0}".format(desc.ZExtent)))

print(("Spatial reference name: {0}:".format(desc.spatialReference.name)))
```

### Example 2

```python
import arcpy

# Create a Describe object from the shapefile
#
desc = arcpy.Describe("C:/temp/xy.shp")

# Print dataset properties
#
print(("Dataset Type: {0}".format(desc.datasetType)))
print(("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(
    desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax)))
print(("MExtent: {0}".format(desc.MExtent)))
print(("ZExtent: {0}".format(desc.ZExtent)))

print(("Spatial reference name: {0}:".format(desc.spatialReference.name)))
```

---

## dBase Table properties

## Summary

The Describe function returns the Table and Dataset property groups for dBase tables.

---

## DecryptPYT

## Summary

Decrypt an encrypted Python toolbox file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| toolbox | The encrypted Python toolbox that will be unencrypted. | String |
| password | The password used to unlock the encrypted Python toolbox. | String |

## Code Samples

### Example 1

```python
DecryptPYT (toolbox, password)
```

### Example 2

```python
import arcpy

toolbox = 'd:/tools/analysis.pyt'
password = '<your password>'

arcpy.DecryptPYT(toolbox, password)
```

### Example 3

```python
import arcpy

toolbox = 'd:/tools/analysis.pyt'
password = '<your password>'

arcpy.DecryptPYT(toolbox, password)
```

---

## Describe object properties

## Summary

The Describe function returns the following properties for all Describe objects.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/Data/chesapeake.gdb")

# Print some Describe Object properties
#
if hasattr(desc, "name"):
    print("Name:        " + desc.name)
if hasattr(desc, "dataType"):
    print("DataType:    " + desc.dataType)
if hasattr(desc, "catalogPath"):
    print("CatalogPath: " + desc.catalogPath)

# Examine children and print their name and dataType
#
print("Children:")
for child in desc.children:
    print("\t%s = %s" % (child.name, child.dataType))
```

### Example 2

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/Data/chesapeake.gdb")

# Print some Describe Object properties
#
if hasattr(desc, "name"):
    print("Name:        " + desc.name)
if hasattr(desc, "dataType"):
    print("DataType:    " + desc.dataType)
if hasattr(desc, "catalogPath"):
    print("CatalogPath: " + desc.catalogPath)

# Examine children and print their name and dataType
#
print("Children:")
for child in desc.children:
    print("\t%s = %s" % (child.name, child.dataType))
```

---

## Describe

## Summary

Describes a data element and returns a Describe object with multiple properties, such as data type, fields, indexes, and many others. Its properties are dynamic, meaning that depending on the data type described, different describe properties will be available for use.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| value | The specified data element or geoprocessing object to describe. | String |
| data_type | The type of data. This is only necessary when naming conflicts exist, for example, if a geodatabase contains a feature dataset (FeatureDataset) and a feature class (FeatureClass) with the same name. In this case, the data type is used to clarify which dataset will be described. (The default value is None) | String |

## Code Samples

### Example 1

```python
Describe (value, {data_type})
```

### Example 2

```python
import arcpy

# Get the layer as a parameter and describe it.
#
# The layer could be a layer in ArcMap (like "some_layer")
# Or, it could be a .lyr file (like "C:/data/some.lyr")
#
layerString = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(layerString)

# Print selected layer and describe object properties
# 
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
    print(".lyr file: {}".format(desc.catalogPath))
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))

if desc.FIDSet != '':
    print("Number of selected features: {}".format(len(desc.FIDSet.split(";"))))
```

### Example 3

```python
import arcpy

# Get the layer as a parameter and describe it.
#
# The layer could be a layer in ArcMap (like "some_layer")
# Or, it could be a .lyr file (like "C:/data/some.lyr")
#
layerString = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(layerString)

# Print selected layer and describe object properties
# 
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
    print(".lyr file: {}".format(desc.catalogPath))
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))

if desc.FIDSet != '':
    print("Number of selected features: {}".format(len(desc.FIDSet.split(";"))))
```

---

## DisconnectUser

## Summary

The DisconnectUser function allows an administrator to disconnect users who are currently connected to an enterprise geodatabase.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| sde_workspace | The enterprise geodatabase the users will be disconnected from. The connection properties specified in the enterprise geodatabase must have administrative rights that allow the user to disconnect other connections. | String |
| users[users,...] | Specifies the users who will be disconnected from the geodatabase.sde_id—Users will be disconnected based on the ID value returned from the ListUsers function. This can be passed to the function as an individual SDE ID value or a list containing multiple SDE ID values.ALL—All connected users will be disconnected.Note:This function will not disconnect the user who is running the function. | Integer |

## Code Samples

### Example 1

```python
DisconnectUser (sde_workspace, {users})
```

### Example 2

```python
import arcpy

arcpy.DisconnectUser("D:\\MyProject\\admin.sde", "ALL")
```

### Example 3

```python
import arcpy

arcpy.DisconnectUser("D:\\MyProject\\admin.sde", "ALL")
```

### Example 4

```python
import arcpy

admin_workspace = "D:\\MyProject\\admin.sde"
arcpy.env.workspace = admin_workspace
user_name = "GDB"

# Look through the users in the connected user list and get the connection ID.
# Use the connection ID to disconnect the user that matches the username variable
users = arcpy.ListUsers(admin_workspace)
for item in users:
    if item.Name == user_name:
        arcpy.DisconnectUser(admin_workspace, item.ID)
```

### Example 5

```python
import arcpy

admin_workspace = "D:\\MyProject\\admin.sde"
arcpy.env.workspace = admin_workspace
user_name = "GDB"

# Look through the users in the connected user list and get the connection ID.
# Use the connection ID to disconnect the user that matches the username variable
users = arcpy.ListUsers(admin_workspace)
for item in users:
    if item.Name == user_name:
        arcpy.DisconnectUser(admin_workspace, item.ID)
```

### Example 6

```python
import arcpy

# Set the admistrative workspace connection
admin_workspace = "D:\\MyProject\\admin.sde"

# Create a list of users to disconnect.
user_names = ["TRAVIS", "DEBBIE", "PHIL"]

# Get a list of connected users
connected_users = arcpy.ListUsers(admin_workspace)

# Loop through the list of connected users and execute DisconnectUser
# if the user name is in the user_names list
for user in connected_users:
    if user.Name in user_names:
        print('Disconnecting {0}'.format(user.Name))
        arcpy.DisconnectUser(admin_workspace, user.ID)
```

### Example 7

```python
import arcpy

# Set the admistrative workspace connection
admin_workspace = "D:\\MyProject\\admin.sde"

# Create a list of users to disconnect.
user_names = ["TRAVIS", "DEBBIE", "PHIL"]

# Get a list of connected users
connected_users = arcpy.ListUsers(admin_workspace)

# Loop through the list of connected users and execute DisconnectUser
# if the user name is in the user_names list
for user in connected_users:
    if user.Name in user_names:
        print('Disconnecting {0}'.format(user.Name))
        arcpy.DisconnectUser(admin_workspace, user.ID)
```

---

## Domain Network properties

## Summary

The following properties are returned by the domainNetworks object in a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Creation Time: {dom.creationTime}")
    print(f"Release Number: {dom.releaseNumber}")
    print(f"Is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Tier Definition: {dom.tierDefinition}")
    print(f"Subnetwork Controller Type: {dom.subnetworkControllerType} \n")
    
    # Tier Group properties
    for tierGroup in dom.tierGroups:
        print(f"*** - Tier Group properties - ***")
        print(f"Tier Group Name: {tierGroup.name}")
        print(f"Tier Group Creation Time: {tierGroup.creationTime}")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Creation Time: {dom.creationTime}")
    print(f"Release Number: {dom.releaseNumber}")
    print(f"Is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Tier Definition: {dom.tierDefinition}")
    print(f"Subnetwork Controller Type: {dom.subnetworkControllerType} \n")
    
    # Tier Group properties
    for tierGroup in dom.tierGroups:
        print(f"*** - Tier Group properties - ***")
        print(f"Tier Group Name: {tierGroup.name}")
        print(f"Tier Group Creation Time: {tierGroup.creationTime}")
```

---

## Edge Source Properties

## Summary

Provides information about edge sources in a network dataset.

## Code Samples

### Example 1

```python
# Name: NDSAttributeProperties_ex01.py
# Description: Print the information about edge sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

# Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Edge sources")

# Get all the edge sources for the network dataset
edgeSources = desc.edgeSources

if not edgeSources:
    print(" %*s" % (justify, "(No edge sources)"))
    sys.exit(0)

for edgeSource in edgeSources:
    print(" %*s: %s" % (justify, "Source Name" , edgeSource.name))
    print(" %*s: %s" % (justify, "Source ID" , str(edgeSource.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", edgeSource.sourceType))
    print(" %*s: %s" % (justify, "Element Type", edgeSource.elementType))
    print(" %*s: %s" % (justify, "From Elevation Field",
                        edgeSource.fromElevationFieldName))
    print(" %*s: %s" % (justify, "To Elevation Field",
                        edgeSource.toElevationFieldName))
    print(" ")
```

### Example 2

```python
# Name: NDSAttributeProperties_ex01.py
# Description: Print the information about edge sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

# Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Edge sources")

# Get all the edge sources for the network dataset
edgeSources = desc.edgeSources

if not edgeSources:
    print(" %*s" % (justify, "(No edge sources)"))
    sys.exit(0)

for edgeSource in edgeSources:
    print(" %*s: %s" % (justify, "Source Name" , edgeSource.name))
    print(" %*s: %s" % (justify, "Source ID" , str(edgeSource.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", edgeSource.sourceType))
    print(" %*s: %s" % (justify, "Element Type", edgeSource.elementType))
    print(" %*s: %s" % (justify, "From Elevation Field",
                        edgeSource.fromElevationFieldName))
    print(" %*s: %s" % (justify, "To Elevation Field",
                        edgeSource.toElevationFieldName))
    print(" ")
```

---

## Edge Source properties

## Summary

The properties below are returned by the edgeSources object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUN_EdgeSourceProperties.py
Description: This script reports the edge source properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print("Domain Network Creation Time: {0}".format(dom.creationTime))
    print("Domain Network Release Number: {0}".format(dom.releaseNumber))
    print("Domain Network is Structure Network: {0}".format(dom.isStructureNetwork))
    print("Domain Network ID: {0}".format(dom.domainNetworkId))
    print("Domain Network Name: {0}".format(dom.domainNetworkName))
    print("Domain Network Alias Name: {0}".format(dom.domainNetworkAliasName))
    print("Domain Network Subnetwork Table Name: {0}".format(dom.subnetworkTableName))
    print("Domain Network Subnetwork Label Field Name: {0}".format(dom.subnetworkLabelFieldName))
    print("Domain Network Tier Definition: {0}".format(dom.tierDefinition))
    print("Domain Network Subnetwork Controller Type: {0} \n".format(dom.subnetworkControllerType))

    # Edge Source Properties
    for edgeSource in dom.edgeSources:
        print(" -- Edge Source Properties -- ")
        print("Edge Source Id: {0}".format(edgeSource.sourceId))
        print("Object Class ID: {0}".format(edgeSource.objectClassId))
        print("Edge Source Name: {0}".format(edgeSource.sourceName))
        print("Uses Geometry: {0}".format(edgeSource.usesGeometry))
        print("Shape Type: {0} \n".format(edgeSource.shapeType))
        print("Feature Class Usage: {0}".format(edgeSource.utilityNetworkFeatureClassUsageType))
        print("Asset Type Field Name: {0}".format(edgeSource.assetTypeFieldName))
        print("Supported Properties: {0} \n".format(edgeSource.supportedProperties))

        # Asset Group Properties
        for ag in edgeSource.assetGroups:
            print(" - Asset Group Properties - ")
            print("Asset Group Code: {0}".format(ag.assetGroupCode))
            print("Asset Group Name: {0} \n".format(ag.assetGroupName))

            # Asset Type Properties
            for at in ag.assetTypes:
                print(" - Asset Type Properties - ")
                print("Asset Type Code: {0}".format(at.assetTypeCode))
                print("Asset Type Name: {0}".format(at.assetTypeName))
                print("Asset Type Containment View Scale: {0}".format(at.containmentViewScale))
                print("Asset Type Association Delete Type: {0}".format(at.associationDeleteType))
                print("Asset Type Association Role Type: {0}".format(at.associationRoleType))
                print("Asset Type Terminal Configuration Supported: {0}".format(at.isTerminalConfigurationSupported))
                print("Asset Type Terminal Configuration ID: {0}".format(at.terminalConfigurationID))
                print("Asset Type Linear Connectivity Policy Supported: {0}".format(at.isLinearConnectivityPolicySupported))
                print("Asset Type Connectivity Policy: {0}".format(at.connectivityPolicy))
                print("Asset Type Categories: {0}".format(at.categories))
                print("Asset Type Split Content: {0} \n".format(at.splitContent))
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUN_EdgeSourceProperties.py
Description: This script reports the edge source properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print("Domain Network Creation Time: {0}".format(dom.creationTime))
    print("Domain Network Release Number: {0}".format(dom.releaseNumber))
    print("Domain Network is Structure Network: {0}".format(dom.isStructureNetwork))
    print("Domain Network ID: {0}".format(dom.domainNetworkId))
    print("Domain Network Name: {0}".format(dom.domainNetworkName))
    print("Domain Network Alias Name: {0}".format(dom.domainNetworkAliasName))
    print("Domain Network Subnetwork Table Name: {0}".format(dom.subnetworkTableName))
    print("Domain Network Subnetwork Label Field Name: {0}".format(dom.subnetworkLabelFieldName))
    print("Domain Network Tier Definition: {0}".format(dom.tierDefinition))
    print("Domain Network Subnetwork Controller Type: {0} \n".format(dom.subnetworkControllerType))

    # Edge Source Properties
    for edgeSource in dom.edgeSources:
        print(" -- Edge Source Properties -- ")
        print("Edge Source Id: {0}".format(edgeSource.sourceId))
        print("Object Class ID: {0}".format(edgeSource.objectClassId))
        print("Edge Source Name: {0}".format(edgeSource.sourceName))
        print("Uses Geometry: {0}".format(edgeSource.usesGeometry))
        print("Shape Type: {0} \n".format(edgeSource.shapeType))
        print("Feature Class Usage: {0}".format(edgeSource.utilityNetworkFeatureClassUsageType))
        print("Asset Type Field Name: {0}".format(edgeSource.assetTypeFieldName))
        print("Supported Properties: {0} \n".format(edgeSource.supportedProperties))

        # Asset Group Properties
        for ag in edgeSource.assetGroups:
            print(" - Asset Group Properties - ")
            print("Asset Group Code: {0}".format(ag.assetGroupCode))
            print("Asset Group Name: {0} \n".format(ag.assetGroupName))

            # Asset Type Properties
            for at in ag.assetTypes:
                print(" - Asset Type Properties - ")
                print("Asset Type Code: {0}".format(at.assetTypeCode))
                print("Asset Type Name: {0}".format(at.assetTypeName))
                print("Asset Type Containment View Scale: {0}".format(at.containmentViewScale))
                print("Asset Type Association Delete Type: {0}".format(at.associationDeleteType))
                print("Asset Type Association Role Type: {0}".format(at.associationRoleType))
                print("Asset Type Terminal Configuration Supported: {0}".format(at.isTerminalConfigurationSupported))
                print("Asset Type Terminal Configuration ID: {0}".format(at.terminalConfigurationID))
                print("Asset Type Linear Connectivity Policy Supported: {0}".format(at.isLinearConnectivityPolicySupported))
                print("Asset Type Connectivity Policy: {0}".format(at.connectivityPolicy))
                print("Asset Type Categories: {0}".format(at.categories))
                print("Asset Type Split Content: {0} \n".format(at.splitContent))
```

---

## Editor Tracking properties

## Summary

The Describe function returns the following properties for datasets that have editor tracking enabled.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the feature class
#
gdb_fc = "C:/data/ParcelBase.gdb/parcels_enabled"
desc = arcpy.Describe(gdb_fc)

# If the feature class has editor tracking enabled, then
#   list how many features were last edited by each user.
#
if desc.editorTrackingEnabled:
    #
    # Get the editorFieldName from the describe object
    whoField = desc.editorFieldName
    #
    # Use a cursor to search through all the features
    userDictionary = {}
    cur = arcpy.da.SearchCursor(gdb_fc, [whoField])
    for row in cur:
        featureEditedBy = row[0]
        if featureEditedBy in userDictionary:
            userDictionary[featureEditedBy] += 1
        else:
            userDictionary[featureEditedBy] = 1
    #
    # Print the results
    for user in list(userDictionary.keys()):
        if user == None:
            print('Last edited before editor tracking was enabled: '+ \
                   str(userDictionary[user]))
        else:
            print("Last edited by " + user + ": " + str(userDictionary[user]))
else:
    print('Editor tracking not enabled for '+gdb_fc)
```

### Example 2

```python
import arcpy

# Create a Describe object from the feature class
#
gdb_fc = "C:/data/ParcelBase.gdb/parcels_enabled"
desc = arcpy.Describe(gdb_fc)

# If the feature class has editor tracking enabled, then
#   list how many features were last edited by each user.
#
if desc.editorTrackingEnabled:
    #
    # Get the editorFieldName from the describe object
    whoField = desc.editorFieldName
    #
    # Use a cursor to search through all the features
    userDictionary = {}
    cur = arcpy.da.SearchCursor(gdb_fc, [whoField])
    for row in cur:
        featureEditedBy = row[0]
        if featureEditedBy in userDictionary:
            userDictionary[featureEditedBy] += 1
        else:
            userDictionary[featureEditedBy] = 1
    #
    # Print the results
    for user in list(userDictionary.keys()):
        if user == None:
            print('Last edited before editor tracking was enabled: '+ \
                   str(userDictionary[user]))
        else:
            print("Last edited by " + user + ": " + str(userDictionary[user]))
else:
    print('Editor tracking not enabled for '+gdb_fc)
```

---

## EncryptPYT

## Summary

Encrypts a Python toolbox file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| toolbox | The Python toolbox that will be encrypted in place. | String |
| password | The password used to lock the encrypted Python toolbox. | String |

## Code Samples

### Example 1

```python
EncryptPYT (toolbox, password)
```

### Example 2

```python
import arcpy

toolbox = 'd:/tools/analysis.pyt'
password = '<your password>'

arcpy.EncryptPYT(toolbox, password)
```

### Example 3

```python
import arcpy

toolbox = 'd:/tools/analysis.pyt'
password = '<your password>'

arcpy.EncryptPYT(toolbox, password)
```

---

## Evaluator properties

## Summary

The properties below are returned by the evaluator object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes

for na in netattrs:
    print(f"Name: {na.name}")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")

    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes

for na in netattrs:
    print(f"Name: {na.name}")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")

    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

---

## Exists

## Summary

Determines the existence of the specified data object. This function tests for the existence of various data types including feature classes, tables, datasets, shapefiles, workspaces, layers, and files. The function returns a Boolean indicating whether the element exists.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The path to the dataset to be checked for existence. | String |

## Code Samples

### Example 1

```python
Exists (dataset)
```

### Example 2

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Check for existence of data before deleting
if arcpy.Exists("roadbuffer"):
    arcpy.Delete_management("roadbuffer")
```

### Example 3

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Check for existence of data before deleting
if arcpy.Exists("roadbuffer"):
    arcpy.Delete_management("roadbuffer")
```

---

## Feature Class properties

## Summary

The Describe function returns the following properties for feature classes. The Table and Dataset property groups are also supported. The Editor Tracking property group is supported if editor tracking has been enabled for this feature class.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the feature class
#
desc = arcpy.Describe("C:/data/arch.dgn/Point")

# Print some feature class properties
#
print("Feature Type:  " + desc.featureType)
print("Shape Type :   " + desc.shapeType)
print("Spatial Index: " + str(desc.hasSpatialIndex))
```

### Example 2

```python
import arcpy

# Create a Describe object from the feature class
#
desc = arcpy.Describe("C:/data/arch.dgn/Point")

# Print some feature class properties
#
print("Feature Type:  " + desc.featureType)
print("Shape Type :   " + desc.shapeType)
print("Spatial Index: " + str(desc.hasSpatialIndex))
```

---

## Field group properties

## Summary

The Describe function returns the properties described below for datasets that have field groups added to them.

## Code Samples

### Example 1

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.MapleTrees"

# Print a report of the field group properties
field_groups = arcpy.Describe(fc).fieldGroups
for fg in field_groups:
    print(f"Field Group Name: {fg.name}")
    print(f"Fields: {fg.fieldNames}")
    print(f"Restrictive: {fg.isEditingRestrictive}")
```

### Example 2

```python
# Import the required modules
import arcpy

# Path to the input feature class or table
fc = "C:\\MyProject\\MyDatabase.sde\\myGDB.USER1.MapleTrees"

# Print a report of the field group properties
field_groups = arcpy.Describe(fc).fieldGroups
for fg in field_groups:
    print(f"Field Group Name: {fg.name}")
    print(f"Fields: {fg.fieldNames}")
    print(f"Restrictive: {fg.isEditingRestrictive}")
```

---

## File properties

## Summary

When used with the Describe function, a file returns a Describe dataType property value of "File".

## Code Samples

### Example 1

```python
import arcpy


# Create a Describe object
#
desc = arcpy.Describe("C:/data/Install.log")

# Print some Describe Object properties for the file
#
print("Data Type: " + desc.dataType)
print("Path:      " + desc.path)
print("Base Name: " + desc.baseName)
print("Extension: " + desc.extension)
```

### Example 2

```python
import arcpy


# Create a Describe object
#
desc = arcpy.Describe("C:/data/Install.log")

# Print some Describe Object properties for the file
#
print("Data Type: " + desc.dataType)
print("Path:      " + desc.path)
print("Base Name: " + desc.baseName)
print("Extension: " + desc.extension)
```

---

## Filter Barriers properties

## Summary

The properties below are returned by the filterBarriers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Filter Barrier Properties
        print(" - Filter Barrier Properties - ")
        for filb in ust.filterBarriers:
            try:
                print(f"Name: {filb.name}")
                print(f"Type: {filb.type}")
                print(f"Operator: {filb.operator}")
                print(f"Value: {filb.value}")
                print(f"CombineUsingOr: {filb.combineUsingOr}")
                print(f"Is Specific Value: {filb.isSpecificValue} \n")
            except:
                print("Skipped filter barrier properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Filter Barrier Properties
        print(" - Filter Barrier Properties - ")
        for filb in ust.filterBarriers:
            try:
                print(f"Name: {filb.name}")
                print(f"Type: {filb.type}")
                print(f"Operator: {filb.operator}")
                print(f"Value: {filb.value}")
                print(f"CombineUsingOr: {filb.combineUsingOr}")
                print(f"Is Specific Value: {filb.isSpecificValue} \n")
            except:
                print("Skipped filter barrier properties. \n")
```

---

## Filter Function Barriers properties

## Summary

The properties below are returned by the filterFunctionBarriers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Filter Function Barrier Properties
        print(" - Filter Function Barrier Properties - ")
        for ffb in ust.filterFunctionBarriers:
            try:
                print(f"Name: {ffb.networkAttributeName}")
                print(f"Type: {ffb.functionType}")
                print(f"Operator: {ffb.networkAttributeOperator}")
                print(f"Value: {ffb.value}")
                print(f"Use Local Values: {ffb.useLocalValues} \n")
            except:
                print("Skipped filter function properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Filter Function Barrier Properties
        print(" - Filter Function Barrier Properties - ")
        for ffb in ust.filterFunctionBarriers:
            try:
                print(f"Name: {ffb.networkAttributeName}")
                print(f"Type: {ffb.functionType}")
                print(f"Operator: {ffb.networkAttributeOperator}")
                print(f"Value: {ffb.value}")
                print(f"Use Local Values: {ffb.useLocalValues} \n")
            except:
                print("Skipped filter function properties. \n")
```

---

## Folder properties

## Summary

The Describe function returns the Workspace property group for folders.

## Code Samples

### Example 1

```python
import arcpy
 

# Create a Describe object
#
desc = arcpy.Describe("C:/data")

# Print the dataType and a workspace property
#
print("Data Type:      " + desc.dataType)
print("Workspace Type: " + desc.workspaceType)
```

### Example 2

```python
import arcpy
 

# Create a Describe object
#
desc = arcpy.Describe("C:/data")

# Print the dataType and a workspace property
#
print("Data Type:      " + desc.dataType)
print("Workspace Type: " + desc.workspaceType)
```

---

## FromCoordString

## Summary

Converts a coordinate system notation string to a PointGeometry object in WGS84 coordinates.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| string | The input coordinates. | String |
| notation | The coordinate system notation of the input string.DD— Decimal degrees is used, for example, 34.05719570N 117.19647020W.DDM— Degrees decimal minutes is used, for example, 34 03.43174200N 117 11.78821200W.DMS— Degree Minute Seconds, is used, for example, 34 03 25.90452000N 117 11 47.29272000W.GARS— Global Area Reference System is used, for example, 126LJ47. It is based on latitude and longitude, and it divides and subdivides the world into cells.GEOREF— World Geographic Reference System is used, for example, EJCE4821203432.MGRS— Military Grid Reference System is used, for example, 11SMT8186968515.USNG— United States National Grid is used, for example, 11S MT 81869 68515.UTM— Universal Transverse Mercator is used, for example, 11S 481868 3768515. It is based on zone number, MGRS latitude band, and the easting and northing planar coordinate pair in that zone.UTMNS— Universal Transverse Mercator (no spaces) is used, for example, 11N4818683768515. It is based on zone number, hemisphere designator, and the easting and northing planar coordinate pair in that zone. | String |

## Code Samples

### Example 1

```python
FromCoordString (string, notation)
```

### Example 2

```python
import arcpy
coord_string = '14S PB 59361 43195'
point_geometry = arcpy.FromCoordString(coord_string, 'USNG')
```

### Example 3

```python
import arcpy
coord_string = '14S PB 59361 43195'
point_geometry = arcpy.FromCoordString(coord_string, 'USNG')
```

---

## FromGeohash

## Summary

Converts a geohash string to an Extent object in WGS 1984 coordinates that represents the corresponding bounding box in the geohash grid.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| geohash_string | The geohash string used to obtain the extent in WGS 1984 coordinates. | String |

## Code Samples

### Example 1

```python
FromGeohash (geohash_string)
```

### Example 2

```python
import arcpy
extent = arcpy.FromGeohash('dp1k05k8')
```

### Example 3

```python
import arcpy
extent = arcpy.FromGeohash('dp1k05k8')
```

### Example 4

```python
import arcpy

# Spatial reference set to GCS_WGS_1984
spatial_reference = arcpy.SpatialReference(4326)

extent = arcpy.FromGeohash('dp1k05k8')
extent_x = (extent.XMax + extent.XMin) / 2
extent_y = (extent.YMax + extent.YMin) / 2

pnt = arcpy.Point(extent_x, extent_y)
pnt_geom = arcpy.PointGeometry(pnt, spatial_reference)
```

### Example 5

```python
import arcpy

# Spatial reference set to GCS_WGS_1984
spatial_reference = arcpy.SpatialReference(4326)

extent = arcpy.FromGeohash('dp1k05k8')
extent_x = (extent.XMax + extent.XMin) / 2
extent_y = (extent.YMax + extent.YMin) / 2

pnt = arcpy.Point(extent_x, extent_y)
pnt_geom = arcpy.PointGeometry(pnt, spatial_reference)
```

---

## FromWKB

## Summary

Creates a geometry object from a well-known binary (WKB) string stored as a bytearray or bytes object.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| byte_array | A WKB string stored in a bytearray or bytes object. | Bytearray |

## Code Samples

### Example 1

```python
FromWKB (byte_array)
```

### Example 2

```python
import arcpy

fc = "c:/base/gdb.gdb/counties"

rows = arcpy.da.SearchCursor(fc, ['SHAPE@'])
studyarea = rows.next()[0]

# Create geometry to WKB
polyWKB = studyarea.WKB

# Convert WKB back to a geometry
polyGeom = arcpy.FromWKB(polyWKB)
```

### Example 3

```python
import arcpy

fc = "c:/base/gdb.gdb/counties"

rows = arcpy.da.SearchCursor(fc, ['SHAPE@'])
studyarea = rows.next()[0]

# Create geometry to WKB
polyWKB = studyarea.WKB

# Convert WKB back to a geometry
polyGeom = arcpy.FromWKB(polyWKB)
```

---

## FromWKT

## Summary

Creates a geometry object from a well-known text (WKT) string.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wkt_string | A WKT string. | String |
| spatial_reference | The spatial reference of the geometry. It can be specified with either a SpatialReference object or a string equivalent. | SpatialReference |

## Code Samples

### Example 1

```python
FromWKT (wkt_string, {spatial_reference})
```

---

## Function Barrier properties

## Summary

The properties below are returned by the functionBarriers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Function Barrier Properties
        print(" - Function Barrier Properties - ")
        for fb in ust.functionBarriers:
            try:
                print(f"Name: {fb.networkAttributeName}")
                print(f"Type: {fb.functionType}")
                print(f"Operator: {fb.networkAttributeOperator}")
                print(f"Value: {fb.value} ")
                print(f"Use Local Values: {fb.useLocalValues} \n")
            except:
                print("Skipped function barrier properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Function Barrier Properties
        print(" - Function Barrier Properties - ")
        for fb in ust.functionBarriers:
            try:
                print(f"Name: {fb.networkAttributeName}")
                print(f"Type: {fb.functionType}")
                print(f"Operator: {fb.networkAttributeOperator}")
                print(f"Value: {fb.value} ")
                print(f"Use Local Values: {fb.useLocalValues} \n")
            except:
                print("Skipped function barrier properties. \n")
```

---

## Function properties

## Summary

The properties below are returned by the functions object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")
```

---

## Geodatabase Feature Class properties

## Summary

The Describe function returns the following properties for geodatabase feature classes. The Feature Class, Geodatabase Table, Editor Tracking Dataset, Table, and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the GDB Feature Class
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/chesapeake/bayshed_1")

# Print GDB FeatureClass properties
#
print("Area Field Name  : " + desc.areaFieldName)
print("Length Field Name: " + desc.lengthFieldName)
```

### Example 2

```python
import arcpy

# Create a Describe object from the GDB Feature Class
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/chesapeake/bayshed_1")

# Print GDB FeatureClass properties
#
print("Area Field Name  : " + desc.areaFieldName)
print("Length Field Name: " + desc.lengthFieldName)
```

---

## Geodatabase Table properties

## Summary

The Describe function returns the following properties for geodatabase tables. The Editor Tracking, Table, and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the GDB table.
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/munich")

# Print GDB Table properties
#
print("%-22s %s" % ("AliasName:", desc.aliasName))
print("%-22s %s" % ("DefaultSubtypeCode:", desc.defaultSubtypeCode))
print("%-22s %s" % ("GlobalIDFieldName:", desc.globalIDFieldName))
print("%-22s %s" % ("ModelName:", desc.modelName))
print("%-22s %s" % ("RasterFieldName:", desc.rasterFieldName))
print("%-22s %s" % ("RelationshipClassNames:", desc.relationshipClassNames))
```

### Example 2

```python
import arcpy

# Create a Describe object from the GDB table.
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/munich")

# Print GDB Table properties
#
print("%-22s %s" % ("AliasName:", desc.aliasName))
print("%-22s %s" % ("DefaultSubtypeCode:", desc.defaultSubtypeCode))
print("%-22s %s" % ("GlobalIDFieldName:", desc.globalIDFieldName))
print("%-22s %s" % ("ModelName:", desc.modelName))
print("%-22s %s" % ("RasterFieldName:", desc.rasterFieldName))
print("%-22s %s" % ("RelationshipClassNames:", desc.relationshipClassNames))
```

---

## GenerateOptimalCoordinateSystem

## Summary

Generates a SpatialReference object with a custom projected coordinate system optimal for the specified extent and intended purpose of your map or analysis.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| extent | The extent of interest. The Extent object must have a spatial reference in a geographic coordinate system such as WGS84. | Extent |
| property | A property that represents the purpose of the projection.EQUAL_AREA—Preserves the relative area of regions everywhere on earth. Shape and distances will be distorted.CONFORMAL—Preserves angles in small areas, so shapes are for the most part preserved. Size and distances will be distorted.EQUIDISTANT_ONE_POINT—Preserves distance when measured through the center of the projection. Area, shape, and other distances will be distorted.EQUIDISTANT_MERIDIANS—Preserves distance when measured along meridians. Area, shape, and other distances will be distorted.COMPROMISE_WORLD—Does not preserve area, shape, or distance specifically, but creates a balance between these geometric properties. Compromise projections are only suggested for very large areas. Not all properties are supported for all extents of interest. The CONFORMAL and EQUIDISTANT_MERIDIANS properties are only supported for large-scale extents, and the COMPROMISE_WORLD property is only supported for full-world extents. The EQUAL_AREA and EQUIDISTANT_ONE_POINT properties are supported for all extents | String |
| custom_name | The name of the custom projected coordinate system. If unspecified, the name will be Custom_Projection. | String |

## Code Samples

### Example 1

```python
GenerateOptimalCoordinateSystem (extent, property, {custom_name})
```

### Example 2

```python
import arcpy

# Input features in Projected Coordinate System
infc = r"C:\Projected.gdb\Colorado_Counties"

# Get extent of features
desc = arcpy.Describe(infc)
extent = desc.extent

# Project the extent to Geographic Coordinate System WGS84
gcs_sr = arcpy.SpatialReference(4326)
prj_extent = extent.projectAs(gcs_sr)

# Create custom projected coordinate system
custom_sr = arcpy.GenerateOptimalCoordinateSystem(prj_extent, "EQUAL_AREA",
                                                  "EQUAL_AREA_COLORADO")

# Project the input features to the custom projection
fc_prj = arcpy.management.Project(infc, "TestPoly_Projected", custom_sr)
```

### Example 3

```python
import arcpy

# Input features in Projected Coordinate System
infc = r"C:\Projected.gdb\Colorado_Counties"

# Get extent of features
desc = arcpy.Describe(infc)
extent = desc.extent

# Project the extent to Geographic Coordinate System WGS84
gcs_sr = arcpy.SpatialReference(4326)
prj_extent = extent.projectAs(gcs_sr)

# Create custom projected coordinate system
custom_sr = arcpy.GenerateOptimalCoordinateSystem(prj_extent, "EQUAL_AREA",
                                                  "EQUAL_AREA_COLORADO")

# Project the input features to the custom projection
fc_prj = arcpy.management.Project(infc, "TestPoly_Projected", custom_sr)
```

### Example 4

```python
import arcpy

gcs_sr = arcpy.SpatialReference(4326) # Create WGS84 spatial reference

# Create polygon
poly_info = [[20, 20], [20, 60], [60, 60], [60, 20], [20, 20]]
poly_pts = arcpy.Array([arcpy.Point(*coords) for coords in poly_info])
poly = arcpy.Polygon(poly_pts, gcs_sr)

# Create extent object from polygon
extent = poly.extent

# Create custom projected coordinate system
custom_sr = arcpy.GenerateOptimalCoordinateSystem(extent, "CONFORMAL")

# Project the polygon to the custom projection
poly_prj = poly.projectAs(custom_sr)
```

### Example 5

```python
import arcpy

gcs_sr = arcpy.SpatialReference(4326) # Create WGS84 spatial reference

# Create polygon
poly_info = [[20, 20], [20, 60], [60, 60], [60, 20], [20, 20]]
poly_pts = arcpy.Array([arcpy.Point(*coords) for coords in poly_info])
poly = arcpy.Polygon(poly_pts, gcs_sr)

# Create extent object from polygon
extent = poly.extent

# Create custom projected coordinate system
custom_sr = arcpy.GenerateOptimalCoordinateSystem(extent, "CONFORMAL")

# Project the polygon to the custom projection
poly_prj = poly.projectAs(custom_sr)
```

---

## Geometric Network properties

## Summary

The Describe function returns the following properties for geometric networks. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the geometric network.
#
desc = arcpy.Describe("C:/data/wellingham.gdb/water/water_Net")

# Print some geometric network properties
#
print("NetworkType:                    " + desc.networkType)
print("OrphanJunctionFeatureClassName: " + \
    desc.orphanJunctionFeatureClassName)
print("Feature Class Names:")
for fcname in desc.featureClassNames:
    print("  " + fcname)
```

### Example 2

```python
import arcpy

# Create a Describe object from the geometric network.
#
desc = arcpy.Describe("C:/data/wellingham.gdb/water/water_Net")

# Print some geometric network properties
#
print("NetworkType:                    " + desc.networkType)
print("OrphanJunctionFeatureClassName: " + \
    desc.orphanJunctionFeatureClassName)
print("Feature Class Names:")
for fcname in desc.featureClassNames:
    print("  " + fcname)
```

---

## Geostatistical Layer properties

## Summary

The Describe function returns the following properties for geostatistical layers. The Layer property group is also supported.

## Code Samples

### Example 1

```python
# Name: Describe_GA_Layer_Example_01.py
# Description: Print the Describe properties of a geostatistical layer.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Check out Geostatistical Analyst extension
arcpy.CheckOutExtension("GeoStats")

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
GALayer = "IDW_galayer"

# Execute IDW
arcpy.ga.IDW(inPointFeatures, zField, GALayer)

# Describe the geostatistical layer
desc = arcpy.Describe(GALayer)

# Save extent of geostatistical layer
aoi = desc.areaOfInterest

# Save name of geostatistical layer
name = desc.nameString

# Save data type of geostatistical layer
dt = desc.dataType

# Save data sources and primary input dataset
dc = desc.dataCollection
ds = dc.getValue(0,0)

# Print describe properties
print("Layer name:       " + name)
print("Data type:        " + dt)
print("Input data:       " + ds)
print("Minimum X Extent: " + str(aoi.XMin))
print("Maximum X Extent: " + str(aoi.XMax))
print("Minimum Y Extent: " + str(aoi.YMin))
print("Maximum Y Extent: " + str(aoi.YMax))
```

### Example 2

```python
# Name: Describe_GA_Layer_Example_01.py
# Description: Print the Describe properties of a geostatistical layer.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Check out Geostatistical Analyst extension
arcpy.CheckOutExtension("GeoStats")

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
GALayer = "IDW_galayer"

# Execute IDW
arcpy.ga.IDW(inPointFeatures, zField, GALayer)

# Describe the geostatistical layer
desc = arcpy.Describe(GALayer)

# Save extent of geostatistical layer
aoi = desc.areaOfInterest

# Save name of geostatistical layer
name = desc.nameString

# Save data type of geostatistical layer
dt = desc.dataType

# Save data sources and primary input dataset
dc = desc.dataCollection
ds = dc.getValue(0,0)

# Print describe properties
print("Layer name:       " + name)
print("Data type:        " + dt)
print("Input data:       " + ds)
print("Minimum X Extent: " + str(aoi.XMin))
print("Maximum X Extent: " + str(aoi.XMax))
print("Minimum Y Extent: " + str(aoi.YMin))
print("Maximum Y Extent: " + str(aoi.YMax))
```

---

## GetActivePortalURL

## Summary

Returns the URL of the active portal.

## Code Samples

### Example 1

```python
GetActivePortalURL ()
```

### Example 2

```python
import arcpy

# For example: 'http://www.arcgis.com/'
arcpy.GetActivePortalURL()
```

### Example 3

```python
import arcpy

# For example: 'http://www.arcgis.com/'
arcpy.GetActivePortalURL()
```

---

## GetAllMessages

## Summary

Returns the message types, return codes, and message strings from the previously run tool.

## Code Samples

### Example 1

```python
GetAllMessages ()
```

### Example 2

```python
import arcpy
from pprint import pprint

arcpy.management.CreateSpatialReference()
pprint(arcpy.GetAllMessages(), width=120)

"""
[[0, 'Start Time: Wednesday, March 22, 2023 5:01:17 PM'],
 [0, 0, 'Spatial Reference = Unknown'],
 [0, 0, 'XY Domain (XMin,YMin XMax,YMax) = -450359962737.049,-450359962737.049 450359962737.049,450359962737.049'],
 [0, 0, 'Z Domain (Min,Max) = -100000,900719825474.099'],
 [0, 0, 'M Domain (Min,Max) = -100000,900719825474.099'],
 [3, 0, 'Succeeded at Wednesday, March 22, 2023 5:01:18 PM (Elapsed Time: 0.34 seconds)']]
"""

try:
    arcpy.management.CopyFeatures('c:/data/infc.shp', 'c:/data/infc.shp')
except arcpy.ExecuteError:
    pprint.pprint(arcpy.GetAllMessages(), width=100)

"""
[[2, 0, 'Start Time: Wednesday, March 22, 2023 5:06:14 PM'],
 [100, -2147467259, 'Failed to execute. Parameters are not valid.'],
 [100, 733, 'ERROR 000733: Output Feature Class: Same as input Input Features'],
 [100, -2147467259, 'Failed to execute (CopyFeatures).'],
 [3, 0, 'Failed at Wednesday, March 22, 2023 5:06:15 PM (Elapsed Time: 1.16 seconds)']]
"""
```

### Example 3

```python
import arcpy
from pprint import pprint

arcpy.management.CreateSpatialReference()
pprint(arcpy.GetAllMessages(), width=120)

"""
[[0, 'Start Time: Wednesday, March 22, 2023 5:01:17 PM'],
 [0, 0, 'Spatial Reference = Unknown'],
 [0, 0, 'XY Domain (XMin,YMin XMax,YMax) = -450359962737.049,-450359962737.049 450359962737.049,450359962737.049'],
 [0, 0, 'Z Domain (Min,Max) = -100000,900719825474.099'],
 [0, 0, 'M Domain (Min,Max) = -100000,900719825474.099'],
 [3, 0, 'Succeeded at Wednesday, March 22, 2023 5:01:18 PM (Elapsed Time: 0.34 seconds)']]
"""

try:
    arcpy.management.CopyFeatures('c:/data/infc.shp', 'c:/data/infc.shp')
except arcpy.ExecuteError:
    pprint.pprint(arcpy.GetAllMessages(), width=100)

"""
[[2, 0, 'Start Time: Wednesday, March 22, 2023 5:06:14 PM'],
 [100, -2147467259, 'Failed to execute. Parameters are not valid.'],
 [100, 733, 'ERROR 000733: Output Feature Class: Same as input Input Features'],
 [100, -2147467259, 'Failed to execute (CopyFeatures).'],
 [3, 0, 'Failed at Wednesday, March 22, 2023 5:06:15 PM (Elapsed Time: 1.16 seconds)']]
"""
```

---

## GetArgumentCount

## Summary

Returns the number of arguments passed to the script.

## Code Samples

### Example 1

```python
GetArgumentCount ()
```

### Example 2

```python
import arcpy

# Set workspace
arcpy.env.workspace = "c:/data/airport.gdb"

# Set local variables
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_feature_class = arcpy.GetParameterAsText(2)
xy_tolerance = arcpy.GetParameterAsText(3)

# Check for required number of arguments
if arcpy.GetArgumentCount() < 3:
    print("3 arguments required for Clip_analysis tool")

# Execute Clip tool
try:
    arcpy.Clip_analysis(in_features, clip_features,
                        out_feature_class, xy_tolerance)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy

# Set workspace
arcpy.env.workspace = "c:/data/airport.gdb"

# Set local variables
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_feature_class = arcpy.GetParameterAsText(2)
xy_tolerance = arcpy.GetParameterAsText(3)

# Check for required number of arguments
if arcpy.GetArgumentCount() < 3:
    print("3 arguments required for Clip_analysis tool")

# Execute Clip tool
try:
    arcpy.Clip_analysis(in_features, clip_features,
                        out_feature_class, xy_tolerance)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 4

```python
import arcpy

args = [arcpy.GetParameterAsText(i) for i in range(arcpy.GetArgumentCount())]
```

### Example 5

```python
import arcpy

args = [arcpy.GetParameterAsText(i) for i in range(arcpy.GetArgumentCount())]
```

---

## GetIDMessage

## Summary

Get the string of the error or warning ID message.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| message_ID | The geoprocessing message ID. | Integer |

## Code Samples

### Example 1

```python
GetIDMessage (message_ID)
```

### Example 2

```python
import arcpy

message = arcpy.GetIDMessage(84001)

# The returned value should be: u'Reading Data....'
arcpy.AddMessage(message)
```

### Example 3

```python
import arcpy

message = arcpy.GetIDMessage(84001)

# The returned value should be: u'Reading Data....'
arcpy.AddMessage(message)
```

---

## GetImageEXIFProperties

## Summary

Returns an image file’s Exchangeable image file format (EXIF) metadata, including XMP format.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| geotagged_image | The image file path that contains geotagged EXIF properties.(The default value is None) | String |

## Code Samples

### Example 1

```python
GetImageEXIFProperties (geotagged_image)
```

### Example 2

```python
[7.172077777777778, 50.68396666666666, 60.0, {'width': 2592, 'height': 1944, 'planes': 3, 'EXIF_KIND': 'IMAGE', 'EXIF_BAND_COUNT': 3, 'EXIF_HAS_TABLE': False, 'EXIF_HAS_XFORM': False, 'EXIF_DateTimeOriginal': '2009:01:13 11:38:12', 'EXIF_FocalLength': 11.3, 'EXIF_PixelXDimension': 2592, 'EXIF_PixelYDimension': 1944, 'EXIF_Model': 'Caplio 500SE ', 'EXIF_Make': 'RICOH ', 'EXIF_GPSImgDirection': 27.7, 'EXIF_GPSImgDirectionRef': 'M', 'EXIF_Orientation': '1'}]
```

### Example 3

```python
[7.172077777777778, 50.68396666666666, 60.0, {'width': 2592, 'height': 1944, 'planes': 3, 'EXIF_KIND': 'IMAGE', 'EXIF_BAND_COUNT': 3, 'EXIF_HAS_TABLE': False, 'EXIF_HAS_XFORM': False, 'EXIF_DateTimeOriginal': '2009:01:13 11:38:12', 'EXIF_FocalLength': 11.3, 'EXIF_PixelXDimension': 2592, 'EXIF_PixelYDimension': 1944, 'EXIF_Model': 'Caplio 500SE ', 'EXIF_Make': 'RICOH ', 'EXIF_GPSImgDirection': 27.7, 'EXIF_GPSImgDirectionRef': 'M', 'EXIF_Orientation': '1'}]
```

### Example 4

```python
import arcpy

# Get exif metadata in JSON format from image
arcpy.GetImageEXIFProperties(r"c:/droneimages/Picture044.jpg")
```

### Example 5

```python
import arcpy

# Get exif metadata in JSON format from image
arcpy.GetImageEXIFProperties(r"c:/droneimages/Picture044.jpg")
```

---

## GetInstallInfo

## Summary

Returns a dictionary that contains information about the installation.

## Code Samples

### Example 1

```python
GetInstallInfo ()
```

### Example 2

```python
import arcpy

# Use the dictionary iteritems to iterate through the key/value pairs from 
# GetInstallInfo.
d = arcpy.GetInstallInfo()
for key, value in list(d.items()):
    # Print a formatted string of the install key and its value
    print("{:<13} : {}".format(key, value))
```

### Example 3

```python
import arcpy

# Use the dictionary iteritems to iterate through the key/value pairs from 
# GetInstallInfo.
d = arcpy.GetInstallInfo()
for key, value in list(d.items()):
    # Print a formatted string of the install key and its value
    print("{:<13} : {}".format(key, value))
```

### Example 4

```python
import arcpy
print(arcpy.GetInstallInfo()['Version'])
```

### Example 5

```python
import arcpy
print(arcpy.GetInstallInfo()['Version'])
```

---

## GetLogHistory

## Summary

Determines whether history logging is active.

## Code Samples

### Example 1

```python
GetLogHistory ()
```

### Example 2

```python
import arcpy
if arcpy.GetLogHistory():
    arcpy.SetLogHistory(False)
```

### Example 3

```python
import arcpy
if arcpy.GetLogHistory():
    arcpy.SetLogHistory(False)
```

---

## GetLogMetadata

## Summary

Determines whether geoprocessing operations are written to dataset metadata.

## Code Samples

### Example 1

```python
GetLogMetadata ()
```

### Example 2

```python
import arcpy
if arcpy.GetLogMetadata():
    arcpy.SetLogMetadata(False)
```

### Example 3

```python
import arcpy
if arcpy.GetLogMetadata():
    arcpy.SetLogMetadata(False)
```

---

## GetMaxSeverity

## Summary

Gets the maximum severity returned from the previously run tool.

## Code Samples

### Example 1

```python
GetMaxSeverity ()
```

### Example 2

```python
import arcpy

# Set current workspace
arcpy.env.workspace = "c:/data/mydata.gdb"

try:
    arcpy.analysis.Clip("Roads", "County", "Roads_Clip")
except arcpy.ExecuteError:
    pass

severity = arcpy.GetMaxSeverity()

if severity == 2:
    # If the tool returned an error
    print(f"Error returned \n{arcpy.GetMessages(2)}")
elif severity == 1:
    # If the tool returned no errors, but returned a warning
    print(f"Warning returned \n{arcpy.GetMessages(1)}")
else:
    # If the tool did not return an error or a warning
    print(arcpy.GetMessages())
```

### Example 3

```python
import arcpy

# Set current workspace
arcpy.env.workspace = "c:/data/mydata.gdb"

try:
    arcpy.analysis.Clip("Roads", "County", "Roads_Clip")
except arcpy.ExecuteError:
    pass

severity = arcpy.GetMaxSeverity()

if severity == 2:
    # If the tool returned an error
    print(f"Error returned \n{arcpy.GetMessages(2)}")
elif severity == 1:
    # If the tool returned no errors, but returned a warning
    print(f"Warning returned \n{arcpy.GetMessages(1)}")
else:
    # If the tool did not return an error or a warning
    print(arcpy.GetMessages())
```

---

## GetMessage

## Summary

Returns a geoprocessing tool message by index position.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The message to retrieve. | Integer |

## Code Samples

### Example 1

```python
GetMessage (index)
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

arcpy.management.GetCount(fc)

# Print the first and last message returned by the last
# tool run (GetCount).
message_count = arcpy.GetMessageCount()
print(arcpy.GetMessage(0))
print(arcpy.GetMessage(message_count - 1))
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)

arcpy.management.GetCount(fc)

# Print the first and last message returned by the last
# tool run (GetCount).
message_count = arcpy.GetMessageCount()
print(arcpy.GetMessage(0))
print(arcpy.GetMessage(message_count - 1))
```

---

## GetMessageCount

## Summary

Returns a numeric count of all the returned messages from the previously run tool.

## Code Samples

### Example 1

```python
GetMessageCount ()
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)
arcpy.management.GetCount(fc)

# Print the first and last geoprocessing tool messages
message_count = arcpy.GetMessageCount()
print(arcpy.GetMessage(0))
print(arcpy.GetMessage(message_count - 1))
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)
arcpy.management.GetCount(fc)

# Print the first and last geoprocessing tool messages
message_count = arcpy.GetMessageCount()
print(arcpy.GetMessage(0))
print(arcpy.GetMessage(message_count - 1))
```

---

## GetMessages

## Summary

Returns the geoprocessing messages from a tool by a specified severity level.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| severity | Specifies the type of messages to be returned. 0—Informative, warning, and error messages are returned.1—Only warning messages are returned.2—Only error messages are returned.Not specifying a severity level will return all types of messages.(The default value is 0) | Integer |

## Code Samples

### Example 1

```python
GetMessages ({severity})
```

### Example 2

```python
import arcpy

fc = arcpy.GetParameterAsText(0)
arcpy.GetCount_management(fc)

# Print all of the geoprocessing messages returned by the
#  last tool (GetCount)
print(arcpy.GetMessages())
```

### Example 3

```python
import arcpy

fc = arcpy.GetParameterAsText(0)
arcpy.GetCount_management(fc)

# Print all of the geoprocessing messages returned by the
#  last tool (GetCount)
print(arcpy.GetMessages())
```

---

## GetPackageInfo

## Summary

Returns a dictionary that contains information about a package file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| input_package | The path to the package file. | String |

## Code Samples

### Example 1

```python
GetPackageInfo (input_package)
```

### Example 2

```python
import arcpy
import pprint

pprint.pprint(arcpy.GetPackageInfo("c:/packages/maps/Leith.mpkx"))
```

### Example 3

```python
import arcpy
import pprint

pprint.pprint(arcpy.GetPackageInfo("c:/packages/maps/Leith.mpkx"))
```

---

## GetParameter

## Summary

From the parameter list, select the desired parameter by its index or its name. The parameter is returned as an object.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The index position of the parameter, or the name of the parameter. | Integer |

## Code Samples

### Example 1

```python
GetParameter (index)
```

### Example 2

```python
import arcpy

# Get the spatial reference from the tool dialog.
spatial_ref = arcpy.GetParameter(0)

# Display the Spatial Reference properties
arcpy.AddMessage("Name is: {0}".format(spatial_ref.name))
arcpy.AddMessage("Type is: {0}".format(spatial_ref.type))
arcpy.AddMessage("Factory code is: {0}".format(spatial_ref.factoryCode))
```

### Example 3

```python
import arcpy

# Get the spatial reference from the tool dialog.
spatial_ref = arcpy.GetParameter(0)

# Display the Spatial Reference properties
arcpy.AddMessage("Name is: {0}".format(spatial_ref.name))
arcpy.AddMessage("Type is: {0}".format(spatial_ref.type))
arcpy.AddMessage("Factory code is: {0}".format(spatial_ref.factoryCode))
```

### Example 4

```python
import arcpy

# Get the spatial reference from the tool dialog.
spatial_ref = arcpy.GetParameter("in_spatial_reference")

# Display the Spatial Reference properties
arcpy.AddMessage(f"Name is: {spatial_ref.name}")
arcpy.AddMessage(f"Type is: {spatial_ref.type}")
arcpy.AddMessage(f"Factory code is: {spatial_ref.factoryCode}")
```

### Example 5

```python
import arcpy

# Get the spatial reference from the tool dialog.
spatial_ref = arcpy.GetParameter("in_spatial_reference")

# Display the Spatial Reference properties
arcpy.AddMessage(f"Name is: {spatial_ref.name}")
arcpy.AddMessage(f"Type is: {spatial_ref.type}")
arcpy.AddMessage(f"Factory code is: {spatial_ref.factoryCode}")
```

---

## GetParameterAsText

## Summary

Gets the specified parameter as a text string by its index position or parameter name.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The index position of the parameter, or the name of the parameter. | Integer |

## Code Samples

### Example 1

```python
GetParameterAsText (index)
```

### Example 2

```python
import os
import arcpy

# Set the input workspace, get the feature class name to copy
#  and the output location.
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

out_featureclass = os.path.join(out_workspace,
                                os.path.basename(in_featureclass))

# Copy feature class to output location
arcpy.management.CopyFeatures(in_featureclass, out_featureclass)
```

### Example 3

```python
import os
import arcpy

# Set the input workspace, get the feature class name to copy
#  and the output location.
arcpy.env.workspace = arcpy.GetParameterAsText(0)
in_featureclass = arcpy.GetParameterAsText(1)
out_workspace = arcpy.GetParameterAsText(2)

out_featureclass = os.path.join(out_workspace,
                                os.path.basename(in_featureclass))

# Copy feature class to output location
arcpy.management.CopyFeatures(in_featureclass, out_featureclass)
```

### Example 4

```python
import os
import arcpy

# Set the input workspace, get the feature class name to copy
#  and the output location.
arcpy.env.workspace = arcpy.GetParameterAsText("workspace")
in_featureclass = arcpy.GetParameterAsText("in_featureclass")
out_workspace = arcpy.GetParameterAsText("out_workspace")

out_featureclass = os.path.join(out_workspace,
                                os.path.basename(in_featureclass))

# Copy feature class to output location
arcpy.management.CopyFeatures(in_featureclass, out_featureclass)
```

### Example 5

```python
import os
import arcpy

# Set the input workspace, get the feature class name to copy
#  and the output location.
arcpy.env.workspace = arcpy.GetParameterAsText("workspace")
in_featureclass = arcpy.GetParameterAsText("in_featureclass")
out_workspace = arcpy.GetParameterAsText("out_workspace")

out_featureclass = os.path.join(out_workspace,
                                os.path.basename(in_featureclass))

# Copy feature class to output location
arcpy.management.CopyFeatures(in_featureclass, out_featureclass)
```

---

## GetParameterCount

## Summary

Returns a count of the parameter values for the specified tool. If the tool is contained in a custom toolbox, use the ImportToolbox function to access the custom tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| tool_name | The name of the tool for which the number of parameters will be returned. | String |

## Code Samples

### Example 1

```python
GetParameterCount (tool_name)
```

### Example 2

```python
import arcpy

print(arcpy.GetParameterCount("Buffer_analysis"))
```

### Example 3

```python
import arcpy

print(arcpy.GetParameterCount("Buffer_analysis"))
```

---

## GetParameterInfo

## Summary

Returns a list of parameter objects for a given tool and is commonly used in a script tool's ToolValidator class.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| tool_name | The tool name. Including the toolbox alias will help to resolve any conflicts with duplicate tool names. Note:When the GetParameterInfo function is used as part of a script tool's ToolValidator class, the tool_name argument is optional. | String |

## Code Samples

### Example 1

```python
GetParameterInfo (tool_name)
```

### Example 2

```python
import arcpy

# Load tool parameter objects into list.
params = arcpy.GetParameterInfo("HotSpots")

for param in params:
    print("Name: {}, Type: {}, Value: {}".format(
        param.name, param.parameterType, param.value))
```

### Example 3

```python
import arcpy

# Load tool parameter objects into list.
params = arcpy.GetParameterInfo("HotSpots")

for param in params:
    print("Name: {}, Type: {}, Value: {}".format(
        param.name, param.parameterType, param.value))
```

### Example 4

```python
import os
import arcpy

# Set data variables for Clip tool.
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_feature_class = arcpy.GetParameterAsText(2)

# Execute Clip tool
output = arcpy.Clip_analysis(in_features, clip_features,
                             out_feature_class)[0]

# Get parameter objects
params = arcpy.GetParameterInfo()

# Use describe on result object and get shape type.
desc = arcpy.Describe(output)

# Set symbology property for out_feature_class parameter
# Layer files are located in same folder as the .py file
lyr_location = os.path.dirname(__file__)

if desc.shapeType == "Polygon":
    params[2].symbology = os.path.join(lyr_location, "Polygon.lyr")
elif desc.shapeType == "Polyline":
    params[2].symbology = os.path.join(lyr_location, "Polyline.lyr")
else:
    params[2].symbology = os.path.join(lyr_location, "Point.lyr")
```

### Example 5

```python
import os
import arcpy

# Set data variables for Clip tool.
in_features = arcpy.GetParameterAsText(0)
clip_features = arcpy.GetParameterAsText(1)
out_feature_class = arcpy.GetParameterAsText(2)

# Execute Clip tool
output = arcpy.Clip_analysis(in_features, clip_features,
                             out_feature_class)[0]

# Get parameter objects
params = arcpy.GetParameterInfo()

# Use describe on result object and get shape type.
desc = arcpy.Describe(output)

# Set symbology property for out_feature_class parameter
# Layer files are located in same folder as the .py file
lyr_location = os.path.dirname(__file__)

if desc.shapeType == "Polygon":
    params[2].symbology = os.path.join(lyr_location, "Polygon.lyr")
elif desc.shapeType == "Polyline":
    params[2].symbology = os.path.join(lyr_location, "Polyline.lyr")
else:
    params[2].symbology = os.path.join(lyr_location, "Point.lyr")
```

---

## GetParameterValue

## Summary

For a specified tool name, returns the default value of the desired parameter. The parameter is specified by either index or parameter name.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| tool_name | The tool name for which the parameter default value will be returned. | String |
| index | The index position of the parameter or the name of the parameter. | Integer |

## Code Samples

### Example 1

```python
GetParameterValue (tool_name, index)
```

### Example 2

```python
import arcpy

# Returns 'POLYGON'
print(arcpy.GetParameterValue("CreateFeatureClass_management", 2))
```

### Example 3

```python
import arcpy

# Returns 'POLYGON'
print(arcpy.GetParameterValue("CreateFeatureClass_management", 2))
```

### Example 4

```python
import arcpy

# Returns 'POLYGON'
print(arcpy.GetParameterValue("CreateFeatureClass_management", "geometry_type"))
```

### Example 5

```python
import arcpy

# Returns 'POLYGON'
print(arcpy.GetParameterValue("CreateFeatureClass_management", "geometry_type"))
```

---

## GetPortalDescription

## Summary

Returns a dictionary of portal information.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| portal_URL | The portal URL. If unspecified, the active portal will be used. | String |

## Code Samples

### Example 1

```python
GetPortalDescription ({portal_URL})
```

### Example 2

```python
import arcpy

portal_desc = arcpy.GetPortalDescription()
helper_services = portal_desc['helperServices']
```

### Example 3

```python
import arcpy

portal_desc = arcpy.GetPortalDescription()
helper_services = portal_desc['helperServices']
```

### Example 4

```python
import arcpy

portal_desc = arcpy.GetPortalDescription()
user_name = portal_desc['user']['fullName']
user_privileges = portal_desc['user']['privileges']
```

### Example 5

```python
import arcpy

portal_desc = arcpy.GetPortalDescription()
user_name = portal_desc['user']['fullName']
user_privileges = portal_desc['user']['privileges']
```

---

## GetPortalInfo

## Summary

Returns a dictionary that contains information about available portals.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| portal_URL | The portal URL. The URL returned by GetActivePortalURL is used by default. | String |

## Code Samples

### Example 1

```python
GetPortalInfo ({portal_URL})
```

### Example 2

```python
import arcpy

# For example:
#  {'portal_version': 2.3, 'SSL_enabled': False, 'organization': 
#   'PortalHost 10.2.1', 'role': 'account_publisher', 'organizationtype': ''}
print(arcpy.GetPortalInfo(portal_URL=arcpy.GetActivePortalURL()))
```

### Example 3

```python
import arcpy

# For example:
#  {'portal_version': 2.3, 'SSL_enabled': False, 'organization': 
#   'PortalHost 10.2.1', 'role': 'account_publisher', 'organizationtype': ''}
print(arcpy.GetPortalInfo(portal_URL=arcpy.GetActivePortalURL()))
```

---

## GetReturnCode

## Summary

Returns the message error code for a geoprocessing message.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The specified position of the message in the returned list of messages, warnings, or errors. | Integer |

## Code Samples

### Example 1

```python
GetReturnCode (index)
```

### Example 2

```python
import arcpy

arcpy.env.workspace = "c:/census/data.gdb"
arcpy.analysis.Erase("housing", "income", "low_income")

# Return the return code of the message in index
# position 3 (4th message)
print(arcpy.GetReturnCode(3))
```

### Example 3

```python
import arcpy

arcpy.env.workspace = "c:/census/data.gdb"
arcpy.analysis.Erase("housing", "income", "low_income")

# Return the return code of the message in index
# position 3 (4th message)
print(arcpy.GetReturnCode(3))
```

---

## GetSeverity

## Summary

Gets the severity code (0, 1, 2) of the specified message by index.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | Numeric index position of the message in the stack. | Integer |

## Code Samples

### Example 1

```python
GetSeverity (index)
```

### Example 2

```python
import arcpy

in_featureclass = arcpy.GetParameterAsText(0)
out_featureclass = arcpy.GetParameterAsText(1)

# Run the CopyFeatures tool. If it fails, print out the
# severity and message for each message.
try:
    arcpy.CopyFeatures_management(in_featureclass, out_featureclass)
except arcpy.ExecuteError:
    for i in xrange(0, arcpy.GetMessageCount()):
        print('{0}: {1}'.format(arcpy.GetSeverity(i),
                                arcpy.GetMessage(i)))
```

### Example 3

```python
import arcpy

in_featureclass = arcpy.GetParameterAsText(0)
out_featureclass = arcpy.GetParameterAsText(1)

# Run the CopyFeatures tool. If it fails, print out the
# severity and message for each message.
try:
    arcpy.CopyFeatures_management(in_featureclass, out_featureclass)
except arcpy.ExecuteError:
    for i in xrange(0, arcpy.GetMessageCount()):
        print('{0}: {1}'.format(arcpy.GetSeverity(i),
                                arcpy.GetMessage(i)))
```

---

## GetSeverityLevel

## Summary

Returns the severity level. The severity level is used to control how geoprocessing tools throw exceptions.

## Code Samples

### Example 1

```python
GetSeverityLevel ()
```

### Example 2

```python
import arcpy
severity_level = arcpy.GetSeverityLevel()
print(severity_level)
```

### Example 3

```python
import arcpy
severity_level = arcpy.GetSeverityLevel()
print(severity_level)
```

---

## GetSigninToken

## Summary

Returns token information when signed in to ArcGIS.com or a local portal.

## Code Samples

### Example 1

```python
GetSigninToken ()
```

### Example 2

```python
import arcpy

token = arcpy.GetSigninToken()
if token is not None:
    print(token['token'])
```

### Example 3

```python
import arcpy

token = arcpy.GetSigninToken()
if token is not None:
    print(token['token'])
```

---

## GetSTACInfo

## Summary

Retrieves information from a SpatioTemporal Asset Catalog (STAC) URL.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| stac_url | The URL of the STAC resource. | String |
| verbose | Specifies the level of information returned. If set to True, detailed information is returned. If set to False, only essential information is returned.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
GetSTACInfo (stac_url, {verbose})
```

### Example 2

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1", verbose=True
)
print(stac_info)
```

### Example 3

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1", verbose=True
)
print(stac_info)
```

### Example 4

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1/collections/landsat-c2-l2",
    verbose=False
)
print(stac_info)
```

### Example 5

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1/collections/landsat-c2-l2",
    verbose=False
)
print(stac_info)
```

### Example 6

```python
import arcpy
    stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/wa_m_4712125_sw_10_060_20191029_20191217"
)
print(stac_info)
```

### Example 7

```python
import arcpy
    stac_info = arcpy.GetSTACInfo(
    "https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/wa_m_4712125_sw_10_060_20191029_20191217"
)
print(stac_info)
```

### Example 8

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://earth-search.aws.element84.com/v1/collections/naip/items", verbose=True
)
print(stac_info)
```

### Example 9

```python
import arcpy
stac_info = arcpy.GetSTACInfo(
    "https://earth-search.aws.element84.com/v1/collections/naip/items", verbose=True
)
print(stac_info)
```

---

## GetSystemEnvironment

## Summary

Gets a specified system environment variable value, such as TEMP.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| environment | The name of the system environment variable. | String |

## Code Samples

### Example 1

```python
GetSystemEnvironment (environment)
```

### Example 2

```python
import arcpy

# Set the scratchWorkspace environment to the value returned
# from the system environment variable TEMP.
arcpy.env.scratchWorkspace = arcpy.GetSystemEnvironment("TEMP")
```

### Example 3

```python
import arcpy

# Set the scratchWorkspace environment to the value returned
# from the system environment variable TEMP.
arcpy.env.scratchWorkspace = arcpy.GetSystemEnvironment("TEMP")
```

---

## Historical Traffic Data

## Summary

Provides information about the historical traffic information stored in the network dataset such as the speed profile table and time slice durations.

## Code Samples

### Example 1

```python
# Name: NDSHistoricalTrafficDataProperties_ex01.py
# Description: Print historical traffic information for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the historical traffic data object
if desc.supportsHistoricalTrafficData:
    traffic = desc.historicalTrafficData
else:
    #If the directions are not set for the network dataset, exit
    print("No historical traffic information")
    sys.exit()

print("Historical Traffic Information ----")
print("Time interval: " , traffic.timeInterval)
print("Time interval units: " , traffic.timeIntervalUnits)
print("First time slice field name: " , traffic.firstTimeSliceFieldName)
print("Last time slice field name: " , traffic.lastTimeSliceFieldName)
print("First time slice start time: " , traffic.firstTimeSliceStartTime)
print("Time slice duration in minutes: ",traffic.timeSliceDurationInMinutes)
print("Profiles table name: ", traffic.profilesTableName)
print("Join table name: ", traffic.joinTableName)
print("Join table base travel time field name: ", traffic.joinTableBaseTravelTimeFieldName)
print("Join table base travel time units: ", traffic.joinTableBaseTravelTimeUnits)
print("Join table ProfileID field names: ", traffic.joinTableProfileIDFieldNames)
```

### Example 2

```python
# Name: NDSHistoricalTrafficDataProperties_ex01.py
# Description: Print historical traffic information for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the historical traffic data object
if desc.supportsHistoricalTrafficData:
    traffic = desc.historicalTrafficData
else:
    #If the directions are not set for the network dataset, exit
    print("No historical traffic information")
    sys.exit()

print("Historical Traffic Information ----")
print("Time interval: " , traffic.timeInterval)
print("Time interval units: " , traffic.timeIntervalUnits)
print("First time slice field name: " , traffic.firstTimeSliceFieldName)
print("Last time slice field name: " , traffic.lastTimeSliceFieldName)
print("First time slice start time: " , traffic.firstTimeSliceStartTime)
print("Time slice duration in minutes: ",traffic.timeSliceDurationInMinutes)
print("Profiles table name: ", traffic.profilesTableName)
print("Join table name: ", traffic.joinTableName)
print("Join table base travel time field name: ", traffic.joinTableBaseTravelTimeFieldName)
print("Join table base travel time units: ", traffic.joinTableBaseTravelTimeUnits)
print("Join table ProfileID field names: ", traffic.joinTableProfileIDFieldNames)
```

---

## ImportCredentials

## Summary

Imports credentials from a GIS server connection file for ArcGIS Server nontoken-based secured services.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| secure_server_connections[secure_server_connections,...] | A list of credentials for secured services. Credentials can be stored in connection files that are created in ArcGIS Pro.The following connection file types are supported:ArcGIS Server (.ags)WMS Server (.wms)WMTS Server (.wmts) | String |

## Code Samples

### Example 1

```python
ImportCredentials (secure_server_connections)
```

### Example 2

```python
import arcpy

# import credentials
secured_credentials = arcpy.ImportCredentials([r"C:\Project\SecuredServices.ags"])
aprx = arcpy.mp.ArcGISProject(r"C:\Project\USA.aprx")
m = aprx.listMaps()[0]

# add secured service to map
m.addDataFromPath('http://SampleServer:6080/arcgis/rest/services/secured/ProjectArea/FeatureServer/0')

# clear credentials when finished
arcpy.ClearCredentials(secured_credentials)
```

### Example 3

```python
import arcpy

# import credentials
secured_credentials = arcpy.ImportCredentials([r"C:\Project\SecuredServices.ags"])
aprx = arcpy.mp.ArcGISProject(r"C:\Project\USA.aprx")
m = aprx.listMaps()[0]

# add secured service to map
m.addDataFromPath('http://SampleServer:6080/arcgis/rest/services/secured/ProjectArea/FeatureServer/0')

# clear credentials when finished
arcpy.ClearCredentials(secured_credentials)
```

---

## ImportToolbox

## Summary

Imports a geoprocessing toolbox for use in ArcPy, allowing access to the toolbox's associated tools.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| input_file | The geoprocessing toolbox to be accessed from ArcPy. | String |
| module_name | If the toolbox does not have an alias, the module_name is required. When a tool is accessed through the ArcPy site package, the toolbox alias where the tool is contained is a required suffix (arcpy.<toolname>_<alias> or arcpy.<alias>.<toolname>). Since ArcPy depends on toolbox aliases to access and run the correct tool, aliases are important when importing custom toolboxes. It is recommended that you define a custom toolbox's alias; however, if the toolbox alias is not defined, a temporary alias can be set as the second parameter. | String |

## Code Samples

### Example 1

```python
import arcpy
arcpy.ImportToolbox('c:/logistics/logistics.ags;World/ServiceAreas')
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 2

```python
import arcpy
arcpy.ImportToolbox('c:/logistics/logistics.ags;World/ServiceAreas')
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 3

```python
import arcpy
tbx = "http://logistics.arcgis.com/arcgis/services;World/ServiceAreas;UseSSOIdentityIfPortalOwned"
arcpy.ImportToolbox(tbx)
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 4

```python
import arcpy
tbx = "http://logistics.arcgis.com/arcgis/services;World/ServiceAreas;UseSSOIdentityIfPortalOwned"
arcpy.ImportToolbox(tbx)
arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 5

```python
import arcpy

token = 'sadsa213d2j32jsdw02dm2'
referrer = 'http://www.arcgis.com/'
tbx = 'http://logistics.arcgis.com/arcgis/services;' + \
      'World/ServiceAreas;token={};{}'.format(token, referrer)
arcpy.ImportToolbox(tbx)
result = arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 6

```python
import arcpy

token = 'sadsa213d2j32jsdw02dm2'
referrer = 'http://www.arcgis.com/'
tbx = 'http://logistics.arcgis.com/arcgis/services;' + \
      'World/ServiceAreas;token={};{}'.format(token, referrer)
arcpy.ImportToolbox(tbx)
result = arcpy.GenerateServiceAreas_ServiceAreas()
```

### Example 7

```python
ImportToolbox (input_file, {module_name})
```

### Example 8

```python
import arcpy

# Import custom toolbox
arcpy.ImportToolbox("c:/tools/My_Analysis_Tools.atbx")

try:
    # Run tool in the custom toolbox.  The tool is identified by the tool name 
    # and the toolbox alias.
    arcpy.GetPoints_myanalysis("c:/data/forest.shp")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 9

```python
import arcpy

# Import custom toolbox
arcpy.ImportToolbox("c:/tools/My_Analysis_Tools.atbx")

try:
    # Run tool in the custom toolbox.  The tool is identified by the tool name 
    # and the toolbox alias.
    arcpy.GetPoints_myanalysis("c:/data/forest.shp")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 10

```python
import arcpy

tbx = 'https://utility.arcgisonline.com/arcgis/rest/services/;' + \
      'Utilities/PrintingTools'
arcpy.ImportToolbox(tbx)
arcpy.PrintingTools.GetLayoutTemplatesInfo()
```

### Example 11

```python
import arcpy

tbx = 'https://utility.arcgisonline.com/arcgis/rest/services/;' + \
      'Utilities/PrintingTools'
arcpy.ImportToolbox(tbx)
arcpy.PrintingTools.GetLayoutTemplatesInfo()
```

---

## InsertCursor

## Summary

Inserts rows of attribute values into a specified feature class or table.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The feature class or table into which rows will be inserted. | String |
| spatial_reference | Coordinates are specified in the spatial_reference provided and converted on the fly to the coordinate system of the dataset. | SpatialReference |

## Code Samples

### Example 1

```python
InsertCursor (dataset, {spatial_reference})
```

### Example 2

```python
import arcpy

# Create an insert cursor for a table
rows = arcpy.InsertCursor("c:/base/data.gdb/roads_lut")

# Create 25 new rows. Set the initial row ID and distance values
for x in range(1, 26):
    row = rows.newRow()
    row.setValue("rowid", x)
    row.setValue("distance", 100)
    rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows
```

### Example 3

```python
import arcpy

# Create an insert cursor for a table
rows = arcpy.InsertCursor("c:/base/data.gdb/roads_lut")

# Create 25 new rows. Set the initial row ID and distance values
for x in range(1, 26):
    row = rows.newRow()
    row.setValue("rowid", x)
    row.setValue("distance", 100)
    rows.insertRow(row)

# Delete cursor and row objects to remove locks on the data
del row
del rows
```

---

## IsBeingEdited

## Summary

Determines whether the given dataset or workspace is in an edit session.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The input dataset or workspace to be checked for an ongoing edit session. | String |

## Code Samples

### Example 1

```python
IsBeingEdited (dataset)
```

### Example 2

```python
import arcpy

arcpy.env.workspace = r"C:\data\myGDB.gdb"

if not arcpy.IsBeingEdited(arcpy.env.workspace):
    edit = arcpy.da.Editor(arcpy.env.workspace)
    edit.startEditing()
```

### Example 3

```python
import arcpy

arcpy.env.workspace = r"C:\data\myGDB.gdb"

if not arcpy.IsBeingEdited(arcpy.env.workspace):
    edit = arcpy.da.Editor(arcpy.env.workspace)
    edit.startEditing()
```

### Example 4

```python
import arcpy

aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]

for lyr in map.listLayers():
    if lyr.isFeatureLayer and arcpy.IsBeingEdited(lyr):
        print(lyr.name)
```

### Example 5

```python
import arcpy

aprx = arcpy.mp.ArcGISProject("CURRENT")
map = aprx.listMaps()[0]

for lyr in map.listLayers():
    if lyr.isFeatureLayer and arcpy.IsBeingEdited(lyr):
        print(lyr.name)
```

---

## IsSynchronous

## Summary

Determines if a tool is running synchronous or asynchronous. When a tool is synchronous, the results are automatically returned, but no other action may be taken until the tool has completed. All non-server tools are synchronous. Server tools may be asynchronous, meaning that once the tool has been submitted to the server, other functionality can be run without waiting, and the results must be explicitly requested from the server.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| tool_name | The name of the tool to determine if it is synchronous. | String |

## Code Samples

### Example 1

```python
IsSynchronous (tool_name)
```

### Example 2

```python
import time
import arcpy

# Add server toolbox from a local ArcGIS Server
arcpy.ImportToolbox("pondermatic;buffertools")

# Create and load a recordset object for the tool's input
record_set = arcpy.RecordSet()
record_set.load("c:/temp/lines.shp")

# Run the server tool
results = arcpy.BufferLines_mytools(record_set, "100")

# If the tool is asynchronous, wait until the task is finished (status = 4)
if not arcpy.IsSynchronous("BufferLines"):
    while results.status < 4:
        time.sleep(0.1)

# Get output from task and export to a feature class on disk
result = results.getOutput(0)
result.save("c:/temp/bufferlines.shp")
```

### Example 3

```python
import time
import arcpy

# Add server toolbox from a local ArcGIS Server
arcpy.ImportToolbox("pondermatic;buffertools")

# Create and load a recordset object for the tool's input
record_set = arcpy.RecordSet()
record_set.load("c:/temp/lines.shp")

# Run the server tool
results = arcpy.BufferLines_mytools(record_set, "100")

# If the tool is asynchronous, wait until the task is finished (status = 4)
if not arcpy.IsSynchronous("BufferLines"):
    while results.status < 4:
        time.sleep(0.1)

# Get output from task and export to a feature class on disk
result = results.getOutput(0)
result.save("c:/temp/bufferlines.shp")
```

---

## Asset Group properties

## Summary

The properties below are returned by the assetGroups object when using Describe on a utility network.

---

## Asset Type properties

## Summary

The properties below are returned by the assetTypes object when using Describe on a utility network.

---

## Junction Source

## Summary

Provides information about junction sources in a network dataset.

## Code Samples

### Example 1

```python
# Name: NDSJunctionSourceProperties_ex01.py
# Description: Print the information about the junction sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Junction sources")

#Get all the junction sources for the network dataset
junctions = desc.junctionSources

if not junctions:
    print(" %*s" % (justify, "(No junction sources)"))
    sys.exit(0)

for junction in junctions:
    print(" %*s: %s" % (justify, "Source Name" , junction.name))
    print(" %*s: %s" % (justify, "Source ID" , str(junction.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", junction.sourceType))
    print(" %*s: %s" % (justify, "Element Type", junction.elementType))
    print(" %*s: %s" % (justify, "Elevation Field",
                        junction.elevationFieldName))
    print(" ")
```

### Example 2

```python
# Name: NDSJunctionSourceProperties_ex01.py
# Description: Print the information about the junction sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

justify = 35
print("------- Junction sources")

#Get all the junction sources for the network dataset
junctions = desc.junctionSources

if not junctions:
    print(" %*s" % (justify, "(No junction sources)"))
    sys.exit(0)

for junction in junctions:
    print(" %*s: %s" % (justify, "Source Name" , junction.name))
    print(" %*s: %s" % (justify, "Source ID" , str(junction.sourceID)))
    print(" %*s: %s" % (justify, "Source Type", junction.sourceType))
    print(" %*s: %s" % (justify, "Element Type", junction.elementType))
    print(" %*s: %s" % (justify, "Elevation Field",
                        junction.elevationFieldName))
    print(" ")
```

---

## Junction Source properties

## Summary

The properties below are returned by the junctionSources object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUN_JunctionSourceProperties.py
Description: This script reports the junction source properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Domain Network Creation Time: {dom.creationTime}")
    print(f"Domain Network Release Number: {dom.releaseNumber}")
    print(f"Domain Network is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Domain Network Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Domain Network Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Domain Network Tier Definition: {dom.tierDefinition}")
    print(f"Domain Network Subnetwork Controller Type: {dom.subnetworkControllerType} \n")

    # Junction Source Properties
    for jSource in dom.junctionSources:
        print(" -- Junction Source Properties -- ")
        print(f"Edge Source Id: {jSource.sourceId}")
        print(f"Object Class ID: {jSource.objectClassId}")
        print(f"Edge Source Name: {jSource.sourceName}")
        print(f"Uses Geometry: {jSource.usesGeometry}")
        print(f"Shape Type: {jSource.shapeType} \n")
        print(f"Feature Class Usage: {jSource.utilityNetworkFeatureClassUsageType}")
        print(f"Asset Type Field Name: {jSource.assetTypeFieldName}")
        print(f"Supported Properties: {jSource.supportedProperties} \n")

        # Asset Group Properties
        for ag in jSource.assetGroups:
            print(" - Asset Group Properties - ")
            print(f"Asset Group Code: {ag.assetGroupCode}")
            print(f"Asset Group Name: {ag.assetGroupName} \n")

            # Asset Type Properties
            for at in ag.assetTypes:
                print(" - Asset Type Properties - ")
                print("Asset Type Code: {0}".format(at.assetTypeCode))
                print("Asset Type Name: {0}".format(at.assetTypeName))
                print("Asset Type Containment View Scale: {0}".format(at.containmentViewScale))
                print("Asset Type Association Delete Type: {0}".format(at.associationDeleteType))
                print("Asset Type Association Role Type: {0}".format(at.associationRoleType))
                print("Asset Type Terminal Configuration Supported: {0}".format(at.isTerminalConfigurationSupported))
                print("Asset Type Terminal Configuration ID: {0}".format(at.terminalConfigurationID))
                print("Asset Type Linear Connectivity Policy Supported: {0}".format(at.isLinearConnectivityPolicySupported))
                print("Asset Type Connectivity Policy: {0}".format(at.connectivityPolicy))
                print("Asset Type Categories: {0}".format(at.categories))
                print("Asset Type Split Content: {0} \n".format(at.splitContent))
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUN_JunctionSourceProperties.py
Description: This script reports the junction source properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Domain Network Creation Time: {dom.creationTime}")
    print(f"Domain Network Release Number: {dom.releaseNumber}")
    print(f"Domain Network is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Domain Network Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Domain Network Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Domain Network Tier Definition: {dom.tierDefinition}")
    print(f"Domain Network Subnetwork Controller Type: {dom.subnetworkControllerType} \n")

    # Junction Source Properties
    for jSource in dom.junctionSources:
        print(" -- Junction Source Properties -- ")
        print(f"Edge Source Id: {jSource.sourceId}")
        print(f"Object Class ID: {jSource.objectClassId}")
        print(f"Edge Source Name: {jSource.sourceName}")
        print(f"Uses Geometry: {jSource.usesGeometry}")
        print(f"Shape Type: {jSource.shapeType} \n")
        print(f"Feature Class Usage: {jSource.utilityNetworkFeatureClassUsageType}")
        print(f"Asset Type Field Name: {jSource.assetTypeFieldName}")
        print(f"Supported Properties: {jSource.supportedProperties} \n")

        # Asset Group Properties
        for ag in jSource.assetGroups:
            print(" - Asset Group Properties - ")
            print(f"Asset Group Code: {ag.assetGroupCode}")
            print(f"Asset Group Name: {ag.assetGroupName} \n")

            # Asset Type Properties
            for at in ag.assetTypes:
                print(" - Asset Type Properties - ")
                print("Asset Type Code: {0}".format(at.assetTypeCode))
                print("Asset Type Name: {0}".format(at.assetTypeName))
                print("Asset Type Containment View Scale: {0}".format(at.containmentViewScale))
                print("Asset Type Association Delete Type: {0}".format(at.associationDeleteType))
                print("Asset Type Association Role Type: {0}".format(at.associationRoleType))
                print("Asset Type Terminal Configuration Supported: {0}".format(at.isTerminalConfigurationSupported))
                print("Asset Type Terminal Configuration ID: {0}".format(at.terminalConfigurationID))
                print("Asset Type Linear Connectivity Policy Supported: {0}".format(at.isLinearConnectivityPolicySupported))
                print("Asset Type Connectivity Policy: {0}".format(at.connectivityPolicy))
                print("Asset Type Categories: {0}".format(at.categories))
                print("Asset Type Split Content: {0} \n".format(at.splitContent))
```

---

## Landmark Source

## Summary

The Landmark Source object provides information about the configuration of landmarks used in generating driving directions.

## Code Samples

### Example 1

```python
# Name: NDSLandmarks_ex01.py
# Description: Print information about the directions landmarks associated
#              with edge sources in the network dataset.

import arcpy
import sys

def printLandmarkInfo(landmarks):
    for lm in landmarks:
        print("\nLandmarks feature class name:", lm.featureClassName)
        print("Label field name:", lm.labelFieldName)
        print("Level field name:", lm.levelFieldName)
        print("Search tolerance:", lm.searchTolerance)
        print("Search tolerance units:", lm.searchToleranceUnits)
        print("Landmarks are spatial:", lm.useSpatialSearch)

network = r"C:/Data/NetworkDatasetWithLandmarks.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("\n--------------------")
    print("Edge source name: " , source.name)
    # Get the directions information specific to this edge source
    sDir = source.sourceDirections
    # Check if the edge source has turn and confirmation landmarks associated with it.
    # If so, print some information about the landmarks.
    if hasattr(sDir, "landmarkEventSources"):
        landmarkEventSources = sDir.landmarkEventSources
        print("\n--Confirmation landmark information--")
        printLandmarkInfo(landmarkEventSources)
    else:
        print("Source does not have confirmation landmarks.")
    if hasattr(sDir, "landmarkManeuverSources"):
        landmarkManeuverSources = sDir.landmarkManeuverSources
        print("\n--Turn landmark information--")
        printLandmarkInfo(landmarkManeuverSources)
    else:
        print("Source does not have turn landmarks.")
```

### Example 2

```python
# Name: NDSLandmarks_ex01.py
# Description: Print information about the directions landmarks associated
#              with edge sources in the network dataset.

import arcpy
import sys

def printLandmarkInfo(landmarks):
    for lm in landmarks:
        print("\nLandmarks feature class name:", lm.featureClassName)
        print("Label field name:", lm.labelFieldName)
        print("Level field name:", lm.levelFieldName)
        print("Search tolerance:", lm.searchTolerance)
        print("Search tolerance units:", lm.searchToleranceUnits)
        print("Landmarks are spatial:", lm.useSpatialSearch)

network = r"C:/Data/NetworkDatasetWithLandmarks.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("\n--------------------")
    print("Edge source name: " , source.name)
    # Get the directions information specific to this edge source
    sDir = source.sourceDirections
    # Check if the edge source has turn and confirmation landmarks associated with it.
    # If so, print some information about the landmarks.
    if hasattr(sDir, "landmarkEventSources"):
        landmarkEventSources = sDir.landmarkEventSources
        print("\n--Confirmation landmark information--")
        printLandmarkInfo(landmarkEventSources)
    else:
        print("Source does not have confirmation landmarks.")
    if hasattr(sDir, "landmarkManeuverSources"):
        landmarkManeuverSources = sDir.landmarkManeuverSources
        print("\n--Turn landmark information--")
        printLandmarkInfo(landmarkManeuverSources)
    else:
        print("Source does not have turn landmarks.")
```

---

## LAS Dataset properties

## Summary

The Describe function returns the following properties for LAS dataset files. The File and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

desc = arcpy.Describe(r'E:\GIS_Data\lidar\test_bmore.lasd')

if desc.usesRelativePath: 
    pathType = 'Relative'
else: pathType = 'Absolute'

# Determine state of statistics
if desc.needsUpdateStatistics:
    if desc.hasStatistics:
        statistics = 'Out-of-date'
    else:
        statistics = 'Missing'
else:
    statistics = 'Current'


print('LAS Dataset Name: {0} \r'\
      'Point Count: {1} \r'\
      'Surface Constraint Count: {2} \r'\
      'Path Type: {3} \r'\
      'Statistics Status: {4}'.format(desc.basename, desc.pointCount, 
                                      desc.constraintCount, pathType,
                                      statistics))
```

### Example 2

```python
import arcpy

desc = arcpy.Describe(r'E:\GIS_Data\lidar\test_bmore.lasd')

if desc.usesRelativePath: 
    pathType = 'Relative'
else: pathType = 'Absolute'

# Determine state of statistics
if desc.needsUpdateStatistics:
    if desc.hasStatistics:
        statistics = 'Out-of-date'
    else:
        statistics = 'Missing'
else:
    statistics = 'Current'


print('LAS Dataset Name: {0} \r'\
      'Point Count: {1} \r'\
      'Surface Constraint Count: {2} \r'\
      'Path Type: {3} \r'\
      'Statistics Status: {4}'.format(desc.basename, desc.pointCount, 
                                      desc.constraintCount, pathType,
                                      statistics))
```

---

## Layer properties

## Summary

The Describe function returns the following properties for Layers. The Dataset property group is also supported, as well as the properties of the data type, the layer references. For example, a layer that references a feature class will have access to the Feature Class property group, while a layer that references a raster dataset will have access to the Raster Dataset property group.

## Code Samples

### Example 1

```python
import arcpy

# Create an in memory feature layer from a feature class.
#
arcpy.MakeFeatureLayer_management(
        "C:/data/chesapeake.gdb/bayshed",
        "mainlines_layer")

# Create a Describe object from the feature layer.
#
desc = arcpy.Describe("mainlines_layer")

# Print some properties of the feature layer, and its featureclass.
#
print("Name String:        " + desc.nameString)
print("Where Clause:       " + desc.whereClause)
print("Feature class type: " + desc.featureClass.featureType)
```

### Example 2

```python
import arcpy

# Create an in memory feature layer from a feature class.
#
arcpy.MakeFeatureLayer_management(
        "C:/data/chesapeake.gdb/bayshed",
        "mainlines_layer")

# Create a Describe object from the feature layer.
#
desc = arcpy.Describe("mainlines_layer")

# Print some properties of the feature layer, and its featureclass.
#
print("Name String:        " + desc.nameString)
print("Where Clause:       " + desc.whereClause)
print("Feature class type: " + desc.featureClass.featureType)
```

### Example 3

```python
import arcpy


# Create a Describe object from a .lyr file.
#
desc = arcpy.Describe("c:/data/water_pipes.lyr")

# Print some properties of the feature layer
#
print("Name String:        " + desc.nameString)
print("Where Clause:       " + desc.whereClause)

# Find out if the layer represents a feature class
if desc.dataElement.dataType == "FeatureClass":
    print("Feature class:      " + desc.dataElement.catalogPath)
    print("Feature class Type: " + desc.featureClass.featureType)
else:
    print("Not a regular feature class")
```

### Example 4

```python
import arcpy


# Create a Describe object from a .lyr file.
#
desc = arcpy.Describe("c:/data/water_pipes.lyr")

# Print some properties of the feature layer
#
print("Name String:        " + desc.nameString)
print("Where Clause:       " + desc.whereClause)

# Find out if the layer represents a feature class
if desc.dataElement.dataType == "FeatureClass":
    print("Feature class:      " + desc.dataElement.catalogPath)
    print("Feature class Type: " + desc.featureClass.featureType)
else:
    print("Not a regular feature class")
```

---

## LinearUnitConversionFactor

## Summary

Returns the factor for converting a distance measurement to a different linear unit.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| from_unit | The original or source linear unit.Kilometers—KilometersMeters—MetersDecimeters—DecimetersMillimeters—MillimetersCentimeters—CentimetersNauticalMilesInt—International nautical milesMilesInt—Statute milesYardsInt—International yardsFeetInt—International feetInchesInt—International inchesNauticalMilesUS—US survey nautical milesMilesUS—US survey milesYardsUS—US survey yardsFeetUS—US survey feetInchesUS—US survey inchesPoints—Points | String |
| to_unit | The target or destination linear unit.Kilometers—KilometersMeters—MetersDecimeters—DecimetersMillimeters—MillimetersCentimeters—CentimetersNauticalMilesInt—International nautical milesMilesInt—Statute milesYardsInt—International yardsFeetInt—International feetInchesInt—International inchesNauticalMilesUS—US survey nautical milesMilesUS—US survey milesYardsUS—US survey yardsFeetUS—US survey feetInchesUS—US survey inchesPoints—Points | String |

## Code Samples

### Example 1

```python
LinearUnitConversionFactor (from_unit, to_unit)
```

### Example 2

```python
import arcpy

# Convert 620.5 MilesInt to Kilometers
620.5 * arcpy.LinearUnitConversionFactor(from_unit="MilesInt", to_unit="Kilometers")

print(area)  # This will print a value of 998.597952
```

### Example 3

```python
import arcpy

# Convert 620.5 MilesInt to Kilometers
620.5 * arcpy.LinearUnitConversionFactor(from_unit="MilesInt", to_unit="Kilometers")

print(area)  # This will print a value of 998.597952
```

### Example 4

```python
import arcpy
import locale
import sys

dist = arcpy.GetParameter(n)  # Update n to the parameter index
dist_value, dist_unit = dist.split(" ")  # For example, "10 Kilometers"

# Convert the distance into "Meters" as needed later in this script
try:
    conv_factor = arcpy.LinearUnitConversionFactor(dist_unit, "Meters")
except ValueError as e:
    # If fails, the likely distance unit is "Unknown" or "Decimal Degrees".
    # Add code to either deal with it or produce an appropriate error as shown below.
    arcpy.AddError('Invalid linear unit type.')
    sys.exit()

# Apply the conv_factor to the supplied value
# locale.atof is required for locales that don't use a period as the separator
dist_m = locale.atof(dist_value) * conv_factor
```

### Example 5

```python
import arcpy
import locale
import sys

dist = arcpy.GetParameter(n)  # Update n to the parameter index
dist_value, dist_unit = dist.split(" ")  # For example, "10 Kilometers"

# Convert the distance into "Meters" as needed later in this script
try:
    conv_factor = arcpy.LinearUnitConversionFactor(dist_unit, "Meters")
except ValueError as e:
    # If fails, the likely distance unit is "Unknown" or "Decimal Degrees".
    # Add code to either deal with it or produce an appropriate error as shown below.
    arcpy.AddError('Invalid linear unit type.')
    sys.exit()

# Apply the conv_factor to the supplied value
# locale.atof is required for locales that don't use a period as the separator
dist_m = locale.atof(dist_value) * conv_factor
```

---

## ListDatasets

## Summary

Returns a list of datasets in the current workspace. Search conditions can be specified for the dataset name and dataset type to limit the list that is returned.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| feature_type | Specifies the type of dataset that will be returned.Coverage—Coverages will be returned.Feature—Coverages or geodatabase datasets will be returned, depending on the workspace.GeometricNetwork—Geometric network datasets will be returned.LasDataset—LAS datasets will be returned.Mosaic—Mosaic datasets will be returned.Network—Network datasets will be returned.ParcelFabric—Parcel fabric datasets will be returned.ParcelFabricForArcmap—ArcMap parcel fabric datasets will be returned.Raster—Raster datasets will be returned.RasterCatalog—Raster catalog datasets will be returned.Terrain—Terrain datasets will be returned. Tin—TIN datasets will be returned.Topology—Topology datasets will be returned.TraceNetwork—Trace network datasets will be returned.UtilityNetwork—Utility network datasets will be returned.All—All datasets in the workspace will be returned.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListDatasets ({wild_card}, {feature_type})
```

### Example 2

```python
import arcpy

arcpy.env.workspace = "c:/data"

# Print all the feature datasets in the workspace that start with the letter C.
datasets = arcpy.ListDatasets("C*", "Feature")

for dataset in datasets:
    print(dataset)
```

### Example 3

```python
import arcpy

arcpy.env.workspace = "c:/data"

# Print all the feature datasets in the workspace that start with the letter C.
datasets = arcpy.ListDatasets("C*", "Feature")

for dataset in datasets:
    print(dataset)
```

### Example 4

```python
import arcpy
arcpy.env.workspace = 'c:/data'

# Print all the feature datasets in the workspace that start with the letter c
# or f.
datasets1 = list(set(arcpy.ListDatasets("c*", "Feature")) |
                 set(arcpy.ListDatasets("f*", "Feature")))
print(datasets1)

# Print all the feature datasets in the workspace that start with the letters
# except c.
datasets2 = list(set(arcpy.ListDatasets("*", "Feature")) -
                 set(arcpy.ListDatasets("c*", "Feature")))
print(datasets2)

# Print all the feature datasets in the workspace that contain both the letter c
# and f.
datasets3 = list(set(arcpy.ListDatasets("*c*", "Feature")) &
                 set(arcpy.ListDatasets("*f*", "Feature")))
print(datasets3)
```

### Example 5

```python
import arcpy
arcpy.env.workspace = 'c:/data'

# Print all the feature datasets in the workspace that start with the letter c
# or f.
datasets1 = list(set(arcpy.ListDatasets("c*", "Feature")) |
                 set(arcpy.ListDatasets("f*", "Feature")))
print(datasets1)

# Print all the feature datasets in the workspace that start with the letters
# except c.
datasets2 = list(set(arcpy.ListDatasets("*", "Feature")) -
                 set(arcpy.ListDatasets("c*", "Feature")))
print(datasets2)

# Print all the feature datasets in the workspace that contain both the letter c
# and f.
datasets3 = list(set(arcpy.ListDatasets("*c*", "Feature")) &
                 set(arcpy.ListDatasets("*f*", "Feature")))
print(datasets3)
```

### Example 6

```python
import arcpy

arcpy.env.workspace = 'c:/data/myGDB.gdb/TN_dataset'

# Print all the trace networks in the workspace.
datasets = arcpy.ListDatasets(feature_type="tracenetwork")
for dataset in datasets:
    print(dataset)
```

### Example 7

```python
import arcpy

arcpy.env.workspace = 'c:/data/myGDB.gdb/TN_dataset'

# Print all the trace networks in the workspace.
datasets = arcpy.ListDatasets(feature_type="tracenetwork")
for dataset in datasets:
    print(dataset)
```

### Example 8

```python
import arcpy

arcpy.env.workspace = 'c:/data/mySQLserver.sde'

# Print all the raster datasets in the workspace.
datasets = arcpy.ListDatasets("", "Raster")
for dataset in datasets:
    print(dataset)
```

### Example 9

```python
import arcpy

arcpy.env.workspace = 'c:/data/mySQLserver.sde'

# Print all the raster datasets in the workspace.
datasets = arcpy.ListDatasets("", "Raster")
for dataset in datasets:
    print(dataset)
```

### Example 10

```python
import arcpy
arcpy.env.workspace = 'c:/data/mySQLserver.sde' 

# Print all the feature datasets owned by 'user1' in the enterprise gdb
datasets = arcpy.ListDatasets("user1*", "Feature")
for dataset in datasets:
    print(dataset)
```

### Example 11

```python
import arcpy
arcpy.env.workspace = 'c:/data/mySQLserver.sde' 

# Print all the feature datasets owned by 'user1' in the enterprise gdb
datasets = arcpy.ListDatasets("user1*", "Feature")
for dataset in datasets:
    print(dataset)
```

---

## ListDataStoreItems

## Summary

Returns a list of the folders or databases registered with an ArcGIS Server site.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| connection_file | For a hosting server, provide the server URL or use the MY_HOSTED_SERVICES keyword. For a stand-alone server, an ArcGIS Server connection file (.ags) representing the server with which you want to register the data. | String |
| datastore_type | The type of data that you want to list.DATABASE—Enterprise databases registered with the server will be listed.FOLDER—File-based data sources registered with the server will be listed. | String |

## Code Samples

### Example 1

```python
ListDataStoreItems (connection_file, datastore_type)
```

### Example 2

```python
import arcpy

print("Registered FOLDER items are:")

for item in arcpy.ListDataStoreItems("GIS Servers/MyConnection.ags", "FOLDER"):
    print("Name: {}".format(item[0]))
    print("Server's path: {}".format(item[1]))
    print("Publisher's path: {}".format(item[2]))
    if item[3] == "managed":
        print("This is ArcGIS Server's Managed Database")
```

### Example 3

```python
import arcpy

print("Registered FOLDER items are:")

for item in arcpy.ListDataStoreItems("GIS Servers/MyConnection.ags", "FOLDER"):
    print("Name: {}".format(item[0]))
    print("Server's path: {}".format(item[1]))
    print("Publisher's path: {}".format(item[2]))
    if item[3] == "managed":
        print("This is ArcGIS Server's Managed Database")
```

### Example 4

```python
import arcpy

print("Registered databases items are:")

for item in arcpy.ListDataStoreItems("MY_HOSTED_SERVICES", "DATABASE"):
    print("Name: {}".format(item[0]))
    print("Database Connection Properties for Server: {}".format(item[1]))
    print("Database Connection Properties for Publisher: {}".format(item[2]))
    if item[3] == "managed":
        print("This is ArcGIS Server's Managed Database")
```

### Example 5

```python
import arcpy

print("Registered databases items are:")

for item in arcpy.ListDataStoreItems("MY_HOSTED_SERVICES", "DATABASE"):
    print("Name: {}".format(item[0]))
    print("Database Connection Properties for Server: {}".format(item[1]))
    print("Database Connection Properties for Publisher: {}".format(item[2]))
    if item[3] == "managed":
        print("This is ArcGIS Server's Managed Database")
```

---

## ListEnvironments

## Summary

Returns a list of geoprocessing environment names.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |

## Code Samples

### Example 1

```python
ListEnvironments ({wild_card})
```

### Example 2

```python
import arcpy

environments = arcpy.ListEnvironments()

# Sort the environment names
environments.sort()

for environment in environments:
    # Format and print each environment and its current setting.
    # (The environments are accessed by key from arcpy.env.)
    print("{0:<30}: {1}".format(environment, arcpy.env[environment]))
```

### Example 3

```python
import arcpy

environments = arcpy.ListEnvironments()

# Sort the environment names
environments.sort()

for environment in environments:
    # Format and print each environment and its current setting.
    # (The environments are accessed by key from arcpy.env.)
    print("{0:<30}: {1}".format(environment, arcpy.env[environment]))
```

---

## ListFeatureClasses

## Summary

Returns a list of the feature classes in the current workspace, limited by name, feature type, and optional feature dataset.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| feature_type | The feature type that will limit the results. Valid feature types are listed in the following table: Annotation—Annotation feature classesArc—Arc (or polyline) feature classesDimension—Dimension feature classesEdge—Edge feature classes Junction—Junction feature classes Label— Label feature classes Line—Polyline (or arc) feature classes Multipatch—Multipatch feature classes Multipoint—Multipoint feature classNode—Node feature classes Point—Point feature classes Polygon—Polygon feature classes Polyline—Polyline (or arc) feature classes Region—Region feature classes Route—Route feature classes Tic—Tic feature classes All— All feature classes in the workspace. This is the default.(The default value is All) | String |
| feature_dataset | Limits the feature classes returned to the feature dataset, if specified. If blank, only stand-alone feature classes will be returned in the workspace. | String |

## Code Samples

### Example 1

```python
ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset})
```

### Example 2

```python
import os
import arcpy

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = "c:/base"

# Use the ListFeatureClasses function to return a list of
#  shapefiles.
featureclasses = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.CopyFeatures_management(
        fc, os.path.join("c:/base/output.gdb",
                         os.path.splitext(fc)[0]))
```

### Example 3

```python
import os
import arcpy

# Set the workspace for ListFeatureClasses
arcpy.env.workspace = "c:/base"

# Use the ListFeatureClasses function to return a list of
#  shapefiles.
featureclasses = arcpy.ListFeatureClasses()

# Copy shapefiles to a file geodatabase
for fc in featureclasses:
    arcpy.CopyFeatures_management(
        fc, os.path.join("c:/base/output.gdb",
                         os.path.splitext(fc)[0]))
```

### Example 4

```python
import arcpy
import os

arcpy.env.workspace = "c:/base/gdb.gdb"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)
```

### Example 5

```python
import arcpy
import os

arcpy.env.workspace = "c:/base/gdb.gdb"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        print(path)
```

---

## ListFields

## Summary

Returns a list of fields in a feature class, shapefile, or table in a specified dataset. The returned list can be limited with search criteria for name and field type and will contain Field objects.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The specified feature class or table with the fields to be returned. | String |
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas.(The default value is None) | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| field_type | Specifies the field type that will be returned.All— All field types are returned. This is the default.Blob—Fields of Blob type are returned.BigInteger—Fields of Big Integer type are returned.Date—Fields of Date type are returned.DateOnly—Fields of Date Only type are returned.Double—Fields of Double type are returned.Geometry—Fields of Geometry type are returned.GlobalID—Fields of Global ID type are returned.Guid—Fields of GUID type are returned.Integer—Fields of Integer type are returned.OID—Fields of Object ID type are returned.Raster—Fields of Raster type are returned.Single—Fields of Single type are returned.SmallInteger—Fields of Small Integer type are returned.String—Fields of String type are returned.TimeOnly—Fields of Time Only type are returned.TimestampOffset—Fields of Timestamp Offset type are returned.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListFields (dataset, {wild_card}, {field_type})
```

### Example 2

```python
import arcpy

# For each field in the Hospitals feature class, print
# the field name, type, and length.
fields = arcpy.ListFields("c:/data/municipal.gdb/hospitals")

for field in fields:
    print(f"{field.name} has a type of {field.type} with a length of {field.length}")
```

### Example 3

```python
import arcpy

# For each field in the Hospitals feature class, print
# the field name, type, and length.
fields = arcpy.ListFields("c:/data/municipal.gdb/hospitals")

for field in fields:
    print(f"{field.name} has a type of {field.type} with a length of {field.length}")
```

### Example 4

```python
import arcpy

featureclass = "c:/data/municipal.gdb/hospitals"
field_names = [f.name for f in arcpy.ListFields(featureclass)]
```

### Example 5

```python
import arcpy

featureclass = "c:/data/municipal.gdb/hospitals"
field_names = [f.name for f in arcpy.ListFields(featureclass)]
```

---

## ListFiles

## Summary

Returns a list of files in the current workspace.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |

## Code Samples

### Example 1

```python
ListFiles ({wild_card})
```

### Example 2

```python
import os
import arcpy

arcpy.env.workspace = "c:/temp"

# Copy each file with a .csv extension to a dBASE file
for csv_file in arcpy.ListFiles("*.csv"):
    # Use splitext to set the output table name
    dbase_file = os.path.splitext(csv_file)[0] + ".dbf"
    arcpy.CopyRows_management(csv_file, dbase_file)
```

### Example 3

```python
import os
import arcpy

arcpy.env.workspace = "c:/temp"

# Copy each file with a .csv extension to a dBASE file
for csv_file in arcpy.ListFiles("*.csv"):
    # Use splitext to set the output table name
    dbase_file = os.path.splitext(csv_file)[0] + ".dbf"
    arcpy.CopyRows_management(csv_file, dbase_file)
```

---

## ListIndexes

## Summary

Returns a list of the indexes in a feature class, shapefile, or table in a specified dataset.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The specified feature class or table with the indexes to be returned. | String |
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |

## Code Samples

### Example 1

```python
ListIndexes (dataset, {wild_card})
```

### Example 2

```python
import arcpy

featureclass = "c:/data/roads.shp"

# Get list of indexes for roads.shp and print properties
indexes = arcpy.ListIndexes(featureclass)
for index in indexes:
    print("Name        : {0}".format(index.name))
    print("IsAscending : {0}".format(index.isAscending))
    print("IsUnique    : {0}".format(index.isUnique))
```

### Example 3

```python
import arcpy

featureclass = "c:/data/roads.shp"

# Get list of indexes for roads.shp and print properties
indexes = arcpy.ListIndexes(featureclass)
for index in indexes:
    print("Name        : {0}".format(index.name))
    print("IsAscending : {0}".format(index.isAscending))
    print("IsUnique    : {0}".format(index.isUnique))
```

---

## ListInstallations

## Summary

Returns a list of installation types.

## Code Samples

### Example 1

```python
ListInstallations ()
```

### Example 2

```python
import arcpy

print(arcpy.ListInstallations()[0])
```

### Example 3

```python
import arcpy

print(arcpy.ListInstallations()[0])
```

---

## ListPortalURLs

## Summary

Returns a list of available portal URLs.

## Code Samples

### Example 1

```python
ListPortalURLs ()
```

### Example 2

```python
import arcpy

# For example: ['http://testext.arcgis.com/', 'http://www.arcgis.com/']
print(arcpy.ListPortalURLs())
```

### Example 3

```python
import arcpy

# For example: ['http://testext.arcgis.com/', 'http://www.arcgis.com/']
print(arcpy.ListPortalURLs())
```

---

## ListPrinterNames

## Summary

Returns a list of available printers on the local computer.

## Code Samples

### Example 1

```python
ListPrinterNames ()
```

### Example 2

```python
import arcpy

# Print available printers
printers = arcpy.ListPrinterNames()
for printer in printers:
    print(printer)
```

### Example 3

```python
import arcpy

# Print available printers
printers = arcpy.ListPrinterNames()
for printer in printers:
    print(printer)
```

---

## ListRasterProducts

## Summary

Returns a list of paths to the raster products associated with a metadata file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| metadata_file_path | The path to the metadata file. | String |

## Code Samples

### Example 1

```python
ListRasterProducts (metadata_file_path)
```

### Example 2

```python
import arcpy
arcpy.ListRasterProducts(r'c:\temp\LC80390382013135LGN01\LC80390382013135LGN01_MTL.txt')

# For example:
# ['c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Multispectral', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\QA', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Panchromatic', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Multiband', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Thermal', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Pansharpen', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Water', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Vegetation', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\SnowIce', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Cirrus', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Cloud', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Landcover']
```

### Example 3

```python
import arcpy
arcpy.ListRasterProducts(r'c:\temp\LC80390382013135LGN01\LC80390382013135LGN01_MTL.txt')

# For example:
# ['c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Multispectral', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\QA', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Panchromatic', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Multiband', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Thermal', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Pansharpen', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Water', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Vegetation', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\SnowIce', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Cirrus', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Cloud', 
# 'c:\\temp\\LC80390382013135LGN01\\LC80390382013135LGN01_MTL.txt\\Landcover']
```

---

## ListRasters

## Summary

Returns a list of the rasters in the current workspace.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| raster_type | The raster type that will limit the results. The following are valid raster types: BMP—Bitmap graphic raster dataset format.GIF—Graphic Interchange Format for raster datasets.IMG— ERDAS IMAGINE raster data format.JP2—JPEG 2000 raster dataset format.JPG—Joint Photographics Experts Group raster dataset format.PNG— Portable Network Graphics raster dataset format.TIF—Tagged Image File for raster datasets.GRID— Grid data format.All—All supported raster types are returned. This is the default.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListRasters ({wild_card}, {raster_type})
```

### Example 2

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/data/DEMS"

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "GRID")
for raster in rasters:
    print(raster)
```

### Example 3

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/data/DEMS"

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", "GRID")
for raster in rasters:
    print(raster)
```

---

## ListSpatialReferences

## Summary

Returns a list of available spatial reference names for use as an argument to the SpatialReference class.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| spatial_reference_type | Limits the spatial references listed by type.GCS—Lists only geographic coordinate systems.PCS—Lists only projected coordinate systems.ALL—Lists both projected and geographic coordinate systems. This is the default.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListSpatialReferences ({wild_card}, {spatial_reference_type})
```

### Example 2

```python
import arcpy

# Get the list of spatial references and print it.
srs = arcpy.ListSpatialReferences(spatial_reference_type="GCS")
for sr_name in srs:
    print(sr_name)
```

### Example 3

```python
import arcpy

# Get the list of spatial references and print it.
srs = arcpy.ListSpatialReferences(spatial_reference_type="GCS")
for sr_name in srs:
    print(sr_name)
```

### Example 4

```python
import arcpy

# Get the list of spatial references
srs = arcpy.ListSpatialReferences("*utm/new zealand*")

# Create a SpatialReference object for each one and print the
# central meridian
for sr_string in srs:
    sr_object = arcpy.SpatialReference(sr_string)
    print("{0.centralMeridian}   {0.name}".format(sr_object))
```

### Example 5

```python
import arcpy

# Get the list of spatial references
srs = arcpy.ListSpatialReferences("*utm/new zealand*")

# Create a SpatialReference object for each one and print the
# central meridian
for sr_string in srs:
    sr_object = arcpy.SpatialReference(sr_string)
    print("{0.centralMeridian}   {0.name}".format(sr_object))
```

---

## ListTables

## Summary

Returns a list of tables in the current workspace.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| table_type | The table type to limit the results.dBASE—Only tables of type dBASE are returned.INFO—Only stand-alone INFO tables are returned.ALL—All stand-alone tables, including geodatabase tables, are returned. This is the default.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListTables ({wild_card}, {table_type})
```

### Example 2

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/data/mydata.gdb"

# Get and print a list of tables
tables = arcpy.ListTables()
for table in tables:
    print(table)
```

### Example 3

```python
import arcpy

# Set the current workspace
arcpy.env.workspace = "c:/data/mydata.gdb"

# Get and print a list of tables
tables = arcpy.ListTables()
for table in tables:
    print(table)
```

---

## ListToolboxes

## Summary

Returns a list of toolboxes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |

## Code Samples

### Example 1

```python
ListToolboxes ({wild_card})
```

### Example 2

```python
import arcpy

# Get and print a list of all toolboxes.
toolboxes = arcpy.ListToolboxes()

for toolbox in toolboxes:
    print(toolbox)
```

### Example 3

```python
import arcpy

# Get and print a list of all toolboxes.
toolboxes = arcpy.ListToolboxes()

for toolbox in toolboxes:
    print(toolbox)
```

---

## ListTools

## Summary

Returns a list of geoprocessing tools.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |

## Code Samples

### Example 1

```python
ListTools ({wild_card})
```

### Example 2

```python
import arcpy

# Create a list of tools in the Analysis toolbox
tools = arcpy.ListTools("*_analysis")

# Loop through the list and print each tool's usage.
for tool in tools:
    print(arcpy.Usage(tool))
```

### Example 3

```python
import arcpy

# Create a list of tools in the Analysis toolbox
tools = arcpy.ListTools("*_analysis")

# Loop through the list and print each tool's usage.
for tool in tools:
    print(arcpy.Usage(tool))
```

---

## ListTransformations

## Summary

Returns a list of valid transformation methods. An extent can be used to narrow the list of valid transformation methods for a specific geographic area.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| from_sr | The starting geographic coordinate system. This can be specified with a SpatialReference object, the name of the spatial reference, or a path to a projection file (.prj). | SpatialReference |
| to_sr | The final geographic coordinate system. This can be specified with a SpatialReference object, the name of the spatial reference, or a path to a projection file (.prj). | SpatialReference |
| extent | Only transformations that span the entire extent will be returned. The extent needs to be specified in coordinates from the from_sr. When working with data, the extent on a Describe object can be used. | Extent |
| vertical | Specifies whether to return a list of vertical or horizontal transformations. By default, the function returns transformations that ignore vertical coordinate systems on the from_sr and to_sr. The function returns only one type of transformation. If set to False, horizontal transformations will be returned; if set to True, vertical transformations will be returned.To use True, both the from_sr and to_sr arguments must have a vertical coordinate system.To use a transformation result as input to the Project tool, the tool's vertical parameter must be set appropriately to NO_VERTICAL or VERTICAL to match the transformation.(The default value is False) | Boolean |
| first_only | Specifies whether to limit the list of transformations to a single item or return all valid transformations. This is a performance optimization.(The default value is False) | Boolean |

## Code Samples

### Example 1

```python
ListTransformations (from_sr, to_sr, {extent}, {vertical}, {first_only})
```

### Example 2

```python
import arcpy

from_sr = arcpy.SpatialReference('WGS 1984')
to_sr = arcpy.SpatialReference('NAD 1927 StatePlane California VI FIPS 0406')

extent = arcpy.Extent(-178.217598182, 18.9217863640001,
                      -66.969270909, 71.4062354550001)
transformations = arcpy.ListTransformations(from_sr, to_sr, extent)
```

### Example 3

```python
import arcpy

from_sr = arcpy.SpatialReference('WGS 1984')
to_sr = arcpy.SpatialReference('NAD 1927 StatePlane California VI FIPS 0406')

extent = arcpy.Extent(-178.217598182, 18.9217863640001,
                      -66.969270909, 71.4062354550001)
transformations = arcpy.ListTransformations(from_sr, to_sr, extent)
```

---

## ListUsers

## Summary

Returns a list of named tuples containing information for users who are connected to an enterprise geodatabase.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| sde_workspace | An enterprise geodatabase (sde connection file). The connection properties specified in the enterprise geodatabase must have administrative rights that allow the user to disconnect other connections. | String |

## Code Samples

### Example 1

```python
ListUsers (sde_workspace)
```

### Example 2

```python
import arcpy

arcpy.ListUsers("C:\\MyProject\\admin.sde")
```

### Example 3

```python
import arcpy

arcpy.ListUsers("C:\\MyProject\\admin.sde")
```

### Example 4

```python
import arcpy

users = arcpy.ListUsers("C:\\MyProject\\admin.sde")
for user in users:
    print("Username: {0}, Connected at: {1}".format(
        user.Name, user.ConnectionTime))
```

### Example 5

```python
import arcpy

users = arcpy.ListUsers("C:\\MyProject\\admin.sde")
for user in users:
    print("Username: {0}, Connected at: {1}".format(
        user.Name, user.ConnectionTime))
```

### Example 6

```python
import arcpy

# Set the admistrative workspace connection
arcpy.env.workspace = "C:\\MyProject\\admin.sde"
admin = arcpy.env.workspace

# Create a list of users
users = arcpy.ListUsers(admin)

# Create a list of SDE ID's.
# Use a list comprehension to get the ID values in a new list.
id_users = [user.ID for user in users]
print(id_users)
```

### Example 7

```python
import arcpy

# Set the admistrative workspace connection
arcpy.env.workspace = "C:\\MyProject\\admin.sde"
admin = arcpy.env.workspace

# Create a list of users
users = arcpy.ListUsers(admin)

# Create a list of SDE ID's.
# Use a list comprehension to get the ID values in a new list.
id_users = [user.ID for user in users]
print(id_users)
```

---

## ListVersions

## Summary

Returns a list of versions that the connected user has permission to use.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| sde_workspace | An enterprise geodatabase workspace. | String |

## Code Samples

### Example 1

```python
ListVersions (sde_workspace)
```

### Example 2

```python
import arcpy

database = "Database Connections/toolboxDEFAULTVersion.sde"
versions = arcpy.ListVersions(database)

# Print the versions available to the user
for version in versions:
    print(version)
```

### Example 3

```python
import arcpy

database = "Database Connections/toolboxDEFAULTVersion.sde"
versions = arcpy.ListVersions(database)

# Print the versions available to the user
for version in versions:
    print(version)
```

---

## ListWorkspaces

## Summary

Returns a list of workspaces in the current workspace.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| wild_card | Limits the results returned. If a value is not specified, all values are returned. The wildcard is not case sensitive.SymbolDescriptionExample*Represents zero or more characters.Te* finds Tennessee and Texas. | * |
| * | Represents zero or more characters. | Te* finds Tennessee and Texas. |
| workspace_type | The workspace type that will limit the results returned.Coverage—Coverage workspaces will be returned.FileGDB—File geodatabases (.gdb) will be returned.Folder—Shapefile workspaces will be returned.SDE—Enterprise databases (.sde) will be returned.SQLite—SQLite databases (.sqlite, .gpkg) will be returned.All—All workspaces will be returned. This is the default.(The default value is All) | String |

## Code Samples

### Example 1

```python
ListWorkspaces ({wild_card}, {workspace_type})
```

### Example 2

```python
import arcpy

arcpy.env.workspace = "c:/data"

# List all file geodatabases in the current workspace
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
    # Compact each geodatabase
    arcpy.management.Compact(workspace)
```

### Example 3

```python
import arcpy

arcpy.env.workspace = "c:/data"

# List all file geodatabases in the current workspace
workspaces = arcpy.ListWorkspaces("*", "FileGDB")

for workspace in workspaces:
    # Compact each geodatabase
    arcpy.management.Compact(workspace)
```

---

## Live Traffic Data

## Summary

Provides information about the live traffic information stored in the network dataset such as the streets—TMC join table and the path to the DTF files.

## Code Samples

### Example 1

```python
{"url":"https://www.arcgis.com/","region":"NorthAmericaTrafficFeed"}
```

### Example 2

```python
{"url":"https://www.arcgis.com/","region":"NorthAmericaTrafficFeed"}
```

### Example 3

```python
# Name: NDSLiveTrafficDataProperties_ex01.py
# Description: Print live traffic information for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanDiego.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the historical traffic data object
if desc.supportsLiveTrafficData:
    traffic = desc.liveTrafficData
else:
    #If the directions are not set for the network dataset, exit
    print "No live traffic information"
    sys.exit()

print("Live Traffic Information ----")
print("TMC Table Name: " , traffic.tmcTableName)
print("TMC Field Name: " , traffic.tmcFieldName)
print("Traffic Feed: " , traffic.trafficFeedLocation)
```

### Example 4

```python
# Name: NDSLiveTrafficDataProperties_ex01.py
# Description: Print live traffic information for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanDiego.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the historical traffic data object
if desc.supportsLiveTrafficData:
    traffic = desc.liveTrafficData
else:
    #If the directions are not set for the network dataset, exit
    print "No live traffic information"
    sys.exit()

print("Live Traffic Information ----")
print("TMC Table Name: " , traffic.tmcTableName)
print("TMC Field Name: " , traffic.tmcFieldName)
print("Traffic Feed: " , traffic.trafficFeedLocation)
```

---

## Location-Allocation Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the location-allocation solver.

---

## Location Referencing Dataset properties

## Summary

The Describe function returns the following properties for a Location Referencing Dataset.

## Code Samples

### Example 1

```python
Name: DescribeLRSDatasetProperties.py
Description: This script reports the properties of a linear referencing system (LRS)

# Import required modules
import arcpy

# Describe function on an LRS 
desc = arcpy.Describe("C:\\Data\\LRData\\LrsSchema.sde\\GPRefresh.DBO.LRS\\GPRefresh.DBO.LRS")

# LRS Describe properties
lrsXML = desc.lrsMetadata
eventBehaviors = desc.eventBehaviorRules
```

### Example 2

```python
Name: DescribeLRSDatasetProperties.py
Description: This script reports the properties of a linear referencing system (LRS)

# Import required modules
import arcpy

# Describe function on an LRS 
desc = arcpy.Describe("C:\\Data\\LRData\\LrsSchema.sde\\GPRefresh.DBO.LRS\\GPRefresh.DBO.LRS")

# LRS Describe properties
lrsXML = desc.lrsMetadata
eventBehaviors = desc.eventBehaviorRules
```

---

## Manage Subnetwork properties

## Summary

The properties below are returned by the manageSubnetwork object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the tier name        
        print(f"Tier Name: {tier.name}")
        # Print the ManageSubnetwork properties  
        print(f"Manage IsDirty: {tier.ManageSubnetwork.isDirty}\n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the tier name        
        print(f"Tier Name: {tier.name}")
        # Print the ManageSubnetwork properties  
        print(f"Manage IsDirty: {tier.ManageSubnetwork.isDirty}\n")
```

---

## Map Document properties

## Summary

When used with the Describe function, a map document returns a Describe dataType property that returns a value of "MapDocument".

## Code Samples

### Example 1

```python
import arcpy

map_document = r"C:\Project\Project.mxd"
desc = arcpy.Describe(map_document)
print(desc.datatype)  # MapDocument
```

### Example 2

```python
import arcpy

map_document = r"C:\Project\Project.mxd"
desc = arcpy.Describe(map_document)
print(desc.datatype)  # MapDocument
```

---

## Mosaic Dataset properties

## Summary

The Describe function returns the following properties for mosaic datasets. The Raster Dataset and Dataset property groups are also supported. The Editor Tracking property group is supported if editor tracking has been enabled for this mosaic dataset.

---

## Nearest Asset properties

## Summary

The properties below are returned by the nearestAssets object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
```

---

## Nearest Neighbor properties

## Summary

The properties below are returned by the nearestNeighbor object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
```

---

## Network Analyst layer properties

## Summary

The Describe function returns the properties described below for Network Analyst layers.

## Code Samples

### Example 1

```python
# Name: NALayerProperties_ex01.py
# Description: Lists all the properties that can be derived by describing a 
#              network analysis layer.

import arcpy

#Arguments..
#in_layer is the name of the Network Analysis layer file to be described.  
in_layer = "C:/Data/Route.lyr"  

#Get the description object using Describe. 
desc = arcpy.Describe(in_layer) 

arcpy.AddMessage(" ")
arcpy.AddMessage("== Description of network analysis layer " + in_layer + " ==")
arcpy.AddMessage(" ") 

#Print general infomation.
justify = 35 
nds = desc.network 
solvername = desc.solverName 
arcpy.AddMessage("---- General information:") 
arcpy.AddMessage(" %*s: %s" % (justify, "Network" , nds.catalogPath)) 
arcpy.AddMessage(" %*s: %s" % (justify, "SolverName" , desc.solverName)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Impedance" , desc.impedance)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Accumulators" , desc.accumulators)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Restrictions" , desc.restrictions)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Ignore invalid locations?" , 
                str(desc.ignoreInvalidLocations))) 
arcpy.AddMessage(" %*s: %s" % (justify, "UTurn policy" , desc.UTurns)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Using hierarchy?" , desc.useHierarchy))
arcpy.AddMessage(" %*s: %s" % (justify, "Exclude Restricted Elements?" ,
                               desc.excludeRestrictedElements))
arcpy.AddMessage(" ") 

#A note about the dynamic properties (indicated by X in the help system)
#In order to access the dynamic properties use Python's built in getattr()
#function. In order to find out if a dynamic property is supported by the 
#describe object, use Python's built in hasattr() function. 

# Print attribute parameter information
arcpy.AddMessage(" ---- Attribute Parameter information ----") 
count = desc.parameterCount 
if count == 0: 
    arcpy.AddMessage(" ---- No Attribute Parameters defined ----") 
else: 
    parameters = desc.parameters 
    for i in range(0, count): 
        attributeName = getattr(parameters,"attributeName" + str(i)) 
        parameterName = getattr(parameters, "parameterName" + str(i)) 
        parameterValue = getattr(parameters, "parameterValue" + str(i)) 
        arcpy.AddMessage(" %*s: %s: %s" % (justify, attributeName, 
                                           parameterName, parameterValue))   

# Print hierarchy information
if desc.useHierarchy.lower() == "use_hierarchy": 
    arcpy.AddMessage(" ---- Hierarchy information ----")
    arcpy.AddMessage(" %*s: %s" % (justify, "Hierarchy Attribute Name",
                                   desc.hierarchyAttribute)) 
    count = desc.hierarchyLevelCount
    arcpy.AddMessage(" %*s: %d" % (justify, "Hierarchy Level Count" , count)) 
    
    for i in range(0, count ): 
        levelRange = "" 
        if i == 0:      
            levelUB = getattr(desc,"maxValueForHierarchy" + str(i+1))            
            levelRange = "up to %s" % levelUB 
        elif i == (count - 1): 
            prevLevelUB = getattr(desc, "maxValueForHierarchy" + str(i)) 
            levelRange = "%s and higher" % (prevLevelUB + 1)
        else: 
            prevLevelUB =  getattr(desc, "maxValueForHierarchy" + str(i)) 
            levelUB = getattr(desc,"maxValueForHierarchy" + str(i + 1)) 
            levelRange = "%s - %s" % ((prevLevelUB + 1), levelUB)
        
        arcpy.AddMessage(" %*s %d range: %s" % (justify, "level", (i + 1), 
                                                levelRange))

    arcpy.AddMessage(" ") 

# Print locator information. 
arcpy.AddMessage("---- Locator information:") 
count = desc.locatorCount 
arcpy.AddMessage(" %*s: %d" % (justify, "Count" , count)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Find Closest?" , desc.findClosest)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Search Tolerance", 
                               desc.searchTolerance))
arcpy.AddMessage(" %*s: %s" % (justify, "Exclude Restricted Elements",
                               desc.excludeRestrictedElements))
locators = desc.locators 
for i in range(0, count): 
    sourceName = getattr(locators, "source" + str(i)) 
    sourceType = getattr(locators, "snapType" + str(i))
    searchQuery = getattr(locators, "searchQuery" + str(i))
    arcpy.AddMessage(" %*s: %s" %(justify, sourceName, sourceType))
    arcpy.AddMessage(" %*s: %s" %(justify, sourceName, searchQuery))
```

### Example 2

```python
# Name: NALayerProperties_ex01.py
# Description: Lists all the properties that can be derived by describing a 
#              network analysis layer.

import arcpy

#Arguments..
#in_layer is the name of the Network Analysis layer file to be described.  
in_layer = "C:/Data/Route.lyr"  

#Get the description object using Describe. 
desc = arcpy.Describe(in_layer) 

arcpy.AddMessage(" ")
arcpy.AddMessage("== Description of network analysis layer " + in_layer + " ==")
arcpy.AddMessage(" ") 

#Print general infomation.
justify = 35 
nds = desc.network 
solvername = desc.solverName 
arcpy.AddMessage("---- General information:") 
arcpy.AddMessage(" %*s: %s" % (justify, "Network" , nds.catalogPath)) 
arcpy.AddMessage(" %*s: %s" % (justify, "SolverName" , desc.solverName)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Impedance" , desc.impedance)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Accumulators" , desc.accumulators)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Restrictions" , desc.restrictions)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Ignore invalid locations?" , 
                str(desc.ignoreInvalidLocations))) 
arcpy.AddMessage(" %*s: %s" % (justify, "UTurn policy" , desc.UTurns)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Using hierarchy?" , desc.useHierarchy))
arcpy.AddMessage(" %*s: %s" % (justify, "Exclude Restricted Elements?" ,
                               desc.excludeRestrictedElements))
arcpy.AddMessage(" ") 

#A note about the dynamic properties (indicated by X in the help system)
#In order to access the dynamic properties use Python's built in getattr()
#function. In order to find out if a dynamic property is supported by the 
#describe object, use Python's built in hasattr() function. 

# Print attribute parameter information
arcpy.AddMessage(" ---- Attribute Parameter information ----") 
count = desc.parameterCount 
if count == 0: 
    arcpy.AddMessage(" ---- No Attribute Parameters defined ----") 
else: 
    parameters = desc.parameters 
    for i in range(0, count): 
        attributeName = getattr(parameters,"attributeName" + str(i)) 
        parameterName = getattr(parameters, "parameterName" + str(i)) 
        parameterValue = getattr(parameters, "parameterValue" + str(i)) 
        arcpy.AddMessage(" %*s: %s: %s" % (justify, attributeName, 
                                           parameterName, parameterValue))   

# Print hierarchy information
if desc.useHierarchy.lower() == "use_hierarchy": 
    arcpy.AddMessage(" ---- Hierarchy information ----")
    arcpy.AddMessage(" %*s: %s" % (justify, "Hierarchy Attribute Name",
                                   desc.hierarchyAttribute)) 
    count = desc.hierarchyLevelCount
    arcpy.AddMessage(" %*s: %d" % (justify, "Hierarchy Level Count" , count)) 
    
    for i in range(0, count ): 
        levelRange = "" 
        if i == 0:      
            levelUB = getattr(desc,"maxValueForHierarchy" + str(i+1))            
            levelRange = "up to %s" % levelUB 
        elif i == (count - 1): 
            prevLevelUB = getattr(desc, "maxValueForHierarchy" + str(i)) 
            levelRange = "%s and higher" % (prevLevelUB + 1)
        else: 
            prevLevelUB =  getattr(desc, "maxValueForHierarchy" + str(i)) 
            levelUB = getattr(desc,"maxValueForHierarchy" + str(i + 1)) 
            levelRange = "%s - %s" % ((prevLevelUB + 1), levelUB)
        
        arcpy.AddMessage(" %*s %d range: %s" % (justify, "level", (i + 1), 
                                                levelRange))

    arcpy.AddMessage(" ") 

# Print locator information. 
arcpy.AddMessage("---- Locator information:") 
count = desc.locatorCount 
arcpy.AddMessage(" %*s: %d" % (justify, "Count" , count)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Find Closest?" , desc.findClosest)) 
arcpy.AddMessage(" %*s: %s" % (justify, "Search Tolerance", 
                               desc.searchTolerance))
arcpy.AddMessage(" %*s: %s" % (justify, "Exclude Restricted Elements",
                               desc.excludeRestrictedElements))
locators = desc.locators 
for i in range(0, count): 
    sourceName = getattr(locators, "source" + str(i)) 
    sourceType = getattr(locators, "snapType" + str(i))
    searchQuery = getattr(locators, "searchQuery" + str(i))
    arcpy.AddMessage(" %*s: %s" %(justify, sourceName, sourceType))
    arcpy.AddMessage(" %*s: %s" %(justify, sourceName, searchQuery))
```

---

## Network Analyst Locator

## Summary

Provides the source, snap type, and search query information about the classes that are used to determine the network locations.

## Code Samples

### Example 1

```python
# Name: NALayerLocatorProperties_ex01.py
# Description: Prints the source name and snap type information
#              for the locators used by a network analysis layer

import arcpy

in_layer = "C:/Data/Route.lyr" 

# Create a Describe object from layer file.
desc = arcpy.Describe(in_layer) 

count = desc.locatorCount 
locators = desc.locators 

#print locator information
print "Total Locators: ", count 
for i in range(0, count): 
    sourceName = getattr(locators,"source" + str(i))
    snapType = getattr(locators,"snapType" + str(i))
    query = getattr(locators, "searchQuery" + str(i))
    print "%s : %s : %s" % (sourceName,snapType, query)
```

### Example 2

```python
# Name: NALayerLocatorProperties_ex01.py
# Description: Prints the source name and snap type information
#              for the locators used by a network analysis layer

import arcpy

in_layer = "C:/Data/Route.lyr" 

# Create a Describe object from layer file.
desc = arcpy.Describe(in_layer) 

count = desc.locatorCount 
locators = desc.locators 

#print locator information
print "Total Locators: ", count 
for i in range(0, count): 
    sourceName = getattr(locators,"source" + str(i))
    snapType = getattr(locators,"snapType" + str(i))
    query = getattr(locators, "searchQuery" + str(i))
    print "%s : %s : %s" % (sourceName,snapType, query)
```

---

## Network Analyst Solver

## Summary

The Network Analyst Solver object provides the analysis properties specific to a network analyst solver.

## Code Samples

### Example 1

```python
# Name: NALayerSolverProperties_ex01.py
# Description: Lists all the solver specific properties that can be
#              derived by describing a network analysis layer. 

import arcpy

# ============ 
# Helper functions 
# ============ 
def printRoute(justify=35): 
    '''Displays information about a Route layer'''        
    arcpy.AddMessage("---- Route properties:")
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Find Best Sequence?", 
                                   props.findBestSequence))
    arcpy.AddMessage(" %*s: %s" % (justify, "OrderingType", 
                                   props.orderingType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Use Time Windows?", 
                                   props.useTimeWindows)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape", 
                                   props.routesShape)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Start Time", props.startTime)) 

def printClosestFac(justify=35): 
    '''Displays information about a Closest Facility layer'''
    arcpy.AddMessage("---- Closest Facilty properties:") 
    props = desc.solverProperties
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel Direction",
                                   props.travelDirection)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Target Facility Count",
                                   props.defaultTargetFacilityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Cutoff",
                                   props.defaultCutoff)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape", 
                                   props.cfRoutesShape)) 

def printServiceArea(justify=35): 
    '''Displays information about a Service Area layer'''    
    arcpy.AddMessage("---- Service Area properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel Direction",
                                   props.travelDirection))
    arcpy.AddMessage(" %*s: %s" % (justify, "Default breaks",
                                   props.defaultBreaks)) 
    # Polygon info 
    arcpy.AddMessage(" ") 
    arcpy.AddMessage(" %*s: %s" % (justify, "Polygon Type?",
                                   props.serviceAreaPolygons)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Overlap Type",
                                   props.serviceAreaPolygonType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Multiple Facilities Options?",
                                   props.mergeSimilarRanges)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Excluded sources",
                                   props.exclusionSources)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Trim Polygons?",
                                   props.trimPolygons))
    arcpy.AddMessage(" %*s: %s" % (justify, "Trim Distance?",
                                   props.trimDistance)) 
    # Line info 
    arcpy.AddMessage(" ") 
    arcpy.AddMessage(" %*s: %s" % (justify, "Line overlap type",
                                   props.serviceAreaLinesType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Split lines at breaks?",
                                   props.splitLinesAtBreaks))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output line shape",
                                   props.serviceAreaLines)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output line shape",
                                   props.includeNetworkSourceFields)) 

def printODMatrix(justify=40): 
    '''Displays information about an OD Cost Matrix layer.'''
    arcpy.AddMessage("---- OD Cost Matrix properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Target Destination Count",
                                   props.defaultTargetDestinationCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Cutoff",
                                   props.defaultCutoff)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape",
                                   props.odLinesShape)) 

def printVRP(justify=35): 
    '''Displays information about a Vehicle routing problem layer'''
    arcpy.AddMessage("---- Vehicle Routing Problem properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Date",
                                   props.defaultDate))
    arcpy.AddMessage(" %*s: %s" % (justify, "Capacity Count",
                                   props.capacityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Time Field Units",
                                   props.timeFieldUnits)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Distance Field Units",
                                   props.distanceFieldUnits))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape",
                                   props.vrpRoutesShape)) 
    arcpy.AddMessage(" %*s: %s"%(justify,"Time window violation penalty factor",
                                   props.timeWindowViolationPenaltyFactor))
    arcpy.AddMessage(" %*s: %s"%(justify,"Penalty factor value",
                                   props.timeWindowViolationPenaltyFactorValue))
    arcpy.AddMessage(" %*s: %s" % (justify,"Excess transit time penalty factor",
                                   props.excessTransitTimePenaltyFactor))
    arcpy.AddMessage(" %*s: %s" % (justify,"Penalty factor value",
                                   props.excessTransitTimePenaltyFactorValue))

def printLocationAllocation(justify=35):
    '''Displays information about a Location-Allocation layer'''
    arcpy.AddMessage("---- Location-Allocation properties:") 
    props = desc.solverProperties
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel from" , 
                                   props.travelDirection)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Location-allocation problem type", 
                                   props.problemType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Number of facilities to find", 
                                   props.defaultTargetFacilityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance cutoff", 
                                   props.defaultCutoff))
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance transformation", 
                                   props.impedanceTransformation))
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance parameter", 
                                   props.impedanceParameter))
    arcpy.AddMessage(" %*s: %s" % (justify, "Target market share", 
                                   props.targetMarketShare))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output path shape", 
                                   props.laLinesShape)) 

# ============ 
# main module 
# ============  

# Get the arguments.. 
in_layer = "C:/Data/Route.lyr" 
justify = 35 

#Describe the layer file and get the solver name
desc = arcpy.Describe(in_layer) 
solvername = desc.solvername 

# Branch on type of solver (Route, Closest Facility, etc) 
if solvername.lower() == "route solver": 
    printRoute(justify) 
elif solvername.lower() == "closest facility solver": 
    printClosestFac(justify) 
elif solvername.lower() == "service area solver":
    printServiceArea(justify) 
elif solvername.lower() == "od cost matrix solver": 
    printODMatrix(justify) 
elif solvername.lower() == "vehicle routing problem solver": 
    printVRP(justify) 
elif solvername.lower() == "location-allocation solver": 
    printLocationAllocation(justify) 
else: 
    arcpy.AddError("Unknown solver: %s" % solvername) 

arcpy.AddMessage(" ") 
arcpy.AddMessage("==== End description ====") 
arcpy.AddMessage(" ")
```

### Example 2

```python
# Name: NALayerSolverProperties_ex01.py
# Description: Lists all the solver specific properties that can be
#              derived by describing a network analysis layer. 

import arcpy

# ============ 
# Helper functions 
# ============ 
def printRoute(justify=35): 
    '''Displays information about a Route layer'''        
    arcpy.AddMessage("---- Route properties:")
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Find Best Sequence?", 
                                   props.findBestSequence))
    arcpy.AddMessage(" %*s: %s" % (justify, "OrderingType", 
                                   props.orderingType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Use Time Windows?", 
                                   props.useTimeWindows)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape", 
                                   props.routesShape)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Start Time", props.startTime)) 

def printClosestFac(justify=35): 
    '''Displays information about a Closest Facility layer'''
    arcpy.AddMessage("---- Closest Facilty properties:") 
    props = desc.solverProperties
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel Direction",
                                   props.travelDirection)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Target Facility Count",
                                   props.defaultTargetFacilityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Cutoff",
                                   props.defaultCutoff)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape", 
                                   props.cfRoutesShape)) 

def printServiceArea(justify=35): 
    '''Displays information about a Service Area layer'''    
    arcpy.AddMessage("---- Service Area properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel Direction",
                                   props.travelDirection))
    arcpy.AddMessage(" %*s: %s" % (justify, "Default breaks",
                                   props.defaultBreaks)) 
    # Polygon info 
    arcpy.AddMessage(" ") 
    arcpy.AddMessage(" %*s: %s" % (justify, "Polygon Type?",
                                   props.serviceAreaPolygons)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Overlap Type",
                                   props.serviceAreaPolygonType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Multiple Facilities Options?",
                                   props.mergeSimilarRanges)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Excluded sources",
                                   props.exclusionSources)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Trim Polygons?",
                                   props.trimPolygons))
    arcpy.AddMessage(" %*s: %s" % (justify, "Trim Distance?",
                                   props.trimDistance)) 
    # Line info 
    arcpy.AddMessage(" ") 
    arcpy.AddMessage(" %*s: %s" % (justify, "Line overlap type",
                                   props.serviceAreaLinesType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Split lines at breaks?",
                                   props.splitLinesAtBreaks))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output line shape",
                                   props.serviceAreaLines)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output line shape",
                                   props.includeNetworkSourceFields)) 

def printODMatrix(justify=40): 
    '''Displays information about an OD Cost Matrix layer.'''
    arcpy.AddMessage("---- OD Cost Matrix properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Target Destination Count",
                                   props.defaultTargetDestinationCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Cutoff",
                                   props.defaultCutoff)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape",
                                   props.odLinesShape)) 

def printVRP(justify=35): 
    '''Displays information about a Vehicle routing problem layer'''
    arcpy.AddMessage("---- Vehicle Routing Problem properties:") 
    props = desc.solverProperties 
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Default Date",
                                   props.defaultDate))
    arcpy.AddMessage(" %*s: %s" % (justify, "Capacity Count",
                                   props.capacityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Time Field Units",
                                   props.timeFieldUnits)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Distance Field Units",
                                   props.distanceFieldUnits))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output Route Shape",
                                   props.vrpRoutesShape)) 
    arcpy.AddMessage(" %*s: %s"%(justify,"Time window violation penalty factor",
                                   props.timeWindowViolationPenaltyFactor))
    arcpy.AddMessage(" %*s: %s"%(justify,"Penalty factor value",
                                   props.timeWindowViolationPenaltyFactorValue))
    arcpy.AddMessage(" %*s: %s" % (justify,"Excess transit time penalty factor",
                                   props.excessTransitTimePenaltyFactor))
    arcpy.AddMessage(" %*s: %s" % (justify,"Penalty factor value",
                                   props.excessTransitTimePenaltyFactorValue))

def printLocationAllocation(justify=35):
    '''Displays information about a Location-Allocation layer'''
    arcpy.AddMessage("---- Location-Allocation properties:") 
    props = desc.solverProperties
    arcpy.AddMessage(" %*s: %s" % (justify, "Layer Name?" , desc.nameString))    
    arcpy.AddMessage(" %*s: %s" % (justify, "Travel from" , 
                                   props.travelDirection)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Location-allocation problem type", 
                                   props.problemType)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Number of facilities to find", 
                                   props.defaultTargetFacilityCount)) 
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance cutoff", 
                                   props.defaultCutoff))
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance transformation", 
                                   props.impedanceTransformation))
    arcpy.AddMessage(" %*s: %s" % (justify, "Impedance parameter", 
                                   props.impedanceParameter))
    arcpy.AddMessage(" %*s: %s" % (justify, "Target market share", 
                                   props.targetMarketShare))
    arcpy.AddMessage(" %*s: %s" % (justify, "Output path shape", 
                                   props.laLinesShape)) 

# ============ 
# main module 
# ============  

# Get the arguments.. 
in_layer = "C:/Data/Route.lyr" 
justify = 35 

#Describe the layer file and get the solver name
desc = arcpy.Describe(in_layer) 
solvername = desc.solvername 

# Branch on type of solver (Route, Closest Facility, etc) 
if solvername.lower() == "route solver": 
    printRoute(justify) 
elif solvername.lower() == "closest facility solver": 
    printClosestFac(justify) 
elif solvername.lower() == "service area solver":
    printServiceArea(justify) 
elif solvername.lower() == "od cost matrix solver": 
    printODMatrix(justify) 
elif solvername.lower() == "vehicle routing problem solver": 
    printVRP(justify) 
elif solvername.lower() == "location-allocation solver": 
    printLocationAllocation(justify) 
else: 
    arcpy.AddError("Unknown solver: %s" % solvername) 

arcpy.AddMessage(" ") 
arcpy.AddMessage("==== End description ====") 
arcpy.AddMessage(" ")
```

---

## Network Attribute Parameter

## Summary

Provides information about attribute parameters associated with the network analysis layer.

## Code Samples

### Example 1

```python
# Name: NALayerAttributeParameterProperties_ex01.py
# Description: Prints the attribute parameter information for a given network 
#              analysis layernetwork analysis layer.

import arcpy 

in_layer = "C:/Data/Route.lyr" 

# Create Describe object from layer file.
desc = arcpy.Describe(in_layer) 

count = desc.parameterCount 
parameters = desc.parameters 

# Print attribute parameter values
print "Total Attribute Parameters: ", count 
for i in range(0, count): 
    attrName = getattr(parameters,"attributeName" + str(i))
    paramName = getattr(parameters,"parameterName" + str(i))
    paramValue = getattr(parameters,"parameterValue" + str(i))
    print "%s : %s : %s" % (attrName,paramName,paramValue)
```

### Example 2

```python
# Name: NALayerAttributeParameterProperties_ex01.py
# Description: Prints the attribute parameter information for a given network 
#              analysis layernetwork analysis layer.

import arcpy 

in_layer = "C:/Data/Route.lyr" 

# Create Describe object from layer file.
desc = arcpy.Describe(in_layer) 

count = desc.parameterCount 
parameters = desc.parameters 

# Print attribute parameter values
print "Total Attribute Parameters: ", count 
for i in range(0, count): 
    attrName = getattr(parameters,"attributeName" + str(i))
    paramName = getattr(parameters,"parameterName" + str(i))
    paramValue = getattr(parameters,"parameterValue" + str(i))
    print "%s : %s : %s" % (attrName,paramName,paramValue)
```

---

## Network Attributes properties

## Summary

The following properties are supported by the networkAttributes object in a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print(f"ID: {na.Id}")
    print(f"Name: {na.name}")
    print(f"Network Attribute To Substitute: {na.networkAttributeToSubstitute}")
    print(f"Data Type: {na.dataType}")
    print(f"Field Type: {na.fieldType}")
    print(f"Usage Type: {na.usageType}")
    print(f"isEmbedded: {na.isEmbedded}")
    print(f"isApportionable: {na.isApportionable}")
    print(f"isOverridable: {na.isOverridable}")
    print(f"isSubstitution: {na.isSubstitution}")
    print(f"Domain name: {na.domainName}")
    print(f"bitPosition: {na.bitPosition}")
    print(f"bitSize: {na.bitSize}")
    print(f"Junction Weight ID: {na.junctionWeightId}")
    print(f"Edge Weight ID: {na.edgeWeightId} \n")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")
    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print(f"ID: {na.Id}")
    print(f"Name: {na.name}")
    print(f"Network Attribute To Substitute: {na.networkAttributeToSubstitute}")
    print(f"Data Type: {na.dataType}")
    print(f"Field Type: {na.fieldType}")
    print(f"Usage Type: {na.usageType}")
    print(f"isEmbedded: {na.isEmbedded}")
    print(f"isApportionable: {na.isApportionable}")
    print(f"isOverridable: {na.isOverridable}")
    print(f"isSubstitution: {na.isSubstitution}")
    print(f"Domain name: {na.domainName}")
    print(f"bitPosition: {na.bitPosition}")
    print(f"bitSize: {na.bitSize}")
    print(f"Junction Weight ID: {na.junctionWeightId}")
    print(f"Edge Weight ID: {na.edgeWeightId} \n")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")
    except:
        print(f"{na.name} does not have any attribute assignments \n")
```

---

## Network Attributes

## Summary

Provides information about network attributes that are defined for a given network dataset.

## Code Samples

### Example 1

```python
# Name: NDSAttributeProperties_ex01.py
# Description: Print the information about network attributes defined for the
#              network dataset

import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

# Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

# Get a list of network attributes
attributes = desc.attributes
#print information for each attribute
for attribute in attributes:
    print("----------------------------------\n")
    print("Name: ", attribute.name)
    print("Units: ", attribute.units)
    print("Usage Type: ", attribute.usageType)
    print("Data Type: ", attribute.dataType)
    print("Use By Default: ", str(attribute.useByDefault))
    #Information about  default evaluators
    print("Default edge evaluator type: ", attribute.defaultEdgeEvaluatorType)
    print("Default edge evaluator data: ", str(attribute.defaultEdgeData))
    print("Default junction evaluator type: ",attribute.defaultJunctionEvaluatorType)
    print("Default junction evaluator data: ",str(attribute.defaultJunctionData))
    #Turn specific information is supported only if network dataset supports
    #turns
    if desc.supportsTurns:
        print("Default turn evaluator type: ",attribute.defaultTurnEvaluatorType)
        print("Default turn evaluator data: ", str(attribute.defaultTurnData))

    #Describe all other evaluators
    count = attribute.evaluatorCount
    print("Evaluator count: ", count)
    for i in range(0, count):
        text = "Evaluator %d" % i
        print(text, " ---")
        edgeDir = getattr(attribute,"edgeDirection" + str(i))
        print("Edge direction: ", edgeDir)
        srcName = getattr(attribute,"sourceName" + str(i))
        print("Source Name: ", srcName)
        evaluatortype = getattr(attribute,"evaluatorType" + str(i))
        evaluatordata = getattr(attribute,"data" + str(i))
        print("Evaluator Type: ", evaluatortype)
        print("Evaluator Data: ", evaluatordata)

    #Describe attribute parameters
    print("Parameter Information........")
    paramcount = attribute.parameterCount
    if paramcount == 0:
        print("No Parameters defined.")
    else:
        print("Parameter Count: ", paramcount)
    for i in range (0, paramcount):
        paramName = getattr(attribute, "parameterName" + str(i))
        paramType = getattr(attribute, "parameterType" + str(i))
        paramDefaultValue = getattr(attribute, "parameterDefaultValue" + str(i))
        print("Parameter Name: ", paramName)
        print("Parameter Type: ", paramType)
        print("Parameter Default Value: ", paramDefaultValue)
```

### Example 2

```python
# Name: NDSAttributeProperties_ex01.py
# Description: Print the information about network attributes defined for the
#              network dataset

import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"

# Create a Describe object from the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

# Get a list of network attributes
attributes = desc.attributes
#print information for each attribute
for attribute in attributes:
    print("----------------------------------\n")
    print("Name: ", attribute.name)
    print("Units: ", attribute.units)
    print("Usage Type: ", attribute.usageType)
    print("Data Type: ", attribute.dataType)
    print("Use By Default: ", str(attribute.useByDefault))
    #Information about  default evaluators
    print("Default edge evaluator type: ", attribute.defaultEdgeEvaluatorType)
    print("Default edge evaluator data: ", str(attribute.defaultEdgeData))
    print("Default junction evaluator type: ",attribute.defaultJunctionEvaluatorType)
    print("Default junction evaluator data: ",str(attribute.defaultJunctionData))
    #Turn specific information is supported only if network dataset supports
    #turns
    if desc.supportsTurns:
        print("Default turn evaluator type: ",attribute.defaultTurnEvaluatorType)
        print("Default turn evaluator data: ", str(attribute.defaultTurnData))

    #Describe all other evaluators
    count = attribute.evaluatorCount
    print("Evaluator count: ", count)
    for i in range(0, count):
        text = "Evaluator %d" % i
        print(text, " ---")
        edgeDir = getattr(attribute,"edgeDirection" + str(i))
        print("Edge direction: ", edgeDir)
        srcName = getattr(attribute,"sourceName" + str(i))
        print("Source Name: ", srcName)
        evaluatortype = getattr(attribute,"evaluatorType" + str(i))
        evaluatordata = getattr(attribute,"data" + str(i))
        print("Evaluator Type: ", evaluatortype)
        print("Evaluator Data: ", evaluatordata)

    #Describe attribute parameters
    print("Parameter Information........")
    paramcount = attribute.parameterCount
    if paramcount == 0:
        print("No Parameters defined.")
    else:
        print("Parameter Count: ", paramcount)
    for i in range (0, paramcount):
        paramName = getattr(attribute, "parameterName" + str(i))
        paramType = getattr(attribute, "parameterType" + str(i))
        paramDefaultValue = getattr(attribute, "parameterDefaultValue" + str(i))
        print("Parameter Name: ", paramName)
        print("Parameter Type: ", paramType)
        print("Parameter Default Value: ", paramDefaultValue)
```

---

## Network Dataset properties

## Summary

The Describe function returns the following properties for network datasets. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
# Name: NDSProperties_ex01.py
# Description: Print some of the network dataset properties.
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"
# Create Describe object for the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

# Print general network dataset properties
print("Network type:   " + desc.networkType)
print("Supports turns? " + str(desc.supportsTurns))
print("Supports directions? " + str(desc.supportsDirections))
print("Is buildable?   " + str(desc.isBuildable))
print("Elevation model: " + desc.elevationModel)
print("Supports historical traffic data: " + str(desc.supportsHistoricalTrafficData))
print("Time zone attribute name: " + desc.timeZoneAttributeName)
print("Time zone table name: " + desc.timeZoneTableName)
print("Optimizations: " + ", ".join(desc.optimizations))
```

### Example 2

```python
# Name: NDSProperties_ex01.py
# Description: Print some of the network dataset properties.
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/Data/Paris.gdb/Transportation"
# Create Describe object for the network dataset
desc = arcpy.Describe("ParisMultimodal_ND")

# Print general network dataset properties
print("Network type:   " + desc.networkType)
print("Supports turns? " + str(desc.supportsTurns))
print("Supports directions? " + str(desc.supportsDirections))
print("Is buildable?   " + str(desc.isBuildable))
print("Elevation model: " + desc.elevationModel)
print("Supports historical traffic data: " + str(desc.supportsHistoricalTrafficData))
print("Time zone attribute name: " + desc.timeZoneAttributeName)
print("Time zone table name: " + desc.timeZoneTableName)
print("Optimizations: " + ", ".join(desc.optimizations))
```

---

## Network Directions Attribute Mapping

## Summary

The Network Directions Attribute Mapping object provides information about the descriptor attributes in your network dataset that are mapped to specific properties in the network dataset's directions configuration.

## Code Samples

### Example 1

```python
# Name: NDSDirectionsAttributeMapping_ex01.py
# Description: Print information about the directions attribute mappings
#              for the network dataset.

import arcpy
import sys

network = r"C:/Data/NetworkDatasetWithDirections.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

# If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the network's directions properties
directions = desc.directions

# Loop through the attribute mappings
if hasattr(directions, "attributeMappings"):
    attrMappings = directions.attributeMappings
    for mapping in attrMappings:
        print("\nKey:", mapping.key)
        print("Attribute:", mapping.attribute)
else:
    print("Network dataset does not contain directions attribute mappings.")
```

### Example 2

```python
# Name: NDSDirectionsAttributeMapping_ex01.py
# Description: Print information about the directions attribute mappings
#              for the network dataset.

import arcpy
import sys

network = r"C:/Data/NetworkDatasetWithDirections.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

# If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the network's directions properties
directions = desc.directions

# Loop through the attribute mappings
if hasattr(directions, "attributeMappings"):
    attrMappings = directions.attributeMappings
    for mapping in attrMappings:
        print("\nKey:", mapping.key)
        print("Attribute:", mapping.attribute)
else:
    print("Network dataset does not contain directions attribute mappings.")
```

---

## Network Directions

## Summary

The Network Directions object for the network dataset provides information about directions settings at the network dataset level, such as the output length units or length attribute, that are used to generate directions.

## Code Samples

### Example 1

```python
# Name: NDSDirectionProperties_ex01.py
# Description: Print direction setting for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the direction object
if desc.supportsDirections:
    direction = desc.directions
else:
    #If the directions are not set for the network dataset, exit
    print("No direction information")
    sys.exit()

print("Direction Information ----")
print("Length attribute name: " , direction.lengthAttributeName)
print("Time attribute name: " , direction.timeAttributeName)
print("Road Class attribute name: " , direction.roadClassAttributeName)
print("Default Output Length Units: " , direction.defaultOutputLengthUnits)
print("Signpost Feature Class: " , direction.signPostFeatureClassName)
print("Signpost Streets Table: " , direction.signpostStreetsTableName)
```

### Example 2

```python
# Name: NDSDirectionProperties_ex01.py
# Description: Print direction setting for the network dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#Get the direction object
if desc.supportsDirections:
    direction = desc.directions
else:
    #If the directions are not set for the network dataset, exit
    print("No direction information")
    sys.exit()

print("Direction Information ----")
print("Length attribute name: " , direction.lengthAttributeName)
print("Time attribute name: " , direction.timeAttributeName)
print("Road Class attribute name: " , direction.roadClassAttributeName)
print("Default Output Length Units: " , direction.defaultOutputLengthUnits)
print("Signpost Feature Class: " , direction.signPostFeatureClassName)
print("Signpost Streets Table: " , direction.signpostStreetsTableName)
```

---

## Network Source Directions Field Mapping

## Summary

The Network Source Directions Field Mapping object provides information about the fields in your data that are mapped to specific properties in the network dataset's directions configuration.

## Code Samples

### Example 1

```python
# Name: NDSSourceDirectionsFieldMapping_ex01.py
# Description: Print information about the directions field mappings associated
#              with edge sources in the network dataset.

import arcpy
import sys

network = r"C:/Data/NetworkDatasetWithLandmarks.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("\n--------------------")
    print("Edge source name: " , source.name)
    # Get the directions information specific to this edge source
    sDir = source.sourceDirections
    # Check if the edge source has turn and confirmation landmarks associated with it.
    # If so, print some information about the landmarks.
    if hasattr(sDir, "fieldMappings"):
        fieldMappings = sDir.fieldMappings
        print("\n--Field mapping information--")
        for fm in fieldMappings:
            print("\nProperty key:", fm.key)
            print("Along field name:", fm.alongField)
            print("Against field name:", fm.againstField)
            print("Undirected field name:", fm.undirectedField)
    else:
        print("Source does not directions field mappings.")
```

### Example 2

```python
# Name: NDSSourceDirectionsFieldMapping_ex01.py
# Description: Print information about the directions field mappings associated
#              with edge sources in the network dataset.

import arcpy
import sys

network = r"C:/Data/NetworkDatasetWithLandmarks.gdb/Transportation/Streets_ND"

# Create Describe object for the network dataset
desc = arcpy.Describe(network)

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("\n--------------------")
    print("Edge source name: " , source.name)
    # Get the directions information specific to this edge source
    sDir = source.sourceDirections
    # Check if the edge source has turn and confirmation landmarks associated with it.
    # If so, print some information about the landmarks.
    if hasattr(sDir, "fieldMappings"):
        fieldMappings = sDir.fieldMappings
        print("\n--Field mapping information--")
        for fm in fieldMappings:
            print("\nProperty key:", fm.key)
            print("Along field name:", fm.alongField)
            print("Against field name:", fm.againstField)
            print("Undirected field name:", fm.undirectedField)
    else:
        print("Source does not directions field mappings.")
```

---

## Network Source Directions

## Summary

The Network Source Directions object provides information used for generating driving directions that are specific to edge sources in the network dataset.

## Code Samples

### Example 1

```python
# Name: NDSNetworkSourceDirectionProperties_ex01.py
# Description: Print direction settings specific to edge sources in the network
#              dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Print the direction information specific to edge source
    sDir = source.sourceDirections
    # Check if the administrative area information is defined for the network
    #dataset. Otherwise adminAreaFieldName property throws an exception
    if hasattr(sDir, "adminAreaFieldName"):
        print("Administrative area field: " , sDir.AdminAreaFieldName)
    else:
        print("Administrative area field: " , "Not set")
```

### Example 2

```python
# Name: NDSNetworkSourceDirectionProperties_ex01.py
# Description: Print direction settings specific to edge sources in the network
#              dataset.

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

#If there are no edge sources in the network dataset, quit.
if not sources:
    print("No edge sources")
    sys.exit()

#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Print the direction information specific to edge source
    sDir = source.sourceDirections
    # Check if the administrative area information is defined for the network
    #dataset. Otherwise adminAreaFieldName property throws an exception
    if hasattr(sDir, "adminAreaFieldName"):
        print("Administrative area field: " , sDir.AdminAreaFieldName)
    else:
        print("Administrative area field: " , "Not set")
```

---

## Network Source

## Summary

Provides information about the network sources in the network dataset. Network sources can be of four types; edge sources, junction sources, turn sources, and system junction sources. Use the sourceType property to identify the type of network source.

## Code Samples

### Example 1

```python
# Name: NDSNetworkSourceProperties_ex01.py
# Description: Print the information about the network sources for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- Network sources")

#Get all the network sources for the network dataset
sources = desc.sources
if not sources:
    print("%*s" % (justify, "(No network sources)"))
    sys.exit(0)

for source in sources:
    print("%*s: %s" % (justify, "Source Name" , source.name))
    print("%*s: %s" % (justify, "Source ID" , str(source.sourceID)))
    print("%*s: %s" % (justify, "Source Type", source.sourceType))
    print("%*s: %s" % (justify, "Element Type", source.elementType))
    print(" ")
```

### Example 2

```python
# Name: NDSNetworkSourceProperties_ex01.py
# Description: Print the information about the network sources for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- Network sources")

#Get all the network sources for the network dataset
sources = desc.sources
if not sources:
    print("%*s" % (justify, "(No network sources)"))
    sys.exit(0)

for source in sources:
    print("%*s: %s" % (justify, "Source Name" , source.name))
    print("%*s: %s" % (justify, "Source ID" , str(source.sourceID)))
    print("%*s: %s" % (justify, "Source Type", source.sourceType))
    print("%*s: %s" % (justify, "Element Type", source.elementType))
    print(" ")
```

---

## NumPyArrayToRaster

## Summary

Converts a NumPy array to a raster.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_array | The NumPy array to convert to a raster. A two- or three-dimensional NumPy array is required. | NumPyArray |
| lower_left_corner | A Point object defining the lower left corner of the output raster in map units.The default will set the lower left corner to coordinate (0.0, 0.0).(The default value is None) | Point |
| x_cell_size | The cell size in the x direction specified in map units. The input can be a specified cell size (type: double) value, or a raster.When a dataset is specified, the x cell size of that dataset is used for the x cell size of the output raster.If only the x_cell_size is identified and not the y_cell_size, a square cell will result with the specified size.If neither x_cell_size nor y_cell_size is specified, a default of 1.0 will be used for both the x and y cell size.(The default value is 1.0) | Double |
| y_cell_size | The cell size in the y direction specified in map units. The input can be a specified cell size (type: double) value, or a raster.When a dataset is specified, the x cell size of that dataset is used for the y cell size of the output raster.If only the y_cell_size is identified and not the x_cell_size, a square cell will result with the specified size.If neither x_cell_size nor y_cell_size is specified, a default of 1.0 will be used for both the x and y cell size.(The default value is 1.0) | Double |
| value_to_nodata | The value in the NumPy array to assign to NoData in the output raster. If no value is specified for value_to_nodata, there will not be any NoData values in the resulting raster.(The default value is None) | Double |
| mdinfo | The string or JSON that defines the variables and dimensions within the multidimensional raster dataset, used to build multidimensional information. The string should use the following format: {"variables":[{"name": <variable_name>, "dimensions": [{"name": <dimension_name>, "description": <dimension_description>, "unit": <dimension_unit>, "extent": [<dimension_min>, <dimension_max>], "values": [<dimension_values>,…]},…]}, …]}(The default value is None) | String |

## Code Samples

### Example 1

```python
NumPyArrayToRaster (in_array, {lower_left_corner}, {x_cell_size}, {y_cell_size}, {value_to_nodata}, {mdinfo})
```

### Example 2

```python
import arcpy
import numpy

# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,2500)
myArray.shape = (50,50)

# Convert array to a geodatabase raster
myRaster = arcpy.NumPyArrayToRaster(myArray,x_cell_size=1)
myRaster.save("C:/output/fgdb.gdb/myRandomRaster")
```

### Example 3

```python
import arcpy
import numpy

# Create a simple array from scratch using random values
myArray = numpy.random.random_integers(0,100,2500)
myArray.shape = (50,50)

# Convert array to a geodatabase raster
myRaster = arcpy.NumPyArrayToRaster(myArray,x_cell_size=1)
myRaster.save("C:/output/fgdb.gdb/myRandomRaster")
```

### Example 4

```python
# Note that, if the input raster is multiband, the data blocks will also be
# multiband, having dimensions (bands, rows, columns).  Otherwise, they will
# have dimensions (rows, columns).

import arcpy
import numpy
import os

# Input raster
filein = os.path.join(os.getcwd(),r"input\input.tif")

# Output raster (after processing)
fileout = os.path.join(os.getcwd(),r"output\blockprocessingrdb22.tif")

# Size of processing data block
# where memorysize = datatypeinbytes*nobands*blocksize^2
blocksize = 512

# ----------------------------------------------------------------------------
# Create raster object from file
myRaster = arcpy.Raster(filein)

# Set environmental variables for output
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = filein
arcpy.env.cellSize = filein

# Loop over data blocks
filelist = []
blockno = 0
for x in range(0, myRaster.width, blocksize):
    for y in range(0, myRaster.height, blocksize):

        # Lower left coordinate of block (in map units)
        mx = myRaster.extent.XMin + x * myRaster.meanCellWidth
        my = myRaster.extent.YMin + y * myRaster.meanCellHeight
        # Upper right coordinate of block (in cells)
        lx = min([x + blocksize, myRaster.width])
        ly = min([y + blocksize, myRaster.height])
        #   noting that (x, y) is the lower left coordinate (in cells)

        # Extract data block
        myData = arcpy.RasterToNumPyArray(myRaster, arcpy.Point(mx, my),
                                          lx-x, ly-y)

        # PROCESS DATA BLOCK -----------------------------
        # e.g. Calculate mean of each cell of all bands.
        myData -= numpy.mean(myData, axis=0, keepdims=True)
        # ------------------------------------------------

        # Convert data block back to raster
        myRasterBlock = arcpy.NumPyArrayToRaster(myData, arcpy.Point(mx, my),
                                                 myRaster.meanCellWidth,
                                                 myRaster.meanCellHeight)

        # Save on disk temporarily as 'filename_#.ext'
        filetemp = ('_%i.' % blockno).join(fileout.rsplit('.',1))
        myRasterBlock.save(filetemp)

        # Maintain a list of saved temporary files
        filelist.append(filetemp)
        blockno += 1

# Mosaic temporary files
arcpy.management.Mosaic(';'.join(filelist[1:]), filelist[0])
if arcpy.Exists(fileout):
    arcpy.management.Delete(fileout)
arcpy.management.Rename(filelist[0], fileout)

# Remove temporary files
for fileitem in filelist:
    if arcpy.Exists(fileitem):
        arcpy.management.Delete(fileitem)

# Release raster objects from memory
del myRasterBlock
del myRaster
# ----------------------------------------------------------------------------
```

### Example 5

```python
# Note that, if the input raster is multiband, the data blocks will also be
# multiband, having dimensions (bands, rows, columns).  Otherwise, they will
# have dimensions (rows, columns).

import arcpy
import numpy
import os

# Input raster
filein = os.path.join(os.getcwd(),r"input\input.tif")

# Output raster (after processing)
fileout = os.path.join(os.getcwd(),r"output\blockprocessingrdb22.tif")

# Size of processing data block
# where memorysize = datatypeinbytes*nobands*blocksize^2
blocksize = 512

# ----------------------------------------------------------------------------
# Create raster object from file
myRaster = arcpy.Raster(filein)

# Set environmental variables for output
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = filein
arcpy.env.cellSize = filein

# Loop over data blocks
filelist = []
blockno = 0
for x in range(0, myRaster.width, blocksize):
    for y in range(0, myRaster.height, blocksize):

        # Lower left coordinate of block (in map units)
        mx = myRaster.extent.XMin + x * myRaster.meanCellWidth
        my = myRaster.extent.YMin + y * myRaster.meanCellHeight
        # Upper right coordinate of block (in cells)
        lx = min([x + blocksize, myRaster.width])
        ly = min([y + blocksize, myRaster.height])
        #   noting that (x, y) is the lower left coordinate (in cells)

        # Extract data block
        myData = arcpy.RasterToNumPyArray(myRaster, arcpy.Point(mx, my),
                                          lx-x, ly-y)

        # PROCESS DATA BLOCK -----------------------------
        # e.g. Calculate mean of each cell of all bands.
        myData -= numpy.mean(myData, axis=0, keepdims=True)
        # ------------------------------------------------

        # Convert data block back to raster
        myRasterBlock = arcpy.NumPyArrayToRaster(myData, arcpy.Point(mx, my),
                                                 myRaster.meanCellWidth,
                                                 myRaster.meanCellHeight)

        # Save on disk temporarily as 'filename_#.ext'
        filetemp = ('_%i.' % blockno).join(fileout.rsplit('.',1))
        myRasterBlock.save(filetemp)

        # Maintain a list of saved temporary files
        filelist.append(filetemp)
        blockno += 1

# Mosaic temporary files
arcpy.management.Mosaic(';'.join(filelist[1:]), filelist[0])
if arcpy.Exists(fileout):
    arcpy.management.Delete(fileout)
arcpy.management.Rename(filelist[0], fileout)

# Remove temporary files
for fileitem in filelist:
    if arcpy.Exists(fileitem):
        arcpy.management.Delete(fileitem)

# Release raster objects from memory
del myRasterBlock
del myRaster
# ----------------------------------------------------------------------------
```

### Example 6

```python
import arcpy
import numpy

# Create multidimensional raster object from the NetCDF file
in_raster = Raster("myData.nc", True)
lowerLeft = arcpy.Point(in_raster.extent.XMin, in_raster.extent.YMin)
blockSize = 256

# Convert Raster to Array 
myRasterBlock = arcpy.NumPyArrayToRaster(in_raster, lowerLeft, blockSize, blockSize)
```

### Example 7

```python
import arcpy
import numpy

# Create multidimensional raster object from the NetCDF file
in_raster = Raster("myData.nc", True)
lowerLeft = arcpy.Point(in_raster.extent.XMin, in_raster.extent.YMin)
blockSize = 256

# Convert Raster to Array 
myRasterBlock = arcpy.NumPyArrayToRaster(in_raster, lowerLeft, blockSize, blockSize)
```

---

## OD Cost Matrix Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the od cost matrix solver.

---

## Output Condition properties

## Summary

The properties below are returned by the outputConditions object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Output Condition Properties
        print(" - Output Condition Properties - ")
        for oc in ust.outputConditions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Name: {oc.name}")
                print(f"Type: {oc.type}")
                print(f"Operator: {oc.operator}")
                print(f"Value: {oc.value}")
                print(f"CombineUsingOr: {oc.combineUsingOr}")
                print(f"Is Specific Value: {oc.isSpecificValue} \n")
            except:
                print("Skipped output condition properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Output Condition Properties
        print(" - Output Condition Properties - ")
        for oc in ust.outputConditions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Name: {oc.name}")
                print(f"Type: {oc.type}")
                print(f"Operator: {oc.operator}")
                print(f"Value: {oc.value}")
                print(f"CombineUsingOr: {oc.combineUsingOr}")
                print(f"Is Specific Value: {oc.isSpecificValue} \n")
            except:
                print("Skipped output condition properties. \n")
```

---

## Output Filter properties

## Summary

The properties below are returned by the outputFilters object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Output Filter Properties
        print(" - Output Filter Properties - ")
        for ofp in ust.outputFilters:
            # Try to get these properties if the exist, else, print the empty list
            try:
                for of in ofp:
                    print(f"Network Source ID: {of.networkSourceID}")
                    print(f"Asset Group Code: {of.assetGroupCode}")
                    print(f"Asset Type Code: {of.assetTypeCode} \n")
            except:
                print("Skipped output filter properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Output Filter Properties
        print(" - Output Filter Properties - ")
        for ofp in ust.outputFilters:
            # Try to get these properties if the exist, else, print the empty list
            try:
                for of in ofp:
                    print(f"Network Source ID: {of.networkSourceID}")
                    print(f"Asset Group Code: {of.assetGroupCode}")
                    print(f"Asset Type Code: {of.assetTypeCode} \n")
            except:
                print("Skipped output filter properties. \n")
```

---

## Parcel Fabric properties

## Summary

The Describe function returns the following properties for parcel fabrics. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the parcel fabric dataset
desc = arcpy.Describe("C:/Data/Parcels.gdb/County/ParcelFabric")

# Print parcel type names associated with the parcel fabric
for p in desc.parcelTypeNames:
    print ("Parcel type: " + p)

# Print parcel type lists
for p in desc.parcelTypes:
    print(p)

# Print the name for the Lots parcel type
for i in desc.parcelTypes:
    if i[0] == 'Lot':
        print(i[0])

# Print topology name associated with the parcel fabric
print("topology: " + desc.topology.name)

# Print the name of the parcel fabric records feature class
print("Records: " + desc.recordsFeatureClass.name")

# Print the names of the adjustment feature classes
print("adjustment points: " + desc.AdjustmentPointsFeatureClass.name)
print("adjustment lines: " + desc.AdjustmentLinesFeatureClass.name)
print("adjustment vectors: " + desc.AdjustmentVectorsFeatureClass.name)
```

### Example 2

```python
import arcpy

# Create a Describe object from the parcel fabric dataset
desc = arcpy.Describe("C:/Data/Parcels.gdb/County/ParcelFabric")

# Print parcel type names associated with the parcel fabric
for p in desc.parcelTypeNames:
    print ("Parcel type: " + p)

# Print parcel type lists
for p in desc.parcelTypes:
    print(p)

# Print the name for the Lots parcel type
for i in desc.parcelTypes:
    if i[0] == 'Lot':
        print(i[0])

# Print topology name associated with the parcel fabric
print("topology: " + desc.topology.name)

# Print the name of the parcel fabric records feature class
print("Records: " + desc.recordsFeatureClass.name")

# Print the names of the adjustment feature classes
print("adjustment points: " + desc.AdjustmentPointsFeatureClass.name)
print("adjustment lines: " + desc.AdjustmentLinesFeatureClass.name)
print("adjustment vectors: " + desc.AdjustmentVectorsFeatureClass.name)
```

---

## ParseFieldName

## Summary

Parses a fully qualified field name into its components (database, owner name, table name, and field name) depending on the workspace. ParseFieldName returns a string that includes the parsed table name and contains the database, owner, table, and field names, separated by commas. The workspace must be a file, or enterprise geodatabase.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The field name to be parsed. | String |
| workspace | Specifies the workspace for fully qualifying the field name. The workspace must be a file, or enterprise geodatabase. | String |

## Code Samples

### Example 1

```python
ParseFieldName (name, {workspace})
```

### Example 2

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

# Parse the field name into database, owner, table and field
fullname = arcpy.ParseFieldName(field_name, workspace)
database, owner, table, field = fullname.split(", ")
```

### Example 3

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

# Parse the field name into database, owner, table and field
fullname = arcpy.ParseFieldName(field_name, workspace)
database, owner, table, field = fullname.split(", ")
```

---

## ParseTableName

## Summary

Parses a table name into its components (database, owner, table) depending on the workspace. ParseTableName returns a string containing the parsed table name, with the database name, owner name, and table name, separated by commas. This workspace must be a personal, file, or enterprise geodatabase.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | Specifies which table will be parsed. | String |
| workspace | Specifies the workspace for fully qualifying the table name. The workspace must be a personal, file, or enterprise geodatabase. | String |

## Code Samples

### Example 1

```python
ParseTableName (name, {workspace})
```

### Example 2

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

# Parse the table name into database, owner, and table
fullname = arcpy.ParseTableName(field_name, workspace)
database, owner, table = fullname.split(", ")
```

### Example 3

```python
import arcpy

field_name = arcpy.GetParameterAsText(0)
workspace = arcpy.GetParameterAsText(1)

# Parse the table name into database, owner, and table
fullname = arcpy.ParseTableName(field_name, workspace)
database, owner, table = fullname.split(", ")
```

---

## Projection File properties

## Summary

The Describe function returns the following properties for projection files.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe Object from a prj file.
#
desc = arcpy.Describe("C:\data\mexico.prj")

# Print some properties of the SpatialReference class object.
#
SR = desc.spatialReference
print("Name:            " + SR.name)
print("Type:            " + SR.type)
print("isHighPrecision: " + str(SR.isHighPrecision))
print("scaleFactor:     " + str(SR.scaleFactor))
```

### Example 2

```python
import arcpy

# Create a Describe Object from a prj file.
#
desc = arcpy.Describe("C:\data\mexico.prj")

# Print some properties of the SpatialReference class object.
#
SR = desc.spatialReference
print("Name:            " + SR.name)
print("Type:            " + SR.type)
print("isHighPrecision: " + str(SR.isHighPrecision))
print("scaleFactor:     " + str(SR.scaleFactor))
```

---

## ProductInfo

## Summary

Returns the current product license.

## Code Samples

### Example 1

```python
ProductInfo ()
```

### Example 2

```python
import arcpy

print(arcpy.ProductInfo())
```

### Example 3

```python
import arcpy

print(arcpy.ProductInfo())
```

---

## Propagator properties

## Summary

The properties below are returned by the propagators object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Propagator Properties
        print(" - Propagator Properties - ")
        for p in ust.propagators:
            # Try to get these properties if they exist; otherwise, print the empty list
            try:
                print(f"Network Attribute Name: {p.networkAttributeName}")
                print(f"Trace Propagator Function Type: {p.tracePropagatorFunctionType}")
                print(f"Network Attribute Filter Operator: {p.networkAttributeOperator}")
                print(f"Network Attribute Value: {p.value}")
                print(f"Propagated Attribute Name: {p.propagatedAttributeName}")
                print(f"Substitution Attribute Name: {p.substitutionAttributeName}")
            except:
                print("Skipped propagator properties. \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties     
        ust = tier.updateSubnetworkTraceConfiguration

        # Propagator Properties
        print(" - Propagator Properties - ")
        for p in ust.propagators:
            # Try to get these properties if they exist; otherwise, print the empty list
            try:
                print(f"Network Attribute Name: {p.networkAttributeName}")
                print(f"Trace Propagator Function Type: {p.tracePropagatorFunctionType}")
                print(f"Network Attribute Filter Operator: {p.networkAttributeOperator}")
                print(f"Network Attribute Value: {p.value}")
                print(f"Propagated Attribute Name: {p.propagatedAttributeName}")
                print(f"Substitution Attribute Name: {p.substitutionAttributeName}")
            except:
                print("Skipped propagator properties. \n")
```

---

## Raster Band properties

## Summary

The Describe function returns the following properties for raster bands. The Table and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the raster band
#
desc = arcpy.Describe("C:/data/preston.img/Band_1")

# Print some raster band properties
#
print("Height: %d" % desc.height)
print("Width:  %d" % desc.width)
print("Integer Raster: %s" % desc.isInteger)
```

### Example 2

```python
import arcpy

# Create a Describe object from the raster band
#
desc = arcpy.Describe("C:/data/preston.img/Band_1")

# Print some raster band properties
#
print("Height: %d" % desc.height)
print("Width:  %d" % desc.width)
print("Integer Raster: %s" % desc.isInteger)
```

---

## Raster Catalog properties

## Summary

The Describe function returns the following properties for raster catalogs. The Geodatabase Feature Class, Feature Class, Geodatabase Table, Table, and Dataset property groups are also supported. The Editor Tracking property group is supported if editor tracking has been enabled for this raster catalog.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the raster catalog
#
desc = arcpy.Describe("C:/data/simon.gdb/idaho")

# Print the RasterFieldName property
#
print("Raster field name: " + desc.rasterFieldName)
```

### Example 2

```python
import arcpy

# Create a Describe object from the raster catalog
#
desc = arcpy.Describe("C:/data/simon.gdb/idaho")

# Print the RasterFieldName property
#
print("Raster field name: " + desc.rasterFieldName)
```

---

## Raster Dataset properties

## Summary

The Describe function returns the following properties for raster datasets. The Dataset property group is also supported. Single-band raster datasets also support the Raster Band property group.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the raster dataset
#
desc = arcpy.Describe(r"C:\temp\FGDB.gdb\RD")

# Print some raster dataset properties
# 
print("Band Count:       %d" % desc.bandCount)
print("Compression Type: %s" % desc.compressionType)
print("Raster Format:    %s" % desc.format)
print("Permanent:        %s" % desc.permanent)
print("Sensor Type:      %s" % desc.sensorType)
```

### Example 2

```python
import arcpy

# Create a Describe object from the raster dataset
#
desc = arcpy.Describe(r"C:\temp\FGDB.gdb\RD")

# Print some raster dataset properties
# 
print("Band Count:       %d" % desc.bandCount)
print("Compression Type: %s" % desc.compressionType)
print("Raster Format:    %s" % desc.format)
print("Permanent:        %s" % desc.permanent)
print("Sensor Type:      %s" % desc.sensorType)
```

---

## RasterToNumPyArray

## Summary

Converts a raster to a NumPy array.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| in_raster | The input raster to convert to a NumPy array. | Raster |
| lower_left_corner | The lower left corner within the in_raster from which to extract the processing block to convert to an array. The x- and y-values are in map units. If no value is specified, the origin of the input raster will be used.(The default value is None) | Point |
| ncols | The number of columns from the lower_left_corner in the in_raster to convert to the NumPy array.If no value is specified, the number of columns of the input raster will be used.(The default value is None) | Integer |
| nrows | The number of rows from the lower_left_corner in the in_raster to convert to the NumPy array.If no value is specified, the number of rows of the input raster will used.(The default value is None) | Integer |
| nodata_to_value | The value to assign the in_raster NoData values in the resulting NumPy array.If no value is specified, the NoData value of in_raster will be used.(The default value is None) | Variant |

## Code Samples

### Example 1

```python
RasterToNumPyArray (in_raster, {lower_left_corner}, {ncols}, {nrows}, {nodata_to_value})
```

### Example 2

```python
import arcpy
import numpy

# Get input Raster properties
inRas = arcpy.Raster('C:/data/inRaster')
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

# Calculate percentage of the row for each cell value
arrSum = arr.sum(1)
arrSum.shape = (arr.shape[0],1)
arrPerc = (arr)/arrSum

#Convert Array to raster (keep the origin and cellsize the same as the input)
newRaster = arcpy.NumPyArrayToRaster(arrPerc,lowerLeft,cellSize,
                                     value_to_nodata=0)
newRaster.save("C:/output/fgdb.gdb/PercentRaster")
```

### Example 3

```python
import arcpy
import numpy

# Get input Raster properties
inRas = arcpy.Raster('C:/data/inRaster')
lowerLeft = arcpy.Point(inRas.extent.XMin,inRas.extent.YMin)
cellSize = inRas.meanCellWidth

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(inRas,nodata_to_value=0)

# Calculate percentage of the row for each cell value
arrSum = arr.sum(1)
arrSum.shape = (arr.shape[0],1)
arrPerc = (arr)/arrSum

#Convert Array to raster (keep the origin and cellsize the same as the input)
newRaster = arcpy.NumPyArrayToRaster(arrPerc,lowerLeft,cellSize,
                                     value_to_nodata=0)
newRaster.save("C:/output/fgdb.gdb/PercentRaster")
```

### Example 4

```python
# Note that, if the input raster is multiband, the data blocks will also be
# multiband, having dimensions (bands, rows, columns).  Otherwise, they will
# have dimensions of (rows, columns).

import arcpy
import numpy
import os

# Input raster
filein = os.path.join(os.getcwd(),r"input\input.tif")

# Output raster (after processing)
fileout = os.path.join(os.getcwd(),r"output\blockprocessingrdb22.tif")

# Size of processing data block
#  where memorysize = datatypeinbytes * numbands * blocksize^2
blocksize = 512

# ----------------------------------------------------------------------------
# Create raster object from file
myRaster = arcpy.Raster(filein)

# Set environmental variables for output
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = filein
arcpy.env.cellSize = filein

# Loop over data blocks
filelist = []
blocknum = 0
for x in range(0, myRaster.width, blocksize):
    for y in range(0, myRaster.height, blocksize):

        # Lower left coordinate of block (in map units)
        mx = myRaster.extent.XMin + x * myRaster.meanCellWidth
        my = myRaster.extent.YMin + y * myRaster.meanCellHeight
        # Upper right coordinate of block (in cells)
        lx = min([x + blocksize, myRaster.width])
        ly = min([y + blocksize, myRaster.height])
        #   noting that (x, y) is the lower left coordinate (in cells)

        # Extract data block
        myData = arcpy.RasterToNumPyArray(myRaster, arcpy.Point(mx, my),
                                          lx-x, ly-y)

        # PROCESS DATA BLOCK -----------------------------
        # e.g., Calculate mean of each cell of all bands.
        myData -= numpy.mean(myData, axis=0, keepdims=True)
        # ------------------------------------------------

        # Convert data block back to raster
        myRasterBlock = arcpy.NumPyArrayToRaster(myData, arcpy.Point(mx, my),
                                                 myRaster.meanCellWidth,
                                                 myRaster.meanCellHeight)

        # Save on disk temporarily as 'filename_#.ext'
        filetemp = ('_%i.' % blocknum).join(fileout.rsplit('.',1))
        myRasterBlock.save(filetemp)

        # Maintain a list of saved temporary files
        filelist.append(filetemp)
        blocknum += 1

# Mosaic temporary files
arcpy.management.Mosaic(';'.join(filelist[1:]), filelist[0])
if arcpy.Exists(fileout):
    arcpy.management.Delete(fileout)
arcpy.management.Rename(filelist[0], fileout)

# Remove temporary files
for fileitem in filelist:
    if arcpy.Exists(fileitem):
        arcpy.management.Delete(fileitem)

# Release raster objects from memory
del myRasterBlock
del myRaster
# ----------------------------------------------------------------------------
```

### Example 5

```python
# Note that, if the input raster is multiband, the data blocks will also be
# multiband, having dimensions (bands, rows, columns).  Otherwise, they will
# have dimensions of (rows, columns).

import arcpy
import numpy
import os

# Input raster
filein = os.path.join(os.getcwd(),r"input\input.tif")

# Output raster (after processing)
fileout = os.path.join(os.getcwd(),r"output\blockprocessingrdb22.tif")

# Size of processing data block
#  where memorysize = datatypeinbytes * numbands * blocksize^2
blocksize = 512

# ----------------------------------------------------------------------------
# Create raster object from file
myRaster = arcpy.Raster(filein)

# Set environmental variables for output
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = filein
arcpy.env.cellSize = filein

# Loop over data blocks
filelist = []
blocknum = 0
for x in range(0, myRaster.width, blocksize):
    for y in range(0, myRaster.height, blocksize):

        # Lower left coordinate of block (in map units)
        mx = myRaster.extent.XMin + x * myRaster.meanCellWidth
        my = myRaster.extent.YMin + y * myRaster.meanCellHeight
        # Upper right coordinate of block (in cells)
        lx = min([x + blocksize, myRaster.width])
        ly = min([y + blocksize, myRaster.height])
        #   noting that (x, y) is the lower left coordinate (in cells)

        # Extract data block
        myData = arcpy.RasterToNumPyArray(myRaster, arcpy.Point(mx, my),
                                          lx-x, ly-y)

        # PROCESS DATA BLOCK -----------------------------
        # e.g., Calculate mean of each cell of all bands.
        myData -= numpy.mean(myData, axis=0, keepdims=True)
        # ------------------------------------------------

        # Convert data block back to raster
        myRasterBlock = arcpy.NumPyArrayToRaster(myData, arcpy.Point(mx, my),
                                                 myRaster.meanCellWidth,
                                                 myRaster.meanCellHeight)

        # Save on disk temporarily as 'filename_#.ext'
        filetemp = ('_%i.' % blocknum).join(fileout.rsplit('.',1))
        myRasterBlock.save(filetemp)

        # Maintain a list of saved temporary files
        filelist.append(filetemp)
        blocknum += 1

# Mosaic temporary files
arcpy.management.Mosaic(';'.join(filelist[1:]), filelist[0])
if arcpy.Exists(fileout):
    arcpy.management.Delete(fileout)
arcpy.management.Rename(filelist[0], fileout)

# Remove temporary files
for fileitem in filelist:
    if arcpy.Exists(fileitem):
        arcpy.management.Delete(fileitem)

# Release raster objects from memory
del myRasterBlock
del myRaster
# ----------------------------------------------------------------------------
```

### Example 6

```python
# Note that, if the input multidimensional raster is also multiband, the data blocks will have dimensions (bands, rows, columns, slices).  Otherwise, they will
# have dimensions of (rows, columns, slices).

import arcpy
import numpy

# Get input multidimensional Raster 
in_mdim_raster = arcpy.Raster('C:/data/water_temp.nc', True)

lowerLeft = arcpy.Point(in_mdim_raster.extent.XMin,in_mdim_raster.extent.YMin)
blockSize = 512

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(in_mdim_raster, lower_left_corner = lowerLeft, ncols = blockSize, nrows = blockSize, nodata_to_value=0)

# the shape of the numpy array is [rows, cols, slices]
print(arr.shape)
```

### Example 7

```python
# Note that, if the input multidimensional raster is also multiband, the data blocks will have dimensions (bands, rows, columns, slices).  Otherwise, they will
# have dimensions of (rows, columns, slices).

import arcpy
import numpy

# Get input multidimensional Raster 
in_mdim_raster = arcpy.Raster('C:/data/water_temp.nc', True)

lowerLeft = arcpy.Point(in_mdim_raster.extent.XMin,in_mdim_raster.extent.YMin)
blockSize = 512

# Convert Raster to numpy array
arr = arcpy.RasterToNumPyArray(in_mdim_raster, lower_left_corner = lowerLeft, ncols = blockSize, nrows = blockSize, nodata_to_value=0)

# the shape of the numpy array is [rows, cols, slices]
print(arr.shape)
```

---

## Record Set and Feature Set properties

## Summary

The Describe function returns the following properties for instances of the RecordSet and FeatureSet objects. The Table and Dataset property groups are also supported by both. In addition, Feature Set supports the Feature Class property group. Many of these properties will be empty unless the RecordSet or FeatureSet has been populated by calling its load method.

## Code Samples

### Example 1

```python
import arcpy

# Describe a populated arcpy.FeatureSet
#
fSet = arcpy.FeatureSet()
fSet.load("C:\data\moad.gdb\Water_Bodies")
desc = arcpy.Describe(fSet)

# print a JSON representation
print((desc.pjson))
```

### Example 2

```python
import arcpy

# Describe a populated arcpy.FeatureSet
#
fSet = arcpy.FeatureSet()
fSet.load("C:\data\moad.gdb\Water_Bodies")
desc = arcpy.Describe(fSet)

# print a JSON representation
print((desc.pjson))
```

---

## RefreshLayer

## Summary

Refreshes the map views containing the specified layers.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| layer_name[layer_name,...] | The layer in the table of contents that will be refreshed. | String |

## Code Samples

### Example 1

```python
RefreshLayer (layer_name)
```

### Example 2

```python
import arcpy
lyr_name = "Cities"

with arcpy.da.UpdateCursor(lyr_name, "Class") as ucur:
    for row in ucur:
        row[0] += 1
        ucur.updateRow(row)

arcpy.RefreshLayer(lyr_name)
```

### Example 3

```python
import arcpy
lyr_name = "Cities"

with arcpy.da.UpdateCursor(lyr_name, "Class") as ucur:
    for row in ucur:
        row[0] += 1
        ucur.updateRow(row)

arcpy.RefreshLayer(lyr_name)
```

### Example 4

```python
import arcpy

lyrs = ["fc1", "fc2"]

for lyr_name in lyrs:
    with arcpy.da.UpdateCursor(lyr_name, "Class") as ucur:
        for row in ucur:
            row[0] += 1
            ucur.updateRow(row)

arcpy.RefreshLayer(lyrs)
```

### Example 5

```python
import arcpy

lyrs = ["fc1", "fc2"]

for lyr_name in lyrs:
    with arcpy.da.UpdateCursor(lyr_name, "Class") as ucur:
        for row in ucur:
            row[0] += 1
            ucur.updateRow(row)

arcpy.RefreshLayer(lyrs)
```

---

## Relationship Class properties

## Summary

The Describe function returns the following properties for relationship classes. The Geodatabase Table, Table, and Dataset property groups are also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/moad.gdb/West/bapCompAttRel")

# Print relationship class properties
#
print ("Backward Path Label: {}".format(desc.backwardPathLabel))
print ("Cardinality: {}".format(desc.cardinality))
print ("Class key: {}".format(desc.classKey))
print ("Destination Class Names: {}".format(desc.destinationClassNames))
print ("Forward Path Label: {}".format(desc.forwardPathLabel)) 
print ("Is Attributed: {}".format(desc.isAttributed))
print ("Is Composite: {}".format(desc.isComposite)) 
print ("Is Reflexive: {}".format(desc.isReflexive))
print ("Key Type: {}".format(desc.keyType))
print ("Notification Direction: {}".format(desc.notification))
print ("Origin Class Names: {}".format(desc.originClassNames))
```

### Example 2

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/moad.gdb/West/bapCompAttRel")

# Print relationship class properties
#
print ("Backward Path Label: {}".format(desc.backwardPathLabel))
print ("Cardinality: {}".format(desc.cardinality))
print ("Class key: {}".format(desc.classKey))
print ("Destination Class Names: {}".format(desc.destinationClassNames))
print ("Forward Path Label: {}".format(desc.forwardPathLabel)) 
print ("Is Attributed: {}".format(desc.isAttributed))
print ("Is Composite: {}".format(desc.isComposite)) 
print ("Is Reflexive: {}".format(desc.isReflexive))
print ("Key Type: {}".format(desc.keyType))
print ("Notification Direction: {}".format(desc.notification))
print ("Origin Class Names: {}".format(desc.originClassNames))
```

---

## Relationship Rules properties

## Summary

The Describe function returns the following properties for the relationship class rules of a RelationshipClass data type.

## Code Samples

### Example 1

```python
import arcpy
desc = arcpy.Describe(r'D:\Riverside.gdb\Electric\PolesToTransformers')
for rule in desc.relationshipRules:
	  print("Rule id: {}".format(rule.ruleID))
	  print("Destination Class ID: {}".format(rule.destinationClassID))
	  print("Destination Subtype Code: {}".format(rule.destinationSubtypeCode))
	  print("Origin Class ID: {}".format(rule.originClassID))
	  print("Origin Subtype Code: {}".format(rule.originSubtypeCode))
	  print("Destination Min Cardinality: {}".format(rule.destinationMinimumCardinality))
	  print("Destination Max Cardinality: {}".format(rule.destinationMaximumCardinality))
	  print("Origin Min Cardinality: {}".format(rule.originMinimumCardinality))
	  print("Origin Max Cardinality: {}".format(rule.originMaximumCardinality))
```

### Example 2

```python
import arcpy
desc = arcpy.Describe(r'D:\Riverside.gdb\Electric\PolesToTransformers')
for rule in desc.relationshipRules:
	  print("Rule id: {}".format(rule.ruleID))
	  print("Destination Class ID: {}".format(rule.destinationClassID))
	  print("Destination Subtype Code: {}".format(rule.destinationSubtypeCode))
	  print("Origin Class ID: {}".format(rule.originClassID))
	  print("Origin Subtype Code: {}".format(rule.originSubtypeCode))
	  print("Destination Min Cardinality: {}".format(rule.destinationMinimumCardinality))
	  print("Destination Max Cardinality: {}".format(rule.destinationMaximumCardinality))
	  print("Origin Min Cardinality: {}".format(rule.originMinimumCardinality))
	  print("Origin Max Cardinality: {}".format(rule.originMaximumCardinality))
```

---

## RemoveDataStoreItem

## Summary

Unregisters a folder or database from an ArcGIS Server site.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| connection_file | For a hosting server, provide the server URL or use the MY_HOSTED_SERVICES keyword. For a stand-alone server, an ArcGIS Server connection file (.ags) representing the server with which you want to register the data. | String |
| datastore_type | The type of data being unregistered.DATABASE—The data resides in an enterprise database.FOLDER—The data is file-based. | String |
| connection_name | The name of the folder or database being unregistered, as it is currently registered with the ArcGIS Server site. | String |

## Code Samples

### Example 1

```python
RemoveDataStoreItem (connection_file, datastore_type, connection_name)
```

### Example 2

```python
import arcpy

arcpy.RemoveDataStoreItem("GIS Servers/MyConnection.ags", "FOLDER",
                          "My local data folder")
```

### Example 3

```python
import arcpy

arcpy.RemoveDataStoreItem("GIS Servers/MyConnection.ags", "FOLDER",
                          "My local data folder")
```

### Example 4

```python
import arcpy

arcpy.RemoveDataStoreItem("https://webadaptorhost.domain.com/webadaptorname", "DATABASE",
                          "MSSQL_Conn")
```

### Example 5

```python
import arcpy

arcpy.RemoveDataStoreItem("https://webadaptorhost.domain.com/webadaptorname", "DATABASE",
                          "MSSQL_Conn")
```

---

## RemoveToolbox

## Summary

Removes the specified toolbox, either by specifying its path or referencing its alias. Removes the specified toolbox from the current geoprocessing session. Server toolboxes can also be removed using a semicolon delimiter.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| toolbox | The name of the toolbox, including either path or alias, to be removed from the current geoprocessing session. The name/path or alias should be placed in a double-quoted string. Server toolboxes can be removed using a semicolon delimiter.The name, including path, or alias, of the toolbox to be removed from the current geoprocessing session. Place the name/path, or alias, string inside double quotes. Server toolboxes can also be removed using a semicolon delimiter. Syntax for Internet ArcGIS ServerURL servername;{username};{password}Syntax for Local ArcGIS Servermachinename;servername.Syntax for Internet ArcGIS ServerURL;servername;{username};{password} Syntax for Local ArcGIS Server machinename;servername | String |

## Code Samples

### Example 1

```python
RemoveToolbox (toolbox)
```

### Example 2

```python
import arcpy

# Remove a toolbox from session
arcpy.RemoveToolbox("c:/mytoolboxes/operations.tbx")
```

### Example 3

```python
import arcpy

# Remove a toolbox from session
arcpy.RemoveToolbox("c:/mytoolboxes/operations.tbx")
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

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 3

```python
import arcpy

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\NDVI_Raster.tif")

# Render the raster with a linear stretch and the NDVI color scheme
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'min': 0, 'max': 0.8}, colormap='NDVI')
rendered_raster
```

### Example 4

```python
import arcpy

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 5

```python
import arcpy

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat7.tif")

# Render the Landsat 7 image in false color composite
# Include a linear standard deviation stretch, and a gamma stretch for each band
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'bands': [4,3,2], 'numberOfStandardDeviations': 2, 'gamma': [1,1.7,1.2]})
rendered_raster
```

### Example 6

```python
import arcpy

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 7

```python
import arcpy

# Set input raster
in_Raster = arcpy.Raster(r"C:\Data\Landcover.tif")

# Render the landcover dataset with a custom color map
rendered_raster = arcpy.Render(inRaster, colormap=
	{"values": [11,21,31], "colors": ["#486DA2",  "gray",  "green"],
	"labels":["water", "urban", "forest"]})

rendered_raster
```

### Example 8

```python
import arcpy

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

### Example 9

```python
import arcpy

# Set input multidimensional raster
in_Raster = arcpy.Raster(r"C:\Data\Landsat8_Time_Series.crf", True)

# Render each slice in the imagery time series data with a stretched 
# Normalized Difference Water Index described in a raster function template
rendered_raster = arcpy.Render(inRaster, rendering_rule=
	{'rft': r"C:\Data\NDWI.rft.xml"}, colormap="Red to Green")

rendered_raster
```

---

## Representation Class properties

## Summary

The Describe function returns the following properties for representation classes. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/moad.gdb/Water_Bodies")

# Print RepresentationClass properties for each representation 
#   in the feature class.
#
for child in desc.representations:
    if child.datasetType == "RepresentationClass":
        print(child.name)
        print("\t%-25s %s" % ("Override field name:", child.overrideFieldName))
        print("\t%-25s %s" % ("Shape override required:", child.requireShapeOverride))
        print("\t%-25s %s" % ("RuleID field name:", child.ruleIDFieldName))
```

### Example 2

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/moad.gdb/Water_Bodies")

# Print RepresentationClass properties for each representation 
#   in the feature class.
#
for child in desc.representations:
    if child.datasetType == "RepresentationClass":
        print(child.name)
        print("\t%-25s %s" % ("Override field name:", child.overrideFieldName))
        print("\t%-25s %s" % ("Shape override required:", child.requireShapeOverride))
        print("\t%-25s %s" % ("RuleID field name:", child.ruleIDFieldName))
```

---

## ResetEnvironments

## Summary

Resets all environment settings to their default settings.

## Code Samples

### Example 1

```python
ResetEnvironments ()
```

### Example 2

```python
import arcpy

# Reset environment settings to default settings.
arcpy.ResetEnvironments()
```

### Example 3

```python
import arcpy

# Reset environment settings to default settings.
arcpy.ResetEnvironments()
```

---

## ResetProgressor

## Summary

Resets the progressor to its initial state.

## Code Samples

### Example 1

```python
ResetProgressor ()
```

### Example 2

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

### Example 3

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

---

## Route Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the route solver.

---

## Schematic Dataset properties

## Summary

The Describe function returns the Dataset property group for schematic datasets.

---

## Schematic Diagram properties

## Summary

The Describe function returns the following properties for schematic diagrams. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object for a schematic diagram
#
desc = arcpy.Describe("C:/data/blanding.gdb/CityPower/Feeders/Feeder 0801-Rice Creek")

# Print the diagram class name property
#
print("Diagram Class Name: " + desc.diagramClassName)
```

### Example 2

```python
import arcpy

# Create a Describe object for a schematic diagram
#
desc = arcpy.Describe("C:/data/blanding.gdb/CityPower/Feeders/Feeder 0801-Rice Creek")

# Print the diagram class name property
#
print("Diagram Class Name: " + desc.diagramClassName)
```

---

## Schematic Folder properties

## Summary

The Describe function returns the Dataset property group for schematic folders.

---

## SDC Feature Class properties

## Summary

The Describe function returns the Geodatabase Feature Class, Feature Class, Geodatabase Table, Table, and Dataset property groups for SDC feature classes.

---

## SearchCursor

## Summary

Returns rows of attribute values from a feature class or table.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The feature class or table containing the rows to be searched. | String |
| where_clause | An expression that limits the rows returned in the cursor. For more information about where clauses and SQL statements, see Introduction to query expressions. | String |
| spatial_reference | Coordinates are returned in the spatial reference provided. | SpatialReference |
| fields | A semicolon-delimited string of fields to be included in the cursor. By default, all fields are included. | String |
| sort_fields | The fields to sort the rows in the cursor.Ascending and descending order for each field is denoted by A for ascending and D for descending, using the form "field1 A;field2 D". | String |

## Code Samples

### Example 1

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field = "StreetName"
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    print(row.getValue(field))
```

### Example 2

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field = "StreetName"
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    print(row.getValue(field))
```

### Example 3

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field = "StreetName"
cursor = arcpy.SearchCursor(fc)
row = cursor.next()
while row:
    print(row.getValue(field))
    row = cursor.next()
```

### Example 4

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field = "StreetName"
cursor = arcpy.SearchCursor(fc)
row = cursor.next()
while row:
    print(row.getValue(field))
    row = cursor.next()
```

### Example 5

```python
SearchCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
```

### Example 6

```python
import arcpy

# Create a search cursor for a feature class
rows = arcpy.SearchCursor("c:/data/counties.shp",
                          fields="NAME; STATE_NAME; POP2000",
                          sort_fields="STATE_NAME A; POP2000 D")

# Iterate through the rows in the cursor and print out the
# state name, county and population of each.
for row in rows:
    print("State: {0}, County: {1}, Population: {2}".format(
        row.getValue("STATE_NAME"),
        row.getValue("NAME"),
        row.getValue("POP2000")))
```

### Example 7

```python
import arcpy

# Create a search cursor for a feature class
rows = arcpy.SearchCursor("c:/data/counties.shp",
                          fields="NAME; STATE_NAME; POP2000",
                          sort_fields="STATE_NAME A; POP2000 D")

# Iterate through the rows in the cursor and print out the
# state name, county and population of each.
for row in rows:
    print("State: {0}, County: {1}, Population: {2}".format(
        row.getValue("STATE_NAME"),
        row.getValue("NAME"),
        row.getValue("POP2000")))
```

---

## Service Area Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the service area solver.

---

## SetLogHistory

## Summary

Controls whether information about the execution of geoprocessing tools is written to an external log file.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| log_history | Specifies whether geoprocessing history logging is enabled. True—XML log files will be created in the directory %AppData%\Roaming\Esri\ArcGISPro\ArcToolbox\History. False—XML log files are not created. | Boolean |

## Code Samples

### Example 1

```python
SetLogHistory (log_history)
```

### Example 2

```python
import arcpy
if arcpy.GetLogHistory():
    arcpy.SetLogHistory(False)
```

### Example 3

```python
import arcpy
if arcpy.GetLogHistory():
    arcpy.SetLogHistory(False)
```

---

## SetLogMetadata

## Summary

Controls whether geoprocessing tool input and output datasets' metadata is updated to include the tool name, parameters, when the tool was run, and other information.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| log_metadata | Specifies whether dataset metadata is updated. True—The dataset metadata will contain a Geoprocessing history section with logging of the tools used with that dataset. False—The dataset metadata will not be updated. | Boolean |

## Code Samples

### Example 1

```python
SetLogMetadata (log_metadata)
```

### Example 2

```python
import arcpy
if arcpy.GetLogMetadata():
    arcpy.SetLogMetadata(False)
```

### Example 3

```python
import arcpy
if arcpy.GetLogMetadata():
    arcpy.SetLogMetadata(False)
```

---

## SetMessageLevels

## Summary

Sets additional categories of informative messages to be returned with geoprocessing tool messages.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| levels[levels,...] | Specifies the categories of messages that will be included in geoprocessing tool messages.NORMAL—Only standard tool messages will be included. This is the default.Standard tool messages will be always be included. Use this option to reset back to the default, if other options have been previously set.COMMANDSYNTAX—The tool messages will include a command syntax message. Command syntax is not Python code. It's a space-delimited string of the tool name and the parameter values used to run the tool.DIAGNOSTICS—The tool messages will include diagnostic messages. The messages include details about geoprocessing preprocessing and postprocessing, geoprocessing thread disconnecting and reconnecting, and more. Diagnostic messages are the same as the geoprocessing event messages logged in the ArcGIS Pro Diagnostic Monitor. Esri staff uses diagnostic messages to troubleshoot geoprocessing tool issues.PROJECTIONTRANSFORMATION—The tool messages will include geographic transformation-related messages. These messages are applicable when a tool requires transforming input datasets to a different coordinate system.Multiple options can be set using a list. A single option can be set as a string or a list.(The default value is NORMAL) | String |

## Code Samples

### Example 1

```python
SetMessageLevels (levels)
```

### Example 2

```python
import arcpy

arcpy.SetMessageLevels(['COMMANDSYNTAX'])
```

### Example 3

```python
import arcpy

arcpy.SetMessageLevels(['COMMANDSYNTAX'])
```

---

## SetParameter

## Summary

Sets a specified parameter property by index or parameter name using an object. This function is used to pass objects from a script to a script tool. If you need to pass a string, use the SetParameterAsText function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The specified parameter's index position or parameter name. | Integer |
| value | The object that will set the specified parameter's property. | Object |

## Code Samples

### Example 1

```python
SetParameter (index, value)
```

### Example 2

```python
import arcpy

# Get the input feature class name.
fc = arcpy.GetParameterAsText(0)

# Obtain the spatial reference object and return it to the tool.
spatial_ref = arcpy.Describe(fc).spatialReference
arcpy.SetParameter(1, spatial_ref)
```

### Example 3

```python
import arcpy

# Get the input feature class name.
fc = arcpy.GetParameterAsText(0)

# Obtain the spatial reference object and return it to the tool.
spatial_ref = arcpy.Describe(fc).spatialReference
arcpy.SetParameter(1, spatial_ref)
```

### Example 4

```python
import arcpy

# Get the input feature class name.
fc = arcpy.GetParameterAsText("in_features")

# Obtain the spatial reference object and return it to the tool.
spatial_ref = arcpy.Describe(fc).spatialReference
arcpy.SetParameter("out_spatial_reference", spatial_ref)
```

### Example 5

```python
import arcpy

# Get the input feature class name.
fc = arcpy.GetParameterAsText("in_features")

# Obtain the spatial reference object and return it to the tool.
spatial_ref = arcpy.Describe(fc).spatialReference
arcpy.SetParameter("out_spatial_reference", spatial_ref)
```

---

## SetParameterAsText

## Summary

Sets a specified parameter property by index or parameter name using a string value. This function is used to pass values from a script to a script tool. If you need to pass an object, such as a SpatialReference object, use the SetParameter function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The specified parameter's index position or parameter name. | Integer |
| text | The string value that will set the specified parameter's property. | String |

## Code Samples

### Example 1

```python
SetParameterAsText (index, text)
```

### Example 2

```python
import arcpy

# Get the feature class from the tool.
fc = arcpy.GetParameterAsText(0)

# Determine the shape type of the feature class.
describe = arcpy.Describe(fc)

# Set tool output parameters based on shape type.
if describe.shapeType == "Polygon":
    arcpy.AddMessage("Feature Type is polygon")
    arcpy.SetParameterAsText(1, "true")  # Is polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "false") # Is not point

elif describe.shapeType == "Polyline":
    arcpy.AddMessage("Feature Type is polyline")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "true")  # Is line
    arcpy.SetParameterAsText(3, "false") # Is not point

elif describe.shapeType == "Point":
    arcpy.AddMessage("Feature Type is point")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "true")  # Is point

else:
    arcpy.AddMessage("Unknown feature type")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "false") # Is not point
```

### Example 3

```python
import arcpy

# Get the feature class from the tool.
fc = arcpy.GetParameterAsText(0)

# Determine the shape type of the feature class.
describe = arcpy.Describe(fc)

# Set tool output parameters based on shape type.
if describe.shapeType == "Polygon":
    arcpy.AddMessage("Feature Type is polygon")
    arcpy.SetParameterAsText(1, "true")  # Is polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "false") # Is not point

elif describe.shapeType == "Polyline":
    arcpy.AddMessage("Feature Type is polyline")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "true")  # Is line
    arcpy.SetParameterAsText(3, "false") # Is not point

elif describe.shapeType == "Point":
    arcpy.AddMessage("Feature Type is point")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "true")  # Is point

else:
    arcpy.AddMessage("Unknown feature type")
    arcpy.SetParameterAsText(1, "false") # Is not polygon
    arcpy.SetParameterAsText(2, "false") # Is not line
    arcpy.SetParameterAsText(3, "false") # Is not point
```

### Example 4

```python
import arcpy

# Get the feature class from the tool.
fc = arcpy.GetParameterAsText("in_features")

# Determine the shape type of the feature class.
describe = arcpy.Describe(fc)

# Set tool output parameters based on shape type.
if describe.shapeType == "Polygon":
    arcpy.AddMessage("Feature Type is polygon")
    arcpy.SetParameterAsText("is_polygon", "true")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "false")

elif describe.shapeType == "Polyline":
    arcpy.AddMessage("Feature Type is polyline")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "true")
    arcpy.SetParameterAsText("is_point", "false")

elif describe.shapeType == "Point":
    arcpy.AddMessage("Feature Type is point")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "true")

else:
    arcpy.AddMessage("Unknown feature type")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "false")
```

### Example 5

```python
import arcpy

# Get the feature class from the tool.
fc = arcpy.GetParameterAsText("in_features")

# Determine the shape type of the feature class.
describe = arcpy.Describe(fc)

# Set tool output parameters based on shape type.
if describe.shapeType == "Polygon":
    arcpy.AddMessage("Feature Type is polygon")
    arcpy.SetParameterAsText("is_polygon", "true")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "false")

elif describe.shapeType == "Polyline":
    arcpy.AddMessage("Feature Type is polyline")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "true")
    arcpy.SetParameterAsText("is_point", "false")

elif describe.shapeType == "Point":
    arcpy.AddMessage("Feature Type is point")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "true")

else:
    arcpy.AddMessage("Unknown feature type")
    arcpy.SetParameterAsText("is_polygon", "false")
    arcpy.SetParameterAsText("is_line", "false")
    arcpy.SetParameterAsText("is_point", "false")
```

---

## SetParameterSymbology

## Summary

Sets the symbology properties of the specified output parameter of a script tool by index or parameter name.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The specified output parameter's index position or parameter name. The specified symbology properties are applied to this output of the script tool. | Integer |
| text | Set the specified parameter's symbology properties using the path to a layer file (.lyrx) or a JSON string representation of a CIM or Web Map Specification object. A JSON string representation must be preceded by the appropriate keyword as follows:JSONRENDERER=—A JSON renderer object formatted using either the CIM or Esri Web Map schema.JSONCIMDEF=—A JSON CIM definition object for a layer. JSONCLASSDEF=—A JSON class definition from the Esri Web Map schema. | String |

## Code Samples

### Example 1

```python
SetParameterSymbology (index, text)
```

### Example 2

```python
import arcpy

# Obtain script tool input parameter values.
inras = arcpy.GetParameter(0)
outras = arcpy.GetParameterAsText(1)
outsym = r"C:\Path\To\OutRasterSymbology.lyrx"

# Reclassify raster and apply custom symbology from layer
reclass = arcpy.sa.Reclassify(
  inras,
  "Value",
  arcpy.sa.RemapRange(
    [[0, 100, 0],
    [101, 200, 1],
    [201, 300, 3]]),
  "NODATA")
reclass.save(outras)
arcpy.SetParameterSymbology(1, outsym)
```

### Example 3

```python
import arcpy

# Obtain script tool input parameter values.
inras = arcpy.GetParameter(0)
outras = arcpy.GetParameterAsText(1)
outsym = r"C:\Path\To\OutRasterSymbology.lyrx"

# Reclassify raster and apply custom symbology from layer
reclass = arcpy.sa.Reclassify(
  inras,
  "Value",
  arcpy.sa.RemapRange(
    [[0, 100, 0],
    [101, 200, 1],
    [201, 300, 3]]),
  "NODATA")
reclass.save(outras)
arcpy.SetParameterSymbology(1, outsym)
```

### Example 4

```python
import arcpy

# Obtain script tool input parameter values.
inras = arcpy.GetParameter("in_raster")
outras = arcpy.GetParameterAsText("out_raster")
outsym = r"C:\Path\To\OutRasterSymbology.lyrx"

# Reclassify raster and apply custom symbology from layer
reclass = arcpy.sa.Reclassify(
  inras,
  "Value",
  arcpy.sa.RemapRange(
    [[0, 100, 0],
    [101, 200, 1],
    [201, 300, 3]]),
  "NODATA")
reclass.save(outras)
arcpy.SetParameterSymbology("out_raster", outsym)
```

### Example 5

```python
import arcpy

# Obtain script tool input parameter values.
inras = arcpy.GetParameter("in_raster")
outras = arcpy.GetParameterAsText("out_raster")
outsym = r"C:\Path\To\OutRasterSymbology.lyrx"

# Reclassify raster and apply custom symbology from layer
reclass = arcpy.sa.Reclassify(
  inras,
  "Value",
  arcpy.sa.RemapRange(
    [[0, 100, 0],
    [101, 200, 1],
    [201, 300, 3]]),
  "NODATA")
reclass.save(outras)
arcpy.SetParameterSymbology("out_raster", outsym)
```

### Example 6

```python
import arcpy

# Obtain script tool input parameter values.
infc = arcpy.GetParameter(0)
outfc = arcpy.GetParameter(1)

# Define symbology
outsym = """{
  "type" : "CIMSimpleRenderer",
  "patch" : "Default",
  "symbol" : {
    "type" : "CIMSymbolReference",
    "symbol" : {
      "type" : "CIMLineSymbol",
      "symbolLayers" : [
        {
          "type" : "CIMSolidStroke",
          "effects" : [
            {
              "type" : "CIMGeometricEffectDashes",
              "dashTemplate" : [ 5, 5],
              "lineDashEnding" : "NoConstraint",
              "controlPointEnding" : "NoConstraint"
            }
          ],
          "enable" : true,
          "capStyle" : "Round",
          "joinStyle" : "Round",
          "lineStyle3D" : "Strip",
          "miterLimit" : 10,
          "width" : 1,
          "color" : {
            "type" : "CIMRGBColor",
            "values" : [
              0,
              0,
              0,
              100
            ]
          }
        }
      ]
    }
  }
}"""

# Convert input polygon to line and apply a dashed line symbology
arcpy.management.FeatureToLine(infc, outfc)
arcpy.SetParameterSymbology(1, f"JSONRENDERER={outsym}")
```

### Example 7

```python
import arcpy

# Obtain script tool input parameter values.
infc = arcpy.GetParameter(0)
outfc = arcpy.GetParameter(1)

# Define symbology
outsym = """{
  "type" : "CIMSimpleRenderer",
  "patch" : "Default",
  "symbol" : {
    "type" : "CIMSymbolReference",
    "symbol" : {
      "type" : "CIMLineSymbol",
      "symbolLayers" : [
        {
          "type" : "CIMSolidStroke",
          "effects" : [
            {
              "type" : "CIMGeometricEffectDashes",
              "dashTemplate" : [ 5, 5],
              "lineDashEnding" : "NoConstraint",
              "controlPointEnding" : "NoConstraint"
            }
          ],
          "enable" : true,
          "capStyle" : "Round",
          "joinStyle" : "Round",
          "lineStyle3D" : "Strip",
          "miterLimit" : 10,
          "width" : 1,
          "color" : {
            "type" : "CIMRGBColor",
            "values" : [
              0,
              0,
              0,
              100
            ]
          }
        }
      ]
    }
  }
}"""

# Convert input polygon to line and apply a dashed line symbology
arcpy.management.FeatureToLine(infc, outfc)
arcpy.SetParameterSymbology(1, f"JSONRENDERER={outsym}")
```

### Example 8

```python
import arcpy

# Obtain script tool input parameter values.
infc = arcpy.GetParameter(0)
outfc = arcpy.GetParameter(1)
desc = arcpy.da.Describe(infc)

# Define symbology
sym_poly = """{
  "type": "simple",
  "symbol": {
    "type": "esriSFS",
    "style": "esriSFSSolid",
    "color": [
      10,
      120,
      230,
      255
    ],
    "outline": {
      "type": "esriSLS",
      "style": "esriSLSSolid",
      "color": [
        255,
        255,
        255,
        255
      ],
      "width": 2
    }
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

sym_line = """{
  "type": "simple",
  "symbol": {
    "type": "esriSLS",
    "style": "esriSLSSolid",
    "color": [
      10,
      120,
      230,
      255
    ],
    "width": 2
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

sym_point = """{
  "type": "simple",
  "symbol": {
    "type": "esriSMS",
    "style": "esriSMSCircle",
    "color": [
      10,
      120,
      230,
      255
    ],
    "size": 8,
    "angle": 0,
    "xoffset": 0,
    "yoffset": 0,
    "outline": {
      "color": [
        255,
        255,
        255,
        255
      ],
      "width": 2
    }
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

# Set symbology properties for the output based on shape type of the input
if desc['shapeType'] == 'Polygon':
    # JSON renderer specifying a blue polygon fill with a white outline of width 2
    outsym = f"JSONRENDERER={sym_poly}"

elif desc['shapeType'] == 'Polyline':
    # JSON renderer specifying a blue line of width 2
    outsym = f"JSONRENDERER={sym_line}"

elif desc['shapeType'] == 'Point':
    # JSON renderer specifying a blue point of size 8 with a white outline of width 2
    outsym = f"JSONRENDERER={sym_point}"

else:
    arcpy.AddError('Invalid shape type, must be either "Polygon", "Polyline", or "Point"')

# Run Copy Features
arcpy.management.CopyFeatures(infc, outfc)
arcpy.SetParameterSymbology(1, outsym)
```

### Example 9

```python
import arcpy

# Obtain script tool input parameter values.
infc = arcpy.GetParameter(0)
outfc = arcpy.GetParameter(1)
desc = arcpy.da.Describe(infc)

# Define symbology
sym_poly = """{
  "type": "simple",
  "symbol": {
    "type": "esriSFS",
    "style": "esriSFSSolid",
    "color": [
      10,
      120,
      230,
      255
    ],
    "outline": {
      "type": "esriSLS",
      "style": "esriSLSSolid",
      "color": [
        255,
        255,
        255,
        255
      ],
      "width": 2
    }
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

sym_line = """{
  "type": "simple",
  "symbol": {
    "type": "esriSLS",
    "style": "esriSLSSolid",
    "color": [
      10,
      120,
      230,
      255
    ],
    "width": 2
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

sym_point = """{
  "type": "simple",
  "symbol": {
    "type": "esriSMS",
    "style": "esriSMSCircle",
    "color": [
      10,
      120,
      230,
      255
    ],
    "size": 8,
    "angle": 0,
    "xoffset": 0,
    "yoffset": 0,
    "outline": {
      "color": [
        255,
        255,
        255,
        255
      ],
      "width": 2
    }
  },
  "label": "",
  "description": "",
  "rotationType": "geographic",
  "rotationExpression": ""
}"""

# Set symbology properties for the output based on shape type of the input
if desc['shapeType'] == 'Polygon':
    # JSON renderer specifying a blue polygon fill with a white outline of width 2
    outsym = f"JSONRENDERER={sym_poly}"

elif desc['shapeType'] == 'Polyline':
    # JSON renderer specifying a blue line of width 2
    outsym = f"JSONRENDERER={sym_line}"

elif desc['shapeType'] == 'Point':
    # JSON renderer specifying a blue point of size 8 with a white outline of width 2
    outsym = f"JSONRENDERER={sym_point}"

else:
    arcpy.AddError('Invalid shape type, must be either "Polygon", "Polyline", or "Point"')

# Run Copy Features
arcpy.management.CopyFeatures(infc, outfc)
arcpy.SetParameterSymbology(1, outsym)
```

### Example 10

```python
import arcpy

# Obtain script tool parameter values.
infc = arcpy.GetParameterAsText(0)
outfc = arcpy.GetParameterAsText(1)
dist = arcpy.GetParameter(2)

# Define symbology
outsym = """{
  "type": "classBreaksDef",
  "classificationField": "Shape_Area",
  "classificationMethod": "esriClassifyNaturalBreaks",
  "breakCount": 5,
  "baseSymbol": {
      "type": "esriSFS",
      "style": "esriSFSSolid",
      "color": [
          0,
          0,
          0,
          200
      ],
      "outline": {
          "type": "esriSLS",
          "style": "esriSLSSolid",
          "color": [
              110,
              110,
              110,
              255
          ],
          "width": 0.4
      }
  },
  "colorRamp": {
      "type": "algorithmic",
      "fromColor": [
          245,
          245,
          0,
          200
      ],
      "toColor": [
          245,
          0,
          0,
          200
      ],
      "algorithm": "esriHSVAlgorithm"
  }
}"""

# Run aggregate points and symbolize the output polygon by area using natural breaks.
arcpy.cartography.AggregatePoints(infc, outfc, dist)
arcpy.SetParameterSymbology(1, f"JSONCLASSDEF={outsym}")
```

### Example 11

```python
import arcpy

# Obtain script tool parameter values.
infc = arcpy.GetParameterAsText(0)
outfc = arcpy.GetParameterAsText(1)
dist = arcpy.GetParameter(2)

# Define symbology
outsym = """{
  "type": "classBreaksDef",
  "classificationField": "Shape_Area",
  "classificationMethod": "esriClassifyNaturalBreaks",
  "breakCount": 5,
  "baseSymbol": {
      "type": "esriSFS",
      "style": "esriSFSSolid",
      "color": [
          0,
          0,
          0,
          200
      ],
      "outline": {
          "type": "esriSLS",
          "style": "esriSLSSolid",
          "color": [
              110,
              110,
              110,
              255
          ],
          "width": 0.4
      }
  },
  "colorRamp": {
      "type": "algorithmic",
      "fromColor": [
          245,
          245,
          0,
          200
      ],
      "toColor": [
          245,
          0,
          0,
          200
      ],
      "algorithm": "esriHSVAlgorithm"
  }
}"""

# Run aggregate points and symbolize the output polygon by area using natural breaks.
arcpy.cartography.AggregatePoints(infc, outfc, dist)
arcpy.SetParameterSymbology(1, f"JSONCLASSDEF={outsym}")
```

---

## SetProgressor

## Summary

Establishes a progressor object to support progress information to be displayed in the Geoprocessing pane. The appearance of the progressor can be controlled by choosing either the default progressor or the step progressor.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| type | Specifies the progressor type. default—The progressor moves continuously from side to side in a repeating pattern.step—The progressor shows the percentage complete.(The default value is default) | String |
| message | The progressor label. The default is no label. | String |
| min_range | The minimum value for the progressor. The default is 0.(The default value is 0) | Integer |
| max_range | The maximum value for the progressor. The default is 100.(The default value is 100) | Integer |
| step_value | The progressor step interval for updating the progress bar.(The default value is 1) | Integer |

## Code Samples

### Example 1

```python
SetProgressor (type, {message}, {min_range}, {max_range}, {step_value})
```

### Example 2

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

### Example 3

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

---

## SetProgressorLabel

## Summary

Updates the progressor label in the Geoprocessing pane.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| label | The label to be set on the progressor. | String |

## Code Samples

### Example 1

```python
SetProgressorLabel (label)
```

### Example 2

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

### Example 3

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

---

## SetProgressorPosition

## Summary

Updates the progressor status bar in the Geoprocessing pane.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| position | Sets the position of the progressor status bar. | Integer |

## Code Samples

### Example 1

```python
SetProgressorPosition ({position})
```

### Example 2

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

### Example 3

```python
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = "c:/data"

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()
```

---

## SetSeverityLevel

## Summary

Controls how geoprocessing tools throw exceptions.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| severity_level | Specifies the severity level 0—A tool will not throw an exception, even if the tool produces an error or warning.1—If a tool produces a warning or an error, it will throw an exception.2—If a tool produces an error, it will throw an exception. This is the default. | Integer |

## Code Samples

### Example 1

```python
SetSeverityLevel (severity_level)
```

### Example 2

```python
import arcpy

fc1 = 'c:/resources/resources.gdb/boundary'
fc2 = 'c:/resources/resources.gdb/boundary2'

# Set the severity level to 1 (tool warnings will throw an exception)
arcpy.SetSeverityLevel(1)
print("Severity is set to : {0}".format(arcpy.GetSeverityLevel()))

try:
    # FeatureCompare returns warning messages when a miscompare is
    # found.  This normally would not cause an exception, however, by
    # setting the severity level to 1, all tool warnings will also
    # return an exception.
    arcpy.management.FeatureCompare(fc1, fc2, "OBJECTID")
except arcpy.ExecuteWarning:
    print(arcpy.GetMessages(1))
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy

fc1 = 'c:/resources/resources.gdb/boundary'
fc2 = 'c:/resources/resources.gdb/boundary2'

# Set the severity level to 1 (tool warnings will throw an exception)
arcpy.SetSeverityLevel(1)
print("Severity is set to : {0}".format(arcpy.GetSeverityLevel()))

try:
    # FeatureCompare returns warning messages when a miscompare is
    # found.  This normally would not cause an exception, however, by
    # setting the severity level to 1, all tool warnings will also
    # return an exception.
    arcpy.management.FeatureCompare(fc1, fc2, "OBJECTID")
except arcpy.ExecuteWarning:
    print(arcpy.GetMessages(1))
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## Shapefile Feature Class properties

## Summary

The Describe function returns the Feature Class, Table, and Dataset property groups for shapefiles.

---

## Shields Description

## Summary

The Network Dataset Shields Description object provides additional shields information which is used to enhance the direction information when the streets have multiple street names.

## Code Samples

### Example 1

```python
# Name: NDSShieldsDescriptionProperties_ex01.py
# Description: Print additional information about directions shields for each
#              edge source

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Get the direction information specific to edge source
    sDir = source.sourceDirections
    #Get the shields for each source
    shields = sDir.shields
    if shields:
        print("----Shields description")
        print("Description count: " , shields.descriptionCount)
        sDesc = shields.description
        if sDesc:
            for i in range(0, shields.descriptionCount):
                shieldType = getattr(sDesc,"shieldType" + str(i))
                sheildDesc = getattr(sDesc, "shieldDescription" + str(i))
                print("Type: " , shieldType)
                print("Description: " , sheildDesc)
    else:
        print("(No shield information)")
```

### Example 2

```python
# Name: NDSShieldsDescriptionProperties_ex01.py
# Description: Print additional information about directions shields for each
#              edge source

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Get the direction information specific to edge source
    sDir = source.sourceDirections
    #Get the shields for each source
    shields = sDir.shields
    if shields:
        print("----Shields description")
        print("Description count: " , shields.descriptionCount)
        sDesc = shields.description
        if sDesc:
            for i in range(0, shields.descriptionCount):
                shieldType = getattr(sDesc,"shieldType" + str(i))
                sheildDesc = getattr(sDesc, "shieldDescription" + str(i))
                print("Type: " , shieldType)
                print("Description: " , sheildDesc)
    else:
        print("(No shield information)")
```

---

## Shields

## Summary

The Network Dataset Shields object provides information about the directions shields settings for a given edge source.

## Code Samples

### Example 1

```python
# Name: NDSShieldsProperties_ex01.py
# Description: Print information about directions shields for each edge source

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Get the direction information specific to edge source
    sDir = source.sourceDirections
    #Get the shields for each source
    shields = sDir.shields
    if shields:
        print("Shield type field: " , shields.typeFieldName)
        print("Number field:" , shields.numberFieldName)
        print("Combined field: " , shields.combinedFieldName)
        print("Description count: " , shields.descriptionCount)
    else:
        print("(No shield information)")
```

### Example 2

```python
# Name: NDSShieldsProperties_ex01.py
# Description: Print information about directions shields for each edge source

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Get the direction information specific to edge source
    sDir = source.sourceDirections
    #Get the shields for each source
    shields = sDir.shields
    if shields:
        print("Shield type field: " , shields.typeFieldName)
        print("Number field:" , shields.numberFieldName)
        print("Combined field: " , shields.combinedFieldName)
        print("Description count: " , shields.descriptionCount)
    else:
        print("(No shield information)")
```

---

## SignInToPortal

## Summary

Allows you to sign in to a portal.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| portal_url | The URL of the portal to sign in to. | String |
| username | The username of the user signing in to the portal. If the portal uses IWA, leave this parameter empty. You can only sign in as the current Windows user. | String |
| password | The password of the user signing in to the portal. If the portal uses PKI authentication, use the password to the PKCS12 certificate file. If the portal uses IWA, leave this parameter empty. | String |
| cert_file | The path to the certificate file. If the portal uses PKI authentication, use the path to the PKCS12 formatted certificate file (.pfx or .p12) or the PEM formatted certificate file (.pem). | String |
| key_file | The path to the key file. If the portal uses PKI authentication, use the path to the PEM formatted key file (.pem). | String |
| token | The token that will be used to authenticate with the portal.An ArcGIS portal token can be created using any of the following:The GetSigninToken function in an authenticated sessionThe generateToken REST service on Portal for ArcGIS The SignInToPortal functionWhen using a token to authenticate, the token, token_referer, and token_expiry values must be specified. | String |
| token_referer | The referer that will be used to generate the token (if applicable). | String |
| token_expiry | The expiration time stamp for the token. This is a value measured in the number of seconds since epoch.Note:The API that produces the token may return the expiry value in seconds or milliseconds. | Integer |

## Code Samples

### Example 1

```python
SignInToPortal (portal_url, {username}, {password}, {cert_file}, {key_file}, {token}, {token_referer}, {token_expiry})
```

### Example 2

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     'username', 'password')
```

### Example 3

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     'username', 'password')
```

### Example 4

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     cert_file="C:\\path\\to\\mycert.pfx", 
                     password="cert.password")
```

### Example 5

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     cert_file="C:\\path\\to\\mycert.pfx", 
                     password="cert.password")
```

### Example 6

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     cert_file="C:\\path\\to\\mycert.pem", 
                     key_file="C:\\path\\to\\mykey.pem")
```

### Example 7

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname", 
                     cert_file="C:\\path\\to\\mycert.pem", 
                     key_file="C:\\path\\to\\mykey.pem")
```

### Example 8

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname")
```

### Example 9

```python
import arcpy

arcpy.SignInToPortal("https://webadaptorhost.domain.com/webadaptorname")
```

### Example 10

```python
import arcpy
import requests

# assemble arguments into a dictionary
# for additional help on the generateToken REST service, see your portal documentation
portal_url = "https://example.com/portal/"
gen_token_url = f"{portal_url}sharing/rest/generateToken"
params = {"f": "json",               # Response format
		  "username": "username",    # Your ArcGIS Portal username
		  "password": "password",    # Your ArcGIS Portal password
		  "referer": gen_token_url,  # URL of the referring application (usually your portal)
		  "expiration": 60           # Token expiration time in minutes (default: 60)
 		}

# get a token using python's requests module
resp = requests.post(gen_token_url, data=params)

# check response. If failed, show response.text
assert resp.status_code == 200, resp.text

# now use token with SignInToPortal
token = resp.json()['token']
token_expiry = int(resp.json()['expires']/1000)  # convert to seconds since generateToken returns milliseconds
resp = arcpy.SignInToPortal(portal_url, token=token, token_referer=portal_url, token_expiry=token_expiry)
```

### Example 11

```python
import arcpy
import requests

# assemble arguments into a dictionary
# for additional help on the generateToken REST service, see your portal documentation
portal_url = "https://example.com/portal/"
gen_token_url = f"{portal_url}sharing/rest/generateToken"
params = {"f": "json",               # Response format
		  "username": "username",    # Your ArcGIS Portal username
		  "password": "password",    # Your ArcGIS Portal password
		  "referer": gen_token_url,  # URL of the referring application (usually your portal)
		  "expiration": 60           # Token expiration time in minutes (default: 60)
 		}

# get a token using python's requests module
resp = requests.post(gen_token_url, data=params)

# check response. If failed, show response.text
assert resp.status_code == 200, resp.text

# now use token with SignInToPortal
token = resp.json()['token']
token_expiry = int(resp.json()['expires']/1000)  # convert to seconds since generateToken returns milliseconds
resp = arcpy.SignInToPortal(portal_url, token=token, token_referer=portal_url, token_expiry=token_expiry)
```

### Example 12

```python
import arcpy
import keyring

portal = "https://example.com/portal/"
username = "user"
password = keyring.get_password(portal, username)

arcpy.SignInToPortal(portal, username, password)
```

### Example 13

```python
import arcpy
import keyring

portal = "https://example.com/portal/"
username = "user"
password = keyring.get_password(portal, username)

arcpy.SignInToPortal(portal, username, password)
```

---

## Street Name Fields

## Summary

The Street Name Fields object provides information about the fields containing the street names used in reporting driving directions.

## Code Samples

### Example 1

```python
# Name: NDSStreetNameFieldsProperties_ex01.py
# Description: Print information about field names used to generate street names
#              in directions

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Print the direction information specific to edge source
    sDir = source.sourceDirections
    # Get the street name fields for each source
    sStreetFields = sDir.streetNameFields
    for sStreetField in sStreetFields:
        print("Prefix direction field: " , sStreetField.prefixDirectionFieldName)
        print("Prefix type field: " , sStreetField.prefixTypeFieldName)
        print("Street name field: " , sStreetField.streetNameFieldName)
        print("Suffix direction field: " , sStreetField.suffixDirectionFieldName)
        print("Suffix type field: " , sStreetField.suffixTypeFieldName)
        print("Priority: " , sStreetField.priority)
        print("Full name field: " , sStreetField.fullNameFieldName)
        print("Highway direction field: ",sStreetField.highwayDirectionFieldName)
        print("Language field: " , sStreetField.languageFieldName)
```

### Example 2

```python
# Name: NDSStreetNameFieldsProperties_ex01.py
# Description: Print information about field names used to generate street names
#              in directions

import arcpy
import sys

# Set the workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

# Create Describe object for the network dataset
desc = arcpy.Describe("Streets_ND")

#If the directions are not set for the network dataset, exit
if not desc.supportsDirections:
    print("No direction information")
    sys.exit()

print("Source Direction Information ----")

# Get all the edge sources
sources = desc.edgeSources

if not sources:
    print("No edge sources")
    sys.exit()
#Loop through all the edge sources
for source in sources:
    print("--------------------")
    print("Name: " , source.name)
    print("Source ID: " , source.sourceID)
    #Print the direction information specific to edge source
    sDir = source.sourceDirections
    # Get the street name fields for each source
    sStreetFields = sDir.streetNameFields
    for sStreetField in sStreetFields:
        print("Prefix direction field: " , sStreetField.prefixDirectionFieldName)
        print("Prefix type field: " , sStreetField.prefixTypeFieldName)
        print("Street name field: " , sStreetField.streetNameFieldName)
        print("Suffix direction field: " , sStreetField.suffixDirectionFieldName)
        print("Suffix type field: " , sStreetField.suffixTypeFieldName)
        print("Priority: " , sStreetField.priority)
        print("Full name field: " , sStreetField.fullNameFieldName)
        print("Highway direction field: ",sStreetField.highwayDirectionFieldName)
        print("Language field: " , sStreetField.languageFieldName)
```

---

## System Junction Object Source properties

## Summary

The following properties are supported by the systemJunctionObjectSource object in a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# System Junction Object Source properties
sjosources = d.systemJunctionObjectSource
print("*** - System Junction Object Source properties - ***")
print(f"ID: {sjosources.sourceID}")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# System Junction Object Source properties
sjosources = d.systemJunctionObjectSource
print("*** - System Junction Object Source properties - ***")
print(f"ID: {sjosources.sourceID}")
```

---

## System Junction Source properties

## Summary

The following properties are supported by the systemJunctionSource object in a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print(f"Name: {sjsources.name}")
print(f"ID: {sjsources.sourceID}")
print(f"Type: {sjsources.sourceType} \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print(f"Name: {sjsources.name}")
print(f"ID: {sjsources.sourceID}")
print(f"Type: {sjsources.sourceType} \n")
```

---

## System Junction Source

## Summary

Provides information about system junction sources in a network dataset.

## Code Samples

### Example 1

```python
# Name: NDSSystemJunctionSourceProperties_ex01.py
# Description: Print the information about the system junction sources
#              defined for the network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- System junction source")

#SDC network datasets do not have system junction source.
networktype = desc.networkType
if networktype.lower() == "sdc":
    print("%*s" % (justify, "(No system junction source)"))
    sys.exit(0)

#Get the system junction source for the network dataset.
sjSource = desc.systemJunctionSource
if not sjSource:
    print("%*s" % (justify, "(No system junction sources)"))
    sys.exit(0)

print("%*s: %s" % (justify, "Source Name" , sjSource.name))
print("%*s: %s" % (justify, "Source ID" , str(sjSource.sourceID)))
print("%*s: %s" % (justify, "Source Type", sjSource.sourceType))
print("%*s: %s" % (justify, "Element Type", sjSource.elementType))
print(" %*s: %s" % (justify, "Elevation Field",sjSource.elevationFieldName))
print(" ")
```

### Example 2

```python
# Name: NDSSystemJunctionSourceProperties_ex01.py
# Description: Print the information about the system junction sources
#              defined for the network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- System junction source")

#SDC network datasets do not have system junction source.
networktype = desc.networkType
if networktype.lower() == "sdc":
    print("%*s" % (justify, "(No system junction source)"))
    sys.exit(0)

#Get the system junction source for the network dataset.
sjSource = desc.systemJunctionSource
if not sjSource:
    print("%*s" % (justify, "(No system junction sources)"))
    sys.exit(0)

print("%*s: %s" % (justify, "Source Name" , sjSource.name))
print("%*s: %s" % (justify, "Source ID" , str(sjSource.sourceID)))
print("%*s: %s" % (justify, "Source Type", sjSource.sourceType))
print("%*s: %s" % (justify, "Element Type", sjSource.elementType))
print(" %*s: %s" % (justify, "Elevation Field",sjSource.elevationFieldName))
print(" ")
```

---

## Table properties

## Summary

The Describe function returns the following properties for tables. The Dataset property group is also supported. The Editor Tracking property group is supported if editor tracking has been enabled for this table.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the table.
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/munich")

# If the table has an OID, print the OID field name
#
if desc.hasOID:
    print("OIDFieldName: " + desc.OIDFieldName)

# Print the names and types of all the fields in the table
#
for field in desc.fields:
    print("%-22s %s %s" % (field.name, ":", field.type))
    #print field.name + " = " + field.type
```

### Example 2

```python
import arcpy

# Create a Describe object from the table.
#
desc = arcpy.Describe("C:/data/chesapeake.gdb/munich")

# If the table has an OID, print the OID field name
#
if desc.hasOID:
    print("OIDFieldName: " + desc.OIDFieldName)

# Print the names and types of all the fields in the table
#
for field in desc.fields:
    print("%-22s %s %s" % (field.name, ":", field.type))
    #print field.name + " = " + field.type
```

---

## Table View properties

## Summary

The Describe function returns the following properties for table views. The Table property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a table view from a feature class
#
arcpy.MakeTableView_management(
        "C:/data/wellingham.gdb/water/water_pipes", 
        "pipes_view")

# Create a Describe object from the table view
#
desc = arcpy.Describe("pipes_view")

# Print some table view properties
#
print("Table View Name: " + desc.nameString)
print("Where Clause:    " + desc.whereClause)
print("Table Name:      " + desc.name)
```

### Example 2

```python
import arcpy

# Create a table view from a feature class
#
arcpy.MakeTableView_management(
        "C:/data/wellingham.gdb/water/water_pipes", 
        "pipes_view")

# Create a Describe object from the table view
#
desc = arcpy.Describe("pipes_view")

# Print some table view properties
#
print("Table View Name: " + desc.nameString)
print("Where Clause:    " + desc.whereClause)
print("Table Name:      " + desc.name)
```

---

## Terminal Configuration properties

## Summary

The properties below are returned by the terminalConfigurations object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

---

## Terminal Path properties

## Summary

The properties below are returned by the terminalPaths object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

---

## Terminal properties

## Summary

The properties below are returned by the terminals object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

---

## TestSchemaLock

## Summary

Tests if a schema lock can be acquired for a feature class, table, or feature dataset. Tools that alter schema will require a schema lock to be placed on the input data. The Add Field tool is an example of such a tool. If the tool requires a schema lock and is unable to acquire one when the tool is run, an appropriate error message is returned. Scripts that use such tools should test if a schema lock can be acquired on the input data. The TestSchemaLock function will not actually apply a schema lock on the input data, but will return a Boolean.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The input data to be tested if a schema lock can be applied. | String |

## Code Samples

### Example 1

```python
TestSchemaLock (dataset)
```

### Example 2

```python
import arcpy

data = arcpy.GetParameterAsText(0)

# Test if a schema lock can be applied, and if so, add a new field
#
if arcpy.TestSchemaLock(data):
    arcpy.AddField_management(data, "Flag", "LONG")
else:
    print("Unable to acquire the necessary schema lock to add the new field")
```

### Example 3

```python
import arcpy

data = arcpy.GetParameterAsText(0)

# Test if a schema lock can be applied, and if so, add a new field
#
if arcpy.TestSchemaLock(data):
    arcpy.AddField_management(data, "Flag", "LONG")
else:
    print("Unable to acquire the necessary schema lock to add the new field")
```

---

## Text File properties

## Summary

If the text file contains tabular data, the Describe function returns the Table and Dataset property groups for text files; otherwise, refer to the File property group.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from the text file.
#
desc = arcpy.Describe("C:/data/evac_table.txt")

# Print some table properties
#
print("HasOID: " + str(desc.hasOID))

print("\nField names:")
for field in desc.fields:
    print("   " + field.name)
```

### Example 2

```python
import arcpy

# Create a Describe object from the text file.
#
desc = arcpy.Describe("C:/data/evac_table.txt")

# Print some table properties
#
print("HasOID: " + str(desc.hasOID))

print("\nField names:")
for field in desc.fields:
    print("   " + field.name)
```

---

## Tier Group properties

## Summary

The properties below are returned by the tierGroups object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:

    # Tier Group properties
    for tierGroup in dom.tierGroups:
        print(f"*** - Tier Group properties - ***")
        print(f"Tier Group Name: {tierGroup.name}")
        print(f"Tier Group Creation Time: {tierGroup.creationTime}")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:

    # Tier Group properties
    for tierGroup in dom.tierGroups:
        print(f"*** - Tier Group properties - ***")
        print(f"Tier Group Name: {tierGroup.name}")
        print(f"Tier Group Creation Time: {tierGroup.creationTime}")
```

---

## Tier properties

## Summary

The properties below are returned by the tiers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUN_TierProperties.py
Description: This script reports the tier properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Domain Network Creation Time: {dom.creationTime}")
    print(f"Domain Network Release Number: {dom.releaseNumber}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Domain Network is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network Tier Definition: {dom.tierDefinition}")
    print(f"Domain Network Subnetwork Controller Type: {dom.subnetworkControllerType} \n")
    print(f"Domain Network Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Domain Network Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")    
    
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
        print(f"Rank: {tier.rank}")
        print(f"Tier topology type: {tier.tierTopology}")
        print(f"Tier group name: {tier.tierGroupName} \n")
        print(f"Subnetwork field name: {tier.subnetworkFieldName}")
        print(f"Supports disjoint subnetwork: {tier.supportDisjointSubnetwork}")
        print(f"Update Subnetwork Edit Mode For Default Version: {tier.updateSubnetworkEditModeForDefaultVersion}")
        print(f"Update Subnetwork Edit Mode For Named Version: {tier.updateSubnetworkEditModeForNamedVersion}")
        print(f"Update Subnetwork On Structures: {tier.updateSubnetworkOnStructures}")
        print(f"Update Subnetwork On Containers: {tier.updateSubnetworkOnContainers}")
        print(f"Diagram templates: {tier.diagramTemplates} \n")
        print (f"Manage IsDirty: {tier.ManageSubnetwork.isDirty} \n")

        # Subnetwork Controller Properties
        for sc in tier.validSubnetworkControllers:
            print(" -- Subnetwork Controllers Properties -- ")
            print(f"Asset Group Code: {sc.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in sc.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")

        # Valid Device Properties        
        for vd in tier.validDevices:
            print(" -- Valid Devices Properties -- ")
            print(f"Asset Group Code: {vd.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")

        # Valid Lines Properties        
        for vl in tier.validLines:
            print(" -- Valid Lines Properties -- ")
            print(f"Asset Group Code: {vl.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vl.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")

        # Valid Junctions Properties        
        for vj in tier.validJunctions:
            print(" -- Valid Junctions Properties -- ")
            print(f"Asset Group Code: {vj.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vj.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")		
				
        # Valid Junction Objects Properties        
        for vjo in tier.validJunctionObjects:
            print(" -- Valid JunctionObjects Properties -- ")
            print(f"Asset Group Code: {vjo.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vjo.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")
                
        # Valid Junction Objects Subnetwork Controller Properties
        for vjosc in tier.validJunctionObjectSubnetworkControllers:
            print(" -- Valid Junction Object Subnetwork Controllers Properties -- ")
            print(f"Asset Group Code: {vjosc.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vjosc.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")                

        # Valid Edge Objects Properties        
        for veo in tier.validEdgeObjects:
            print(" -- Valid EdgeObjects Properties -- ")
            print(f"Asset Group Code: {veo.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in veo.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")		
                
        # Aggregated Lines for SubnetLine Properties        
        for al in tier.aggregatedLinesForSubnetLine:
            print(" -- Aggregated Lines for SubnetLine Properties -- ")
            print(f"Asset Group Code: {al.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in al.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")	
                
        # Update Subnetwork Trace Configuration Properties
        print(" -- Update Subnetwork Trace Properties -- ")        
        ust = tier.updateSubnetworkTraceConfiguration
        print(f"Include Containers: {ust.includeContainers}")
        print(f"Include Content: {ust.includeContent}")
        print(f"Include Structures: {ust.includeStructures}")
        print(f"Include Barriers: {ust.includeBarriers}")
        print(f"Validate Consistency: {ust.validateConsistency}")
        print(f"Validate Locatability: {ust.validateLocatability}")
        print(f"Include Isolated: {ust.includeIsolated}")
        print(f"Ignore Barriers at Starting Points: {ust.ignoreBarriersAtStartingPoints}")
        print(f"Include Up To First Spatial Container: {ust.includeUpToFirstSpatialContainer}")
        print(f"Allow Indeterminate Flow: {ust.allowIndeterminateFlow}")
        print(f"Domain Network Name: {ust.domainNetworkName}")
        print(f"Tier Name: {ust.tierName}")
        print(f"Target Tier Name: {ust.targetTierName}")
        print(f"Subnetwork Name: {ust.subnetworkName}")
        print(f"Diagram Template Name: {ust.diagramTemplateName}")
        print(f"Shortest Path Network Attribute Name: {ust.shortestPathNetworkAttributeName}")
        print(f"Filter Bitset Network Attribute Name: {ust.filterBitsetNetworkAttributeName}")
        print(f"Traversability Scope: {ust.traversabilityScope}")
        print(f"Filter Scope: {ust.filterScope} \n")

        # Condition Barrier Properties
        print(" - Condition Barrier Properties - ")
        for cb in ust.conditionBarriers:
            try:
                print(f"Name: {cb.name} ")
                print(f"Type: {cb.type} ")
                print(f"Operator: {cb.operator} ")
                print(f"Value: {cb.value} ")
                print(f"CombineUsingOr: {cb.combineUsingOr}")
                print(f"Is Specific Value: {cb.isSpecificValue} \n")
            except:
                print("Skipped condition barrier properties. \n")
        
        # Function Barrier Properties
        print(" - Function Barrier Properties - ")
        for fb in ust.functionBarriers:
            try:
                print(f"Name: {fb.networkAttributeName}")
                print(f"Type: {fb.functionType}")
                print(f"Operator: {fb.networkAttributeOperator}")
                print(f"Value: {fb.value} ")
                print(f"Use Local Values: {fb.useLocalValues} \n")
            except:
                print("Skipped function barrier properties. \n")
            
        # Filter Barrier Properties
        print(" - Filter Barrier Properties - ")
        for filb in ust.filterBarriers:
            try:
                print(f"Name: {filb.name}")
                print(f"Type: {filb.type}")
                print(f"Operator: {filb.operator}")
                print(f"Value: {filb.value}")
                print(f"CombineUsingOr: {filb.combineUsingOr}")
                print(f"Is Specific Value: {filb.isSpecificValue} \n")
            except:
                print("Skipped filter barrier properties. \n")
        
        # Filter Function Barrier Properties
        print(" - Filter Function Barrier Properties - ")
        for ffb in ust.filterFunctionBarriers:
            try:
                print(f"Name: {ffb.networkAttributeName}")
                print(f"Type: {ffb.functionType}")
                print(f"Operator: {ffb.networkAttributeOperator}")
                print(f"Value: {ffb.value}")
                print(f"Use Local Values: {ffb.useLocalValues} \n")
            except:
                print("Skipped filter function properties. \n")

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
            
        # Output Filter Properties
        print(" - Output Filter Properties - ")
        for ofp in ust.outputFilters:
            # Try to get these properties if the exist, else, print the empty list
            try:
                for of in ofp:
                    print(f"Network Source ID: {of.networkSourceID}")
                    print(f"Asset Group Code: {of.assetGroupCode}")
                    print(f"Asset Type Code: {of.assetTypeCode} \n")
            except:
                print("Skipped output filter properties. \n")

        # Output Condition Properties
        print(" - Output Condition Properties - ")
        for oc in ust.outputConditions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Name: {oc.name}")
                print(f"Type: {oc.type}")
                print(f"Operator: {oc.operator}")
                print(f"Value: {oc.value}")
                print(f"CombineUsingOr: {oc.combineUsingOr}")
                print(f"Is Specific Value: {oc.isSpecificValue} \n")
            except:
                print("Skipped output condition properties. \n")
            
        # Propagators Properties
        print(" - Propagator Properties - ")
        for p in ust.propagators:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Network Attribute Name: {p.networkAttributeName}")
                print(f"Trace Propagator Function Type: {p.tracePropagatorFunctionType}")
                print(f"Network Attribute Filter Operator: {p.networkAttributeOperator}")
                print(f"Network Attribute Value: {p.value}")
                print(f"Propagated Attribute Name: {p.propagatedAttributeName}")
                print(f"Substitution Attribute Name: {p.substitutionAttributeName}")
            except:
                print("Skipped propagator properties. \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUN_TierProperties.py
Description: This script reports the tier properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Domain Network Creation Time: {dom.creationTime}")
    print(f"Domain Network Release Number: {dom.releaseNumber}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Domain Network is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network Tier Definition: {dom.tierDefinition}")
    print(f"Domain Network Subnetwork Controller Type: {dom.subnetworkControllerType} \n")
    print(f"Domain Network Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Domain Network Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")    
    
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
        print(f"Rank: {tier.rank}")
        print(f"Tier topology type: {tier.tierTopology}")
        print(f"Tier group name: {tier.tierGroupName} \n")
        print(f"Subnetwork field name: {tier.subnetworkFieldName}")
        print(f"Supports disjoint subnetwork: {tier.supportDisjointSubnetwork}")
        print(f"Update Subnetwork Edit Mode For Default Version: {tier.updateSubnetworkEditModeForDefaultVersion}")
        print(f"Update Subnetwork Edit Mode For Named Version: {tier.updateSubnetworkEditModeForNamedVersion}")
        print(f"Update Subnetwork On Structures: {tier.updateSubnetworkOnStructures}")
        print(f"Update Subnetwork On Containers: {tier.updateSubnetworkOnContainers}")
        print(f"Diagram templates: {tier.diagramTemplates} \n")
        print (f"Manage IsDirty: {tier.ManageSubnetwork.isDirty} \n")

        # Subnetwork Controller Properties
        for sc in tier.validSubnetworkControllers:
            print(" -- Subnetwork Controllers Properties -- ")
            print(f"Asset Group Code: {sc.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in sc.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")

        # Valid Device Properties        
        for vd in tier.validDevices:
            print(" -- Valid Devices Properties -- ")
            print(f"Asset Group Code: {vd.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")

        # Valid Lines Properties        
        for vl in tier.validLines:
            print(" -- Valid Lines Properties -- ")
            print(f"Asset Group Code: {vl.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vl.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")

        # Valid Junctions Properties        
        for vj in tier.validJunctions:
            print(" -- Valid Junctions Properties -- ")
            print(f"Asset Group Code: {vj.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vj.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")		
				
        # Valid Junction Objects Properties        
        for vjo in tier.validJunctionObjects:
            print(" -- Valid JunctionObjects Properties -- ")
            print(f"Asset Group Code: {vjo.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vjo.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")
                
        # Valid Junction Objects Subnetwork Controller Properties
        for vjosc in tier.validJunctionObjectSubnetworkControllers:
            print(" -- Valid Junction Object Subnetwork Controllers Properties -- ")
            print(f"Asset Group Code: {vjosc.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in vjosc.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")                

        # Valid Edge Objects Properties        
        for veo in tier.validEdgeObjects:
            print(" -- Valid EdgeObjects Properties -- ")
            print(f"Asset Group Code: {veo.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in veo.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode}")		
                
        # Aggregated Lines for SubnetLine Properties        
        for al in tier.aggregatedLinesForSubnetLine:
            print(" -- Aggregated Lines for SubnetLine Properties -- ")
            print(f"Asset Group Code: {al.assetGroupCode} \n")
            print(" - Asset Type Properties - ")
            for at in al.assetTypes:
                print(f"Asset Type Code: {at.assetTypeCode} \n")	
                
        # Update Subnetwork Trace Configuration Properties
        print(" -- Update Subnetwork Trace Properties -- ")        
        ust = tier.updateSubnetworkTraceConfiguration
        print(f"Include Containers: {ust.includeContainers}")
        print(f"Include Content: {ust.includeContent}")
        print(f"Include Structures: {ust.includeStructures}")
        print(f"Include Barriers: {ust.includeBarriers}")
        print(f"Validate Consistency: {ust.validateConsistency}")
        print(f"Validate Locatability: {ust.validateLocatability}")
        print(f"Include Isolated: {ust.includeIsolated}")
        print(f"Ignore Barriers at Starting Points: {ust.ignoreBarriersAtStartingPoints}")
        print(f"Include Up To First Spatial Container: {ust.includeUpToFirstSpatialContainer}")
        print(f"Allow Indeterminate Flow: {ust.allowIndeterminateFlow}")
        print(f"Domain Network Name: {ust.domainNetworkName}")
        print(f"Tier Name: {ust.tierName}")
        print(f"Target Tier Name: {ust.targetTierName}")
        print(f"Subnetwork Name: {ust.subnetworkName}")
        print(f"Diagram Template Name: {ust.diagramTemplateName}")
        print(f"Shortest Path Network Attribute Name: {ust.shortestPathNetworkAttributeName}")
        print(f"Filter Bitset Network Attribute Name: {ust.filterBitsetNetworkAttributeName}")
        print(f"Traversability Scope: {ust.traversabilityScope}")
        print(f"Filter Scope: {ust.filterScope} \n")

        # Condition Barrier Properties
        print(" - Condition Barrier Properties - ")
        for cb in ust.conditionBarriers:
            try:
                print(f"Name: {cb.name} ")
                print(f"Type: {cb.type} ")
                print(f"Operator: {cb.operator} ")
                print(f"Value: {cb.value} ")
                print(f"CombineUsingOr: {cb.combineUsingOr}")
                print(f"Is Specific Value: {cb.isSpecificValue} \n")
            except:
                print("Skipped condition barrier properties. \n")
        
        # Function Barrier Properties
        print(" - Function Barrier Properties - ")
        for fb in ust.functionBarriers:
            try:
                print(f"Name: {fb.networkAttributeName}")
                print(f"Type: {fb.functionType}")
                print(f"Operator: {fb.networkAttributeOperator}")
                print(f"Value: {fb.value} ")
                print(f"Use Local Values: {fb.useLocalValues} \n")
            except:
                print("Skipped function barrier properties. \n")
            
        # Filter Barrier Properties
        print(" - Filter Barrier Properties - ")
        for filb in ust.filterBarriers:
            try:
                print(f"Name: {filb.name}")
                print(f"Type: {filb.type}")
                print(f"Operator: {filb.operator}")
                print(f"Value: {filb.value}")
                print(f"CombineUsingOr: {filb.combineUsingOr}")
                print(f"Is Specific Value: {filb.isSpecificValue} \n")
            except:
                print("Skipped filter barrier properties. \n")
        
        # Filter Function Barrier Properties
        print(" - Filter Function Barrier Properties - ")
        for ffb in ust.filterFunctionBarriers:
            try:
                print(f"Name: {ffb.networkAttributeName}")
                print(f"Type: {ffb.functionType}")
                print(f"Operator: {ffb.networkAttributeOperator}")
                print(f"Value: {ffb.value}")
                print(f"Use Local Values: {ffb.useLocalValues} \n")
            except:
                print("Skipped filter function properties. \n")

        # Functions Properties
        print(" - Functions Properties - ")
        for f in ust.functions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Function Type: {f.functionType}")
                print(f"Function Network Attribute Name: {f.networkAttributeName}")
                print(f"Function Summary Attribute Name: {f.summaryAttributeName} \n")
                # Function Conditions
                print(" - Function Conditions - ")
                for fc in f.conditions:
                    print(f"Name: {fc.name}")
                    print(f"Type: {fc.type}")
                    print(f"Operator: {fc.operator}")
                    print(f"Value: {fc.value}")
                    print(f"CombineUsingOr: {fc.combineUsingOr}")
                    print(f"Is Specific Value: {fc.isSpecificValue} \n")
            except:
                print("Skipped functions properties. \n")

        # Nearest Neighbor Properties
        print(" - Nearest Neighbor Properties - ")
        nn = ust.nearestNeighbor
        # Try to get these properties if the exist, else, print the empty list
        try:
            print(f"Count: {nn.count}")
            print(f"Cost Network Attribute Name: {nn.costNetworkAttributeName}")
            print(f"Nearest Categories: {nn.nearestCategories} \n")
            print(f" - Nearest Asset Properties - ")
            for nsta in nn.nearestAssets:
                try:
                    print(f"Network Source ID: {nsta.networkSourceID}")
                    print(f"Asset Group Code: {nsta.assetGroupCode}")
                    print(f"Asset Type Code: {nsta.assetTypeCode} \n")
                except:
                    print("Skipped nearest assets properties. \n")
        except:
            print("Skipped nearest neighbor properties. \n")
            
        # Output Filter Properties
        print(" - Output Filter Properties - ")
        for ofp in ust.outputFilters:
            # Try to get these properties if the exist, else, print the empty list
            try:
                for of in ofp:
                    print(f"Network Source ID: {of.networkSourceID}")
                    print(f"Asset Group Code: {of.assetGroupCode}")
                    print(f"Asset Type Code: {of.assetTypeCode} \n")
            except:
                print("Skipped output filter properties. \n")

        # Output Condition Properties
        print(" - Output Condition Properties - ")
        for oc in ust.outputConditions:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Name: {oc.name}")
                print(f"Type: {oc.type}")
                print(f"Operator: {oc.operator}")
                print(f"Value: {oc.value}")
                print(f"CombineUsingOr: {oc.combineUsingOr}")
                print(f"Is Specific Value: {oc.isSpecificValue} \n")
            except:
                print("Skipped output condition properties. \n")
            
        # Propagators Properties
        print(" - Propagator Properties - ")
        for p in ust.propagators:
            # Try to get these properties if the exist, else, print the empty list
            try:
                print(f"Network Attribute Name: {p.networkAttributeName}")
                print(f"Trace Propagator Function Type: {p.tracePropagatorFunctionType}")
                print(f"Network Attribute Filter Operator: {p.networkAttributeOperator}")
                print(f"Network Attribute Value: {p.value}")
                print(f"Propagated Attribute Name: {p.propagatedAttributeName}")
                print(f"Substitution Attribute Name: {p.substitutionAttributeName}")
            except:
                print("Skipped propagator properties. \n")
```

---

## TIN properties

## Summary

The Describe function returns the following properties for TINs. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/antelope_island")

# Print TIN properties
print("%-21s %s" % ("HasEdgeTagValues:", desc.hasEdgeTagValues))
print("%-21s %s" % ("HasNodeTagValues:", desc.hasNodeTagValues))
print("%-21s %s" % ("HasTriangleTagValues:", desc.hasTriangleTagValues))
print("%-21s %s" % ("IsDelaunay:", desc.isDelaunay))
print("%-21s %s" % ("ZFactor:", desc.ZFactor))

# Print the field names in the TIN
print("\nFields in the TIN:")
for field in desc.fields:
    print("\t%s" % field.name)
```

### Example 2

```python
import arcpy

# Create a Describe object
#
desc = arcpy.Describe("C:/data/antelope_island")

# Print TIN properties
print("%-21s %s" % ("HasEdgeTagValues:", desc.hasEdgeTagValues))
print("%-21s %s" % ("HasNodeTagValues:", desc.hasNodeTagValues))
print("%-21s %s" % ("HasTriangleTagValues:", desc.hasTriangleTagValues))
print("%-21s %s" % ("IsDelaunay:", desc.isDelaunay))
print("%-21s %s" % ("ZFactor:", desc.ZFactor))

# Print the field names in the TIN
print("\nFields in the TIN:")
for field in desc.fields:
    print("\t%s" % field.name)
```

---

## Toolbox properties

## Summary

The Describe function returns the Dataset property group for toolboxes.

---

## Topology properties

## Summary

The Describe function returns the following properties for topologies. The Dataset property group is also supported.

## Code Samples

### Example 1

```python
import arcpy

# Create a Describe object from a topology.
#
desc = arcpy.Describe("C:/data/moad.gdb/East/ParkZones_topology")

# Print some topology properties
#
print("%-27s %s" % ("ClusterTolerance:", desc.clusterTolerance))
print("%-27s %s" % ("ZClusterTolerance:", desc.ZClusterTolerance))
print("%-27s %s" % ("FeatureClassNames:", desc.featureClassNames))
print("%-27s %s" % ("MaximumGeneratedErrorCount:", desc.maximumGeneratedErrorCount))
```

### Example 2

```python
import arcpy

# Create a Describe object from a topology.
#
desc = arcpy.Describe("C:/data/moad.gdb/East/ParkZones_topology")

# Print some topology properties
#
print("%-27s %s" % ("ClusterTolerance:", desc.clusterTolerance))
print("%-27s %s" % ("ZClusterTolerance:", desc.ZClusterTolerance))
print("%-27s %s" % ("FeatureClassNames:", desc.featureClassNames))
print("%-27s %s" % ("MaximumGeneratedErrorCount:", desc.maximumGeneratedErrorCount))
```

---

## Assignments properties

## Summary

The properties below are returned by the assignments object when using Describe on a trace network.

---

## Association Source properties

## Summary

The following properties are supported by the associationSource object in a trace network.

---

## Connectivity Policies properties

## Summary

The following property is returned by the connectivityPolicies object in a trace network.

---

## Evaluator properties

## Summary

The properties below are returned by the evaluator object when using Describe on a trace network.

---

## Network Attribute properties

## Summary

The following properties are supported by the networkAttributes object in a trace network.

---

## Trace Network properties

## Summary

The Describe function returns the following properties for a trace network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeTraceNetworkProperties.py
Description: This script reports the properties of a trace network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Trace Network
TN = (r"C:\MyProject\MyNetworkData.gdb\FDS\HydroNetwork")
d = arcpy.Describe(TN)

# Top level TN properties
print("Creation Time: {0}".format(d.creationTime))
print("Pro Version: {0}".format(d.proVersion))
print("Global ID: {0}".format(d.globalId))
print("Schema generation: {0}".format(d.schemaGeneration))
print("Minimal dirty area size: {0}".format(d.minimalDirtyAreaSize))
print("Create Dirty Area For Any Attribute Update: {0}\n".format(d.createDirtyAreaForAnyAttributeUpdate))

# Association source properties
asources = d.associationSource
print("*** - Assocation Sources properties - ***")
print("Name: {0}".format(asources.name))
print("ID: {0}".format(asources.sourceID))
print("Type: {0} \n".format(asources.sourceType))

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print("Name: {0}".format(sjsources.name))
print("ID: {0}".format(sjsources.sourceID))
print("Type: {0} \n".format(sjsources.sourceType))

# Source properties
sources = d.sources
for s in sources:
    print("*** - Sources properties - ***")
    print("Name: {0}".format(s.name))
    print("ID: {0}".format(s.sourceID))
    print("Source Type: {0} \n".format(s.sourceType))
    print("Element Type: {0} \n".format(s.elementType))
    cp = s.connectivityPolicies
    print("Connectivity Policy: {0} \n".format(cp.classConnectivity))

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print("ID: {0}".format(na.Id))
    print("Name: {0}".format(na.name))
    print("Data Type: {0}".format(na.dataType))
    print("Usage Type: {0}".format(na.usageType))
    print("isEmbedded: {0}".format(na.isEmbedded))
    print("isApportionable: {0}".format(na.isApportionable))
    print("bitPosition: {0}".format(na.bitPosition))
    print("bitSize: {0}".format(na.bitSize))
    print("Junction Weight ID: {0}".format(na.junctionWeightId))
    print("Edge Weight ID: {0} \n".format(na.edgeWeightId))

    # For each attribute assignment in the attribute assignments object:
    try:
        tnas = na.assignments
        for tna in tnas:
            print(" -- Attribute Assignment Properties -- ")
            print("Trace Network Assignment Attribute ID: {0}".format(tna.attributeId))
            print("Trace Network Assignment Attribute Source Name: {0} \n".format(tna.networkSourceName))
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = tna.evaluator
            print("Field Evaluator Type: {0}".format(fe.evaluatorType))
            print("Field Evaluator Name: {0} \n".format(fe.fieldName))
    except:
        print("{0} does not have any attribute assignments \n".format(na.name))
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeTraceNetworkProperties.py
Description: This script reports the properties of a trace network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Trace Network
TN = (r"C:\MyProject\MyNetworkData.gdb\FDS\HydroNetwork")
d = arcpy.Describe(TN)

# Top level TN properties
print("Creation Time: {0}".format(d.creationTime))
print("Pro Version: {0}".format(d.proVersion))
print("Global ID: {0}".format(d.globalId))
print("Schema generation: {0}".format(d.schemaGeneration))
print("Minimal dirty area size: {0}".format(d.minimalDirtyAreaSize))
print("Create Dirty Area For Any Attribute Update: {0}\n".format(d.createDirtyAreaForAnyAttributeUpdate))

# Association source properties
asources = d.associationSource
print("*** - Assocation Sources properties - ***")
print("Name: {0}".format(asources.name))
print("ID: {0}".format(asources.sourceID))
print("Type: {0} \n".format(asources.sourceType))

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print("Name: {0}".format(sjsources.name))
print("ID: {0}".format(sjsources.sourceID))
print("Type: {0} \n".format(sjsources.sourceType))

# Source properties
sources = d.sources
for s in sources:
    print("*** - Sources properties - ***")
    print("Name: {0}".format(s.name))
    print("ID: {0}".format(s.sourceID))
    print("Source Type: {0} \n".format(s.sourceType))
    print("Element Type: {0} \n".format(s.elementType))
    cp = s.connectivityPolicies
    print("Connectivity Policy: {0} \n".format(cp.classConnectivity))

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print("ID: {0}".format(na.Id))
    print("Name: {0}".format(na.name))
    print("Data Type: {0}".format(na.dataType))
    print("Usage Type: {0}".format(na.usageType))
    print("isEmbedded: {0}".format(na.isEmbedded))
    print("isApportionable: {0}".format(na.isApportionable))
    print("bitPosition: {0}".format(na.bitPosition))
    print("bitSize: {0}".format(na.bitSize))
    print("Junction Weight ID: {0}".format(na.junctionWeightId))
    print("Edge Weight ID: {0} \n".format(na.edgeWeightId))

    # For each attribute assignment in the attribute assignments object:
    try:
        tnas = na.assignments
        for tna in tnas:
            print(" -- Attribute Assignment Properties -- ")
            print("Trace Network Assignment Attribute ID: {0}".format(tna.attributeId))
            print("Trace Network Assignment Attribute Source Name: {0} \n".format(tna.networkSourceName))
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = tna.evaluator
            print("Field Evaluator Type: {0}".format(fe.evaluatorType))
            print("Field Evaluator Name: {0} \n".format(fe.fieldName))
    except:
        print("{0} does not have any attribute assignments \n".format(na.name))
```

---

## Source properties

## Summary

The following properties are supported by the sources object in a trace network.

---

## System Junction Source properties

## Summary

The following properties are supported by the systemJunctionSource object in a trace network.

---

## Turn Source

## Summary

Provides information about turn sources in a network dataset.

## Code Samples

### Example 1

```python
# Name: NDSTurnSourceProperties_ex01.py
# Description: Print the information about the turn sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- Turn sources")

#Get all the turn sources for the network dataset
turns = desc.turnSources

#Not all network datasets can have turn sources.
if not turns:
    print("%*s" % (justify, "(No turn sources)"))
    sys.exit(0)

for turnSource in turns:
    print("%*s: %s" % (justify, "Source Name" , turnSource.name))
    print("%*s: %s" % (justify, "Source ID" , str(turnSource.sourceID)))
    print("%*s: %s" % (justify, "Source Type", turnSource.sourceType))
    print("%*s: %s" % (justify, "Element Type", turnSource.elementType))
    print(" ")
```

### Example 2

```python
# Name: NDSTurnSourceProperties_ex01.py
# Description: Print the information about the turn sources defined for the
#              network dataset

import arcpy
import sys

# Set workspace
arcpy.env.workspace = "C:/Data/SanFrancisco.gdb/Transportation"

#Create a Describe object from the network dataset
desc = arcpy.Describe("Streets_ND")

justify = 35
print("------- Turn sources")

#Get all the turn sources for the network dataset
turns = desc.turnSources

#Not all network datasets can have turn sources.
if not turns:
    print("%*s" % (justify, "(No turn sources)"))
    sys.exit(0)

for turnSource in turns:
    print("%*s: %s" % (justify, "Source Name" , turnSource.name))
    print("%*s: %s" % (justify, "Source ID" , str(turnSource.sourceID)))
    print("%*s: %s" % (justify, "Source Type", turnSource.sourceType))
    print("%*s: %s" % (justify, "Element Type", turnSource.elementType))
    print(" ")
```

---

## Update Subnetwork Trace Configuration properties

## Summary

The properties below are returned by the updateSubnetworkTraceConfiguration object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties
        print(" -- Update Subnetwork Trace Properties -- ")        
        ust = tier.updateSubnetworkTraceConfiguration
        print(f"Include Containers: {ust.includeContainers}")
        print(f"Include Content: {ust.includeContent}")
        print(f"Include Structures: {ust.includeStructures}")
        print(f"Include Barriers: {ust.includeBarriers}")
        print(f"Validate Consistency: {ust.validateConsistency}")
        print(f"Validate Locatability: {ust.validateLocatability}")
        print(f"Include Isolated: {ust.includeIsolated}")
        print(f"Ignore Barriers at Starting Points: {ust.ignoreBarriersAtStartingPoints}")
        print(f"Include Up To First Spatial Container: {ust.includeUpToFirstSpatialContainer}")
        print(f"Allow Indeterminate Flow: {ust.allowIndeterminateFlow}")
        print(f"Domain Network Name: {ust.domainNetworkName}")
        print(f"Tier Name: {ust.tierName}")
        print(f"Target Tier Name: {ust.targetTierName}")
        print(f"Subnetwork Name: {ust.subnetworkName}")
        print(f"Diagram Template Name: {ust.diagramTemplateName}")
        print(f"Shortest Path Network Attribute Name: {ust.shortestPathNetworkAttributeName}")
        print(f"Filter Bitset Network Attribute Name: {ust.filterBitsetNetworkAttributeName}")
        print(f"Traversability Scope: {ust.traversabilityScope}")
        print(f"Filter Scope: {ust.filterScope} \n")
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    print(f"Domain Network Name: {dom.domainNetworkName}")
    
    # For each tier in the domain network
    for tier in dom.tiers:
        print(f"Tier Name: {tier.name}")
                
        # Update Subnetwork Trace Configuration Properties
        print(" -- Update Subnetwork Trace Properties -- ")        
        ust = tier.updateSubnetworkTraceConfiguration
        print(f"Include Containers: {ust.includeContainers}")
        print(f"Include Content: {ust.includeContent}")
        print(f"Include Structures: {ust.includeStructures}")
        print(f"Include Barriers: {ust.includeBarriers}")
        print(f"Validate Consistency: {ust.validateConsistency}")
        print(f"Validate Locatability: {ust.validateLocatability}")
        print(f"Include Isolated: {ust.includeIsolated}")
        print(f"Ignore Barriers at Starting Points: {ust.ignoreBarriersAtStartingPoints}")
        print(f"Include Up To First Spatial Container: {ust.includeUpToFirstSpatialContainer}")
        print(f"Allow Indeterminate Flow: {ust.allowIndeterminateFlow}")
        print(f"Domain Network Name: {ust.domainNetworkName}")
        print(f"Tier Name: {ust.tierName}")
        print(f"Target Tier Name: {ust.targetTierName}")
        print(f"Subnetwork Name: {ust.subnetworkName}")
        print(f"Diagram Template Name: {ust.diagramTemplateName}")
        print(f"Shortest Path Network Attribute Name: {ust.shortestPathNetworkAttributeName}")
        print(f"Filter Bitset Network Attribute Name: {ust.filterBitsetNetworkAttributeName}")
        print(f"Traversability Scope: {ust.traversabilityScope}")
        print(f"Filter Scope: {ust.filterScope} \n")
```

---

## UpdateCursor

## Summary

Updates or deletes rows of attribute values from a feature class or table.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| dataset | The feature class or table containing the rows to be updated or deleted. | String |
| where_clause | An expression that limits the rows returned in the cursor. For more information about where clauses and SQL statements, see Introduction to query expressions. | String |
| spatial_reference | Coordinates are specified in the spatial_reference value provided and converted on the fly to the coordinate system of the dataset. | SpatialReference |
| fields | A semicolon-delimited string of fields to be included in the cursor. By default, all fields are included. | String |
| sort_fields | The fields used to sort the rows in the cursor.Ascending and descending order for each field is denoted by A for ascending and D for descending, using the form "field1 A;field2 B". | String |

## Code Samples

### Example 1

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field1 = "field1"
field2 = "field2"

cursor = arcpy.UpdateCursor(fc)
for row in cursor:
    # field2 will be equal to field1 multiplied by 3.0
    row.setValue(field2, row.getValue(field1) * 3.0)
    cursor.updateRow(row)
```

### Example 2

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field1 = "field1"
field2 = "field2"

cursor = arcpy.UpdateCursor(fc)
for row in cursor:
    # field2 will be equal to field1 multiplied by 3.0
    row.setValue(field2, row.getValue(field1) * 3.0)
    cursor.updateRow(row)
```

### Example 3

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field1 = "field1"
field2 = "field2"

cursor = arcpy.UpdateCursor(fc)
row = cursor.next()
while row:
    # field2 will be equal to field1 multiplied by 3.0
    row.setValue(field2, row.getValue(field1) * 3.0)
    cursor.updateRow(row)
    row = cursor.next()
```

### Example 4

```python
import arcpy

fc = "c:/data/base.gdb/roads"
field1 = "field1"
field2 = "field2"

cursor = arcpy.UpdateCursor(fc)
row = cursor.next()
while row:
    # field2 will be equal to field1 multiplied by 3.0
    row.setValue(field2, row.getValue(field1) * 3.0)
    cursor.updateRow(row)
    row = cursor.next()
```

### Example 5

```python
UpdateCursor (dataset, {where_clause}, {spatial_reference}, {fields}, {sort_fields})
```

### Example 6

```python
import arcpy

# Create an update cursor for a feature class
rows = arcpy.UpdateCursor("c:/data/base.gdb/roads")

# Update the field used in buffer so the distance is based on the
# road type. Road type is either 1, 2, 3, or 4. Distance is in meters.
for row in rows:
    # Fields from the table can be dynamically accessed from the
    # row object. Here fields named BUFFER_DISTANCE and ROAD_TYPE
    # are used
    row.setValue("BUFFER_DISTANCE", row.getValue("ROAD_TYPE") * 100)
    rows.updateRow(row)

# Delete cursor and row objects to remove locks on the data.
del row
del rows
```

### Example 7

```python
import arcpy

# Create an update cursor for a feature class
rows = arcpy.UpdateCursor("c:/data/base.gdb/roads")

# Update the field used in buffer so the distance is based on the
# road type. Road type is either 1, 2, 3, or 4. Distance is in meters.
for row in rows:
    # Fields from the table can be dynamically accessed from the
    # row object. Here fields named BUFFER_DISTANCE and ROAD_TYPE
    # are used
    row.setValue("BUFFER_DISTANCE", row.getValue("ROAD_TYPE") * 100)
    rows.updateRow(row)

# Delete cursor and row objects to remove locks on the data.
del row
del rows
```

---

## Usage

## Summary

Returns the syntax for the specified tool or function.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| tool_name | The tool name to display the syntax. | String |

## Code Samples

### Example 1

```python
import arcpy
help(arcpy.Buffer_analysis)
```

### Example 2

```python
import arcpy
help(arcpy.Buffer_analysis)
```

### Example 3

```python
import arcpy
arcpy.Buffer_analysis?
```

### Example 4

```python
import arcpy
arcpy.Buffer_analysis?
```

### Example 5

```python
Usage (tool_name)
```

### Example 6

```python
import arcpy

print(arcpy.Usage("Buffer_analysis"))
print(arcpy.Usage("MakeFeatureLayer_management"))
```

### Example 7

```python
import arcpy

print(arcpy.Usage("Buffer_analysis"))
print(arcpy.Usage("MakeFeatureLayer_management"))
```

---

## Utility Network properties

## Summary

The Describe function returns the following properties for a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\pro21.USER1.Naperville\\pro21.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Top level UN properties
print(f"Creation Time: {d.creationTime}")
print(f"Pro Version: {d.proVersion}")
print(f"Global ID: {d.globalId}")
print(f"Properties: {d.properties}")
print(f"Schema generation: {d.schemaGeneration}")
print(f"Minimal dirty area size: {d.minimalDirtyAreaSize}")
print(f"Create Dirty Area For Any Attribute Update: {d.createDirtyAreaForAnyAttributeUpdate} \n")

# Association source properties
asources = d.associationSource
print("*** - Association Sources properties - ***")
print(f"Name: {asources.name}")
print(f"ID: {asources.sourceID}")
print(f"Type: {asources.sourceType} \n")

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print(f"Name: {sjsources.name}")
print(f"ID: {sjsources.sourceID}")
print(f"Type: {sjsources.sourceType} \n")

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Creation Time: {dom.creationTime}")
    print(f"Release Number: {dom.releaseNumber}")
    print(f"Is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Tier Definition: {dom.tierDefinition}")
    print(f"Subnetwork Controller Type: {dom.subnetworkControllerType} \n")

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print(f"ID: {na.Id}")
    print(f"Name: {na.name}")
    print(f"Data Type: {na.dataType}")
    print(f"Usage Type: {na.usageType}")
    print(f"isEmbedded: {na.isEmbedded}")
    print(f"isApportionable: {na.isApportionable}")
    print(f"isOverridable: {na.isOverridable}")
    print(f"Domain name: {na.domainName}")
    print(f"bitPosition: {na.bitPosition}")
    print(f"bitSize: {na.bitSize}")
    print(f"Junction Weight ID: {na.junctionWeightId}")
    print(f"Edge Weight ID: {na.edgeWeightId} \n")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")
    except:
        print(f"{na.name} does not have any attribute assignments \n")

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configurations object:
    try:
        for lc in tc.validConfigurations:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configurations \n")

# Categories properties
categories = d.categories
for cat in categories:
    print("*** - Categories properties - ***")
    print(f"Category creation time: {cat.creationTime}")
    print(f"Category Name: {cat.name} \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\pro21.USER1.Naperville\\pro21.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Top level UN properties
print(f"Creation Time: {d.creationTime}")
print(f"Pro Version: {d.proVersion}")
print(f"Global ID: {d.globalId}")
print(f"Properties: {d.properties}")
print(f"Schema generation: {d.schemaGeneration}")
print(f"Minimal dirty area size: {d.minimalDirtyAreaSize}")
print(f"Create Dirty Area For Any Attribute Update: {d.createDirtyAreaForAnyAttributeUpdate} \n")

# Association source properties
asources = d.associationSource
print("*** - Association Sources properties - ***")
print(f"Name: {asources.name}")
print(f"ID: {asources.sourceID}")
print(f"Type: {asources.sourceType} \n")

# System junction source properties
sjsources = d.systemJunctionSource
print("*** - System Junction Source properties - ***")
print(f"Name: {sjsources.name}")
print(f"ID: {sjsources.sourceID}")
print(f"Type: {sjsources.sourceType} \n")

# Domain Network properties
domnets = d.domainNetworks
for dom in domnets:
    print("*** - Domain Network properties - ***")
    print(f"Creation Time: {dom.creationTime}")
    print(f"Release Number: {dom.releaseNumber}")
    print(f"Is Structure Network: {dom.isStructureNetwork}")
    print(f"Domain Network ID: {dom.domainNetworkId}")
    print(f"Domain Network Name: {dom.domainNetworkName}")
    print(f"Domain Network Alias Name: {dom.domainNetworkAliasName}")
    print(f"Subnetwork Table Name: {dom.subnetworkTableName}")
    print(f"Subnetwork Label Field Name: {dom.subnetworkLabelFieldName}")
    print(f"Tier Definition: {dom.tierDefinition}")
    print(f"Subnetwork Controller Type: {dom.subnetworkControllerType} \n")

# Network Attribute properties
netattrs = d.networkAttributes
for na in netattrs:
    print("*** - Network Attribute properties - ***")
    print(f"ID: {na.Id}")
    print(f"Name: {na.name}")
    print(f"Data Type: {na.dataType}")
    print(f"Usage Type: {na.usageType}")
    print(f"isEmbedded: {na.isEmbedded}")
    print(f"isApportionable: {na.isApportionable}")
    print(f"isOverridable: {na.isOverridable}")
    print(f"Domain name: {na.domainName}")
    print(f"bitPosition: {na.bitPosition}")
    print(f"bitSize: {na.bitSize}")
    print(f"Junction Weight ID: {na.junctionWeightId}")
    print(f"Edge Weight ID: {na.edgeWeightId} \n")

    # For each attribute assignment in the attribute assignments object:
    try:
        unas = na.assignments
        for una in unas:
            print(" -- Attribute Assignment Properties -- ")
            print(f"Utility Network Assignment Attribute ID: {una.networkAttributeId}")
            print(f"Utility Network Assignment Attribute Source Name: {una.networkSourceName} \n")
            # For each field evaluator in the attribute evaluator object:
            print(" - Field Evaluator Properties - ")
            fe = una.evaluator
            print(f"Field Evaluator Type: {fe.evaluatorType}")
            print(f"Field Evaluator Name: {fe.fieldName} \n")
    except:
        print(f"{na.name} does not have any attribute assignments \n")

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configurations object:
    try:
        for lc in tc.validConfigurations:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configurations \n")

# Categories properties
categories = d.categories
for cat in categories:
    print("*** - Categories properties - ***")
    print(f"Category creation time: {cat.creationTime}")
    print(f"Category Name: {cat.name} \n")
```

---

## Valid Configuration Paths properties

## Summary

The properties below are returned by the validConfigurationPaths object when using Describe on a utility network.

## Code Samples

### Example 1

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

### Example 2

```python
'''****************************************************************************
Name:        DescribeUtilityNetworkProperties.py
Description: This script reports the properties of a utility network
Created by:  Esri
****************************************************************************'''

# Import required modules
import arcpy

# Describe function on a Utility Network
UN = "C:\\MyProject\\databaseConn.sde\\mygdb.USER1.Naperville\\mygdb.USER1.ElectricNetwork"
d = arcpy.Describe(UN)

# Terminal Configuration properties
termconfigs = d.terminalConfigurations
for tc in termconfigs:
    print("*** - Terminal Configuration Properties - ***")
    print(f"ID: {tc.terminalConfigurationId}")
    print(f"Name: {tc.terminalConfigurationName}")
    print(f"Traversability Model: {tc.traversabilityModel}")
    print(f"Default Configuration: {tc.defaultConfiguration} \n")

    # For each terminal in the terminals object:
    for t in tc.terminals:
        print(" -- Terminal Properties -- ")
        print(f"Terminal ID: {t.terminalId}")
        print(f"Terminal Name: {t.terminalName}")
        print(f"Terminal Is Upstream: {t.isUpstreamTerminal} \n")

    # For each configuration in the valid configuration paths object:
    try:
        for lc in tc.validConfigurationPaths:
            print(" - Configuration Properties - ")
            print(f"Configuration Id: {lc.id}")
            print(f"Configuration Name: {lc.name}")
            print(f"Description: {lc.description} \n")
            try:
                for tp in lc.terminalPaths:
                    print(f"From terminal id: {tp.fromTerminalId}")
                    print(f"To terminal id: {tp.toTerminalId}")
            except:
                print(f"{lc.name} does not have any terminal paths \n")
    except:
        print(f"{t.terminalName} does not have any valid configuration paths \n")
```

---

## Valid Device properties

## Summary

The properties below are returned by the validDevices object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid device Properties        
        for vd in tier.validDevices:
            print(" -- Valid Devices Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid device Properties        
        for vd in tier.validDevices:
            print(" -- Valid Devices Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Edge Objects properties

## Summary

The properties below are returned by the validEdgeObjects object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid edge object Properties        
        for veo in tier.validEdgeObjects:
            print(" -- Valid Edge Object Properties -- ")
            print("Asset Group Code: {0} \n".format(veo.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in veo.assetTypes:

                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid edge object Properties        
        for veo in tier.validEdgeObjects:
            print(" -- Valid Edge Object Properties -- ")
            print("Asset Group Code: {0} \n".format(veo.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in veo.assetTypes:

                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Junction Object Subnetwork Controller properties

## Summary

The properties below are returned by the validJunctionObjectSubnetworkControllers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid junction object subnetwork controller Properties        
        for vjosc in tier.validJunctionObjectSubnetworkControllers:
            print(" -- Valid Junction Object Subnetwork Controller Properties -- ")
            print("Asset Group Code: {0} \n".format(vjosc.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vjosc.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid junction object subnetwork controller Properties        
        for vjosc in tier.validJunctionObjectSubnetworkControllers:
            print(" -- Valid Junction Object Subnetwork Controller Properties -- ")
            print("Asset Group Code: {0} \n".format(vjosc.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vjosc.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Junction Objects properties

## Summary

The properties below are returned by the validJunctionObjects object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the junction object Properties        
        for vjo in tier.validJunctionObjects:
            print(" -- Valid Junction Object Properties -- ")
            print("Asset Group Code: {0} \n".format(vjo.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vjo.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the junction object Properties        
        for vjo in tier.validJunctionObjects:
            print(" -- Valid Junction Object Properties -- ")
            print("Asset Group Code: {0} \n".format(vjo.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vjo.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Junctions properties

## Summary

The properties below are returned by the validJunctions object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid junction properties        
        for vj in tier.validJunctions:
            print(" -- Valid Junction Properties -- ")
            print("Asset Group Code: {0} \n".format(vj.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vj.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid junction properties        
        for vj in tier.validJunctions:
            print(" -- Valid Junction Properties -- ")
            print("Asset Group Code: {0} \n".format(vj.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vj.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Line properties

## Summary

The properties below are returned by the validLines object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid line Properties        
        for vd in tier.validLines:
            print(" -- Valid Lines Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid line Properties        
        for vd in tier.validLines:
            print(" -- Valid Lines Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## Valid Subnetwork Controller properties

## Summary

The properties below are returned by the validSubnetworkControllers object when using Describe on a utility network.

## Code Samples

### Example 1

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid subnetwork controller Properties        
        for vd in tier.validSubnetworkControllers:
            print(" -- Valid Subnetwork Controller Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

### Example 2

```python
# Import required modules
import arcpy

# Describe functions on a Utility Network
UN = "C:\\Projects\\MyProject\\unowner.sde\\Naperville.UNOWNER.Naperville\\Naperville.UNOWNER.Naperville" 
d = arcpy.Describe(UN)

# Domain Network properties
domnets = d.domainNetworks

# For each domain network in the utility network
for dom in domnets:
    # For each tier in the domain network
    for tier in dom.tiers:
        # Print the valid subnetwork controller Properties        
        for vd in tier.validSubnetworkControllers:
            print(" -- Valid Subnetwork Controller Properties -- ")
            print("Asset Group Code: {0} \n".format(vd.assetGroupCode))
            print(" - Asset Type Properties - ")
            for at in vd.assetTypes:
                print("Asset Type Code: {0}".format(at.assetTypeCode))
```

---

## ValidateDataStoreItem

## Summary

Validates whether a folder or database has been successfully registered with an ArcGIS Server site.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| connection_file | For a hosting server, provide the server URL or use the MY_HOSTED_SERVICES keyword. For a stand-alone server, use an ArcGIS Server connection file (.ags) representing the server with which you want to register the data. | String |
| datastore_type | The type of data being validated.DATABASE—The data resides in an enterprise database.FOLDER—The data is file-based. | String |
| connection_name | The name by which the folder or database being validated is registered with the ArcGIS Server site. | String |

## Code Samples

### Example 1

```python
ValidateDataStoreItem (connection_file, datastore_type, connection_name)
```

### Example 2

```python
import arcpy

conn = "GIS Servers/MyConnection.ags"
for store_type in ["FOLDER", "DATABASE"]:
    print("Validating data store items of type {}".format(store_type))
    for i in arcpy.ListDataStoreItems(conn, store_type):
        validity = arcpy.ValidateDataStoreItem(conn, store_type, i[0])
        print("The data item '{}' is {}".format(i[0], validity))
```

### Example 3

```python
import arcpy

conn = "GIS Servers/MyConnection.ags"
for store_type in ["FOLDER", "DATABASE"]:
    print("Validating data store items of type {}".format(store_type))
    for i in arcpy.ListDataStoreItems(conn, store_type):
        validity = arcpy.ValidateDataStoreItem(conn, store_type, i[0])
        print("The data item '{}' is {}".format(i[0], validity))
```

---

## ValidateFieldName

## Summary

Returns a valid field name for a database based on a field name and a path to a database. All invalid characters in the input field name are replaced with an underscore. The field name restrictions depend on the type of database.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The field name that will be validated. | String |
| workspace | The workspace that will be used to validate the field name. The workspace can be a file system, a file, or an enterprise geodatabase.If the workspace is not specified, the Current Workspace environment will be used. If the Current Workspace environment is not set, a folder workspace will be used. | String |

## Code Samples

### Example 1

```python
ValidateFieldName (name, {workspace})
```

### Example 2

```python
import arcpy
import os

class ShapeError(Exception):
    pass


try:
    # Get the input feature class and make sure it contains polygons.
    in_fc = arcpy.GetParameterAsText(0)
    if arcpy.Describe(input).shapeType != "Polygon":
        # Raise a custom exception
        raise ShapeError("Input does not contain polygons")

    # Get the new field name and validate it.
    field_name = arcpy.GetParameterAsText(1)
    field_name = arcpy.ValidateFieldName(field_name, os.path.dirname(in_fc))

    # Add the new field and calculate the value.
    arcpy.management.AddField(in_fc, field_name, "DOUBLE")
    arcpy.management.CalculateField(
        in_fc, field_name, "!shape.area! / !shape.length!", "PYTHON3"
    )
except ShapeError as err:
    print(err)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

### Example 3

```python
import arcpy
import os

class ShapeError(Exception):
    pass


try:
    # Get the input feature class and make sure it contains polygons.
    in_fc = arcpy.GetParameterAsText(0)
    if arcpy.Describe(input).shapeType != "Polygon":
        # Raise a custom exception
        raise ShapeError("Input does not contain polygons")

    # Get the new field name and validate it.
    field_name = arcpy.GetParameterAsText(1)
    field_name = arcpy.ValidateFieldName(field_name, os.path.dirname(in_fc))

    # Add the new field and calculate the value.
    arcpy.management.AddField(in_fc, field_name, "DOUBLE")
    arcpy.management.CalculateField(
        in_fc, field_name, "!shape.area! / !shape.length!", "PYTHON3"
    )
except ShapeError as err:
    print(err)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
```

---

## ValidateTableName

## Summary

Returns a valid table name for a workspace based on a table name and a workspace path. All invalid characters in the input table name are replaced with an underscore. The table name restrictions depend on the type of database.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The table name that will be validated. | String |
| workspace | The workspace that will be used to validate the table name.If the workspace is not specified, the Current Workspace environment will be used. If the Current Workspace environment is not set, a folder workspace will be used. | String |

## Code Samples

### Example 1

```python
ValidateTableName (name, {workspace})
```

### Example 2

```python
import os
import arcpy

# Get the input and output workspaces.
arcpy.env.workspace = arcpy.GetParameterAsText(0)
out_workspace = arcpy.GetParameterAsText(1)

# Get a list of input feature classes to be copied and copy to new output 
# location.
for fc in arcpy.ListFeatureClasses():
    out_fc = arcpy.ValidateTableName(fc, out_workspace)
    arcpy.management.CopyFeatures(fc, os.path.join(out_workspace, out_fc))
```

### Example 3

```python
import os
import arcpy

# Get the input and output workspaces.
arcpy.env.workspace = arcpy.GetParameterAsText(0)
out_workspace = arcpy.GetParameterAsText(1)

# Get a list of input feature classes to be copied and copy to new output 
# location.
for fc in arcpy.ListFeatureClasses():
    out_fc = arcpy.ValidateTableName(fc, out_workspace)
    arcpy.management.CopyFeatures(fc, os.path.join(out_workspace, out_fc))
```

---

## Vehicle Routing Problem Solver properties

## Summary

The following properties are supported by the network analyst solver object when working with the vehicle routing problem solver. Note that the distance cost attribute can be obtained from the accumulators property on the Describe object.

---

## VPF Coverage properties

## Summary

The Describe function returns the Dataset property group for VPF coverages.

---

## VPF Feature Class properties

## Summary

The Describe function returns the Feature Class, Table, and Dataset property groups for VPF feature classes.

---

## VPF Table properties

## Summary

The Describe function returns the Table and Dataset property groups for VPF tables.

---

## Workspace properties

## Summary

The Describe function returns the properties described below for a workspace.

## Code Samples

### Example 1

```python
describe = arcpy.Describe(data)
# Not - if describe.workspaceFactoryProgID == 'esriDataSourcesGDB.FileGDBWorkspaceFactory.1'
if describe.workspaceFactoryProgID.startswith('esriDataSourcesGDB.FileGDBWorkspaceFactory'):
    continue
```

### Example 2

```python
describe = arcpy.Describe(data)
# Not - if describe.workspaceFactoryProgID == 'esriDataSourcesGDB.FileGDBWorkspaceFactory.1'
if describe.workspaceFactoryProgID.startswith('esriDataSourcesGDB.FileGDBWorkspaceFactory'):
    continue
```

### Example 3

```python
import arcpy

# Create a Describe object for an Enterprise database
desc = arcpy.Describe(r"c:\data\Connection to state.sde")

print(f"Connection string:       {desc.connectionString}")
print(f"WorkspaceFactoryProgID:  {desc.workspaceFactoryProgID}")
print(f"Workspace type:          {desc.workspaceType}")

# Print connection properties
cp = desc.connectionProperties
print("\nDatabase Connection Properties:")
print(f"  Server:          {cp.server}")
print(f"  Instance:        {cp.instance}")
print(f"  Database:        {cp.database}")
print(f"  Database client: {cp.dbClient}")
print(f"  User:            {cp.user}")
print(f"  Version:         {cp.version}")

# Print workspace domain names
domains = desc.domains
print("\nDomains:")
for domain in domains:
    print(f"  {domain}")
```

### Example 4

```python
import arcpy

# Create a Describe object for an Enterprise database
desc = arcpy.Describe(r"c:\data\Connection to state.sde")

print(f"Connection string:       {desc.connectionString}")
print(f"WorkspaceFactoryProgID:  {desc.workspaceFactoryProgID}")
print(f"Workspace type:          {desc.workspaceType}")

# Print connection properties
cp = desc.connectionProperties
print("\nDatabase Connection Properties:")
print(f"  Server:          {cp.server}")
print(f"  Instance:        {cp.instance}")
print(f"  Database:        {cp.database}")
print(f"  Database client: {cp.dbClient}")
print(f"  User:            {cp.user}")
print(f"  Version:         {cp.version}")

# Print workspace domain names
domains = desc.domains
print("\nDomains:")
for domain in domains:
    print(f"  {domain}")
```

---
