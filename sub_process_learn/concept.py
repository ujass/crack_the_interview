import subprocess

"""
Note: shell = True, then we can pass whole command as a string. 
                    not safe
                    
Capture output = True, get the standard output and erros. 
"""
# if windows subprocess.run('ls', shell= True)
subprocess.run('ls -la', shell=True)        # shell true is not safe
subprocess.run('ls')

# safe ways
subprocess.run(['ls', '-la'])

"""
Let us do something with the subprocess command
"""

process1 = subprocess.run(['ls', '-la'])
print(process1)
print(process1.args)
print(process1.returncode)      # 0 means, 0 errors. run successfully
print(process1.stdout)          # why this is none

"""
Reason is that, subprocess printing everything to the commandline. 
let us catch that thing
"""
print('\nSecond example... (capture the output)')
process2 = subprocess.run(['ls', '-la'], capture_output=True)
print(process2.stdout)  # this is capture as bytes

# 1. decode the bytes
print(process2.stdout.decode())

# 2. capture the text dirctly
process3 = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(process3)         # row data
print(process3.stdout)

"""
Redirect the output to the file. 
"""

# with open('output.txt', 'w') as f:
#     process4 = subprocess.run(['ls', '-la'], stdout=f, text=True)
#     # now check the output file

"""
let us try to list the directory which is not exist
"""

process5 = subprocess.run(['ls', '-la', 'fack/path'], capture_output=True, text=True)
print(process5.returncode)      # here, python just sent the non zero exit code.
                                # means, code does not work properly
print(process5.stderr)          # will send an error code


"""
How to bypass an error 
"""
process6 = subprocess.run(['ls', '-la', 'fack/path'], stderr=subprocess.DEVNULL)
print(process6.stderr)      # None
