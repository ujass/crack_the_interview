import os

# home directory
print(os.environ.get('HOME'))

# this is bad way to make a path
file_path = os.environ.get('HOME') + 'test.txt'

# why??
# because we think path is correct but we forgot the / before the test.txt.
print(file_path)

"""
Who can help me with the path proble??? 
solution - os.path is best way to solve this problem
"""
print('\nSecond example... (os.path.join)')
file_path_2 = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path_2)

"""
Check perticular path exist or not? 
"""

print(os.path.exists('fack/path/checking.txt'))     # False

"""
Find the base directory name, 
"""
print(os.path.basename('/base/sub_base/test.txt'))
print(os.path.dirname('/base/sub_base'))
print(os.path.dirname('/base/sub_base/test.txt'))

"""
CHeck perticular path ends with file or at directory
"""

print(os.path.isdir('/home/meditab'))       # true
print(os.path.isfile('/home/meditab/'))     # false

"""
split the extension of the  end file from the path. 
"""

print(os.path.splitext('/home/meditab/demo.txt'))