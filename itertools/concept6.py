"""
Filter : same as map, takes iterable and function to filter.
""" 
import itertools
import operator 
print("Example 1 started... - Filter ") 

def lessThan2(n):
    return True if n < 2 else False 

numbers = [0,1,2,3,4]
results = filter(lessThan2, numbers) 
print(*results)
 
"""
accumulate : It is the prefix sum of the iterables. 
""" 
print("\n\nExample 2 started... - Accumulate = prefix sum")
prefix  = itertools.accumulate(numbers) 
print(*prefix) 

"""
Operator: it has different opeators like *, +, pow
""" 
print('\n\nExample 3 started... - operator + accmulate')
numbers1 = [1,2,3,4,5]
prefix_mul = itertools.accumulate(numbers1, operator.mul) 
print(*prefix_mul)

