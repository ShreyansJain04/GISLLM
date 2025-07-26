# Complete ArcPy Classes Reference

*Consolidated from 50 individual documentation files*

---

## AIO

## Summary

Creates an AIO object to handle local and cloud files, and data stores in a unified way that can be used in Python.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| path | To construct an AIO object to handle a cloud store, use the .acs file path.To construct an AIO object to handle a local file store, this parameter can be a local folder path or it can be left empty. If a local folder path is provided, it will be used as the current working directory. | String |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| handle | An open file handle. The data type is AIOFile.Note:An instance of this class is returned by the AIO object's open method. | Object |
| src | The source path of the file. | String |
| dst | The target path of the file. | String |
| options | Specifies the options that will be used.RECURSIVE—Subdirectories and their contents will be recursively copied. This option is only applicable for folder operations.SYNC_STRATEGY—The criteria that will be used for overwriting if the target file exists.NUM_THREADS—The number of threads that will be used for parallel file copying.CHUNK_SIZE—The maximum chunk size (in bytes) that will be used to split large objects when uploading or downloading.Syntax—RECURSIVE=[YES\|NO], SYNC_STRATEGY=[TIMESTAMP\|ETAG\|OVERWRITE], NUM_THREADS=(integer) CHUNK_SIZE=(integer) [x-amz-*\|x-goog-*\|x-ms-*=(value)]Example—{'RECURSIVE':'YES', 'SYNC_STRATEGY':'OVERWRITE', 'NUM_THREADS':'10', 'CHUNK_SIZE':'8'}(The default value is None) | Dictionary |
| src | The source path of the file. | String |
| dst | The target path of the file. | String |
| options | Specifies the options that will be used.RECURSIVE—Subdirectories and their contents will be recursively copied. This option is only applicable for folder operations.SYNC_STRATEGY—The criteria that will be used for overwriting if the target file exists.NUM_THREADS—The number of threads that will be used for parallel file copying.CHUNK_SIZE—The maximum chunk size (in bytes) that will be used to split large objects when uploading or downloading.Syntax—RECURSIVE=[YES\|NO], SYNC_STRATEGY=[TIMESTAMP\|ETAG\|OVERWRITE], NUM_THREADS=(integer) CHUNK_SIZE=(integer) [x-amz-*\|x-goog-*\|x-ms-*=(value)]Example— {'RECURSIVE':'YES', 'SYNC_STRATEGY':'OVERWRITE', 'NUM_THREADS':'10', 'CHUNK_SIZE':'8'}(The default value is None) | Dictionary |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The path for which the access time will be obtained. The value can be a relative path from the current working directory or an absolute path. | String |
| path | The path for which the creation time will be obtained. The value can be a relative path from the current working directory or an absolute path. | String |
| type | Specifies the path style for the returned URI (for cloud only). The data type is CloudPathType.Available options are CloudPathType.VSI, CloudPathType.ACS, CloudPathType.HTTP, and CloudPathType.CLOUDSTORES.(The default value is CloudPathType.VSI) | Object |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| type | Specifies the path style for the returned URI (for cloud only). The data type is CloudPathType. Available options are CloudPathType.VSI, CloudPathType.ACS, CloudPathType.HTTP, and CloudPathType.CLOUDSTORES.(The default value is CloudPathType.VSI) | Object |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). (The default value is None) | String |
| type | Specifies the path style for the returned URI (for cloud only). The data type is CloudPathType. Available options are CloudPathType.VSI, CloudPathType.ACS, CloudPathType.HTTP, and CloudPathType.CLOUDSTORES.(The default value is CloudPathType.VSI) | Object |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| mode | Specifies the mode that will be used for opening a file.r—The file will be opened in read mode.w—The file will be opened in write mode.rb—The file will be opened in binary format for reading.wb—The file will be opened in binary format for writing.Note:Only read mode honors the encoding parameter.(The default value is None) | String |
| encoding | The type of encoding that will be used to open a file.utf-8—UTF-8 encoding will be used. This is the default.utf-16—UTF-16 encoding will be used. ascii—ASCII encoding will be used.(The default value is utf-8) | String |
| mime | The Multipurpose Internet Mail Extensions (MIME) headers. It is recommended that you set MIME headers when creating the file for faster creation and setting of metadata.(The default value is None) | Dictionary |
| path | A relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path[path,...] | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| src | The source path of the file. | String |
| dst | The target path of the file. | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| depth | The recursion depth.A value of -1 is for recursive scanning.A value of 0 is for scanning the current directory.A value greater than 0 (>0) is for an arbitrary level.(The default value is 0) | Integer |
| type | Specifies the path style for the returned URI (for cloud only). The data type is CloudPathType. Available options are CloudPathType.VSI, CloudPathType.ACS, CloudPathType.HTTP, and CloudPathType.CLOUDSTORES.(The default value is CloudPathType.VSI) | Object |

## Methods

### chdir (path)

Changes the working directory relative to the current working directory..

### close (handle)

Closes the open file handle.

### copy (src, dst, {options})

Copies a file from the source to the destination.For a cloud-based AIO object: If the src or dst value is a local path, use an absolute local path. If the src or dst value is a cloud path, use a relative path from the current working directory or an absolute vsi cloud path. If the src and dst values are cloud paths, use absolute vsi cloud paths.For a local AIO object:The src and dst values can be a relative path from the current working directory or an absolute path.

### copytree (src, dst, {options})

Copies the contents from one directory to another.For a cloud-based AIO object: If the src or dst value is a local path, use an absolute local path. If the src or dst value is a cloud path, use a relative path from the current working directory or an absolute vsi cloud path. If the src and dst values are cloud paths, use absolute vsi cloud paths.For a local AIO object: The src and dst values can be a relative path from the current working directory or an absolute path.

### exists (path)

Verifies whether a path exists.

### getatime (path)

Gets the file access time for a file.

### getctime (path)

Gets the file creation time for a file.

### getcwd ({type})

Gets the current working directory.

### getmtime (path)

Gets the file modification time for a file.

### getpath (path, {type})

Constructs a URI path.

### getsize (path)

Gets the size of a file in bytes.

### isdir (path)

Verifies whether a path is a directory.

### isfile (path)

Verifies whether a path is a file.

### listdir ({path}, {type})

Lists the contents of a directory nonrecursively.

### makedirs (path)

Creates a directory recursively.

### mkdir (path)

Creates a directory.

### open (path, {mode}, {encoding}, {mime})

Opens a file handle.The handle must be explicitly closed.

### remove (path)

Deletes a file.

### removefiles (path)

Delete multiple files.

### rename (src, dst)

Renames or moves a file or a directory. Renaming cloud files is computationally intensive, as copy and delete are performed on the server side.For a cloud based AIO object: If the src or dst value is a local path, use an absolute local path. If the src or dst value is a cloud path, use a relative path from the current working directory or an absolute vsi cloud path. If the src and dst values are cloud paths, use absolute vsi cloud paths.For a local AIO object: The src and dst values can be a relative path from the current working directory or an absolute path.

### rmtree (path)

Removes a directory and its contents recursively.

### scandir (path, {depth}, {type})

Returns an iterable of entries in a directory.

## Code Samples

### Example 1

```python
AIO ({path})
```

### Example 2

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovidername()
```

### Example 3

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovidername()
```

### Example 4

```python
chdir (path)
```

### Example 5

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.chdir(r"aio")  # relative path
```

### Example 6

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.chdir(r"aio")  # relative path
```

### Example 7

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.chdir(r"/vsis3/u-agu/arcio")  # absolute VSI path
```

### Example 8

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.chdir(r"/vsis3/u-agu/arcio")  # absolute VSI path
```

### Example 9

```python
local_io = AIO(r"C:\data")
local_io.chdir(r"aio")
```

### Example 10

```python
local_io = AIO(r"C:\data")
local_io.chdir(r"aio")
```

### Example 11

```python
close (handle)
```

### Example 12

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.read(size=4)
cloud_io.close(rcsfile)
```

### Example 13

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.read(size=4)
cloud_io.close(rcsfile)
```

### Example 14

```python
copy (src, dst, {options})
```

### Example 15

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.copy(r'/vsis3/data/list/utf8_test.json', 
              r'/vsis3/data/list/new_dir_new/utf8_test.json')
```

### Example 16

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.copy(r'/vsis3/data/list/utf8_test.json', 
              r'/vsis3/data/list/new_dir_new/utf8_test.json')
```

### Example 17

```python
local_io = AIO(r"C:\data")
local_io.copy(r"C:\data\datatest.json", r"C:\data_temp\datatest.json")
```

### Example 18

```python
local_io = AIO(r"C:\data")
local_io.copy(r"C:\data\datatest.json", r"C:\data_temp\datatest.json")
```

### Example 19

```python
copytree (src, dst, {options})
```

### Example 20

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.copytree(r'/vsis3/data/list', r'/vsis3/data/data_new_dir')
```

### Example 21

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.copytree(r'/vsis3/data/list', r'/vsis3/data/data_new_dir')
```

### Example 22

```python
local_io = AIO(r"C:\data")
local_io.copytree(r"C:\data\list", r"C:\data\data_new_dir")
```

### Example 23

```python
local_io = AIO(r"C:\data")
local_io.copytree(r"C:\data\list", r"C:\data\data_new_dir")
```

### Example 24

```python
exists (path)
```

### Example 25

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.exists(r"C:\data\datacloud.acs\data")
```

### Example 26

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.exists(r"C:\data\datacloud.acs\data")
```

### Example 27

```python
getatime (path)
```

### Example 28

```python
local_io = AIO(r"C:\data")
local_io.getatime(r"data.json")
```

### Example 29

```python
local_io = AIO(r"C:\data")
local_io.getatime(r"data.json")
```

### Example 30

```python
getctime (path)
```

### Example 31

```python
local_io = AIO(r"C:\data")
local_io.getctime(r"data.json")
```

### Example 32

```python
local_io = AIO(r"C:\data")
local_io.getctime(r"data.json")
```

### Example 33

```python
getcwd ({type})
```

### Example 34

```python
local_io = AIO()
local_io.getcwd()
```

### Example 35

```python
local_io = AIO()
local_io.getcwd()
```

### Example 36

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getcwd()
```

### Example 37

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getcwd()
```

### Example 38

```python
getmtime (path)
```

### Example 39

```python
local_io = AIO(r"C:\data")
local_io.getmtime(r"data.json")
```

### Example 40

```python
local_io = AIO(r"C:\data")
local_io.getmtime(r"data.json")
```

### Example 41

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getmtime(r"data.json")
```

### Example 42

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getmtime(r"data.json")
```

### Example 43

```python
getpath (path, {type})
```

### Example 44

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getpath('cog.tif', CloudPathType.HTTP)
```

### Example 45

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getpath('cog.tif', CloudPathType.HTTP)
```

### Example 46

```python
getsize (path)
```

### Example 47

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getsize(r'cog.tif')
```

### Example 48

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getsize(r'cog.tif')
```

### Example 49

```python
isdir (path)
```

### Example 50

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.isdir(r'cog')
```

### Example 51

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.isdir(r'cog')
```

### Example 52

```python
isfile (path)
```

### Example 53

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.isfile(r'cog')
```

### Example 54

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.isfile(r'cog')
```

### Example 55

```python
listdir ({path}, {type})
```

### Example 56

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.listdir('data_folder')
```

### Example 57

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.listdir('data_folder')
```

### Example 58

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.listdir('data_folder', CloudPathType.ACS)
```

### Example 59

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.listdir('data_folder', CloudPathType.ACS)
```

### Example 60

```python
local_io = AIO(r"C:\data")
local_io.listdir()
```

### Example 61

```python
local_io = AIO(r"C:\data")
local_io.listdir()
```

### Example 62

```python
makedirs (path)
```

### Example 63

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.makedirs(r"datasensor\datatest\data")
```

### Example 64

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.makedirs(r"datasensor\datatest\data")
```

### Example 65

```python
mkdir (path)
```

### Example 66

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.mkdir(r'cog')
```

### Example 67

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.mkdir(r'cog')
```

### Example 68

```python
open (path, {mode}, {encoding}, {mime})
```

### Example 69

```python
from arcpy import AIO
local_io = AIO(r"C:\data")
rcsfile = local_io.open(r'testfile.txt', 'r')
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 70

```python
from arcpy import AIO
local_io = AIO(r"C:\data")
rcsfile = local_io.open(r'testfile.txt', 'r')
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 71

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'})
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 72

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'})
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 73

```python
# Using with statement (context manager to close the opened file)
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'}) as rcsfile:
    rcsfile.write("This is a test file.")
```

### Example 74

```python
# Using with statement (context manager to close the opened file)
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'}) as rcsfile:
    rcsfile.write("This is a test file.")
```

### Example 75

```python
remove (path)
```

### Example 76

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.remove(r'rcsfile.txt')
```

### Example 77

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.remove(r'rcsfile.txt')
```

### Example 78

```python
local_io = AIO(r"c:\data")
local_io.remove(r'rcsfile.txt')
```

### Example 79

```python
local_io = AIO(r"c:\data")
local_io.remove(r'rcsfile.txt')
```

### Example 80

```python
removefiles (path)
```

### Example 81

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.removefiles(['/vsis3/data/list/to_be_deleted/datatest.json','/vsis3/u-agu/list/to_be_deleted/data_new.json'])
```

### Example 82

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.removefiles(['/vsis3/data/list/to_be_deleted/datatest.json','/vsis3/u-agu/list/to_be_deleted/data_new.json'])
```

### Example 83

```python
local_io = AIO(r"c:\data")
local_io.removefiles([r'C:\data\datatest.json',r'C:\data\data_new.json'])
```

### Example 84

```python
local_io = AIO(r"c:\data")
local_io.removefiles([r'C:\data\datatest.json',r'C:\data\data_new.json'])
```

### Example 85

```python
rename (src, dst)
```

### Example 86

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rename(r'to_be_renamed/cog.tif',r'to_be_renamed/cognew.tif')
```

### Example 87

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rename(r'to_be_renamed/cog.tif',r'to_be_renamed/cognew.tif')
```

### Example 88

```python
local_io = AIO(r"C:\data")
local_io.rename(r'test.json',r'new_test.json')
```

### Example 89

```python
local_io = AIO(r"C:\data")
local_io.rename(r'test.json',r'new_test.json')
```

### Example 90

```python
rmtree (path)
```

### Example 91

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rmtree(r"aio")  # Relative path
```

### Example 92

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rmtree(r"aio")  # Relative path
```

### Example 93

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rmtree(r"/vsis3/data/arcio")  # Absolute VSI path
```

### Example 94

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.rmtree(r"/vsis3/data/arcio")  # Absolute VSI path
```

### Example 95

```python
local_io = AIO(r"C:\data")
local_io.rmtree(r"aio")
```

### Example 96

```python
local_io = AIO(r"C:\data")
local_io.rmtree(r"aio")
```

### Example 97

```python
scandir (path, {depth}, {type})
```

### Example 98

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
# Depth = 0, performs cur dir scanning only
from arcpy import CloudPathType
for item in cloud_io.scandir(r'list', depth=0, type=CloudPathType.HTTP):
    print(item.path)
    print(item.is_dir())
    print(item.is_file())
    ob = item.stat()
    print(ob.st_mode)
    # Cloud specific operations through cloud property
    print(item.cloud.getvsipath())
    print(item.cloud.getpath(CloudPathType.ACS))
```

### Example 99

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
# Depth = 0, performs cur dir scanning only
from arcpy import CloudPathType
for item in cloud_io.scandir(r'list', depth=0, type=CloudPathType.HTTP):
    print(item.path)
    print(item.is_dir())
    print(item.is_file())
    ob = item.stat()
    print(ob.st_mode)
    # Cloud specific operations through cloud property
    print(item.cloud.getvsipath())
    print(item.cloud.getpath(CloudPathType.ACS))
```

### Example 100

```python
local_io = AIO(r"c:\data")
# Depth = -1, performs recursive scanning
for item in local_io.scandir(r'aio', -1):
    print(item.name)
    print(item.path)
    print(item.is_dir())
    print(item.is_file())
    ob = item.stat()
    print(ob.st_mode)
```

### Example 101

```python
local_io = AIO(r"c:\data")
# Depth = -1, performs recursive scanning
for item in local_io.scandir(r'aio', -1):
    print(item.name)
    print(item.path)
    print(item.is_dir())
    print(item.is_file())
    ob = item.stat()
    print(ob.st_mode)
```

### Example 102

```python
# To create an AIO object based on cloud store
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getcwd()
cloud_io.listdir(r'aio') 
# aio is a virtual folder in the cloud store referred in datacloud.acs
```

### Example 103

```python
# To create an AIO object based on cloud store
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.getcwd()
cloud_io.listdir(r'aio') 
# aio is a virtual folder in the cloud store referred in datacloud.acs
```

### Example 104

```python
# To create an AIO object based on local file system
local_io = AIO()
local_io.getcwd()  # Returns the current working directory
```

### Example 105

```python
# To create an AIO object based on local file system
local_io = AIO()
local_io.getcwd()  # Returns the current working directory
```

### Example 106

```python
# To create an AIO object based on local file system with path parameter
local_io = AIO(r"C:\data")  # Set the current working directory as C:\data
local_io.getcwd()  # Return the current working directory that is C:\data
```

### Example 107

```python
# To create an AIO object based on local file system with path parameter
local_io = AIO(r"C:\data")  # Set the current working directory as C:\data
local_io.getcwd()  # Return the current working directory that is C:\data
```

---

## AIODirEntry

## Summary

Contains methods to get the file path and other file attributes of a directory entry.

## Methods

### close ()

Closes the iterator (for cloud AIO only).

### is_dir ()

Verifies whether an entry is a directory.

### is_file ()

Verifies whether an entry is a file.

### stat ()

Gets the stat result of the entry.

## Code Samples

### Example 1

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getvsipath())
```

### Example 2

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getvsipath())
```

### Example 3

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.name)
```

### Example 4

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.name)
```

### Example 5

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.name)
```

### Example 6

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.name)
```

### Example 7

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.name)
```

### Example 8

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.name)
```

### Example 9

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.name)
```

### Example 10

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.name)
```

### Example 11

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.path)
    item.close()
```

### Example 12

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.path)
    item.close()
```

### Example 13

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.is_dir())
```

### Example 14

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.is_dir())
```

### Example 15

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.is_dir())
```

### Example 16

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.is_dir())
```

### Example 17

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.is_file())
```

### Example 18

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.is_file())
```

### Example 19

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.is_file())
```

### Example 20

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    print(item.is_file())
```

### Example 21

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    ob = item.stat()
    print(ob.st_mode)
```

### Example 22

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    ob = item.stat()
    print(ob.st_mode)
```

### Example 23

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    ob = item.stat()
    print(ob.st_mode)
```

### Example 24

```python
local_io = AIO(r"c:\data")
for item in local_io.scandir(r'aio', -1):
    ob = item.stat()
    print(ob.st_mode)
```

---

## AIOFile

## Summary

Contains methods that perform file-related operations such as seek, tell, read, and write.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| size | The number of bytes that will be read. A value of -1 reads all the content. | Integer |
| offset | The number of bytes that will be read. A value of -1 reads all the content.(The default value is -1) | Integer |
| whence | Specifies how the file position indicator will be set. os.SEEK_SET—The position will be set relative to the beginning of the file.os.SEEK_CUR—The position will be set relative to the current file position.os.SEEK_END—The position will be set relative to the end of the file. A nonzero value for os.SEEK_CUR or os.SEEK_END is not supported for local files when the file is opened in a nonbinary mode. | Object |
| b | The data that will be written. | String |

## Methods

### close ()

Flushes and closes the open file handle.

### flush ()

Flushes the write buffers of the file.

### read (size)

Reads data from an object and returns binary or text depending on the opened items.

### rewind ()

Resets the stream position to the start.

### seek (offset, {whence})

Changes the stream position to the specified byte offset.

### tell ()

Returns the current stream position.

### write (b)

Writes data to a local file or cloud object.

## Code Samples

### Example 1

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.clearcache()
```

### Example 2

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.clearcache()
```

### Example 3

```python
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.close()
```

### Example 4

```python
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.close()
```

### Example 5

```python
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.flush()
```

### Example 6

```python
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.flush()
```

### Example 7

```python
read (size)
```

### Example 8

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.read(size=4)
rcsfile.close()
```

### Example 9

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.read(size=4)
rcsfile.close()
```

### Example 10

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r'testfile.txt', 'r') as rcsfile:
    rcsfile.read(size=4)
```

### Example 11

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r'testfile.txt', 'r') as rcsfile:
    rcsfile.read(size=4)
```

### Example 12

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.rewind()
```

### Example 13

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.rewind()
```

### Example 14

```python
seek (offset, {whence})
```

### Example 15

```python
import os
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.seek(offset=6, whence=os.SEEK_CUR)
```

### Example 16

```python
import os
rcsfile = cloud_io.open(r'cog.txt', 'r')
rcsfile.seek(offset=6, whence=os.SEEK_CUR)
```

### Example 17

```python
rcsfile = cloud_io.open(r'cog.tif', 'rb')
print(rcsfile.tell())
```

### Example 18

```python
rcsfile = cloud_io.open(r'cog.tif', 'rb')
print(rcsfile.tell())
```

### Example 19

```python
from arcpy import AIO
local_io = AIO(r"C:\data")
rcsfile = local_io.open(r'testfile.txt', 'r')
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 20

```python
from arcpy import AIO
local_io = AIO(r"C:\data")
rcsfile = local_io.open(r'testfile.txt', 'r')
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 21

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'})
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 22

```python
from arcpy import AIO
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'})
rcsfile.write("This is a test file.")
rcsfile.close()
```

### Example 23

```python
# Using with statement (context manager to close the opened file)
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'}) as rcsfile:
    rcsfile.write("This is a test file.")
```

### Example 24

```python
# Using with statement (context manager to close the opened file)
cloud_io = AIO(r"C:\data\datacloud.acs")
with cloud_io.open(r"C:\data\info\datafile.txt", 'w', mime={'Content-Type': 'text/plain'}) as rcsfile:
    rcsfile.write("This is a test file.")
```

---

## Annotation

## Summary

An Annotation object allows access to the text graphic of an annotation feature.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| cim_version | A string that represents the major version of the CIM.V2—The 2.x version of the CIM will be used.V3—The 3.x version of the CIM will be used.When you return an object's CIM definition, you must specify a cim_version parameter value. Esri follows the semantic versioning specification. This means that at major releases (for example, 3.0), breaking API changes are allowed. The cim_version parameter provides control over the version of the CIM that is used, in the possible event of a breaking change in a future version. If you are authoring scripts for ArcGIS Pro 2.x, specify the cim_version as V2. If you are authoring scripts for ArcGIS Pro 3.x, specify the cim_version as V3. Scripts with a + value of V2 will continue to work in ArcGIS Pro 3.x. | String |
| definition_object | A modified CIM graphic object originally retrieved using the getGraphic method or created using the arcpy.cim.CreateCIMObjectFromClassName function. | Object |

## Methods

### getGraphic (cim_version)

Gets an annotation object's CIM text graphic.

### setGraphic (definition_object)

Sets an annotation object's CIM text graphic.

## Code Samples

### Example 1

```python
getGraphic (cim_version)
```

### Example 2

```python
setGraphic (definition_object)
```

### Example 3

```python
import arcpy

infc = "c:/data/fgdb.gdb/anno_fc"

# Enter a for loop for each feature
with arcpy.da.SearchCursor(infc, ['OID@','ANNO@']) as cursor:
    for row in cursor:
        # Access the current annotation feature's object and access the text
        # graphic
        annoObj = row[1]
        cimTextGraphic = annoObj.getGraphic("V3")

        # Print if a text graphic has a leader line
        print(f'Feature {row[0]} has leader: {len(cimTextGraphic.leaders) > 0}')
```

### Example 4

```python
import arcpy

infc = "c:/data/fgdb.gdb/anno_fc"

# Enter a for loop for each feature
with arcpy.da.SearchCursor(infc, ['OID@','ANNO@']) as cursor:
    for row in cursor:
        # Access the current annotation feature's object and access the text
        # graphic
        annoObj = row[1]
        cimTextGraphic = annoObj.getGraphic("V3")

        # Print if a text graphic has a leader line
        print(f'Feature {row[0]} has leader: {len(cimTextGraphic.leaders) > 0}')
```

### Example 5

```python
import arcpy

infc = "c:/data/fgdb.gdb/anno_fc_1"

# Enter a for loop for each feature
with arcpy.da.UpdateCursor(infc, ['OID@', 'ANNO@']) as cursor:
    for row in cursor:
        # Access the current annotation feature's object and access the text
        # graphic
        annoObj = row[1]
        cimTextGraphic = annoObj.getGraphic("V3")
        cimTextGraphic.symbol.symbol.underline = True
        annoObj.setGraphic(cimTextGraphic)

        row[1] = annoObj
        cursor.updateRow(row)
```

### Example 6

```python
import arcpy

infc = "c:/data/fgdb.gdb/anno_fc_1"

# Enter a for loop for each feature
with arcpy.da.UpdateCursor(infc, ['OID@', 'ANNO@']) as cursor:
    for row in cursor:
        # Access the current annotation feature's object and access the text
        # graphic
        annoObj = row[1]
        cimTextGraphic = annoObj.getGraphic("V3")
        cimTextGraphic.symbol.symbol.underline = True
        annoObj.setGraphic(cimTextGraphic)

        row[1] = annoObj
        cursor.updateRow(row)
```

### Example 7

```python
import arcpy

# Create components for text symbol
fillRGBColor = arcpy.cim.CreateCIMObjectFromClassName('CIMRGBColor', 'V3')
fillRGBColor.values = [0, 0, 0, 50]

symLyr1 = arcpy.cim.CreateCIMObjectFromClassName('CIMSolidFill', 'V3')
symLyr1.color = fillRGBColor

polySym = arcpy.cim.CreateCIMObjectFromClassName('CIMPolygonSymbol', 'V3')
polySym.symbolLayers = [symLyr1]

# Create the text symbol itself and assign values
textSym = arcpy.cim.CreateCIMObjectFromClassName('CIMTextSymbol', 'V3')
textSym.symbol = polySym
textSym.fontFamilyName = "Arial"
textSym.fontStyleName = "Regular"
textSym.height = 10

infc = "c:/data/fgdb.gdb/anno_fc_1"

flds2ins = ["ANNO@"]
with arcpy.da.InsertCursor(infc, flds2ins) as cursor:
    cimSymbolRef = arcpy.cim.CreateCIMObjectFromClassName('CIMSymbolReference', 'V3')
    cimSymbolRef.symbol = textSym

    # Reference symbol 0, this will allow the symbol to be stored as symbol
    # reference + overrides
    cimSymbolRef.symbolName = "0"
    cimTextGraphic = arcpy.cim.CreateCIMObjectFromClassName('CIMTextGraphic', 'V3')
    cimTextGraphic.symbol = cimSymbolRef
    cimTextGraphic.text = "Test Graphic"

    array = arcpy.Array([arcpy.Point(500000.0, -25.0), arcpy.Point(500000.0, -10.5)])
    spatial_reference = arcpy.SpatialReference(26917)
    cimTextGraphic.shape = arcpy.Polyline(array, spatial_reference)

    annoObj = arcpy.Annotation()
    annoObj.setGraphic(cimTextGraphic)
    cursor.insertRow([annoObj])
```

### Example 8

```python
import arcpy

# Create components for text symbol
fillRGBColor = arcpy.cim.CreateCIMObjectFromClassName('CIMRGBColor', 'V3')
fillRGBColor.values = [0, 0, 0, 50]

symLyr1 = arcpy.cim.CreateCIMObjectFromClassName('CIMSolidFill', 'V3')
symLyr1.color = fillRGBColor

polySym = arcpy.cim.CreateCIMObjectFromClassName('CIMPolygonSymbol', 'V3')
polySym.symbolLayers = [symLyr1]

# Create the text symbol itself and assign values
textSym = arcpy.cim.CreateCIMObjectFromClassName('CIMTextSymbol', 'V3')
textSym.symbol = polySym
textSym.fontFamilyName = "Arial"
textSym.fontStyleName = "Regular"
textSym.height = 10

infc = "c:/data/fgdb.gdb/anno_fc_1"

flds2ins = ["ANNO@"]
with arcpy.da.InsertCursor(infc, flds2ins) as cursor:
    cimSymbolRef = arcpy.cim.CreateCIMObjectFromClassName('CIMSymbolReference', 'V3')
    cimSymbolRef.symbol = textSym

    # Reference symbol 0, this will allow the symbol to be stored as symbol
    # reference + overrides
    cimSymbolRef.symbolName = "0"
    cimTextGraphic = arcpy.cim.CreateCIMObjectFromClassName('CIMTextGraphic', 'V3')
    cimTextGraphic.symbol = cimSymbolRef
    cimTextGraphic.text = "Test Graphic"

    array = arcpy.Array([arcpy.Point(500000.0, -25.0), arcpy.Point(500000.0, -10.5)])
    spatial_reference = arcpy.SpatialReference(26917)
    cimTextGraphic.shape = arcpy.Polyline(array, spatial_reference)

    annoObj = arcpy.Annotation()
    annoObj.setGraphic(cimTextGraphic)
    cursor.insertRow([annoObj])
```

---

## ArcSDESQLExecute

## Summary

The ArcSDESQLExecute class provides a means of executing SQL statements via an enterprise geodatabase connection.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| server | Name of the server on which the database is installed or a valid connection file. | String |
| instance | The port number. | String |
| database | Name of the database. | String |
| user | The user name. | String |
| password | The password for the user name. | String |
| sql_statement | The SQL statement.The execute method returns a list of lists in the case where the statement returns rows from a table; for statements that do not return rows, it will return an indication of the success or failure of the statement (True for success; None for failure). Statements that return a single value from a single row will return the value in an appropriate type (string, float, float). | Variant |

## Methods

### commitTransaction ()

No DML statements will be committed until the commitTransaction method is called. Note:A commit may also occur when the connection to the enterprise geodatabase is terminated (check specific DBMS documentation to see how each DBMS deals with a disconnect while in a transaction).

### execute (sql_statement)

Sends the SQL statement to the database via an ArcSDE connection. If execute is run outside of a transaction, a commit will automatically take place once the SQL DML (INSERT, UPDATE, DELETE . . .) statement has been executed.

### rollbackTransaction ()

Rollback any DML operations to the previous commit.

### startTransaction ()

To control when your changes are committed to the database, call the startTransaction method before calling execute. This starts a transaction, and no DML statements will be committed until the commitTransaction method is called.

## Code Samples

### Example 1

```python
ArcSDESQLExecute ({server}, {instance}, {database}, {user}, {password})
```

### Example 2

```python
commitTransaction ()
```

### Example 3

```python
execute (sql_statement)
```

### Example 4

```python
rollbackTransaction ()
```

### Example 5

```python
startTransaction ()
```

### Example 6

```python
import arcpy

# Use a connection file to create the connection
egdb = r'Database Connections\Connection to bedrock.sde'
egdb_conn = arcpy.ArcSDESQLExecute(egdb)

table_name = 'vtest.GDB.Crime'
field_name = 'CRIMETYPE'

sql = '''
SELECT {0}, COUNT({0}) AS f_count FROM {1}
GROUP BY {0}
ORDER BY f_count DESC
'''.format(field_name, table_name)

egdb_return = egdb_conn.execute(sql)
for i in egdb_return:
    print('{}: {}'.format(*i))
```

### Example 7

```python
import arcpy

# Use a connection file to create the connection
egdb = r'Database Connections\Connection to bedrock.sde'
egdb_conn = arcpy.ArcSDESQLExecute(egdb)

table_name = 'vtest.GDB.Crime'
field_name = 'CRIMETYPE'

sql = '''
SELECT {0}, COUNT({0}) AS f_count FROM {1}
GROUP BY {0}
ORDER BY f_count DESC
'''.format(field_name, table_name)

egdb_return = egdb_conn.execute(sql)
for i in egdb_return:
    print('{}: {}'.format(*i))
```

### Example 8

```python
import sys
import arcpy

try:
    # Make data path relative
    arcpy.env.workspace = sys.path[0]

    # Two ways to create the object, which also creates the
    # connection to the enterprise geodatabase.
    # Using the first method, pass a set of strings containing
    # the connection properties:
    #   <serverName>, <portNumber>, <version>, <userName>, <password>
    #   arcpy.ArcSDESQLExecute("gpserver3","5151","#","toolbox","toolbox")
    # Using the second method pass the path to a valid connection file
    egdb_conn = arcpy.ArcSDESQLExecute(r"data\Connection to GPSERVER3.sde")

    # Get the SQL statements, separated by ; from a text string.
    sql_statement = arcpy.GetParameterAsText(0)
    sql_statement_list = sql_statement.split(";")

    print("+++++++++++++++++++++++++++++++++++++++++++++\n")

    # For each SQL statement passed in, execute it.
    for sql in sql_statement_list:
        print("Execute SQL Statement: {0}".format(sql))
        try:
            # Pass the SQL statement to the database.
            egdb_return = egdb_conn.execute(sql)
        except Exception as err:
            print(err)
            egdb_return = False

        # If the return value is a list (a list of lists), display
        # each list as a row from the table being queried.
        if isinstance(egdb_return, list):
            print("Number of rows returned by query: {0} rows".format(
                len(egdb_return)))
            for row in egdb_return:
                print(row)
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")
        else:
            # If the return value was not a list, the statement was
            # most likely a DDL statement. Check its status.
            if egdb_return == True:
                print("SQL statement: {0} ran successfully.".format(sql))
            else:
                print("SQL statement: {0} FAILED.".format(sql))
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")

except Exception as err:
    print(err)
```

### Example 9

```python
import sys
import arcpy

try:
    # Make data path relative
    arcpy.env.workspace = sys.path[0]

    # Two ways to create the object, which also creates the
    # connection to the enterprise geodatabase.
    # Using the first method, pass a set of strings containing
    # the connection properties:
    #   <serverName>, <portNumber>, <version>, <userName>, <password>
    #   arcpy.ArcSDESQLExecute("gpserver3","5151","#","toolbox","toolbox")
    # Using the second method pass the path to a valid connection file
    egdb_conn = arcpy.ArcSDESQLExecute(r"data\Connection to GPSERVER3.sde")

    # Get the SQL statements, separated by ; from a text string.
    sql_statement = arcpy.GetParameterAsText(0)
    sql_statement_list = sql_statement.split(";")

    print("+++++++++++++++++++++++++++++++++++++++++++++\n")

    # For each SQL statement passed in, execute it.
    for sql in sql_statement_list:
        print("Execute SQL Statement: {0}".format(sql))
        try:
            # Pass the SQL statement to the database.
            egdb_return = egdb_conn.execute(sql)
        except Exception as err:
            print(err)
            egdb_return = False

        # If the return value is a list (a list of lists), display
        # each list as a row from the table being queried.
        if isinstance(egdb_return, list):
            print("Number of rows returned by query: {0} rows".format(
                len(egdb_return)))
            for row in egdb_return:
                print(row)
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")
        else:
            # If the return value was not a list, the statement was
            # most likely a DDL statement. Check its status.
            if egdb_return == True:
                print("SQL statement: {0} ran successfully.".format(sql))
            else:
                print("SQL statement: {0} FAILED.".format(sql))
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")

except Exception as err:
    print(err)
```

### Example 10

```python
# WARNING - DO NOT USE ON VERSIONED TABLES OR FEATURE CLASSES.
#   DO NOT USE ON ANY enterprise geodatabase SYSTEM TABLES.
#   DOING SO MAY RESULT IN DATA CORRUPTION.

import sys
import arcpy

try:
    # Make data path relative (not relevant unless data is moved
    # here and paths modified)
    arcpy.env.workspace = sys.path[0]

    # Column name:value that should be in the record.
    sql_values = {"STREET_NAM": "'EUREKA'"}

    # Value that is incorrect if found in the above column.
    bad_val = "'EREKA'"

    #List of tables to look in for the bad value.
    tables = ["streetaddresses_blkA", "streetaddresses_blkB",
              "streetaddresses_blkC"]

    # Two ways to create the object, which also creates the connection
    # to the enterprise geodatabase.
    # Using the first method, pass a set of strings containing the
    #   connection properties:
    #   <serverName>, <portNumber>, <version>, <userName>, <password>
    egdb_conn = arcpy.ArcSDESQLExecute("gpserver3", "5151", "#",
                                      "toolbox", "toolbox")

    # Using the second method pass the path to a valid enterprise geodatabase connection file
    #   arcpy.ArcSDESQLExecute("data\Connection to GPSERVER3.sde")

    for tbl in tables:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for col, val in list(sql_values.items()):
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # Check for the incorrect value in the column for the
            # specific rows. If the table contains the incorrect value,
            # correct it using the update SQL statement.
            print("Analyzing table {0} for bad data: "
                  "Column:{1} Value: {2}".format(tbl, col, bad_val))
            try:
                sql = "select OBJECTID,{0} from {1} where {0} = {2}".format(
                      col, tbl, bad_val)
                print("Attempt to execute SQL Statement: {0}".format(sql))
                egdb_return = egdb_conn.execute(sql)
            except Exception as err:
                print(err)
                egdb_return = False

            if isinstance(egdb_return, list):
                if len(egdb_return) > 0:
                    print("Identified {0} rows with incorrect data. Starting "
                          "transaction for update.".format(len(egdb_return)))
                    # Start the transaction
                    egdb_conn.startTransaction()
                    print("Transaction started...")
                    # Perform the update
                    try:
                        sql = "update {0} set {1}={2} where {1} = {3}".format(
                              tbl, col, val, bad_val)
                        print("Changing bad value: {0} to the good value: "
                              "{1} using update statement:\n {2}".format(
                              bad_val, val, sql))
                        egdb_return = egdb_conn.execute(sql)
                    except Exception as err:
                        print(err)
                        egdb_return = False

                    # If the update completed successfully, commit the
                    # changes.  If not, rollback.
                    if egdb_return == True:
                        print("Update statement: \n"
                              "{0} ran successfully.".format(sql))
                        # Commit the changes
                        egdb_conn.commitTransaction()
                        print("Committed Transaction")

                        # List the changes.
                        try:
                            print("Displaying updated rows for "
                                  "visual inspection.")
                            sql = "select OBJECTID" + \
                                  ",{0} from {1} where {0} = {2}".format(
                                  col, tbl, val)
                            print("Executing SQL Statement: \n{0}".format(sql))
                            egdb_return = egdb_conn.execute(sql)
                        except Exception as err:
                            print(err)
                            egdb_return = False

                        if isinstance(egdb_return, list):
                            print("{0} rows".format(len(egdb_return)))
                            for row in egdb_return:
                                print(row)
                            print("++++++++++++++++++++++++++++++++++++++++\n")
                        else:
                            if egdb_return == True:
                                print("SQL statement: \n{0}\n"
                                      "ran successfully.".format(sql))
                            else:
                                print("SQL statement: \n{0}\n"
                                      "FAILED.".format(sql))
                            print("++++++++++++++++++++++++++++++++++++++++\n")

                        print("++++++++++++++++++++++++++++++++++++++++\n")
                    else:
                        print("SQL statement: \n{0}\nFAILED. "
                              "Rolling back all changes.".format(sql))
                        # Rollback changes
                        egdb_conn.rollbackTransaction()
                        print("Rolled back any changes.")
                        print("++++++++++++++++++++++++++++++++++++++++\n")
            else:
                print "No records required updating."

    # Disconnect and exit
    del egdb_conn
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

