# Data Management and Workflows

*Consolidated from 101 individual documentation files*

---

## World files for CAD and BIM data

## Code Samples

### Example 1

```python
25933.063000,9032.704720,1702332.110159, 309622.102491,-8987.532001,1300.050854
32047.556994,13057.483520,1706354.400361 303697.073028,-9091.566340,1337.519601
```

### Example 2

```python
25933.063000,9032.704720,1702332.110159, 309622.102491,-8987.532001,1300.050854
32047.556994,13057.483520,1706354.400361 303697.073028,-9091.566340,1337.519601
```

---

## Add the ST_Geometry type to a PostgreSQL database

## Code Samples

### Example 1

```python
"""
Name: create_spatial_type.py
Description: Provide connection information to an enterprise database
and create spatial type in the Oracle or PostgreSQL database.
Type create_spatial_type.py -h or create_spatial_type.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS: ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-p", dest="Password", type="string", default="", help="SDE user password")
parser.add_option ("-t", dest="tablespace", type="string", default="", help="Default tablespace for SDE user")
parser.add_option ("--path", dest="libpath", type="string", default="", help="path to the ST shape library including library file name.")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("{}: error: {}\n".format(sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	password = options.Password 
	tablespace = options.tablespace
	database = options.Database.lower()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	lib_path = options.libpath

	if( database_type ==""):	
		print("{}: error: {}\n".format(sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")	
	
	# Process: Create spatial type...
	try:
		print("Create spatial type...\n")
		arcpy.management.CreateSpatialType(input_database=Connection_File_Name_full_path, sde_user_password=password, tablespace_name=tablespace, st_shape_library_path=lib_path)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_spatial_type.py
Description: Provide connection information to an enterprise database
and create spatial type in the Oracle or PostgreSQL database.
Type create_spatial_type.py -h or create_spatial_type.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS: ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-p", dest="Password", type="string", default="", help="SDE user password")
parser.add_option ("-t", dest="tablespace", type="string", default="", help="Default tablespace for SDE user")
parser.add_option ("--path", dest="libpath", type="string", default="", help="path to the ST shape library including library file name.")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("{}: error: {}\n".format(sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	password = options.Password 
	tablespace = options.tablespace
	database = options.Database.lower()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	lib_path = options.libpath

	if( database_type ==""):	
		print("{}: error: {}\n".format(sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")	
	
	# Process: Create spatial type...
	try:
		print("Create spatial type...\n")
		arcpy.management.CreateSpatialType(input_database=Connection_File_Name_full_path, sde_user_password=password, tablespace_name=tablespace, st_shape_library_path=lib_path)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_spatial_type.py --DBMS POSTGRESQL -i pgserve --auth DATABASE_AUTH -U postgres -P M3tsy$ -D spdata -p 3$@b0eg -t sde --path /net/pgserve/opt/PostgreSQL/12.4/lib/st_geometry.so
```

### Example 4

```python
create_spatial_type.py --DBMS POSTGRESQL -i pgserve --auth DATABASE_AUTH -U postgres -P M3tsy$ -D spdata -p 3$@b0eg -t sde --path /net/pgserve/opt/PostgreSQL/12.4/lib/st_geometry.so
```

---

## Add the ST_Geometry type to an Oracle database

## Code Samples

### Example 1

```python
"""
Name: create_spatial_type.py
Description: Provide connection information to an enterprise database
and create spatial type in the Oracle or PostgreSQL database.
Type create_spatial_type.py -h or create_spatial_type.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS: ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-p", dest="Password", type="string", default="", help="SDE user password")
parser.add_option ("-t", dest="tablespace", type="string", default="", help="Default tablespace for SDE user")
parser.add_option ("--path", dest="libpath", type="string", default="", help="path to the ST shape library including library file name.")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("{}: error: {}\n".format(sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	password = options.Password 
	tablespace = options.tablespace
	database = options.Database.lower()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	lib_path = options.libpath

	if( database_type ==""):	
		print("{}: error: {}\n".format(sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")	
	
	# Process: Create spatial type...
	try:
		print("Create spatial type...\n")
		arcpy.management.CreateSpatialType(input_database=Connection_File_Name_full_path, sde_user_password=password, tablespace_name=tablespace, st_shape_library_path=lib_path)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_spatial_type.py
Description: Provide connection information to an enterprise database
and create spatial type in the Oracle or PostgreSQL database.
Type create_spatial_type.py -h or create_spatial_type.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS: ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-p", dest="Password", type="string", default="", help="SDE user password")
parser.add_option ("-t", dest="tablespace", type="string", default="", help="Default tablespace for SDE user")
parser.add_option ("--path", dest="libpath", type="string", default="", help="path to the ST shape library including library file name.")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("{}: error: {}\n".format(sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	password = options.Password 
	tablespace = options.tablespace
	database = options.Database.lower()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	lib_path = options.libpath

	if( database_type ==""):	
		print("{}: error: {}\n".format(sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")	
	
	# Process: Create spatial type...
	try:
		print("Create spatial type...\n")
		arcpy.management.CreateSpatialType(input_database=Connection_File_Name_full_path, sde_user_password=password, tablespace_name=tablespace, st_shape_library_path=lib_path)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_spatial_type.py --DBMS ORACLE -i oserve/orcl --auth DATABASE_AUTH -U sys -P M3tsy$ -p 3$@b0eg -t sde --path /net/oserve/ora/shape/libst_shapelib.so
```

### Example 4

```python
create_spatial_type.py --DBMS ORACLE -i oserve/orcl --auth DATABASE_AUTH -U sys -P M3tsy$ -p 3$@b0eg -t sde --path /net/oserve/ora/shape/libst_shapelib.so
```

---

## Connect to Google BigQuery from ArcGIS

## Code Samples

### Example 1

```python
# -----------------------------------------------------------------------
# Modify this section to configure an ODBC connection to Google BigQuery Data 
# Warehouse.
#
# To make a connection, copy GoogleBigQueryODBC.did to the lib folder under the 
# extracted directory for Google BigQuery ODBC driver. Edit 
# simba.googlebigqueryodbc.ini and set DriverManagerEncoding=UTF-16. Configure and 
# store the odbcinst.ini in the /etc folder. 
#
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export SIMBAGOOGLEBIGQUERYODBCINI=<Location_to_simba.googlebigqueryodbc.ini>/simba.googlebigqueryodbc.ini
```

### Example 2

```python
# -----------------------------------------------------------------------
# Modify this section to configure an ODBC connection to Google BigQuery Data 
# Warehouse.
#
# To make a connection, copy GoogleBigQueryODBC.did to the lib folder under the 
# extracted directory for Google BigQuery ODBC driver. Edit 
# simba.googlebigqueryodbc.ini and set DriverManagerEncoding=UTF-16. Configure and 
# store the odbcinst.ini in the /etc folder. 
#
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export SIMBAGOOGLEBIGQUERYODBCINI=<Location_to_simba.googlebigqueryodbc.ini>/simba.googlebigqueryodbc.ini
```

---

## Connect to Dameng from ArcGIS

## Code Samples

### Example 1

```python
# Modify this section to configure a connection to Dameng.
export DAMENGDIR=<Dameng_InstallDir> 
export LD_LIBRARY_PATH=$DAMENGDIR/bin:$LD_LIBRARY_PATH
```

### Example 2

```python
# Modify this section to configure a connection to Dameng.
export DAMENGDIR=<Dameng_InstallDir> 
export LD_LIBRARY_PATH=$DAMENGDIR/bin:$LD_LIBRARY_PATH
```

---

## Connect to Db2 from ArcGIS

## Code Samples

### Example 1

```python
#
# Modify this section to configure a connection to Db2
export DB2_CLIENT_HOME=<DB2_InstallDir>
export DB2INSTANCE=<DB2_instance_name>
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 2

```python
#
# Modify this section to configure a connection to Db2
export DB2_CLIENT_HOME=<DB2_InstallDir>
export DB2INSTANCE=<DB2_instance_name>
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 3

```python
#
# For connection with Db2
#
export DB2_CLIENT_HOME=/home/db2prod
export DB2INSTANCE=db2prod
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 4

```python
#
# For connection with Db2
#
export DB2_CLIENT_HOME=/home/db2prod
export DB2INSTANCE=db2prod
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

---

## Connect to Oracle from ArcGIS

## Code Samples

### Example 1

```python
#
# For connection with Oracle Runtime or Administrator Client
#
export ORACLE_BASE=<Oracle_Installdir>/app
export ORACLE_HOME=$ORACLE_BASE/<Oracle_release>/product/<Oracle_version>/<client_version>
export ORACLE_SID=<set when applicable>
export TNS_ADMIN=<set when applicable. e.g.$ORACLE_HOME/network/admin>
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
```

### Example 2

```python
#
# For connection with Oracle Runtime or Administrator Client
#
export ORACLE_BASE=<Oracle_Installdir>/app
export ORACLE_HOME=$ORACLE_BASE/<Oracle_release>/product/<Oracle_version>/<client_version>
export ORACLE_SID=<set when applicable>
export TNS_ADMIN=<set when applicable. e.g.$ORACLE_HOME/network/admin>
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
```

### Example 3

```python
#
# For connection with Oracle Instant Client
#
export LD_LIBRARY_PATH=<Location_to_instantclient_11_2>:$LD_LIBRARY_PATH
```

### Example 4

```python
#
# For connection with Oracle Instant Client
#
export LD_LIBRARY_PATH=<Location_to_instantclient_11_2>:$LD_LIBRARY_PATH
```

### Example 5

```python
ORACLE_BASE=<Oracle_Installdir>
```

### Example 6

```python
ORACLE_HOME=$ORACLE_BASE/<Oracle_Release>/product/<Oracle_Version>/client_1
```

---

## Connect to Amazon Redshift from ArcGIS

## Code Samples

### Example 1

```python
# -----------------------------------------------------------------------
# Modify this section to configure Amazon Redshift ODBC connector
# 
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export AMAZONREDSHIFTODBCINI=<Location_to_amazon.redshiftodbc.ini>/amazon.redshiftodbc.ini
```

### Example 2

```python
# -----------------------------------------------------------------------
# Modify this section to configure Amazon Redshift ODBC connector
# 
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export AMAZONREDSHIFTODBCINI=<Location_to_amazon.redshiftodbc.ini>/amazon.redshiftodbc.ini
```

---

## Connect to SAP HANA from ArcGIS

## Code Samples

### Example 1

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to SAP HANA.
#
# To make a connection, name the SAP HANA ODBC configuration files as .odbcinst.ini
# and .odbc.ini and store them in the ArcGIS Server user $HOME directory.
#
# -----------------------------------------------------------------------
export SAPHANADIR=<SAPHANA_InstallDir>/sap/hdbclient
export LD_LIBRARY_PATH=$SAPHANADIR:$LD_LIBRARY_PATH
```

### Example 2

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to SAP HANA.
#
# To make a connection, name the SAP HANA ODBC configuration files as .odbcinst.ini
# and .odbc.ini and store them in the ArcGIS Server user $HOME directory.
#
# -----------------------------------------------------------------------
export SAPHANADIR=<SAPHANA_InstallDir>/sap/hdbclient
export LD_LIBRARY_PATH=$SAPHANADIR:$LD_LIBRARY_PATH
```

### Example 3

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
SPATIALTYPES=1

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 4

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
ENCRYPT=Yes
sslTrustStore=<path to DigiCertGlobalRootCA.crt.pem>

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 5

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
ENCRYPT=Yes
sslTrustStore=-----BEGIN CERTIFICATE-----<contents of the DigiCertGlobalRootCA.crt.pem file>-----END CERTIFICATE-----

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 6

```python
Description  =SAP HANA ODBC
Driver64         = /<usr>/sap/hdbclient/libodbcHDB.so
```

---

## Connect to Snowflake from ArcGIS

## Code Samples

### Example 1

```python
#
# Modify this section to configure a connection to Snowflake Data Warehouse
# 
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export LD_PRELOAD=$LD_PRELOAD:$LIB_ODBC_DRIVER_MANAGER:<Location_to_libSnowflake.so>/libSnowflake.so
```

### Example 2

```python
#
# Modify this section to configure a connection to Snowflake Data Warehouse
# 
# -----------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Location_to_ODBC_driver_manager_libraries>/libodbc.so.2
export LD_PRELOAD=$LD_PRELOAD:$LIB_ODBC_DRIVER_MANAGER:<Location_to_libSnowflake.so>/libSnowflake.so
```

---

## Connect to Teradata from ArcGIS

## Code Samples

### Example 1

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to Teradata.
#
# To make a connection, name the Teradata ODBC configuration files as  
# .odbcinst.ini and .odbc.ini and store them in the ArcGIS Server user $HOME directory. 
#
# -------------------------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Teradata_InstallDir>/<version>/14.00/odbc_64/lib/libodbc.so
export TDDIR=<Teradata_InstallDir>/client/<version>/odbc_64
export LD_LIBRARY_PATH=$TDDIR/lib:$LD_LIBRARY_PATH
export ODBCINI=<Location_to_.odbc.ini>/.odbc.ini
```

### Example 2

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to Teradata.
#
# To make a connection, name the Teradata ODBC configuration files as  
# .odbcinst.ini and .odbc.ini and store them in the ArcGIS Server user $HOME directory. 
#
# -------------------------------------------------------------------------------------
export LIB_ODBC_DRIVER_MANAGER=<Teradata_InstallDir>/<version>/14.00/odbc_64/lib/libodbc.so
export TDDIR=<Teradata_InstallDir>/client/<version>/odbc_64
export LD_LIBRARY_PATH=$TDDIR/lib:$LD_LIBRARY_PATH
export ODBCINI=<Location_to_.odbc.ini>/.odbc.ini
```

---

## Supported databases and data warehouses

## Code Samples

### Example 1

```python
CREATE TABLE mytable (
  id INTEGER PRIMARY KEY NOT NULL, 
  item TEXT, 
  weight INTEGER,
  store TEXT;
```

### Example 2

```python
CREATE TABLE mytable (
  id INTEGER PRIMARY KEY NOT NULL, 
  item TEXT, 
  weight INTEGER,
  store TEXT;
```

### Example 3

```python
INSERT INTO mytable (id, item, weight, store) VALUES(
 1,
 "magnetic dual elliptical trainer with seat",
 75,
 "CardioPlus Equipment"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 2,
 "superfit treadmill4000",
 81.2,
 "Sports Pit"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 3,
 "serenity yoga mat",
 .4588,
 "Aerobic Angels Sporting Goods"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 4,
 "swim fins",
 "two",
 "The Plunge"
);
```

### Example 4

```python
INSERT INTO mytable (id, item, weight, store) VALUES(
 1,
 "magnetic dual elliptical trainer with seat",
 75,
 "CardioPlus Equipment"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 2,
 "superfit treadmill4000",
 81.2,
 "Sports Pit"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 3,
 "serenity yoga mat",
 .4588,
 "Aerobic Angels Sporting Goods"
);

INSERT INTO mytable (id, item, weight, store) VALUES(
 4,
 "swim fins",
 "two",
 "The Plunge"
);
```

### Example 5

```python
database mybackupdb;
```

### Example 6

```python
database mybackupdb;
```

### Example 7

```python
CREATE TABLE mybackupdb.spatial_ref_sys 
  AS sysspatial.spatial_ref_sys WITH DATA;

CREATE TABLE mybackupdb.geometry_columns 
  AS sysspatial.geometry_columns WITH DATA;
```

### Example 8

```python
CREATE TABLE mybackupdb.spatial_ref_sys 
  AS sysspatial.spatial_ref_sys WITH DATA;

CREATE TABLE mybackupdb.geometry_columns 
  AS sysspatial.geometry_columns WITH DATA;
```

### Example 9

```python
--Restore the geometry columns table.
INSERT INTO sysspatial.geometry_columns 
  SELECT * FROM mybackupdb.geometry_columns;

--Restore the spatial_ref_sys table.
INSERT INTO sysspatial.spatial_ref_sys 
  SELECT * FROM mybackupdb.spatial_ref_sys 
  MINUS 
    SELECT * FROM sysspatial.spatial_ref_sys;
```

### Example 10

```python
--Restore the geometry columns table.
INSERT INTO sysspatial.geometry_columns 
  SELECT * FROM mybackupdb.geometry_columns;

--Restore the spatial_ref_sys table.
INSERT INTO sysspatial.spatial_ref_sys 
  SELECT * FROM mybackupdb.spatial_ref_sys 
  MINUS 
    SELECT * FROM sysspatial.spatial_ref_sys;
```

### Example 11

```python
DROP TABLE mybackupdb.spatial_ref_sys;

DROP TABLE mybackupdb.geometry_columns;
```

### Example 12

```python
DROP TABLE mybackupdb.spatial_ref_sys;

DROP TABLE mybackupdb.geometry_columns;
```

---

## Initialize Dameng geometry

## Code Samples

### Example 1

```python
SP_INIT_GEO_SYS(1);
```

### Example 2

```python
SP_INIT_GEO_SYS(1);
```

### Example 3

```python
SELECT SF_CHECK_GEO_SYS;
```

### Example 4

```python
SELECT SF_CHECK_GEO_SYS;
```

### Example 5

```python
LINEID    SF_CHECK_GEO_SYS
1         1
```

---

## Spatially enable an SQLite database

## Code Samples

### Example 1

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 2

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 3

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 4

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 5

```python
SELECT CreateOGCTables();
```

### Example 6

```python
SELECT CreateOGCTables();
```

### Example 7

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 8

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 9

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 10

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 11

```python
SELECT CreateGpkgTables();
```

### Example 12

```python
SELECT CreateGpkgTables();
```

---

## Alter configuration keywords

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "DB2", "TEAMDATA", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "DB2", "TEAMDATA", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME")
```

### Example 3

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 4

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 5

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 6

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

---

## Db2 configuration parameters

## Code Samples

### Example 1

```python
CREATE TABLE btab (col1 BLOB INLINE LENGTH 220)
```

### Example 2

```python
CREATE TABLE btab (col1 BLOB INLINE LENGTH 220)
```

### Example 3

```python
ST_GEOM_STORAGE_INLINE "INLINE LENGTH 3000"
```

---

## Connect to Db2 from ArcGIS

## Code Samples

### Example 1

```python
#
# Modify this section to configure a connection to Db2
export DB2_CLIENT_HOME=<DB2_InstallDir>
export DB2INSTANCE=<DB2_instance_name>
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 2

```python
#
# Modify this section to configure a connection to Db2
export DB2_CLIENT_HOME=<DB2_InstallDir>
export DB2INSTANCE=<DB2_instance_name>
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 3

```python
#
# For connection with Db2
#
export DB2_CLIENT_HOME=/home/db2prod
export DB2INSTANCE=db2prod
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

### Example 4

```python
#
# For connection with Db2
#
export DB2_CLIENT_HOME=/home/db2prod
export DB2INSTANCE=db2prod
export PATH=DB2_CLIENT_HOME/bin:$PATH
export LD_LIBRARY_PATH=$DB2_CLIENT_HOME/lib64:$LD_LIBRARY_PATH
```

---

## Manage connections to a geodatabase in Db2

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "dgdb.sde", "DB2", "spdb2", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "dgdb.sde", "DB2", "spdb2", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME")
```

### Example 3

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\dgdb.sde")
```

### Example 4

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\dgdb.sde")
```

### Example 5

```python
[user(ClientName=u'PC4', ConnectionTime=datetime.datetime(2018, 2, 18, 8, 30, 19),
 ID=18, IsDirecConnection=True, Name=u'publisher1')]
[user(ClientName=u'PC25', ConnectionTime=datetime.datetime(2018, 2, 21, 14, 10, 43),
 ID=33, IsDirecConnection=True, Name=u'editor2')]
[user(ClientName=u'PC11', ConnectionTime=datetime.datetime(2018, 2, 22, 9, 18, 26),
 ID=39, IsDirecConnection=True, Name=u'reader5')]
[user(ClientName=u'PCA2', ConnectionTime=datetime.datetime(2018, 2, 22, 11, 21, 2),
 ID=41, IsDirecConnection=True, Name=u'sde')]
```

### Example 6

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\dgdb.sde",33)
```

### Example 7

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\dgdb.sde",33)
```

---

## Rebuild system table indexes

## Code Samples

### Example 1

```python
# Name: RSysIdxDb2.py
# Description: Rebuilds indexes on the states, state_lineages,
# and mv_tables_modified tables in an enterprise geodatabase
# in DB2.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = DB2
instance = db2gdb
account_authentication = OPERATING_SYSTEM_AUTH | DATABASE_AUTH
#Leave username and password blank if using OPERATING_SYSTEM_AUTH
username = sde
password = gdb_admin_password


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 2

```python
# Name: RSysIdxDb2.py
# Description: Rebuilds indexes on the states, state_lineages,
# and mv_tables_modified tables in an enterprise geodatabase
# in DB2.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = DB2
instance = db2gdb
account_authentication = OPERATING_SYSTEM_AUTH | DATABASE_AUTH
#Leave username and password blank if using OPERATING_SYSTEM_AUTH
username = sde
password = gdb_admin_password


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 3

```python
0 22 * * 3 /usr/bin/rsysidxdb2.py
```

---

## Create a geodatabase in Db2

## Code Samples

### Example 1

```python
CREATE USER TEMPORARY TABLESPACE geospace PAGESIZE 8 K MANAGED BY AUTOMATIC STORAGE BUFFERPOOL IBMDEFAULTBP;

GRANT USE OF TABLESPACE geospace TO geodatausers WITH GRANT OPTION;
```

### Example 2

```python
CREATE USER TEMPORARY TABLESPACE geospace PAGESIZE 8 K MANAGED BY AUTOMATIC STORAGE BUFFERPOOL IBMDEFAULTBP;

GRANT USE OF TABLESPACE geospace TO geodatausers WITH GRANT OPTION;
```

### Example 3

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 4

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 5

```python
enable_gdb.py --DBMS DB2 -i db2prod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 6

