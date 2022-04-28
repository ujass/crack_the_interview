import os
import stat

"""
Here we learn about how can we use python to run os level commands. 

1. Let us create the folder.
"""
print('First example... (Create folder)')
# print current working directory
print(os.getcwd())

# this will change directory to the given path
os.chdir('/home/meditab/dummy')
print(os.getcwd())

# list add the dirctory in the current working directory
print(os.listdir())

"""
How to make new directory with os??
There are 2 methods available 
1. mkdir(d1)             - only create one directory - d1
2. makedirs(d1/d2)       - will create subdirectory as well. - d1/d2 
"""

# always mention full path of the directory we want to make.
path = "/home/meditab/dummy/dumy3"

# access_rights = 0o666 # mention access code if we need it.

try:
    os.mkdir(path)
    print("Folder created...")
except FileExistsError:
    print("File already exist denied")
except OSError:
    print ("Creation of the directory %s failed" % path)
except Exception as e:
    print("Exception occur in file creation {}".format(e))
else:
    print ("Successfully created the directory %s " % path)

# os.chmod('./', 755)
# os.makedirs('/demo_dir')     # this will work
# os.makedirs('/demo_dir1/sub_dir1')      # this will throw error, because demo_dir is not present yet

"""
2. Delete the created folder  with os. 
"""
# print('\n\nSecond example... (delete folder)')
# try:
#     os.rmdir(path)
#     print("Folder successfully deleted...")
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("Exception occure in deleting file")

print(os.listdir())

"""
Let us create a file and rename it.
Rename the folder / file 
"""
#
# with open(path + "/test.txt") as fp:
#     pass
#
# print(os.getcwd())
# # os.rename('dumy3.txt', 'd3.txt')
# print(os.listdir())


"""
use os.walk method to find the folder of the converyor_management & console_simulatore

os.walk(path_from_where_we want_to_start)
"""

for dirpath, dirnames, filenames in os.walk('/home/meditab/dummy'):
    print(dirpath)
    print(dirnames)
    print(filenames)

