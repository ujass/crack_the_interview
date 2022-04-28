"""
Let us do the cat & other linux command with the subprocess
"""

"""
1. cat file content of test.txt file. 

run(['cat', 'test.txt'] list contain the list of command we want to run in one shot
"""

import subprocess

p1 = subprocess.run(['cat', 'test.txt'], capture_output=True)
print(p1.stdout)        # this is in bytes
# get the answer in text, either add text=True in subprocess or p1.stdout.decode()

print(p1.stdout.decode())


"""
Let us do the grep 
"""
                    # we can do here also                                  # grep from here
p2 = subprocess.run(['grep', '-n', 'line'], capture_output=True, text=True, input=p1.stdout.decode())
print(p2.stdout)