```python
enable_gdb.py --DBMS DB2 -i db2prod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 7

```python
/enable_gdb.py --DBMS DB2 -i db2prod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 8

```python
/enable_gdb.py --DBMS DB2 -i db2prod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

---

## Update database statistics

## Code Samples

### Example 1

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

### Example 2

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

---

## Upgrade a geodatabase in Db2

## Code Samples

### Example 1

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "DB2",
                                          "mydbgdb",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 2

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "DB2",
                                          "mydbgdb",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 3

```python
GRANT EXECUTE 
 ON MON_GET_CONNECTION 
 TO SDE;
```

### Example 4

```python
GRANT EXECUTE 
 ON MON_GET_CONNECTION 
 TO SDE;
```

### Example 5

```python
SQL0551N  "SASHA" does not have the privilege to perform operation "SELECT" on object "SYSIBM.SYSDUMMY1".  SQLSTATE=42501
```

### Example 6

```python
GRANT SELECT 
 ON SYSIBM.SYSDUMMY1 
 TO PUBLIC;
```

### Example 7

```python
GRANT SELECT 
 ON SYSIBM.SYSDUMMY1 
 TO PUBLIC;
```

### Example 8

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 9

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 10

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux or UNIX computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 11

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux or UNIX computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 12

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 13

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 14

```python
gdbupgrade --DBMS DB2 -i mydbgdb --auth DATABASE_AUTH -u sde -p mysdepassword --upgrade TRUE
```

---

## Create a file geodatabase

## Code Samples

### Example 1

```python
# Import system modules
import os
import sys
import arcpy

# Set workspace
arcpy.env.workspace = r"Z:\home\user\mydata"

# Set local variables
out_folder_path = r"Z:\home\user\mydata"
out_name = "myfgdb.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)
```

### Example 2

```python
# Import system modules
import os
import sys
import arcpy

# Set workspace
arcpy.env.workspace = r"Z:\home\user\mydata"

# Set local variables
out_folder_path = r"Z:\home\user\mydata"
out_name = "myfgdb.gdb"

# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)
```

### Example 3

```python
import arcpy

arcpy.CreateFileGDB_management(r"Z:\home\user\gdbs", "myfgdb.gdb")
```

### Example 4

```python
import arcpy

arcpy.CreateFileGDB_management(r"Z:\home\user\gdbs", "myfgdb.gdb")
```

---

## File geodatabases: compress vs. compact

## Code Samples

### Example 1

```python
A41 A41 A41
```

---

## License a file geodatabase

## Code Samples

### Example 1

```python
datalicinstall c:\\data\proj3.sdlic
```

### Example 2

```python
datalicinstall c:\\data\proj3.sdlic
```

### Example 3

```python
./datalicinstall/usr/data/proj3.sdlic
```

### Example 4

```python
./datalicinstall/usr/data/proj3.sdlic
```

---

## File geodatabases SQL reference

## Code Samples

### Example 1

```python
SELECT COUNTY_NAME, POP1997 - POP1990 AS PopChange
 FROM counties
 ORDER BY COUNTY_NAME
```

### Example 2

```python
SELECT COUNTY_NAME, POP1997 - POP1990 AS PopChange
 FROM counties
 ORDER BY COUNTY_NAME
```

### Example 3

```python
SELECT name,salary,
 CASE
	 WHEN salary <= 2000 THEN 'low'
	 WHEN salary > 2000 AND salary <= 3000 THEN 'average'
	 WHEN salary > 3000 THEN 'high'
	END AS salary_level
	FROM employees
```

### Example 4

```python
SELECT name,salary,
 CASE
	 WHEN salary <= 2000 THEN 'low'
	 WHEN salary > 2000 AND salary <= 3000 THEN 'average'
	 WHEN salary > 3000 THEN 'high'
	END AS salary_level
	FROM employees
```

### Example 5

```python
SELECT Name, COALESCE(Business_Phone, Cell_Phone, Home_Phone)
Contact_Phone
 FROM Contact_Info
```

### Example 6

```python
SELECT Name, COALESCE(Business_Phone, Cell_Phone, Home_Phone)
Contact_Phone
 FROM Contact_Info
```

### Example 7

```python
SELECT Location, NULLIF(Sales, Forecast) AS Results
 FROM StoreSales
```

### Example 8

```python
SELECT Location, NULLIF(Sales, Forecast) AS Results
 FROM StoreSales
```

### Example 9

```python
SELECT state_name, SUM(POP1990) AS TotalPopulation
 FROM counties
 GROUP BY STATE_NAME
 ORDER BY STATE_NAME
```

### Example 10

```python
SELECT state_name, SUM(POP1990) AS TotalPopulation
 FROM counties
 GROUP BY STATE_NAME
 ORDER BY STATE_NAME
```

### Example 11

```python
SELECT department, MAX(salary) AS Highest_salary
 FROM employees
 GROUP BY department HAVING MAX(salary) < 50000
```

### Example 12

```python
SELECT department, MAX(salary) AS Highest_salary
 FROM employees
 GROUP BY department HAVING MAX(salary) < 50000
```

### Example 13

```python
SELECT Table1.name, Table1.Address, Table2.name, Table2.Salary
 FROM Table1
  CROSS JOIN Table2
```

### Example 14

```python
SELECT Table1.name, Table1.Address, Table2.name, Table2.Salary
 FROM Table1
  CROSS JOIN Table2
```

### Example 15

```python
SELECT Table1.C1, Table1.C2, Table2.C3, Table2.C4
 FROM Table1
  INNER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 16

```python
SELECT Table1.C1, Table1.C2, Table2.C3, Table2.C4
 FROM Table1
  INNER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 17

```python
SELECT Table1.C1, Table1.C2, Table2.C3, Table2.C4
 FROM Table1
  LEFT OUTER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 18

```python
SELECT Table1.C1, Table1.C2, Table2.C3, Table2.C4
 FROM Table1
  LEFT OUTER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 19

```python
SELECT * FROM Table1
 RIGHT OUTER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 20

```python
SELECT * FROM Table1
 RIGHT OUTER JOIN Table2 ON Table1.C1 = Table2.C3
```

### Example 21

```python
SELECT STATE_NAME, POP1990
 FROM counties
 ORDER BY STATE_NAME
```

### Example 22

```python
SELECT STATE_NAME, POP1990
 FROM counties
 ORDER BY STATE_NAME
```

### Example 23

```python
SELECT STATE_NAME, POP1990
 FROM counties
 ORDER BY STATE_NAME
 COLLATE CASE DESC
```

### Example 24

```python
SELECT STATE_NAME, POP1990
 FROM counties
 ORDER BY STATE_NAME
 COLLATE CASE DESC
```

### Example 25

```python
SELECT state_name
 FROM counties
 WHERE state_name SIMILAR TO 'North%'
```

### Example 26

```python
SELECT state_name
 FROM counties
 WHERE state_name SIMILAR TO 'North%'
```

---

## Create a mobile geodatabase

## Code Samples

### Example 1

```python
# Import system modules
import os
import sys
import arcpy

# Set workspace
env.workspace = "Z:\home\user\mydata"

# Set local variables
out_folder_path = "Z:\home\user\mydata"
out_name = "mymgdb.geodatabase"

# Run CreateMobileGDB
arcpy.CreateMobileGDB_management(out_folder_path, out_name)
```

### Example 2

```python
# Import system modules
import os
import sys
import arcpy

# Set workspace
env.workspace = "Z:\home\user\mydata"

# Set local variables
out_folder_path = "Z:\home\user\mydata"
out_name = "mymgdb.geodatabase"

# Run CreateMobileGDB
arcpy.CreateMobileGDB_management(out_folder_path, out_name)
```

### Example 3

```python
import arcpy

arcpy.CreateMobileGDB_management("Z:\home\user\gdbs", "mymgdb.geodatabase")
```

### Example 4

```python
import arcpy

arcpy.CreateMobileGDB_management("Z:\home\user\gdbs", "mymgdb.geodatabase")
```

---

## Load ST_Geometry to a mobile geodatabase for SQL access

## Code Samples

### Example 1

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 2

```python
SELECT load_extension('stgeometry_sqlite.dll','SDE_SQL_funcs_init');
```

### Example 3

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 4

```python
SELECT load_extension('libstgeometry_sqlite','SDE_SQL_funcs_init');
```

### Example 5

```python
SELECT CreateOGCTables();
```

### Example 6

```python
SELECT CreateOGCTables();
```

---

## Add users to Oracle

## Code Samples

### Example 1

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_database_user.py --DBMS ORACLE -i dbsrv/orcl -U sys -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 4

```python
create_database_user.py --DBMS ORACLE -i dbsrv/orcl -U sys -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 5

```python
./create_database_user.py --DBMS ORACLE -i dbsrv/orcl -U sys -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 6

```python
./create_database_user.py --DBMS ORACLE -i dbsrv/orcl -U sys -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

---

## Alter configuration keywords

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "ORACLE", "teamdata/orcl", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "ORACLE", "teamdata/orcl", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME")
```

### Example 3

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 4

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 5

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 6

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

---

## Oracle configuration parameters

## Code Samples

### Example 1

```python
SQL> SELECT * FROM SDE.DBTUNE
  2  WHERE KEYWORD = 'DEFAULTS' AND PARAMETER_NAME LIKE 'RAS%';

KEYWORD   PARAMETER_NAME   CONFIG_STRING
------------  ----------------------   -------------------------
DEFAULTS   RASTER_STORAGE   BLOB

DEFAULTS   RAS_INDEX_ID        PCTFREE 0 INITRANS 8 TABLESPACE IDX1 NOLOGGING

DEFAULTS   RAS_STORAGE        PCTFREE 0 INITRANS 8 TABLESPACE RASTER
```

### Example 2

```python
SQL> SELECT * FROM SDE.DBTUNE
  2  WHERE KEYWORD = 'DEFAULTS' AND PARAMETER_NAME LIKE 'RAS%';

KEYWORD   PARAMETER_NAME   CONFIG_STRING
------------  ----------------------   -------------------------
DEFAULTS   RASTER_STORAGE   BLOB

DEFAULTS   RAS_INDEX_ID        PCTFREE 0 INITRANS 8 TABLESPACE IDX1 NOLOGGING

DEFAULTS   RAS_STORAGE        PCTFREE 0 INITRANS 8 TABLESPACE RASTER
```

### Example 3

```python
DEFAULTS  RAS_STORAGE  PCTFREE 0 INITRANS 8 TABLESPACE RASTER
```

### Example 4

```python
CREATE TABLE myuser.sde_ras_6
(raster_id number(38),
 raster_flags number(38),
 description varchar2(65))
PCTFREE			0
INITRANS       8
TABLESPACE raster
```

### Example 5

```python
CREATE TABLE myuser.sde_ras_6
(raster_id number(38),
 raster_flags number(38),
 description varchar2(65))
PCTFREE			0
INITRANS       8
TABLESPACE raster
```

### Example 6

```python
SQL> connect <user>/<password>
SQL> SELECT default_tablespace 
 FROM user_users;
```

### Example 7

```python
SQL> connect <user>/<password>
SQL> SELECT default_tablespace 
 FROM user_users;
```

### Example 8

```python
SQL> connect system/<password>
SQL> SELECT default_tablespace 
 FROM dba_users 
 WHERE username = <'USER'>;
```

### Example 9

```python
SQL> connect system/<password>
SQL> SELECT default_tablespace 
 FROM dba_users 
 WHERE username = <'USER'>;
```

### Example 10

```python
SQL> connect <user>/<password>
SQL> SELECT * FROM user_tablespaces 
WHERE tablespace_name = <'TABLESPACE'>;
```

### Example 11

```python
SQL> connect <user>/<password>
SQL> SELECT * FROM user_tablespaces 
WHERE tablespace_name = <'TABLESPACE'>;
```

### Example 12

```python
ORA-14016: underlying table of a LOCAL partitioned index must be partitioned
```

### Example 13

```python
RASTER_STORAGE BLOB
ATTRIBUTE_BINARY BLOB
```

### Example 14

```python
RASTER_STORAGE BLOB
ATTRIBUTE_BINARY BLOB
```

### Example 15

```python
RASTER_STORAGE "BLOB"
BLK_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE RASTER 
             LOB (BLOCK_DATA) STORE AS 
             (TABLESPACE RASTER_LOB_SEGMENT 
              CACHE PCTVERSION 0)" 

AUX_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE RASTER 
             LOB (OBJECT) STORE AS 
             (TABLESPACE RASTER 
              CACHE PCTVERSION 0)"
```

### Example 16

```python
RASTER_STORAGE "BLOB"
BLK_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE RASTER 
             LOB (BLOCK_DATA) STORE AS 
             (TABLESPACE RASTER_LOB_SEGMENT 
              CACHE PCTVERSION 0)" 

AUX_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE RASTER 
             LOB (OBJECT) STORE AS 
             (TABLESPACE RASTER 
              CACHE PCTVERSION 0)"
```

### Example 17

```python
ATTRIBUTE_BINARY "BLOB"

B_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE BIZZTABS 
             LOB (DOCUMENT) STORE AS 
             (TABLESPACE BIZZ_LOB_SEGMENT 
              CACHE PCTVERSION 0)"

A_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE BIZZTABS 
             LOB (DOCUMENT) STORE AS 
             (TABLESPACE BIZZ_LOB_SEGMENT 
              CACHE PCTVERSION 0)"
```

### Example 18

```python
ATTRIBUTE_BINARY "BLOB"

B_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE BIZZTABS 
             LOB (DOCUMENT) STORE AS 
             (TABLESPACE BIZZ_LOB_SEGMENT 
              CACHE PCTVERSION 0)"

A_STORAGE "PCTFREE 0 INITRANS 4 TABLESPACE BIZZTABS 
             LOB (DOCUMENT) STORE AS 
             (TABLESPACE BIZZ_LOB_SEGMENT 
              CACHE PCTVERSION 0)"
```

### Example 19

```python
ORA-00904: "DOCUMENT": invalid identifier
```

### Example 20

```python
ORA-00904: "DOCUMENT": invalid identifier
```

---

## Configure extproc to access ST_Geometry in Oracle

## Code Samples

### Example 1

```python
SELECT file_spec
 FROM user_libraries
 WHERE library_name = 'ST_SHAPELIB';
```

### Example 2

```python
SELECT file_spec
 FROM user_libraries
 WHERE library_name = 'ST_SHAPELIB';
```

### Example 3

```python
CREATE or REPLACE LIBRARY ST_SHAPELIB
 AS 'C:\mylibraries\st_shapelib.dll';
```

### Example 4

```python
CREATE or REPLACE LIBRARY ST_SHAPELIB
 AS 'C:\mylibraries\st_shapelib.dll';
```

### Example 5

```python
ALTER PACKAGE sde.st_geometry_shapelib_pkg COMPILE
 REUSE SETTINGS;
```

### Example 6

```python
ALTER PACKAGE sde.st_geometry_shapelib_pkg COMPILE
 REUSE SETTINGS;
```

### Example 7

```python
SELECT object_name, object_type
  FROM USER_OBJECTS
  WHERE STATUS = 'INVALID';
```

### Example 8

```python
SELECT object_name, object_type
  FROM USER_OBJECTS
  WHERE STATUS = 'INVALID';
```

---

## Connect to Oracle from ArcGIS

## Code Samples

### Example 1

```python
#
# For connection with Oracle Runtime or Administrator Client
#
export ORACLE_BASE=<Oracle_Installdir>/app
export ORACLE_HOME=$ORACLE_BASE/<Oracle_release>/product/<Oracle_version>/<client_version>
export ORACLE_SID=<set when applicable>
export TNS_ADMIN=<set when applicable. e.g.$ORACLE_HOME/network/admin>
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
```

### Example 2

```python
#
# For connection with Oracle Runtime or Administrator Client
#
export ORACLE_BASE=<Oracle_Installdir>/app
export ORACLE_HOME=$ORACLE_BASE/<Oracle_release>/product/<Oracle_version>/<client_version>
export ORACLE_SID=<set when applicable>
export TNS_ADMIN=<set when applicable. e.g.$ORACLE_HOME/network/admin>
export PATH=$ORACLE_HOME/bin:$PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
```

### Example 3

```python
#
# For connection with Oracle Instant Client
#
export LD_LIBRARY_PATH=<Location_to_instantclient_11_2>:$LD_LIBRARY_PATH
```

### Example 4

```python
#
# For connection with Oracle Instant Client
#
export LD_LIBRARY_PATH=<Location_to_instantclient_11_2>:$LD_LIBRARY_PATH
```

### Example 5

```python
ORACLE_BASE=<Oracle_Installdir>
```

### Example 6

```python
ORACLE_HOME=$ORACLE_BASE/<Oracle_Release>/product/<Oracle_Version>/client_1
```

---

## Manage connections to a geodatabase in Oracle

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "oragdb.sde", "ORACLE", "spora", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "oragdb.sde", "ORACLE", "spora", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME")
```

### Example 3

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\oragdb.sde")
```

### Example 4

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\oragdb.sde")
```

### Example 5

```python
[user(ClientName=u'PC4', ConnectionTime=datetime.datetime(2018, 10, 18, 8, 30, 19),
 ID=18, IsDirecConnection=True, Name=u'publisher1')]
[user(ClientName=u'PC25', ConnectionTime=datetime.datetime(2018, 10, 21, 14, 10, 43),
 ID=33, IsDirecConnection=True, Name=u'editor2')]
[user(ClientName=u'PC11', ConnectionTime=datetime.datetime(2018, 10, 22, 9, 18, 26),
 ID=39, IsDirecConnection=True, Name=u'reader5')]
[user(ClientName=u'PCA2', ConnectionTime=datetime.datetime(2018, 10, 22, 11, 21, 2),
 ID=41, IsDirecConnection=True, Name=u'sde')]
```

### Example 6

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\oragdb.sde",33)
```

### Example 7

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\oragdb.sde",33)
```

---

## Privileges for geodatabases in Oracle

## Code Samples

### Example 1

```python
GRANT EXECUTE ON dbms_pipe TO public;
GRANT EXECUTE ON dbms_lock TO public;
GRANT EXECUTE ON dbms_lob TO public;
GRANT EXECUTE ON dbms_utility TO public;
GRANT EXECUTE ON dbms_sql TO public;
GRANT EXECUTE ON utl_raw TO public;
```

### Example 2

```python
GRANT EXECUTE ON dbms_pipe TO public;
GRANT EXECUTE ON dbms_lock TO public;
GRANT EXECUTE ON dbms_lob TO public;
GRANT EXECUTE ON dbms_utility TO public;
GRANT EXECUTE ON dbms_sql TO public;
GRANT EXECUTE ON utl_raw TO public;
```

### Example 3

```python
EXEC dbms_utility.compile_schema( 'SDE' );
```

### Example 4

```python
EXEC dbms_utility.compile_schema( 'SDE' );
```

---

## Rebuild system table indexes

## Code Samples

### Example 1

```python
# Name: RSysIdxOracle.py
# Description: Rebuilds indexes on the states, state_lineages,
# and mv_tables_modified tables in an enterprise geodatabase
# in Oracle.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = ORACLE
instance = "myserver/orcl"
account_authentication = OPERATING_SYSTEM_AUTH | DATABASE_AUTH
#Leave username and password blank if using OPERATING_SYSTEM_AUTH
username = gdb_admin
password = gdb_admin_password


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 2

```python
# Name: RSysIdxOracle.py
# Description: Rebuilds indexes on the states, state_lineages,
# and mv_tables_modified tables in an enterprise geodatabase
# in Oracle.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = ORACLE
instance = "myserver/orcl"
account_authentication = OPERATING_SYSTEM_AUTH | DATABASE_AUTH
#Leave username and password blank if using OPERATING_SYSTEM_AUTH
username = gdb_admin
password = gdb_admin_password


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 3

```python
0 22 * * 3 /usr/bin/rsysidxdb2.py
```

---

## Create a geodatabase in Oracle

## Code Samples

### Example 1

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
./create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 4

```python
./create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 5

```python
create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 6

```python
create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 7

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 8

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 9

```python
enable_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 10

```python
enable_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 11

```python
create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 12

```python
create_gdb.py --DBMS ORACLE -i gisprod/orcl --auth DATABASE_AUTH -U sys
 -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t sde -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

---

## ST_Geometry in Oracle

## Code Samples

### Example 1

```python
CREATE TABLE hazardous_sites (name        varchar2(128),
                              location    st_geometry);
```

### Example 2

```python
CREATE TABLE hazardous_sites (name        varchar2(128),
                              location    st_geometry);
```

### Example 3

```python
SELECT name, sde.st_area(geometry)
FROM us_states
ORDER BY name;
```

### Example 4

```python
SELECT name, sde.st_area(geometry)
FROM us_states
ORDER BY name;
```

### Example 5

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?

 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 1) );
```

### Example 6

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?

 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 1) );
```

### Example 7

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?
 
 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 PT_Z                           NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 5, 1) );
```

### Example 8

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?
 
 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 PT_Z                           NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 5, 1) );
```

### Example 9

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?

 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 PT_Z                           NUMBER                  IN
 MEASURE                        NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 5, 401, 1) );
```

### Example 10

```python
METHOD

 FINAL CONSTRUCTOR FUNCTION ST_POINT RETURNS SELF AS RESULT
 Argument Name                  Type                    In/Out Default?

 PT_X                           NUMBER                  IN
 PT_Y                           NUMBER                  IN
 PT_Z                           NUMBER                  IN
 MEASURE                        NUMBER                  IN
 SRID                           NUMBER                  IN