except Exception as err:
    print(err)
```

### Example 11

```python
# WARNING - DO NOT USE ON VERSIONED TABLES OR FEATURE CLASSES.
#   DO NOT USE ON ANY enterprise geodatabase SYSTEM TABLES.
#   DOING SO MAY RESULT IN DATA CORRUPTION.

import sys
import arcpy

try:
    # Make data path relative (not relevant unless data is moved
    # here and paths modified)
    arcpy.env.workspace = sys.path[0]

    # Column name:value that should be in the record.
    sql_values = {"STREET_NAM": "'EUREKA'"}

    # Value that is incorrect if found in the above column.
    bad_val = "'EREKA'"

    #List of tables to look in for the bad value.
    tables = ["streetaddresses_blkA", "streetaddresses_blkB",
              "streetaddresses_blkC"]

    # Two ways to create the object, which also creates the connection
    # to the enterprise geodatabase.
    # Using the first method, pass a set of strings containing the
    #   connection properties:
    #   <serverName>, <portNumber>, <version>, <userName>, <password>
    egdb_conn = arcpy.ArcSDESQLExecute("gpserver3", "5151", "#",
                                      "toolbox", "toolbox")

    # Using the second method pass the path to a valid enterprise geodatabase connection file
    #   arcpy.ArcSDESQLExecute("data\Connection to GPSERVER3.sde")

    for tbl in tables:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for col, val in list(sql_values.items()):
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            # Check for the incorrect value in the column for the
            # specific rows. If the table contains the incorrect value,
            # correct it using the update SQL statement.
            print("Analyzing table {0} for bad data: "
                  "Column:{1} Value: {2}".format(tbl, col, bad_val))
            try:
                sql = "select OBJECTID,{0} from {1} where {0} = {2}".format(
                      col, tbl, bad_val)
                print("Attempt to execute SQL Statement: {0}".format(sql))
                egdb_return = egdb_conn.execute(sql)
            except Exception as err:
                print(err)
                egdb_return = False

            if isinstance(egdb_return, list):
                if len(egdb_return) > 0:
                    print("Identified {0} rows with incorrect data. Starting "
                          "transaction for update.".format(len(egdb_return)))
                    # Start the transaction
                    egdb_conn.startTransaction()
                    print("Transaction started...")
                    # Perform the update
                    try:
                        sql = "update {0} set {1}={2} where {1} = {3}".format(
                              tbl, col, val, bad_val)
                        print("Changing bad value: {0} to the good value: "
                              "{1} using update statement:\n {2}".format(
                              bad_val, val, sql))
                        egdb_return = egdb_conn.execute(sql)
                    except Exception as err:
                        print(err)
                        egdb_return = False

                    # If the update completed successfully, commit the
                    # changes.  If not, rollback.
                    if egdb_return == True:
                        print("Update statement: \n"
                              "{0} ran successfully.".format(sql))
                        # Commit the changes
                        egdb_conn.commitTransaction()
                        print("Committed Transaction")

                        # List the changes.
                        try:
                            print("Displaying updated rows for "
                                  "visual inspection.")
                            sql = "select OBJECTID" + \
                                  ",{0} from {1} where {0} = {2}".format(
                                  col, tbl, val)
                            print("Executing SQL Statement: \n{0}".format(sql))
                            egdb_return = egdb_conn.execute(sql)
                        except Exception as err:
                            print(err)
                            egdb_return = False

                        if isinstance(egdb_return, list):
                            print("{0} rows".format(len(egdb_return)))
                            for row in egdb_return:
                                print(row)
                            print("++++++++++++++++++++++++++++++++++++++++\n")
                        else:
                            if egdb_return == True:
                                print("SQL statement: \n{0}\n"
                                      "ran successfully.".format(sql))
                            else:
                                print("SQL statement: \n{0}\n"
                                      "FAILED.".format(sql))
                            print("++++++++++++++++++++++++++++++++++++++++\n")

                        print("++++++++++++++++++++++++++++++++++++++++\n")
                    else:
                        print("SQL statement: \n{0}\nFAILED. "
                              "Rolling back all changes.".format(sql))
                        # Rollback changes
                        egdb_conn.rollbackTransaction()
                        print("Rolled back any changes.")
                        print("++++++++++++++++++++++++++++++++++++++++\n")
            else:
                print "No records required updating."

    # Disconnect and exit
    del egdb_conn
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

except Exception as err:
    print(err)
```

---

## Array

## Summary

The array object can contain points and arrays and is used to construct geometry objects.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| items | Items can include a Point object, another Array object, or any iterable object that returns Point objects. | Object |
| value | Either a Point or Array object can be appended to the array. | Object |
| value | Either a Point or Array object can be appended to the array. | Object |
| point_object | A Point object. | Point |
| items | Extends the array by adding strings, integers, or lists. | Object |
| index | The index position of the array. | Integer |
| index | The index position of the Array object. | Integer |
| value | The Point or Array object to be inserted. | Object |
| index | The index position that will be removed. | Integer |
| index | The index position that will be replaced. | Integer |
| value | The new Point or Array object to be added to the Array object. | Object |

## Methods

### add (value)

Adds a Point or Array object to the end of the array.

### append (value)

Appends an object to the array in the last position.

### clone (point_object)

Clone the Point object.

### extend (items)

Extends the array by appending elements.

### getObject (index)

Returns the object at the given index position in the array. The getObject method is equivalent to indexing an object; that is, obj.getObject(0) is equivalent to obj[0].

### insert (index, value)

Adds an object to the Array object at the specified index.

### next ()

Returns the next object at the current index.

### remove (index)

Removes the object at the specified index position from the array.

### removeAll ()

Removes all values and creates an empty object.

### replace (index, value)

Replaces the object at the specified index position in the Array object.

### reset ()

Sets the current enumeration index (used by the next method) back to the first element.

## Code Samples

### Example 1

```python
Array  ({items})
```

### Example 2

```python
add (value)
```

### Example 3

```python
append (value)
```

### Example 4

```python
clone (point_object)
```

### Example 5

```python
extend (items)
```

### Example 6

```python
getObject (index)
```

### Example 7

```python
insert (index, value)
```

### Example 8

```python
remove (index)
```

### Example 9

```python
removeAll ()
```

### Example 10

```python
replace (index, value)
```

### Example 11

```python
import arcpy

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Polyline objects
features = []

for feature in feature_info:
    # Create a Polyline object based on the array of points
    # Append to the list of Polyline objects
    features.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/geometry/polylines.shp")
```

### Example 12

```python
import arcpy

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Polyline objects
features = []

for feature in feature_info:
    # Create a Polyline object based on the array of points
    # Append to the list of Polyline objects
    features.append(
        arcpy.Polyline(
            arcpy.Array([arcpy.Point(*coords) for coords in feature])))

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/geometry/polylines.shp")
```

---

## Chart

## Summary

The Chart class defines an ArcGIS Pro chart. The class allows you to create various types of charts, including bar charts, line charts, scatterplots, scatterplot matrices, QQ plots, histograms, box plots, and data clocks. The class can also be used to define the chart title, axes, and other properties.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The name of the chart. A chart must have a unique name per layer. This name is only used for identification; it is not displayed. | String |
| layer_or_layerfile | The chart will be added to the target object. This argument can be a Layer or Table object. | Object |
| path | The path where the chart will be exported in SVG format. | String |
| width | The width of the output graphic. | Integer |
| height | The height of the output graphic. | Integer |

## Methods

### addToLayer (layer_or_layerfile)

The addToLayer method adds the chart object to a layer or table view.

### exportToSVG (path, width, height)

The exportToSVG method exports the chart to SVG format.

### updateChart ()

The updateChart method updates chart properties to sync changes between the object and the chart previously added to a layer.

## Code Samples

### Example 1

```python
Chart (name)
```

### Example 2

```python
addToLayer (layer_or_layerfile)
```

### Example 3

```python
import arcpy

# Insert creation of chart object here
...

aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
censusLayer = map.listLayers('Census Block Groups')[0]

# Add chart object to a layer
chart.addToLayer(censusLayer)
```

### Example 4

```python
import arcpy

# Insert creation of chart object here
...

aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
censusLayer = map.listLayers('Census Block Groups')[0]

# Add chart object to a layer
chart.addToLayer(censusLayer)
```

### Example 5

```python
exportToSVG (path, width, height)
```

### Example 6

```python
import arcpy

# Insert creation of chart object here
...

aprx = arcpy.mp.ArcGISProject('current')
censusLayer = aprx.listMaps()[0].listLayers('Census Block Groups')[0]

# Set data source of chart object to a layer in current project
chart.dataSource = censusLayer

# Save the chart to file with dimensions width=500, height=500
chart.exportToSVG('populationByState.svg', 500, 500)
```

### Example 7

```python
import arcpy

# Insert creation of chart object here
...

aprx = arcpy.mp.ArcGISProject('current')
censusLayer = aprx.listMaps()[0].listLayers('Census Block Groups')[0]

# Set data source of chart object to a layer in current project
chart.dataSource = censusLayer

# Save the chart to file with dimensions width=500, height=500
chart.exportToSVG('populationByState.svg', 500, 500)
```

### Example 8

```python
import arcpy

# Insert creation of chart object here
...

featureServiceURL = r'https://services1.arcgis.com/hLJbHVT9ZrDIzK0I/arcgis/rest/services/CrimesChiTheft/FeatureServer/0'

# Set data source of chart object to a feature service URL
chart.dataSource = featureServiceURL

# Save the chart to file with dimensions width=800, height=600
chart.exportToSVG('theftsPerBeat.svg', 800, 600)
```

### Example 9

```python
import arcpy

# Insert creation of chart object here
...

featureServiceURL = r'https://services1.arcgis.com/hLJbHVT9ZrDIzK0I/arcgis/rest/services/CrimesChiTheft/FeatureServer/0'

# Set data source of chart object to a feature service URL
chart.dataSource = featureServiceURL

# Save the chart to file with dimensions width=800, height=600
chart.exportToSVG('theftsPerBeat.svg', 800, 600)
```

### Example 10

```python
updateChart ()
```

### Example 11

```python
import arcpy

# Insert creation of chart object here
...

chart.addToLayer(myLayer)

# Further modification is necessary
chart.description = "Data from the U.S. Census Bureau"
chart.updateChart()
```

### Example 12

```python
import arcpy

# Insert creation of chart object here
...

chart.addToLayer(myLayer)

# Further modification is necessary
chart.description = "Data from the U.S. Census Bureau"
chart.updateChart()
```

### Example 13

```python
import arcpy

aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
censusLayer = map.listLayers('Census Block Groups')[0]
chart = arcpy.Chart('MyChart')

chart.type = 'scatter'
chart.title = 'Relationship between Percent Vacant (Housing) and Population Density'
chart.description = 'This chart examines the relationship between housing vacancy and population density.'
chart.xAxis.field = 'Per_Vacant'
chart.yAxis.field = 'Pop_Density'
chart.xAxis.title = 'Vacant Housing %'
chart.yAxis.title = 'Population Density (per Sq. Mile)'
chart.addToLayer(censusLayer)
```

### Example 14

```python
import arcpy

aprx = arcpy.mp.ArcGISProject("current")
map = aprx.listMaps()[0]
censusLayer = map.listLayers('Census Block Groups')[0]
chart = arcpy.Chart('MyChart')

chart.type = 'scatter'
chart.title = 'Relationship between Percent Vacant (Housing) and Population Density'
chart.description = 'This chart examines the relationship between housing vacancy and population density.'
chart.xAxis.field = 'Per_Vacant'
chart.yAxis.field = 'Pop_Density'
chart.xAxis.title = 'Vacant Housing %'
chart.yAxis.title = 'Population Density (per Sq. Mile)'
chart.addToLayer(censusLayer)
```

### Example 15

```python
import arcpy
import csv

temp_csv_file = r'c:\temp\data.csv'
out_svg_file = r'c:\temp\chart.svg'
# Data for automobile miles per gallon (MPG) and horsepower 
columns = ['mpg', 'horsepower'] 
data = [
    [18, 130], 
    [15, 165], 
    [26, 113],
    [18, 150],
    [28, 90], 
    [32, 61],
    [16, 150],
    [17, 140]
]

