import concept      # Do not worry about yellow line. and run this file. 


print("Concept 2 file name is {}".format(__name__))         # __main__ when run this file

# check the output, now the file name should be concept. 
# now, it is no longer main file it is imported file and it's name is file name. 

"""
Then what is main? 

- when python run a file it sets some variables before running anything. 
- and name is one of its special variable.  
- when python runs python file then first python file which we run it's name will be 
    set to = __main__


Why do we use this? 
- Sometimes we want to run different code, when it is imported and different code when 
    running directly.
"""


# If anyhow we want to run the main of concept then into concept 2. then possible.
# concept.main()