SQL> INSERT INTO sample_pt VALUES (sde.ST_Point (10, 20, 5, 401, 1) );
```

### Example 11

```python
##ST_GEOMETRY
GEOMETRY_STORAGE    "ST_GEOMETRY"
ATTRIBUTE_BINARY    "BLOB"
RASTER_STORAGE	    "BLOB"
ST_GEOM_LOB_STORAGE  " STORE AS (
#               TABLESPACE <tablespace_name>
                ENABLE STORAGE IN ROW CHUNK 8K RETENTION CACHE)"

UI_TEXT             "User Interface text description for ST_GEOMETRY"

COMMENT             "Any general comment for ST_GEOMETRY keyword"

END
```

### Example 12

```python
ST_GEOM_LOB_STORAGE  " STORE AS (
  ENABLE STORAGE IN ROW CHUNK 8K RETENTION CACHE)"
```

### Example 13

```python
##ST_GEOMETRY
GEOMETRY_STORAGE    "ST_GEOMETRY"
ATTRIBUTE_BINARY    "BLOB"
RASTER_STORAGE	    "BLOB"
ST_GEOM_LOB_STORAGE  " STORE AS (TABLESPACE TERRA_NDX ENABLE STORAGE IN ROW CHUNK 8K
 RETENTION CACHE)"

UI_TEXT             "User Interface text description for ST_GEOMETRY"

COMMENT             "Any general comment for ST_GEOMETRY keyword"

END
```

### Example 14

```python
##ST_GEOMETRY
GEOMETRY_STORAGE    "ST_GEOMETRY"
ATTRIBUTE_BINARY    "BLOB"
RASTER_STORAGE	    "BLOB"
ST_GEOM_LOB_STORAGE  " STORE AS (ENABLE STORAGE IN ROW CHUNK 8K RETENTION CACHE)"

UI_TEXT             "User Interface text description for ST_GEOMETRY"

COMMENT             "Any general comment for ST_GEOMETRY keyword"

END
```

---

## Update open_cursors setting in geodatabases in Oracle

## Code Samples

### Example 1

```python
GRANT INHERIT PRIVILEGES ON USER SYS TO SDE;
```

### Example 2

```python
GRANT INHERIT PRIVILEGES ON USER SYS TO SDE;
```

### Example 3

```python
EXECUTE sde.gdb_util.update_open_cursors;
```

### Example 4

```python
EXECUTE sde.gdb_util.update_open_cursors;
```

### Example 5

```python
REVOKE INHERIT PRIVILEGES ON USER SYS FROM SDE;
```

### Example 6

```python
REVOKE INHERIT PRIVILEGES ON USER SYS FROM SDE;
```

---

## Update database statistics

## Code Samples

### Example 1

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

### Example 2

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

---

## Upgrade a geodatabase in Oracle

## Code Samples

### Example 1

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "ORACLE",
                                          "myogdb",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 2

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "ORACLE",
                                          "myogdb",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 3

```python
SELECT owner, object_name
FROM all_objects
WHERE object_type = 'PACKAGE'
  AND object_name = 'CTX_DDL';
```

### Example 4

```python
SELECT owner, object_name
FROM all_objects
WHERE object_type = 'PACKAGE'
  AND object_name = 'CTX_DDL';
```

### Example 5

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 6

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 7

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux or UNIX computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 8

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux or UNIX computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 9

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 10

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

---

## Add login roles to PostgreSQL

## Code Samples

### Example 1

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_database_user.py --DBMS POSTGRESQL -i pgdb7 -D gisdata -U postgres -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 4

```python
create_database_user.py --DBMS POSTGRESQL -i pgdb7 -D gisdata -U postgres -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 5

```python
./create_database_user.py --DBMS POSTGRESQL -i pgdb7 -D gisdata -U postgres -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 6

```python
./create_database_user.py --DBMS POSTGRESQL -i pgdb7 -D gisdata -U postgres -P $hHhH --utype DATABASE_USER -u geodata -p 0wn1t
```

### Example 7

```python
CREATE ROLE editors 
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;

CREATE ROLE viewers
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
```

### Example 8

```python
CREATE ROLE editors 
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;

CREATE ROLE viewers
NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT;
```

### Example 9

```python
CREATE ROLE editor1 LOGIN 
ENCRYPTED PASSWORD 'sooper.secret' 
NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT IN ROLE editors;
```

### Example 10

```python
CREATE ROLE editor1 LOGIN 
ENCRYPTED PASSWORD 'sooper.secret' 
NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT IN ROLE editors;
```

### Example 11

```python
CREATE ROLE reader1 LOGIN 
ENCRYPTED PASSWORD 'almostas.secret' 
NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT IN ROLE viewers;
```

### Example 12

```python
CREATE ROLE reader1 LOGIN 
ENCRYPTED PASSWORD 'almostas.secret' 
NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT IN ROLE viewers;
```

### Example 13

```python
GRANT USAGE ON SCHEMA geodata TO editors;
GRANT USAGE ON SCHEMA geodata TO viewers;
```

### Example 14

```python
GRANT USAGE ON SCHEMA geodata TO editors;
GRANT USAGE ON SCHEMA geodata TO viewers;
```

### Example 15

```python
GRANT USAGE ON SCHEMA sde TO editors;
GRANT USAGE ON SCHEMA sde TO viewers;
```

### Example 16

```python
GRANT USAGE ON SCHEMA sde TO editors;
GRANT USAGE ON SCHEMA sde TO viewers;
```

---

## Alter configuration keywords

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "POSTGRESQL", "teamserver", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME", "projects")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management (r'/usr/connectionfiles', "admin.sde", "POSTGRESQL", "teamserver", "DATABASE_AUTH", "sde", "Cky00r", "SAVE_USERNAME", "projects")
```

### Example 3

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 4

```python
arcpy.ExportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 5

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

### Example 6

```python
arcpy.ImportGeodatabaseConfigurationKeywords_management (r'/usr/connectionfiles/admin.sde', r'/usr/tmp/config.vi')
```

---

## Create a geodatabase in a PostgreSQL cloud-based database service

## Code Samples

### Example 1

```python
arcpy.management.EnableEnterpriseGeodatabase(r"C:\proprojects\pg_proj\postresdbaas.sde",r"C:\authcodes\keyfile")
```

### Example 2

```python
arcpy.management.EnableEnterpriseGeodatabase(r"C:\proprojects\pg_proj\postresdbaas.sde",r"C:\authcodes\keyfile")
```

### Example 3

```python
arcpy.management.EnableEnterpriseGeodatabase("/usr/connectionfiles/postresdbaas.sde","/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes")
```

### Example 4

```python
arcpy.management.EnableEnterpriseGeodatabase("/usr/connectionfiles/postresdbaas.sde","/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes")
```

### Example 5

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 6

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 7

```python
./enable_gdb.py --DBMS POSTGRESQL -i database-1-instance-1.zyxjtlpj9fer.us-west-2.rds.amazonaws.com --auth DATABASE_AUTH 
-u sde -p sdeP@ss -D myauroradb -l '/usr/arcgis/auth/keycodes'
```

### Example 8

```python
./enable_gdb.py --DBMS POSTGRESQL -i database-1-instance-1.zyxjtlpj9fer.us-west-2.rds.amazonaws.com --auth DATABASE_AUTH 
-u sde -p sdeP@ss -D myauroradb -l '/usr/arcgis/auth/keycodes'
```

### Example 9

```python
enable_gdb.py --DBMS POSTGRESQL -i my-pg-flex.postgres.database.azure.com --auth DATABASE_AUTH 
-u sde -p EsDeeEpass -D azurepgf -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 10

```python
enable_gdb.py --DBMS POSTGRESQL -i my-pg-flex.postgres.database.azure.com --auth DATABASE_AUTH 
-u sde -p EsDeeEpass -D azurepgf -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 11

```python
enable_gdb.py --DBMS POSTGRESQL -i 98.765.43.210 --auth DATABASE_AUTH 
-u sde -p Zpassw0rd -D gcspostgres -l '\\Users\MyUser\Documents\AuthFiles\keycodes'
```

### Example 12

```python
enable_gdb.py --DBMS POSTGRESQL -i 98.765.43.210 --auth DATABASE_AUTH 
-u sde -p Zpassw0rd -D gcspostgres -l '\\Users\MyUser\Documents\AuthFiles\keycodes'
```

---

## PostgreSQL data types supported in ArcGIS

## Code Samples

### Example 1

```python
SELECT id, name, total::text
 FROM me.mydb.tableb;
```

### Example 2

```python
SELECT id, name, total::text
 FROM me.mydb.tableb;
```

### Example 3

```python
GRANT select 
 ON public.geometry_columns 
 TO <login_name>;

GRANT select 
 ON public.geography_columns 
 TO <login_name>;

GRANT select
 ON public.spatial_ref_sys
 TO <login_name>;
```

### Example 4

```python
GRANT select 
 ON public.geometry_columns 
 TO <login_name>;

GRANT select 
 ON public.geography_columns 
 TO <login_name>;

GRANT select
 ON public.spatial_ref_sys
 TO <login_name>;
```

### Example 5

```python
##PG_GEOMETRY
GEOMETRY_STORAGE    "PG_GEOMETRY"
UI_TEXT             "User Interface text description for POSTGIS geometry storage" 
END
```

### Example 6

```python
##PG_GEOGRAPHY
GEOMETRY_STORAGE    "PG_GEOGRAPHY"
UI_TEXT             "User Interface text description for POSTGIS geography storage" 
END
```

---

## Tutorial: Get started with geodatabases in PostgreSQL

## Code Samples

### Example 1

```python
#TYPE  DATABASE     USER    ADDRESS            METHOD

host     all        all     .orgnetwork.com     md5
```

---

## Manage connections to a geodatabase in PostgreSQL

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "pgdb.sde", "POSTGRESQL", "mydbc", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME", "pg1")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp", "pgdb.sde", "POSTGRESQL", "mydbc", "DATABASE_AUTH", "sde", "mysdepwd", "SAVE_USERNAME", "pg1")
```

### Example 3

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\pgdb.sde")
```

### Example 4

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\pgdb.sde")
```

### Example 5

```python
[user(ClientName=u'PC4', ConnectionTime=datetime.datetime(2018, 10, 18, 8, 30, 19),
 ID=18, IsDirecConnection=True, Name=u'publisher1')]
[user(ClientName=u'PC25', ConnectionTime=datetime.datetime(2018, 10, 21, 14, 10, 43),
 ID=33, IsDirecConnection=True, Name=u'editor2')]
[user(ClientName=u'PC11', ConnectionTime=datetime.datetime(2018, 10, 22, 9, 18, 26),
 ID=39, IsDirecConnection=True, Name=u'reader5')]
[user(ClientName=u'PCA2', ConnectionTime=datetime.datetime(2018, 10, 22, 11, 21, 2),
 ID=41, IsDirecConnection=True, Name=u'sde')]
```

### Example 6

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\pgdb.sde",33)
```

### Example 7

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\pgdb.sde",33)
```

---

## Rebuild system table indexes

## Code Samples

### Example 1

```python
# Name: RSysIdxpg.py
# Description: Rebuilds indexes on the sde_states, sde_state_lineages,
# and sde_mv_tables_modified tables in an enterprise geodatabase
# in PostgreSQL.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = POSTGRESQL
instance = pg_cluster
account_authentication = DATABASE_AUTH
username = gdb_admin
password = gdb_admin_password
database = database_name


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass, database
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo, database)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 2

```python
# Name: RSysIdxpg.py
# Description: Rebuilds indexes on the sde_states, sde_state_lineages,
# and sde_mv_tables_modified tables in an enterprise geodatabase
# in PostgreSQL.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = POSTGRESQL
instance = pg_cluster
account_authentication = DATABASE_AUTH
username = gdb_admin
password = gdb_admin_password
database = database_name


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

#Variable defined within the script; other variable options commented out at the end of the line
saveUserInfo = "SAVE_USERNAME" #DO_NOT_SAVE_USERNAME

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass, database
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, username, password, saveUserInfo, database)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 3

```python
0 22 * * 3 /usr/bin/rsysidxdb2.py
```

---

## Restore a geodatabase to PostgreSQL

## Code Samples

### Example 1

```python
dropdb –U sde mypgdb
```

### Example 2

```python
dropdb –U sde mypgdb
```

### Example 3

```python
CREATE ROLE sde LOGIN 
  ENCRYPTED PASSWORD '0shallpass'
  SUPERUSER INHERIT;
```

### Example 4

```python
CREATE ROLE sde LOGIN 
  ENCRYPTED PASSWORD '0shallpass'
  SUPERUSER INHERIT;
```

### Example 5

```python
--Re-create dataowners group and login roles.
CREATE ROLE dataowners
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE owner1 LOGIN
  ENCRYPTED PASSWORD 'pw.4.owner1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT dataowners TO owner1;

CREATE ROLE owner2 LOGIN
  ENCRYPTED PASSWORD 'pw.4.owner2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT dataowners TO owner2;

--Re-create editors group and login roles.
CREATE ROLE editors
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE editor1 LOGIN
  ENCRYPTED PASSWORD 'pw.4editor1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT editors TO editor1;

CREATE ROLE editor2 LOGIN
  ENCRYPTED PASSWORD 'pw.4editor2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT editors TO editor2;

--Re-create readers group and login roles.
CREATE ROLE readers
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE reader1 LOGIN
  ENCRYPTED PASSWORD 'pw.4reader1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT readers TO reader1;

CREATE ROLE reader2 LOGIN
  ENCRYPTED PASSWORD 'pw.4reader2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT readers TO reader2;
```

### Example 6

```python
--Re-create dataowners group and login roles.
CREATE ROLE dataowners
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE owner1 LOGIN
  ENCRYPTED PASSWORD 'pw.4.owner1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT dataowners TO owner1;

CREATE ROLE owner2 LOGIN
  ENCRYPTED PASSWORD 'pw.4.owner2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT dataowners TO owner2;

--Re-create editors group and login roles.
CREATE ROLE editors
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE editor1 LOGIN
  ENCRYPTED PASSWORD 'pw.4editor1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT editors TO editor1;

CREATE ROLE editor2 LOGIN
  ENCRYPTED PASSWORD 'pw.4editor2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT editors TO editor2;

--Re-create readers group and login roles.
CREATE ROLE readers
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

CREATE ROLE reader1 LOGIN
  ENCRYPTED PASSWORD 'pw.4reader1'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT readers TO reader1;

CREATE ROLE reader2 LOGIN
  ENCRYPTED PASSWORD 'pw.4reader2'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT readers TO reader2;
```

### Example 7

```python
createdb –U sde –E UTF8 –D tblspgdb -O sde mypgdb
```

### Example 8

```python
createdb –U sde –E UTF8 –D tblspgdb -O sde mypgdb
```

### Example 9

```python
CREATE SCHEMA sde
  AUTHORIZATION sde;

GRANT USAGE ON SCHEMA sde TO dataowners;
GRANT USAGE ON SCHEMA sde TO editors;
GRANT USAGE ON SCHEMA sde TO readers;
```

### Example 10

```python
CREATE SCHEMA sde
  AUTHORIZATION sde;

GRANT USAGE ON SCHEMA sde TO dataowners;
GRANT USAGE ON SCHEMA sde TO editors;
GRANT USAGE ON SCHEMA sde TO readers;
```

### Example 11

```python
ALTER DATABASE mypgdb
  SET SEARCH_PATH="$user",public,sde;
```

### Example 12

```python
ALTER DATABASE mypgdb
  SET SEARCH_PATH="$user",public,sde;
```

---

## Create a geodatabase in PostgreSQL on Linux

## Code Samples

### Example 1

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 4

```python
create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 5

```python
./create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 6

```python
./create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 7

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 8

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 9

```python
enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 10

```python
enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 11

```python
./enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 12

```python
./enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

---

## Create a geodatabase in PostgreSQL on Windows

## Code Samples

### Example 1

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 4

```python
create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 5

```python
./create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 6

```python
./create_gdb.py --DBMS POSTGRESQL -i pgprod -D entgdb --auth DATABASE_AUTH 
-U postgres -P N0pe3king! -u sde -p Tgdbst@rtsh3r3 -t gis -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 7

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 8

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 9

```python
enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 10

```python
enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 11

```python
./enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

### Example 12

```python
./enable_gdb.py --DBMS POSTGRESQL -i pgprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '/usr/arcgis/server/framework/runtime/.wine/drive_c/Program Files/ESRI/License/sysgen/keycodes'
```

---

## ST_Geometry in PostgreSQL

## Code Samples

### Example 1

```python
CREATE TABLE hazardous_sites (name varchar(128), location st_geometry);
```

### Example 2

```python
CREATE TABLE hazardous_sites (name varchar(128), location st_geometry);
```

### Example 3

```python
SELECT name, st_area(geometry)
FROM us_states
ORDER BY name;
```

### Example 4

```python
SELECT name, st_area(geometry)
FROM us_states
ORDER BY name;
```

### Example 5

```python
##ST_GEOMETRY
GEOMETRY_STORAGE    "ST_GEOMETRY"
UI_TEXT   "User-interface for ST_GEOMETRY keyword"

END
```

### Example 6

```python
SELECT st_register_spatial_column('<database_name>', '<schema_name>', 
'<table_name>', '<spatial_column_name>', <srid>, <coordinate_dimension>)
```

### Example 7

```python
SELECT st_register_spatial_column('<database_name>', '<schema_name>', 
'<table_name>', '<spatial_column_name>', <srid>, <coordinate_dimension>)
```

### Example 8

```python
SELECT st_register_spatial_column(
'mycitydb', 'sasha', 'blocks', 'shape', 4236, 3);
```

### Example 9

```python
SELECT st_register_spatial_column(
'mycitydb', 'sasha', 'blocks', 'shape', 4236, 3);
```

### Example 10

```python
SELECT st_unregister_spatial_column(
'<database_name>', '<schema_name>',
 '<table_name>', '<column_name>')
```

### Example 11

```python
SELECT st_unregister_spatial_column(
'<database_name>', '<schema_name>',
 '<table_name>', '<column_name>')
```

### Example 12

```python
SELECT st_isregistered_spatial_column(
'<database_name>', '<schema_name>',
 '<table_name>', '<column_name>', <srid>)
```

### Example 13

```python
SELECT st_isregistered_spatial_column(
'<database_name>', '<schema_name>',
 '<table_name>', '<column_name>', <srid>)
```

### Example 14

```python
SELECT st_get_coord_dimension(
'<schema_name>', '<table_name>', '<column_name>', <srid>)
```

### Example 15

```python
SELECT st_get_coord_dimension(
'<schema_name>', '<table_name>', '<column_name>', <srid>)
```

### Example 16

```python
SELECT st_get_coord_dimension(
'sasha', 'blocks', 'shape', 4236);

st_get_coord_dimension
---------------------------
xyz
```

### Example 17

```python
SELECT st_get_coord_dimension(
'sasha', 'blocks', 'shape', 4236);

st_get_coord_dimension
---------------------------
xyz
```

---

## Update database statistics

## Code Samples

### Example 1

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

### Example 2

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

---

## Upgrade a geodatabase in PostgreSQL

## Code Samples

### Example 1

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "POSTGRESQL",
                                          "mypgdbcluster",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME",
                                          "mypgdb")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 2

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "POSTGRESQL",
                                          "mypgdbcluster",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME",
                                          "mypgdb")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 3

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase in PostgreSQL

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 4

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase in PostgreSQL

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 5

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase in PostgreSQL

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 6

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Linux computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase in PostgreSQL

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "<user>/connections/<Connection_file>"
Default_gdb = "<user>/connections/<Connection_file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 7

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 8

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 9

```python
gdbupgrade --DBMS POSTGRESQL -i mypgdbcluster --auth DATABASE_AUTH -u sde -p mysdepassword --upgrade TRUE -D mypgdb
```

---

## Connect to SAP HANA from ArcGIS

## Code Samples

### Example 1

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to SAP HANA.
#
# To make a connection, name the SAP HANA ODBC configuration files as .odbcinst.ini
# and .odbc.ini and store them in the ArcGIS Server user $HOME directory.
#
# -----------------------------------------------------------------------
export SAPHANADIR=<SAPHANA_InstallDir>/sap/hdbclient
export LD_LIBRARY_PATH=$SAPHANADIR:$LD_LIBRARY_PATH
```

### Example 2

```python
# -----------------------------------------------------------------------
# Modify this section to configure a connection to SAP HANA.
#
# To make a connection, name the SAP HANA ODBC configuration files as .odbcinst.ini
# and .odbc.ini and store them in the ArcGIS Server user $HOME directory.
#
# -----------------------------------------------------------------------
export SAPHANADIR=<SAPHANA_InstallDir>/sap/hdbclient
export LD_LIBRARY_PATH=$SAPHANADIR:$LD_LIBRARY_PATH
```

### Example 3

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
SPATIALTYPES=1

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 4

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
ENCRYPT=Yes
sslTrustStore=<path to DigiCertGlobalRootCA.crt.pem>

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 5

```python
[<HANA_DNS>]
Driver=/<usr>/sap/hdbclient/libodbcHDB.so
Description=SAP Hana ODBC
ServerNode=<HANA_Server_IP>:<SAP_HANA_port>
UID=<user_name>
Password=<user_password>
ENCRYPT=Yes
sslTrustStore=-----BEGIN CERTIFICATE-----<contents of the DigiCertGlobalRootCA.crt.pem file>-----END CERTIFICATE-----

[ODBC]
IANAAppCodePage=4
InstallDir=/<usr>/sap/hdbclient
Trace=0
TraceDll=/opt/odbc64v51/lib/odbctrac.so
TraceFile=/tmp/odbctrace.out
UseCursorLib=0
```

### Example 6

```python
Description  =SAP HANA ODBC
Driver64         = /<usr>/sap/hdbclient/libodbcHDB.so
```

---

## Create a geodatabase in SAP HANA

## Code Samples

### Example 1