# Write this list to a .csv file
with open(temp_csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Write column headers
    writer.writerow(columns)
    
    # Write data rows
    writer.writerows(data)

chart = arcpy.Chart('MyChart')
chart.type = 'scatter'
chart.title = 'Relationship between MPG and Horsepower'
chart.xAxis.field = 'mpg'
chart.yAxis.field = 'horsepower'
chart.dataSource = temp_csv_file
chart.exportToSVG(out_svg_file, width=750, height=400)
```

### Example 16

```python
import arcpy
import csv

temp_csv_file = r'c:\temp\data.csv'
out_svg_file = r'c:\temp\chart.svg'
# Data for automobile miles per gallon (MPG) and horsepower 
columns = ['mpg', 'horsepower'] 
data = [
    [18, 130], 
    [15, 165], 
    [26, 113],
    [18, 150],
    [28, 90], 
    [32, 61],
    [16, 150],
    [17, 140]
]

# Write this list to a .csv file
with open(temp_csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Write column headers
    writer.writerow(columns)
    
    # Write data rows
    writer.writerows(data)

chart = arcpy.Chart('MyChart')
chart.type = 'scatter'
chart.title = 'Relationship between MPG and Horsepower'
chart.xAxis.field = 'mpg'
chart.yAxis.field = 'horsepower'
chart.dataSource = temp_csv_file
chart.exportToSVG(out_svg_file, width=750, height=400)
```

---

## CloudDirEntryOp

## Summary

Gets the file path and other file attributes of a directory entry from the cloud.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| type | Specifies the path style that will be used for the returned URI (for cloud only). The data type is CloudPathType.Use the following options from the CloudPathType enumeration: CloudPathType.VSI, CloudPathType.ACS, CloudPathType.HTTP, and CloudPathType.CLOUDSTORES.(The default value is CloudPathType.VSI) | Object |

## Methods

### getpath ({type})

Gets the absolute path of the entry in CloudPathType format.

### getvsipath ()

Gets the absolute path of the entry in VSI format.

## Code Samples

### Example 1

```python
getpath ({type})
```

### Example 2

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getpath(CloudPathType.ACS))
```

### Example 3

```python
from arcpy import CloudPathType
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getpath(CloudPathType.ACS))
```

### Example 4

```python
getvsipath ()
```

### Example 5

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getvsipath())
```

### Example 6

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
for item in cloud_io.scandir(r'list', depth=0):
    print(item.cloud.getvsipath())
```

---

## CloudFileOp

## Summary

Performs file related operations that are cloud specific.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| blocksize | The block size.(The default value is 32768) | Integer |
| cachesize | The cache size.(The default value is 0) | Integer |

## Methods

### clearcache ()

Clears file properties and BLOB region cache. Call this method when an external process updates the file.

### usebufferedreader ()

Caches last read bytes.

### usecachedfile ({blocksize}, {cachesize})

Uses least recently used (LRU) block cache for handling files on cloud.

## Code Samples

### Example 1

```python
clearcache ()
```

### Example 2

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.clearcache()
```

### Example 3

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.clearcache()
```

### Example 4

```python
usebufferedreader ()
```

### Example 5

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.usebufferedreader()
```

### Example 6

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.usebufferedreader()
```

### Example 7

```python
usecachedfile ({blocksize}, {cachesize})
```

### Example 8

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.usecachedfile(blocksize=32768, cachesize=0)
```

### Example 9

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
rcsfile = cloud_io.open(r'testfile.txt', 'r')
rcsfile.cloud.usecachedfile(blocksize=32768, cachesize=0)
```

---

## CloudOp

## Summary

Contains IO methods that are cloud specific.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| src | The relative path from the current working directory or an absolute vsi cloud path. | String |
| dst | The local, or target, path of the file. | String |
| options | Specifies the options that will be used.RECURSIVE—Subdirectories and their contents will be recursively copied. This option is only applicable for folder operations.SYNC_STRATEGY—The criteria that will be used for overwriting if the target file exists.NUM_THREADS—The number of threads that will be used for parallel file copying.CHUNK_SIZE—The maximum chunk size (in bytes) that will be used to split large objects when uploading or downloading.Syntax—RECURSIVE=[YES\|NO], SYNC_STRATEGY=[TIMESTAMP\|ETAG\|OVERWRITE], NUM_THREADS=(integer) CHUNK_SIZE=(integer) [x-amz-*\|x-goog-*\|x-ms-*=(value)]Example—{'RECURSIVE':'YES', 'SYNC_STRATEGY':'OVERWRITE', 'NUM_THREADS':'10', 'CHUNK_SIZE':'8'}(The default value is None) | Dictionary |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| domain | The metadata domain, for example, (https://gdal.org/api/cpl.html#_CPPv418VSIGetFileMetadataPKcPKc12CSLConstList).(The default value is None) | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| expiry | The expiry time in seconds. | Integer |
| upload | Specifies whether the URL will be generated for upload. If True, the URL will be generated.(The default value is False) | Boolean |
| src | The local (source) path of the file. | String |
| dst | The relative path from the current working directory or an absolute vsi cloud path. | String |
| options | Specifies the options that will be used.RECURSIVE—Subdirectories and their contents will be recursively copied. This option is only applicable to folder operations.SYNC_STRATEGY—The criteria that will be used for overwriting if the target file exists.NUM_THREADS—The number of threads that will be used for parallel file copying.CHUNK_SIZE—The maximum chunk size (in bytes) that will be used to split large objects when uploading or downloading.Syntax—RECURSIVE=[YES\|NO], SYNC_STRATEGY=[TIMESTAMP\|ETAG\|OVERWRITE], NUM_THREADS=(integer) CHUNK_SIZE=(integer) [x-amz-*\|x-goog-*\|x-ms-*=(value)]Example—{'RECURSIVE':'YES', 'SYNC_STRATEGY':'OVERWRITE', 'NUM_THREADS':'10', 'CHUNK_SIZE':'8'}(The default value is None) | Dictionary |
| path | The relative path from the current working directory or an absolute path (absolute vsi path for cloud). | String |
| domain | The metadata domain, for example, (https://gdal.org/api/cpl.html#_CPPv418VSISetFileMetadataPKc12CSLConstListPKc12CSLConstList).(The default value is None) | String |
| metadata | The metadata that will be set.(The default value is None) | Dictionary |
| options | The options that will be used to set the metadata.(The default value is None) | Dictionary |
| certificate | Specifies whether the SSL certificate and Online Certificate Status Protocol (OCSP) certificate check will be verified. | Boolean |
| stat | Specifies whether stat on the root container or connected folder will be tested. | Boolean |
| list | Specifies whether list directory access will be tested. | Boolean |
| read | Specifies whether the read file permission will be tested. | Boolean |
| modify | Specifies whether the write and delete permissions will be tested. If delete access is denied, a test file will remain on the cloud. | Boolean |
| path | The path to the file that will be used for the read test. If no value is provided, the first entry from the current directory listing will be used. | String |

## Methods

### clearcache (path)

Clears in-memory directory listings, file properties, and BLOB region cache. Call this method when an external process updates folders or files in the cloud store that were previously accessed.

### getbucketname ()

Gets the name of a connected bucket or container.

### getendpoint (path)

Gets the cloud endpoint specified in the connection.

### getfile (src, dst, {options})

Downloads a file from the cloud.

### getmetadata (path, {domain})

Gets the metadata of a file or folder.

### getobjectstorepath ()

Gets the root path of the connection.

### getproperties (path)

Gets the header properties.

### getprovidername ()

Gets the cloud provider name.

### getprovideroptions ()

Gets the provider options specified in the connection.

### getregion ()

Gets the cloud region specified in the connection.

### getsignedurl (path, expiry, {upload})

Generates a temporary HTTP presigned URL.

### putfile (src, dst, {options})

Uploads a file to cloud.

### setmetadata (path, {domain}, {metadata}, {options})

Sets the metadata of a file or folder.

### validate ({certificate}, {stat}, {list}, {read}, {modify}, {path})

Tests the cloud connection for various file operations. Available permissions may be granular depending on the server ACL configuration.

## Code Samples

### Example 1

```python
clearcache (path)
```

### Example 2

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.clearcache(r"aio")
```

### Example 3

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.clearcache(r"aio")
```

### Example 4

```python
getbucketname ()
```

### Example 5

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getbucketname()
```

### Example 6

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getbucketname()
```

### Example 7

```python
getendpoint (path)
```

### Example 8

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getendpoint()
```

### Example 9

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getendpoint()
```

### Example 10

```python
getfile (src, dst, {options})
```

### Example 11

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getfile(r'utf8_test.json', r"c:\data\datafile.json")
```

### Example 12

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getfile(r'utf8_test.json', r"c:\data\datafile.json")
```

### Example 13

```python
getmetadata (path, {domain})
```

### Example 14

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getmetadata(r'aio')
```

### Example 15

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getmetadata(r'aio')
```

### Example 16

```python
getobjectstorepath ()
```

### Example 17

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getobjectstorepath()
```

### Example 18

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getobjectstorepath()
```

### Example 19

```python
getproperties (path)
```

### Example 20

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getproperties(r'aio')
```

### Example 21

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getproperties(r'aio')
```

### Example 22

```python
getprovidername ()
```

### Example 23

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovidername()
```

### Example 24

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovidername()
```

### Example 25

```python
getprovideroptions ()
```

### Example 26

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovideroptions()
```

### Example 27

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getprovideroptions()
```

### Example 28

```python
getregion ()
```

### Example 29

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getregion()
```

### Example 30

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getregion()
```

### Example 31

```python
getsignedurl (path, expiry, {upload})
```

### Example 32

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getsignedurl(r'data.json', 5)
```

### Example 33

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.getsignedurl(r'data.json', 5)
```

### Example 34

```python
putfile (src, dst, {options})
```

### Example 35

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.putfile(r"C:\data\data_file.json", r'data_folder\data_file_new.json')
```

### Example 36

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.putfile(r"C:\data\data_file.json", r'data_folder\data_file_new.json')
```

### Example 37

```python
setmetadata (path, {domain}, {metadata}, {options})
```

### Example 38

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.setmetadata(
    r"cog.tif",
    "HEADERS",
    {
        "x-amz-id-2": "HxM4BcALW+HnJ13owxzMpeQXXI59VKK3I9zujbqyLBCinCt6prnzKXR4Ixhb/AloFVJLGtuqKG7nSLCLaxObTw==",
        "x-amz-request-id": "KYTDPC2WH2ZQK2D2",
        "Date": "Tue, 13 Jun 2023 13:39:33 GMT",
        "Last-Modified": "Wed, 16 Sep 2020 13:49:34 GMT",
        "ETag": '"c220c099c46c60703de0c55763d04371"',
        "x-amz-meta-s3b-last-modified": "20171213T210220Z",
        "Content-Disposition": "attachment",
        "Accept-Ranges": "bytes",
        "Content-Range": "bytes 0-16383/4339079",
        "Content-Type": "text/plain",
        "Server": "AmazonS3",
        "Content-Length": "4545",
    },
)
```

### Example 39

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.setmetadata(
    r"cog.tif",
    "HEADERS",
    {
        "x-amz-id-2": "HxM4BcALW+HnJ13owxzMpeQXXI59VKK3I9zujbqyLBCinCt6prnzKXR4Ixhb/AloFVJLGtuqKG7nSLCLaxObTw==",
        "x-amz-request-id": "KYTDPC2WH2ZQK2D2",
        "Date": "Tue, 13 Jun 2023 13:39:33 GMT",
        "Last-Modified": "Wed, 16 Sep 2020 13:49:34 GMT",
        "ETag": '"c220c099c46c60703de0c55763d04371"',
        "x-amz-meta-s3b-last-modified": "20171213T210220Z",
        "Content-Disposition": "attachment",
        "Accept-Ranges": "bytes",
        "Content-Range": "bytes 0-16383/4339079",
        "Content-Type": "text/plain",
        "Server": "AmazonS3",
        "Content-Length": "4545",
    },
)
```

### Example 40

```python
validate ({certificate}, {stat}, {list}, {read}, {modify}, {path})
```

### Example 41

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.validate(True, True, True, True)
```

### Example 42

```python
cloud_io = AIO(r"C:\data\datacloud.acs")
cloud_io.cloud.validate(True, True, True, True)
```

---

## CrossValidationResult

## Summary

The CrossValidationResult class is returned by the Cross Validation tool and contains access to the cross-validation results that can be generated for any geostatistical layer.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| index | The index position of the input as an integer, or the parameter name. | Variant |
| parameter_list | The parameters on which the map service image will be based. | Integer |
| height | The height of the image. | Double |
| width | The width of the image. | Double |
| resolution | The resolution of the image. | Double |
| index | The index position of the message. | Integer |
| severity | The type of messages to be returned.0—Informative, warning, and error messages are returned.1—Only warning messages are returned.2—Only error messages are returned.Not specifying a severity level will return all types of messages.(The default value is 0) | Integer |
| index | The index position of the output as an integer, or the parameter name. | Variant |
| index | The message index position. | Integer |

## Methods

### cancel ()

Cancels an associated job

### getInput (index)

Returns a given input, either as a string or a RecordSet object.

### getMapImageURL ({parameter_list}, {height}, {width}, {resolution})

Returns a map service image for a given output, if one exists.

### getMessage (index)

Returns a specific message by index position.

### getMessages ({severity})

Returns the geoprocessing tool messages.

### getOutput (index)

Returns a given output, either as a RecordSet object or a string.If the output of the tool, such as Make Feature Layer, is a layer, getOutput will return a Layer object.

### getSeverity (index)

Returns the severity of a specific message.

## Code Samples

### Example 1

```python
getInput (index)
```

### Example 2

```python
getMapImageURL ({parameter_list}, {height}, {width}, {resolution})
```

### Example 3

```python
getMessage (index)
```

### Example 4

```python
getMessages ({severity})
```

### Example 5

```python
getOutput (index)
```

### Example 6

```python
getSeverity (index)
```

### Example 7

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
cvResult = arcpy.CrossValidation_ga("C:/gapyexamples/data/kriging.lyr")
print("Root Mean Square error = " + str(cvResult.rootMeanSquare))
```

### Example 8

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
cvResult = arcpy.CrossValidation_ga("C:/gapyexamples/data/kriging.lyr")
print("Root Mean Square error = " + str(cvResult.rootMeanSquare))
```

### Example 9

```python
# Name: CrossValidation_Example_02.py
# Description: Perform cross validation on an input geostatistical layer.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"

# Execute CrossValidation
cvResult = arcpy.CrossValidation_ga(inLayer)
print("Root Mean Square error = " + str(cvResult.rootMeanSquare))
```

### Example 10

```python
# Name: CrossValidation_Example_02.py
# Description: Perform cross validation on an input geostatistical layer.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"

# Execute CrossValidation
cvResult = arcpy.CrossValidation_ga(inLayer)
print("Root Mean Square error = " + str(cvResult.rootMeanSquare))
```

---

## Cursor

## Summary

A cursor is a data access object that can be used to iterate through the set of rows in a table or to insert new rows into a table. Cursors have three forms: search, insert, or update. Cursors are commonly used to read and update attributes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| row | The row to be deleted. | Row |
| row | The row to be inserted. | Row |
| row | The row used to update the current position of the cursor. | Row |

## Methods

### deleteRow (row)

Deletes a row in the database. The row corresponding to the current position of the cursor will be deleted.

### insertRow (row)

Inserts a new row into the database.

### newRow ()

Creates an empty Row object.

### next ()

Returns the next object at the current index.

### reset ()

Sets the current enumeration index (used by the next method) back to the first element.

### updateRow (row)

The updateRow method can be used to update the row at the current position of an update cursor.

## Code Samples

### Example 1

```python
deleteRow (row)
```

### Example 2

```python
insertRow (row)
```

### Example 3

```python
updateRow (row)
```

### Example 4

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Create the search cursor
cursor = arcpy.SearchCursor("roads", '"TYPE" <> 4')

# Iterate through the rows in the cursor
for row in cursor:
    print("Name: {0},  CFCC code: {1}".format(row.NAME, row.CFCC))

del cursor, row
```

### Example 5

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Create the search cursor
cursor = arcpy.SearchCursor("roads", '"TYPE" <> 4')

# Iterate through the rows in the cursor
for row in cursor:
    print("Name: {0},  CFCC code: {1}".format(row.NAME, row.CFCC))

del cursor, row
```

### Example 6

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Create the update cursor
cursor = arcpy.UpdateCursor("roads")

# Update the road buffer distance field based on road type.
#   Road type is either 1,2,3,4  Distance is in meters.
for row in cursor:
    row.setValue("BUFFER_DIST", row.getValue("TYPE") * 100)
    cursor.updateRow(row)

# Delete cursor and row objects
del cursor, row
```

### Example 7

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/base/data.gdb"

# Create the update cursor
cursor = arcpy.UpdateCursor("roads")

# Update the road buffer distance field based on road type.
#   Road type is either 1,2,3,4  Distance is in meters.
for row in cursor:
    row.setValue("BUFFER_DIST", row.getValue("TYPE") * 100)
    cursor.updateRow(row)

# Delete cursor and row objects
del cursor, row
```

### Example 8

```python
import datetime
import arcpy

# Create insert cursor for table
cursor = arcpy.InsertCursor("c:/base/data.gdb/roads_maint")

# Create 25 new rows. Set default values on distance and CFCC code
for i in range(1000, 1025):
    row = cursor.newRow()
    row.setValue('rowid', i)
    row.setValue('distance', 100)
    row.setValue('CFCC', 'A10')
    row.setValue('LastInsp', datetime.datetime.now())
    cursor.insertRow(row)

# Delete cursor and row objects
del cursor, row
```

### Example 9

```python
import datetime
import arcpy

# Create insert cursor for table
cursor = arcpy.InsertCursor("c:/base/data.gdb/roads_maint")

# Create 25 new rows. Set default values on distance and CFCC code
for i in range(1000, 1025):
    row = cursor.newRow()
    row.setValue('rowid', i)
    row.setValue('distance', 100)
    row.setValue('CFCC', 'A10')
    row.setValue('LastInsp', datetime.datetime.now())
    cursor.insertRow(row)

# Delete cursor and row objects
del cursor, row
```

---

## env

## Summary

Environment settings are exposed as properties on the env class. Geoprocessing environment settings can be thought of as additional parameters that affect a tool's results.

---

## EnvManager

## Summary

EnvManager is a class for managing geoprocessing environments.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| **kwargs | Environment settings are passed as keyword arguments; one or more environments can be passed using the environment name. with arcpy.EnvManager(cellSize=10, extent='-16, 25, 44, 64'): # Code to be run with the environments setFor a complete list of the environments and their names, see the env class. | Variant |

## Methods

### reset ()

Resets the environment settings to their values prior to calling EnvManager.

## Code Samples

### Example 1

```python
EnvManager (**kwargs)
```

### Example 2

```python
with arcpy.EnvManager(cellSize=10, extent='-16, 25, 44, 64'):
    # Code to be run with the environments set
```

### Example 3

```python
with arcpy.EnvManager(cellSize=10, extent='-16, 25, 44, 64'):
    # Code to be run with the environments set
```

### Example 4

```python
import arcpy
feature_class = r'd:\data\data.gdb\cities'

with arcpy.EnvManager(cellSize=10, extent='-16, 25, 44, 64'):
    raster = arcpy.sa.PointDensity(feature_class, 'POP_RANK')
```

### Example 5

```python
import arcpy
feature_class = r'd:\data\data.gdb\cities'

with arcpy.EnvManager(cellSize=10, extent='-16, 25, 44, 64'):
    raster = arcpy.sa.PointDensity(feature_class, 'POP_RANK')
```

### Example 6

```python
import arcpy

with arcpy.EnvManager(workspace=r'd:\data\data.gdb'):
    feature_classes = arcpy.ListFeatureClasses(feature_type='POLYGON')

print('The polygon feature classes are {}'.format(', '.join(feature_classes)))
```

### Example 7

```python
import arcpy

with arcpy.EnvManager(workspace=r'd:\data\data.gdb'):
    feature_classes = arcpy.ListFeatureClasses(feature_type='POLYGON')

print('The polygon feature classes are {}'.format(', '.join(feature_classes)))
```

---

## ExecuteError

## Summary

The ExecuteError exception class is raised whenever a geoprocessing tool encounters an error.

## Code Samples

### Example 1

```python
import arcpy

in_features = "c:/base/transport.gdb/roads"

try:
    # Note: CopyFeatures will always fail if the input and output are
    # the same feature class
    arcpy.CopyFeatures_management(in_features, in_features)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())
```

### Example 2

```python
import arcpy

in_features = "c:/base/transport.gdb/roads"

try:
    # Note: CopyFeatures will always fail if the input and output are
    # the same feature class
    arcpy.CopyFeatures_management(in_features, in_features)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())
```

---

## ExecuteWarning

## Summary

The ExecuteWarning exception class is raised when a geoprocessing tool encounters a warning, and the SetSeverityLevel function has updated the severity level to 1. Setting the severity level to 1 instructs arcpy to throw the ExecuteWarning exception when a warning is encountered.

## Code Samples

### Example 1

```python
import arcpy

try:
    # If a tool produces a warning, it will throw an exception
    arcpy.SetSeverityLevel(1)

    # Note: DeleteFeatures on a feature class will always return a warning
    arcpy.DeleteFeatures_management("c:/base/transport.gdb/roads")

except arcpy.ExecuteWarning:
    print(arcpy.GetMessages())
```

### Example 2

```python
import arcpy

try:
    # If a tool produces a warning, it will throw an exception
    arcpy.SetSeverityLevel(1)

    # Note: DeleteFeatures on a feature class will always return a warning
    arcpy.DeleteFeatures_management("c:/base/transport.gdb/roads")

except arcpy.ExecuteWarning:
    print(arcpy.GetMessages())
```

---

## Extent

## Summary

An extent is a rectangle specified by providing the coordinate of the lower left corner and the coordinate of the upper right corner in map units.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| XMin | The extent XMin value. | Double |
| YMin | The extent YMin value. | Double |
| XMax | The extent XMax value. | Double |
| YMax | The extent YMax value. | Double |
| ZMin | The extent ZMin value. None if no z-value. | Double |
| ZMax | The extent ZMax value. None if no z-value. | Double |
| MMin | The extent MMin value. None if no m-value. | Double |
| MMax | The extent MMax value. None if no m-value. | Double |
| spatial_reference | The spatial reference of the extent. | SpatialReference |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
Extent  ({XMin}, {YMin}, {XMax}, {YMax}, {ZMin}, {ZMax}, {MMin}, {MMax}, {spatial_reference})
```

### Example 2

```python
contains (second_geometry, {relation})
```

### Example 3

```python
crosses (second_geometry)
```

### Example 4

```python
disjoint (second_geometry)
```

### Example 5

```python
equals (second_geometry)
```

### Example 6

```python
overlaps (second_geometry)
```

### Example 7

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 8

```python
touches (second_geometry)
```

### Example 9

```python
within (second_geometry, {relation})
```

### Example 10

```python
import arcpy

feature_class = 'c:/Data/Florida.gdb/airports'

# Fetch each feature from the cursor and examine the extent properties
for row in arcpy.da.SearchCursor(feature_class, ['SHAPE@', 'CNTY_NAME']):
    extent = row[0].extent
    print('Extent of county {}:'.format(row[1]))
    print('XMin: {}, YMin: {}'.format(extent.XMin, extent.YMin))
    print('XMax: {}, YMax: {}'.format(extent.XMax, extent.YMax))
```

### Example 11

```python
import arcpy

feature_class = 'c:/Data/Florida.gdb/airports'

# Fetch each feature from the cursor and examine the extent properties
for row in arcpy.da.SearchCursor(feature_class, ['SHAPE@', 'CNTY_NAME']):
    extent = row[0].extent
    print('Extent of county {}:'.format(row[1]))
    print('XMin: {}, YMin: {}'.format(extent.XMin, extent.YMin))
    print('XMax: {}, YMax: {}'.format(extent.XMax, extent.YMax))
```

---

## FeatureSet

## Summary

FeatureSet objects are a lightweight representation of a feature class. They are a data element that contains not only schema, but also the data. The FeatureSet object is also how feature data is sent and received from the server.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| table_path | The features to load into the FeatureSet object. The input can be a catalog path to a feature class, a URL to a hosted feature layer, a JSON with the syntax {"url":"<url>", "serviceToken":"<ServiceToken>"} to load data from external sources that require an access token, an Esri (featureSet) JSON string, or a GeoJSON string. Esri JSON and GeoJSON are standards for encoding feature (geometry and attribute) data as a .json file. | String |
| where_clause | An SQL expression used to select a subset of records.For more information about SQL syntax, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| time_filter | The time instant or the time extent to query. The time filter can only be applied to hosted feature layers, and the layer must be time enabled.Format a time instant as a string, for example, "1199145600000" (1 Jan 2008 00:00:00 GMT). Format a time extent as a comma-delimited string, for example, "1199145600000, 1230768000000" (1 Jan 2008 00:00:00 GMT to 1 Jan 2009 00:00:00 GMT). A null value specified for the start time or the end time will represent infinity for the start or the end time, respectively, for example, "null, 1230768000000".(The default value is None) | String |
| renderer | The output FeatureSet symbology can be set using a string or dictionary representation of either a JSON renderer or a JSON definition object.Learn more about JSON renderers and JSON definition objects.(The default value is None) | String |
| is_renderer | Specifies the type of the value used with the renderer argument. Set to True if the value is a renderer object; set to False if the value is a definition.(The default value is None) | Boolean |
| geojson_geometry_type | The geometry type of the GeoJSON file that will be loaded. A single GeoJSON file may contain multiple types of geometry records. Only the records of the specified geometry type will be loaded. By default, this is the geometry type of the first record.This option is only supported if the table_path value is GeoJSON.POINT—Treat GeoJSON Point geometry type as point features.MULTIPOINT—Treat GeoJSON MultiPoint geometry type as multipoint features.POLYLINE—Treat GeoJSON LineString and MultiLineString geometry types as polyline features.POLYGON—Treat GeoJSON Polygon and MultiPolygon geometry types as polygon features.Only the listed GeoJSON geometry types are supported. (The default value is None) | String |
| table_path | The features to load into the FeatureSet object. The input can be a catalog path to a feature class, a URL to a hosted feature layer, a JSON with the syntax {"url":"<url>", "serviceToken":"<ServiceToken>"} to load data from external sources that require an access token, an Esri (featureSet) JSON string, or a GeoJSON string. Esri JSON and GeoJSON are standards for encoding feature (geometry and attribute) data as a .json file. | String |
| where_clause | An SQL expression used to select a subset of records.For more information about SQL syntax, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| time_filter | The time instant or the time extent to query. The time filter can only be applied to hosted feature layers, and the layer must be time enabled.Format a time instant as a string, for example, "1199145600000" (1 Jan 2008 00:00:00 GMT). Format a time extent as a comma-delimited string, for example, "1199145600000, 1230768000000" (1 Jan 2008 00:00:00 GMT to 1 Jan 2009 00:00:00 GMT). A null value specified for the start time or the end time will represent infinity for the start or the end time, respectively, for example, "null, 1230768000000".(The default value is None) | String |
| renderer | The output FeatureSet symbology can be set using a string or dictionary representation of either a JSON renderer or a JSON definition object.Learn more about JSON renderers and JSON definition objects.(The default value is None) | String |
| is_renderer | Specifies the type of the value used with the renderer argument. Set to True if the value is a renderer object; set to False if the value is a definition.(The default value is None) | Boolean |
| geojson_geometry_type | The geometry type of the GeoJSON file that will be loaded. A single GeoJSON file may contain multiple types of geometry records. Only the records of the specified geometry type will be loaded. By default, this is the geometry type of the first record.This option is only supported if the table_path value is GeoJSON.POINT—Treat GeoJSON Point geometry type as point features.MULTIPOINT—Treat GeoJSON MultiPoint geometry type as multipoint features.POLYLINE—Treat GeoJSON LineString and MultiLineString geometry types as polyline features.POLYGON—Treat GeoJSON Polygon and MultiPolygon geometry types as polygon features.Only the listed GeoJSON geometry types are supported. (The default value is None) | String |
| table_path | The output table to be created. | String |

## Methods

### load ({table_path}, {where_clause}, {time_filter}, {renderer}, {is_renderer}, {geojson_geometry_type})

Loads a table into the FeatureSet object.

### save (table_path)

Export to a table.

## Code Samples

### Example 1

```python
FeatureSet ({table_path}, {where_clause}, {time_filter}, {renderer}, {is_renderer}, {geojson_geometry_type})
```

### Example 2

```python
load ({table_path}, {where_clause}, {time_filter}, {renderer}, {is_renderer}, {geojson_geometry_type})
```

### Example 3

```python
save (table_path)
```

### Example 4

```python
import arcpy

arcpy.env.overwriteOutput = True

arcpy.ImportToolbox("http://flame7/arcgis/services;BufferByVal",
                    "servertools")

# List of coordinates
coordinates = [[-117.196717216, 34.046944853],
               [-117.186226483, 34.046498438],
               [-117.179530271, 34.038016569],
               [-117.187454122, 34.039132605],
               [-117.177744614, 34.056765964],
               [-117.156205131, 34.064466609],
               [-117.145491191, 34.068261129],
               [-117.170825195, 34.073618099],
               [-117.186784501, 34.068149525],
               [-117.158325598, 34.03489167]]

# Create an in_memory feature class to initially contain the coordinate pairs
feature_class = arcpy.CreateFeatureclass_management(
    "in_memory", "tempfc", "POINT")[0]

# Open an insert cursor
with arcpy.da.InsertCursor(feature_class, ["SHAPE@XY"]) as cursor:
    # Iterate through list of coordinates and add to cursor
    for (x, y) in coordinates:
        cursor.insertRow([(x, y)])

# Create a FeatureSet object and load in_memory feature class
feature_set = arcpy.FeatureSet(feature_class)

results = arcpy.BufferPoints_servertools(feature_set)
```

### Example 5

```python
import arcpy

arcpy.env.overwriteOutput = True

arcpy.ImportToolbox("http://flame7/arcgis/services;BufferByVal",
                    "servertools")

# List of coordinates
coordinates = [[-117.196717216, 34.046944853],
               [-117.186226483, 34.046498438],
               [-117.179530271, 34.038016569],
               [-117.187454122, 34.039132605],
               [-117.177744614, 34.056765964],
               [-117.156205131, 34.064466609],
               [-117.145491191, 34.068261129],
               [-117.170825195, 34.073618099],
               [-117.186784501, 34.068149525],
               [-117.158325598, 34.03489167]]

# Create an in_memory feature class to initially contain the coordinate pairs
feature_class = arcpy.CreateFeatureclass_management(
    "in_memory", "tempfc", "POINT")[0]

# Open an insert cursor
with arcpy.da.InsertCursor(feature_class, ["SHAPE@XY"]) as cursor:
    # Iterate through list of coordinates and add to cursor
    for (x, y) in coordinates:
        cursor.insertRow([(x, y)])

# Create a FeatureSet object and load in_memory feature class
feature_set = arcpy.FeatureSet(feature_class)

results = arcpy.BufferPoints_servertools(feature_set)
```

### Example 6

```python
import arcpy

# Set data
in_data = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer/0"
query = "STATE_NAME = 'California'"
renderer = '''{
    "renderer": {
        "type": "simple",
        "symbol": {
            "type": "esriSFS",
            "style": "esriSFSSolid",
            "color": [
                255,
                0,
                0,
                255
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
                "width": 2
            }
        },
        "label": "",
        "description": "",
        "rotationType": "geographic",
        "rotationExpression": ""
    }
}'''

# Create FeatureSet with query and renderer
feature_set = arcpy.FeatureSet(in_data, query, renderer=renderer, is_renderer=True)
```

### Example 7

```python
import arcpy

# Set data
in_data = "https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer/0"
query = "STATE_NAME = 'California'"
renderer = '''{
    "renderer": {
        "type": "simple",
        "symbol": {
            "type": "esriSFS",
            "style": "esriSFSSolid",
            "color": [
                255,
                0,
                0,
                255
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
                "width": 2
            }
        },
        "label": "",
        "description": "",
        "rotationType": "geographic",
        "rotationExpression": ""
    }
}'''

# Create FeatureSet with query and renderer
feature_set = arcpy.FeatureSet(in_data, query, renderer=renderer, is_renderer=True)
```

### Example 8

```python
import arcpy

# Set data
esri_json = '''{
 "objectIdFieldName": "objectid",
 "globalIdFieldName": "globalid",
 "geometryType": "esriGeometryPoint",
 "spatialReference": {
  "wkid": 102100,
  "latestWkid": 3857
 },
 "fields": [
  {
   "name": "objectid",
   "alias": "OBJECTID",
   "type": "esriFieldTypeOID"
  },
  {
   "name": "requestid",
   "alias": "Service Request ID",
   "type": "esriFieldTypeString",
   "length": 25
  },
  {
   "name": "requesttype",
   "alias": "Problem",
   "type": "esriFieldTypeString",
   "length": 100
  },
  {
   "name": "comments",
   "alias": "Comments",
   "type": "esriFieldTypeString",
   "length": 255
  }
 ],
 "features": [
  {
   "geometry": {
    "x": -9809161.170230601,
    "y": 5123045.5266209831
   },
   "attributes": {
    "objectid": 246362,
    "requestid": "1",
    "requesttype": "Sidewalk Damage",
    "comments": "Pothole"
   }
  },
  {
   "geometry": {
    "x": -9074857.9234435894,
    "y": 4982391.2604217697
   },
   "attributes": {
    "objectid": 246382,
    "requestid": "2",
    "requesttype": "Pothole",
    "comments": ""
   }
  }
 ]
}'''

# Create FeatureSet from Esri JSON
feature_set = arcpy.FeatureSet(data_json)
```

### Example 9

```python
import arcpy

# Set data
esri_json = '''{
 "objectIdFieldName": "objectid",
 "globalIdFieldName": "globalid",
 "geometryType": "esriGeometryPoint",
 "spatialReference": {
  "wkid": 102100,
  "latestWkid": 3857
 },
 "fields": [
  {
   "name": "objectid",
   "alias": "OBJECTID",
   "type": "esriFieldTypeOID"
  },
  {
   "name": "requestid",
   "alias": "Service Request ID",
   "type": "esriFieldTypeString",
   "length": 25
  },
  {
   "name": "requesttype",
   "alias": "Problem",
   "type": "esriFieldTypeString",
   "length": 100
  },
  {
   "name": "comments",
   "alias": "Comments",
   "type": "esriFieldTypeString",
   "length": 255
  }
 ],
 "features": [
  {
   "geometry": {
    "x": -9809161.170230601,
    "y": 5123045.5266209831
   },
   "attributes": {
    "objectid": 246362,
    "requestid": "1",
    "requesttype": "Sidewalk Damage",
    "comments": "Pothole"
   }
  },
  {
   "geometry": {
    "x": -9074857.9234435894,
    "y": 4982391.2604217697
   },
   "attributes": {
    "objectid": 246382,
    "requestid": "2",
    "requesttype": "Pothole",
    "comments": ""
   }
  }
 ]
}'''

# Create FeatureSet from Esri JSON
feature_set = arcpy.FeatureSet(data_json)
```

### Example 10

```python
import arcpy

geo_json = '''{
    "crs": {
        "properties": {
            "name": "EPSG: 3857"
        },
        "type": "name"
    },
    "features": [
        {
            "geometry": {
                "coordinates": [
                    -9809161.170230601,
                    5123045.526620984
                ],
                "type": "Point"
            },
            "id": 246362,
            "properties": {
                "comments": "Pothole",
                "objectid": 246362,
                "requestid": "1",
                "requesttype": "Sidewalk Damage"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    -9074857.923443586,
                    4982391.260421775
                ],
                "type": "Point"
            },
            "id": 246382,
            "properties": {
                "comments": "",
                "objectid": 246382,
                "requestid": "2",
                "requesttype": "Pothole"
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}'''

# Create FeatureSet from Geo JSON
feature_set = arcpy.FeatureSet(geo_json, geojson_geometry_type="POINT")
```

### Example 11

```python
import arcpy

geo_json = '''{
    "crs": {
        "properties": {
            "name": "EPSG: 3857"
        },
        "type": "name"
    },
    "features": [
        {
            "geometry": {
                "coordinates": [
                    -9809161.170230601,
                    5123045.526620984
                ],
                "type": "Point"
            },
            "id": 246362,
            "properties": {
                "comments": "Pothole",
                "objectid": 246362,
                "requestid": "1",
                "requesttype": "Sidewalk Damage"
            },
            "type": "Feature"
        },
        {
            "geometry": {
                "coordinates": [
                    -9074857.923443586,
                    4982391.260421775
                ],
                "type": "Point"
            },
            "id": 246382,
            "properties": {
                "comments": "",
                "objectid": 246382,
                "requestid": "2",
                "requesttype": "Pothole"
            },
            "type": "Feature"
        }
    ],
    "type": "FeatureCollection"
}'''

# Create FeatureSet from Geo JSON
feature_set = arcpy.FeatureSet(geo_json, geojson_geometry_type="POINT")
```

### Example 12

```python
import arcpy

url = {"url": "https://services.arcgis.com/O9GvsOYzrcFwdwqx/arcgis/rest/services/MyTimeEnabledLayer/FeatureServer/0"}
filter = "Country = 'United States'"
in_start, in_end = 1672473600000, 1718434800000
time_filter = f"{in_start}, {in_end}"

# Create FeatureSet using a time filter
feature_set = arcpy.FeatureSet(table_path=url, time_filter=time_filter)
```

### Example 13

```python
import arcpy

url = {"url": "https://services.arcgis.com/O9GvsOYzrcFwdwqx/arcgis/rest/services/MyTimeEnabledLayer/FeatureServer/0"}
filter = "Country = 'United States'"
in_start, in_end = 1672473600000, 1718434800000
time_filter = f"{in_start}, {in_end}"

# Create FeatureSet using a time filter
feature_set = arcpy.FeatureSet(table_path=url, time_filter=time_filter)
```

---

## Field

## Summary

The field object represents a column in a table. A field has many properties, the most obvious ones being its name and its type.

## Code Samples

### Example 1

```python
import arcpy

feature_class = "c:/data/counties.shp"

# Create a list of fields using the ListFields function
fields = arcpy.ListFields(feature_class)

# Iterate through the list of fields
for field in fields:
    # Print field properties
    print("Field:       {0}".format(field.name))
    print("Alias:       {0}".format(field.aliasName))
    print("Type:        {0}".format(field.type))
    print("Is Editable: {0}".format(field.editable))
    print("Required:    {0}".format(field.required))
    print("Scale:       {0}".format(field.scale))
    print("Precision:   {0}".format(field.precision))
```

### Example 2

```python
import arcpy

feature_class = "c:/data/counties.shp"

# Create a list of fields using the ListFields function
fields = arcpy.ListFields(feature_class)

# Iterate through the list of fields
for field in fields:
    # Print field properties
    print("Field:       {0}".format(field.name))
    print("Alias:       {0}".format(field.aliasName))
    print("Type:        {0}".format(field.type))
    print("Is Editable: {0}".format(field.editable))
    print("Required:    {0}".format(field.required))
    print("Scale:       {0}".format(field.scale))
    print("Precision:   {0}".format(field.precision))
```

---

## FieldInfo

## Summary

Provides field info methods and properties for layer and table views.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| field_name | The field name from the input feature class or table. | String |
| new_field_name | Sets the field name for the new layer or table view. | String |
| visible | Sets whether the field is visible or hidden.VISIBLE—Field is visible.HIDDEN—Field is hidden. | String |
| split_rule | Sets the behavior of an attribute's values when a feature is split.NONE—The attributes of the two resulting features take on a copy of the original value. RATIO—The attributes of resulting features are a ratio of the original feature's value. The ratio is based on the division of the original geometry. If the geometry is divided equally, each new feature's attribute gets one-half of the value of the original object's attribute. | String |
| field_name | The field name used to find its index position | String |
| field_name | The new field name used to find its index position. | String |
| index | The index position. | Integer |
| index | The index position. | Integer |
| index | The index position. | String |
| index | The index position. | String |
| string | The string representation of the object.In addition to FieldInfo methods and properties, you can also construct a FieldInfo object from a formatted string. Each field is defined by four space-delimited values. Fields are separated by a semicolon.The name of the input field.The name of the output field (not currently supported). Sets whether the field is visible or hidden.VISIBLE—The field is visible.HIDDEN—The field is hidden. Sets the behavior of an attribute's values when a feature is split. NONE—The attributes of the two resulting features take on a copy of the original value. RATIO—The attributes of resulting features are a ratio of the original feature's value. The ratio is based on the division of the original geometry. If the geometry is divided equally, each new feature's attribute gets one-half of the value of the original object's attribute. import arcpy field_info_str "fieldA fieldA VISIBLE NONE;fieldB fieldB HIDDEN RATIO" field_info = arcpy.FieldInfo() field_info.loadFromString(field_info_str) | String |
| index | The index position of the FieldInfo object. | Integer |
| index | The index position. | Integer |
| field_name | The field name to set into the table. | String |
| index | The index position. | None |
| new_field_name | The new field name that will be set in the table. | String |
| index | The index position. | Integer |
| rule | The split rule to set into the table.NONE—The attributes of the two resulting features take on a copy of the original value. RATIO—The attributes of resulting features are a ratio of the original feature's value. The ratio is based on the division of the original geometry. If the geometry is divided equally, each new feature's attribute gets one-half of the value of the original object's attribute. | String |
| index | The index position. | Integer |
| visible | The visible policy to set into the table.VISIBLE—Field is visible.HIDDEN—Field is hidden. | String |

## Methods

### addField (field_name, new_field_name, visible, split_rule)

Adds a field info entry

### exportToString ()

Exports the object to its string representation.

### findFieldByName (field_name)

Finds the field index by field name

### findFieldByNewName (field_name)

Finds the field index by new field name.

### getFieldName (index)

Gets the field name from the table by index position.

### getNewName (index)

Returns the new field name from the table by index position.

### getSplitRule (index)

Gets the split rule from the table by index position.

### getVisible (index)

Returns the visible flag from the table by index position.

### loadFromString (string)

Defines a FieldInfo object from a formatted string.

### removeField (index)

Removes a FieldInfo entry from a table.

### setFieldName (index, field_name)

Sets the field name into the table.

### setNewName (index, new_field_name)

Sets a new field name in the table.Note:While the setNewName method updates a field name in the object, the name change will not be applied when the FieldInfo object is used as input to a geoprocessing tool.

### setSplitRule (index, rule)

Sets the split rule into the table.

### setVisible (index, visible)

Set the visible flag of a field on the table.

## Code Samples

### Example 1

```python
FieldInfo  ()
```

### Example 2

```python
addField (field_name, new_field_name, visible, split_rule)
```

### Example 3

```python
exportToString ()
```

### Example 4

```python
findFieldByName (field_name)
```

### Example 5

```python
findFieldByNewName (field_name)
```

### Example 6

```python
getFieldName (index)
```

### Example 7

```python
getNewName (index)
```

### Example 8

```python
getSplitRule (index)
```

### Example 9

```python
getVisible (index)
```

### Example 10

```python
loadFromString (string)
```

### Example 11

```python
import arcpy
field_info_str "fieldA fieldA VISIBLE NONE;fieldB fieldB HIDDEN RATIO"
field_info = arcpy.FieldInfo()
field_info.loadFromString(field_info_str)
```

### Example 12

```python
import arcpy
field_info_str "fieldA fieldA VISIBLE NONE;fieldB fieldB HIDDEN RATIO"
field_info = arcpy.FieldInfo()
field_info.loadFromString(field_info_str)
```

### Example 13

```python
removeField (index)
```

### Example 14

```python
setFieldName (index, field_name)
```

### Example 15

```python
setNewName (index, new_field_name)
```

### Example 16

```python
setSplitRule (index, rule)
```

### Example 17

```python
setVisible (index, visible)
```

### Example 18

```python
import arcpy

feature_class = "c:/Data/wells.shp"
layer = "temp_layer"
arcpy.management.MakeFeatureLayer(feature_class, layer)

# Create a describe object
desc = arcpy.Describe(layer)

# Access Describe's fieldInfo property
field_info = desc.fieldInfo

# Use the count property to iterate through all the fields
for index in range(0, field_info.count):
    # Print fieldinfo properties
    print(f"Field Name: {field_info.getFieldName(index)}")
    print(f"\tSplit Rule: {field_info.getSplitRule(index)}")
    print(f"\tVisible:    {field_info.getVisible(index)}")
```

### Example 19

```python
import arcpy

feature_class = "c:/Data/wells.shp"
layer = "temp_layer"
arcpy.management.MakeFeatureLayer(feature_class, layer)

# Create a describe object
desc = arcpy.Describe(layer)

# Access Describe's fieldInfo property
field_info = desc.fieldInfo

# Use the count property to iterate through all the fields
for index in range(0, field_info.count):
    # Print fieldinfo properties
    print(f"Field Name: {field_info.getFieldName(index)}")
    print(f"\tSplit Rule: {field_info.getSplitRule(index)}")
    print(f"\tVisible:    {field_info.getVisible(index)}")
```

---

## FieldMap

## Summary

The FieldMap object provides a field definition and a list of input fields taken from a set of tables or feature classes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| table_dataset | The table added to the field map. | String |
| field_name | The input field name. | String |
| start_position | The start position of an input text value.(The default value is -1) | Integer |
| end_position | The end position of an input text value.(The default value is -1) | Integer |
| table_dataset | The table added to the field map. | String |
| field_name | The field name. | String |
| index | The index position. | Integer |
| index | The index position. | Integer |
| index | The index position. | Integer |
| index | The index position. | Integer |
| index | The index position. | Integer |
| index | The index position. | Integer |
| end_position | The end position of an input text value. | Integer |
| index | The index position. | Integer |
| start_position | The start position of an input text value. | Integer |

## Methods

### addInputField (table_dataset, field_name, {start_position}, {end_position})

Adds input field to the field map.

### findInputFieldIndex (table_dataset, field_name)

Finds an input field from the field map.

### getEndTextPosition (index)

Returns the end text position from the field map.

### getInputFieldName (index)

Returns the name of an input field from the field map, based on the field's index position.

### getInputTableName (index)

Returns the name of an input table from the field map, based on the table's index position.

### getStartTextPosition (index)

Returns the start text position from the FieldMap object.

### removeAll ()

Removes all values and creates an empty object.

### removeInputField (index)

Removes an input field from the FieldMap object.

### setEndTextPosition (index, end_position)

Sets end text position for the field map.

### setStartTextPosition (index, start_position)

Sets the start text position from the field map.

## Code Samples

### Example 1

```python
FieldMap  ()
```

### Example 2

```python
addInputField (table_dataset, field_name, {start_position}, {end_position})
```

### Example 3

```python
findInputFieldIndex (table_dataset, field_name)
```

### Example 4

```python
getEndTextPosition (index)
```

### Example 5

```python
getInputFieldName (index)
```

### Example 6

```python
getInputTableName (index)
```

### Example 7

```python
getStartTextPosition (index)
```

### Example 8

```python
removeAll ()
```

### Example 9

```python
removeInputField (index)
```

### Example 10

```python
setEndTextPosition (index, end_position)
```

### Example 11

```python
setStartTextPosition (index, start_position)
```

### Example 12

```python
import arcpy

# Set the workspace
arcpy.env.workspace = 'c:/base'

in_features_1 = 'data.gdb/Trees'
in_features_2 = 'Plants.shp'
out_features = 'data.gdb/Vegetation'

# Create the required FieldMap and FieldMappings objects.
fm_type = arcpy.FieldMap()
fm_diam = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Get the field names of vegetation type and diameter for both
# original files.
tree_type = "Tree_Type"
plant_type = "Plant_Type"

tree_diam = "Tree_Diameter"
plant_diam = "Diameter"

# Add fields to their corresponding FieldMap objects.
fm_type.addInputField(in_features_1, tree_type)
fm_type.addInputField(in_features_2, plant_type)

fm_diam.addInputField(in_features_1, tree_diam)
fm_diam.addInputField(in_features_2, plant_diam)

# Set the output field properties for both FieldMap objects.
type_field = fm_type.outputField
type_field.name = 'Veg_Type'
fm_type.outputField = type_field

diam_field = fm_diam.outputField
diam_field.name = 'Veg_Diam'
fm_diam.outputField = diam_field

# Add the FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm_type)
fms.addFieldMap(fm_diam)

# Merge the two feature classes.
arcpy.management.Merge([in_features_1, in_features_2], out_features, fms)
```

### Example 13

```python
import arcpy

# Set the workspace
arcpy.env.workspace = 'c:/base'

in_features_1 = 'data.gdb/Trees'
in_features_2 = 'Plants.shp'
out_features = 'data.gdb/Vegetation'

# Create the required FieldMap and FieldMappings objects.
fm_type = arcpy.FieldMap()
fm_diam = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Get the field names of vegetation type and diameter for both
# original files.
tree_type = "Tree_Type"
plant_type = "Plant_Type"

tree_diam = "Tree_Diameter"
plant_diam = "Diameter"

# Add fields to their corresponding FieldMap objects.
fm_type.addInputField(in_features_1, tree_type)
fm_type.addInputField(in_features_2, plant_type)

fm_diam.addInputField(in_features_1, tree_diam)
fm_diam.addInputField(in_features_2, plant_diam)

# Set the output field properties for both FieldMap objects.
type_field = fm_type.outputField
type_field.name = 'Veg_Type'
fm_type.outputField = type_field

diam_field = fm_diam.outputField
diam_field.name = 'Veg_Diam'
fm_diam.outputField = diam_field

# Add the FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm_type)
fms.addFieldMap(fm_diam)

# Merge the two feature classes.
arcpy.management.Merge([in_features_1, in_features_2], out_features, fms)
```

### Example 14

```python
import arcpy

in_features = r'c:/base/data.gdb/AccidentData'
out_features = r'c:/base/data.gdb/AverageAccidents'

# Create the necessary FieldMap and FieldMappings objects.
fm = arcpy.FieldMap()
fm1 = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Each field with accident data begins with 'Yr'.
# The next step loops through each of the fields beginning with 'Yr',
# and adds them to the FieldMap object.
for field in arcpy.ListFields(in_features, 'Yr*'):
    fm.addInputField(in_features, field.name)

# Set the merge rule to find the mean value of all fields in the
# FieldMap object.
fm.mergeRule = 'Mean'

# Set the properties of the output field.
out_field = fm.outputField
out_field.name = 'AvgAccidents'
out_field.aliasName = 'AvgAccidents'
fm.outputField = out_field

# Add the intersection field to the second FieldMap object.
fm1.addInputField(in_features, "Intersection")

# Add both FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm)
fms.addFieldMap(fm1)

# Create the output feature class using the FieldMappings object.
arcpy.conversion.ExportFeatures(in_features, out_features, field_mapping=fms)
```

### Example 15

```python
import arcpy

in_features = r'c:/base/data.gdb/AccidentData'
out_features = r'c:/base/data.gdb/AverageAccidents'

# Create the necessary FieldMap and FieldMappings objects.
fm = arcpy.FieldMap()
fm1 = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Each field with accident data begins with 'Yr'.
# The next step loops through each of the fields beginning with 'Yr',
# and adds them to the FieldMap object.
for field in arcpy.ListFields(in_features, 'Yr*'):
    fm.addInputField(in_features, field.name)

# Set the merge rule to find the mean value of all fields in the
# FieldMap object.
fm.mergeRule = 'Mean'

# Set the properties of the output field.
out_field = fm.outputField
out_field.name = 'AvgAccidents'
out_field.aliasName = 'AvgAccidents'
fm.outputField = out_field

# Add the intersection field to the second FieldMap object.
fm1.addInputField(in_features, "Intersection")

# Add both FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm)
fms.addFieldMap(fm1)

# Create the output feature class using the FieldMappings object.
arcpy.conversion.ExportFeatures(in_features, out_features, field_mapping=fms)
```

---

## FieldMappings

## Summary

The FieldMappings object is a collection of FieldMap objects. Use the object as a parameter value for tools that perform field mapping, such as the Merge tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| field_map | The field map to add to the field mappings | FieldMap |
| table_dataset | The table to add to the field mappings object. | String |
| field_map_name | Find the field map by name. | String |
| index | The index position of the FieldMap object. | Integer |
| string | The string representation of the object.In addition to FieldMappings and FieldMap methods and properties, you can also construct a FieldMappings object from a formatted string. The following example shows the creation of a FieldMappings object that could be used with the Merge tool.import arcpy fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1' fieldmappings = arcpy.FieldMappings() fieldmappings.loadFromString(fieldmappings_string)The first nine values in the string define an output field and are space delimited.The name of the output field.The alias of the output field.Whether the output field is editable (true or false).Whether the output field supports nulls (true or false).Whether the output field is required (true or false).The length of the output field (text fields only).The field type of the output field.The precision of the output field (float and double fields only).The scale of the output field (float and double fields only). The remaining values define the field map characteristics and are comma delimited.The field map merge rule.The concatenator to join values.The path to the input table.The field name from the input table.The start position of an input text value.The end position of an input text value. Any number of input fields can be mapped to the output field, not only two, as implied in the example. Include the merge rule and concatenator once, and include the dataset path, field name, and start position and end position for each input field.Enclose any values with spaces, such as the field alias or concatenator, in quotation marks.To skip a value, use a # for string values, and -1 for numeric values.As shown in the following example, use a semicolon delimiter to separate multiple output fields.import arcpy fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1;CAPITAL "Capital" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,CAPITAL,-1,-1,c:\\data\\fgdb.gdb\\south_america,CAPITAL2,-1,-1' fieldmappings = arcpy.FieldMappings() fieldmappings.loadFromString(fieldmappings_string) | String |
| index | The index position of the FieldMap. | Integer |
| index | The index position of the FieldMap object to be replaced. | Integer |
| value | The replacement FieldMap object. | FieldMap |

## Methods

### addFieldMap (field_map)

Add a field map to the field mappings.

### addTable (table_dataset)

Adds a table to the field mappings object.

### exportToString ()

Exports the object to its string representation.

### findFieldMapIndex (field_map_name)

Find a field map within the field mappings by name.

### getFieldMap (index)

Returns a FieldMap object from the FieldMappings object by index position.

### loadFromString (string)

Defines a FieldMappings object from a formatted string.

### removeAll ()

Removes all values and creates an empty object.

### removeFieldMap (index)

Removes a FieldMap object from the FieldMappings object.

### replaceFieldMap (index, value)

Replace a FieldMap object within the FieldMappings object.

## Code Samples

### Example 1

```python
FieldMappings ()
```

### Example 2

```python
addFieldMap (field_map)
```

### Example 3

```python
addTable (table_dataset)
```

### Example 4

```python
exportToString ()
```

### Example 5

```python
findFieldMapIndex (field_map_name)
```

### Example 6

```python
getFieldMap (index)
```

### Example 7

```python
loadFromString (string)
```

### Example 8

```python
import arcpy

fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1'

fieldmappings = arcpy.FieldMappings()
fieldmappings.loadFromString(fieldmappings_string)
```

### Example 9

```python
import arcpy

fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1'

fieldmappings = arcpy.FieldMappings()
fieldmappings.loadFromString(fieldmappings_string)
```

### Example 10

```python
import arcpy

fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1;CAPITAL "Capital" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,CAPITAL,-1,-1,c:\\data\\fgdb.gdb\\south_america,CAPITAL2,-1,-1'

fieldmappings = arcpy.FieldMappings()
fieldmappings.loadFromString(fieldmappings_string)
```

### Example 11

```python
import arcpy

fieldmappings_string = 'REGION "Region" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,REGION,-1,-1,c:\\data\\fgdb.gdb\\south_america,REGION2,-1,-1;CAPITAL "Capital" true true false 21 Text -1 -1,First,#,c:\\data\\fgdb.gdb\\north_america,CAPITAL,-1,-1,c:\\data\\fgdb.gdb\\south_america,CAPITAL2,-1,-1'

fieldmappings = arcpy.FieldMappings()
fieldmappings.loadFromString(fieldmappings_string)
```

### Example 12

```python
removeAll ()
```

### Example 13

```python
removeFieldMap (index)
```

### Example 14

```python
replaceFieldMap (index, value)
```

### Example 15

```python
import arcpy

# Set the workspace
arcpy.env.workspace = 'c:/base'

in_features_1 = 'data.gdb/Trees'
in_features_2 = 'Plants.shp'
out_features = 'data.gdb/Vegetation'

# Create the required FieldMap and FieldMappings objects.
fm_type = arcpy.FieldMap()
fm_diam = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Get the field names of vegetation type and diameter for both
# original files.
tree_type = "Tree_Type"
plant_type = "Plant_Type"

tree_diam = "Tree_Diameter"
plant_diam = "Diameter"

# Add fields to their corresponding FieldMap objects.
fm_type.addInputField(in_features_1, tree_type)
fm_type.addInputField(in_features_2, plant_type)

fm_diam.addInputField(in_features_1, tree_diam)
fm_diam.addInputField(in_features_2, plant_diam)

# Set the output field properties for both FieldMap objects.
type_field = fm_type.outputField
type_field.name = 'Veg_Type'
fm_type.outputField = type_field

diam_field = fm_diam.outputField
diam_field.name = 'Veg_Diam'
fm_diam.outputField = diam_field

# Add the FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm_type)
fms.addFieldMap(fm_diam)

# Merge the two feature classes.
arcpy.management.Merge([in_features_1, in_features_2], out_features, fms)
```

### Example 16

```python
import arcpy

# Set the workspace
arcpy.env.workspace = 'c:/base'

in_features_1 = 'data.gdb/Trees'
in_features_2 = 'Plants.shp'
out_features = 'data.gdb/Vegetation'

# Create the required FieldMap and FieldMappings objects.
fm_type = arcpy.FieldMap()
fm_diam = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Get the field names of vegetation type and diameter for both
# original files.
tree_type = "Tree_Type"
plant_type = "Plant_Type"

tree_diam = "Tree_Diameter"
plant_diam = "Diameter"

# Add fields to their corresponding FieldMap objects.
fm_type.addInputField(in_features_1, tree_type)
fm_type.addInputField(in_features_2, plant_type)

fm_diam.addInputField(in_features_1, tree_diam)
fm_diam.addInputField(in_features_2, plant_diam)

# Set the output field properties for both FieldMap objects.
type_field = fm_type.outputField
type_field.name = 'Veg_Type'
fm_type.outputField = type_field

diam_field = fm_diam.outputField
diam_field.name = 'Veg_Diam'
fm_diam.outputField = diam_field

# Add the FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm_type)
fms.addFieldMap(fm_diam)

# Merge the two feature classes.
arcpy.management.Merge([in_features_1, in_features_2], out_features, fms)
```

### Example 17

```python
import arcpy

in_features = r'c:/base/data.gdb/AccidentData'
out_features = r'c:/base/data.gdb/AverageAccidents'

# Create the necessary FieldMap and FieldMappings objects.
fm = arcpy.FieldMap()
fm1 = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Each field with accident data begins with 'Yr'.
# The next step loops through each of the fields beginning with 'Yr',
# and adds them to the FieldMap object.
for field in arcpy.ListFields(in_features, 'Yr*'):
    fm.addInputField(in_features, field.name)

# Set the merge rule to find the mean value of all fields in the
# FieldMap object.
fm.mergeRule = 'Mean'

# Set the properties of the output field.
out_field = fm.outputField
out_field.name = 'AvgAccidents'
out_field.aliasName = 'AvgAccidents'
fm.outputField = out_field

# Add the intersection field to the second FieldMap object.
fm1.addInputField(in_features, "Intersection")

# Add both FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm)
fms.addFieldMap(fm1)

# Create the output feature class using the FieldMappings object.
arcpy.conversion.ExportFeatures(in_features, out_features, field_mapping=fms)
```

### Example 18

```python
import arcpy

in_features = r'c:/base/data.gdb/AccidentData'
out_features = r'c:/base/data.gdb/AverageAccidents'

# Create the necessary FieldMap and FieldMappings objects.
fm = arcpy.FieldMap()
fm1 = arcpy.FieldMap()
fms = arcpy.FieldMappings()

# Each field with accident data begins with 'Yr'.
# The next step loops through each of the fields beginning with 'Yr',
# and adds them to the FieldMap object.
for field in arcpy.ListFields(in_features, 'Yr*'):
    fm.addInputField(in_features, field.name)

# Set the merge rule to find the mean value of all fields in the
# FieldMap object.
fm.mergeRule = 'Mean'

# Set the properties of the output field.
out_field = fm.outputField
out_field.name = 'AvgAccidents'
out_field.aliasName = 'AvgAccidents'
fm.outputField = out_field

# Add the intersection field to the second FieldMap object.
fm1.addInputField(in_features, "Intersection")

# Add both FieldMap objects to the FieldMappings object.
fms.addFieldMap(fm)
fms.addFieldMap(fm1)

# Create the output feature class using the FieldMappings object.
arcpy.conversion.ExportFeatures(in_features, out_features, field_mapping=fms)
```

---

## Filter

## Summary

The Filter object allows you to specify the choices available for a parameter.

## Code Samples

### Example 1

```python
import arcpy

class ToolValidator:
    def __init__(self):
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        return

    def updateParameters(self):
        # Provide default values for "file format type" and
        #  "feature type in file"

        if not self.params[1].altered:
            self.params[1].value = "OLD_FORMAT"
        if not self.params[2].altered:
            self.params[2].value = "POINT"

        # Update the value list filter of the "feature type in file"
        # parameter depending on the type of file (old vs. new format)
        # input
        if self.params[1].value == "OLD_FORMAT":
            self.params[2].filter.list = ["POINT", "LINE", "POLYGON"]
        elif self.params[1].value == "NEW_FORMAT":
            self.params[2].filter.list = ["POINT", "LINE", "POLYGON",
                                          "POINT_WITH_ANNO",
                                          "LINE_WITH_ANNO",
                                          "POLYGON_WITH_ANNO"]

        return

    def updateMessages(self):
        return
```

### Example 2

```python
import arcpy

class ToolValidator:
    def __init__(self):
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        return

    def updateParameters(self):
        # Provide default values for "file format type" and
        #  "feature type in file"

        if not self.params[1].altered:
            self.params[1].value = "OLD_FORMAT"
        if not self.params[2].altered:
            self.params[2].value = "POINT"

        # Update the value list filter of the "feature type in file"
        # parameter depending on the type of file (old vs. new format)
        # input
        if self.params[1].value == "OLD_FORMAT":
            self.params[2].filter.list = ["POINT", "LINE", "POLYGON"]
        elif self.params[1].value == "NEW_FORMAT":
            self.params[2].filter.list = ["POINT", "LINE", "POLYGON",
                                          "POINT_WITH_ANNO",
                                          "LINE_WITH_ANNO",
                                          "POLYGON_WITH_ANNO"]

        return

    def updateMessages(self):
        return
```

### Example 3

```python
def updateParameters(self):
    # Update the value list filter in the second parameter based
    # on the shape type in the first parameter

    string_filter = self.params[1].filter
    feature_class = self.params[0].value
    if feature_class:
        shape_type = arcpy.Describe(feature_class).shapeType
        if shape_type in ["Point", "Multipoint"]:
            string_filter.list = ["RED", "GREEN", "BLUE"]
        elif shape_type == "Polygon":
            string_filter.list = ["WHITE", "GRAY", "BLACK"]
        else:
            string_filter.list = ["ORANGE", "INDIGO", "VIOLET"]
    else:
        string_filter.list = ["RED", "GREEN", "BLUE"]

    # If the user hasn't changed the keyword value, set it to the
    # default value (first value in the value list filter).
    if not self.params[1].altered:
        self.params[1].value = string_filter.list[0]

    return
```

### Example 4

```python
def updateParameters(self):
    # Update the value list filter in the second parameter based
    # on the shape type in the first parameter

    string_filter = self.params[1].filter
    feature_class = self.params[0].value
    if feature_class:
        shape_type = arcpy.Describe(feature_class).shapeType
        if shape_type in ["Point", "Multipoint"]:
            string_filter.list = ["RED", "GREEN", "BLUE"]
        elif shape_type == "Polygon":
            string_filter.list = ["WHITE", "GRAY", "BLACK"]
        else:
            string_filter.list = ["ORANGE", "INDIGO", "VIOLET"]
    else:
        string_filter.list = ["RED", "GREEN", "BLUE"]

    # If the user hasn't changed the keyword value, set it to the
    # default value (first value in the value list filter).
    if not self.params[1].altered:
        self.params[1].value = string_filter.list[0]

    return
```

### Example 5

```python
def updateParameters(self):
    # Update the value list filter in the third parameter based on the
	   # attributes of the field selected in the second parameter

    if self.params[1].value:
        fc = self.params[0].value
        field = self.params[1].valueAsText
        values = self.params[2].filter
        attribute_values = [row[0] for row in arcpy.da.SearchCursor(fc, [field])]
        unique_attributes = set(attribute_values)
        values.list = [int(value) for value in unique_attributes]
    return
```

### Example 6

```python
def updateParameters(self):
    # Update the value list filter in the third parameter based on the
	   # attributes of the field selected in the second parameter

    if self.params[1].value:
        fc = self.params[0].value
        field = self.params[1].valueAsText
        values = self.params[2].filter
        attribute_values = [row[0] for row in arcpy.da.SearchCursor(fc, [field])]
        unique_attributes = set(attribute_values)
        values.list = [int(value) for value in unique_attributes]
    return
```

---

## Geometry

## Summary

Geometry objects define a spatial location and an associated geometric shape.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| geometry | The geometry type.point—The geometry is a point.polygon—The geometry is a polygon.polyline—The geometry is a polyline.multipoint—The geometry is a multipoint. | String |
| inputs | The coordinate information used to create the object. The data type can be Point or Array objects. | Object |
| spatial_reference | The spatial reference of the new geometry.(The default value is None) | SpatialReference |
| has_z | Specifies whether the geometry will be z-enabled.(The default value is False) | Boolean |
| has_m | Specifies whether the geometry will be m-enabled.(The default value is False) | Boolean |
| has_id | Specifies whether the geometry will support point IDs.(The default value is False) | Boolean |
| other | The second geometry. If the geometry is a polygon, the distance is measured to the centroid of the polygon. | PointGeometry |
| method | The method used to measure distance. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| distance | The buffer distance.The buffer distance is in the same units as the geometry that is being buffered. A negative distance can only be specified against a polygon geometry. | Double |
| envelope | An Extent object used to define the clip extent. | Extent |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| cutter | The cutting polyline geometry. | PolyLine |
| method | The method of densification. DISTANCE—Creates a feature that is a piecewise linear approximation of the input.ANGLE—Creates a feature that is a piecewise linear approximation of the input. Vertices are introduced at points where the angle between tangents at those points is the provided angle.GEODESIC—Densifies and reshapes segments between input vertices so that the output segments follow the shortest ground path connecting input vertices. | String |
| distance | The maximum distance between vertices. The actual distance between vertices will usually be less than the maximum distance, as new vertices will be evenly distributed along the original segment. If using a type of DISTANCE or ANGLE, the distance is measured in the units of the geometry's spatial reference. If using a type of GEODESIC, the distance is measured in meters. | Double |
| deviation | Densify uses straight lines to approximate curves. You use deviation to control the accuracy of this approximation. The deviation is the maximum distance between the new segment and the original curve. The smaller its value, the more segments will be required to approximate the curve. If using a type of DISTANCE, the deviation is measured in the units of the geometry's spatial reference. If using a type of ANGLE, the deviation is measured in radians. If using a type of GEODESIC, the deviation is not used. | Double |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| max_offset | The maximum offset tolerance. | Double |
| method | The method used to measure area. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| units | The units in which the area will be calculated.Learn more about area unitsSquareKilometers—Square kilometersHectares—HectaresAres—AresSquareMeters—Square metersSquareDecimeters—Square decimetersSquareCentimeters—Square centimetersSquareMillimeters—Square millimetersSquareMilesInt—Square statute milesAcresInt—International acresSquareYardsInt—Square international yardsSquareFeetInt—Square international feetSquareInchesInt—Square international inchesSquareMilesUS—Square US survey milesAcresUS—Square US survey acresSquareYardsUS—Square US survey yardsSquareFeetUS—Square US survey feetSquareInchesUS—Square US survey inchesUnknown—Unknown | String |
| method | The method used to measure length. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| units | The units in which the length will be calculated.Learn more about linear unitsKilometers—KilometersMeters—MetersDecimeters—DecimetersMillimeters—MillimetersCentimeters—CentimetersNauticalMilesInt—International nautical milesMilesInt—Statute milesYardsInt—International yardsFeetInt—International feetInchesInt—International inchesNauticalMiles—US survey nautical milesMiles—US survey milesYards—US survey yardsFeet—US survey feetInches—US survey inchesDecimalDegrees—Decimal degreesPoints—PointsUnknown—Unknown | String |
| index | The index position of the geometry. | Integer |
| other | The second geometry. | Object |
| dimension | The topological dimension (shape type) of the resulting geometry. 1—A zero-dimensional geometry (point or multipoint). 2—A one-dimensional geometry (polyline). 4—A two-dimensional geometry (polygon). | Integer |
| in_point | A point (PointGeometry or Point) that is used to measure from the start point of the polyline. If the point does not intersect the line, the function will use the nearest location on the line from the point. | PointGeometry |
| use_percentage | If False, the measure will be returned as a distance; if True, the measure will be returned as a percentage.(The default value is False) | Boolean |
| dx | The distance the geometry will be moved along the x-axis. (The default value is 0.0) | Double |
| dy | The distance the geometry will be moved along the y-axis. (The default value is 0.0) | Double |
| dz | The distance the geometry will be moved along the z-axis. The geometry must be z-aware and have z-values.(The default value is 0.0) | Double |
| second_geometry | A second geometry. | Object |
| angle | The angle in degrees to the returned point. | Double |
| distance | The distance in the units of the geometry's spatial reference to the returned point. | Double |
| method | PLANAR measurements reflect the projection of geographic data onto the 2D surface (in other words, they will not take into account the curvature of the earth). GEODESIC, GREAT_ELLIPTIC, LOXODROME, or PRESERVE_SHAPE measurement types can be chosen as an alternative if desired. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is when you want to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—A loxodrome is not the shortest distance between two points but instead defines the line of constant bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system, and the 2D plane of that coordinate system will be used as the basis for the measurements.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| value | The distance along the line.The distance will be evaluated based on the geodesic parameter value. If the geodesic parameter value is False, the distance will be evaluated in meters. If the geodesic parameter value is True, the distance will be evaluated in the units of the feature's spatial reference.If the value exceeds the length of the line or precedes the length of the line (a negative value), the behaviour will depend on the geodesic parameter value as follows:If the geodesic parameter value is False, exceeding the length of the line will return the endpoint of the line, and a negative distance value will return the starting point of the line.If the geodesic parameter value is True, exceeding or preceding the length of the line will cause the method to fail. | Double |
| use_percentage | Specifies whether the distance is specified as a fixed unit of measure (False) or a ratio of the length of the line (True).For percentages, express the value parameter as a double from 0.0 (0 percent) to 1.0 (100 percent).Note:This parameter is only supported when the geodesic parameter value is False.(The default value is False) | Boolean |
| geodesic | Specifies whether the distance measure will be geodesic (True) or planar (False).(The default value is False) | Boolean |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| in_point | The input point. Both PointGeometry and Point objects are accepted. | PointGeometry |
| as_percentage | If False, the measure will be returned as a distance; if True, the measure will be returned as a percentage.(The default value is False) | Boolean |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object.The default origin, arcpy.Point(0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0)) | Point |
| rotation_angle | The angle, in radians, to rotate the geometry around its origin.The default rotation angle is 0.0 radians (no rotation).(The default value is 0.0) | Float |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object. The default origin, arcpy.Point(0.0, 0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0, 0.0)) | Point |
| sx | The factor that will be used to scale the geometry along the x-axis. (The default value is 1.0) | Double |
| sy | The factor that will be used to scale the geometry along the y-axis. (The default value is 1.0) | Double |
| sz | The factor that will be used to scale the geometry along the z-axis. The geometry must be z-aware and have z-values.(The default value is 1.0) | Double |
| start_measure | The starting distance from the beginning of the line. | Double |
| end_measure | The ending distance from the beginning of the line. | Double |
| use_percentage | The start and end measures may be specified as fixed units or as a ratio.If True, start_measure and end_measure are used as a percentage; if False, start_measure and end_measure are used as a distance. For percentages, the measures should be expressed as a double from 0.0 (0 percent) to 1.0 (100 percent).(The default value is False) | Boolean |
| in_point | A point (PointGeometry or Point) to be snapped to the line. | PointGeometry |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### angleAndDistanceTo (other, {method})

