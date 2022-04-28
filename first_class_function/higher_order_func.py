"""
Part 2 of - First class function. 
Topic - Pass function as an argument.


What is higher order function.?
- When function accepts other functions as arguments / return functions as their result, 
  that is called higher order function.

*   Great example is built in map function which take function as argument & array of numbers
    and run this function on each item of the array and return the result. 
"""

"""
1. Pass function as an argument.
"""
def square(x):
    return x*x 

def cube(x):
    return x*x*x

# This is our custom map function which takes function & array list
# Run function on each item ans return the answer.
def my_map(func, arg_list):
    result = [] 
    for i in arg_list:
        result.append(func(i)) 
    return result 

arr = [1,2,3,4,5]

#           Pass without paranthesis.
squares = my_map(square, arr) 
print(squares) 

    

        
        

