"""
This shows how we can take password from the user securly.
"""

from getpass import getpass
user = input() 
pas = getpass() 

print(f'User name= {user} and password= {pas}')