Returns a tuple of angle and distance to a point or polygon.

### boundary ()

Constructs the boundary of the geometry.

### buffer (distance)

Constructs a polygon at a specified distance from the geometry.

### clip (envelope)

Constructs the intersection of the geometry and the specified extent.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### convexHull ()

Constructs the geometry that is the minimal bounding polygon such that all outer angles are convex.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### cut (cutter)

Splits this geometry into a part left of the cutting polyline, and a part right of it. When a polyline or polygon is cut, it is split where it intersects the cutter polyline. Each piece is classified as left of or right of the cutter. This classification is based on the orientation of the cutter line. Parts of the target polyline that do not intersect the cutting polyline are returned as part of the right of result for that input polyline. If a geometry is not cut, the left geometry will be empty (None).

### densify (method, distance, {deviation})

Creates a geometry with added vertices.

### difference (other)

Constructs the geometry that is composed only of the region unique to the base geometry but not part of the other geometry. The following illustration shows the results when the red polygon is the source geometry.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### distanceTo (other)

Returns the minimum distance between two geometries. The distance is in the units of the geometry's spatial reference. If the geometries intersect, the minimum distance is 0.Both geometries must have the same projection.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### generalize (max_offset)

Creates a new simplified geometry using a specified maximum offset tolerance.

### getArea ({method}, {units})

Returns the area of the feature using a measurement method.

### getLength ({method}, {units})

Returns the length of the feature using a measurement method.

### getPart ({index})

Returns an Array object of Point objects for a particular part of the geometry if an index is specified. If an index is not specified, an Array object containing an Array of Point objects for each geometry part is returned. The getPart method is equivalent to indexing an object; that is, obj.getPart(0) is equivalent to obj[0].

### intersect (other, dimension)

Constructs a geometry that is the geometric intersection of the two input geometries. Different dimension values can be used to create different shape types. The intersection of two geometries of the same shape type is a geometry containing only the regions of overlap between the original geometries. For faster results, test if the two geometries are disjoint before calling intersect.

### measureOnLine (in_point, {use_percentage})

Returns a measure from the start point of this line to the in_point.

### move ({dx}, {dy}, {dz})

Moves a geometry by specified distances along the x-, y-, and z-axes to create a new geometry.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### pointFromAngleAndDistance (angle, distance, {method})

Returns a point at a given angle in degrees and distance in the units of the geometry's spatial reference using the specified measurement type.

### positionAlongLine (value, {use_percentage}, {geodesic})

Returns a point on a line at a specified distance from the beginning of the line.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### queryPointAndDistance (in_point, {as_percentage})

Finds the point on the polyline nearest to the in_point and the distance between those points. It also returns information about the side of the line the point is on as well as the distance along the line where the nearest point occurs.

### rotate ({origin}, {rotation_angle})

Rotates a geometry around a specified origin by the degrees given in radians.The rotation is applied relative to the origin, so that the geometry rotates around the origin. The position of the rotated geometry is significantly affected by the choice of origin.Rotate does not apply to the z-direction.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The location of the geometry will change, but the geometry will maintain relative positions to other geometries rotated in the same way. Positions will rotate around the origin.The origin is at the centroid of the geometry (the centroid is within or touching geometry)—The geometry will rotate (spin) in place around its centroid.The origin is on a vertex of the geometry—The geometry will rotate around the chosen vertex.

### scale ({origin}, {sx}, {sy}, {sz})

Scales a geometry from a specified origin by specified factors along the x-, y-, and z-axes to create a new geometry. The position of a transformed point (or vertex) is given by ( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )The transformation is applied relative to the origin, so that the origin remains stationary while the geometry expands or contracts around it. The position and the direction of the expansion or contraction for the resulting geometries is significantly affected by the origin.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The size and location of the geometry will change, but the geometry will maintain relative positions to other geometries scaled in the same way. Positions will expand away from or contract toward the origin point.The origin is at the centroid of the geometry (if the centroid is within or touching geometry)—The size of the geometry will change, but the geometry's location will remain anchored at the centroid. The geometry will grow or shrink in place around the centroid.The origin is on a vertex of the geometry—The size of the geometry will change, but the position of the geometry will remain anchored at the chosen vertex. The geometry will grow from or shrink toward the chosen vertex.

### segmentAlongLine (start_measure, end_measure, {use_percentage})

Returns a Polyline between start and end measures. Similar to Polyline.positionAlongLine but will return a polyline segment between two points on the polyline instead of a single point.

### snapToLine (in_point)

Returns a new point based on in_point snapped to this geometry.

### symmetricDifference (other)

Constructs the geometry that is the union of two geometries minus the instersection of those geometries.The two input geometries must be the same shape type.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### union (other)

Constructs the geometry that is the set-theoretic union of the input geometries. The two geometries being unioned must be the same shape type.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
Geometry (geometry, inputs, {spatial_reference}, {has_z}, {has_m}, {has_id})
```

### Example 2

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 3

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 4

```python
angleAndDistanceTo (other, {method})
```

### Example 5

```python
boundary ()
```

### Example 6

```python
buffer (distance)
```

### Example 7

```python
clip (envelope)
```

### Example 8

```python
contains (second_geometry, {relation})
```

### Example 9

```python
convexHull ()
```

### Example 10

```python
crosses (second_geometry)
```

### Example 11

```python
cut (cutter)
```

### Example 12

```python
densify (method, distance, {deviation})
```

### Example 13

```python
difference (other)
```

### Example 14

```python
disjoint (second_geometry)
```

### Example 15

```python
distanceTo (other)
```

### Example 16

```python
equals (second_geometry)
```

### Example 17

```python
generalize (max_offset)
```

### Example 18

```python
getArea ({method}, {units})
```

### Example 19

```python
getLength ({method}, {units})
```

### Example 20

```python
getPart ({index})
```

### Example 21

```python
intersect (other, dimension)
```

### Example 22

```python
measureOnLine (in_point, {use_percentage})
```

### Example 23

```python
move ({dx}, {dy}, {dz})
```

### Example 24

```python
overlaps (second_geometry)
```

### Example 25

```python
pointFromAngleAndDistance (angle, distance, {method})
```

### Example 26

```python
positionAlongLine (value, {use_percentage}, {geodesic})
```

### Example 27

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 28

```python
queryPointAndDistance (in_point, {as_percentage})
```

### Example 29

```python
rotate ({origin}, {rotation_angle})
```

### Example 30

```python
scale ({origin}, {sx}, {sy}, {sz})
```

### Example 31

```python
segmentAlongLine (start_measure, end_measure, {use_percentage})
```

### Example 32

```python
snapToLine (in_point)
```

### Example 33

```python
symmetricDifference (other)
```

### Example 34

```python
touches (second_geometry)
```

### Example 35

```python
union (other)
```

### Example 36

```python
within (second_geometry, {relation})
```

### Example 37

```python
import arcpy

# Run the Copy Features tool, setting the output to the geometry object.
# geometries is returned as a list of geometry objects.
geometries = arcpy.CopyFeatures_management("c:/data/streets.shp",
                                           arcpy.Geometry())

# Walk through each geometry, totaling the length
length = 0
for geometry in geometries:
    length += geometry.length

print("Total length: {0}".format(length))
```

### Example 38

```python
import arcpy

# Run the Copy Features tool, setting the output to the geometry object.
# geometries is returned as a list of geometry objects.
geometries = arcpy.CopyFeatures_management("c:/data/streets.shp",
                                           arcpy.Geometry())

# Walk through each geometry, totaling the length
length = 0
for geometry in geometries:
    length += geometry.length

print("Total length: {0}".format(length))
```

---

## GeostatisticalDatasets

## Summary

The GeostatisticalDatasets class is used to manage datasets associated with a geostatistical model source. A geostatistical model source must be a geostatistical layer.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| ga_model_source | The geostatistical model source used to generate the properties of the class. The model source must be a geostatistical layer. | String |

## Code Samples

### Example 1

```python
GeostatisticalDatasets (ga_model_source)
```

### Example 2

```python
# Name: GeostatisticalDatasets_Example_01.py
# Description: Uses a Kernel Interpolation With Barriers model source
#   and changes the feature class and field to a new dataset and field.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
ga_layer = 'C:/data/kernelsmoothing.lyr'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(ga_layer)

# Set the dataset1 property to the new data
geo_datasets.dataset1 = 'C:/data/data.gdb/new'

# Set the new field
geo_datasets.dataset1Field = 'newfield'

# Create a new geostatistical layer with the new data
arcpy.GACreateGeostatisticalLayer_ga(ga_layer, geo_datasets, 'outGALayer1')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer1', 'C:/data/newlayer1.lyr',
                                 'ABSOLUTE')
```

### Example 3

```python
# Name: GeostatisticalDatasets_Example_01.py
# Description: Uses a Kernel Interpolation With Barriers model source
#   and changes the feature class and field to a new dataset and field.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
ga_layer = 'C:/data/kernelsmoothing.lyr'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(ga_layer)

# Set the dataset1 property to the new data
geo_datasets.dataset1 = 'C:/data/data.gdb/new'

# Set the new field
geo_datasets.dataset1Field = 'newfield'

# Create a new geostatistical layer with the new data
arcpy.GACreateGeostatisticalLayer_ga(ga_layer, geo_datasets, 'outGALayer1')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer1', 'C:/data/newlayer1.lyr',
                                 'ABSOLUTE')
```

### Example 4

```python
# Name: GeostatisticalDatasets_Example_02.py
# Description: Uses an IDW model source and adds a weight field.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
ga_layer = 'c:/data/IDW.lyr'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(ga_layer)

# Set the weight field
geo_datasets.dataset1WeightField = 'weightfield'

# Create a new geostatistical layer that uses a weight field
arcpy.GACreateGeostatisticalLayer_ga(ga_layer, geo_datasets, 'outGALayer2')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer2', 'C:/data/newlayer2.lyr',
                                 'ABSOLUTE')
```

### Example 5

```python
# Name: GeostatisticalDatasets_Example_02.py
# Description: Uses an IDW model source and adds a weight field.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
ga_layer = 'c:/data/IDW.lyr'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(ga_layer)

# Set the weight field
geo_datasets.dataset1WeightField = 'weightfield'

# Create a new geostatistical layer that uses a weight field
arcpy.GACreateGeostatisticalLayer_ga(ga_layer, geo_datasets, 'outGALayer2')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer2', 'C:/data/newlayer2.lyr',
                                 'ABSOLUTE')
```

### Example 6

```python
# Name: GeostatisticalDatasets_Example_03.py
# Description: Uses a cokriging model with two datasets and changes
#   the datasets, fields, and the declustering polygon feature class.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
cokriging_xml = 'C:/data/cokriging.xml'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(cokriging_xml)

# Set the first dataset and field
geo_datasets.dataset1 = 'C:/data/data.gdb/new1'
geo_datasets.dataset1Field = 'newfield1'

# Set the second dataset and field
geo_datasets.dataset2 = 'C:/data/data.gdb/new2'
geo_datasets.dataset2Field = 'newfield2'

# Set the new declustering polygons for the second dataset
geo_datasets.declusterPolygons2 = 'C:/data/data.gdb/decluster2'

# Create a new geostatistical layer with the new data
arcpy.GACreateGeostatisticalLayer_ga(cokriging_xml, geo_datasets, 'outGALayer3')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer3', 'C:/data/newlayer3.lyr',
                                 'ABSOLUTE')
```

### Example 7

```python
# Name: GeostatisticalDatasets_Example_03.py
# Description: Uses a cokriging model with two datasets and changes
#   the datasets, fields, and the declustering polygon feature class.

# Requirements: Geostatistical Analyst Extension

import arcpy

# Define the model source
cokriging_xml = 'C:/data/cokriging.xml'

# Create the GeostatisticalDatasets object
geo_datasets = arcpy.GeostatisticalDatasets(cokriging_xml)

# Set the first dataset and field
geo_datasets.dataset1 = 'C:/data/data.gdb/new1'
geo_datasets.dataset1Field = 'newfield1'

# Set the second dataset and field
geo_datasets.dataset2 = 'C:/data/data.gdb/new2'
geo_datasets.dataset2Field = 'newfield2'

# Set the new declustering polygons for the second dataset
geo_datasets.declusterPolygons2 = 'C:/data/data.gdb/decluster2'

# Create a new geostatistical layer with the new data
arcpy.GACreateGeostatisticalLayer_ga(cokriging_xml, geo_datasets, 'outGALayer3')

# Save the new geostatistical layer as a layer file
arcpy.SaveToLayerFile_management('outGALayer3', 'C:/data/newlayer3.lyr',
                                 'ABSOLUTE')
```

---

## Index

## Summary

The Index object contains information about an index on a table. There are two types of indexes: spatial and attribute. Spatial indexes exist on the shape field of a feature class.

## Code Samples

### Example 1

```python
import arcpy

feature_class = "c:/data/well.shp"

# Create a list of indexes using the ListIndexes function
indexes = arcpy.ListIndexes(feature_class)

# Iterate through the list of indexes
for index in indexes:
    # Print index properties
    print("Name: {0}".format(index.name))
    print("\tType            : {0}".format(index.isAscending))
    print("\tScale           : {0}".format(index.isUnique))
    print("\tNumber of fields: {0}".format(len(index.fields)))
```

### Example 2

```python
import arcpy

feature_class = "c:/data/well.shp"

# Create a list of indexes using the ListIndexes function
indexes = arcpy.ListIndexes(feature_class)

# Iterate through the list of indexes
for index in indexes:
    # Print index properties
    print("Name: {0}".format(index.name))
    print("\tType            : {0}".format(index.isAscending))
    print("\tScale           : {0}".format(index.isUnique))
    print("\tNumber of fields: {0}".format(len(index.fields)))
```

---

## Multipoint

## Summary

A Multipoint object is an ordered collection of points.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inputs | The coordinate information used to create the object. The data type can be Point or Array objects. | Object |
| spatial_reference | The spatial reference of the new geometry.(The default value is None) | SpatialReference |
| has_z | Specifies whether the geometry will be z-enabled.(The default value is False) | Boolean |
| has_m | Specifies whether the geometry will be m-enabled.(The default value is False) | Boolean |
| has_id | Specifies whether the geometry will support point IDs.(The default value is False) | Boolean |
| distance | The buffer distance.The buffer distance is in the same units as the geometry that is being buffered. A negative distance can only be specified against a polygon geometry. | Double |
| envelope | An Extent object used to define the clip extent. | Extent |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| cutter | The cutting polyline geometry. | PolyLine |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| index | The index position of the geometry. | Integer |
| other | The second geometry. | Object |
| dimension | The topological dimension (shape type) of the resulting geometry. 1—A zero-dimensional geometry (point or multipoint). 2—A one-dimensional geometry (polyline). 4—A two-dimensional geometry (polygon). | Integer |
| dx | The distance the geometry will be moved along the x-axis. (The default value is 0.0) | Double |
| dy | The distance the geometry will be moved along the y-axis. (The default value is 0.0) | Double |
| dz | The distance the geometry will be moved along the z-axis. The geometry must be z-aware and have z-values.(The default value is 0.0) | Double |
| second_geometry | A second geometry. | Object |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object.The default origin, arcpy.Point(0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0)) | Point |
| rotation_angle | The angle, in radians, to rotate the geometry around its origin.The default rotation angle is 0.0 radians (no rotation).(The default value is 0.0) | Float |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object. The default origin, arcpy.Point(0.0, 0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0, 0.0)) | Point |
| sx | The factor that will be used to scale the geometry along the x-axis. (The default value is 1.0) | Double |
| sy | The factor that will be used to scale the geometry along the y-axis. (The default value is 1.0) | Double |
| sz | The factor that will be used to scale the geometry along the z-axis. The geometry must be z-aware and have z-values.(The default value is 1.0) | Double |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### boundary ()

Constructs the boundary of the geometry.

### buffer (distance)

Constructs a polygon at a specified distance from the geometry.

### clip (envelope)

Constructs the intersection of the geometry and the specified extent.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### convexHull ()

Constructs the geometry that is the minimal bounding polygon such that all outer angles are convex.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### cut (cutter)

Splits this geometry into a part left of the cutting polyline, and a part right of it. When a polyline or polygon is cut, it is split where it intersects the cutter polyline. Each piece is classified as left of or right of the cutter. This classification is based on the orientation of the cutter line. Parts of the target polyline that do not intersect the cutting polyline are returned as part of the right of result for that input polyline. If a geometry is not cut, the left geometry will be empty (None).

### difference (other)

Constructs the geometry that is composed only of the region unique to the base geometry but not part of the other geometry. The following illustration shows the results when the red polygon is the source geometry.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### distanceTo (other)

Returns the minimum distance between two geometries. The distance is in the units of the geometry's spatial reference. If the geometries intersect, the minimum distance is 0.Both geometries must have the same projection.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### getPart ({index})

Returns an Array object of Point objects for a particular part of the geometry if an index is specified. If an index is not specified, an Array object containing an Array of Point objects for each geometry part is returned. The getPart method is equivalent to indexing an object; that is, obj.getPart(0) is equivalent to obj[0].

### intersect (other, dimension)

Constructs a geometry that is the geometric intersection of the two input geometries. Different dimension values can be used to create different shape types. The intersection of two geometries of the same shape type is a geometry containing only the regions of overlap between the original geometries. For faster results, test if the two geometries are disjoint before calling intersect.

### move ({dx}, {dy}, {dz})

Moves a geometry by specified distances along the x-, y-, and z-axes to create a new geometry.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### rotate ({origin}, {rotation_angle})

Rotates a geometry around a specified origin by the degrees given in radians.The rotation is applied relative to the origin, so that the geometry rotates around the origin. The position of the rotated geometry is significantly affected by the choice of origin.Rotate does not apply to the z-direction.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The location of the geometry will change, but the geometry will maintain relative positions to other geometries rotated in the same way. Positions will rotate around the origin.The origin is at the centroid of the geometry (the centroid is within or touching geometry)—The geometry will rotate (spin) in place around its centroid.The origin is on a vertex of the geometry—The geometry will rotate around the chosen vertex.

### scale ({origin}, {sx}, {sy}, {sz})

Scales a geometry from a specified origin by specified factors along the x-, y-, and z-axes to create a new geometry. The position of a transformed point (or vertex) is given by ( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )The transformation is applied relative to the origin, so that the origin remains stationary while the geometry expands or contracts around it. The position and the direction of the expansion or contraction for the resulting geometries is significantly affected by the origin.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The size and location of the geometry will change, but the geometry will maintain relative positions to other geometries scaled in the same way. Positions will expand away from or contract toward the origin point.The origin is at the centroid of the geometry (if the centroid is within or touching geometry)—The size of the geometry will change, but the geometry's location will remain anchored at the centroid. The geometry will grow or shrink in place around the centroid.The origin is on a vertex of the geometry—The size of the geometry will change, but the position of the geometry will remain anchored at the chosen vertex. The geometry will grow from or shrink toward the chosen vertex.

### symmetricDifference (other)

Constructs the geometry that is the union of two geometries minus the instersection of those geometries.The two input geometries must be the same shape type.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### union (other)

Constructs the geometry that is the set-theoretic union of the input geometries. The two geometries being unioned must be the same shape type.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
Multipoint (inputs, {spatial_reference}, {has_z}, {has_m}, {has_id})
```

### Example 2

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 3

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 4

```python
boundary ()
```

### Example 5

```python
buffer (distance)
```

### Example 6

```python
clip (envelope)
```

### Example 7

```python
contains (second_geometry, {relation})
```

### Example 8

```python
convexHull ()
```

### Example 9

```python
crosses (second_geometry)
```

### Example 10

```python
cut (cutter)
```

### Example 11

```python
difference (other)
```

### Example 12

```python
disjoint (second_geometry)
```

### Example 13

```python
distanceTo (other)
```

### Example 14

```python
equals (second_geometry)
```

### Example 15

```python
getPart ({index})
```

### Example 16

```python
intersect (other, dimension)
```

### Example 17

```python
move ({dx}, {dy}, {dz})
```

### Example 18

```python
overlaps (second_geometry)
```

### Example 19

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 20

```python
rotate ({origin}, {rotation_angle})
```

### Example 21

```python
scale ({origin}, {sx}, {sy}, {sz})
```

### Example 22

```python
symmetricDifference (other)
```

### Example 23

```python
touches (second_geometry)
```

### Example 24

```python
union (other)
```

### Example 25

```python
within (second_geometry, {relation})
```

### Example 26

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Multipoint objects
features = []

# Create Multipoint objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
    multipoint = arcpy.Multipoint(array, spatial_ref)
    features.append(multipoint)

# Persist a copy of the Multipoint objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/multipoints.shp")
```

### Example 27

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will hold each of the Multipoint objects
features = []

# Create Multipoint objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
    multipoint = arcpy.Multipoint(array, spatial_ref)
    features.append(multipoint)

# Persist a copy of the Multipoint objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/multipoints.shp")
```

---

## NetCDFFileProperties

## Summary

The network Common Data Form (netCDF) is a binary, self-describing, machine-independent file format for storing scientific data.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| netcdffile | The input netCDF file. | String |
| variable_name[variable_name,...] | A variable name of the netCDF file. | String |
| variable_name | A variable name of the netCDF file. | String |
| attribute_name | An attribute name of the netCDF file. | String |
| dimension_name | A dimension name of the netCDF file. | String |
| value | The dimension value. | Integer |
| dimension_name | A dimension name of the netCDF file. | String |
| dimension_name | A dimension name of the netCDF file. | String |
| index | The index position. | Integer |
| variable_name | A variable name of the netCDF file. | String |
| name | A variable or dimension name of the netCDF file. | String |
| variable_name | A variable name of the netCDF file. | String |
| x_dimension | The x-dimension. | Integer |
| y_dimension | The y-dimension. | Integer |
| dimension_name | A variable name of the netCDF file. | String |

## Methods

### getAttributeNames ({variable_name})

Returns the attribute names of a variable in a netCDF file.

### getAttributeValue (variable_name, attribute_name)

Returns the value of an attribute.

### getDimensionIndex (dimension_name, value)

Returns the dimension index.

### getDimensionSize (dimension_name)

Returns the dimension size.

### getDimensionValue (dimension_name, index)

Returns the dimension value.

### getDimensions ()

Returns the dimensions.

### getDimensionsByVariable (variable_name)

Returns the dimensions by variable.

### getFieldType (name)

Returns the field type of a variable or dimension.

### getSpatialReference (variable_name, x_dimension, y_dimension)

Returns the spatial reference of a variable.

### getVariables ()

Returns the variables.

### getVariablesByDimension (dimension_name)

Returns the variables by dimension.

## Code Samples

### Example 1

```python
NetCDFFileProperties (netcdffile)
```

### Example 2

```python
getAttributeNames ({variable_name})
```

### Example 3

```python
getAttributeValue (variable_name, attribute_name)
```

### Example 4

```python
getDimensionIndex (dimension_name, value)
```

### Example 5

```python
getDimensionSize (dimension_name)
```

### Example 6

```python
getDimensionValue (dimension_name, index)
```

### Example 7

```python
getDimensions ()
```

### Example 8

```python
getDimensionsByVariable (variable_name)
```

### Example 9

```python
getFieldType (name)
```

### Example 10

```python
getSpatialReference (variable_name, x_dimension, y_dimension)
```

### Example 11

```python
getVariables ()
```

### Example 12

```python
getVariablesByDimension (dimension_name)
```

### Example 13

```python
import arcpy

in_netcdf = "c:/netCDF/crwr.nc"

nc_fp = arcpy.NetCDFFileProperties(in_netcdf)

# Get Variables
for nc_var in nc_fp.getVariables():
    print("Variable: {}".format(nc_var))
    print("\tVariable type: {}".format(nc_fp.getFieldType(nc_var)))

    # Get dimensions by variable
    for nc_dim_by_var in nc_fp.getDimensionsByVariable(nc_var):
        print("Dimension: {}".format(nc_dim_by_var))
    print(nc_fp.getAttributeValue(nc_var, "units"))

    # Get Variable Attributes
    for nc_va_name in nc_fp.getAttributeNames(nc_var):
        print("Attribute Name: {}".format(nc_va_name))

# Get Dimensions
for nc_dim in nc_fp.getDimensions():
    print("Dimension: {}".format(nc_dim))
    print("\tDimension size: {}".format(nc_fp.getDimensionSize(nc_dim)))
    print("\tDimension type: {}".format(nc_fp.getFieldType(nc_dim)))

    for i in range(0, nc_fp.getDimensionSize(nc_dim)):
        nc_dim_value = nc_fp.getDimensionValue(nc_dim, i)
        print("\tDimension value: {}".format(nc_dim_value))
        print("\tDimension index: {}".format(
            nc_fp.getDimensionIndex(nc_dim, nc_dim_value)))

    # Get Variable by dimension
    for nc_vars_by_dim in nc_fp.getVariablesByDimension(nc_dim):
        print("\tVariable by dimension: {}".format(nc_vars_by_dim))

# Get Global Attribues
for nc_att_name in nc_fp.getAttributeNames(""):
    print("Attribute Name: {}".format(nc_att_name))
    print(nc_fp.getAttributeValue("", nc_att_name))
```

### Example 14

```python
import arcpy

in_netcdf = "c:/netCDF/crwr.nc"

nc_fp = arcpy.NetCDFFileProperties(in_netcdf)

# Get Variables
for nc_var in nc_fp.getVariables():
    print("Variable: {}".format(nc_var))
    print("\tVariable type: {}".format(nc_fp.getFieldType(nc_var)))

    # Get dimensions by variable
    for nc_dim_by_var in nc_fp.getDimensionsByVariable(nc_var):
        print("Dimension: {}".format(nc_dim_by_var))
    print(nc_fp.getAttributeValue(nc_var, "units"))

    # Get Variable Attributes
    for nc_va_name in nc_fp.getAttributeNames(nc_var):
        print("Attribute Name: {}".format(nc_va_name))

# Get Dimensions
for nc_dim in nc_fp.getDimensions():
    print("Dimension: {}".format(nc_dim))
    print("\tDimension size: {}".format(nc_fp.getDimensionSize(nc_dim)))
    print("\tDimension type: {}".format(nc_fp.getFieldType(nc_dim)))

    for i in range(0, nc_fp.getDimensionSize(nc_dim)):
        nc_dim_value = nc_fp.getDimensionValue(nc_dim, i)
        print("\tDimension value: {}".format(nc_dim_value))
        print("\tDimension index: {}".format(
            nc_fp.getDimensionIndex(nc_dim, nc_dim_value)))

    # Get Variable by dimension
    for nc_vars_by_dim in nc_fp.getVariablesByDimension(nc_dim):
        print("\tVariable by dimension: {}".format(nc_vars_by_dim))

# Get Global Attribues
for nc_att_name in nc_fp.getAttributeNames(""):
    print("Attribute Name: {}".format(nc_att_name))
    print(nc_fp.getAttributeValue("", nc_att_name))
```

---

## Parameter

## Summary

Every tool parameter has an associated Parameter object with properties and methods that are useful in tool validation.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| name | The parameter name. (The default value is None) | String |
| displayName | The parameter label as shown in the Geoprocessing pane.(The default value is None) | String |
| direction | The direction of the parameter. (The default value is Input) | String |
| datatype | The data type of the parameter.For a list of parameter data types, see Geoprocessing data types.(The default value is GPString) | String |
| parameterType | The parameter type.(The default value is Required) | String |
| enabled | Specifies whether the parameter is visible in the Geoprocessing pane.(The default value is True) | Boolean |
| category | The category of the parameter. (The default value is None) | String |
| symbology | The path to a layer file (.lyrx or .lyr) used for drawing the output.(The default value is None) | String |
| multiValue | Specifies whether the parameter is a multivalue parameter.(The default value is False) | Boolean |
| message | The string to be added as an error message to the geoprocessing tool messages. | String |
| message_type | Defines whether the message will be an error or a warning. ERROR—The message will be an error message.WARNING—The message will be a warning message. | String |
| message_ID | The message ID allows you to reference existing system messages. | Integer |
| add_argument1 | Depending on which message ID is used, an argument may be necessary to complete the message. Common examples include dataset or field names. The data type is variable depending on the message. | Object |
| add_argument2 | Depending on which message ID is used, an argument may be necessary to complete the message. Common examples include dataset or field names. The data type is variable depending on the message. | Object |
| message | The string to be added as a warning message to the geoprocessing tool messages. | String |

## Methods

### clearMessage ()

Clears out any message text and sets the status to informative (no error or warning).

### hasError ()

Returns True if the parameter contains an error.To evaluate whether a parameter has an error, hasError should be called within the tool validation's updateMessages method.

### hasWarning ()

Returns True if the parameter contains a warning.

### isInputValueDerived ()

Returns True if the tool is being validated inside a Model and the input value is the output of another tool in the model.

### setErrorMessage (message)

Sets a parameter as having an error with the supplied message. Tools do not execute if any of the parameters have an error.

### setIDMessage (message_type, message_ID, {add_argument1}, {add_argument2})

Sets a parameter as having a system message.

### setWarningMessage (message)

Sets a parameter as having an error with the supplied message. Unlike errors, tools will execute with warning messages.

## Code Samples

### Example 1

```python
Parameter ({name}, {displayName}, {direction}, {datatype}, {parameterType}, {enabled}, {category}, {symbology}, {multiValue})
```

### Example 2

```python
import arcpy
param = arcpy.Parameter()
param.datatype = "GPValueTable"
param.columns = [["GPFeatureLayer", "Features"], ["GPLong", "Ranks"]]
```

### Example 3

```python
import arcpy
param = arcpy.Parameter()
param.datatype = "GPValueTable"
param.columns = [["GPFeatureLayer", "Features"], ["GPLong", "Ranks"]]
```

### Example 4

