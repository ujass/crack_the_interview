print(__name__)     # __main__

print("Concept 1 file name is {}, always run".format(__name__))   # __main__ when run this file

""" 
Now, let us create another file with concept 2 and name it with the concept 2. 
and import concept 1 and run concept 2 file. 
""" 

# Below part will not run when we import this file to somewhere else. 
def main():
    print("Concept 1 file name is {}, only run with main method".format(__name__)) 


# Basically, below checks that this file is directly run by the python. 
# then & then run the main method...
if __name__ == '__main__':
    print("Run directly")
    main()
else:
    print("Run from imported") 


