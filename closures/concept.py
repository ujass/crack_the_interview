"""
First class function:
    - It allow us to treat function like any other object. 
    - we can pass functions as argument to another function. 
    - we can return functions 
    - we can assign functions to variables. 

Closure allows us to take advantage of the first class function ans return an inner 
function that remembers and has access to variable of local scope which they have created.
"""


"""
Example - 1
"""

def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)      # This is actually called free variable. Why ???
                            # because we have not define message in inner_func but still 
                            # it can access the message variable.
                            # so, this message consider as a free variable.

    return inner_func() 

print("Example 1 started...")
outer_func() 

"""
Example - 2.
Now let us just not execute the inner_func instead just return it. 
"""

print('\n \nSecond example started...') 

def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)   

    return inner_func 

my_func = outer_func()  # now, my_func store the inner_func 

# let us check 
print(my_func)              # Adderess of the funciton. 
print(my_func.__name__)     # print the name of the function. 

# let's run this just as a function. 
my_func()       # output = 'Hi' 

# This is the magic, we are done with the execution of our outer function ans return inner_func
# And, inner_func still has access to the message variable. --- this is closure.  

"""
what is closure in simple term ???
- A closure is an inner function that remembers and has access to the variables in the local
    scope, in which it was created, even after the outer function has finish execution.

- "A closer closes over a free variable from its environment"
""" 


"""
Example - 3. 
set custom variable to the outer_func.
""" 

print("\n \nThird example started...") 

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)   

    return inner_func  

hi_func = outer_func('hi') 
hello_func = outer_func('Hello')
 
hi_func() 
hello_func()  

"""
Example - 4 
""" 

print("\n \nFourth example started...") 

def outer_func(msg):
    def inner_func():
        print(msg)          # we do not need to store the msg in variable 
                            # we can directly pass it to the inner_func

    return inner_func   


hi_msg = outer_func('hi') 
bye_msg = outer_func('bye') 

hi_msg()
bye_msg() 