```python
class ValueTableSampleTool(object):
    # __init__ left out to simplify example

    def getParameterInfo(self):
        in_fc = arcpy.Parameter(
            name='in_features',
            displayName='Input Features',
            datatype='GPFeatureLayer',
            direction='Input',
            parameterType='Required')

        vt = arcpy.Parameter(
            name='summary_fields',
            displayName='Summary fields',
            datatype='GPValueTable',
            direction='Input',
            parameterType='Optional')

        vt.parameterDependencies = [in_fc.name]
        vt.columns = [['Field', 'Field'], ['GPString', 'Statistic'], ['GPDouble', 'Multiplier']]
        vt.filters[0].list = ['Double', 'Float', 'Short', 'Long']
        vt.filters[1].type = 'ValueList'
        vt.filters[1].list = ['SUM', 'MIN', 'MAX', 'MEAN']
        vt.filters[2].type = 'Range'
        vt.filters[2].list = [0, 10]

        return [in_fc, vt]
```

### Example 5

```python
class ValueTableSampleTool(object):
    # __init__ left out to simplify example

    def getParameterInfo(self):
        in_fc = arcpy.Parameter(
            name='in_features',
            displayName='Input Features',
            datatype='GPFeatureLayer',
            direction='Input',
            parameterType='Required')

        vt = arcpy.Parameter(
            name='summary_fields',
            displayName='Summary fields',
            datatype='GPValueTable',
            direction='Input',
            parameterType='Optional')

        vt.parameterDependencies = [in_fc.name]
        vt.columns = [['Field', 'Field'], ['GPString', 'Statistic'], ['GPDouble', 'Multiplier']]
        vt.filters[0].list = ['Double', 'Float', 'Short', 'Long']
        vt.filters[1].type = 'ValueList'
        vt.filters[1].list = ['SUM', 'MIN', 'MAX', 'MEAN']
        vt.filters[2].type = 'Range'
        vt.filters[2].list = [0, 10]

        return [in_fc, vt]
```

### Example 6

```python
class CompositeSampleTool(object):
    # __init__ left out to simplify example

    def getParameterInfo(self):
        composite = arcpy.Parameter(
            name="composite_example",
            displayName="Composite Example",
            datatype=["GPString", "GPDouble"],
            parameterType="Optional",
            direction="Input",
            multiValue=True)

        composite.filters = ["CodedValue", "Range"]
        composite.filters[0].list = ["MIN", "MAX"]
        composite.filters[1].list = [1, 100]

        return [composite]
```

### Example 7

```python
class CompositeSampleTool(object):
    # __init__ left out to simplify example

    def getParameterInfo(self):
        composite = arcpy.Parameter(
            name="composite_example",
            displayName="Composite Example",
            datatype=["GPString", "GPDouble"],
            parameterType="Optional",
            direction="Input",
            multiValue=True)

        composite.filters = ["CodedValue", "Range"]
        composite.filters[0].list = ["MIN", "MAX"]
        composite.filters[1].list = [1, 100]

        return [composite]
```

### Example 8

```python
clearMessage ()
```

### Example 9

```python
hasError ()
```

### Example 10

```python
hasWarning ()
```

### Example 11

```python
isInputValueDerived ()
```

### Example 12

```python
setErrorMessage (message)
```

### Example 13

```python
setIDMessage (message_type, message_ID, {add_argument1}, {add_argument2})
```

### Example 14

```python
setWarningMessage (message)
```

### Example 15

```python
def updateParameters(self):
    # If the option to use a weights file ("Get Spatial Weights From File") 
    # is selected, enable the parameter for specifying the file; 
    # otherwise, disable it.

    if self.params[3].value == "Get Spatial Weights From File":
        self.params[8].enabled = True
    else:
        self.params[8].enabled = False

    return
```

### Example 16

```python
def updateParameters(self):
    # If the option to use a weights file ("Get Spatial Weights From File") 
    # is selected, enable the parameter for specifying the file; 
    # otherwise, disable it.

    if self.params[3].value == "Get Spatial Weights From File":
        self.params[8].enabled = True
    else:
        self.params[8].enabled = False

    return
```

### Example 17

```python
def updateParameters(self):
    # Set the default distance threshold to 1/100 of the larger of
    # the width or height of the extent of the input features.  Do
    # not set if there is no input dataset yet, or the user has set
    # a specific distance (Altered is true).

    if self.params[0].value:
        if not self.params[6].altered:
            extent = arcpy.Describe(self.params[0].value)
        width = extent.XMax - extent.XMin
        height = extent.YMax - extent.YMin

        if width < height:
            self.params[6].value = width / 100
        else:
            self.params[6].value = height / 100

        return
```

### Example 18

```python
def updateParameters(self):
    # Set the default distance threshold to 1/100 of the larger of
    # the width or height of the extent of the input features.  Do
    # not set if there is no input dataset yet, or the user has set
    # a specific distance (Altered is true).

    if self.params[0].value:
        if not self.params[6].altered:
            extent = arcpy.Describe(self.params[0].value)
        width = extent.XMax - extent.XMin
        height = extent.YMax - extent.YMin

        if width < height:
            self.params[6].value = width / 100
        else:
            self.params[6].value = height / 100

        return
```

### Example 19

```python
def updateMessages(self):
    self.params[6].clearMessage()

    # Check whether the threshold distance contains a value of
    # zero and the user has specified a fixed distance band.
    if self.params[6].value <= 0:
        if self.params[3].value == "Fixed Distance Band":
            self.params[6].setErrorMessage(
                "Zero or a negative distance is invalid when "
                "using a fixed distance band. Please use a "
                "positive value greater than zero.")
        elif self.params[6].value < 0:
            self.params[6].setErrorMessage(
                "A positive distance value is required when "
                "using a fixed distance band. Be sure to specify "
                "a distance.")

    return
```

### Example 20

```python
def updateMessages(self):
    self.params[6].clearMessage()

    # Check whether the threshold distance contains a value of
    # zero and the user has specified a fixed distance band.
    if self.params[6].value <= 0:
        if self.params[3].value == "Fixed Distance Band":
            self.params[6].setErrorMessage(
                "Zero or a negative distance is invalid when "
                "using a fixed distance band. Please use a "
                "positive value greater than zero.")
        elif self.params[6].value < 0:
            self.params[6].setErrorMessage(
                "A positive distance value is required when "
                "using a fixed distance band. Be sure to specify "
                "a distance.")

    return
```

---

## PauseDrawing

## Summary

The PauseDrawing class pauses the drawing of the map view while using it within a context manager (with statement).

## Code Samples

### Example 1

```python
PauseDrawing ()
```

### Example 2

```python
import arcpy
from random import randint

featureclass_1 = r"c:\data\myGDB.gdb\fc1"
featureclass_2 = r"c:\data\myGDB.gdb\fc2"

with arcpy.PauseDrawing():
    with arcpy.da.UpdateCursor(featureclass_1, "class_field") as cursor:
        for row in cursor:
            classification = randint(1, 5)
            row[0] = classification
            cursor.updateRow(row)

    with arcpy.da.UpdateCursor(featureclass_2, "class_field") as cursor:
        for row in cursor:
            classification = randint(1, 5)
            row[0] = classification
            cursor.updateRow(row)
    arcpy.RefreshLayer((featureclass_1, featureclass_2))

# The map view will refresh now that the PauseDrawing context manager has closed.
```

### Example 3

```python
import arcpy
from random import randint

featureclass_1 = r"c:\data\myGDB.gdb\fc1"
featureclass_2 = r"c:\data\myGDB.gdb\fc2"

with arcpy.PauseDrawing():
    with arcpy.da.UpdateCursor(featureclass_1, "class_field") as cursor:
        for row in cursor:
            classification = randint(1, 5)
            row[0] = classification
            cursor.updateRow(row)

    with arcpy.da.UpdateCursor(featureclass_2, "class_field") as cursor:
        for row in cursor:
            classification = randint(1, 5)
            row[0] = classification
            cursor.updateRow(row)
    arcpy.RefreshLayer((featureclass_1, featureclass_2))

# The map view will refresh now that the PauseDrawing context manager has closed.
```

### Example 4

```python
import arcpy
from random import randint

featureclass_1 = r"c:\data\myGDB.gdb\fc1"
featureclass_2 = r"c:\data\myGDB.gdb\fc2"

calculation_code_block = """
from random import randint
def f():
    return randint(1, 5)
"""

with arcpy.PauseDrawing():
    # Use cursors to copy geometries from one feature layer to another
    with arcpy.da.InsertCursor(featureclass_1, ["SHAPE@"]) as icur:
        with arcpy.da.SearchCursor(featureclass_2, "SHAPE@") as scur:
            for row in scur:
                icur.insertRow((row[0]))

    # Use CalculateField to update the class field
    arcpy.management.CalculateField(
        in_table=featureclass_1,
        field="class",
        expression="f()",
        expression_type="PYTHON3",
        code_block=calculation_code_block
        )

# The map view will refresh now that the PauseDrawing context manager has closed.
```

### Example 5

```python
import arcpy
from random import randint

featureclass_1 = r"c:\data\myGDB.gdb\fc1"
featureclass_2 = r"c:\data\myGDB.gdb\fc2"

calculation_code_block = """
from random import randint
def f():
    return randint(1, 5)
"""

with arcpy.PauseDrawing():
    # Use cursors to copy geometries from one feature layer to another
    with arcpy.da.InsertCursor(featureclass_1, ["SHAPE@"]) as icur:
        with arcpy.da.SearchCursor(featureclass_2, "SHAPE@") as scur:
            for row in scur:
                icur.insertRow((row[0]))

    # Use CalculateField to update the class field
    arcpy.management.CalculateField(
        in_table=featureclass_1,
        field="class",
        expression="f()",
        expression_type="PYTHON3",
        code_block=calculation_code_block
        )

# The map view will refresh now that the PauseDrawing context manager has closed.
```

---

## Point

## Summary

A representation of an x,y pair, optionally with measure, height, and ID attributes.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| X | The X coordinate of the point. (The default value is 0.0) | Double |
| Y | The Y coordinate of the point. (The default value is 0.0) | Double |
| Z | The Z coordinate of the point. (The default value is None) | Double |
| M | The M value of the point. (The default value is None) | Double |
| ID | The shape ID of the point. (The default value is 0) | Integer |
| point_object | A Point object. | Point |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### clone (point_object)

Clone the Point object.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
pt = arcpy.Point(-12683890.6, 5811151.5)
pt_geometry = arcpy.PointGeometry(pt, spatial_reference=arcpy.SpatialReference(3857))
```

### Example 2

```python
pt = arcpy.Point(-12683890.6, 5811151.5)
pt_geometry = arcpy.PointGeometry(pt, spatial_reference=arcpy.SpatialReference(3857))
```

### Example 3

```python
Point ({X}, {Y}, {Z}, {M}, {ID})
```

### Example 4

```python
clone (point_object)
```

### Example 5

```python
contains (second_geometry, {relation})
```

### Example 6

```python
crosses (second_geometry)
```

### Example 7

```python
disjoint (second_geometry)
```

### Example 8

```python
equals (second_geometry)
```

### Example 9

```python
overlaps (second_geometry)
```

### Example 10

```python
touches (second_geometry)
```

### Example 11

```python
within (second_geometry, {relation})
```

### Example 12

```python
import arcpy

# Create point object
point = arcpy.Point(2000, 2500)

# Print point properties
print("Point properties:")
print(" X:  {0}".format(point.X))
print(" Y:  {0}".format(point.Y))
```

### Example 13

```python
import arcpy

# Create point object
point = arcpy.Point(2000, 2500)

# Print point properties
print("Point properties:")
print(" X:  {0}".format(point.X))
print(" Y:  {0}".format(point.Y))
```

### Example 14

```python
import arcpy

# Create cursor to retrieve Hawaii shape
feature_class = "c:/data/Hawaii.shp"
cursor = arcpy.da.SearchCursor(feature_class, ["SHAPE@"])

for row in cursor:
    # Get the geometry object from the shape field
    print("Number of Hawaiian islands: {0}".format(row[0].partCount))

    # GetPart returns an array of point objects for each part.
    for island in row[0].getPart():
        print("Vertices in island: {0}".format(island.count))
        for point in island:
            print("X: {0}, Y: {1})".format(point.X, point.Y))
```

### Example 15

```python
import arcpy

# Create cursor to retrieve Hawaii shape
feature_class = "c:/data/Hawaii.shp"
cursor = arcpy.da.SearchCursor(feature_class, ["SHAPE@"])

for row in cursor:
    # Get the geometry object from the shape field
    print("Number of Hawaiian islands: {0}".format(row[0].partCount))

    # GetPart returns an array of point objects for each part.
    for island in row[0].getPart():
        print("Vertices in island: {0}".format(island.count))
        for point in island:
            print("X: {0}, Y: {1})".format(point.X, point.Y))
```

---

## PointGeometry

## Summary

A PointGeometry object is a shape that has neither length nor area at a given scale.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inputs | A Point object used to create the object. | Point |
| spatial_reference | The spatial reference of the new geometry.(The default value is None) | SpatialReference |
| has_z | Specifies whether the geometry will be z-enabled.(The default value is False) | Boolean |
| has_m | Specifies whether the geometry will be m-enabled.(The default value is False) | Boolean |
| has_id | Specifies whether the geometry will support point IDs.(The default value is False) | Boolean |
| other | The second geometry. If the geometry is a polygon, the distance is measured to the centroid of the polygon. | PointGeometry |
| method | The method used to measure distance. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| distance | The buffer distance.The buffer distance is in the same units as the geometry that is being buffered. A negative distance can only be specified against a polygon geometry. | Double |
| envelope | An Extent object used to define the clip extent. | Extent |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| precision | The precision length of the hash string to return for the PointGeometry. The minimum length is 1 and the maximum length is 20. The default length is 8.(The default value is 8) | Integer |
| index | The index position of the geometry. | Integer |
| other | The second geometry. | Object |
| dimension | The topological dimension (shape type) of the resulting geometry. 1—A zero-dimensional geometry (point or multipoint). 2—A one-dimensional geometry (polyline). 4—A two-dimensional geometry (polygon). | Integer |
| dx | The distance the geometry will be moved along the x-axis. (The default value is 0.0) | Double |
| dy | The distance the geometry will be moved along the y-axis. (The default value is 0.0) | Double |
| dz | The distance the geometry will be moved along the z-axis. The geometry must be z-aware and have z-values.(The default value is 0.0) | Double |
| second_geometry | A second geometry. | Object |
| angle | The angle in degrees to the returned point. | Double |
| distance | The distance in the units of the geometry's spatial reference to the returned point. | Double |
| method | PLANAR measurements reflect the projection of geographic data onto the 2D surface (in other words, they will not take into account the curvature of the earth). GEODESIC, GREAT_ELLIPTIC, LOXODROME, or PRESERVE_SHAPE measurement types can be chosen as an alternative if desired. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is when you want to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—A loxodrome is not the shortest distance between two points but instead defines the line of constant bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system, and the 2D plane of that coordinate system will be used as the basis for the measurements.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object.The default origin, arcpy.Point(0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0)) | Point |
| rotation_angle | The angle, in radians, to rotate the geometry around its origin.The default rotation angle is 0.0 radians (no rotation).(The default value is 0.0) | Float |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object. The default origin, arcpy.Point(0.0, 0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0, 0.0)) | Point |
| sx | The factor that will be used to scale the geometry along the x-axis. (The default value is 1.0) | Double |
| sy | The factor that will be used to scale the geometry along the y-axis. (The default value is 1.0) | Double |
| sz | The factor that will be used to scale the geometry along the z-axis. The geometry must be z-aware and have z-values.(The default value is 1.0) | Double |
| other | A second geometry. | Object |
| notation | The coordinate system notation to be generated. DD— Decimal degrees is used, for example, 34.05719570N 117.19647020W.DDM— Degrees decimal minutes is used, for example, 34 03.43174200N 117 11.78821200W.DMS— Degree Minute Seconds, is used, for example, 34 03 25.90452000N 117 11 47.29272000W.GARS— Global Area Reference System is used, for example, 126LJ47. It is based on latitude and longitude, and it divides and subdivides the world into cells.GEOREF— World Geographic Reference System is used, for example, EJCE4821203432.MGRS— Military Grid Reference System is used, for example, 11SMT8186968515.USNG— United States National Grid is used, for example, 11S MT 81869 68515.UTM— Universal Transverse Mercator is used, for example, 11S 481868 3768515. It is based on zone number, MGRS latitude band, and the easting and northing planar coordinate pair in that zone.UTMNS— Universal Transverse Mercator (no spaces) is used, for example, 11N4818683768515. It is based on zone number, hemisphere designator, and the easting and northing planar coordinate pair in that zone. | None |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### angleAndDistanceTo (other, {method})

Returns a tuple of angle and distance to a point or polygon.

### boundary ()

Constructs the boundary of the geometry.

### buffer (distance)

Constructs a polygon at a specified distance from the geometry.

### clip (envelope)

Constructs the intersection of the geometry and the specified extent.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### convexHull ()

Constructs the geometry that is the minimal bounding polygon such that all outer angles are convex.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### difference (other)

Constructs the geometry that is composed only of the region unique to the base geometry but not part of the other geometry. The following illustration shows the results when the red polygon is the source geometry.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### distanceTo (other)

Returns the minimum distance between two geometries. The distance is in the units of the geometry's spatial reference. If the geometries intersect, the minimum distance is 0.Both geometries must have the same projection.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### getGeohash (precision)

Converts a PointGeometry in geographic coordinate system coordinates of latitude and longitude to a geohash string that is accurate to an arbitrary precision within a bounding box in the geohash grid.

### getPart ({index})

Returns an Array object of Point objects for a particular part of the geometry if an index is specified. If an index is not specified, an Array object containing an Array of Point objects for each geometry part is returned. The getPart method is equivalent to indexing an object; that is, obj.getPart(0) is equivalent to obj[0].

### intersect (other, dimension)

Constructs a geometry that is the geometric intersection of the two input geometries. Different dimension values can be used to create different shape types. The intersection of two geometries of the same shape type is a geometry containing only the regions of overlap between the original geometries. For faster results, test if the two geometries are disjoint before calling intersect.

### move ({dx}, {dy}, {dz})

Moves a geometry by specified distances along the x-, y-, and z-axes to create a new geometry.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### pointFromAngleAndDistance (angle, distance, {method})

Returns a point at a given angle in degrees and distance in the units of the geometry's spatial reference using the specified measurement type.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### rotate ({origin}, {rotation_angle})

Rotates a geometry around a specified origin by the degrees given in radians.The rotation is applied relative to the origin, so that the geometry rotates around the origin. The position of the rotated geometry is significantly affected by the choice of origin.Rotate does not apply to the z-direction.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The location of the geometry will change, but the geometry will maintain relative positions to other geometries rotated in the same way. Positions will rotate around the origin.The origin is at the centroid of the geometry (the centroid is within or touching geometry)—The geometry will rotate (spin) in place around its centroid.The origin is on a vertex of the geometry—The geometry will rotate around the chosen vertex.

### scale ({origin}, {sx}, {sy}, {sz})

Scales a geometry from a specified origin by specified factors along the x-, y-, and z-axes to create a new geometry. The position of a transformed point (or vertex) is given by ( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )The transformation is applied relative to the origin, so that the origin remains stationary while the geometry expands or contracts around it. The position and the direction of the expansion or contraction for the resulting geometries is significantly affected by the origin.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The size and location of the geometry will change, but the geometry will maintain relative positions to other geometries scaled in the same way. Positions will expand away from or contract toward the origin point.The origin is at the centroid of the geometry (if the centroid is within or touching geometry)—The size of the geometry will change, but the geometry's location will remain anchored at the centroid. The geometry will grow or shrink in place around the centroid.The origin is on a vertex of the geometry—The size of the geometry will change, but the position of the geometry will remain anchored at the chosen vertex. The geometry will grow from or shrink toward the chosen vertex.

### symmetricDifference (other)

Constructs the geometry that is the union of two geometries minus the instersection of those geometries.The two input geometries must be the same shape type.

### toCoordString (notation)

Converts a PointGeometry to the selected coordinate system notation.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### union (other)

Constructs the geometry that is the set-theoretic union of the input geometries. The two geometries being unioned must be the same shape type.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
PointGeometry (inputs, {spatial_reference}, {has_z}, {has_m}, {has_id})
```

### Example 2

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 3

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 4

```python
angleAndDistanceTo (other, {method})
```

### Example 5

```python
boundary ()
```

### Example 6

```python
buffer (distance)
```

### Example 7

```python
clip (envelope)
```

### Example 8

```python
contains (second_geometry, {relation})
```

### Example 9

```python
convexHull ()
```

### Example 10

```python
crosses (second_geometry)
```

### Example 11

```python
difference (other)
```

### Example 12

```python
disjoint (second_geometry)
```

### Example 13

```python
distanceTo (other)
```

### Example 14

```python
equals (second_geometry)
```

### Example 15

```python
getGeohash (precision)
```

### Example 16

```python
import arcpy

# Spatial reference set to GCS_WGS_1984
spatial_reference = arcpy.SpatialReference(4326)
pnt = arcpy.Point(-88.236, 40.096)
pnt_geometry = arcpy.PointGeometry(pnt, spatial_reference)
print(pnt_geometry.getGeohash(6))  # dp1k05
```

### Example 17

```python
import arcpy

# Spatial reference set to GCS_WGS_1984
spatial_reference = arcpy.SpatialReference(4326)
pnt = arcpy.Point(-88.236, 40.096)
pnt_geometry = arcpy.PointGeometry(pnt, spatial_reference)
print(pnt_geometry.getGeohash(6))  # dp1k05
```

### Example 18

```python
getPart ({index})
```

### Example 19

```python
intersect (other, dimension)
```

### Example 20

```python
move ({dx}, {dy}, {dz})
```

### Example 21

```python
overlaps (second_geometry)
```

### Example 22

```python
pointFromAngleAndDistance (angle, distance, {method})
```

### Example 23

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 24

```python
rotate ({origin}, {rotation_angle})
```

### Example 25

```python
scale ({origin}, {sx}, {sy}, {sz})
```

### Example 26

```python
symmetricDifference (other)
```

### Example 27

```python
toCoordString (notation)
```

### Example 28

```python
touches (second_geometry)
```

### Example 29

```python
union (other)
```

### Example 30

```python
within (second_geometry, {relation})
```

### Example 31

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of coordinate pairs
feature_info = [[1, 2], [3, 5], [7, 3]]

# A list to hold the PointGeometry objects
features = []

# For each coordinate pair, create a PointGeometry object
for pt in feature_info:
    point = arcpy.Point(*pt)

    point_geometry = arcpy.PointGeometry(point, spatial_ref)
    features.append(point_geometry)

# Persist a copy of the PointGeometry objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/geometry/f.gdb/points")
```

### Example 32

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of coordinate pairs
feature_info = [[1, 2], [3, 5], [7, 3]]

# A list to hold the PointGeometry objects
features = []

# For each coordinate pair, create a PointGeometry object
for pt in feature_info:
    point = arcpy.Point(*pt)

    point_geometry = arcpy.PointGeometry(point, spatial_ref)
    features.append(point_geometry)

# Persist a copy of the PointGeometry objects using CopyFeatures
arcpy.CopyFeatures_management(features, "c:/geometry/f.gdb/points")
```

---

## Polygon

## Summary

A Polygon object is a closed shape defined by a connected sequence of x,y coordinate pairs.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inputs | The coordinate information used to create the object. The data type can be Point or Array objects. | Object |
| spatial_reference | The spatial reference of the new geometry.(The default value is None) | SpatialReference |
| has_z | Specifies whether the geometry will be z-enabled.(The default value is False) | Boolean |
| has_m | Specifies whether the geometry will be m-enabled.(The default value is False) | Boolean |
| has_id | Specifies whether the geometry will support point IDs.(The default value is False) | Boolean |
| other | The second geometry. If the geometry is a polygon, the distance is measured to the centroid of the polygon. | PointGeometry |
| method | The method used to measure distance. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| distance | The buffer distance.The buffer distance is in the same units as the geometry that is being buffered. A negative distance can only be specified against a polygon geometry. | Double |
| envelope | An Extent object used to define the clip extent. | Extent |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| cutter | The cutting polyline geometry. | PolyLine |
| method | The method of densification. DISTANCE—Creates a feature that is a piecewise linear approximation of the input.ANGLE—Creates a feature that is a piecewise linear approximation of the input. Vertices are introduced at points where the angle between tangents at those points is the provided angle.GEODESIC—Densifies and reshapes segments between input vertices so that the output segments follow the shortest ground path connecting input vertices. | String |
| distance | The maximum distance between vertices. The actual distance between vertices will usually be less than the maximum distance, as new vertices will be evenly distributed along the original segment. If using a type of DISTANCE or ANGLE, the distance is measured in the units of the geometry's spatial reference. If using a type of GEODESIC, the distance is measured in meters. | Double |
| deviation | Densify uses straight lines to approximate curves. You use deviation to control the accuracy of this approximation. The deviation is the maximum distance between the new segment and the original curve. The smaller its value, the more segments will be required to approximate the curve. If using a type of DISTANCE, the deviation is measured in the units of the geometry's spatial reference. If using a type of ANGLE, the deviation is measured in radians. If using a type of GEODESIC, the deviation is not used. | Double |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| max_offset | The maximum offset tolerance. | Double |
| method | The method used to measure area. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| units | The units in which the area will be calculated.Learn more about area unitsSquareKilometers—Square kilometersHectares—HectaresAres—AresSquareMeters—Square metersSquareDecimeters—Square decimetersSquareCentimeters—Square centimetersSquareMillimeters—Square millimetersSquareMilesInt—Square statute milesAcresInt—International acresSquareYardsInt—Square international yardsSquareFeetInt—Square international feetSquareInchesInt—Square international inchesSquareMilesUS—Square US survey milesAcresUS—Square US survey acresSquareYardsUS—Square US survey yardsSquareFeetUS—Square US survey feetSquareInchesUS—Square US survey inchesUnknown—Unknown | String |
| method | The method used to measure length. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| units | The units in which the length will be calculated.Learn more about linear unitsKilometers—KilometersMeters—MetersDecimeters—DecimetersMillimeters—MillimetersCentimeters—CentimetersNauticalMilesInt—International nautical milesMilesInt—Statute milesYardsInt—International yardsFeetInt—International feetInchesInt—International inchesNauticalMiles—US survey nautical milesMiles—US survey milesYards—US survey yardsFeet—US survey feetInches—US survey inchesDecimalDegrees—Decimal degreesPoints—PointsUnknown—Unknown | String |
| index | The index position of the geometry. | Integer |
| other | The second geometry. | Object |
| dimension | The topological dimension (shape type) of the resulting geometry. 1—A zero-dimensional geometry (point or multipoint). 2—A one-dimensional geometry (polyline). 4—A two-dimensional geometry (polygon). | Integer |
| dx | The distance the geometry will be moved along the x-axis. (The default value is 0.0) | Double |
| dy | The distance the geometry will be moved along the y-axis. (The default value is 0.0) | Double |
| dz | The distance the geometry will be moved along the z-axis. The geometry must be z-aware and have z-values.(The default value is 0.0) | Double |
| second_geometry | A second geometry. | Object |
| angle | The angle in degrees to the returned point. | Double |
| distance | The distance in the units of the geometry's spatial reference to the returned point. | Double |
| method | PLANAR measurements reflect the projection of geographic data onto the 2D surface (in other words, they will not take into account the curvature of the earth). GEODESIC, GREAT_ELLIPTIC, LOXODROME, or PRESERVE_SHAPE measurement types can be chosen as an alternative if desired. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is when you want to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—A loxodrome is not the shortest distance between two points but instead defines the line of constant bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system, and the 2D plane of that coordinate system will be used as the basis for the measurements.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| value | The distance along the line.The distance will be evaluated based on the geodesic parameter value. If the geodesic parameter value is False, the distance will be evaluated in meters. If the geodesic parameter value is True, the distance will be evaluated in the units of the feature's spatial reference.If the value exceeds the length of the line or precedes the length of the line (a negative value), the behaviour will depend on the geodesic parameter value as follows:If the geodesic parameter value is False, exceeding the length of the line will return the endpoint of the line, and a negative distance value will return the starting point of the line.If the geodesic parameter value is True, exceeding or preceding the length of the line will cause the method to fail. | Double |
| use_percentage | Specifies whether the distance is specified as a fixed unit of measure (False) or a ratio of the length of the line (True).For percentages, express the value parameter as a double from 0.0 (0 percent) to 1.0 (100 percent).Note:This parameter is only supported when the geodesic parameter value is False.(The default value is False) | Boolean |
| geodesic | Specifies whether the distance measure will be geodesic (True) or planar (False).(The default value is False) | Boolean |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object.The default origin, arcpy.Point(0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0)) | Point |
| rotation_angle | The angle, in radians, to rotate the geometry around its origin.The default rotation angle is 0.0 radians (no rotation).(The default value is 0.0) | Float |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object. The default origin, arcpy.Point(0.0, 0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0, 0.0)) | Point |
| sx | The factor that will be used to scale the geometry along the x-axis. (The default value is 1.0) | Double |
| sy | The factor that will be used to scale the geometry along the y-axis. (The default value is 1.0) | Double |
| sz | The factor that will be used to scale the geometry along the z-axis. The geometry must be z-aware and have z-values.(The default value is 1.0) | Double |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### angleAndDistanceTo (other, {method})

Returns a tuple of angle and distance to a point or polygon.

### boundary ()

Constructs the boundary of the geometry.

### buffer (distance)

Constructs a polygon at a specified distance from the geometry.

### clip (envelope)

Constructs the intersection of the geometry and the specified extent.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### convexHull ()

Constructs the geometry that is the minimal bounding polygon such that all outer angles are convex.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### cut (cutter)

Splits this geometry into a part left of the cutting polyline, and a part right of it. When a polyline or polygon is cut, it is split where it intersects the cutter polyline. Each piece is classified as left of or right of the cutter. This classification is based on the orientation of the cutter line. Parts of the target polyline that do not intersect the cutting polyline are returned as part of the right of result for that input polyline. If a geometry is not cut, the left geometry will be empty (None).

### densify (method, distance, {deviation})

Creates a geometry with added vertices.

### difference (other)

Constructs the geometry that is composed only of the region unique to the base geometry but not part of the other geometry. The following illustration shows the results when the red polygon is the source geometry.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### distanceTo (other)

Returns the minimum distance between two geometries. The distance is in the units of the geometry's spatial reference. If the geometries intersect, the minimum distance is 0.Both geometries must have the same projection.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### generalize (max_offset)

Creates a new simplified geometry using a specified maximum offset tolerance.

### getArea ({method}, {units})

Returns the area of the feature using a measurement method.

### getLength ({method}, {units})

Returns the length of the feature using a measurement method.

### getPart ({index})

Returns an Array object of Point objects for a particular part of the geometry if an index is specified. If an index is not specified, an Array object containing an Array of Point objects for each geometry part is returned. The getPart method is equivalent to indexing an object; that is, obj.getPart(0) is equivalent to obj[0].

### intersect (other, dimension)

Constructs a geometry that is the geometric intersection of the two input geometries. Different dimension values can be used to create different shape types. The intersection of two geometries of the same shape type is a geometry containing only the regions of overlap between the original geometries. For faster results, test if the two geometries are disjoint before calling intersect.

### move ({dx}, {dy}, {dz})

Moves a geometry by specified distances along the x-, y-, and z-axes to create a new geometry.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### pointFromAngleAndDistance (angle, distance, {method})

Returns a point at a given angle in degrees and distance in the units of the geometry's spatial reference using the specified measurement type.

### positionAlongLine (value, {use_percentage}, {geodesic})

Returns a point on a line at a specified distance from the beginning of the line.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### rotate ({origin}, {rotation_angle})

Rotates a geometry around a specified origin by the degrees given in radians.The rotation is applied relative to the origin, so that the geometry rotates around the origin. The position of the rotated geometry is significantly affected by the choice of origin.Rotate does not apply to the z-direction.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The location of the geometry will change, but the geometry will maintain relative positions to other geometries rotated in the same way. Positions will rotate around the origin.The origin is at the centroid of the geometry (the centroid is within or touching geometry)—The geometry will rotate (spin) in place around its centroid.The origin is on a vertex of the geometry—The geometry will rotate around the chosen vertex.

### scale ({origin}, {sx}, {sy}, {sz})

Scales a geometry from a specified origin by specified factors along the x-, y-, and z-axes to create a new geometry. The position of a transformed point (or vertex) is given by ( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )The transformation is applied relative to the origin, so that the origin remains stationary while the geometry expands or contracts around it. The position and the direction of the expansion or contraction for the resulting geometries is significantly affected by the origin.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The size and location of the geometry will change, but the geometry will maintain relative positions to other geometries scaled in the same way. Positions will expand away from or contract toward the origin point.The origin is at the centroid of the geometry (if the centroid is within or touching geometry)—The size of the geometry will change, but the geometry's location will remain anchored at the centroid. The geometry will grow or shrink in place around the centroid.The origin is on a vertex of the geometry—The size of the geometry will change, but the position of the geometry will remain anchored at the chosen vertex. The geometry will grow from or shrink toward the chosen vertex.

### symmetricDifference (other)

Constructs the geometry that is the union of two geometries minus the instersection of those geometries.The two input geometries must be the same shape type.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### union (other)

Constructs the geometry that is the set-theoretic union of the input geometries. The two geometries being unioned must be the same shape type.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
Polygon (inputs, {spatial_reference}, {has_z}, {has_m}, {has_id})
```

### Example 2

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 3

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 4

```python
angleAndDistanceTo (other, {method})
```

### Example 5

```python
boundary ()
```

### Example 6

```python
buffer (distance)
```

### Example 7

```python
clip (envelope)
```

### Example 8

```python
contains (second_geometry, {relation})
```

### Example 9

```python
convexHull ()
```

### Example 10

```python
crosses (second_geometry)
```

### Example 11

```python
cut (cutter)
```

### Example 12

```python
densify (method, distance, {deviation})
```

### Example 13

```python
difference (other)
```

### Example 14

```python
disjoint (second_geometry)
```

### Example 15

```python
distanceTo (other)
```

### Example 16

```python
equals (second_geometry)
```

### Example 17

```python
generalize (max_offset)
```

### Example 18

```python
getArea ({method}, {units})
```

### Example 19

```python
getLength ({method}, {units})
```

### Example 20

```python
getPart ({index})
```

### Example 21

```python
intersect (other, dimension)
```

### Example 22

```python
move ({dx}, {dy}, {dz})
```

### Example 23

```python
overlaps (second_geometry)
```

### Example 24

```python
pointFromAngleAndDistance (angle, distance, {method})
```

### Example 25

```python
positionAlongLine (value, {use_percentage}, {geodesic})
```

### Example 26

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 27

```python
rotate ({origin}, {rotation_angle})
```

### Example 28

```python
scale ({origin}, {sx}, {sy}, {sz})
```

### Example 29

```python
symmetricDifference (other)
```

### Example 30

```python
touches (second_geometry)
```

### Example 31

```python
union (other)
```

### Example 32

```python
within (second_geometry, {relation})
```

### Example 33

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will contain the Polygon objects
features = []

# Create Polygon objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
   
    # Add the first coordinate pair to the end to close polygon
    array.append(array[0])
    
    polygon = arcpy.Polygon(array, spatial_ref)
    features.append(polygon)

# Persist a copy of the Polygon objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/polygons.shp")
```

### Example 34

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will contain the Polygon objects
features = []

# Create Polygon objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
   
    # Add the first coordinate pair to the end to close polygon
    array.append(array[0])
    
    polygon = arcpy.Polygon(array, spatial_ref)
    features.append(polygon)

