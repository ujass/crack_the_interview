"""
First class function:
    - It allow us to treat function like any other object. 
    - we can pass functions as argument to another function. 
    - we can return functions 
    - we can assign functions to variables. 

Closure allows us to take advantage of the first class function ans return an inner 
function that remembers and has access to variable of local scop which they have created. 

Decorator: 
    - It is just function which takes another function as an argument, add some functionality 
    and return another function. All of this without altering the source code of the original
    function that we passed in. 
"""
 
# Lets learn about a decorator, it is almost same as we learn in closure. 
def decorator_function(message):
    def wrapper_function():
        print(message) 
    return wrapper_function 

# OMG!!! It is exactly same... 
# Now, when we pass the function in decorator and insted of just printing, 
# we execute it and return it... 

"""
Example - 1
"""
print("First example started...")
# This is the simplest decorator. 
def decorator_function(origianl_function):
    def wrapper_function():
        origianl_function() 
    return wrapper_function


def display():
    print('Display function run') 

display_decorator = decorator_function(display) 
# we passed display to the decorator and we got the wrapper_function 
# which is waiting for execution. 

display_decorator()

"""
Why would we want to do somethin like this? 
- Decorating our functions allows us to easily add functionality to our existing functions.
- and we can add that functionality inside our wrapper. 

"""

"""
Example - 2
"""
print("\n \nSecond example started...")

def decorator_function(origianl_function):
    def wrapper_function():
        print('Wrapper executed before {}'.format(origianl_function.__name__))
        origianl_function() 
    return wrapper_function


def display():
    print('Display function run') 

display_decorator = decorator_function(display) 
display_decorator() 

"""
@decorator_function 
def display():
    print('Display function run')  

But, we want something like this right?? 
- Actually we did the same thing, but in conceptual level. 
- let me rewrite the method again. 
"""

print('\n \nThird example started...') 

# This is decorater. just with 2 line. 
display = decorator_function(display) 
display()  

print('\nDecoration started...') 

# and this is what we were looking for. 
# this is same as what we did 4 line above.
@decorator_function             # decorator function, where we pass display2 function
def display2():                 # now our display2 change to the returned wrapper function
                                # who is waiting for execution. 
    print('Second display function') 

display2() 

"""
@decorator_function
def display2():            ==   display2 = decorator_function(decorator_function)

both left and right are the same thing..

Basically, once i put the decorator above the function, the orginal function is no more 
original function, it is the wrapper function. (sometimes wrapper is waiting for execution
or sometime it executed directly. it depends on the requirement.)

how can we say that display2 is not become the wrapper after placing the decorator
above it??? 
""" 

print('\n \nThird example start...') 

@decorator_function
def display_info(name, age):
    print('display_info run with argument {} and {}'.format(name,age)) 

# this is how we can prove it. 
print("Name of display_info after placing decorator is= {}".format(display_info.__name__))

# now, i am saying display_info is no more display_info it is wrapper. 
# let's try to run it and pass arguments to it. 
display_info('ujesh', 24)

# check the output, it must throw an error.
# because our original function takes 2 argument and wrapper takes no arguments.  

""" 
That is why we need to pass *args * **kwargs in our wrapper function, so it allows
us to set any arbitary number of positional or keyword argument for our functions. 

Now, let us do that example in another file. concep2.py
""" 