```python
import arcpy, os, sys, tempfile

if len(sys.argv) != 3:
	print ("usage: enable_gdb.py  database_dsn  sde_pwd")
	sys.exit(3)

path = tempfile.gettempdir()
if os.path.exists(path + r'\enable_gdb.sde'):
    os.remove(path + r'\enable_gdb.sde')
    

arcpy.management.CreateDatabaseConnection(path ,r'enable_gdb.sde', 'SAP HANA',sys.argv[1], 'DATABASE_AUTH','sde',sys.argv[2], 'SAVE_USERNAME')

arcpy.management.EnableEnterpriseGeodatabase(path + r'\enable_gdb.sde', r"\\mykeycodes\Server_Ent_Adv")

if os.path.exists(path + r'\enable_gdb.sde'):
    os.remove(path + r'\enable_gdb.sde')
    
sys.exit(0)
```

### Example 2

```python
import arcpy, os, sys, tempfile

if len(sys.argv) != 3:
	print ("usage: enable_gdb.py  database_dsn  sde_pwd")
	sys.exit(3)

path = tempfile.gettempdir()
if os.path.exists(path + r'\enable_gdb.sde'):
    os.remove(path + r'\enable_gdb.sde')
    

arcpy.management.CreateDatabaseConnection(path ,r'enable_gdb.sde', 'SAP HANA',sys.argv[1], 'DATABASE_AUTH','sde',sys.argv[2], 'SAVE_USERNAME')

arcpy.management.EnableEnterpriseGeodatabase(path + r'\enable_gdb.sde', r"\\mykeycodes\Server_Ent_Adv")

if os.path.exists(path + r'\enable_gdb.sde'):
    os.remove(path + r'\enable_gdb.sde')
    
sys.exit(0)
```

### Example 3

```python
enable_gdb.py hana1 M@kagdb4me
```

### Example 4

```python
enable_gdb.py hana1 M@kagdb4me
```

---

## Manage connections to a geodatabase in SAP HANA

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("/usr/dbconnections", "saphana.sde", "SAPHANA", "spsap", "DATABASE_AUTH", "sde", "thesdepwd", "SAVE_USERNAME")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("/usr/dbconnections", "saphana.sde", "SAPHANA", "spsap", "DATABASE_AUTH", "sde", "thesdepwd", "SAVE_USERNAME")
```

### Example 3

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("/usr/dbconnections/saphana.sde")
```

### Example 4

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("/usr/dbconnections/saphana.sde")
```

### Example 5

```python
[user(ClientName=u'PC4', ConnectionTime=datetime.datetime(2018, 10, 18, 8, 30, 19),
 ID=18, IsDirecConnection=True, Name=u'PUBLISHER1')]
[user(ClientName=u'PC25', ConnectionTime=datetime.datetime(2018, 10, 21, 14, 10, 43),
 ID=33, IsDirecConnection=True, Name=u'EDITOR2')]
[user(ClientName=u'PC11', ConnectionTime=datetime.datetime(2018, 10, 22, 9, 18, 26),
 ID=39, IsDirecConnection=True, Name=u'READER5')]
[user(ClientName=u'PCA2', ConnectionTime=datetime.datetime(2018, 10, 22, 11, 21, 2),
 ID=41, IsDirecConnection=True, Name=u'SDE')]
```

### Example 6

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("/usr/dbconnections/saphana.sde",33)
```

