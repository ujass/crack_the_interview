"""
Chain :- Combine all iterables one after another.
""" 
import itertools
letters = ['a', 'b', 'c'] 
numbers  = [1,2,3] 
names = ['ujesh', 'jay', 'keval'] 

combine = letters + numbers + names  # inefficient when millions of records. 

combined = itertools.chain(letters, numbers, names) 
print(*combined)
