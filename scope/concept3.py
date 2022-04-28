"""
Enclosing scope can be achieved by the nested function
""" 

def outer():
    x = 'outer x'       # this x is local for outer function

    def inner():
        x = 'inner x'   # local to inner function 
        print(x)        # if it could not find the local then it immediatly find
                        # local scope of x with any enclosing function.
    inner() 
    print(x) 

outer() 

"""
We can change the x as we changed local / global variables. 

""" 
print('\n\nSecond example... (Enclosing variable)')

x = 'global2 x'     # this will be unaffected 

def outer2():
    x = 'outer2 x' 

    def inner2():
        # nonlocal x          # this will change the value of enclosing varialbes only.
        x = 'inner2 x' 
        print(x) 

    inner2() 
    print(x) 

outer2() 
print(x)