# Persist a copy of the Polygon objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/polygons.shp")
```

---

## Polyline

## Summary

A Polyline object is a shape defined by one or more paths, in which a path is a series of connected segments.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inputs | The coordinate information used to create the object. The data type can be Point or Array objects. | Object |
| spatial_reference | The spatial reference of the new geometry.(The default value is None) | SpatialReference |
| has_z | Specifies whether the geometry will be z-enabled.(The default value is False) | Boolean |
| has_m | Specifies whether the geometry will be m-enabled.(The default value is False) | Boolean |
| has_id | Specifies whether the geometry will support point IDs.(The default value is False) | Boolean |
| distance | The buffer distance.The buffer distance is in the same units as the geometry that is being buffered. A negative distance can only be specified against a polygon geometry. | Double |
| envelope | An Extent object used to define the clip extent. | Extent |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |
| second_geometry | A second geometry. | Object |
| cutter | The cutting polyline geometry. | PolyLine |
| method | The method of densification. DISTANCE—Creates a feature that is a piecewise linear approximation of the input.ANGLE—Creates a feature that is a piecewise linear approximation of the input. Vertices are introduced at points where the angle between tangents at those points is the provided angle.GEODESIC—Densifies and reshapes segments between input vertices so that the output segments follow the shortest ground path connecting input vertices. | String |
| distance | The maximum distance between vertices. The actual distance between vertices will usually be less than the maximum distance, as new vertices will be evenly distributed along the original segment. If using a type of DISTANCE or ANGLE, the distance is measured in the units of the geometry's spatial reference. If using a type of GEODESIC, the distance is measured in meters. | Double |
| deviation | Densify uses straight lines to approximate curves. You use deviation to control the accuracy of this approximation. The deviation is the maximum distance between the new segment and the original curve. The smaller its value, the more segments will be required to approximate the curve. If using a type of DISTANCE, the deviation is measured in the units of the geometry's spatial reference. If using a type of ANGLE, the deviation is measured in radians. If using a type of GEODESIC, the deviation is not used. | Double |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| max_offset | The maximum offset tolerance. | Double |
| method | The method used to measure length. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—The line follows a single compass bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system and the 2D plane of that coordinate system will be used as the basis for the measurements. Planar measurements reflect the projection of geographic data onto a 2D surface, and do not account for the curvature of the earth.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid, for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| units | The units in which the length will be calculated.Learn more about linear unitsKilometers—KilometersMeters—MetersDecimeters—DecimetersMillimeters—MillimetersCentimeters—CentimetersNauticalMilesInt—International nautical milesMilesInt—Statute milesYardsInt—International yardsFeetInt—International feetInchesInt—International inchesNauticalMiles—US survey nautical milesMiles—US survey milesYards—US survey yardsFeet—US survey feetInches—US survey inchesDecimalDegrees—Decimal degreesPoints—PointsUnknown—Unknown | String |
| index | The index position of the geometry. | Integer |
| other | The second geometry. | Object |
| dimension | The topological dimension (shape type) of the resulting geometry. 1—A zero-dimensional geometry (point or multipoint). 2—A one-dimensional geometry (polyline). 4—A two-dimensional geometry (polygon). | Integer |
| in_point | A point (PointGeometry or Point) that is used to measure from the start point of the polyline. If the point does not intersect the line, the function will use the nearest location on the line from the point. | PointGeometry |
| use_percentage | If False, the measure will be returned as a distance; if True, the measure will be returned as a percentage.(The default value is False) | Boolean |
| dx | The distance the geometry will be moved along the x-axis. (The default value is 0.0) | Double |
| dy | The distance the geometry will be moved along the y-axis. (The default value is 0.0) | Double |
| dz | The distance the geometry will be moved along the z-axis. The geometry must be z-aware and have z-values.(The default value is 0.0) | Double |
| second_geometry | A second geometry. | Object |
| angle | The angle in degrees to the returned point. | Double |
| distance | The distance in the units of the geometry's spatial reference to the returned point. | Double |
| method | PLANAR measurements reflect the projection of geographic data onto the 2D surface (in other words, they will not take into account the curvature of the earth). GEODESIC, GREAT_ELLIPTIC, LOXODROME, or PRESERVE_SHAPE measurement types can be chosen as an alternative if desired. GEODESIC—The shortest line between any two points on the earth's surface on a spheroid (ellipsoid). One use for a geodesic line is when you want to determine the shortest distance between two cities for an airplane's flight path. This is also known as a great circle line if based on a sphere rather than an ellipsoid.GREAT_ELLIPTIC—The line on a spheroid (ellipsoid) defined by the intersection at the surface by a plane that passes through the center of the spheroid and the start and endpoints of a segment. This is also known as a great circle when a sphere is used.LOXODROME—A loxodrome is not the shortest distance between two points but instead defines the line of constant bearing, or azimuth. Great circle routes are often broken into a series of loxodromes, which simplifies navigation. This is also known as a rhumb line.PLANAR—Planar measurements use 2D Cartesian mathematics to calculate lengths and areas. This option is only available when measuring in a projected coordinate system, and the 2D plane of that coordinate system will be used as the basis for the measurements.PRESERVE_SHAPE—This type calculates the area or length of the geometry on the surface of the earth ellipsoid for geometry defined in a projected or geographic coordinate system. This option preserves the shape of the geometry in its coordinate system.(The default value is GEODESIC) | String |
| value | The distance along the line.The distance will be evaluated based on the geodesic parameter value. If the geodesic parameter value is False, the distance will be evaluated in meters. If the geodesic parameter value is True, the distance will be evaluated in the units of the feature's spatial reference.If the value exceeds the length of the line or precedes the length of the line (a negative value), the behaviour will depend on the geodesic parameter value as follows:If the geodesic parameter value is False, exceeding the length of the line will return the endpoint of the line, and a negative distance value will return the starting point of the line.If the geodesic parameter value is True, exceeding or preceding the length of the line will cause the method to fail. | Double |
| use_percentage | Specifies whether the distance is specified as a fixed unit of measure (False) or a ratio of the length of the line (True).For percentages, express the value parameter as a double from 0.0 (0 percent) to 1.0 (100 percent).Note:This parameter is only supported when the geodesic parameter value is False.(The default value is False) | Boolean |
| geodesic | Specifies whether the distance measure will be geodesic (True) or planar (False).(The default value is False) | Boolean |
| spatial_reference | The spatial reference to which the geometry will be projected. The value can be a SpatialReference object or the coordinate system name. | SpatialReference |
| transformation_name | The geotransformation name.With ArcGIS Pro, if you do not specify a transformation, none will be applied. With ArcGIS Server, if you do not specify a transformation, a fallback transformation will be applied. | String |
| in_point | The input point. Both PointGeometry and Point objects are accepted. | PointGeometry |
| as_percentage | If False, the measure will be returned as a distance; if True, the measure will be returned as a percentage.(The default value is False) | Boolean |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object.The default origin, arcpy.Point(0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0)) | Point |
| rotation_angle | The angle, in radians, to rotate the geometry around its origin.The default rotation angle is 0.0 radians (no rotation).(The default value is 0.0) | Float |
| origin | The origin of the transformation. The argument can be either an arcpy.Point object or an arcpy.PointGeometry object. The default origin, arcpy.Point(0.0, 0.0, 0.0), will usually be located outside the target geometry.(The default value is arcpy.Point(0.0, 0.0, 0.0)) | Point |
| sx | The factor that will be used to scale the geometry along the x-axis. (The default value is 1.0) | Double |
| sy | The factor that will be used to scale the geometry along the y-axis. (The default value is 1.0) | Double |
| sz | The factor that will be used to scale the geometry along the z-axis. The geometry must be z-aware and have z-values.(The default value is 1.0) | Double |
| start_measure | The starting distance from the beginning of the line. | Double |
| end_measure | The ending distance from the beginning of the line. | Double |
| use_percentage | The start and end measures may be specified as fixed units or as a ratio.If True, start_measure and end_measure are used as a percentage; if False, start_measure and end_measure are used as a distance. For percentages, the measures should be expressed as a double from 0.0 (0 percent) to 1.0 (100 percent).(The default value is False) | Boolean |
| in_point | A point (PointGeometry or Point) to be snapped to the line. | PointGeometry |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| other | A second geometry. | Object |
| second_geometry | A second geometry. | Object |
| relation | The spatial relationship type.BOUNDARY— Relationship has no restrictions for interiors or boundaries.CLEMENTINI— Interiors of geometries must intersect. Specifying CLEMENTINI is equivalent to specifying None. This is the default.PROPER— Boundaries of geometries must not intersect.(The default value is None) | String |

## Methods

### boundary ()

Constructs the boundary of the geometry.

### buffer (distance)

Constructs a polygon at a specified distance from the geometry.

### clip (envelope)

Constructs the intersection of the geometry and the specified extent.

### contains (second_geometry, {relation})

Indicates if the base geometry contains the comparison geometry. contains is the opposite of within. Only True relationships are shown in this illustration.

### convexHull ()

Constructs the geometry that is the minimal bounding polygon such that all outer angles are convex.

### crosses (second_geometry)

Indicates if the two geometries intersect in a geometry of a lesser shape type. Two polylines cross if they share only points in common, at least one of which is not an endpoint. A polyline and an polygon cross if they share a polyline or a point (for vertical line) in common on the interior of the polygon which is not equivalent to the entire polyline. Only True relationships are shown in this illustration.

### cut (cutter)

Splits this geometry into a part left of the cutting polyline, and a part right of it. When a polyline or polygon is cut, it is split where it intersects the cutter polyline. Each piece is classified as left of or right of the cutter. This classification is based on the orientation of the cutter line. Parts of the target polyline that do not intersect the cutting polyline are returned as part of the right of result for that input polyline. If a geometry is not cut, the left geometry will be empty (None).

### densify (method, distance, {deviation})

Creates a geometry with added vertices.

### difference (other)

Constructs the geometry that is composed only of the region unique to the base geometry but not part of the other geometry. The following illustration shows the results when the red polygon is the source geometry.

### disjoint (second_geometry)

Indicates if the base and comparison geometries share no points in common. Two geometries intersect if disjoint returns False. Only True relationships are shown in this illustration.

### distanceTo (other)

Returns the minimum distance between two geometries. The distance is in the units of the geometry's spatial reference. If the geometries intersect, the minimum distance is 0.Both geometries must have the same projection.

### equals (second_geometry)

Indicates if the base and comparison geometries are of the same shape type and define the same set of points in the plane. This is a 2D comparison only; M and Z values are ignored.Only True relationships are shown in this illustration.

### generalize (max_offset)

Creates a new simplified geometry using a specified maximum offset tolerance.

### getLength ({method}, {units})

Returns the length of the feature using a measurement method.

### getPart ({index})

Returns an Array object of Point objects for a particular part of the geometry if an index is specified. If an index is not specified, an Array object containing an Array of Point objects for each geometry part is returned. The getPart method is equivalent to indexing an object; that is, obj.getPart(0) is equivalent to obj[0].

### intersect (other, dimension)

Constructs a geometry that is the geometric intersection of the two input geometries. Different dimension values can be used to create different shape types. The intersection of two geometries of the same shape type is a geometry containing only the regions of overlap between the original geometries. For faster results, test if the two geometries are disjoint before calling intersect.

### measureOnLine (in_point, {use_percentage})

Returns a measure from the start point of this line to the in_point.

### move ({dx}, {dy}, {dz})

Moves a geometry by specified distances along the x-, y-, and z-axes to create a new geometry.

### overlaps (second_geometry)

Indicates if the intersection of the two geometries has the same shape type as one of the input geometries and is not equivalent to either of the input geometries. Only True relationships are shown in this illustration.

### pointFromAngleAndDistance (angle, distance, {method})

Returns a point at a given angle in degrees and distance in the units of the geometry's spatial reference using the specified measurement type.

### positionAlongLine (value, {use_percentage}, {geodesic})

Returns a point on a line at a specified distance from the beginning of the line.

### projectAs (spatial_reference, {transformation_name})

Projects a geometry from one spatial reference to another.When the geometry object and the destination spatial reference do not have a common datum, specify a transformation_name parameter value. For more information, see Geographic datum transformations and ListTransformations.A vertical transformation will be performed when the following criteria are met: The geometry object has z-coordinates.The geometry object's spatial reference and the spatial_reference parameter values both have a vertical coordinate system.The transformation_name parameter value is a vertical transformation.When the transformation_name parameter value is a vertical transformation, and neither the geometry object nor the destination spatial reference have a vertical coordinate system, the function will fail with a ValueError exception.If either the geometry object or the spatial_reference parameter value have an unknown spatial reference, the output geometry's spatial reference will be that of the spatial_reference parameter value. Use of unknown spatial reference is not recommended for analysis.The projectAs method will not modify m-values, if present.

### queryPointAndDistance (in_point, {as_percentage})

Finds the point on the polyline nearest to the in_point and the distance between those points. It also returns information about the side of the line the point is on as well as the distance along the line where the nearest point occurs.

### reverseOrientation ()

Reverses the order of the vertices in the polyline.

### rotate ({origin}, {rotation_angle})

Rotates a geometry around a specified origin by the degrees given in radians.The rotation is applied relative to the origin, so that the geometry rotates around the origin. The position of the rotated geometry is significantly affected by the choice of origin.Rotate does not apply to the z-direction.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The location of the geometry will change, but the geometry will maintain relative positions to other geometries rotated in the same way. Positions will rotate around the origin.The origin is at the centroid of the geometry (the centroid is within or touching geometry)—The geometry will rotate (spin) in place around its centroid.The origin is on a vertex of the geometry—The geometry will rotate around the chosen vertex.

### scale ({origin}, {sx}, {sy}, {sz})

Scales a geometry from a specified origin by specified factors along the x-, y-, and z-axes to create a new geometry. The position of a transformed point (or vertex) is given by ( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )The transformation is applied relative to the origin, so that the origin remains stationary while the geometry expands or contracts around it. The position and the direction of the expansion or contraction for the resulting geometries is significantly affected by the origin.The following describes a few possible choices for the origin and its affect on the output:The origin is outside the geometry (not within or touching the geometry)—The size and location of the geometry will change, but the geometry will maintain relative positions to other geometries scaled in the same way. Positions will expand away from or contract toward the origin point.The origin is at the centroid of the geometry (if the centroid is within or touching geometry)—The size of the geometry will change, but the geometry's location will remain anchored at the centroid. The geometry will grow or shrink in place around the centroid.The origin is on a vertex of the geometry—The size of the geometry will change, but the position of the geometry will remain anchored at the chosen vertex. The geometry will grow from or shrink toward the chosen vertex.

### segmentAlongLine (start_measure, end_measure, {use_percentage})

Returns a Polyline between start and end measures. Similar to Polyline.positionAlongLine but will return a polyline segment between two points on the polyline instead of a single point.

### snapToLine (in_point)

Returns a new point based on in_point snapped to this geometry.

### symmetricDifference (other)

Constructs the geometry that is the union of two geometries minus the instersection of those geometries.The two input geometries must be the same shape type.

### touches (second_geometry)

Indicates if the boundaries of the geometries intersect. Two geometries touch when the intersection of the geometries is not empty, but the intersection of their interiors is empty. For example, a point touches a polyline only if the point is coincident with one of the polyline end points. Only True relationships are shown in this illustration.

### union (other)

Constructs the geometry that is the set-theoretic union of the input geometries. The two geometries being unioned must be the same shape type.

### within (second_geometry, {relation})

Indicates if the base geometry is within the comparison geometry. within is the opposite operator of contains. Only True relationships are shown in this illustration.The base geometry is within the comparison geometry if the base geometry is the intersection of the geometries and the intersection of their interiors is not empty. within is a Clementini operator, except in the case of an empty base geometry.

## Code Samples

### Example 1

```python
Polyline (inputs, {spatial_reference}, {has_z}, {has_m}, {has_id})
```

### Example 2

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 3

```python
( (x - origin_x) * scale_x + origin_x, (y - origin_y) * scale_y + origin_y, (z - origin_z) * scale_z + origin_z )
```

### Example 4

```python
boundary ()
```

### Example 5

```python
buffer (distance)
```

### Example 6

```python
clip (envelope)
```

### Example 7

```python
contains (second_geometry, {relation})
```

### Example 8

```python
convexHull ()
```

### Example 9

```python
crosses (second_geometry)
```

### Example 10

```python
cut (cutter)
```

### Example 11

```python
densify (method, distance, {deviation})
```

### Example 12

```python
difference (other)
```

### Example 13

```python
disjoint (second_geometry)
```

### Example 14

```python
distanceTo (other)
```

### Example 15

```python
equals (second_geometry)
```

### Example 16

```python
generalize (max_offset)
```

### Example 17

```python
getLength ({method}, {units})
```

### Example 18

```python
getPart ({index})
```

### Example 19

```python
intersect (other, dimension)
```

### Example 20

```python
measureOnLine (in_point, {use_percentage})
```

### Example 21

```python
move ({dx}, {dy}, {dz})
```

### Example 22

```python
overlaps (second_geometry)
```

### Example 23

```python
pointFromAngleAndDistance (angle, distance, {method})
```

### Example 24

```python
positionAlongLine (value, {use_percentage}, {geodesic})
```

### Example 25

```python
projectAs (spatial_reference, {transformation_name})
```

### Example 26

```python
queryPointAndDistance (in_point, {as_percentage})
```

### Example 27

```python
reverseOrientation ()
```

### Example 28

```python
rotate ({origin}, {rotation_angle})
```

### Example 29

```python
scale ({origin}, {sx}, {sy}, {sz})
```

### Example 30

```python
segmentAlongLine (start_measure, end_measure, {use_percentage})
```

### Example 31

```python
snapToLine (in_point)
```

### Example 32

```python
symmetricDifference (other)
```

### Example 33

```python
touches (second_geometry)
```

### Example 34

```python
union (other)
```

### Example 35

```python
within (second_geometry, {relation})
```

### Example 36

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will contain the Polyline objects
features = []

# Create Polyline objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
    polyline = arcpy.Polyline(array, spatial_ref)
    features.append(polyline)

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/polylines.shp")
```

### Example 37

```python
import arcpy

# Create a spatial reference from a wkid
spatial_ref = arcpy.SpatialReference(32145)

# A list of features and coordinate pairs
feature_info = [[[1, 2], [2, 4], [3, 7]],
                [[6, 8], [5, 7], [7, 2], [9, 5]]]

# A list that will contain the Polyline objects
features = []

# Create Polyline objects from an array of points
for feature in feature_info:
    array = arcpy.Array([arcpy.Point(*coords) for coords in feature])
    polyline = arcpy.Polyline(array, spatial_ref)
    features.append(polyline)

# Persist a copy of the Polyline objects using CopyFeatures
arcpy.management.CopyFeatures(features, "c:/geometry/polylines.shp")
```

---

## RandomNumberGenerator

## Summary

Determines the type and seed that will be used to create random numbers.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| string | The string representation of the object. A space-delimited string of the seed and random generator algorithm. For example, 0 ACM599.ACM599—ACM collected algorithm 599 MERSENNE_TWISTER—Mersenne Twister mt19937 STANDARD_C—Standard C Rand | String |

## Methods

### exportToString ()

Exports the object to its string representation.

### loadFromString (string)

Defines a RandomNumberGenerator object from a formatted string.

## Code Samples

### Example 1

```python
exportToString ()
```

### Example 2

```python
loadFromString (string)
```

---

## Raster

## Summary

Creates a raster object that can be used in Python or in a Map algebra expression. A raster object is a variable that references a raster dataset.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| inRaster[inRaster,...] | The input raster dataset or list of raster datasets.When multiple multidimensional raster datasets are provided, the files will be interpreted as a single multidimensional dataset, with variables and dimensions unioned together. If two files contain the same variable with the same dimension values, the slices in the output raster will come from the first multidimensional raster in the list.You can also specify a RasterInfo object as the input inRaster, which will create a new raster dataset on disk. In this case, the is_multidimensional input parameter will be ignored. | Raster |
| is_multidimensional | Determines whether the input raster will be treated as multidimensional. Specify True if the input is multidimensional and should be processed as multidimensional, where processing occurs for every slice in the dataset. Specify False if the input is not multidimensional, or if it is multidimensional and should not be processed as multidimensional.(The default value is False) | Boolean |
| variable | The name of the variable to which the dimension will be added. Only multidimensional rasters in Cloud Raster Format (.crf) are supported. | String |
| new_dimension_name | The name of the new dimension. | String |
| dimension_value | The value to assign to the new dimension. Only one value can be added, as more values (for example, multiple depths) would require new slices to be added to the dataset. To add more than one dimension value along with the new slices, use the addDimension method, then use the Merge function to merge existing data with the raster object. | Double |
| dimension_attributes | A Python dictionary that contains attribute information to be added to the new dimension, such as description or unit. For example, to add a unit attribute, use {"unit": "meters"}.(The default value is None) | Dictionary |
| mdRaster | The multidimensional raster containing the slices to be appended. This raster must have the same variables, with the same dimension names, as the target raster. The cell sizes, extents, and spatial reference systems must also match. The slices in this raster must be for dimension values that follow the dimension values of the slices in the target raster.If a variable has two dimensions, slices will be appended along one dimension. The other dimension must have the same number of slices as the dimension in the target raster. For example, if a salinity variable contains slices over time and depth dimensions, time slices can be appended to another salinity multidimensional raster but only if the same number of depth slices exist in both rasters. | Raster |
| locations[locations,...] | A list of x,y-coordinates. | List |
| spatial_reference | The spatial reference of the input locations. For example, the spatial reference can be specified using the following format: WGS_1984_UTM_Zone_11N.(The default value is None) | String |
| dem | The DEM to be used in the GSD computation.(The default value is None) | String |
| variable | The variable name for the multidimensional dataset. If a variable is not specified and the raster is multidimensional, the histogram of all variables will be calculated. | String |
| aoi[aoi,...] | The area of interest to calculate statistics for. This can be provided as Polygon object or a list of coordinates in the raster's spatial reference system in the form of [min_x, min_y, max_x, max_y]. | List |
| cellsize | The cell size to calculate statistics from. The raster will be resampled to the specified cell size before statistics are calculated. If no value is specified, the cell size of the raster will be used. | Double |
| variable | The variable name of the multidimensional dataset. If a variable is not provided and the raster is multidimensional, the histogram of all variables will be calculated. | String |
| aoi[aoi,...] | The area of interest that will be used to calculate statistics. This can be provided as a Polygon object or a list of coordinates in the raster's spatial reference system in the form of [min_x, min_y, max_x, max_y]. | List |
| cellsize | The cell size that will be used to calculate statistics. The raster will be resampled to the specified cell size before statistics are calculated. If no value is specified, the cell size of the raster will be used. | Double |
| width | The width of the output image in pixels. If a value is not specified, but the height is provided, the aspect ratio of the original raster will be maintained. If neither width nor height are specified, the width of the original raster dataset is used.(The default value is None) | Integer |
| height | The height of the output image in pixels. If a value is not specified, but the width is provided, the aspect ratio of the original raster will be maintained. If neither width nor height are specified, the height of the original raster dataset is used.(The default value is None) | Integer |
| format | The image format of the exported data. The supported formats include JPG, PNG, and PNG32.(The default value is PNG32) | String |
| extent | The extent or bounding box of the exported image. If a value is not specified, the extent of the raster dataset is used.(The default value is None) | Extent |
| spatial_reference | The spatial reference of the exported image. Supported options include the following:NoneSpatialReference data typeICS or ICS:<object_id>, where object_id selects the specific raster whose image coordinate system should be used.If a value is not specified, the spatial reference of the raster dataset is used.(The default value is None) | SpatialReference |
| mosaic_rule | Specifies how the input raster data should be mosaicked. This is applicable when the input raster dataset is a mosaic dataset. For information on how to format the mosaic rule, see Mosaic rule objects.(The default value is None) | Dictionary |
| stac_item | The URL of the STAC item or a pystac.Item object. The URL can be a static STAC item URL or a STAC API item URL, for example, "https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/tx_m_2609719_se_14_060_20201217". STAC items from the following STAC APIs are supported: https://planetarycomputer.microsoft.com/api/stac/v1—The following collections are supported: daymet-annual-pr, daymet-daily-hi, 3dep-seamless, 3dep-lidar-dsm, sentinel-1-rtc, gridmet, daymet-annual-na, daymet-monthly-na, daymet-annual-hi, daymet-monthly-hi, daymet-monthly-pr, hgb, cop-dem-glo-30, cop-dem-glo-90, terraclimate, gnatsgo-rasters, 3dep-lidar-hag, 3dep-lidar-intensity, 3dep-lidar-pointsourceid, mtbs, noaa-c-cap, alos-fnf-mosaic, 3dep-lidar-returns, mobi, landsat-c2-l2, chloris-biomass, daymet-daily-pr, 3dep-lidar-dtm-native, 3dep-lidar-classification, 3dep-lidar-dtm, gap, alos-dem, jrc-gsw, hrea, sentinel-2-l2a, daymet-daily-na, nrcan-landcover, ecmwf-forecast, noaa-mrms-qpe-24h-pass2, sentinel-1-grd, nasadem, io-lulc, landsat-c2-l1, drcog-lulc, chesapeake-lc-7, chesapeake-lc-13, chesapeake-lu, noaa-mrms-qpe-1h-pass1, noaa-mrms-qpe-1h-pass2, noaa-nclimgrid-monthly, usda-cdl, esa-cci-lc, esa-cci-lc-netcdf, noaa-climate-normals-netcdf, noaa-climate-normals-gridded, io-lulc-9-class, io-biodiversity, naip, noaa-cdr-sea-surface-temperature-whoi, noaa-cdr-ocean-heat-content, noaa-cdr-sea-surface-temperature-whoi-netcdf, sentinel-3-olci-wfr-l2-netcdf, noaa-cdr-ocean-heat-content-netcdf, sentinel-3-synergy-v10-l2-netcdf, sentinel-3-olci-lfr-l2-netcdf, sentinel-3-slstr-lst-l2-netcdf, sentinel-3-slstr-wst-l2-netcdf, sentinel-3-synergy-syn-l2-netcdf, sentinel-3-synergy-vgp-l2-netcdf, sentinel-3-synergy-vg1-l2-netcdf, and esa-worldcover, modis-64A1-061, modis-17A2H-061, modis-11A2-061, modis-17A2HGF-061, modis-17A3HGF-061, modis-09A1-061, modis-16A3GF-061, modis-21A2-061, modis-43A4-061, modis-09Q1-061, modis-14A1-061, modis-13Q1-061, modis-14A2-061, modis-15A2H-061, modis-11A1-061, modis-15A3H-061, modis-13A1-061, modis-10A2-061, modis-10A1-061, and aster-l1t. https://earth-search.aws.element84.com/v0—All collections are supported. https://earth-search.aws.element84.com/v1—All collections are supported. https://services.sentinel-hub.com/api/v1/catalog—All collections are supported. https://landsatlook.usgs.gov/stac-server—All collections are supported. https://geoportalstac.azurewebsites.net/stac—All collections are supported.https://gpt.geocloud.com/sentinel/stac —All collections are supported. STAC items from the following static catalogs (and their underlying child catalogs) are supported: https://capella-open-data.s3.us-west-2.amazonaws.com/stac/catalog.json–The GEO, GEC, and SICD product types are supported.https://maxar-opendata.s3.amazonaws.com/events/catalog.jsonhttps://storage.googleapis.com/cfo-public/catalog.jsonhttps://nz-imagery.s3-ap-southeast-2.amazonaws.com/catalog.json https://raw.githubusercontent.com/m-mohr/oam-example/main/catalog.json https://dop-stac.opengeodata.lgln.niedersachsen.de/catalog.json https://pta.data.lit.fmi.fi/stac/root.jsonhttps://datacloud.icgc.cat/stac-catalog/catalog.json https://bdc-sentinel-2.s3.us-west-2.amazonaws.com/catalog.json | String |
| request_params | The STAC item request parameters. These are the requests.get() method parameters and values in dictionary format. This parameter is honored when the stac_item parameter is a URL.{ "verify": False, "headers": {"Authorization": "Bearer access_token_string"} } | Dictionary |
| context | Additional properties that will be used to control the creation of the object.The dictionary supports the assetManagement and processingTemplate keys.The assetManagement key specifies how to manage and select assets for the RasterCollection object. If multiple assets are selected, the collection will be composed of multiband rasters from those selected asset types. The value can be a list, string, or dictionary.When working with individual assets, the asset key can be specified directly, for example, "B02" or {"key": "B02"}, or as a list. Each item in the list represents an asset key or identifier. Items in the list can be strings representing the asset key directly, or dictionaries providing additional details for locating the asset. If the value of the assetManagement key is a dictionary, the following keys are supported:key—A string representing the unique identifier for an asset, for example, "red".path—A list representing the hierarchy of keys to navigate to the asset, for example, ["alternate", "s3"].hrefKey—A string representing the key to access the asset URL, for example, "msft:https-url". If this value is different from the default href key, specify it here.Examples:{ "assetManagement": [ "red", "blue" ] }{ "assetManagement": { "key": "tasmin", "hrefKey": "msft:https-url" } }{ "assetManagement": [ {"key": "TRAD", "path": ["alternate", "s3"]}, {"key": "DRAD", "path": ["alternate", "s3"]} ] }The processingTemplate key specifies the processing template that will be applied to the raster. This is supported for selected collections and raster types. For more information about collections and raster types, see Satellite sensor raster types. The default for supported raster types is "Multiband"; otherwise, it's None.Example:{ "processingTemplate": "Surface Reflectance" } | Dictionary |
| band_index | The index number (1-based) of the band to be returned. | Integer |
| band_id_or_name | The name or index (1-based) of the band. | Integer |
| property_name | The name of the band property. | String |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the color map of the first variable will be returned. | String |
| variable_name | The variable name of the multidimensional raster dataset. | String |
| dimension_name | The dimension name of the multidimensional raster dataset. | String |
| variable_name | The variable name of the multidimensional raster dataset. | String |
| variable_name | The variable name of the multidimensional raster dataset. | String |
| dimension_name | The dimension name of the multidimensional raster dataset. | String |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the histogram of the first variable will be returned. | String |
| property_name | The property name of the raster dataset. | String |
| band_ids_or_names[band_ids_or_names,...] | The index number or names of the bands to return as Raster objects. If not specified, all bands will be extracted. (The default value is None) | String |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the statistics of the first variable will be returned. | String |
| variable_name | The variable name of the multidimensional raster dataset. | String |
| constantValue | The value to evaluate for in the raster. | Double |
| upper_left_corner | The coordinates relative to the origin_coordinate from which to extract the processing block to convert to an array. This should be formatted as a tuple with two values indicating the direction to move in the x- and y-direction, respectively. For example, a value of (2,0) indicates that the array should be extracted starting at the pixel that is two pixels away, in the x-direction, from the origin_coordinate.If no value is specified, (0,0) is used.(The default value is None) | tuple |
| origin_coordinate | The point of origin within the Raster object from which to extract the processing block to convert to an array. The coordinates must be in the units of the raster. If no value is specified, the origin of the raster will be used.(The default value is None) | Point |
| ncols | The number of columns from the upper_left_corner in the Raster object to convert to the NumPy array.If no value is specified, the number of columns of the raster will be used.(The default value is None) | Integer |
| nrows | The number of rows from the upper_left_corner in the Raster object to convert to the NumPy array.If no value is specified, the number of rows of the raster will be used.(The default value is None) | Integer |
| nodata_to_value | The pixel value to assign in the NumPy array for those pixels labeled as NoData in the Raster object.If no value is specified, the NoData value of the raster will be used. (The default value is None) | Variant |
| cell_size | The cell size to use in the NumPy array. This should be formatted as a tuple with two values indicating the cell size in the x- and y-direction, respectively, and units should match those used by the raster. For example, a value of (2, 1) indicates the output cell size should be 2 units in the x-direction and 1 unit in the y-direction. If the cell size is different from the data source, the cell values are resampled using bilinear interpolation.If no value is specified, the cell size of the raster will be used. (The default value is None) | tuple |
| variable_names[variable_names,...] | The variable name or a list of variable names to be removed from the multidimensional raster dataset. | String |
| current_band_name_or_index | The name or the index of the band to be renamed. The band indexing begins at 1. This argument can be a string or integer value. | String |
| new_band_name | The new band name. | String |
| current_variable_name | The current name of the variable in a multidimensional raster dataset. | String |
| new_variable_name | The new name of the variable in a multidimensional raster dataset. | String |
| name | The name to assign to the raster dataset on disk.This method supports persisting a multidimensional raster dataset as Cloud Raster Format (CRF). | String |
| color_map | The color map to apply to the raster. This can be a string indicating the name of the color map or color ramp to use, for example, NDVI or Yellow To Red, respectively. This can also be a Python dictionary with a custom color map or color ramp object—for example, a custom color map {'values': [0, 1, 2, 3, 4, 5], 'colors': ['#000000', '#DCFFDF', '#B8FFBE', '#85FF90', '#50FF60','#00AB10']} or a custom color ramp {"type": "algorithmic", "fromColor": [115, 76, 0, 255],"toColor": [255, 25, 86, 255], "algorithm": "esriHSVAlgorithm"}. | String |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the color map of the first variable will be set. | String |
| histogram_obj[histogram_obj,...] | A list of Python dictionaries containing histogram information to be set—for example, [{'size': 5, 'min': 19.0, 'max': 42.0, 'counts': [275, 17, 3065, 4, 22]}].If the raster is multiband, the histogram for each band will be set with each dictionary in the list. The first band will use the histogram in the first dictionary. The second band will use the histogram in the second dictionary, and so on.size—The number of bins in the histogrammin—The minimum pixel valuemax—The maximum pixel valuecounts—A list containing the number of pixels in each bin, in the order of bins | Dictionary |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the histogram will be set for the first variable. | String |
| property_name | The property name of the raster dataset. | String |
| property_value | The value to assign to the property. | String |
| statistics_obj[statistics_obj,...] | A list of Python dictionaries containing statistics and corresponding values to set. For example, [{'min': 10, 'max': 20}] sets the minimum and maximum pixel values. If the raster is multiband, the statistics for each band will be set with each dictionary in the list. The first band will use the statistics in the first dictionary. The second band will use the statistics in the second dictionary, and so on.min—The minimum pixel valuemax—The maximum pixel valuemean—The mean pixel valuemedian—The median pixel valuestandardDeviation—The standard deviation of the pixel valuescount—The total number of pixelsskipX—The horizontal skip factorskipY—The vertical skip factor | List |
| variable_name | The variable name of the multidimensional raster dataset. If a variable is not specified and the raster is multidimensional, the statistics of the first variable will be set. | String |
| variable_name | The variable name of the multidimensional raster dataset. | String |
| variable_attributes | A Python dictionary that contains attribute information to replace the current attribute information of the variable—for example, {'Description': 'Daily total precipitation', 'Unit': 'mm/day'}. | Dictionary |
| array | The input NumPy array.(The default value is None) | NumPyArray |
| upper_left_corner | The coordinates relative to the origin_coordinate from which to extract the processing block to convert to a raster. This should be formatted as a tuple with two values indicating the number of pixels to move along the x- and y- direction, respectively. For example, (2,0), indicates that the position from which the NumPy array will be written into the raster is 2 pixels away, in the x-direction, from the origin_coordinate. If no value is specified, (0,0) is used.(The default value is None) | tuple |
| origin_coordinate | A Point object defining the origin, from which the numpy array will be written into the Raster. The x- and y-values are in th units of the raster. If no value is specified, the upper left corner of the raster, will be used.If no value is specified, the origin of the raster will be used. This is the default.(The default value is None) | Point |
| value_to_nodata | A value in the NumPy array to be used as the NoData value in the Raster. The value can be an integer or a float. If no value is specified, the NoData value of the Raster will be used.The default value is None.(The default value is None) | Double |

## Methods

### addDimension (variable, new_dimension_name, dimension_value, {dimension_attributes})

Adds a new dimension to a variable in a multidimensional raster object so that the multidimensional raster can be compatible with other multidimensional datasets.

### appendSlices (mdRaster)

Appends the slices from another multidimensional raster.

### computeGSD (locations, spatial_reference, {dem})

Returns the ground sample distance (GSD) x- and y-values for an input image.

### computeHistograms ({variable}, {aoi}, {cellsize})

Returns the histogram of the raster. If the raster is multidimensional, it returns the histogram of a variable.

### computeStatistics ({variable}, {aoi}, {cellsize})

Returns the statistics of the raster. If the raster is multidimensional, it returns the statistics of a variable.

### exportImage ({width}, {height}, {format}, {extent}, {spatial_reference}, {mosaic_rule})

Exports the raster object as an IPython Image object to be used for visualization in Jupyter Notebook.

### fromSTACItem (stac_item, {request_params}, {context})

Creates a Raster object from a SpatioTemporal Asset Catalog (STAC) item.

### getAllBandProperties (band_index)

Returns the attribute information of all band properties of the band index.

### getBandProperty (band_id_or_name, property_name)

Returns the attribute information of a specified band property of the band index.

### getColormap ({variable_name})

Returns the color map of the raster. If the raster is multidimensional, returns the color map of a variable.

### getDimensionAttributes (variable_name, dimension_name)

Returns the attribute information of a dimension for a specific variable in a multidimensional raster dataset, for example, description, unit, and so on.

### getDimensionNames (variable_name)

Returns the dimension names associated with a variable in a multidimensional raster dataset.

### getDimensionValues (variable_name, dimension_name)

Returns the values of a dimension associated with a variable in a multidimensional raster dataset.

### getHistograms ({variable_name})

Returns the histograms of the raster. If the raster is multidimensional, it returns the histogram of a variable. If the raster is multiband, it returns the histogram of each band.

### getProperty (property_name)

Returns the value of the given property.

### getRasterBands ({band_ids_or_names})

Returns a Raster object for each band specified in a multiband raster dataset.

### getRasterInfo ()

Returns a RasterInfo object whose properties are initialized using the raster object properties.

### getStatistics ({variable_name})

Returns the statistics of the raster. If the raster is multidimensional, returns the statistics of a variable.

### getVariableAttributes (variable_name)

Returns the attribute information of a variable in a multidimensional raster dataset (for example, description, unit, and so on).

### isConstant (constantValue)

Identifies whether a raster only contains a constant value.

### read ({upper_left_corner}, {origin_coordinate}, {ncols}, {nrows}, {nodata_to_value}, {cell_size})

Reads a raster and converts the raster to a NumPy array.

### removeVariables (variable_names)

Removes a variable or a list of variables from a Cloud Raster Format (CRF) multidimensional raster dataset.

### renameBand (current_band_name_or_index, new_band_name)

Renames a band in a multiband raster dataset.

### renameVariable (current_variable_name, new_variable_name)

Renames a variable in a Cloud Raster Format (CRF) multidimensional raster dataset.

### save ({name})

Permanently saves the dataset referenced by the raster object.

### setColormap (color_map, {variable_name})

Sets the color map for the raster. If the raster is multidimensional, it sets the color map for a variable.

### setHistograms (histogram_obj, {variable_name})

Sets the histograms of the raster. If the raster is multidimensional, sets the histogram of a variable.

### setProperty (property_name, property_value)

Add a customized property to the raster dataset. If the property name exists, the existing property value will be overwritten.

### setStatistics (statistics_obj, {variable_name})

Sets the statistics for the raster. If the raster is multiband, it sets the statistics for each band. If the raster is multidimensional, it sets the statistics for a variable.

### setVariableAttributes (variable_name, variable_attributes)

Sets the attribute information of a variable in a multidimensional raster (for example, description, unit, and so on).

### write (array, {upper_left_corner}, {origin_coordinate}, {value_to_nodata})

Converts a three- or four-dimensional NumPy array to a raster.

## Code Samples

### Example 1

```python
# out_raster is a resultant raster object
out_raster = Raster("c:/data/inraster")
```

### Example 2

```python
# out_raster is a resultant raster object
out_raster = Raster("c:/data/inraster")
```

### Example 3

```python
out_raster = Slope("inelevation")
```

### Example 4

```python
out_raster = Slope("inelevation")
```

### Example 5

```python
# The plus operator (available with Spatial Analyst or Image Analyst) is
# used on the input rasters to create an output raster object
out_raster = Raster("input1") + Raster("input2") 
																																												
# The Python plus operator is used on numbers, creating a scalar variable
out_var = 4 + 7 

# When there is a combination of rasters with numbers, the Spatial Analyst
# operator is used, creating an output raster object
out_raster = Raster("input") + 10
```

### Example 6

```python
# The plus operator (available with Spatial Analyst or Image Analyst) is
# used on the input rasters to create an output raster object
out_raster = Raster("input1") + Raster("input2") 
																																												
# The Python plus operator is used on numbers, creating a scalar variable
out_var = 4 + 7 

# When there is a combination of rasters with numbers, the Spatial Analyst
# operator is used, creating an output raster object
out_raster = Raster("input") + 10
```

### Example 7

```python
in_raster = Raster('c:/data/inraster')

# Read the cell value at the second row and third column
v = in_raster[1, 2]
```

### Example 8

```python
in_raster = Raster('c:/data/inraster')

# Read the cell value at the second row and third column
v = in_raster[1, 2]
```

### Example 9

```python
in_raster = Raster('c:/data/inraster')
raster_info = in_raster.getRasterInfo()
new_raster = Raster(raster_info)  # Create a new raster

# Modify the cell value at the second row and third column
new_raster[1, 2] = 3
new_raster.save('c:/output/outraster1')
```

### Example 10

```python
in_raster = Raster('c:/data/inraster')
raster_info = in_raster.getRasterInfo()
new_raster = Raster(raster_info)  # Create a new raster

# Modify the cell value at the second row and third column
new_raster[1, 2] = 3
new_raster.save('c:/output/outraster1')
```

### Example 11

```python
Raster (inRaster, {is_multidimensional})
```

