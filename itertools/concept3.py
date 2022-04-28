"""
Permutation: Group the certain number of items where order does matters.
Combinations: Group the certain number of iterms where order does not matters. 

"""
import itertools
letters = ['a', 'b', 'c', 'd'] 

result1 = itertools.combinations(letters, 2) 
print(*result1)
print(*result1)     # exhausted, now we can not iterate this.  

result2 = itertools.permutations(letters, 2) 
print(*result2) 

"""
Note: 
- Combination & permutation does not allows repetation itself. 
- what if we want repeatation? - combinations_with_replacement is the solution.
""" 
print("\n\nExample 2 started... - combination_with_replacement")
# print all 3 digit number combinatin with repeatation. 
numbers = [1,2,3] 
result3 = itertools.combinations_with_replacement(numbers, 2) 
print(*result3)     # print all combination with repeated numbers.  


"""
Product - cartesian product of iterable.
"""
print('\n\nExample 3 started... - Cartesian Product') 
result3 = itertools.product(numbers, repeat=2) 
print(*result3)