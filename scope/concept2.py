"""
How do we know python first go with local scope and then builtin scope.

"""

# lets import the builtin vairabls.
import builtins 

print(dir(builtins)) 

"""
Now let's do some overriding on builtin.
"""
print('\n\nSecond example started...')
# built in min return the min element from the iterator
print(min([1,2,3,4,5]))
# but this overriding do notthing...
def min():
    pass   

# print(min([1,2,3,4,5]))     # error


"""
let us do this thing with another example
"""
print('\n\nThird exaple started...')
def my_max():
    pass 

print(max([12,3,4,5,3,4]))          # this will not find the max in the global scope 
                                    # directly go to the builtin scope
                                    # ans pass the iterator in builtin function.