### Example 7

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("/usr/dbconnections/saphana.sde",33)
```

---

## Upgrade a geodatabase in SAP HANA

## Code Samples

### Example 1

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase. You must connect as the sde user.
arcpy.CreateDatabaseConnection_management("/usr/tmp/",
                                          "egdb_connection.sde",
                                          "SAP HANA",
                                          sys.argv[1],
                                          "DATABASE_AUTH",
                                          "sde",
                                          sys.argv[2],
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/usr/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 2

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase. You must connect as the sde user.
arcpy.CreateDatabaseConnection_management("/usr/tmp/",
                                          "egdb_connection.sde",
                                          "SAP HANA",
                                          sys.argv[1],
                                          "DATABASE_AUTH",
                                          "sde",
                                          sys.argv[2],
                                          "SAVE_USERNAME")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/usr/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 3

```python
"""
Name: upgrade_gdb_for_sap_hana.py
Type upgrade_gdb_for_sap_hana.py -h or upgrade_gdb_sap_hana.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("-i", dest="data_source", type="string", default="", help="SAP HANA ODBC data source name")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print ("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = "DATABASE_AUTH"
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = ""
	database_type = "SAP HANA"
	instance = options.data_source
	
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print ("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print ("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	Conn_File_NameT = instance + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print ("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        			

	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print ("Upgrading Geodatabase...\n")
			arcpy.management.UpgradeGDB(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print ("Running Pre-Requisite Check...\n")
			arcpy.management.UpgradeGDB(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print ("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 4

```python
"""
Name: upgrade_gdb_for_sap_hana.py
Type upgrade_gdb_for_sap_hana.py -h or upgrade_gdb_sap_hana.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("-i", dest="data_source", type="string", default="", help="SAP HANA ODBC data source name")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print ("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = "DATABASE_AUTH"
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = ""
	database_type = "SAP HANA"
	instance = options.data_source
	
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print ("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print ("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	Conn_File_NameT = instance + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print ("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.management.CreateDatabaseConnection(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        			

	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print ("Upgrading Geodatabase...\n")
			arcpy.management.UpgradeGDB(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print ("Running Pre-Requisite Check...\n")
			arcpy.management.UpgradeGDB(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print ("\n")
		parser.print_help()
		parser.exit(2)
```

---

## Add logins and users to SQL Server

## Code Samples

### Example 1

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_database_user.py
Description: Provide connection information to a database user.
Type create_database_user.py -h or create_database_user.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 release")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")                   
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--utype", dest="user_type", type ="choice", choices=['DATABASE_USER', 'OPERATING_SYSTEM_USER'], default='DATABASE_USER', help="Authentication type options (case-sensitive):  DATABASE_USER, OPERATING_SYSTEM_USER.  Default=DATABASE_USER")
parser.add_option ("-u", dest="dbuser", type="string", default="", help="database user name")
parser.add_option ("-p", dest="dbuser_pwd", type="string", default="", help="database user password")
parser.add_option ("-r", dest="role", type="string", default="", help="role to be granted to the user")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print "%s: error: %s\n" % (sys.argv[0], "No command options given")
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	dbuser = options.dbuser
	dbuser_pwd = options.dbuser_pwd	
	tablespace = options.Tablespace
	user_type = options.user_type
	role = options.role

	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
	
	if(database_type == "SQL_SERVER"):
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))
	else:		
		if( dbuser.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Database user must be specified."))
			sys.exit(3)		
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

	if ( user_type == "DATABASE_USER" and (dbuser =="" or dbuser_pwd =="")):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "To create database authenticated user, user name and password must be specified!"))
		parser.print_help()
		sys.exit(3)	

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Creating a user in an enterprise geodatabase or database requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before creating a database user.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")

	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin   

	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)

	try:
		print("\nCreating Database Connection File...\n")
		# Process: Create Database Connection File...
		# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
		#arcpy.CreateDatabaseConnection_management(temp , Connection_File_Name, database_type, instance, database, account_authentication, dbms_admin, dbms_admin_pwd, "TRUE")
		arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
	        for i in range(arcpy.GetMessageCount()):
			if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("\n+++++++++")
				arcpy.AddMessage("Exiting!!")
				arcpy.AddMessage("+++++++++\n")
				sys.exit(3)            
			else:
				arcpy.AddReturnMessage(i)
				arcpy.AddMessage("+++++++++\n")

		print("Creating database user...\n")
		arcpy.CreateDatabaseUser_management(input_workspace=Connection_File_Name_full_path, user_authentication_type=user_type, user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name=tablespace)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_database_user.py --DBMS SQL_SERVER -i ssi5 -D gisdata --auth DATABASE_AUTH -U sa -P !nocopy! --utype DATABASE_USER -u gisd_owner -p T3mpPass
```

### Example 4

```python
create_database_user.py --DBMS SQL_SERVER -i ssi5 -D gisdata --auth DATABASE_AUTH -U sa -P !nocopy! --utype DATABASE_USER -u gisd_owner -p T3mpPass
```

---

## SQL Server configuration parameters

## Code Samples

### Example 1

```python
B_INDEX_ROWID "with fillfactor=99 
ON IDXfg"
```

### Example 2

```python
B_INDEX_USER "with fillfactor=99 
ON IDXfg"
```

### Example 3

```python
B_INDEX_XML "with fillfactor=99 
ON XMLfg"
```

### Example 4

```python
B_INDEX_RASTER "with fillfactor=99 
ON RASfg"
```

### Example 5

```python
B_STORAGE "ON ADDS_FG"
```

### Example 6

```python
A_INDEX_ROWID "with fillfactor=99 
ON IDXfg"
```

### Example 7

```python
A_INDEX_STATEID "with fillfactor=99 
ON STATEIDXfg"
```

### Example 8

```python
A_INDEX_USER "with fillfactor=99 
ON IDXfg"
```

### Example 9

```python
A_INDEX_XML "with fillfactor=99 
ON XMLfg"
```

### Example 10

```python
A_INDEX_RASTER "with fillfactor=99 
ON RASfg"
```

### Example 11

```python
A_STORAGE "ON ADDS_FG"
```

### Example 12

```python
D_INDEX_ALL "with fillfactor=99 
ON Deletes_fg"
```

### Example 13

```python
D_INDEX_DELETED_AT "with fillfactor=80
 ON Deletes_fg"
```

### Example 14

```python
D_STORAGE "ON Deletes_fg"
```

### Example 15

```python
AUX_INDEX_COMPOSITE	"WITH FILLFACTOR= 90 
ON AUX_FG"
```

### Example 16

```python
AUX_STORAGE	"ON AUX_FG"
```

### Example 17

```python
BLK_INDEX_COMPOSITE	"WITH FILLFACTOR = 95 
ON BLK_FG"
```

### Example 18

```python
BLK_STORAGE	"ON BLK_FG"
```

### Example 19

```python
BND_INDEX_COMPOSITE	"WITH FILLFACTOR =90 
ON BND_FG"
```

### Example 20

```python
BND_INDEX_ID	"WITH FILLFACTOR = 90 
ON BND_FG"
```

### Example 21

```python
BND_STORAGE " ON BND_FG"
```

### Example 22

```python
RAS_INDEX_ID	"WITH FILLFACTOR = 85 ON RAS_FG"
```

### Example 23

```python
RAS_STORAGE	" ON RAS_FG"
```

### Example 24

```python
ALTER TABLE data.dbo.mytable 
 ADD CONSTRAINT f4_pk PRIMARY KEY CLUSTERED (OBJECTID) 
 WITH FILLFACTOR=100  
 ON NEWIDXGRP
```

### Example 25

```python
ALTER TABLE data.dbo.mytable 
 ADD CONSTRAINT f4_pk PRIMARY KEY CLUSTERED (OBJECTID) 
 WITH FILLFACTOR=100  
 ON NEWIDXGRP
```

### Example 26

```python
ALTER TABLE date.dbo.mytable 
ADD CONSTRAINT r15_pk PRIMARY KEY CLUSTERED (OBJECTID) 
WITH FILLFACTOR=100
```

### Example 27

```python
ALTER TABLE date.dbo.mytable 
ADD CONSTRAINT r15_pk PRIMARY KEY CLUSTERED (OBJECTID) 
WITH FILLFACTOR=100
```

### Example 28

```python
SELECT * FROM ::fn_helpcollations()
```

### Example 29

```python
SELECT * FROM ::fn_helpcollations()
```

### Example 30

```python
XML_COLUMN_SCHEMA
XML_COLUMN_TYPE
XML_COLUMN_PRIMARY_IDX
XML_COLUMN_PATH_IDX 
XML_COLUMN_PROPERTY_IDX
XML_COLUMN_VALUE_IDX
```

### Example 31

```python
XML_DOC_INDEX
XML_DOC_STORAGE
XML_DOC_OUT_OF_ROW
```

### Example 32

```python
XML_IDX_CLUSTER_DOUBLE
XML_IDX_CLUSTER_ID
XML_IDX_CLUSTER_PK
XML_IDX_CLUSTER_TAG
XML_IDX_INDEX_DOUBLE
XML_IDX_INDEX_ID
XML_IDX_INDEX_PK
XML_IDX_INDEX_TAG
XML_IDX_STORAGE
XML_IDX_OUT_OF_ROW
```

### Example 33

```python
XML_IDX_FULLTEXT_CAT
XML_IDX_FULLTEXT_LANGUAGE
XML_IDX_FULLTEXT_TIMESTAMP
XML_IDX_FULLTEXT_UPDATE_METHOD
```

---

## Manage connections to enterprise geodatabases in SQL Server

## Code Samples

### Example 1

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp","ssgdb.sde","SQL_SERVER","sdept4","DATABASE_AUTH","sa","esayP@ss","SAVE_USERNAME","gisprod")
```

### Example 2

```python
import arcpy
arcpy.CreateDatabaseConnection_management ("c:\\temp","ssgdb.sde","SQL_SERVER","sdept4","DATABASE_AUTH","sa","esayP@ss","SAVE_USERNAME","gisprod")
```

### Example 3

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\ssgdb.sde")
```

### Example 4

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.ListUsers("c:\\temp\ssgdb.sde")
```

### Example 5

```python
[user(ClientName=u'PC4', ConnectionTime=datetime.datetime(2018, 10, 18, 8, 30, 19),
 ID=18, IsDirecConnection=True, Name=u'PUBLISHER1')]
[user(ClientName=u'PC25', ConnectionTime=datetime.datetime(2018, 10, 21, 14, 10, 43),
 ID=33, IsDirecConnection=True, Name=u'EDITOR2')]
[user(ClientName=u'PC11', ConnectionTime=datetime.datetime(2018, 10, 22, 9, 18, 26),
 ID=39, IsDirecConnection=True, Name=u'READER5')]
[user(ClientName=u'PCA2', ConnectionTime=datetime.datetime(2018, 10, 22, 11, 21, 2),
 ID=41, IsDirecConnection=True, Name=u'DBO')]
```

### Example 6

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\ssgdb.sde",33)
```

### Example 7

```python
##No need to import arcpy if you are running functions in the same Python window.
import arcpy

arcpy.DisconnectUser("c:\\temp\ssgdb.sde",33)
```

---

## Rebuild system table indexes

## Code Samples

### Example 1

```python
# Name: RSysIdxSqlServer.py
# Description: Rebuilds indexes on the sde_states, sde_state_lineages,
# and sde_mv_tables_modified tables in an enterprise geodatabase
# in SQL Server.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = SQL_SERVER
instance = sqlserver_instance_name
account_authentication = OPERATING_SYSTEM_AUTH
database = database_name


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, database
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, database)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 2

```python
# Name: RSysIdxSqlServer.py
# Description: Rebuilds indexes on the sde_states, sde_state_lineages,
# and sde_mv_tables_modified tables in an enterprise geodatabase
# in SQL Server.

# Import system modules
import sys
import arcpy
import os

# Provide connection information
platform = SQL_SERVER
instance = sqlserver_instance_name
account_authentication = OPERATING_SYSTEM_AUTH
database = database_name


# Set local variables
if os.name.lower() == "nt":
   slashsyntax = "\\"
   if os.environ.get("TEMP") == None:
      temp = "c:\\temp"
   else:
      temp = os.environ.get("TEMP")
else:
   slashsyntax = "/"
   if os.environ.get("TMP") == None:
      temp = "/usr/tmp"
   else:
      temp = os.environ.get("TMP")

Connection_File_Name = temp + slashsyntax + "connection.sde"

# Check for the .sde file and delete it if present
if os.path.exists(Connection_File_Name):
   os.remove(Connection_File_Name)

print ("Creating Database Connection File...")
# Create Database Connection File
# Usage: out_folder_path, out_name, database_platform, instance, account_authentication, database
arcpy.CreateDatabaseConnectionFile_management(temp, "connection.sde", platform, instance, account_authentication, database)

# Rebuild indexes on system tables
arcpy.RebuildIndexes_management(Connection_File_Name, "SYSTEM", "", "ALL")
print ("Rebuild Complete")
```

### Example 3

```python
0 22 * * 3 /usr/bin/rsysidxdb2.py
```

---

## Create a geodatabase in SQL Server

## Code Samples

### Example 1

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 2

```python
"""
Name: create_enterprise_gdb.py
Description: Provide connection information to a DBMS instance and create an enterprise geodatabase.
Type  create_enterprise_gdb.py -h or create_enterprise_gdb.py --help for usage
Author: Esri
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for 10.1 and higher releases")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', ''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("--auth", dest="Account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-U", dest="Dbms_admin", type="string", default="", help="DBMS administrator user")
parser.add_option ("-P", dest="Dbms_admin_pwd", type="string", default="", help="DBMS administrator password")
parser.add_option ("--schema", dest="Schema_type", type="choice", choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default="SDE_SCHEMA", help="Schema Type for SQL Server geodatabase, SDE or DBO. Default=SDE_SCHEMA")
parser.add_option ("-u", dest="Gdb_admin", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Gdb_admin_pwd", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("-t", dest="Tablespace", type="string", default="", help="Tablespace name")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")
parser.add_option ("--type", dest="Spatial_type", type="choice", choices=['ST_GEOMETRY', 'POSTGIS'], default="ST_GEOMETRY", help="Spatial Type for PostgreSQL geodatabase, ST_GEOMETRY or POSTGIS. Default=ST_GEOMETRY")

# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
	#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	database = options.Database.lower()	
	account_authentication = options.Account_authentication.upper()
	dbms_admin = options.Dbms_admin
	dbms_admin_pwd = options.Dbms_admin_pwd
	schema_type = options.Schema_type.upper()
	gdb_admin = options.Gdb_admin
	gdb_admin_pwd = options.Gdb_admin_pwd	
	tablespace = options.Tablespace
	license = options.Authorization_file
	spatial_type = options.Spatial_type.upper()
	
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)			
	
	if(database_type == "SQL_SERVER"):
		if(schema_type == "SDE_SCHEMA" and gdb_admin.lower() != "sde"):
			print("\n%s: error: %s\n" % (sys.argv[0], "To create SDE schema on SQL Server, geodatabase administrator must be SDE."))
			sys.exit(3)
		if (schema_type == "DBO_SCHEMA" and gdb_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring geodatabase administrator specified when creating DBO schema..."))
		if( account_authentication == "DATABASE_AUTH" and dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified with database authentication"))
			sys.exit(3)
		if( account_authentication == "OPERATING_SYSTEM_AUTH" and dbms_admin != ""):
			print("\nWarning: %s\n" % ("Ignoring DBMS administrator specified when using operating system authentication..."))	
	else:
		if (schema_type == "DBO_SCHEMA"):
			print("\nWarning: %s %s, %s\n" % ("Only SDE schema is supported on", database_type, "switching to SDE schema..." ))
			
		if( gdb_admin.lower() == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "Geodatabase administrator must be specified."))
			sys.exit(3)
	
		if( dbms_admin == ""):
			print("\n%s: error: %s\n" % (sys.argv[0], "DBMS administrator must be specified!"))
			sys.exit(3)

		if (account_authentication == "OPERATING_SYSTEM_AUTH"):
			print("Warning: %s %s, %s\n" % ("Only database authentication is supported on", database_type, "switching to database authentication..." ))

	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
		sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to create...")
		arcpy.AddMessage("+++++++++")
	
	
	try:
		print("Creating enterprise geodatabase...\n")
		arcpy.management.CreateEnterpriseGeodatabase(database_platform=database_type,instance_name=instance, database_name=database, account_authentication=account_authentication, database_admin=dbms_admin, database_admin_password=dbms_admin_pwd, sde_schema=schema_type, gdb_admin_name=gdb_admin, gdb_admin_password=gdb_admin_pwd, tablespace_name=tablespace, authorization_file=license, spatial_type=spatial_type)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()   
		parser.exit(2)
```

### Example 3

```python
create_gdb.py --DBMS SQL_SERVER -i porthos\gisprod -D entgdb --auth DATABASE_AUTH 
-U sa -P N0pe3king! --schema SDE_SCHEMA -u sde -p Tgdbst@rtsh3r3 -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 4

```python
create_gdb.py --DBMS SQL_SERVER -i porthos\gisprod -D entgdb --auth DATABASE_AUTH 
-U sa -P N0pe3king! --schema SDE_SCHEMA -u sde -p Tgdbst@rtsh3r3 -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 5

```python
create_gdb.py --DBMS SQL_SERVER -i porthos\gisprod -D entgdb --auth OPERATING_SYSTEM_AUTH 
--schema DBO_SCHEMA -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 6

```python
create_gdb.py --DBMS SQL_SERVER -i porthos\gisprod -D entgdb --auth OPERATING_SYSTEM_AUTH 
--schema DBO_SCHEMA -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 7

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 8

```python
"""
Name: enable_enterprise_gdb.py
Description: Provide connection information to an enterprise database
and enable enterprise geodatabase.
Type enable_enterprise_gdb.py -h or enable_enterprise_gdb.py --help for usage
"""

# Import system modules
import arcpy, os, optparse, sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 1.0 for " + arcpy.GetInstallInfo()['Version'] )

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQL_SERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS', ''], default="", help="Type of enterprise DBMS:  SQL_SERVER, ORACLE, POSTGRESQL, DB2, INFORMIX, or DB2ZOS.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase  administrator password")
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")
parser.add_option ("-l", dest="Authorization_file", type="string", default="", help="Full path and name of authorization file")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)
	

	#Usage parameters for spatial database connection
	database_type = options.Database_type.upper()
	instance = options.Instance
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	database = options.Database.lower()
	license = options.Authorization_file


	if( database_type ==""):	
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "DBMS type (--DBMS) must be specified."))
		parser.print_help()
		sys.exit(3)		
		
	if (license == ""):
		print(" \n%s: error: \n%s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)

		
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	if (license == ""):
		print(" \n%s: error: %s\n" % (sys.argv[0], "Authorization file (-l) must be specified."))
		parser.print_help()
		sys.exit(3)
	
	# Checks required license level
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enabling enterprise geodatabase functionality requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before enabling an enterprise geodatabase.")
	else:
		print("\n" + product_license + " license available!  Continuing to enable...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username    
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	

	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")	
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
	for i in range(arcpy.GetMessageCount()):

                if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("\n+++++++++")

                        arcpy.AddMessage("Exiting!!")

                        arcpy.AddMessage("+++++++++\n")

                        sys.exit(3)

                else:

                        arcpy.AddReturnMessage(i)

                        arcpy.AddMessage("+++++++++\n")
	
	# Process: Enable geodatabase...
	try:
		print("Enabling Enterprise Geodatabase...\n")
		arcpy.EnableEnterpriseGeodatabase_management(input_database=Connection_File_Name_full_path, authorization_file=license)
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		arcpy.AddMessage("+++++++++\n")
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
			
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
			
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help() 
		parser.exit(2)
```

### Example 9

```python
enable_gdb.py --DBMS SQL_SERVER -i ssprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

### Example 10

```python
enable_gdb.py --DBMS SQL_SERVER -i ssprod --auth DATABASE_AUTH 
-u sde -p Tgdbst@rtsh3r3 -D spdata -l '\\Program Files\ESRI\License\sysgen\keycodes'
```

---

## Update database statistics

## Code Samples

### Example 1

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

### Example 2

```python
# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")
```

---

## Upgrade an enterprise geodatabase in SQL Server

## Code Samples

### Example 1

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "SQL_SERVER",
                                          "prod9",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME",
                                          "myssgdb")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 2

```python
# Open Python.
cd /arcgis/server/tools
./python

# Create a connection to the geodatabase.
arcpy.CreateDatabaseConnection_management("/tmp/",
                                          "egdb_connection.sde",
                                          "SQL_SERVER",
                                          "prod9",
                                          "DATABASE_AUTH",
                                          "sde",
                                          "mysdepassword",
                                          "SAVE_USERNAME",
                                          "myssgdb")

# Import ArcPy and check the geodatabase release.
import arcpy

isCurrent = arcpy.Describe('/tmp/egdb_connection.sde').currentRelease

print isCurrent
```

### Example 3

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 4

```python
# Name: upgradesdegdb_example.py
# Description: Connect from a Windows computer 
# with an existing database connection file 
# and upgrade an enterprise geodatabase

# Import arcpy module
import arcpy
 
# Local variables:
Output_Workspace = "C:\\ArcGIS\connection_files\<Connection file>"
Default_gdb = "C:\\ArcGIS\connection_files\<Connection file>"

# Process: Upgrade Geodatabase
arcpy.UpgradeGDB_management(Default_gdb, "PREREQUISITE_CHECK", "UPGRADE")
```

### Example 5

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

### Example 6

```python
"""
Name: upgrade_gdb.py
Description: Provide connection information to an Enterprise geodatabase 
and upgrade the geodatabase
Type upgrade_gdb.py -h or upgrade_gdb.py --help for usage
"""

# Import system modules
import arcpy
import os
import optparse
import sys


# Define usage and version
parser = optparse.OptionParser(usage = "usage: %prog [Options]", version="%prog 2.0; valid for 10.1 only")

#Define help and options
parser.add_option ("--DBMS", dest="Database_type", type="choice", choices=['SQLSERVER', 'ORACLE', 'POSTGRESQL', 'DB2','INFORMIX','DB2ZOS',''], default="", help="Type of enterprise DBMS:  SQLSERVER, ORACLE, or POSTGRESQL.")
parser.add_option ("-i", dest="Instance", type="string", default="", help="DBMS instance name")
parser.add_option ("--auth", dest="account_authentication", type ="choice", choices=['DATABASE_AUTH', 'OPERATING_SYSTEM_AUTH'], default='DATABASE_AUTH', help="Authentication type options (case-sensitive):  DATABASE_AUTH, OPERATING_SYSTEM_AUTH.  Default=DATABASE_AUTH")
parser.add_option ("-u", dest="User", type="string", default="", help="Geodatabase administrator user name")
parser.add_option ("-p", dest="Password", type="string", default="", help="Geodatabase administrator password")
parser.add_option ("--upgrade", dest="Upgrade", type="choice", choices=['TRUE', 'FALSE'], default="FALSE", help="Upgrade Options (case-sensitive):  TRUE=Perform Pre-requisite check and upgrade geodatabase, FALSE=Perform Pre-requisite check only.  Default=FALSE")                   
parser.add_option ("-D", dest="Database", type="string", default="none", help="Database name:  Not required for Oracle")


# Check if value entered for option
try:
	(options, args) = parser.parse_args()

	
#Check if no system arguments (options) entered
	if len(sys.argv) == 1:
		print("%s: error: %s\n" % (sys.argv[0], "No command options given"))
		parser.print_help()
		sys.exit(3)

	#Usage parameters for spatial database connection to upgrade
	account_authentication = options.account_authentication.upper()
	username = options.User.lower() 
	password = options.Password	
	do_upgrade = options.Upgrade
	database = options.Database.lower()
	database_type = options.Database_type.upper()
	instance = options.Instance
	
	if (database_type == ""):
		print("\nDatabase type must be specified!\n")
		parser.print_help()
		sys.exit(3)
	
	if (database_type == "SQLSERVER"):
		database_type = "SQL_SERVER"
	
	# Get the current product license
	product_license=arcpy.ProductInfo()
	
	# Checks required license level to upgrade
	if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
		print("\n" + product_license + " license found!" + "  Enterprise geodatabase upgrade requires an ArcGIS Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS Server license.")
		sys.exit("Re-authorize ArcGIS before upgrading.")
	else:
		print("\n" + product_license + " license available!  Continuing to upgrade...")
		arcpy.AddMessage("+++++++++")
	
	# Local variables
	instance_temp = instance.replace("\\","_")
	instance_temp = instance_temp.replace("/","_")
	instance_temp = instance_temp.replace(":","_")
	Conn_File_NameT = instance_temp + "_" + database + "_" + username     
	
	if os.environ.get("TEMP") == None:
		temp = "c:\\temp"	
	else:
		temp = os.environ.get("TEMP")
	
	if os.environ.get("TMP") == None:
		temp = "/usr/tmp"		
	else:
		temp = os.environ.get("TMP")  
	
	Connection_File_Name = Conn_File_NameT + ".sde"
	Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"
	
	# Check for the .sde file and delete it if present
	arcpy.env.overwriteOutput=True
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
	print("\nCreating Database Connection File...\n")
	# Process: Create Database Connection File...
	# Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, database, account_authentication, username, password, save_username_password(must be true)
	arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=username, password=password, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
		if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("\n+++++++++")
			arcpy.AddMessage("Exiting!!")
			arcpy.AddMessage("+++++++++\n")
			sys.exit(3)            
		else:
			arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
			
	# Check whether geodatabase needs upgrade
	isCurrent = arcpy.Describe(Connection_File_Name_full_path).currentRelease
	
	if isCurrent == True:
		print("The geodatabase is already at the current release and cannot be upgraded!")
		sys.exit("Upgrade did not run.")
	
	
	# Process: Upgrade geodatabase...
	try:
		if do_upgrade.lower() == "true":
			print("Upgrading Geodatabase...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
	
		else:
			print("Running Pre-Requisite Check...\n")
			arcpy.UpgradeGDB_management(input_workspace=Connection_File_Name_full_path, input_prerequisite_check="PREREQUISITE_CHECK", input_upgradegdb_check="NO_UPGRADE")
			for i in range(arcpy.GetMessageCount()):
				arcpy.AddReturnMessage(i)
			arcpy.AddMessage("+++++++++\n")
		
	        
	except:
		for i in range(arcpy.GetMessageCount()):
			arcpy.AddReturnMessage(i)
		
	if os.path.exists(Connection_File_Name_full_path):
		os.remove(Connection_File_Name_full_path)
	
#Check if no value entered for option	
except SystemExit as e:
	if e.code == 2:
		parser.usage = ""
		print("\n")
		parser.print_help()
		parser.exit(2)
```

---

## Use the fields view

## Code Samples

### Example 1

```python
import arcpy

# For each field in the Buildings feature class, print
# the field name, type, and precision.
fields = arcpy.ListFields("c:/data/campus.gdb/Buildings")

for field in fields:
    print(field.name, field.type, field.precision)
```

### Example 2

```python
import arcpy

# For each field in the Buildings feature class, print
# the field name, type, and precision.
fields = arcpy.ListFields("c:/data/campus.gdb/Buildings")

for field in fields:
    print(field.name, field.type, field.precision)
```

---

## Attribute rule dictionary keywords

## Code Samples

### Example 1

```python
return {
    //result is a single value
    //set the attribute rule target field to 200 for $feature
    'result': 200
}
```

### Example 2

```python
return {
    //result is a single value
    //set the attribute rule target field to 200 for $feature
    'result': 200
}
```

### Example 3

```python
return {
    //result is a dictionary
    //set 'field1', 'field2', and the geometry for $feature
    //ArcGIS Pro 2.7 or ArcGIS Enterprise 10.9 and later
    "result": {
        "attributes": {
            "field1": 'field1', //updates field1 in the $feature 
            "field2": 11 //updates field2 in the $feature 
        },
        "geometry": Rotate($feature) //updates geometry in $feature
    }

}
```

### Example 4

```python
return {
    //result is a dictionary
    //set 'field1', 'field2', and the geometry for $feature
    //ArcGIS Pro 2.7 or ArcGIS Enterprise 10.9 and later
    "result": {
        "attributes": {
            "field1": 'field1', //updates field1 in the $feature 
            "field2": 11 //updates field2 in the $feature 
        },
        "geometry": Rotate($feature) //updates geometry in $feature
    }

}
```

### Example 5

```python
return {
    "errorMessage": "Error message text"
}
```

### Example 6

```python
return {
    "errorMessage": "Error message text"
}
```

### Example 7

```python
return {
    'calculationRequired': [{
        'classname': 'featureclass_name',
        'globalIDs': ['{8B421724-32D0-408A-A8EE-CCC2B064D52B}']
    }]
}
```

### Example 8

```python
return {
    'calculationRequired': [{
        'classname': 'featureclass_name',
        'globalIDs': ['{8B421724-32D0-408A-A8EE-CCC2B064D52B}']
    }]
}
```

### Example 9

```python
return {
    'validationRequired': [{
        'classname': 'featureclass_name',
        'globalIDs': ['{60905A3D-9783-435D-B4C9-AA4ADA59AD32}']
    }]
}
```

### Example 10

```python
return {
    'validationRequired': [{
        'classname': 'featureclass_name',
        'globalIDs': ['{60905A3D-9783-435D-B4C9-AA4ADA59AD32}']
    }]
}
```

### Example 11

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
        'adds': [{
            'attributes': {
                'field_name': 11
            },
            'geometry': Geometry({
                'x': -76.8375008,
                'y': 39.4949383,
                'spatialReference': {
                    'wkid': 4326
                }
            })
        }]
    }]
}
```

### Example 12

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
        'adds': [{
            'attributes': {
                'field_name': 11
            },
            'geometry': Geometry({
                'x': -76.8375008,
                'y': 39.4949383,
                'spatialReference': {
                    'wkid': 4326
                }
            })
        }]
    }]
}
```

### Example 13

```python
"edit": [{
    "className": "ElectricDistributionJunctionObject",
    "adds": [{ //adds a new Electric Distribution Junction Object and creates a midspan association to the $feature
        "percentAlong": 0.5,
        "associationType": 'midspan'
    }]
}]
}
```

### Example 14

```python
"edit": [{
    "className": "ElectricDistributionJunctionObject",
    "adds": [{ //adds a new Electric Distribution Junction Object and creates a midspan association to the $feature
        "percentAlong": 0.5,
        "associationType": 'midspan'
    }]
}]
}
```

### Example 15

```python
//$feature is an edge object in the utility network
//Arcade will add two junction objects and associate them to the $feature
//The junction object with asset group 5 and asset type 1 has a terminal configuration of High/Low
return {
    "result": $feature.assetid,
    "edit": [{
        "className": "ElectricDistributionJunctionObject",
        "adds": [{
            "attributes": { //Adds a junction object
                "assetgroup": 5,
                "assettype": 1
            }, //create a connectivity association between the $feature and junction object
            "toTerminal": "High", //to the high side terminal of the junction object
            "associationType": "junctionEdgeFrom" //on the from side of the edge object
        }, {
            "attributes": { //Adds a junction object
                "assetgroup": 5,
                "assettype": 1
            }, //create a connectivity association between the $feature and junction object
            "toTerminal": "High", //to the high side terminal of the junction object
            "associationType": "junctionEdgeTo" //on the to side of the edge object
        }]
    }]
}
```

### Example 16

```python
//$feature is an edge object in the utility network
//Arcade will add two junction objects and associate them to the $feature
//The junction object with asset group 5 and asset type 1 has a terminal configuration of High/Low
return {
    "result": $feature.assetid,
    "edit": [{
        "className": "ElectricDistributionJunctionObject",
        "adds": [{
            "attributes": { //Adds a junction object
                "assetgroup": 5,
                "assettype": 1
            }, //create a connectivity association between the $feature and junction object
            "toTerminal": "High", //to the high side terminal of the junction object
            "associationType": "junctionEdgeFrom" //on the from side of the edge object
        }, {
            "attributes": { //Adds a junction object
                "assetgroup": 5,
                "assettype": 1
            }, //create a connectivity association between the $feature and junction object
            "toTerminal": "High", //to the high side terminal of the junction object
            "associationType": "junctionEdgeTo" //on the to side of the edge object
        }]
    }]
}
```

### Example 17

```python
return { //creates two new Structure Junction Objects and creates an association between them using a tag
    "edit": [{
        //create two junction objects and identify them uniquely with a tag
        "className": "StructureJunctionObject",
        "adds": [{
            "tag": "jo1", //unique identifier for new feature in the Structure Junction Object class
            "attributes": {
                "AssetGroup": 1,
                "AssetType": 2
            }
        }, {
            "tag": "jo2", //unique identifier for new feature in the Structure Junction Object class
            "attributes": {
                "AssetGroup": 1,
                "AssetType": 2
            }
        }]
    }, {
        "className": "^UN_Association", //edit the association table and create an attachment association between the new junction objects
        "adds": [{
            "fromClass": "StructureJunctionObject",
            "fromGlobalId": "jo1.globalID",
            "toClass": "StructureJunctionObject",
            "toGlobalId": "jo2.globalID",
            "associationType": "attachment"
        }]
    }]
}
```

### Example 18

```python
return { //creates two new Structure Junction Objects and creates an association between them using a tag
    "edit": [{
        //create two junction objects and identify them uniquely with a tag
        "className": "StructureJunctionObject",
        "adds": [{
            "tag": "jo1", //unique identifier for new feature in the Structure Junction Object class
            "attributes": {
                "AssetGroup": 1,
                "AssetType": 2
            }
        }, {
            "tag": "jo2", //unique identifier for new feature in the Structure Junction Object class
            "attributes": {
                "AssetGroup": 1,
                "AssetType": 2
            }
        }]
    }, {
        "className": "^UN_Association", //edit the association table and create an attachment association between the new junction objects
        "adds": [{
            "fromClass": "StructureJunctionObject",
            "fromGlobalId": "jo1.globalID",
            "toClass": "StructureJunctionObject",
            "toGlobalId": "jo2.globalID",
            "associationType": "attachment"
        }]
    }]
}
```

### Example 19

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
        'updates': [{
            'globalID': '{7EBAB596-E9DB-40D8-9756-B2EBED2500B7}',
            'attributes': {
                'field_name': 22
            }
        }]
    }]
}
```

### Example 20

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
        'updates': [{
            'globalID': '{7EBAB596-E9DB-40D8-9756-B2EBED2500B7}',
            'attributes': {
                'field_name': 22
            }
        }]
    }]
}
```

### Example 21

```python
return {
    "result": $feature.assetid,
    "edit": [{
        "className": "electricdistributionassembly",
        "updates": [{
            "objectID": feature_objectid,
            "associationType": 'container'
        }]
    }]
}
```

### Example 22

```python
return {
    "result": $feature.assetid,
    "edit": [{
        "className": "electricdistributionassembly",
        "updates": [{
            "objectID": feature_objectid,
            "associationType": 'container'
        }]
    }]
}
```

### Example 23

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
          'deletes': [{
            'objectID': 22
        }]
    }]
}
```

### Example 24

```python
return {
    'edit': [{
        'className': 'b_edit_dict',
          'deletes': [{
            'objectID': 22
        }]
    }]
}
```

---

## Attribute rule script expression examples

## Code Samples

### Example 1

```python
return "Tx-" + NextSequenceValue ('assetid_seq')
```

### Example 2

```python
return "Tx-" + NextSequenceValue ('assetid_seq')
```

### Example 3

```python
return "Tx-" + NextSequenceValue ('map.assetid_seq')
```

### Example 4

```python
return "Tx-" + NextSequenceValue ('map.assetid_seq')
```

### Example 5

```python
//On Insert or Update, set FacilityID = SubstationName - AssetID use intersect to get the substation name
//If no substation (fail with error message dictionary,  must create in substation.) 
var fsStructureBoundary =  FeatureSetByName($datastore, "Substation", ["name"], true)
var fsSubstation = Intersects(fsStructureBoundary, Geometry($feature))
var substation = First (fsSubstation)

var subname  = ""
if (substation == null)
   return  {"errorMessage": "Transformers must be created in a substation."}
else 
   subname =  substation.name

return subname + " - " + $feature.assetid;
```

### Example 6

```python
//On Insert or Update, set FacilityID = SubstationName - AssetID use intersect to get the substation name
//If no substation (fail with error message dictionary,  must create in substation.) 
var fsStructureBoundary =  FeatureSetByName($datastore, "Substation", ["name"], true)
var fsSubstation = Intersects(fsStructureBoundary, Geometry($feature))
var substation = First (fsSubstation)

var subname  = ""
if (substation == null)
   return  {"errorMessage": "Transformers must be created in a substation."}
else 
   subname =  substation.name

return subname + " - " + $feature.assetid;
```

### Example 7

```python
//Updating the substation name marks its transformers as requiring calculation and updates the yearName to the new name and year. 
//To recalculate the facility id on all transformers, mark all associated transformers as requiring calculation.
var fsDevice =  FeatureSetByName($datastore, "Transformer", ["globalid"], false)
var fsDeviceIntersects = Intersects (fsDevice, Geometry($feature))

var transformers = [];
var count = 0;

for (var i in fsDeviceIntersects)
   transformers[count++] = i.globalid;
var newName = $feature.name + " " + Year(Now())
return {
   'result': newName, 
   'calculationRequired': 
       [
          {
              'className':"Transformer",
              'globalIDs': transformers
           }
       ]
   }
```

### Example 8

```python
//Updating the substation name marks its transformers as requiring calculation and updates the yearName to the new name and year. 
//To recalculate the facility id on all transformers, mark all associated transformers as requiring calculation.
var fsDevice =  FeatureSetByName($datastore, "Transformer", ["globalid"], false)
var fsDeviceIntersects = Intersects (fsDevice, Geometry($feature))

var transformers = [];
var count = 0;

for (var i in fsDeviceIntersects)
   transformers[count++] = i.globalid;
var newName = $feature.name + " " + Year(Now())
return {
   'result': newName, 
   'calculationRequired': 
       [
          {
              'className':"Transformer",
              'globalIDs': transformers
           }
       ]
   }
```

### Example 9

```python
var fsAddress = FeatureSetByName($datastore, "Address_pnts", ["globalid"], false)
var fsListAddpnts = Intersects(fsAddress, $feature)
var AddList = []
var counter = 0
var noAddress = Count(fsListAddpnts)
if (noAddress > 0) {
    for (var address in fsListAddpnts) {
        AddList[counter] = {
            'globalid': address.globalid,
            'attributes': {
                'add_district_name': $feature.DistrictName
            }
        }
        counter++
    }
    return {
        'result': noAddress + ' addresses found in the district.',
        'edit': [{
            'className': 'Address_pnts',
            'updates': AddList
        }]
    }
} else {
    return 'No address points in district.'
}
```

### Example 10

```python
var fsAddress = FeatureSetByName($datastore, "Address_pnts", ["globalid"], false)
var fsListAddpnts = Intersects(fsAddress, $feature)
var AddList = []
var counter = 0
var noAddress = Count(fsListAddpnts)
if (noAddress > 0) {
    for (var address in fsListAddpnts) {
        AddList[counter] = {
            'globalid': address.globalid,
            'attributes': {
                'add_district_name': $feature.DistrictName
            }
        }
        counter++
    }
    return {
        'result': noAddress + ' addresses found in the district.',
        'edit': [{
            'className': 'Address_pnts',
            'updates': AddList
        }]
    }
} else {
    return 'No address points in district.'
}
```

### Example 11

```python
//This calculation attribute rule is added to the shape field of a point feature class called pointClass2
var centerFeature = First(FeatureSetByName($datastore, "pointClass1"))
//Get the x and y values of the feature in the pointClass1
var x0 = Geometry(centerFeature).x
var y0 = Geometry(centerFeature).y
//Get the x and y values of the current feature in the pointClass2
var x1 = Geometry($feature).x;
var y1 = Geometry($feature).y;
var x2 = 0;
var y2 = 0;
var d = 5
//Calculate the Euclidean distance from feature in pointClass1 and current feature in pointClass2
var d1 = sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))

//Calculate the new x and y to be within 5 metric units while maintaining slope
x2 = (x1 - x0) * d / d1 + x0;
y2 = (y1 - y0) * d / d1 + y0;
//Create a point geometry from the new x and y values
var pointA = Point({
    "x": x2,
    "y": y2,
    "z": 0,
    "spatialReference": Geometry(centerFeature).spatialReference
});
return pointA
```

### Example 12

```python
//This calculation attribute rule is added to the shape field of a point feature class called pointClass2
var centerFeature = First(FeatureSetByName($datastore, "pointClass1"))
//Get the x and y values of the feature in the pointClass1
var x0 = Geometry(centerFeature).x
var y0 = Geometry(centerFeature).y
//Get the x and y values of the current feature in the pointClass2
var x1 = Geometry($feature).x;
var y1 = Geometry($feature).y;
var x2 = 0;
var y2 = 0;
var d = 5
//Calculate the Euclidean distance from feature in pointClass1 and current feature in pointClass2
var d1 = sqrt((x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0))

//Calculate the new x and y to be within 5 metric units while maintaining slope
x2 = (x1 - x0) * d / d1 + x0;
y2 = (y1 - y0) * d / d1 + y0;
//Create a point geometry from the new x and y values
var pointA = Point({
    "x": x2,
    "y": y2,
    "z": 0,
    "spatialReference": Geometry(centerFeature).spatialReference
});
return pointA
```

### Example 13

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature. 

Var fs = FeatureSetByName($datastore, “Inspection”, [“comments”], false)
Var poleGuid = $feature.poleguid 
Var fsinspected = Filter(fs, “POLEGUID= @poleguid”);
Return count(fsinspected)
```

### Example 14

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature. 

Var fs = FeatureSetByName($datastore, “Inspection”, [“comments”], false)
Var poleGuid = $feature.poleguid 
Var fsinspected = Filter(fs, “POLEGUID= @poleguid”);
Return count(fsinspected)
```

### Example 15

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipName($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 16

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipName($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 17

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipClass ($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 18

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipClass ($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 19

```python
//A calculation rule that triggers on an update event when the pole comment field is edited. 
//The expression first checks if the comment field changed and creates a new related record.

If ($originalfeature.comment != $feature.comment)
{ 
    Return {
                 “edit”: [{
   “className”: “inspection”,
   “adds”: [{ “attributes”: { “comments”: $feature.comment } }] 
}] 

}
Return;
```

### Example 20

```python
//A calculation rule that triggers on an update event when the pole comment field is edited. 
//The expression first checks if the comment field changed and creates a new related record.

If ($originalfeature.comment != $feature.comment)
{ 
    Return {
                 “edit”: [{
   “className”: “inspection”,
   “adds”: [{ “attributes”: { “comments”: $feature.comment } }] 
}] 

}
Return;
```

### Example 21

```python
if ($feature.name == null)
    return false;
else
    return true;

//another way of writing it
return !($feature.name == null)
```

### Example 22

```python
if ($feature.name == null)
    return false;
else
    return true;

//another way of writing it
return !($feature.name == null)
```

### Example 23

```python
if ($feature.name == null)
    return   {"errorMessage": "Substation must have a valid name."}
else if ($feature.installationDate == null)
    return   {"errorMessage": "Substation must have a valid installation date."}
else
    return true;
```

### Example 24

```python
if ($feature.name == null)
    return   {"errorMessage": "Substation must have a valid name."}
else if ($feature.installationDate == null)
    return   {"errorMessage": "Substation must have a valid installation date."}
else
    return true;
```

### Example 25

```python
if ($feature.lifecyclestatus == 'retired')
{
  return true;
}
return {'errorMessage': 'You are not allowed delete a feature until it is retired'};
```

### Example 26

```python
if ($feature.lifecyclestatus == 'retired')
{
  return true;
}
return {'errorMessage': 'You are not allowed delete a feature until it is retired'};
```

### Example 27

```python
var fsTransformer =  FeatureSetByName($datastore, "L1Electric_Distribution_Device", ["objectid"], true)
var fsTransformerSubset = Intersects(fsTransformer, Geometry($feature))
var totalKva = 0;
for (var t in fsTransformerSubset)
    totalKva += t.kva

if (totalKva > $feature.maxKva)
     return false
else
     return true
```

### Example 28

```python
var fsTransformer =  FeatureSetByName($datastore, "L1Electric_Distribution_Device", ["objectid"], true)
var fsTransformerSubset = Intersects(fsTransformer, Geometry($feature))
var totalKva = 0;
for (var t in fsTransformerSubset)
    totalKva += t.kva

if (totalKva > $feature.maxKva)
     return false
else
     return true
```

### Example 29

```python
if ($feature.structureheight >= 65)
{
    If (DomainName($feature, 'Material') == 'Steel')
    { return true; }
    else
    { return false; }
}
Else
{  return true; }
```

### Example 30

```python
if ($feature.structureheight >= 65)
{
    If (DomainName($feature, 'Material') == 'Steel')
    { return true; }
    else
    { return false; }
}
Else
{  return true; }
```

### Example 31

```python
if ($feature.field == $originalfeature.field) {
    //code if field attribute hasn't changed
} else {
    //code if field attribute has changed.
}
```

### Example 32

```python
if ($feature.field == $originalfeature.field) {
    //code if field attribute hasn't changed
} else {
    //code if field attribute has changed.
}
```

### Example 33

```python
if (Equals(Geometry($feature), Geometry($originalfeature))) {
    //code if geometry hasn't changed
} else {
    //code if geometry has changed
}
```

### Example 34

```python
if (Equals(Geometry($feature), Geometry($originalfeature))) {
    //code if geometry hasn't changed
} else {
    //code if geometry has changed
}
```

### Example 35

```python
if ($originalfeature.field == 0) {
    //code to avoid calculating change if $originalfeature.field was zero
} else {
    var percent_change = Abs(($feature.field - $originalfeature.field) / $originalfeature.field) * 100
    if (percent_change >= 50) {
        //code if percent change is by 50% or more
    } else {
        //code if percent change is less than 50%
    }
}
```

### Example 36

```python
if ($originalfeature.field == 0) {
    //code to avoid calculating change if $originalfeature.field was zero
} else {
    var percent_change = Abs(($feature.field - $originalfeature.field) / $originalfeature.field) * 100
    if (percent_change >= 50) {
        //code if percent change is by 50% or more
    } else {
        //code if percent change is less than 50%
    }
}
```

### Example 37

```python
if ($editContext.editType == "INSERT") {
    //code if the edit is an insert
} else if ($editContext.editType == "UPDATE") {
    //code if the edit is an update
} else if ($editContext.editType == "DELETE") {
    //code if the edit is a delete 
} else if ($editContext.editType == "NA") {
    //code when edit type is not applicable, for example batch calculation or validation rules
}
```

### Example 38

```python
if ($editContext.editType == "INSERT") {
    //code if the edit is an insert
} else if ($editContext.editType == "UPDATE") {
    //code if the edit is an update
} else if ($editContext.editType == "DELETE") {
    //code if the edit is a delete 
} else if ($editContext.editType == "NA") {
    //code when edit type is not applicable, for example batch calculation or validation rules
}
```

---

## Attribute rules and relationship classes

## Code Samples

### Example 1

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature. 

Var fs = FeatureSetByName($datastore, “Inspection”, [“comments”], false)
Var poleGuid = $feature.poleguid 
Var fsinspected = Filter(fs, “POLEGUID= @poleguid”);
Return count(fsinspected)
```

### Example 2

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature. 

Var fs = FeatureSetByName($datastore, “Inspection”, [“comments”], false)
Var poleGuid = $feature.poleguid 
Var fsinspected = Filter(fs, “POLEGUID= @poleguid”);
Return count(fsinspected)
```

### Example 3

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipName($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 4

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipName($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 5

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipClass ($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 6

```python
//A calculation rule that returns the count of a pole inspection records.
//When a pole feature is updated, the calculation rule reads all its related inspections records from the comments field and returns the total inspection count for that feature.

Var fsinspected = FeatureSetByRelationshipClass ($feature, “pole_inspection”, [“comments”], false)
Return count(fsinspected)
```

### Example 7

```python
//A calculation rule that triggers on an update event when the pole comment field is edited. 
//The expression first checks if the comment field changed and creates a new related record.

If ($originalfeature.comment != $feature.comment)
{ 
    Return {
                 “edit”: [{
   “className”: “inspection”,
   “adds”: [{ “attributes”: { “comments”: $feature.comment } }] 
}] 

}
Return;
```

### Example 8

```python
//A calculation rule that triggers on an update event when the pole comment field is edited. 
//The expression first checks if the comment field changed and creates a new related record.

If ($originalfeature.comment != $feature.comment)
{ 
    Return {
                 “edit”: [{
   “className”: “inspection”,
   “adds”: [{ “attributes”: { “comments”: $feature.comment } }] 
}] 

}
Return;
```

### Example 9

```python
//A validation rule that ensures each pole passes one or more inspections.

var fsInspections = FeatureSetByRelationshipClass($feature, "poles");
if (count(fsInspections) == 0) return false;
return true;
```

### Example 10

```python
//A validation rule that ensures each pole passes one or more inspections.

var fsInspections = FeatureSetByRelationshipClass($feature, "poles");
if (count(fsInspections) == 0) return false;
return true;
```

### Example 11

```python
//A validation rule that ensures each pole has one or fewer inspections.

var fsInspections = FeatureSetByRelationshipClass($feature, "poles");
if (count(fsInspections) > 1 ) return false;
return true;
```

### Example 12

```python
//A validation rule that ensures each pole has one or fewer inspections.

var fsInspections = FeatureSetByRelationshipClass($feature, "poles");
if (count(fsInspections) > 1 ) return false;
return true;
```

---

## Automate reconcile and post operations for sync-enabled branch versioned data

## Code Samples

### Example 1

```python
# Import modules
import arcpy, traceback, urllib, json, urllib.request, urllib.parse, os, urllib.error, datetime

# Overwrite the reconcile log output each time the script is run
arcpy.env.overwriteOutput = True

# Script parameters
serviceName = "MyServiceName"
baseURL = "https://MyServer.MyDomain.com"
portalAdmin = "MyAdminUser"
portalAdminPwd = "MyAdmin.Password"
logFileScript = "C:/Logs/validateRecPostScriptLog.txt"
logfileOutputRecPost = 'C:/Logs/reconcile_log.txt' 

# Choose to output a log file for the script
outputScriptReport = True

# Define functions
def openURL(url, params=None):
    """This function used to open a URL and returns the json response"""
    try:
        request_params = {'f':'pjson'}
        if params:
            request_params.update(params)
        encodedParams = urllib.parse.urlencode(request_params)
        request = urllib.request.urlopen(url, encodedParams.encode('UTF-8'))
        response = request.read()
        json_response = json.loads(response)
        return json_response
    except:
        print (traceback.format_exc())

def versionInfo(versionOwner=""):
    """This function queries the versions owned by the versionOwner.
    It returns a list of dictionaries."""
    vmsUrlinfo = "{}/server/rest/services/{}/VersionManagementServer/versionInfos?&ownerFilter={}&includeHidden=&f=json&token={}".format(baseURL, serviceName, versionOwner, token)
    response = openURL(vmsUrlinfo)
    if response['success'] == True:
        versionsDict = response['versions']
        return versionsDict
    else:
        return("Unable to get version info")

def evaluateUrl(validationUrl, validate_params):
    """This function runs evaluate on the validation server
    It returns the json response."""
    evalJsonResp = openURL(validationUrl, validate_params)
    if evalJsonResp['success'] == False:
        return [False, evalJsonResp]
    else:
        return [True, evalJsonResp]

def generateMessage(msg, print_statement=True):
    """This function generates messages as the script runs. If print_statement
    is set to True, print to the screen. If outputScriptReport is set to true,
    write the message to the logfile"""
    if outputScriptReport == True:
        with open(logFileScript, 'a') as log_file:
            log_file.write(msg + "\n")
    if print_statement == True:
        print(msg)

def recPostVersions(versionList, post):
    """This function runs the Reconcile Versions GP tool to reconcile
    and optionally post to the feature service"""
    if post == True:
        postVersion = "POST"
    elif post == False:
        postVersion = "NO_POST"
    # Reconcile and post the replica versions 
    # This tool is set to abort if there are conflicts and detects conflicts by object
    arcpy.management.ReconcileVersions(featureService,
                                        'ALL_VERSIONS',
                                        'sde.DEFAULT',
                                         versionList,
                                        'NO_LOCK_ACQUIRED',
                                        'ABORT_CONFLICTS',
                                        'BY_OBJECT',
                                        'FAVOR_EDIT_VERSION',
                                        postVersion,
                                        'KEEP_VERSION',
                                        logfileOutputRecPost)
    generateMessage(arcpy.GetMessages()+"\n")
    
# Start execution
generateMessage('Starting Validation/Reconcile/Post Automation Script... {:%Y-%b-%d %H:%M:%S}\n'.format(datetime.datetime.now()))

# Sign in to ArcGIS Enterprise    
signIntoPortal = arcpy.SignInToPortal(baseURL+"/portal", portalAdmin, portalAdminPwd)
generateMessage("Signed into ArcGIS Enterprise {} as user {}".format(baseURL+"/portal", portalAdmin))

# Get the token returned by the SignIntoPortal arcpy function to use for making REST requests
token = signIntoPortal['token']

# Build the feature service URL
featureService = "{}/server/rest/services/{}/FeatureServer".format(baseURL, serviceName)

# Get a list of the replica versions from the REST endpoint
listOfRepVersions = []
replicaVersionsURL = featureService + "/replicas?returnVersion=true&f=pjson"
repVersionsJson = openURL(replicaVersionsURL, signIntoPortal)
for repVersion in repVersionsJson:
    versionName = repVersion['replicaVersion']
    listOfRepVersions.append(versionName)
    
# Create an empty list to append version names to validate
listOfVersionsToValidate = []

# Iterate through each version returned by the versionInfo() function to find 
# the versions that need to be validated that are also in the listOfRepVersions list
for version in versionInfo():
    print("")    
    # Parse the version info response, which is a python dictionary/json
    # If the version name is sde.DEFAULT, pass since we do not want to evaluate the default version
    if version['versionName'] == "sde.DEFAULT":
        pass
    # If the modifiedDate property is null, pass
    elif version['modifiedDate'] == "None":
        pass
    # If the evaluation date is null, append the version name to the list to listOfVersions to be evaluated
    elif version['evaluationDate'] == None:
        if version['versionName'] in listOfRepVersions:
            listOfVersionsToValidate.append(version['versionName'])
    # If the evaluation date is not null, but it has been modifed since the last evaluation, add it to the list to be validated
    elif version['evaluationDate'] != None and version['modifiedDate'] > version['evaluationDate']:
        if version['versionName'] in listOfRepVersions:
            listOfVersionsToValidate.append(version['versionName'])
    # If none of these conditions are met
    else:
        generateMessage("Version {} will not be validated.".format(version['versionName']))
            
# Validate versions
generateMessage('The following versions will be validated: {}\n'.format(listOfVersionsToValidate))

# Create lists to contain versions where the validation passed or failed
failEval = []
passEval = []

# For each version in the list of versions, build the json request needed to validate
for i in listOfVersionsToValidate:
    validate_params = { "gdbVersion": i,
             "sessionId": "",
             "evaluationArea": "",
             "changesInVersion": "true",
             "selection": "",
             "evaluationType": '["validationRules"]',
             "returnEdits": "true",
             "async": "false",
             "f": "pjson",
             "token": token
    }
    # Build the REST URL used to validate the service
    validationUrl = baseURL + "/server/rest/services/"+ serviceName +"/ValidationServer/evaluate"
    
    # Call the evalVersion() function to validate the version
    evalVersion = evaluateUrl(validationUrl, validate_params)
    
    # If the evaluate failed, append to the failEval list
    if evalVersion[0] == False:
        generateMessage("Evalution of version {} failed".format(i))
        generateMessage(str(evalVersion[1]))
        failEval.append(i)
        
    # If the evaluate passed, check to see if errors were returned    
    elif evalVersion[0] == True:
        # If errors are returned, only reconcile this version
        if evalVersion[1]['errorsIdentified'] != 0:
            generateMessage("{} Errors were identified in version {}.\nThe version will be reconciled but will not be posted.\n".format((str(evalVersion[1]['errorsIdentified'])),i))
            generateMessage(str(evalVersion[1]), False)
        # If errors were not found this version can be posted
        else:
            generateMessage("Evaluation of version {} passed with no errors identified.\nThis version will be reconciled and posted.\n".format(i))
            generateMessage(str(evalVersion[1]))
            passEval.append(i)

# The versions that passed validation should be reconciled/posted
generateMessage('\nThe following versions passed validation and will be reconciled and posted: {}\n'.format(passEval))

# Run recPostVersions on the list of versions that passed evaluation with the option to post
recPostVersions(passEval, True)

# Open the reconcile log file and append the results to our report
with open(logfileOutputRecPost, 'r') as openRecLog:
    generateMessage(openRecLog.read(), False)
    
# Run recPostVersions with the option to reconcile all replica versions, no post
recPostVersions(listOfRepVersions, False)

# Open the reconcile log file and append the results to our report
with open(logfileOutputRecPost, 'r') as openRecLog:
    generateMessage(openRecLog.read(), False)

# Script execution complete
generateMessage('Validate, Reconcile, & Post Script Complete.')
```

### Example 2

```python
# Import modules
import arcpy, traceback, urllib, json, urllib.request, urllib.parse, os, urllib.error, datetime

# Overwrite the reconcile log output each time the script is run
arcpy.env.overwriteOutput = True

# Script parameters
serviceName = "MyServiceName"
baseURL = "https://MyServer.MyDomain.com"
portalAdmin = "MyAdminUser"
portalAdminPwd = "MyAdmin.Password"
logFileScript = "C:/Logs/validateRecPostScriptLog.txt"
logfileOutputRecPost = 'C:/Logs/reconcile_log.txt' 

# Choose to output a log file for the script
outputScriptReport = True

# Define functions
def openURL(url, params=None):
    """This function used to open a URL and returns the json response"""
    try:
        request_params = {'f':'pjson'}
        if params:
            request_params.update(params)
        encodedParams = urllib.parse.urlencode(request_params)
        request = urllib.request.urlopen(url, encodedParams.encode('UTF-8'))
        response = request.read()
        json_response = json.loads(response)
        return json_response
    except:
        print (traceback.format_exc())

def versionInfo(versionOwner=""):
    """This function queries the versions owned by the versionOwner.
    It returns a list of dictionaries."""
    vmsUrlinfo = "{}/server/rest/services/{}/VersionManagementServer/versionInfos?&ownerFilter={}&includeHidden=&f=json&token={}".format(baseURL, serviceName, versionOwner, token)
    response = openURL(vmsUrlinfo)
    if response['success'] == True:
        versionsDict = response['versions']
        return versionsDict
    else:
        return("Unable to get version info")

def evaluateUrl(validationUrl, validate_params):
    """This function runs evaluate on the validation server
    It returns the json response."""
    evalJsonResp = openURL(validationUrl, validate_params)
    if evalJsonResp['success'] == False:
        return [False, evalJsonResp]
    else:
        return [True, evalJsonResp]

def generateMessage(msg, print_statement=True):
    """This function generates messages as the script runs. If print_statement
    is set to True, print to the screen. If outputScriptReport is set to true,
    write the message to the logfile"""
    if outputScriptReport == True:
        with open(logFileScript, 'a') as log_file:
            log_file.write(msg + "\n")
    if print_statement == True:
        print(msg)

def recPostVersions(versionList, post):
    """This function runs the Reconcile Versions GP tool to reconcile
    and optionally post to the feature service"""
    if post == True:
        postVersion = "POST"
    elif post == False:
        postVersion = "NO_POST"
    # Reconcile and post the replica versions 
    # This tool is set to abort if there are conflicts and detects conflicts by object
    arcpy.management.ReconcileVersions(featureService,
                                        'ALL_VERSIONS',
                                        'sde.DEFAULT',
                                         versionList,
                                        'NO_LOCK_ACQUIRED',
                                        'ABORT_CONFLICTS',
                                        'BY_OBJECT',
                                        'FAVOR_EDIT_VERSION',
                                        postVersion,
                                        'KEEP_VERSION',
                                        logfileOutputRecPost)
    generateMessage(arcpy.GetMessages()+"\n")
    
# Start execution
generateMessage('Starting Validation/Reconcile/Post Automation Script... {:%Y-%b-%d %H:%M:%S}\n'.format(datetime.datetime.now()))

# Sign in to ArcGIS Enterprise    
signIntoPortal = arcpy.SignInToPortal(baseURL+"/portal", portalAdmin, portalAdminPwd)
generateMessage("Signed into ArcGIS Enterprise {} as user {}".format(baseURL+"/portal", portalAdmin))

# Get the token returned by the SignIntoPortal arcpy function to use for making REST requests
token = signIntoPortal['token']

# Build the feature service URL
featureService = "{}/server/rest/services/{}/FeatureServer".format(baseURL, serviceName)

# Get a list of the replica versions from the REST endpoint
listOfRepVersions = []
replicaVersionsURL = featureService + "/replicas?returnVersion=true&f=pjson"
repVersionsJson = openURL(replicaVersionsURL, signIntoPortal)
for repVersion in repVersionsJson:
    versionName = repVersion['replicaVersion']
    listOfRepVersions.append(versionName)
    
# Create an empty list to append version names to validate
listOfVersionsToValidate = []

# Iterate through each version returned by the versionInfo() function to find 
# the versions that need to be validated that are also in the listOfRepVersions list
for version in versionInfo():
    print("")    
    # Parse the version info response, which is a python dictionary/json
    # If the version name is sde.DEFAULT, pass since we do not want to evaluate the default version
    if version['versionName'] == "sde.DEFAULT":
        pass
    # If the modifiedDate property is null, pass
    elif version['modifiedDate'] == "None":
        pass
    # If the evaluation date is null, append the version name to the list to listOfVersions to be evaluated
    elif version['evaluationDate'] == None:
        if version['versionName'] in listOfRepVersions:
            listOfVersionsToValidate.append(version['versionName'])
    # If the evaluation date is not null, but it has been modifed since the last evaluation, add it to the list to be validated
    elif version['evaluationDate'] != None and version['modifiedDate'] > version['evaluationDate']:
        if version['versionName'] in listOfRepVersions:
            listOfVersionsToValidate.append(version['versionName'])
    # If none of these conditions are met
    else:
        generateMessage("Version {} will not be validated.".format(version['versionName']))
            
# Validate versions
generateMessage('The following versions will be validated: {}\n'.format(listOfVersionsToValidate))

# Create lists to contain versions where the validation passed or failed
failEval = []
passEval = []

# For each version in the list of versions, build the json request needed to validate
for i in listOfVersionsToValidate:
    validate_params = { "gdbVersion": i,
             "sessionId": "",
             "evaluationArea": "",
             "changesInVersion": "true",
             "selection": "",
             "evaluationType": '["validationRules"]',
             "returnEdits": "true",
             "async": "false",
             "f": "pjson",
             "token": token
    }
    # Build the REST URL used to validate the service
    validationUrl = baseURL + "/server/rest/services/"+ serviceName +"/ValidationServer/evaluate"
    
    # Call the evalVersion() function to validate the version
    evalVersion = evaluateUrl(validationUrl, validate_params)
    
    # If the evaluate failed, append to the failEval list
    if evalVersion[0] == False:
        generateMessage("Evalution of version {} failed".format(i))
        generateMessage(str(evalVersion[1]))
        failEval.append(i)
        
    # If the evaluate passed, check to see if errors were returned    
    elif evalVersion[0] == True:
        # If errors are returned, only reconcile this version
        if evalVersion[1]['errorsIdentified'] != 0:
            generateMessage("{} Errors were identified in version {}.\nThe version will be reconciled but will not be posted.\n".format((str(evalVersion[1]['errorsIdentified'])),i))
            generateMessage(str(evalVersion[1]), False)
        # If errors were not found this version can be posted
        else:
            generateMessage("Evaluation of version {} passed with no errors identified.\nThis version will be reconciled and posted.\n".format(i))
            generateMessage(str(evalVersion[1]))
            passEval.append(i)

# The versions that passed validation should be reconciled/posted
generateMessage('\nThe following versions passed validation and will be reconciled and posted: {}\n'.format(passEval))

# Run recPostVersions on the list of versions that passed evaluation with the option to post
recPostVersions(passEval, True)

# Open the reconcile log file and append the results to our report
with open(logfileOutputRecPost, 'r') as openRecLog:
    generateMessage(openRecLog.read(), False)
    
# Run recPostVersions with the option to reconcile all replica versions, no post
recPostVersions(listOfRepVersions, False)

# Open the reconcile log file and append the results to our report
with open(logfileOutputRecPost, 'r') as openRecLog:
    generateMessage(openRecLog.read(), False)

# Script execution complete
generateMessage('Validate, Reconcile, & Post Script Complete.')
```

---

## Using Python scripting to batch reconcile and post traditional versions

## Code Samples

### Example 1

```python
# get a list of connected users.
userList = arcpy.ListUsers("C:\\Projects\\MyProject\\admin.sde")
```

### Example 2

```python
# get a list of connected users.
userList = arcpy.ListUsers("C:\\Projects\\MyProject\\admin.sde")
```

### Example 3

```python
# get a list of usernames from the list of named tuples returned from ListUsers
userNames = [u.Name for u in userList]

# take the userNames list and make email addresses by appending the appropriate suffix.
emailList = [name +  '@company.com' for name in userNames]
```

### Example 4

```python
# get a list of usernames from the list of named tuples returned from ListUsers
userNames = [u.Name for u in userList]

# take the userNames list and make email addresses by appending the appropriate suffix.
emailList = [name +  '@company.com' for name in userNames]
```

### Example 5

```python
import smtplib
SERVER = "mailserver.yourcompany.com"
FROM = "SDE Admin <python@yourcompany.com>"
TO = emailList
SUBJECT = "Maintenance is about to be performed"
MSG = "Auto generated Message.\n\rServer maintenance will be performed in 15 minutes. Please log off."

# Prepare actual message
MESSAGE = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MSG)

# Send the mail
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, MESSAGE)
server.quit()
```

### Example 6

```python
import smtplib
SERVER = "mailserver.yourcompany.com"
FROM = "SDE Admin <python@yourcompany.com>"
TO = emailList
SUBJECT = "Maintenance is about to be performed"
MSG = "Auto generated Message.\n\rServer maintenance will be performed in 15 minutes. Please log off."

# Prepare actual message
MESSAGE = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MSG)

# Send the mail
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, MESSAGE)
server.quit()
```

### Example 7

```python
#block new connections to the database.
arcpy.AcceptConnections('C:\\Projects\\MyProject\\admin.sde', False)
```

### Example 8

```python
#block new connections to the database.
arcpy.AcceptConnections('C:\\Projects\\MyProject\\admin.sde', False)
```

### Example 9

```python
import time
time.sleep(900)#time is specified in seconds
```

### Example 10

```python
import time
time.sleep(900)#time is specified in seconds
```

### Example 11

```python
#disconnect all users from the database.
arcpy.DisconnectUser('C:\\Projects\\MyProject\\admin.sde', "ALL")
```

### Example 12

```python
#disconnect all users from the database.
arcpy.DisconnectUser('C:\\Projects\\MyProject\\admin.sde', "ALL")
```

### Example 13

```python
# Get a list of versions to pass into the ReconcileVersions tool.
versionList = arcpy.da.ListVersions('C:\\Projects\\MyProject\\admin.sde')

# Run the ReconcileVersions tool.
arcpy.ReconcileVersions_management('C:\\Projects\\MyProject\\admin.sde', "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "c:/temp/reconcilelog.txt")
```

### Example 14

```python
# Get a list of versions to pass into the ReconcileVersions tool.
versionList = arcpy.da.ListVersions('C:\\Projects\\MyProject\\admin.sde')

# Run the ReconcileVersions tool.
arcpy.ReconcileVersions_management('C:\\Projects\\MyProject\\admin.sde', "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "c:/temp/reconcilelog.txt")
```

### Example 15

```python
# Run the compress tool. 
arcpy.Compress_management('C:\\Projects\\MyProject\\admin.sde')
```

### Example 16

```python
# Run the compress tool. 
arcpy.Compress_management('C:\\Projects\\MyProject\\admin.sde')
```

### Example 17

```python
# Allow new connections to the database.
arcpy.AcceptConnections('C:\\Projects\\MyProject\\admin.sde', True)
```

### Example 18

```python
# Allow new connections to the database.
arcpy.AcceptConnections('C:\\Projects\\MyProject\\admin.sde', True)
```

### Example 19

```python
# set the workspace 
arcpy.env.workspace = "C:\\Projects\\MyProject\\user1.sde"

# Set a variable for the workspace
workspace = arcpy.env.workspace

# Get the username for the workspace
# this assumes you are using database authentication.
# OS authentication connection files do not have a 'user' property.
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user has access to.
# First, get all the stand alone tables, feature classes and rasters owned by the current user.
dataList = arcpy.ListTables('*.' + userName + '.*') + arcpy.ListFeatureClasses('*.' + userName + '.*') + arcpy.ListRasters('*.' + userName + '.*')

# Next, for feature datasets owned by the current user
# get all of the feature classes and add them to the primary list.
for dataset in arcpy.ListDatasets('*.' + userName + '.*'):
    dataList += arcpy.ListFeatureClasses(feature_dataset=dataset)

# Pass in the list of datasets owned by the connected user to the rebuild indexes 
# and update statistics on the data tables
arcpy.RebuildIndexes_management(workspace, "NO_SYSTEM", dataList, "ALL")
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE", "ANALYZE_DELTA", "ANALYZE_ARCHIVE"
```

### Example 20

```python
# set the workspace 
arcpy.env.workspace = "C:\\Projects\\MyProject\\user1.sde"

# Set a variable for the workspace
workspace = arcpy.env.workspace

# Get the username for the workspace
# this assumes you are using database authentication.
# OS authentication connection files do not have a 'user' property.
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user has access to.
# First, get all the stand alone tables, feature classes and rasters owned by the current user.
dataList = arcpy.ListTables('*.' + userName + '.*') + arcpy.ListFeatureClasses('*.' + userName + '.*') + arcpy.ListRasters('*.' + userName + '.*')

# Next, for feature datasets owned by the current user
# get all of the feature classes and add them to the primary list.
for dataset in arcpy.ListDatasets('*.' + userName + '.*'):
    dataList += arcpy.ListFeatureClasses(feature_dataset=dataset)

# Pass in the list of datasets owned by the connected user to the rebuild indexes 
# and update statistics on the data tables
arcpy.RebuildIndexes_management(workspace, "NO_SYSTEM", dataList, "ALL")
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE", "ANALYZE_DELTA", "ANALYZE_ARCHIVE"
```

### Example 21

```python
import arcpy, time, smtplib

# Set the workspace. 
arcpy.env.workspace = 'C:\\Projects\\MyProject\\admin.sde'

# Set a variable for the workspace.
adminConn = arcpy.env.workspace

# Get a list of connected users.
userList = arcpy.ListUsers(adminConn)

# Get a list of usernames of users currently connected and make email addresses.
emailList = [user.Name + "@yourcompany.com" for user in arcpy.ListUsers(adminConn)]

# Take the email list and use it to send an email to connected users.
SERVER = "mailserver.yourcompany.com"
FROM = "SDE Admin <python@yourcompany.com>"
TO = emailList
SUBJECT = "Maintenance is about to be performed"
MSG = "Auto generated Message.\n\rServer maintenance will be performed in 15 minutes. Please log off."

# Prepare actual message.
MESSAGE = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MSG)

# Send the email.
print("Sending email to connected users")
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, MESSAGE)
server.quit()

# Block new connections to the database.
print("The database is no longer accepting connections")
arcpy.AcceptConnections(adminConn, False)

# Wait 15 minutes.
time.sleep(900)

# Disconnect all users from the database.
print("Disconnecting all users")
arcpy.DisconnectUser(adminConn, "ALL")

# Get a list of versions to pass into the ReconcileVersions tool.
# Only reconcile versions that are children of Default.
print("Compiling a list of versions to reconcile")
verList = arcpy.da.ListVersions(adminConn)
versionList = [ver.name for ver in verList if ver.parentVersionName == 'sde.DEFAULT']

# Run the ReconcileVersions tool.
print("Reconciling all versions")
arcpy.ReconcileVersions_management(adminConn, "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "c:/temp/reconcilelog.txt")

# Run the compress tool. 
print("Running compress")
arcpy.Compress_management(adminConn)

# Allow the database to begin accepting connections again.
print("Allow users to connect to the database again")
arcpy.AcceptConnections(adminConn, True)

# Update statistics and indexes for the system tables.
# Note: To use the "SYSTEM" option, the user must be an geodatabase or database administrator.
# Rebuild indexes on the system tables.
print("Rebuilding indexes on the system tables")
arcpy.RebuildIndexes_management(adminConn, "SYSTEM")

# Update statistics on the system tables.
print("Updating statistics on the system tables")
arcpy.AnalyzeDatasets_management(adminConn, "SYSTEM")

print("Finished.")
```

### Example 22

```python
import arcpy, time, smtplib

# Set the workspace. 
arcpy.env.workspace = 'C:\\Projects\\MyProject\\admin.sde'

# Set a variable for the workspace.
adminConn = arcpy.env.workspace

# Get a list of connected users.
userList = arcpy.ListUsers(adminConn)

# Get a list of usernames of users currently connected and make email addresses.
emailList = [user.Name + "@yourcompany.com" for user in arcpy.ListUsers(adminConn)]

# Take the email list and use it to send an email to connected users.
SERVER = "mailserver.yourcompany.com"
FROM = "SDE Admin <python@yourcompany.com>"
TO = emailList
SUBJECT = "Maintenance is about to be performed"
MSG = "Auto generated Message.\n\rServer maintenance will be performed in 15 minutes. Please log off."

# Prepare actual message.
MESSAGE = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, MSG)

# Send the email.
print("Sending email to connected users")
server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, MESSAGE)
server.quit()

# Block new connections to the database.
print("The database is no longer accepting connections")
arcpy.AcceptConnections(adminConn, False)

# Wait 15 minutes.
time.sleep(900)

# Disconnect all users from the database.
print("Disconnecting all users")
arcpy.DisconnectUser(adminConn, "ALL")

# Get a list of versions to pass into the ReconcileVersions tool.
# Only reconcile versions that are children of Default.
print("Compiling a list of versions to reconcile")
verList = arcpy.da.ListVersions(adminConn)
versionList = [ver.name for ver in verList if ver.parentVersionName == 'sde.DEFAULT']

# Run the ReconcileVersions tool.
print("Reconciling all versions")
arcpy.ReconcileVersions_management(adminConn, "ALL_VERSIONS", "sde.DEFAULT", versionList, "LOCK_ACQUIRED", "NO_ABORT", "BY_OBJECT", "FAVOR_TARGET_VERSION", "POST", "DELETE_VERSION", "c:/temp/reconcilelog.txt")

# Run the compress tool. 
print("Running compress")
arcpy.Compress_management(adminConn)

# Allow the database to begin accepting connections again.
print("Allow users to connect to the database again")
arcpy.AcceptConnections(adminConn, True)

# Update statistics and indexes for the system tables.
# Note: To use the "SYSTEM" option, the user must be an geodatabase or database administrator.
# Rebuild indexes on the system tables.
print("Rebuilding indexes on the system tables")
arcpy.RebuildIndexes_management(adminConn, "SYSTEM")

# Update statistics on the system tables.
print("Updating statistics on the system tables")
arcpy.AnalyzeDatasets_management(adminConn, "SYSTEM")

print("Finished.")
```

---

## Aerial imagery raster types

## Code Samples

### Example 1

```python
error = K1 + K2 * r2 + K3 * r4
```

### Example 2

```python
error = K1 + K2 * r2 + K3 * r4
```

### Example 3

```python
error = K1 + K2 * r3 + K3 * r5
```

### Example 4

```python
error = K1 + K2 * r3 + K3 * r5
```

### Example 5

```python
25400 / Image Scan Resolution
```

### Example 6

```python
25400 / Image Scan Resolution
```

---

## Work with multidimensional mosaic datasets

## Code Samples

### Example 1

```python
wind chill = 35.74 + 0.615T -
35.75*(V^0.16) + 0.4275T*(V^0.16)
```

### Example 2

```python
wind chill = 35.74 + 0.615T -
35.75*(V^0.16) + 0.4275T*(V^0.16)
```

---

## Cameras table schema

## Code Samples

### Example 1

```python
K1_mm = K1_cv / (f * f)
```

### Example 2

```python
K1_mm = K1_cv / (f * f)
```

### Example 3

```python
K2_mm = K2_cv / (f * f * f * f)
```

### Example 4

```python
K2_mm = K2_cv / (f * f * f * f)
```

### Example 5

```python
K3_mm = K3_cv / (f * f * f * f * f * f)
```

### Example 6

```python
K3_mm = K3_cv / (f * f * f * f * f * f)
```

### Example 7

```python
P1_mm = -p1_cv/f
```

### Example 8

```python
P1_mm = -p1_cv/f
```

### Example 9

```python
P2_mm = -p2_cv/f
```

### Example 10

```python
P2_mm = -p2_cv/f
```

### Example 11

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 12

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 13

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

### Example 14

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

---

## Create a Reality mapping workspace for drone imagery

## Code Samples

### Example 1

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 2

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 3

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

### Example 4

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

---

## Create an ortho mapping workspace for drone imagery

## Code Samples

### Example 1

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 2

```python
Pixel Size = CCD Diagonal / Image Diagonal(in pixels)
```

### Example 3

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

### Example 4

```python
CCD Diagonal = 2 * (Focal Length * Tan(FOV/2))
```

---

## Esri Grid format

## Code Samples

### Example 1

```python
Record	 VALUE     COUNT
 1        0       628872
 2        1       265043
 3        2       151150
 4        3      3185652
 5        4        79983
 6        5         4782
 7        6        74334
 8        7         8877
 9        8         1817
 10       9          491
 11      10          858
 12      11         8770
 13      12        28789
 14      13        72539
 15      14         3686
 16      15         3932
 17      16        13227
 18      17         1890
 19      18         1305
 20      19       427286
 21      20         6695
```

### Example 2

```python
GRID: LIST JER135.STK
Record  INDEX   GRID
  1       1     jer1
  2       2     jer3
  3       3     jer5
```

### Example 3

```python
Projection STATEPLANE 
Zone     4701 
Datum    NAD27 
Zunits   NO 
Units    FEET 
Spheroid CLARKE1866 
Xshift   0.0000000000 
Yshift   0.0000000000 
Parameters
```

---

## Files, tables, and web services raster types

## Code Samples

### Example 1

```python
from osgeo import gdal 
ds=gdal.Open(r'C:\data\multidimensional_netcdf.nc') 
sd=ds.GetSubDatasets() 
print(sd) 
# [('NETCDF:"C:\\data\\multidimensional_netcdf.nc":water_temp:0', 'variable:"water_temp"; size:"100x100"; datatype:"16-bit integer"; StdTime:"41411"; StdZ:"-5000"; '), ('NETCDF:"C:\\data\\multidimensional_netcdf.nc":water_temp:1', 'variable:"water_temp"; size:"100x100"; datatype:"16-bit integer"; StdTime:"41411"; StdZ:"-4000"; ')]
```

### Example 2

```python
from osgeo import gdal 
ds=gdal.Open(r'C:\data\multidimensional_netcdf.nc') 
sd=ds.GetSubDatasets() 
print(sd) 
# [('NETCDF:"C:\\data\\multidimensional_netcdf.nc":water_temp:0', 'variable:"water_temp"; size:"100x100"; datatype:"16-bit integer"; StdTime:"41411"; StdZ:"-5000"; '), ('NETCDF:"C:\\data\\multidimensional_netcdf.nc":water_temp:1', 'variable:"water_temp"; size:"100x100"; datatype:"16-bit integer"; StdTime:"41411"; StdZ:"-4000"; ')]
```

### Example 3

```python
import arcpy 
r = arcpy.Raster(r'C:\data\multidimensional_netcdf.nc', True) 
xMin = r.extent.XMin 
yMin = r.extent.YMin 
xMax = r.extent.XMax 
yMax = r.extent.YMax 
nRows = r.height 
nCols = r.width 
nBands = r.bandCount 
PixelType = r.pixelType
```

### Example 4

```python
import arcpy 
r = arcpy.Raster(r'C:\data\multidimensional_netcdf.nc', True) 
xMin = r.extent.XMin 
yMin = r.extent.YMin 
xMax = r.extent.XMax 
yMax = r.extent.YMax 
nRows = r.height 
nCols = r.width 
nBands = r.bandCount 
PixelType = r.pixelType
```

### Example 5

```python
OBJECTID,Raster,xMin,yMin,xMax,yMax,nRows,nCols,nBands,PixelType,Variable,Dimensions,StdTime,StdZ 
1,"NETCDF:""C:\\data\\multidimensional_netcdf.nc"":water_temp:0",-64.03996955023871,43.96000000924775,-56.0399713997889,51.95999815969756,100,100,1,F32,water_temp,"StdTime,StdZ",2013-05-17T00:00:00,-5000 
2,"NETCDF:""C:\\data\\multidimensional_netcdf.nc"":water_temp:1",-64.03996955023871,43.96000000924775,-56.0399713997889,51.95999815969756,100,100,1,F32,water_temp,"StdTime,StdZ",2013-05-17T00:00:00,-4000
```

### Example 6

```python
OBJECTID,Raster,xMin,yMin,xMax,yMax,nRows,nCols,nBands,PixelType,Variable,Dimensions,StdTime,StdZ 
1,"NETCDF:""C:\\data\\multidimensional_netcdf.nc"":water_temp:0",-64.03996955023871,43.96000000924775,-56.0399713997889,51.95999815969756,100,100,1,F32,water_temp,"StdTime,StdZ",2013-05-17T00:00:00,-5000 
2,"NETCDF:""C:\\data\\multidimensional_netcdf.nc"":water_temp:1",-64.03996955023871,43.96000000924775,-56.0399713997889,51.95999815969756,100,100,1,F32,water_temp,"StdTime,StdZ",2013-05-17T00:00:00,-4000
```

---

## Indices gallery

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
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 4

```python
NDVI = ((NIR - Red)/(NIR + Red))
```

### Example 5

```python
PVI = (NIR - a*Red - b) / (sqrt(1 + a2))
```

### Example 6

```python
PVI = (NIR - a*Red - b) / (sqrt(1 + a2))
```

### Example 7

```python
SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
```

### Example 8

```python
SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)
```

### Example 9

```python
TSAVI = (s * (NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 10

```python
TSAVI = (s * (NIR - s * Red - a)) / (a * NIR + Red - a * s + X * (1 + s2))
```

### Example 11

```python
VARI = (Green - Red)/ (Green + Red - Blue)
```

### Example 12

```python
VARI = (Green - Red)/ (Green + Red - Blue)
```

### Example 13

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 14

```python
NDSI = (Green - SWIR) / (Green + SWIR)
```

### Example 15

```python
MNDWI = (Green - SWIR) / (Green + SWIR)
```

### Example 16

```python
MNDWI = (Green - SWIR) / (Green + SWIR)
```

### Example 17

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 18

```python
NDMI = (NIR - SWIR1)/(NIR + SWIR1)
```

### Example 19

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 20

```python
Clay Minerals Ratio = SWIR1 / SWIR2
```

### Example 21

```python
Ferrous Minerals Ratio = SWIR / NIR
```

### Example 22

```python
Ferrous Minerals Ratio = SWIR / NIR
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
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 26

```python
BAI = 1/((0.1 -RED)^2 + (0.06 - NIR)^2)
```

### Example 27

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 28

```python
NBR = (NIR - SWIR) / (NIR+ SWIR)
```

### Example 29

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

### Example 30

```python
NDBI = (SWIR - NIR) / (SWIR + NIR)
```

---

## Measure feature volume based on an elevation surface raster

## Code Samples

### Example 1

```python
Cut Volume error = <number of cut cells> * 2.0 * GSD³
```

### Example 2

```python
Cut Volume error = <number of cut cells> * 2.0 * GSD³
```

### Example 3

```python
Fill Volume error = <number of fill cells> * 2.0 * GSD³
```

### Example 4

```python
Fill Volume error = <number of fill cells> * 2.0 * GSD³
```

### Example 5

```python
Total Volume error = Cut error + Fill error
```

### Example 6

```python
Total Volume error = Cut error + Fill error
```

### Example 7

```python
Cut Volume error = <number of cut cells> * 2.0 * GSD³
```

### Example 8

```python
Cut Volume error = <number of cut cells> * 2.0 * GSD³
```

### Example 9

```python
Fill Volume error = <number of fill cells> * 2.0 * GSD³
```

### Example 10

```python
Fill Volume error = <number of fill cells> * 2.0 * GSD³
```

### Example 11

```python
Total Volume error = Cut error + Fill error
```

### Example 12

```python
Total Volume error = Cut error + Fill error
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

## Oriented imagery table

## Code Samples

### Example 1

```python
K1 = K1_cv/(f * f)
```

### Example 2

```python
K1 = K1_cv/(f * f)
```

### Example 3

```python
K2 = K2_cv/(f * f * f* f)
```

### Example 4

```python
K2 = K2_cv/(f * f * f* f)
```

### Example 5

```python
K3 = K3_cv/(f * f * f * f * f * f)
```

### Example 6

```python
K3 = K3_cv/(f * f * f * f * f * f)
```

### Example 7

```python
P1 = P2_cv/f
```

### Example 8

```python
P1 = P2_cv/f
```

### Example 9

```python
P2 = -P1_cv/f
```

### Example 10

```python
P2 = -P1_cv/f
```

### Example 11

```python
A0 = Width of the Image/2-0.5
```

### Example 12

```python
A0 = Width of the Image/2-0.5
```

### Example 13

```python
B0 = Height of the Image/2-0.5
```

### Example 14

```python
B0 = Height of the Image/2-0.5
```

---

## Raster dataset attribute tables

## Code Samples

### Example 1

```python
1   Forest
2   Wetland
3   Crop
4   Urban
```

### Example 2

```python
1   Forest
2   Wetland
3   Crop
4   Urban
```

---

## Tutorial: Create a digital surface model product from satellite imagery in ArcGIS Reality for ArcGIS Pro



---

## World files for raster datasets

## Code Samples

### Example 1

```python
20.17541308822119
0.00000000000000
0.00000000000000
-20.17541308822119
424178.11472601280548
4313415.90726399607956
```

### Example 2

```python
20.17541308822119
0.00000000000000
0.00000000000000
-20.17541308822119
424178.11472601280548
4313415.90726399607956
```

### Example 3

```python
x1 = Ax + By + C
y1 = Dx + Ey + F
```

### Example 4

```python
x1 = Ax + By + C
y1 = Dx + Ey + F
```

### Example 5

```python
x1 is the calculated x-coordinate of the pixel on the map
```

### Example 6

```python
y1 is the calculated y-coordinate of the pixel on the map
```

### Example 7

```python
x is the column number of a pixel in the image
```

### Example 8

```python
y = row number of a pixel in the image
```

### Example 9

```python
A = x-scale; dimension of a pixel in map units in x direction
```

### Example 10

```python
B and D are the rotation terms
```

### Example 11

```python
C and F are the translation terms; where the x,y map coordinates of the center of the upper left pixel
```

### Example 12

```python
E is the negative of y-scale; dimension of a pixel in map units in y direction
```

### Example 13

```python
20.17541308822119 - A
0.00000000000000 - D
0.00000000000000 - B
-20.17541308822119 - E
424178.11472601280548 - C
4313415.90726399607956 - F
```

### Example 14

```python
20.17541308822119 - A
0.00000000000000 - D
0.00000000000000 - B
-20.17541308822119 - E
424178.11472601280548 - C
4313415.90726399607956 - F
```

### Example 15

```python
A = mx · cos t
```

### Example 16

```python
A = mx · cos t
```

### Example 17

```python
B = my · (k · cos t - sin t)
```

### Example 18

```python
B = my · (k · cos t - sin t)
```

### Example 19

```python
D = mx · sin t
```

### Example 20

```python
D = mx · sin t
```

### Example 21

```python
E = -1 · my · (k · sin t + cos t)
```

### Example 22

```python
E = -1 · my · (k · sin t + cos t)
```

### Example 23

```python
C = translation in x direction
```

### Example 24

```python
C = translation in x direction
```

### Example 25

```python
F = translation in y direction
```

### Example 26

```python
F = translation in y direction
```

### Example 27

```python
mx = change of scale in x direction
```

### Example 28

```python
my = change of scale in y direction
```

### Example 29

```python
k = shear factor along the x-axis = tan (skew angle, measured from the y-axis)
```

### Example 30

```python
t = rotation angle, measured counter-clockwise from the x-axis
```

---

## Train a deep learning model for point cloud classification

## Code Samples

### Example 1

```python
point_density = 1 / (point_spacing)
```

### Example 2

```python
point_density = 1 / (point_spacing)
```

### Example 3

```python
block_area = desired_block_point_count / point_density
```

### Example 4

```python
block_area = desired_block_point_count / point_density
```

### Example 5

```python
block_size = 2 * square_root(block_area / Pi)
```

### Example 6

```python
block_size = 2 * square_root(block_area / Pi)
```

---

## Reading netCDF data as a point feature layer

## Code Samples

### Example 1

```python
dimensions:
	station = 10;  // measurement locations
	pressure = 11;
	time = UNLIMITED;
variables:
	float humidity(time, pressure, station);
		humidity:long_name = "Specific humidity" ;
		humidity:coordinates = "lat lon" ;
	float temperature(time, pressure, station);
		temperature:long_name = "Temperature" ;
		temperature:coordinates = "lat lon" ;
	double time(time);
		time:long_name = "time of measurement" ;
		time:units = "days since 1970-01-01 00:00:00" ;
	float lon(station);
		lon:long_name = "station longitude";
		lon:units = "degrees_east";
	float lat(station);
		lat:long_name = "station latitude" ;
		lat:units = "degrees_north" ;
	float pressure(pressure);
		pressure:long_name = "pressure" ;
		pressure:units = "hPa" ;
```

### Example 2

```python
dimensions:
	station = 10;  // measurement locations
	pressure = 11;
	time = UNLIMITED;
variables:
	float humidity(time, pressure, station);
		humidity:long_name = "Specific humidity" ;
		humidity:coordinates = "lat lon" ;
	float temperature(time, pressure, station);
		temperature:long_name = "Temperature" ;
		temperature:coordinates = "lat lon" ;
	double time(time);
		time:long_name = "time of measurement" ;
		time:units = "days since 1970-01-01 00:00:00" ;
	float lon(station);
		lon:long_name = "station longitude";
		lon:units = "degrees_east";
	float lat(station);
		lat:long_name = "station latitude" ;
		lat:units = "degrees_north" ;
	float pressure(pressure);
		pressure:long_name = "pressure" ;
		pressure:units = "hPa" ;
```

---

## Reading netCDF data as a raster layer

## Code Samples

### Example 1

```python
netcdf annualrainfall {
dimensions:
	latitude = 48 ;
	longitude = 115 ;
	time = UNLIMITED ; 
variables:
	float latitude (latitude) ;
		latitude:units = "degrees_north" ;
	float longitude (longitude) ;
		longitude:units = "degrees_east" ;
	int time(time) ;
		time:units = "days since 1895-01-01" ;
		time:time_step = "annual" ;
		time:calendar = "gregorian" ;
	float rainfall (time, latitude, longitude) ;
		rainfall:units = "mm yr-1" ;
		rainfall:_FillValue = -9999.f ;
		rainfall:missing_value = -9999.f ;
}
```

### Example 2

```python
netcdf annualrainfall {
dimensions:
	latitude = 48 ;
	longitude = 115 ;
	time = UNLIMITED ; 
variables:
	float latitude (latitude) ;
		latitude:units = "degrees_north" ;
	float longitude (longitude) ;
		longitude:units = "degrees_east" ;
	int time(time) ;
		time:units = "days since 1895-01-01" ;
		time:time_step = "annual" ;
		time:calendar = "gregorian" ;
	float rainfall (time, latitude, longitude) ;
		rainfall:units = "mm yr-1" ;
		rainfall:_FillValue = -9999.f ;
		rainfall:missing_value = -9999.f ;
}
```

---

## Reading netCDF data as a table view

## Code Samples

### Example 1

```python
dimensions:
	station = 10;  // measurement locations
	pressure = 11;
	time = UNLIMITED;
variables:
	float humidity(time, pressure, station);
		humidity:long_name = "Specific humidity" ;
		humidity:coordinates = "lat lon" ;
	float temperature(time, pressure, station);
		temperature:long_name = "Temperature" ;
		temperature:coordinates = "lat lon" ;
	double time(time);
		time:long_name = "time of measurement" ;
		time:units = "days since 1970-01-01 00:00:00" ;
	float lon(station);
		lon:long_name = "station longitude";
		lon:units = "degrees_east";
	float lat(station);
		lat:long_name = "station latitude" ;
		lat:units = "degrees_north" ;
	float pressure(pressure);
		pressure:long_name = "pressure" ;
		pressure:units = "hPa" ;
```

### Example 2

```python
dimensions:
	station = 10;  // measurement locations
	pressure = 11;
	time = UNLIMITED;
variables:
	float humidity(time, pressure, station);
		humidity:long_name = "Specific humidity" ;
		humidity:coordinates = "lat lon" ;
	float temperature(time, pressure, station);
		temperature:long_name = "Temperature" ;
		temperature:coordinates = "lat lon" ;
	double time(time);
		time:long_name = "time of measurement" ;
		time:units = "days since 1970-01-01 00:00:00" ;
	float lon(station);
		lon:long_name = "station longitude";
		lon:units = "degrees_east";
	float lat(station);
		lat:long_name = "station latitude" ;
		lat:units = "degrees_north" ;
	float pressure(pressure);
		pressure:long_name = "pressure" ;
		pressure:units = "hPa" ;
```

---

## World files for CAD and BIM data

## Code Samples

### Example 1

```python
25933.063000,9032.704720,1702332.110159, 309622.102491,-8987.532001,1300.050854
32047.556994,13057.483520,1706354.400361 303697.073028,-9091.566340,1337.519601
```

### Example 2

```python
25933.063000,9032.704720,1702332.110159, 309622.102491,-8987.532001,1300.050854
32047.556994,13057.483520,1706354.400361 303697.073028,-9091.566340,1337.519601
```

---

## Edit web feature layers

## Code Samples

### Example 1

```python
1 + (Record Count / 1000) + (Payload Size (MB) / 6 MB)
```

### Example 2

```python
1 + (Record Count / 1000) + (Payload Size (MB) / 6 MB)
```

---

## Use an ASCII or text file

## Code Samples

### Example 1

```python
x,y,ID,color
8.6,5.6,001,blue
99.3,77.0,002,blue and red
8.01,44.3,003,orange
```

### Example 2

```python
x,y,ID,color
8.6,5.6,001,blue
99.3,77.0,002,blue and red
8.01,44.3,003,orange
```

### Example 3

```python
[Trees.CSV]
Col14=PLOTS Text
```

### Example 4

```python
[Trees.CSV]
Col14=PLOTS Text
```

### Example 5

```python
ID Name Number 
1 One 1.0
2 Two 2.4564
3 Three 3.45464
```

### Example 6

```python
ID Name Number 
1 One 1.0
2 Two 2.4564
3 Three 3.45464
```

---

## Perform common topology tasks

## Code Samples

### Example 1

```python
arcpy.AddFeatureClassToTopology_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", r"C:\MyProject\MyProject.gdb\Streets\StreetNetwork", 1, 0.1)
```

### Example 2

```python
arcpy.AddFeatureClassToTopology_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", r"C:\MyProject\MyProject.gdb\Streets\StreetNetwork", 1, 0.1)
```

### Example 3

```python
arcpy.RemoveFeatureClassFromTopology_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", r"C:\MyProject\MyProject.gdb\Streets\StreetNetwork")
```

### Example 4

```python
arcpy.RemoveFeatureClassFromTopology_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", r"C:\MyProject\MyProject.gdb\Streets\StreetNetwork")
```

### Example 5

```python
arcpy.SetClusterTolerance_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", 0.00015)
```

### Example 6

```python
arcpy.SetClusterTolerance_management(r"C:\MyProject\MyProject.gdb\Streets\Street_Topo", 0.00015)
```

### Example 7

```python
arcpy.AddRuleToTopology_management("C:\\MyProject\\MyProject.gdb\\Streets\\Street_Topo",
                                                 "Boundary Must Be Covered By Boundary Of (Area-Area)",
                                                 "C:\\MyProject\\MyProject.gdb\\Streets\\Subdivision",
                                                 "",
                                                 "C:\\MyProject\\MyProject.gdb\\Streets\\Parcels",
                                                 "")
```

### Example 8

```python
arcpy.AddRuleToTopology_management("C:\\MyProject\\MyProject.gdb\\Streets\\Street_Topo",
                                                 "Boundary Must Be Covered By Boundary Of (Area-Area)",
                                                 "C:\\MyProject\\MyProject.gdb\\Streets\\Subdivision",
                                                 "",
                                                 "C:\\MyProject\\MyProject.gdb\\Streets\\Parcels",
                                                 "")
```

### Example 9

```python
arcpy.RemoveRuleFromTopology_management("C:\\MyProject\\MyProject.gdb\\Streets\\Street_Topo",
                                                      "Must Not Have Dangles (21)")
```

### Example 10

```python
arcpy.RemoveRuleFromTopology_management("C:\\MyProject\\MyProject.gdb\\Streets\\Street_Topo",
                                                      "Must Not Have Dangles (21)")
```

---

## Create a topology

## Code Samples

### Example 1

```python
import arcpy
import os

# Input variables
input_dataset = r"C:\MyProjects\MyProject.gdb\fds"
topo_name = "Topology"
cluster_tol = 0.001
input_fc = r"C:\MyProjects\MyProject.gdb\fds\fc1 1 1;C:\MyProjects\MyProject.gdb\fds\fc2 1 1"
rules = r"'Must Not Overlap (Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc1 #;'Must Be Covered By Feature Class Of (Area-Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc2 #"
validate = "true"

# Create the topology
out_topo = arcpy.CreateTopology_management(input_dataset, topo_name, cluster_tol)
print("Created topology.")

# Loop through the list of feature classes and add them to the topology
input_fcL = input_fc.split(";")
for fc in input_fcL:
    param = fc.rsplit(" ", 2)
    in_fc = param[0]
    xy_rank = param[1]
    z_rank = param[2]
    arcpy.AddFeatureClassToTopology_management(out_topo, in_fc, xy_rank, z_rank)
    print(arcpy.GetMessages())
    
# Loop through the list of rules and add rules to the topology
rulesL = rules.split(";")
for rule in rulesL:
    r = rule.rsplit(" ", 4)
    rule_type = r[0].replace("'","")
    in_fc1 = r[1]
    subtype1 = r[2]
    in_fc2 = r[3]
    subtype2 = r[4]
    arcpy.AddRuleToTopology_management(out_topo, rule_type, in_fc1, subtype1, in_fc2, subtype2)
    print(arcpy.GetMessages())
    
# Validate the topology
if validate == "true":
    try:
        arcpy.ValidateTopology_management(out_topo)
    except:
        print(arcpy.GetMessages())
print("Finished.")
```

### Example 2

```python
import arcpy
import os

# Input variables
input_dataset = r"C:\MyProjects\MyProject.gdb\fds"
topo_name = "Topology"
cluster_tol = 0.001
input_fc = r"C:\MyProjects\MyProject.gdb\fds\fc1 1 1;C:\MyProjects\MyProject.gdb\fds\fc2 1 1"
rules = r"'Must Not Overlap (Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc1 #;'Must Be Covered By Feature Class Of (Area-Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc2 #"
validate = "true"

# Create the topology
out_topo = arcpy.CreateTopology_management(input_dataset, topo_name, cluster_tol)
print("Created topology.")

# Loop through the list of feature classes and add them to the topology
input_fcL = input_fc.split(";")
for fc in input_fcL:
    param = fc.rsplit(" ", 2)
    in_fc = param[0]
    xy_rank = param[1]
    z_rank = param[2]
    arcpy.AddFeatureClassToTopology_management(out_topo, in_fc, xy_rank, z_rank)
    print(arcpy.GetMessages())
    
# Loop through the list of rules and add rules to the topology
rulesL = rules.split(";")
for rule in rulesL:
    r = rule.rsplit(" ", 4)
    rule_type = r[0].replace("'","")
    in_fc1 = r[1]
    subtype1 = r[2]
    in_fc2 = r[3]
    subtype2 = r[4]
    arcpy.AddRuleToTopology_management(out_topo, rule_type, in_fc1, subtype1, in_fc2, subtype2)
    print(arcpy.GetMessages())
    
# Validate the topology
if validate == "true":
    try:
        arcpy.ValidateTopology_management(out_topo)
    except:
        print(arcpy.GetMessages())
print("Finished.")
```

---

## Configure a trace

## Code Samples

### Example 1

```python
ERROR 002041: One or more dirty areas were discovered.
[[NHDFlowline: {0DBFACDA-45D6-BA67-33CE-A750BE632C05}]]
Failed to execute (Trace).
```

### Example 2

```python
ERROR 002041: One or more dirty areas were discovered.
[[NHDFlowline: {0DBFACDA-45D6-BA67-33CE-A750BE632C05}]]
Failed to execute (Trace).
```

---

## Configure a trace

## Code Samples

### Example 1

```python
ERROR 002041: One or more dirty areas were discovered.
[[ElectricDistributionLine: {C0060506-AG17-4B64-B2E0-9162BE613C05}]]
Failed to execute (Trace).
```

### Example 2

```python
ERROR 002041: One or more dirty areas were discovered.
[[ElectricDistributionLine: {C0060506-AG17-4B64-B2E0-9162BE613C05}]]
Failed to execute (Trace).
```

### Example 3

```python
ERROR 003326: Unlocatable objects discovered.
[[GasDistributionJunctionObject: {4F860903-PK17-5c15-Y2W0-3512BP436C00}]]
Failed to execute (Trace).
```

### Example 4

```python
ERROR 003326: Unlocatable objects discovered.
[[GasDistributionJunctionObject: {4F860903-PK17-5c15-Y2W0-3512BP436C00}]]
Failed to execute (Trace).
```

### Example 5

```python
"sourceMapping": {
		"1": "UN_6_Associations",
		"2": "UN_6_SystemJunctions",
		"4": "Structure Junction",
		"5": "Structure Line",
		"6": "Structure Boundary",
		"7": "Structure Junction Object",
		"8": "Structure Edge Object",
		"9": "Electric Distribution Device",
		"10": "Electric Distribution Line",
		"11": "Electric Distribution Assembly",
		"12": "Electric Distribution Junction",
		"13": "Electric Distribution SubnetLine",
		"14": "Electric Distribution Junction Object",
		"15": "Electric Distribution Edge Object"
	},
```

### Example 6

```python
"sourceMapping": {
		"1": "UN_6_Associations",
		"2": "UN_6_SystemJunctions",
		"4": "Structure Junction",
		"5": "Structure Line",
		"6": "Structure Boundary",
		"7": "Structure Junction Object",
		"8": "Structure Edge Object",
		"9": "Electric Distribution Device",
		"10": "Electric Distribution Line",
		"11": "Electric Distribution Assembly",
		"12": "Electric Distribution Junction",
		"13": "Electric Distribution SubnetLine",
		"14": "Electric Distribution Junction Object",
		"15": "Electric Distribution Edge Object"
	},
```

### Example 7

```python
Filter Barriers
Name: Phases Current
Operator: Does not include any (Bitwise AND equals False)
Type: Specific value
Value: 4 //code for A (100)
```

### Example 8

```python
Filter Barriers
Name: Phases Current
Operator: Does not include any (Bitwise AND equals False)
Type: Specific value
Value: 4 //code for A (100)
```

---

## Define tiers

## Code Samples

### Example 1

```python
Type: esriFieldTypeString
IsNullable: VARIANT_FALSE
DomainFixed: VARIANT_FALSE
Length: 2000
IsIndexed: true
IsUniqueIndex: false
IsEditable: VARIANT_FALSE
Default value: "Unknown"
```

### Example 2

```python
Type: esriFieldTypeString
IsNullable: VARIANT_FALSE
DomainFixed: VARIANT_FALSE
Length: 2000
IsIndexed: true
IsUniqueIndex: false
IsEditable: VARIANT_FALSE
Default value: "Unknown"
```

---

## Network attributes

## Code Samples

### Example 1

```python
ceiling(log2(n + 1))
```

### Example 2

```python
ceiling(log2(n + 1))
```

### Example 3

```python
log2(3+1)=2
```

### Example 4

```python
log2(3+1)=2
```

---

## Polygon Gap is Sliver

## Code Samples

### Example 1

```python
T = 4π(A/P²)
```

### Example 2

```python
T = 4π(A/P²)
```

---

## Polygon Overlap is Sliver

## Code Samples

### Example 1

```python
T = 4π(A/P²)
```

### Example 2

```python
T = 4π(A/P²)
```

---

## Polygon Sliver

## Code Samples

### Example 1

```python
T = 4π(A/P²)
```

### Example 2

```python
T = 4π(A/P²)
```

---