### Example 12

```python
addDimension (variable, new_dimension_name, dimension_value, {dimension_attributes})
```

### Example 13

```python
appendSlices (mdRaster)
```

### Example 14

```python
computeGSD (locations, spatial_reference, {dem})
```

### Example 15

```python
computeHistograms ({variable}, {aoi}, {cellsize})
```

### Example 16

```python
computeStatistics ({variable}, {aoi}, {cellsize})
```

### Example 17

```python
exportImage ({width}, {height}, {format}, {extent}, {spatial_reference}, {mosaic_rule})
```

### Example 18

```python
fromSTACItem (stac_item, {request_params}, {context})
```

### Example 19

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 20

```python
{
"verify": False,
"headers": {"Authorization": "Bearer access_token_string"}
}
```

### Example 21

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 22

```python
{
    "assetManagement": [
        "red",
        "blue"
    ]
}
```

### Example 23

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 24

```python
{
    "assetManagement": {
       "key": "tasmin",
       "hrefKey": "msft:https-url"
    }
}
```

### Example 25

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

### Example 26

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

### Example 27

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 28

```python
{
    "processingTemplate": "Surface Reflectance"
}
```

### Example 29

```python
getAllBandProperties (band_index)
```

### Example 30

```python
getBandProperty (band_id_or_name, property_name)
```

### Example 31

```python
getColormap ({variable_name})
```

### Example 32

```python
getDimensionAttributes (variable_name, dimension_name)
```

### Example 33

```python
getDimensionNames (variable_name)
```

### Example 34

```python
getDimensionValues (variable_name, dimension_name)
```

### Example 35

```python
getHistograms ({variable_name})
```

### Example 36

```python
getProperty (property_name)
```

### Example 37

```python
getRasterBands ({band_ids_or_names})
```

### Example 38

```python
getRasterInfo ()
```

### Example 39

```python
getStatistics ({variable_name})
```

### Example 40

```python
getVariableAttributes (variable_name)
```

### Example 41

```python
isConstant (constantValue)
```

### Example 42

```python
read ({upper_left_corner}, {origin_coordinate}, {ncols}, {nrows}, {nodata_to_value}, {cell_size})
```

### Example 43

```python
removeVariables (variable_names)
```

### Example 44

```python
renameBand (current_band_name_or_index, new_band_name)
```

### Example 45

```python
renameVariable (current_variable_name, new_variable_name)
```

### Example 46

```python
save ({name})
```

### Example 47

```python
setColormap (color_map, {variable_name})
```

### Example 48

```python
setHistograms (histogram_obj, {variable_name})
```

### Example 49

```python
setProperty (property_name, property_value)
```

### Example 50

```python
setStatistics (statistics_obj, {variable_name})
```

### Example 51

```python
setVariableAttributes (variable_name, variable_attributes)
```

### Example 52

```python
write (array, {upper_left_corner}, {origin_coordinate}, {value_to_nodata})
```

### Example 53

```python
import arcpy

my_raster = arcpy.Raster('elevation')
my_min = my_raster.minimum
my_max = my_raster.maximum
my_area = (my_raster.width * my_raster.height) * my_raster.meanCellWidth
```

### Example 54

```python
import arcpy

my_raster = arcpy.Raster('elevation')
my_min = my_raster.minimum
my_max = my_raster.maximum
my_area = (my_raster.width * my_raster.height) * my_raster.meanCellWidth
```

### Example 55

```python
import arcpy

#Create raster object
ras = arcpy.Raster(r"D:\Data\ndfd.crf")

#Define two raster function templates from the input CRF
ras.functions =[r"C:\weather.rft.xml", r"C:\heatindex.rft.xml"]

#Retrieve the first rft and process the raster object using the Apply function
rft = ras.functions
processed_raster = arcpy.ia.Apply(ras, json.dumps(rft[1]))
```

### Example 56

```python
import arcpy

#Create raster object
ras = arcpy.Raster(r"D:\Data\ndfd.crf")

#Define two raster function templates from the input CRF
ras.functions =[r"C:\weather.rft.xml", r"C:\heatindex.rft.xml"]

#Retrieve the first rft and process the raster object using the Apply function
rft = ras.functions
processed_raster = arcpy.ia.Apply(ras, json.dumps(rft[1]))
```

### Example 57

```python
import arcpy
from arcpy.sa import *

elev_raster = Raster('c:/data/elevation')
my_extent = elev_raster.extent
my_cellsize = (elev_raster.meanCellHeight + elev_raster.meanCellWidth) / 2
res01 = arcpy.CreateRandomRaster_management("", "error3", "UNIFORM 0.0 3.0",
                                            my_extent, my_cellsize)
elev_meters = (elev_raster + Raster(res01)) * 0.3048
elev_meters.save("c:/output/fgdb.gdb/elevM_err")
```

### Example 58

```python
import arcpy
from arcpy.sa import *

elev_raster = Raster('c:/data/elevation')
my_extent = elev_raster.extent
my_cellsize = (elev_raster.meanCellHeight + elev_raster.meanCellWidth) / 2
res01 = arcpy.CreateRandomRaster_management("", "error3", "UNIFORM 0.0 3.0",
                                            my_extent, my_cellsize)
elev_meters = (elev_raster + Raster(res01)) * 0.3048
elev_meters.save("c:/output/fgdb.gdb/elevM_err")
```

### Example 59

```python
import arcpy

## Load a netCDF file as a multidimensional raster
mdim_raster = Raster("Precip_2000_2018.nc", True)

## Check if it is multidimensional raster
is_multidimensional = mdim_raster.isMultidimensional

## Return the multidimensional information 
my_mdinfo = mdim_raster.mdinfo

## Return the list of variable names and their dimensions
my_variables = mdim_raster.variables

## Get the time dimension values for the precipitation variable
my_dimensionValues = mdim_raster.getDimensionValues("precip", "StdTime")

# save as a mdim crf
mdim_raster.save("c:/output/Precip_18_yr.crf")
```

### Example 60

```python
import arcpy

## Load a netCDF file as a multidimensional raster
mdim_raster = Raster("Precip_2000_2018.nc", True)

## Check if it is multidimensional raster
is_multidimensional = mdim_raster.isMultidimensional

## Return the multidimensional information 
my_mdinfo = mdim_raster.mdinfo

## Return the list of variable names and their dimensions
my_variables = mdim_raster.variables

## Get the time dimension values for the precipitation variable
my_dimensionValues = mdim_raster.getDimensionValues("precip", "StdTime")

# save as a mdim crf
mdim_raster.save("c:/output/Precip_18_yr.crf")
```

### Example 61

```python
import arcpy

#Load a netCDF file as a multidimensional raster
mdim_raster = Raster("Precip_2000_2018.nc", True)

#Create an array that contains the corner coordinates for a bounding box
array = arcpy.Array([arcpy.Point(-119.8082436, 38.2177764), arcpy.Point(-119.7794812, 38.2038911), arcpy.Point(-119.7432803, 38.2232313), arcpy.Point(-119.7928706, 38.2425716)])

#Specify a spatial reference
spatial_reference = arcpy.SpatialReference(4326)

#Create a polygon object that will be used to specify the aoi
aoi= arcpy.Polygon(array, spatial_reference)

#return the statistics 
stats = mdim_raster.computeStatistics('precip', aoi, cellsize = 463)
```

### Example 62

```python
import arcpy

#Load a netCDF file as a multidimensional raster
mdim_raster = Raster("Precip_2000_2018.nc", True)

#Create an array that contains the corner coordinates for a bounding box
array = arcpy.Array([arcpy.Point(-119.8082436, 38.2177764), arcpy.Point(-119.7794812, 38.2038911), arcpy.Point(-119.7432803, 38.2232313), arcpy.Point(-119.7928706, 38.2425716)])

#Specify a spatial reference
spatial_reference = arcpy.SpatialReference(4326)

#Create a polygon object that will be used to specify the aoi
aoi= arcpy.Polygon(array, spatial_reference)

#return the statistics 
stats = mdim_raster.computeStatistics('precip', aoi, cellsize = 463)
```

### Example 63

```python
from arcpy.ia import *
from arcpy import AIO

# 1) Creates a raster object from NAIP data accesible through Planetary Computer STAC API

naip_ras = Raster.fromSTACItem(
stac_item="https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/tx_m_2609719_se_14_060_20201217"
)

# Apply grayscale raster function to the raster object
gray_ras = Grayscale(naip_ras)

# 2) Creates a raster object from Sentinel-2 L2A data accesible through Earth Search STAC API

sentinel_2_ras = Raster.fromSTACItem(
     stac_item="https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_45XWD_20230328_0_L2A"
)

# Retrieve raster object properties
cols, rows = sentinel_2_ras.width, sentinel_2_ras.height

# 3) Creates a raster object from Landsat C2-L2 data accesible through USGS

# LandsatLook STAC API (with custom processing template selection) - Requires acs (AIO object).

landsat_acs = AIO(r"C:\acs_files\s3_landsat_c2.acs")

qa_landsat_ras = Raster.fromSTACItem(
        stac_item="https://landsatlook.usgs.gov/stac-server/collections/landsat-c2l2-sr/items/LC09_L2SP_088084_20230729_20230801_02_T2_SR",
        context={
	"processingTemplate": "QA",
	},
)

# 4) Creates a raster object from CBERS data accesible through
# CBERS/AMAZONIA on AWS (static) STAC (with custom asset selection) - Requires acs (AIO object).

cbers_acs = AIO(r"C:\acs_files\s3_cbers_pds.acs")

cbers_ras = Raster.fromSTACItem(
        stac_item="https://br-eo-stac-1-0-0.s3.amazonaws.com/CBERS4/MUX/043/076/CBERS_4_MUX_20230630_043_076_L2.json",
        context={"assetManagement": ["B7", "B6", "B5"]},
)
```

### Example 64

```python
from arcpy.ia import *
from arcpy import AIO

# 1) Creates a raster object from NAIP data accesible through Planetary Computer STAC API

naip_ras = Raster.fromSTACItem(
stac_item="https://planetarycomputer.microsoft.com/api/stac/v1/collections/naip/items/tx_m_2609719_se_14_060_20201217"
)

# Apply grayscale raster function to the raster object
gray_ras = Grayscale(naip_ras)

# 2) Creates a raster object from Sentinel-2 L2A data accesible through Earth Search STAC API

sentinel_2_ras = Raster.fromSTACItem(
     stac_item="https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_45XWD_20230328_0_L2A"
)

# Retrieve raster object properties
cols, rows = sentinel_2_ras.width, sentinel_2_ras.height

# 3) Creates a raster object from Landsat C2-L2 data accesible through USGS

# LandsatLook STAC API (with custom processing template selection) - Requires acs (AIO object).

landsat_acs = AIO(r"C:\acs_files\s3_landsat_c2.acs")

qa_landsat_ras = Raster.fromSTACItem(
        stac_item="https://landsatlook.usgs.gov/stac-server/collections/landsat-c2l2-sr/items/LC09_L2SP_088084_20230729_20230801_02_T2_SR",
        context={
	"processingTemplate": "QA",
	},
)

# 4) Creates a raster object from CBERS data accesible through
# CBERS/AMAZONIA on AWS (static) STAC (with custom asset selection) - Requires acs (AIO object).

cbers_acs = AIO(r"C:\acs_files\s3_cbers_pds.acs")

cbers_ras = Raster.fromSTACItem(
        stac_item="https://br-eo-stac-1-0-0.s3.amazonaws.com/CBERS4/MUX/043/076/CBERS_4_MUX_20230630_043_076_L2.json",
        context={"assetManagement": ["B7", "B6", "B5"]},
)
```

---

## RasterInfo

## Summary

Defines a RasterInfo object that describes a set of raster properties to facilitate the creation of a raster dataset using the Raster class.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| json | The input JSON string that will be loaded. An input JSON string example:{ "extent": { "xmin": 1708552.6584149038, "ymin": 40759.4130924825367, "xmax": 1710125.89027346508, "ymax": 42023.4400903051792, "spatialReference": { "wkid": 102663, "latestWkid": 3759 } }, "geodataXform": { "spatialReference": { "wkid": 102663, "latestWkid": 3759 }, "type": "IdentityXform" }, "blockWidth": 128, "blockHeight": 128, "bandCount": 1, "pixelType": "F32", "noData": 3.402823E+38, "pixelSizeX": 10, "pixelSizeY": 10 } | String |
| band_count | The band count. | Integer |
| block_height | The block height. | Integer |
| block_width | The block width. | Integer |
| cell_size | The cell size. The first element of the tuple represents the cell width and the second element represents the cell height. | tuple |
| extent | The extent. | Extent |
| nodata_values | A number or a tuple that specifies the NoData values.If a number is specified, it will be used as the NoData value for all bands. If a tuple is specified, each element in the tuple will be interpreted as the NoData value for the corresponding band. The number of elements in the tuple must match the band count. | Variant |
| pixel_type | The pixel type, such as S32 or F32.U1—Unsigned 1-bit integerU2—Unsigned 2-bit integerU4—Unsigned 4-bit integerS8—Signed 8-bit integerU8—Unsigned 8-bit integerS16— Signed 16-bit integerU16— Unsigned 16-bit integerS32—Signed 32-bit integerU32—Unsigned 32-bit integerF32—32-bit floating pointF64—64-bit double | String |
| spatial_reference | The spatial reference. | SpatialReference |

## Methods

### fromJSONString (json)

Loads properties from a JSON string.

### getBandCount ()

Returns the band count property of the RasterInfo object.

### getBlockHeight ()

Returns the block height property of the RasterInfo object.

### getBlockWidth ()

Returns the block width property of the RasterInfo object.

### getCellSize ()

Returns the cell size property of the RasterInfo object.

### getExtent ()

Returns the extent property of the RasterInfo object.

### getNoDataValues ()

Returns the NoData value property of the RasterInfo object.

### getPixelType ()

Returns the pixel type property of the RasterInfo object.

### getSpatialReference ()

Returns the spatial reference property of the RasterInfo object.

### setBandCount (band_count)

Sets the band count property.

### setBlockHeight (block_height)

Sets the block height property.

### setBlockWidth (block_width)

Sets the block width property.

### setCellSize (cell_size)

Sets the cell size property.

### setExtent (extent)

Sets the extent property.

### setNoDataValues (nodata_values)

Sets the NoData values property.

### setPixelType (pixel_type)

Sets the pixel type property.

### setSpatialReference (spatial_reference)

Sets the spatial reference property.

### toJSONString ()

Returns a JSON representation of the RasterInfo object.

## Code Samples

### Example 1

```python
RasterInfo ()
```

### Example 2

```python
fromJSONString (json)
```

### Example 3

```python
{
	"extent": {
		"xmin": 1708552.6584149038,
		"ymin": 40759.4130924825367,
		"xmax": 1710125.89027346508,
		"ymax": 42023.4400903051792,
		"spatialReference": {
			"wkid": 102663,
			"latestWkid": 3759
		}
	},
	"geodataXform": {
		"spatialReference": {
			"wkid": 102663,
			"latestWkid": 3759
		},
		"type": "IdentityXform"
	},
	"blockWidth": 128,
	"blockHeight": 128,
	"bandCount": 1,
	"pixelType": "F32",
	"noData": 3.402823E+38,
	"pixelSizeX": 10,
	"pixelSizeY": 10
}
```

### Example 4

```python
{
	"extent": {
		"xmin": 1708552.6584149038,
		"ymin": 40759.4130924825367,
		"xmax": 1710125.89027346508,
		"ymax": 42023.4400903051792,
		"spatialReference": {
			"wkid": 102663,
			"latestWkid": 3759
		}
	},
	"geodataXform": {
		"spatialReference": {
			"wkid": 102663,
			"latestWkid": 3759
		},
		"type": "IdentityXform"
	},
	"blockWidth": 128,
	"blockHeight": 128,
	"bandCount": 1,
	"pixelType": "F32",
	"noData": 3.402823E+38,
	"pixelSizeX": 10,
	"pixelSizeY": 10
}
```

### Example 5

```python
getBandCount ()
```

### Example 6

```python
getBlockHeight ()
```

### Example 7

```python
getBlockWidth ()
```

### Example 8

```python
getCellSize ()
```

### Example 9

```python
getExtent ()
```

### Example 10

```python
getNoDataValues ()
```

### Example 11

```python
getPixelType ()
```

### Example 12

```python
getSpatialReference ()
```

### Example 13

```python
setBandCount (band_count)
```

### Example 14

```python
setBlockHeight (block_height)
```

### Example 15

```python
setBlockWidth (block_width)
```

### Example 16

```python
setCellSize (cell_size)
```

### Example 17

```python
setExtent (extent)
```

### Example 18

```python
setNoDataValues (nodata_values)
```

### Example 19

```python
setPixelType (pixel_type)
```

### Example 20

```python
setSpatialReference (spatial_reference)
```

### Example 21

```python
toJSONString ()
```

### Example 22

```python
# Import system modules
import arcpy

# Create raster info object
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
rasInfo.setPixelType("S16")

# Create a new raster dataset using the raster info object
outRas = arcpy.Raster(rasInfo)
outRas.save("C:/arcpyExamples/outputs/newras01.tif")
```

### Example 23

```python
# Import system modules
import arcpy

# Create raster info object
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
rasInfo.setPixelType("S16")

# Create a new raster dataset using the raster info object
outRas = arcpy.Raster(rasInfo)
outRas.save("C:/arcpyExamples/outputs/newras01.tif")
```

### Example 24

```python
# Import system modules
import arcpy

# Create a raster object
inRaster = arcpy.Raster("C:/arcpyExamples/inputs/elevation.tif")

# Get the raster info object
rasInfo = inRaster.getRasterInfo()

# Change some properties for the raster info object
# Change the cell size property
rasInfo.setCellSize((45, 45))
# Change the pixel type property
rasInfo.setPixelType("S32")

# Create a new raster dataset using the raster info object
outRas = arcpy.Raster(rasInfo)
outRas.save("C:/arcpyExamples/outputs/newras02.tif")
```

### Example 25

```python
# Import system modules
import arcpy

# Create a raster object
inRaster = arcpy.Raster("C:/arcpyExamples/inputs/elevation.tif")

# Get the raster info object
rasInfo = inRaster.getRasterInfo()

# Change some properties for the raster info object
# Change the cell size property
rasInfo.setCellSize((45, 45))
# Change the pixel type property
rasInfo.setPixelType("S32")

# Create a new raster dataset using the raster info object
outRas = arcpy.Raster(rasInfo)
outRas.save("C:/arcpyExamples/outputs/newras02.tif")
```

---

## RecordSet

## Summary

RecordSet objects are a lightweight representation of a table. They are a data element that contains not only schema, but also the data. The RecordSet object is also how tables are sent and received from the server.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| table_path | The table to load into the RecordSet object. | String |
| where_clause | An SQL expression used to select a subset of records.For more information about SQL syntax, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| table_path | The table to load into the RecordSet object. | String |
| where_clause | An SQL expression used to select a subset of records.For more information about SQL syntax, see SQL reference for query expressions used in ArcGIS.(The default value is None) | String |
| table_path | The output table to be created. | String |

## Methods

### load ({table_path}, {where_clause})

Loads a table into the RecordSet object.

### save (table_path)

Export to a table.

## Code Samples

### Example 1

```python
RecordSet ({table_path}, {where_clause})
```

### Example 2

```python
load ({table_path}, {where_clause})
```

### Example 3

```python
save (table_path)
```

### Example 4

```python
import arcpy

# Add a custom server toolbox
arcpy.ImportToolbox("http://myserver/arcgis/services;Geocode")

# Get recordset from server tool's first parameter to use as schema
in_recordset = arcpy.GetParameterValue("GeocodeAddress", 0)
```

### Example 5

```python
import arcpy

# Add a custom server toolbox
arcpy.ImportToolbox("http://myserver/arcgis/services;Geocode")

# Get recordset from server tool's first parameter to use as schema
in_recordset = arcpy.GetParameterValue("GeocodeAddress", 0)
```

### Example 6

```python
import arcpy

# Set data
in_dataset = "https://maps.my.org/arcgis/rest/services/Tables/MapServer/0"
query = "Country_Code: 'IT'"

# Create RecordSet with query
record_set = arcpy.RecordSet(in_dataset, query)
```

### Example 7

```python
import arcpy

# Set data
in_dataset = "https://maps.my.org/arcgis/rest/services/Tables/MapServer/0"
query = "Country_Code: 'IT'"

# Create RecordSet with query
record_set = arcpy.RecordSet(in_dataset, query)
```

### Example 8

```python
import arcpy

# Set data
data_json = '''{
 "objectIdFieldName": "objectid",
 "globalIdFieldName": "globalid",
 "fields": [
  {
   "name": "objectid",
   "alias": "OBJECTID",
   "type": "esriFieldTypeOID"
  },
  {
   "name": "requestid",
   "alias": "Service Request ID",
   "type": "esriFieldTypeString",
   "length": 25
  },
  {
   "name": "requesttype",
   "alias": "Problem",
   "type": "esriFieldTypeString",
   "length": 100
  },
  {
   "name": "comments",
   "alias": "Comments",
   "type": "esriFieldTypeString",
   "length": 255
  }
 ],
 "features": [
  {
   "attributes": {
    "objectid": 246362,
    "requestid": "1",
    "requesttype": "Sidewalk Damage",
    "comments": "Pothole"
   }
  },
  {
   "attributes": {
    "objectid": 246382,
    "requestid": "2",
    "requesttype": "Pothole",
    "comments": "Jhh"
   }
  }
 ]
}'''

# Create FeatureSet from Esri JSON
feature_set = arcpy.RecordSet(data_json)
```

### Example 9

```python
import arcpy

# Set data
data_json = '''{
 "objectIdFieldName": "objectid",
 "globalIdFieldName": "globalid",
 "fields": [
  {
   "name": "objectid",
   "alias": "OBJECTID",
   "type": "esriFieldTypeOID"
  },
  {
   "name": "requestid",
   "alias": "Service Request ID",
   "type": "esriFieldTypeString",
   "length": 25
  },
  {
   "name": "requesttype",
   "alias": "Problem",
   "type": "esriFieldTypeString",
   "length": 100
  },
  {
   "name": "comments",
   "alias": "Comments",
   "type": "esriFieldTypeString",
   "length": 255
  }
 ],
 "features": [
  {
   "attributes": {
    "objectid": 246362,
    "requestid": "1",
    "requesttype": "Sidewalk Damage",
    "comments": "Pothole"
   }
  },
  {
   "attributes": {
    "objectid": 246382,
    "requestid": "2",
    "requesttype": "Pothole",
    "comments": "Jhh"
   }
  }
 ]
}'''

# Create FeatureSet from Esri JSON
feature_set = arcpy.RecordSet(data_json)
```

---

## Result

## Summary

The result of a geoprocessing tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| toolname | The name of the executed tool. | String |
| resultID | The job ID. | Integer |
| index | The index position of the input as an integer, or the parameter name. | Variant |
| parameter_list | The parameters on which the map service image will be based. | Integer |
| height | The height of the image. | Double |
| width | The width of the image. | Double |
| resolution | The resolution of the image. | Double |
| index | The index position of the message. | Integer |
| severity | The type of messages to be returned.0—Informative, warning, and error messages are returned.1—Only warning messages are returned.2—Only error messages are returned.Not specifying a severity level will return all types of messages.(The default value is 0) | Integer |
| index | The index position of the output as an integer, or the parameter name. | Variant |
| index | The message index position. | Integer |
| rlt_file | Full path to the output result file (.rlt). | String |

## Methods

### cancel ()

Cancels an associated job

### getAllMessages ()

Returns the message types, return codes, and message strings.

### getInput (index)

Returns a given input, either as a string or a RecordSet object.

### getMapImageURL ({parameter_list}, {height}, {width}, {resolution})

Returns a map service image for a given output, if one exists.

### getMessage (index)

Returns a specific message by index position.

### getMessages ({severity})

Returns the geoprocessing tool messages.

### getOutput (index)

Returns a given output, either as a RecordSet object or a string.If the output of the tool, such as Make Feature Layer, is a layer, getOutput will return a Layer object.

### getSeverity (index)

Returns the severity of a specific message.

### saveToFile (rlt_file)

Saves the result to a result file.Note:saveToFile is not supported in ArcGIS Pro; use the Package Result tool instead.

## Code Samples

### Example 1

```python
Result  (toolname, resultID)
```

### Example 2

```python
getAllMessages ()
```

### Example 3

```python
getInput (index)
```

### Example 4

```python
getMapImageURL ({parameter_list}, {height}, {width}, {resolution})
```

### Example 5

```python
getMessage (index)
```

### Example 6

```python
getMessages ({severity})
```

### Example 7

```python
getOutput (index)
```

### Example 8

```python
getSeverity (index)
```

### Example 9

```python
saveToFile (rlt_file)
```

### Example 10

```python
import arcpy

in_table = arcpy.GetParameterAsText(0)
result = arcpy.management.GetCount(in_table)
print(result[0])
```

### Example 11

```python
import arcpy

in_table = arcpy.GetParameterAsText(0)
result = arcpy.management.GetCount(in_table)
print(result[0])
```

### Example 12

```python
import arcpy

in_table = arcpy.GetParameterAsText(0)
result = arcpy.management.GetCount(in_table)
print(result["row_count"])
```

### Example 13

```python
import arcpy

in_table = arcpy.GetParameterAsText(0)
result = arcpy.management.GetCount(in_table)
print(result["row_count"])
```

### Example 14

```python
import time
import arcpy

# Add a toolbox from a server
arcpy.ImportToolbox("http://myserver/arcgis/services;GP/BufferByVal",
                    "servertools")

# Use GetParameterValue to get a featureset object with the default
# schema of the first parameter of the tool 'bufferpoints'
in_featureset = arcpy.GetParameterValue("bufferpoints", 0)

# Load a shapefile into the featureset
in_featureset.load("C:/Data/roads.shp")

# Run a server tool named BufferPoints with featureset created above
result = arcpy.server.BufferPoints(in_featureset, "500 feet")

# Check the status of the result object every 0.2 seconds
#    until it has a value of 4 (succeeded) or greater
while result.status < 4:
    time.sleep(0.2)

# Get the output FeatureSet back from the server and save to a local geodatabase
out_featureset = result.getOutput(0)
out_featureset.save("c:/temp/base.gdb/roads_buffer")
```

### Example 15

```python
import time
import arcpy

# Add a toolbox from a server
arcpy.ImportToolbox("http://myserver/arcgis/services;GP/BufferByVal",
                    "servertools")

# Use GetParameterValue to get a featureset object with the default
# schema of the first parameter of the tool 'bufferpoints'
in_featureset = arcpy.GetParameterValue("bufferpoints", 0)

# Load a shapefile into the featureset
in_featureset.load("C:/Data/roads.shp")

# Run a server tool named BufferPoints with featureset created above
result = arcpy.server.BufferPoints(in_featureset, "500 feet")

# Check the status of the result object every 0.2 seconds
#    until it has a value of 4 (succeeded) or greater
while result.status < 4:
    time.sleep(0.2)

# Get the output FeatureSet back from the server and save to a local geodatabase
out_featureset = result.getOutput(0)
out_featureset.save("c:/temp/base.gdb/roads_buffer")
```

### Example 16

```python
import arcpy

# Add the toolbox from the server
arcpy.ImportToolbox("http://myserver/arcgis/services;GP/BufferByVal")

# Recreate the original output using the tool name and result id
result_id = 'jfea96e13ba7b443cb04ba47c19899a1b'
result = arcpy.Result("BufferPoints", result_id)
```

### Example 17

```python
import arcpy

# Add the toolbox from the server
arcpy.ImportToolbox("http://myserver/arcgis/services;GP/BufferByVal")

# Recreate the original output using the tool name and result id
result_id = 'jfea96e13ba7b443cb04ba47c19899a1b'
result = arcpy.Result("BufferPoints", result_id)
```

---

## Row

## Summary

The Row object represents the row of a table. The Row object is returned from InsertCursor, SearchCursor, and UpdateCursor.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| field_name | The field from which the value will be accessed. | String |
| field_name | The field to be queried. | None |
| field_name | The field that will be set to null. | String |
| field_name | The field that will be set to the new value. | String |
| object | The value used to set the field value. | Object |

## Methods

### getValue (field_name)

Returns the field value.

### isNull (field_name)

Is the field value null.

### setNull (field_name)

Sets the field value to null.

### setValue (field_name, object)

Sets the field value.

## Code Samples

### Example 1

```python
getValue (field_name)
```

### Example 2

```python
isNull (field_name)
```

### Example 3

```python
setNull (field_name)
```

### Example 4

```python
setValue (field_name, object)
```

### Example 5

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/data"

# Use row object to get and set field values
cursor = arcpy.UpdateCursor("Addresses.dbf", '"STATENAME" = \'Ariz\'' )

# Iterate through rows and update values
for row in cursor:
    row.setValue("STATENAME", "Arizona")
    cursor.updateRow(row)

del cursor, row
```

### Example 6

```python
import arcpy

# Set the workspace
arcpy.env.workspace = "c:/data"

# Use row object to get and set field values
cursor = arcpy.UpdateCursor("Addresses.dbf", '"STATENAME" = \'Ariz\'' )

# Iterate through rows and update values
for row in cursor:
    row.setValue("STATENAME", "Arizona")
    cursor.updateRow(row)

del cursor, row
```

---

## Schema

## Summary

The schema of a dataset.

## Code Samples

### Example 1

```python
def initializeParameters(self):
    # Set the dependencies for the output and its schema properties. The two 
    # input parameters are feature classes.
    self.params[2].parameterDependencies = [0, 1]

    # Feature type, geometry type, and fields all come from the first dependency 
    # (parameter 0), the input features.
    self.params[2].schema.featureTypeRule = "FirstDependency"
    self.params[2].schema.geometryTypeRule = "FirstDependency"
    self.params[2].schema.fieldsRule = "FirstDependency"

    # The extent of the output is the intersection of the input features and 
    # the clip features (parameter 1).
    self.params[2].schema.extentRule = "Intersection"

    return
```

### Example 2

```python
def initializeParameters(self):
    # Set the dependencies for the output and its schema properties. The two 
    # input parameters are feature classes.
    self.params[2].parameterDependencies = [0, 1]

    # Feature type, geometry type, and fields all come from the first dependency 
    # (parameter 0), the input features.
    self.params[2].schema.featureTypeRule = "FirstDependency"
    self.params[2].schema.geometryTypeRule = "FirstDependency"
    self.params[2].schema.fieldsRule = "FirstDependency"

    # The extent of the output is the intersection of the input features and 
    # the clip features (parameter 1).
    self.params[2].schema.extentRule = "Intersection"

    return
```

### Example 3

```python
import arcpy

toolname = "Buffer_analysis"
parameter_index = 1

# Get the schema of the tool parameter
schema = arcpy.GetParameterInfo(toolname)[parameter_index].schema

properties = ['additionalChildren', 'additionalFields', 'cellSize',
              'cellSizeRule', 'clone', 'extent', 'extentRule',
              'featureType', 'featureTypeRule', 'fieldsRule',
              'geometryType', 'geometryTypeRule', 'rasterFormatRule',
              'rasterRule', 'type']

# Walk through all schema properties and print out the value
for prop in properties:
    try:
        val = eval("schema." + prop)
        print("{:<18} : {}".format(prop, val))
    except (NameError, RuntimeError):
        # Properties unsupported by the parameter datatype will be ignored
        pass
```

### Example 4

```python
import arcpy

toolname = "Buffer_analysis"
parameter_index = 1

# Get the schema of the tool parameter
schema = arcpy.GetParameterInfo(toolname)[parameter_index].schema

properties = ['additionalChildren', 'additionalFields', 'cellSize',
              'cellSizeRule', 'clone', 'extent', 'extentRule',
              'featureType', 'featureTypeRule', 'fieldsRule',
              'geometryType', 'geometryTypeRule', 'rasterFormatRule',
              'rasterRule', 'type']

# Walk through all schema properties and print out the value
for prop in properties:
    try:
        val = eval("schema." + prop)
        print("{:<18} : {}".format(prop, val))
    except (NameError, RuntimeError):
        # Properties unsupported by the parameter datatype will be ignored
        pass
```

---

## SearchNeighborhoodSmooth

## Summary

The SearchNeighborhoodSmooth class can be used to define the search neighborhood for IDW, Local Polynomial Interpolation and Radial Basis Functions (only when the INVERSE_MULTIQUADRIC_FUNCTION keyword is used). The smooth search neighborhood class accepts inputs for a minor and major axis, the size of the search ellipse, the angle of the search ellipse, and a smoothing factor.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| majorSemiaxis | The distance, in map units, specifying the length of the major semi axis of the ellipse within which data is selected from. | Double |
| minorSemiaxis | The distance, in map units, specifying the length of the minor semi axis of the ellipse within which data is selected from. | Double |
| angle | The angle of the search ellipse. | Double |
| smoothFactor | Determines how much smoothing will be performed. 0 is no smoothing; 1 is the maximum amount of smoothing. | Double |

## Code Samples

### Example 1

```python
SearchNeighborhoodSmooth ({majorSemiaxis}, {minorSemiaxis}, {angle}, {smoothFactor})
```

### Example 2

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
arcpy.LocalPolynomialInterpolation_ga(
    "ca_ozone_pts", "OZONE", "outLPI", "C:/gapyexamples/output/lpiout", "2000",
    "2", arcpy.SearchNeighborhoodSmooth(300000, 300000, 0, 0.5), "QUARTIC", 
    "", "", "", "", "PREDICTION")
```

### Example 3

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
arcpy.LocalPolynomialInterpolation_ga(
    "ca_ozone_pts", "OZONE", "outLPI", "C:/gapyexamples/output/lpiout", "2000",
    "2", arcpy.SearchNeighborhoodSmooth(300000, 300000, 0, 0.5), "QUARTIC", 
    "", "", "", "", "PREDICTION")
```

### Example 4

```python
# Name: LocalPolynomialInterpolation_Example_02.py
# Description: Local Polynomial interpolation fits many polynomials, each 
#              within specified overlapping neighborhoods. 
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outLPI"
outRaster = "C:/gapyexamples/output/lpiout"
cellSize = 2000.0
power = 2
kernelFunction = "QUARTIC"
bandwidth = ""
useConNumber = ""
conNumber = ""
weightField = ""
outSurface = "PREDICTION"

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
smoothFactor = 0.5
searchNeighbourhood = arcpy.SearchNeighborhoodSmooth(majSemiaxis, minSemiaxis,
                                                     angle, smoothFactor)


# Execute LocalPolynomialInterpolation
arcpy.LocalPolynomialInterpolation_ga(inPointFeatures, zField, outLayer, outRaster,
                                      cellSize, power, searchNeighbourhood,
                                      kernelFunction, bandwidth, useConNumber,
                                      conNumber, weightField, outSurface)
```

### Example 5

```python
# Name: LocalPolynomialInterpolation_Example_02.py
# Description: Local Polynomial interpolation fits many polynomials, each 
#              within specified overlapping neighborhoods. 
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outLPI"
outRaster = "C:/gapyexamples/output/lpiout"
cellSize = 2000.0
power = 2
kernelFunction = "QUARTIC"
bandwidth = ""
useConNumber = ""
conNumber = ""
weightField = ""
outSurface = "PREDICTION"

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
smoothFactor = 0.5
searchNeighbourhood = arcpy.SearchNeighborhoodSmooth(majSemiaxis, minSemiaxis,
                                                     angle, smoothFactor)


# Execute LocalPolynomialInterpolation
arcpy.LocalPolynomialInterpolation_ga(inPointFeatures, zField, outLayer, outRaster,
                                      cellSize, power, searchNeighbourhood,
                                      kernelFunction, bandwidth, useConNumber,
                                      conNumber, weightField, outSurface)
```

---

## SearchNeighborhoodSmoothCircular

## Summary

The SearchNeighborhoodSmoothCircular class can be used to define the search neighborhood for Empirical Bayesian Kriging, IDW, Local Polynomial Interpolation, and Radial Basis Functions (only when the INVERSE_MULTIQUADRIC_FUNCTION keyword is used). The class accepts inputs for the radius of the searching circle and a smoothing factor.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| radius | The distance, in map units, specifying the length of the radius of the searching circle. | Double |
| smoothFactor | Determines how much smoothing will be performed. 0 is no smoothing; 1 is the maximum amount of smoothing. | Double |

## Code Samples

### Example 1

```python
SearchNeighborhoodSmoothCircular ({radius}, {smoothFactor})
```

### Example 2

```python
import arcpy
arcpy.EmpiricalBayesianKriging_ga("ca_ozone_pts", "OZONE", "outEBK", "C:/gapyexamples/output/ebkout",
                                  100000, "NONE", 50, 0.5, 100,
                                  arcpy.SearchNeighborhoodSmoothCircular(300000, 0.5),
                                  "PREDICTION", "", "", "")
```

### Example 3

```python
import arcpy
arcpy.EmpiricalBayesianKriging_ga("ca_ozone_pts", "OZONE", "outEBK", "C:/gapyexamples/output/ebkout",
                                  100000, "NONE", 50, 0.5, 100,
                                  arcpy.SearchNeighborhoodSmoothCircular(300000, 0.5),
                                  "PREDICTION", "", "", "")
```

### Example 4

```python
# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: ESRI

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outEBK"
outRaster = "C:/gapyexamples/output/ebkout"
cellSize = 10000.0
transformation = "NONE"
maxLocalPoints = 50
overlapFactor = 0.5
numberSemivariograms = 100
# Set variables for search neighborhood
radius = 300000
smooth = 0.6
searchNeighbourhood = arcpy.SearchNeighborhoodSmoothCircular(radius, smooth)
outputType = "PREDICTION"
quantileValue = ""
thresholdType = ""
probabilityThreshold = ""

# Execute EmpiricalBayesianKriging
arcpy.EmpiricalBayesianKriging_ga(inPointFeatures, zField, outLayer, outRaster,
                                  cellSize, transformation, maxLocalPoints, overlapFactor, numberSemivariograms,
                                  searchNeighbourhood, outputType, quantileValue, thresholdType, probabilityThreshold)
```

### Example 5

```python
# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: ESRI

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outEBK"
outRaster = "C:/gapyexamples/output/ebkout"
cellSize = 10000.0
transformation = "NONE"
maxLocalPoints = 50
overlapFactor = 0.5
numberSemivariograms = 100
# Set variables for search neighborhood
radius = 300000
smooth = 0.6
searchNeighbourhood = arcpy.SearchNeighborhoodSmoothCircular(radius, smooth)
outputType = "PREDICTION"
quantileValue = ""
thresholdType = ""
probabilityThreshold = ""

