"""

First class function allow us to treat function like any other object. - Corey Schafer
Ex. we can assign function to variable or Pass function as an argument or 
    we can return function.

First class objects in a language are handled uniformly throughout. 
They may be stored in data structures, passed as arguments, or used in control structures. 
A programming language is said to support first-class functions if it treats functions as 
first-class objects. Python supports the concept of First Class functions. - GFG
"""

def square(x):
    return x * x 

f = square(5) 

print(square)
print(f)
 
"""
Below is the first class function behaviour. 

Simple definition of first class function: 
1. we can pass function to variable.
2. Pass functions as arguments. 
3. Return function as result. 


"""


print("First class function behaviour")

# 1. Assign function to a variable. 
f = square 

print(square) 
print(f) 
print(f(5)) 