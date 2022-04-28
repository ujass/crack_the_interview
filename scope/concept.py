"""
LEGB 

Local       Enclosing       Global      Built-in 
1st check   then here       then here   then here       


Function creates it own local scope.
- variables which are defines in the functions are not available to use outside function.
""" 

# First let learn about local & global variabls.
x = 'global x' 

def test():                                         #               _____
    y = 'local y'                                   #                 |
                                                    #                 |
    print(y)        # 'local y' will be printed                       |  <- local scope for y
    print(x)        # 'global x' will be printed                      |
                                                    #               ------

test() 

#print(y)        # this will throw an error, because it could not find in LEGB scope 

"""
How can we say that, variable fist try to find the local & then global

"""
print('\n\nSecond example started...  (local then global)') 

z = 'global z' 

def test2():

    global z            # uncomment this if we want to work with the global z
                        # this will update the global z with local z
    z = 'local z' 
    print(z)            # 'local z' 

test2() 
print(z) 