# Execute EmpiricalBayesianKriging
arcpy.EmpiricalBayesianKriging_ga(inPointFeatures, zField, outLayer, outRaster,
                                  cellSize, transformation, maxLocalPoints, overlapFactor, numberSemivariograms,
                                  searchNeighbourhood, outputType, quantileValue, thresholdType, probabilityThreshold)
```

---

## SearchNeighborhoodStandard

## Summary

The SearchNeighborhoodStandard class can be used to define the search neighborhood for IDW, Local Polynomial Interpolation, and Radial Basis Functions.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| majorSemiaxis | The distance, in map units, specifying the length of the major semi axis of the ellipse within which data is selected from. | Double |
| minorSemiaxis | The distance, in map units, specifying the length of the minor semi axis of the ellipse within which data is selected from. | Double |
| angle | The angle of the search ellipse. | Double |
| nbrMax | Maximum number of neighbors, within the search ellipse, to use when making the prediction. | Long |
| nbrMin | Minimum number of neighbors, within the search ellipse, to use when making the prediction. | Long |
| sectorType | The searching ellipse can be divided into 1, 4, 4 with an offset of 45º, or 8 sectors. | String |

## Code Samples

### Example 1

```python
SearchNeighborhoodStandard ({majorSemiaxis}, {minorSemiaxis}, {angle}, {nbrMax}, {nbrMin}, {sectorType})
```

### Example 2

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
arcpy.IDW_ga("ca_ozone_pts", "OZONE", "outIDW", "C:/gapyexamples/output/idwout", "2000", "2",
             arcpy.SearchNeighborhoodStandard(300000, 300000, 0, 15, 10, "ONE_SECTOR"), "")
```

### Example 3

```python
import arcpy
arcpy.env.workspace = "C:/gapyexamples/data"
arcpy.IDW_ga("ca_ozone_pts", "OZONE", "outIDW", "C:/gapyexamples/output/idwout", "2000", "2",
             arcpy.SearchNeighborhoodStandard(300000, 300000, 0, 15, 10, "ONE_SECTOR"), "")
```

### Example 4

```python
# Name: InverseDistanceWeighting_Example_02.py
# Description: Interpolate a series of point features onto a rectangular raster
#              using Inverse Distance Weighting (IDW).
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
outLayer = "outIDW"
outRaster = "C:/gapyexamples/output/idwout"
cellSize = 2000.0
power = 2

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
maxNeighbors = 15
minNeighbors = 10
sectorType = "ONE_SECTOR"
searchNeighbourhood = arcpy.SearchNeighborhoodStandard(majSemiaxis, minSemiaxis,
                                                       angle, maxNeighbors,
                                                       minNeighbors, sectorType)

# Execute IDW
arcpy.IDW_ga(inPointFeatures, zField, outLayer, outRaster, cellSize, 
             power, searchNeighbourhood)
```

### Example 5

```python
# Name: InverseDistanceWeighting_Example_02.py
# Description: Interpolate a series of point features onto a rectangular raster
#              using Inverse Distance Weighting (IDW).
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
outLayer = "outIDW"
outRaster = "C:/gapyexamples/output/idwout"
cellSize = 2000.0
power = 2

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
maxNeighbors = 15
minNeighbors = 10
sectorType = "ONE_SECTOR"
searchNeighbourhood = arcpy.SearchNeighborhoodStandard(majSemiaxis, minSemiaxis,
                                                       angle, maxNeighbors,
                                                       minNeighbors, sectorType)

# Execute IDW
arcpy.IDW_ga(inPointFeatures, zField, outLayer, outRaster, cellSize, 
             power, searchNeighbourhood)
```

---

## SearchNeighborhoodStandard3D

## Summary

The SearchNeighborhoodStandard3D class can be used to define the three dimensional search neighborhood for the Empirical Bayesian Kriging 3D tool.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| radius | The distance, in map units, specifying the length of the radius of the search neighborhood. | Double |
| nbrMax | The maximum number of neighbors, within the search radius, to use when making the prediction. | Long |
| nbrMin | The minimum number of neighbors, within the search radius, to use when making the prediction. | Long |
| sectorType | The sector type of the search neighborhood. The search neighborhood can be divided into 1, 4, 6, 8, 12, or 20 sectors. Each sector type is based on a Platonic solid. ONE_SECTOR—1 Sector (Sphere)FOUR_SECTORS—4 Sectors (Tetrahedron)SIX_SECTORS—6 Sectors (Cube)EIGHT_SECTORS—8 Sectors (Octahedron)TWELVE_SECTORS—12 Sectors (Dodecahedron)TWENTY_SECTORS—20 Sectors (Icosahedron) | String |

## Code Samples

### Example 1

```python
SearchNeighborhoodStandard3D ({radius}, {nbrMax}, {nbrMin}, {sectorType})
```

### Example 2

```python
import arcpy
arcpy.ga.EmpiricalBayesianKriging3D("my3DLayer", "Shape.Z", "myValueField", "myGALayer", "METER", "",
                                    "POWER", "NONE", 100, 1, 100, "NONE", "",
                                    "NBRTYPE=Standard3D RADIUS=10000 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
                                    "", "PREDICTION", 0.5, "EXCEED", "")
```

### Example 3

```python
import arcpy
arcpy.ga.EmpiricalBayesianKriging3D("my3DLayer", "Shape.Z", "myValueField", "myGALayer", "METER", "",
                                    "POWER", "NONE", 100, 1, 100, "NONE", "",
                                    "NBRTYPE=Standard3D RADIUS=10000 NBR_MAX=15 NBR_MIN=10 SECTOR_TYPE=ONE_SECTOR",
                                    "", "PREDICTION", 0.5, "EXCEED", "")
```

### Example 4

```python
# Name: SearchNeighborhoodStandard3D_Example_02.py
# Description: Interpolates 3D points using a standard 3D neighborhood
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set local variables
in3DPoints = "C:/gapyexamples/input/my3DPoints.shp"
elevationField = "Shape.Z"
valueField = "myValueField"
outGALayer = "myGALayer"
elevationUnit = "METER"
measurementErrorField = "myMEField"
semivariogramModel = "LINEAR"
transformationType = "NONE"
subsetSize = 80
overlapFactor = 1.5
numSimulations = 200
trendRemoval = "FIRST"
elevInflationFactor = 20
radius = 10000
maxNeighbors = 15
minNeighbors = 10
sectorType = "FOUR_SECTORS"
searchNeighborhood = arcpy.SearchNeighborhoodStandard3D(radius, maxNeighbors, minNeighbors, sectorType)
outputElev = 1000
outputType = "PREDICTION"

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Empirical Bayesian Kriging 3D
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints, elevationField, valueField, outGALayer, elevationUnit, myMEField,
                                    semivariogramModel, transformationType, subsetSize, overlapFactor, numSimulations,
                                    trendRemoval, elevInflationFactor, searchNeighborhood, outputElev, outputType)
```

### Example 5

```python
# Name: SearchNeighborhoodStandard3D_Example_02.py
# Description: Interpolates 3D points using a standard 3D neighborhood
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set local variables
in3DPoints = "C:/gapyexamples/input/my3DPoints.shp"
elevationField = "Shape.Z"
valueField = "myValueField"
outGALayer = "myGALayer"
elevationUnit = "METER"
measurementErrorField = "myMEField"
semivariogramModel = "LINEAR"
transformationType = "NONE"
subsetSize = 80
overlapFactor = 1.5
numSimulations = 200
trendRemoval = "FIRST"
elevInflationFactor = 20
radius = 10000
maxNeighbors = 15
minNeighbors = 10
sectorType = "FOUR_SECTORS"
searchNeighborhood = arcpy.SearchNeighborhoodStandard3D(radius, maxNeighbors, minNeighbors, sectorType)
outputElev = 1000
outputType = "PREDICTION"

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Empirical Bayesian Kriging 3D
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints, elevationField, valueField, outGALayer, elevationUnit, myMEField,
                                    semivariogramModel, transformationType, subsetSize, overlapFactor, numSimulations,
                                    trendRemoval, elevInflationFactor, searchNeighborhood, outputElev, outputType)
```

---

## SearchNeighborhoodStandardCircular

## Summary

The SearchNeighborhoodStandardCircular class can be used to define the search neighborhood for Empirical Bayesian Kriging, IDW, Local Polynomial Interpolation, and Radial Basis Functions.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| radius | The distance, in map units, specifying the length of the radius of the searching circle. | Double |
| angle | The angle of the search circle. This parameter will only affect the angle of the sectors. | Double |
| nbrMax | Maximum number of neighbors, within the search ellipse, to use when making the prediction. | Long |
| nbrMin | Minimum number of neighbors, within the search ellipse, to use when making the prediction. | Long |
| sectorType | The searching ellipse can be divided into 1, 4, 4 with an offset of 45º, or 8 sectors. | String |

## Code Samples

### Example 1

```python
SearchNeighborhoodStandardCircular ({radius}, {angle}, {nbrMax}, {nbrMin}, {sectorType})
```

### Example 2

```python
import arcpy
arcpy.EmpiricalBayesianKriging_ga("ca_ozone_pts", "OZONE", "outEBK", "C:/gapyexamples/output/ebkout",
                                  10000, "NONE", 50, 0.5, 100,
                                  arcpy.SearchNeighborhoodStandardCircular(300000, 0, 15, 10, "ONE_SECTOR"),
                                  "PREDICTION", "", "", "")
```

### Example 3

```python
import arcpy
arcpy.EmpiricalBayesianKriging_ga("ca_ozone_pts", "OZONE", "outEBK", "C:/gapyexamples/output/ebkout",
                                  10000, "NONE", 50, 0.5, 100,
                                  arcpy.SearchNeighborhoodStandardCircular(300000, 0, 15, 10, "ONE_SECTOR"),
                                  "PREDICTION", "", "", "")
```

### Example 4

```python
# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: ESRI

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outEBK"
outRaster = "C:/gapyexamples/output/ebkout"
cellSize = 10000.0
transformation = "NONE"
maxLocalPoints = 50
overlapFactor = 0.5
numberSemivariograms = 100
# Set variables for search neighborhood
radius = 300000
angle = 0
maxNeighbors = 15
minNeighbors = 10
sectorType = "ONE_SECTOR"
searchNeighbourhood = arcpy.SearchNeighborhoodStandardCircular(radius,
                                                       angle, maxNeighbors,
                                                       minNeighbors, sectorType)
outputType = "PREDICTION"
quantileValue = ""
thresholdType = ""
probabilityThreshold = ""

# Execute EmpiricalBayesianKriging
arcpy.EmpiricalBayesianKriging_ga(inPointFeatures, zField, outLayer, outRaster,
                                  cellSize, transformation, maxLocalPoints, overlapFactor, numberSemivariograms,
                                  searchNeighbourhood, outputType, quantileValue, thresholdType, probabilityThreshold)
```

### Example 5

```python
# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: ESRI

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outEBK"
outRaster = "C:/gapyexamples/output/ebkout"
cellSize = 10000.0
transformation = "NONE"
maxLocalPoints = 50
overlapFactor = 0.5
numberSemivariograms = 100
# Set variables for search neighborhood
radius = 300000
angle = 0
maxNeighbors = 15
minNeighbors = 10
sectorType = "ONE_SECTOR"
searchNeighbourhood = arcpy.SearchNeighborhoodStandardCircular(radius,
                                                       angle, maxNeighbors,
                                                       minNeighbors, sectorType)
outputType = "PREDICTION"
quantileValue = ""
thresholdType = ""
probabilityThreshold = ""

# Execute EmpiricalBayesianKriging
arcpy.EmpiricalBayesianKriging_ga(inPointFeatures, zField, outLayer, outRaster,
                                  cellSize, transformation, maxLocalPoints, overlapFactor, numberSemivariograms,
                                  searchNeighbourhood, outputType, quantileValue, thresholdType, probabilityThreshold)
```

---

## SpatialReference

## Summary

Each part of the spatial reference has a number of properties (especially the coordinate system) that defines what map projection options are used to define horizontal coordinates.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| item | The horizontal coordinate system used to create the SpatialReference object. The coordinate system can be set using a projection file, name, or factory code.Create a SpatialReference object using the display name of a coordinate system.sr = arcpy.SpatialReference("Sinusoidal (world)")Create a SpatialReference object using the canonical name of a coordinate system.sr = arcpy.SpatialReference("World_Sinusoidal")Create a SpatialReference object using a coordinate system's factory code (or authority code or WKID).# The factory code of 32145 represents: # NAD 1983 StatePlane Vermont FIPS 4400 (Meters) sr = arcpy.SpatialReference(32145)Create a SpatialReference object using a projection file (.prj).sr = arcpy.SpatialReference("c:/coordsystems/NAD 1983.prj")For more information about coordinate system names and factory codes, see the geographic_coordinate_systems.pdf and projected_coordinate_systems.pdf files.For more information, see Using the spatial reference class. | Variant |
| vcs | The vertical coordinate system (VCS). The VCS defines information about the z-coordinates and can be set using a name or factory code. See the following examples:Define the vertical coordinate system using a name.sr = arcpy.SpatialReference("Hawaii Albers Equal Area Conic", "MSL Height")Define the vertical coordinate system using a factory code.# Spatial Reference factory code of 32145 is : NAD 1983 StatePlane Vermont FIPS 4400 (Meters) # Spatial Reference factory code of 5714 is : Mean Sea Level (Height) sr = arcpy.SpatialReference(32145, 5714) | Variant |
| text | A well-known text (WKT or WKT2 format) string that can be used to define a horizontal and vertical coordinate system.Note:When creating a SpatialReference object with a vertical coordinate system using the text argument, define the vertical coordinate system using the VERTCS section of the WKT string. The vcs argument is not used.Create a SpatialReference object using a WKT string with a horizontal coordinate system.# String below is the WKT for the # Geographic Coordinate system "WGS 1984" (factory code=4326) wkt = """ GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]], PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]; -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09; 0.001;0.001;IsHighPrecision """ sr = arcpy.SpatialReference(text=wkt)Create a SpatialReference object using a WKT2 string with a horizontal coordinate system.# The following string is the WKT2 for the # Projected Coordinate System "NAD 1983 StatePlane California V FIPS 0405 (US FEET) # (factory code=2229) wkt2 = """ PROJCRS[ "NAD_1983_StatePlane_California_V_FIPS_0405_Feet", BASEGEOGCRS["GCS_North_American_1983",DATUM["D_North_American_1983", ELLIPSOID["GRS_1980",6378137.0,298.257222101,LENGTHUNIT["Meter",1.0]] ], PRIMEM["Greenwich",0.0,ANGLEUNIT["Degree",0.017453292519943295]],CS[ellipsoidal,2], AXIS["Latitude (lat)",north,ORDER[1]],AXIS["Longitude (lon)",east,ORDER[2]], ANGLEUNIT["Degree",0.017453292519943295]], CONVERSION["Lambert_Conformal_Conic",METHOD["Lambert_Conformal_Conic"], PARAMETER["False_Easting",6561666.666666666,LENGTHUNIT["Foot_US",0.30480060960121924]], PARAMETER["False_Northing",1640416.666666667,LENGTHUNIT["Foot_US",0.30480060960121924]], PARAMETER["Central_Meridian",-118.0,ANGLEUNIT["Degree",0.017453292519943295]], PARAMETER["Standard_Parallel_1",34.033333333333331,ANGLEUNIT["Degree",0.017453292519943295]], PARAMETER["Standard_Parallel_2",35.466666666666669,ANGLEUNIT["Degree",0.017453292519943295]], PARAMETER["Latitude_Of_Origin",33.5,ANGLEUNIT["Degree",0.017453292519943295]]],CS[Cartesian,2], AXIS["Easting (X)",east,ORDER[1]],AXIS["Northing (Y)",north,ORDER[2]], LENGTHUNIT["Foot_US",0.30480060960121924]] """ sr = arcpy.SpatialReference(text=wkt2)Create a SpatialReference object using a WKT string with a horizontal and vertical coordinate system.# The following string is the WKT for the # Geographic Coordinate system "WGS 1984" (factory code=4326) wkt = """ GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]], PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]], VERTCS['WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]], PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]]; -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09; 0.001;0.001;IsHighPrecision """ sr = arcpy.SpatialReference(text=wkt) | String |
| prj_file | The projection file used to populate the SpatialReference object. | String |
| encoding | Specifies the encoding of the exported string.WKT—The spatial reference will be exported to the WKT standard.WKT2—The spatial reference will be exported to the WKT 2 standard.(The default value is WKT) | String |
| string | The WKT string representation of the object. | String |
| x_min | The minimum x-value. | Double |
| x_max | The maximum x-value. | Double |
| y_min | The minimum y-value. | Double |
| y_max | The maximum y-value. | Double |
| false_x | The false x value. | Double |
| false_y | The false y value. | Double |
| xy_units | The xy units. | String |
| m_min | The minimum m-value. | Double |
| m_max | The maximum m-value. | Double |
| false_m | The false m-value. | Double |
| m_units | The m units. | Double |
| z_min | The minimum z-value. | Double |
| z_max | The maximum z-value. | Double |
| false_z | The false z-value. | Double |
| z_units | The false z units. | Double |

## Methods

### create ()

Creates the SpatialReference object using properties.

### createFromFile (prj_file)

Creates the SpatialReference object from a projection file.

### exportToString ({encoding})

Exports the object to its string representation.

### loadFromString (string)

Defines a SpatialReference object from a WKT string. The exportToString method can be used to export a WKT string representation of the spatial reference.Using a WKT string with a horizontal coordinate system.# The following string is the WKT for the # Geographic Coordinate system "WGS 1984" (factory code=4326) wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\ PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];\ -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\ 0.001;0.001;IsHighPrecision' sr = arcpy.SpatialReference() sr.loadFromString(wkt)Using a WKT string with a horizontal and vertical coordinate system. Note that the vertical coordinate system is defined in the VERTCS section of the WKT.# The following string is the WKT for the # Geographic Coordinate system "WGS 1984" (factory code=4326), # with a vertical coordinate system "WGS 1984" (factory code=115700) wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\ PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],\ VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\ PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]];\ -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\ 0.001;0.001;IsHighPrecision' sr = arcpy.SpatialReference() sr.loadFromString(wkt)

### setDomain (x_min, x_max, y_min, y_max)

Sets the XY domain.

### setFalseOriginAndUnits (false_x, false_y, xy_units)

Sets the XY false origin and units.

### setMDomain (m_min, m_max)

Sets the M domain.

### setMFalseOriginAndUnits (false_m, m_units)

Sets the M false origin and units.

### setZDomain (z_min, z_max)

Sets the Z domain.

### setZFalseOriginAndUnits (false_z, z_units)

Sets the Z false origin and units.

## Code Samples

### Example 1

```python
dataset = "c:/data/landbase.gdb/Wetlands"
spatial_ref = arcpy.Describe(dataset).spatialReference
```

### Example 2

```python
dataset = "c:/data/landbase.gdb/Wetlands"
spatial_ref = arcpy.Describe(dataset).spatialReference
```

### Example 3

```python
SpatialReference ({item}, {vcs}, {text})
```

### Example 4

```python
sr = arcpy.SpatialReference("Sinusoidal (world)")
```

### Example 5

```python
sr = arcpy.SpatialReference("Sinusoidal (world)")
```

### Example 6

```python
sr = arcpy.SpatialReference("World_Sinusoidal")
```

### Example 7

```python
sr = arcpy.SpatialReference("World_Sinusoidal")
```

### Example 8

```python
# The factory code of 32145 represents: 
# NAD 1983 StatePlane Vermont FIPS 4400 (Meters)

sr = arcpy.SpatialReference(32145)
```

### Example 9

```python
# The factory code of 32145 represents: 
# NAD 1983 StatePlane Vermont FIPS 4400 (Meters)

sr = arcpy.SpatialReference(32145)
```

### Example 10

```python
sr = arcpy.SpatialReference("c:/coordsystems/NAD 1983.prj")
```

### Example 11

```python
sr = arcpy.SpatialReference("c:/coordsystems/NAD 1983.prj")
```

### Example 12

```python
sr = arcpy.SpatialReference("Hawaii Albers Equal Area Conic", "MSL Height")
```

### Example 13

```python
sr = arcpy.SpatialReference("Hawaii Albers Equal Area Conic", "MSL Height")
```

### Example 14

```python
# Spatial Reference factory code of 32145 is : NAD 1983 StatePlane Vermont FIPS 4400 (Meters)
# Spatial Reference factory code of 5714 is : Mean Sea Level (Height)

sr = arcpy.SpatialReference(32145, 5714)
```

### Example 15

```python
# Spatial Reference factory code of 32145 is : NAD 1983 StatePlane Vermont FIPS 4400 (Meters)
# Spatial Reference factory code of 5714 is : Mean Sea Level (Height)

sr = arcpy.SpatialReference(32145, 5714)
```

### Example 16

```python
# String below is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = """
GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];
-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;
0.001;0.001;IsHighPrecision
"""

sr = arcpy.SpatialReference(text=wkt)
```

### Example 17

```python
# String below is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = """
GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];
-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;
0.001;0.001;IsHighPrecision
"""

sr = arcpy.SpatialReference(text=wkt)
```

### Example 18

```python
# The following string is the WKT2 for the
# Projected Coordinate System "NAD 1983 StatePlane California V FIPS 0405 (US FEET)
# (factory code=2229)
wkt2 = """
PROJCRS[
   "NAD_1983_StatePlane_California_V_FIPS_0405_Feet",
   BASEGEOGCRS["GCS_North_American_1983",DATUM["D_North_American_1983",
   ELLIPSOID["GRS_1980",6378137.0,298.257222101,LENGTHUNIT["Meter",1.0]]
],
PRIMEM["Greenwich",0.0,ANGLEUNIT["Degree",0.017453292519943295]],CS[ellipsoidal,2],
AXIS["Latitude (lat)",north,ORDER[1]],AXIS["Longitude (lon)",east,ORDER[2]],
ANGLEUNIT["Degree",0.017453292519943295]],
CONVERSION["Lambert_Conformal_Conic",METHOD["Lambert_Conformal_Conic"],
PARAMETER["False_Easting",6561666.666666666,LENGTHUNIT["Foot_US",0.30480060960121924]],
PARAMETER["False_Northing",1640416.666666667,LENGTHUNIT["Foot_US",0.30480060960121924]],
PARAMETER["Central_Meridian",-118.0,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Standard_Parallel_1",34.033333333333331,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Standard_Parallel_2",35.466666666666669,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Latitude_Of_Origin",33.5,ANGLEUNIT["Degree",0.017453292519943295]]],CS[Cartesian,2],
AXIS["Easting (X)",east,ORDER[1]],AXIS["Northing (Y)",north,ORDER[2]],
LENGTHUNIT["Foot_US",0.30480060960121924]]
"""

sr = arcpy.SpatialReference(text=wkt2)
```

### Example 19

```python
# The following string is the WKT2 for the
# Projected Coordinate System "NAD 1983 StatePlane California V FIPS 0405 (US FEET)
# (factory code=2229)
wkt2 = """
PROJCRS[
   "NAD_1983_StatePlane_California_V_FIPS_0405_Feet",
   BASEGEOGCRS["GCS_North_American_1983",DATUM["D_North_American_1983",
   ELLIPSOID["GRS_1980",6378137.0,298.257222101,LENGTHUNIT["Meter",1.0]]
],
PRIMEM["Greenwich",0.0,ANGLEUNIT["Degree",0.017453292519943295]],CS[ellipsoidal,2],
AXIS["Latitude (lat)",north,ORDER[1]],AXIS["Longitude (lon)",east,ORDER[2]],
ANGLEUNIT["Degree",0.017453292519943295]],
CONVERSION["Lambert_Conformal_Conic",METHOD["Lambert_Conformal_Conic"],
PARAMETER["False_Easting",6561666.666666666,LENGTHUNIT["Foot_US",0.30480060960121924]],
PARAMETER["False_Northing",1640416.666666667,LENGTHUNIT["Foot_US",0.30480060960121924]],
PARAMETER["Central_Meridian",-118.0,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Standard_Parallel_1",34.033333333333331,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Standard_Parallel_2",35.466666666666669,ANGLEUNIT["Degree",0.017453292519943295]],
PARAMETER["Latitude_Of_Origin",33.5,ANGLEUNIT["Degree",0.017453292519943295]]],CS[Cartesian,2],
AXIS["Easting (X)",east,ORDER[1]],AXIS["Northing (Y)",north,ORDER[2]],
LENGTHUNIT["Foot_US",0.30480060960121924]]
"""

sr = arcpy.SpatialReference(text=wkt2)
```

### Example 20

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = """
GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],
VERTCS['WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]];
-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;
0.001;0.001;IsHighPrecision
"""

sr = arcpy.SpatialReference(text=wkt)
```

### Example 21

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = """
GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],
VERTCS['WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],
PARAMETER['Vertical_Shift',0.0],PARAMETER['Direction',1.0],UNIT['Meter',1.0]];
-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;
0.001;0.001;IsHighPrecision
"""

sr = arcpy.SpatialReference(text=wkt)
```

### Example 22

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision'

sr = arcpy.SpatialReference()
sr.loadFromString(wkt)
```

### Example 23

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326)
wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision'

sr = arcpy.SpatialReference()
sr.loadFromString(wkt)
```

### Example 24

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326), 
# with a vertical coordinate system "WGS 1984" (factory code=115700)

wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],\
              VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision'

sr = arcpy.SpatialReference()
sr.loadFromString(wkt)
```

### Example 25

```python
# The following string is the WKT for the 
# Geographic Coordinate system "WGS 1984" (factory code=4326), 
# with a vertical coordinate system "WGS 1984" (factory code=115700)

wkt = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],\
              VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],\
              PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]];\
              -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;\
              0.001;0.001;IsHighPrecision'

sr = arcpy.SpatialReference()
sr.loadFromString(wkt)
```

### Example 26

```python
createFromFile (prj_file)
```

### Example 27

```python
exportToString ({encoding})
```

### Example 28

```python
loadFromString (string)
```

### Example 29

```python
setDomain (x_min, x_max, y_min, y_max)
```

### Example 30

```python
setFalseOriginAndUnits (false_x, false_y, xy_units)
```

### Example 31

```python
setMDomain (m_min, m_max)
```

### Example 32

```python
setMFalseOriginAndUnits (false_m, m_units)
```

### Example 33

```python
setZDomain (z_min, z_max)
```

### Example 34

```python
setZFalseOriginAndUnits (false_z, z_units)
```

### Example 35

```python
import arcpy

# Set the workspace environment
arcpy.env.workspace = "c:/base/base.gdb"

# Get a list of the feature classes in the input folder
feature_classes = arcpy.ListFeatureClasses()

# Loop through the list
for fc in feature_classes:
    # Create the spatial reference object
    spatial_ref = arcpy.Describe(fc).spatialReference

    # If the spatial reference is unknown
    if spatial_ref.name == "Unknown":
        print(r"{fc} has an unknown spatial reference")

    # Otherwise, print out the feature class name and spatial reference
    else:
        print(f"{fc} : {spatial_ref.name}")
```

### Example 36

```python
import arcpy

# Set the workspace environment
arcpy.env.workspace = "c:/base/base.gdb"

# Get a list of the feature classes in the input folder
feature_classes = arcpy.ListFeatureClasses()

# Loop through the list
for fc in feature_classes:
    # Create the spatial reference object
    spatial_ref = arcpy.Describe(fc).spatialReference

    # If the spatial reference is unknown
    if spatial_ref.name == "Unknown":
        print(r"{fc} has an unknown spatial reference")

    # Otherwise, print out the feature class name and spatial reference
    else:
        print(f"{fc} : {spatial_ref.name}")
```

---

## Value

## Summary

A Value object is returned from GetParameterInfo when used in a script tool's ToolValidator class, and from the GetParameter function depending on the parameter type.

## Code Samples

### Example 1

```python
def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""

    # If the parameter has been altered, but not validated
    if self.params[0].altered and not self.params[0].hasBeenValidated:
        # Create a NetCDFFIleProperties object based on the input and
        #   use it to populate the value list of the sceond parameter.
        net_cdf = arcpy.NetCDFFileProperties(self.params[0].value.value)
        att_names = net_cdf.getAttributeNames()
        self.params[1].filter.list = att_names
        self.params[1].value = att_names[0]

    return
```

### Example 2

```python
def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""

    # If the parameter has been altered, but not validated
    if self.params[0].altered and not self.params[0].hasBeenValidated:
        # Create a NetCDFFIleProperties object based on the input and
        #   use it to populate the value list of the sceond parameter.
        net_cdf = arcpy.NetCDFFileProperties(self.params[0].value.value)
        att_names = net_cdf.getAttributeNames()
        self.params[1].filter.list = att_names
        self.params[1].value = att_names[0]

    return
```

---

## ValueTable

## Summary

A value table is a flexible table-like object, made up of rows and columns containing various values.

## Parameters

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| columns | Adds columns to the ValueTable object. The value can be as follows:The number of columns as an integer. Each column will be added as a GPString data type.The data type of a single column as a string, for example, "GPString". The data types of multiple columns as a list of strings, for example, ["GPDate", "GPLong"]. (The default value is 1) | Integer |
| number_of_columns | The number of columns for the value table. | Integer |
| value | A list of values to be added as a new row. The value argument can be as follows:A list containing appropriate native Python objects, for example, vtab.addRow(['c:/temp/land use.shp', 2]). A space-delimited string representation. Values within the string that contain spaces must be enclosed in quotations, for example, vtab.addRow("'c:/temp/land use.shp' 2"). | Object |
| row | The row index position. | Integer |
| row | The row index position. | Integer |
| row | The row index position. | Integer |
| column | The column index position. | Integer |
| row | The row index position. | Integer |
| column | The column index position. | Integer |
| string | The string representation of the object.Within the string, all values are wrapped in single quotes, with each value in a row separated by a space, and each row separated by a semicolon. Each column in the ValueTable will have a data type of GPString. | String |
| row | The index position of the row to remove. | Integer |
| number_of_columns | The number of columns for the value table. | Integer |
| row | The index position of the row to update. | Integer |
| value | The value to update in the given row. | Object |
| row | The row index. | Integer |
| column | The column index. | Integer |
| value | The value to update the given row and column. This can be a string representation or a native Python type (int, bool, or datetime.datetime). | Object |

## Methods

### addColumns (number_of_columns)

Adds columns to the ValueTable object. The value can be as follows:The number of columns as an integer. Each column will be added as a GPString data type.The data type of a single column as a string, for example, "GPString". The data types of multiple columns as a list of strings, for example, ["GPDate", "GPLong"].The addColumns method is functionally equivalent to the setColumns method.

### addRow (value)

Adds a row with specified values to the value table.

### exportToString ()

Exports the object to its string representation.

### getRow (row)

Returns the values from the row at the specified index. The row's values are returned as a space-delimited string.

### getTrueRow (row)

Returns the value from the row at the specified index. The row's values are returned as a list with appropriate Python objects.The column data type to Python object mappings are the following: Integer to intDouble to floatBoolean to boolDate to datetime.datetime

### getTrueValue (row, column)

Given a column and row index, returns the value as an appropriate Python object.The column data type to Python object mappings are the following: Integer to intDouble to floatBoolean to boolDate to datetime.datetimeThe value for all other column types are returned as strings.

### getValue (row, column)

Returns the value from a given column and row as a string.

### loadFromString (string)

Defines a ValueTable object from a formatted string.

### removeRow (row)

Deletes the row found at the specified index.

### setColumns (number_of_columns)

Adds columns to the ValueTable object. The value can be as follows:The number of columns as an integer. Each column will be added as a GPString data type.The data type of a single column as a string, for example, "GPString". The data types of multiple columns as a list of strings, for example, ["GPDate", "GPLong"].The setColumns method is functionally equivalent to the addColumns method.

### setRow (row, value)

Updates a given row within the ValueTable object. The value argument is space-delimited. Any value that contains spaces must be enclosed in quotations. In the following example, a feature class and an index value are added to the ValueTable object with two columns.vtab.setRow(0, "'c:/temp/land use.shp' 2") Unlike other row operations, the setRow only supports a string value.

### setValue (row, column, value)

Updates the value of a given row and column. The value can be a either a string representation or an appropriate native Python type.For example, if the column is a date type, a datetime.datetime object or a string can be used. # Must be system appropriate string representation of a date vtab.setValue(0, 1, "2021-06-17") vtab.setValue(0, 1, datetime.datetime(2021, 6, 17)

## Code Samples

### Example 1

```python
ValueTable  ({columns})
```

### Example 2

```python
vtab.setRow(0, "'c:/temp/land use.shp' 2")
```

### Example 3

```python
vtab.setRow(0, "'c:/temp/land use.shp' 2")
```

### Example 4

```python
# Must be system appropriate string representation of a date
vtab.setValue(0, 1, "2021-06-17") 

vtab.setValue(0, 1, datetime.datetime(2021, 6, 17)
```

### Example 5

```python
# Must be system appropriate string representation of a date
vtab.setValue(0, 1, "2021-06-17") 

vtab.setValue(0, 1, datetime.datetime(2021, 6, 17)
```

### Example 6

```python
addColumns (number_of_columns)
```

### Example 7

```python
addRow (value)
```

### Example 8

```python
exportToString ()
```

### Example 9

```python
getRow (row)
```

### Example 10

```python
getTrueRow (row)
```

### Example 11

```python
getTrueValue (row, column)
```

### Example 12

```python
getValue (row, column)
```

### Example 13

```python
loadFromString (string)
```

### Example 14

```python
removeRow (row)
```

### Example 15

```python
setColumns (number_of_columns)
```

### Example 16

```python
setRow (row, value)
```

### Example 17

```python
setValue (row, column, value)
```

### Example 18

```python
import arcpy

# Set the workspace. List all of the feature classes in the dataset
arcpy.env.workspace = "c:/data/landbase.gdb/Wetlands"
feature_classes = arcpy.ListFeatureClasses()

# Create the value table for the Analysis toolbox Union function with 2 columns
value_table = arcpy.ValueTable(2)

# Iterate through the list of feature classes
for fc in feature_classes:
    # Update the value table with a rank of 2 for each record, except
    #   for BigBog
    if fc.lower() != "bigbog":
        value_table.addRow(fc + " 2")
    else:
        value_table.addRow(fc + " 1")

# Union the wetlands feature classes with the land use feature class to create
# a single feature class with all of the wetlands and land use data
value_table.addRow("c:/data/landbase.gdb/land_use 2")
arcpy.Union_analysis(value_table, "c:/data/landbase.gdb/wetlands_use")
```

### Example 19

```python
import arcpy

# Set the workspace. List all of the feature classes in the dataset
arcpy.env.workspace = "c:/data/landbase.gdb/Wetlands"
feature_classes = arcpy.ListFeatureClasses()

# Create the value table for the Analysis toolbox Union function with 2 columns
value_table = arcpy.ValueTable(2)

# Iterate through the list of feature classes
for fc in feature_classes:
    # Update the value table with a rank of 2 for each record, except
    #   for BigBog
    if fc.lower() != "bigbog":
        value_table.addRow(fc + " 2")
    else:
        value_table.addRow(fc + " 1")

# Union the wetlands feature classes with the land use feature class to create
# a single feature class with all of the wetlands and land use data
value_table.addRow("c:/data/landbase.gdb/land_use 2")
arcpy.Union_analysis(value_table, "c:/data/landbase.gdb/wetlands_use")
```

### Example 20

```python
import os
import arcpy

# Set the output workspace
arcpy.env.workspace = arcpy.GetParameterAsText(1)

# Create a value table with 2 columns
value_table = arcpy.ValueTable(2)

# Set the values of the table with the contents of the first argument
value_table.loadFromString(arcpy.GetParameterAsText(0))

# Loop through the list of inputs
for i in range(0, value_table.rowCount):
    # Validate the output name for the new workspace
    name = value_table.getRow(i)
    out_name = arcpy.ValidateTableName(os.path.basename(name))

    # Copy the features to the new workspace
    arcpy.CopyFeatures_management(name, out_name)
```

### Example 21

```python
import os
import arcpy

# Set the output workspace
arcpy.env.workspace = arcpy.GetParameterAsText(1)

# Create a value table with 2 columns
value_table = arcpy.ValueTable(2)

# Set the values of the table with the contents of the first argument
value_table.loadFromString(arcpy.GetParameterAsText(0))

# Loop through the list of inputs
for i in range(0, value_table.rowCount):
    # Validate the output name for the new workspace
    name = value_table.getRow(i)
    out_name = arcpy.ValidateTableName(os.path.basename(name))

    # Copy the features to the new workspace
    arcpy.CopyFeatures_management(name, out_name)
```

### Example 22

```python
import arcpy
import datetime

# Create a value table with 3 columns
value_table = arcpy.ValueTable(["GPLong", "GPBoolean", "GPDate"])

# Set the values of the table with native Python types
value_table.addRow([1, True, datetime.datetime(2004, 12, 19)])
value_table.addRow([2, False, datetime.datetime(2008, 2, 13)])

# Retrieve true Python object from ValueTable
event_date = value_table.getTrueValue(1, 2)
```

### Example 23

```python
import arcpy
import datetime

# Create a value table with 3 columns
value_table = arcpy.ValueTable(["GPLong", "GPBoolean", "GPDate"])

# Set the values of the table with native Python types
value_table.addRow([1, True, datetime.datetime(2004, 12, 19)])
value_table.addRow([2, False, datetime.datetime(2008, 2, 13)])

# Retrieve true Python object from ValueTable
event_date = value_table.getTrueValue(1, 2)
```

---

## VCS

## Summary

Provides information about the vertical coordinate system (VCS) component of a SpatialReference object.

## Code Samples

### Example 1

```python
import arcpy

# Create a Spatial Reference (Europe Equidistant Conic) with a VCS (EVRF_2007)
sr = arcpy.SpatialReference(102031, 5621)

# Use the SpatialReference as input to a tool
out = arcpy.management.CreateFeatureDataset(outgdb, "euro_fds", sr)

# Describe the output to confirm the VCS factoryCode
sr = arcpy.Describe(out[0]).spatialReference
print(sr.VCS.factoryCode)  # prints 5621
```

### Example 2

```python
import arcpy

# Create a Spatial Reference (Europe Equidistant Conic) with a VCS (EVRF_2007)
sr = arcpy.SpatialReference(102031, 5621)

# Use the SpatialReference as input to a tool
out = arcpy.management.CreateFeatureDataset(outgdb, "euro_fds", sr)

# Describe the output to confirm the VCS factoryCode
sr = arcpy.Describe(out[0]).spatialReference
print(sr.VCS.factoryCode)  # prints 5621
```

---
