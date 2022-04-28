"""
Cycle - it runs forever on given iterable. 
"""
import itertools
print("Example 1 started... - Cycle") 

counter = itertools.cycle(('On','Off')) 

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))       
print(next(counter))    # very heplful switching & on/off. 


"""
Repeat - repeat the value infinit time.
""" 

print("\n\nExample 2 started... - Repeat") 
counter = itertools.repeat(2) 

print(next(counter))
print(next(counter))
print(next(counter))    # 2,2,2 

# How does this repeat healpful in real life? 

#           func    iterable    argument
squares = map(pow, range(10), itertools.repeat(2))  # return itertool object 
squares = list(squares) 
print(squares) 


