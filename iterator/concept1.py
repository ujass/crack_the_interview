"""
Iterable & iterators both are different. 
Ex. List are iterable but it is not iterator. 


So, what is iterable? 
- something on which we can loop over then it is iterable.

But when we can loop over?
- if anyone has __iter_() method then we can loop over it. 
"""

nums  = [1,2,3,4,5] 

for n in nums:
    print(n) 

# we know this is list and we defenately loop over it. 
# let's check whether it has __iter__() method or not. 
print(dir(nums))        # check output it is __iter__() method there. 

"""
What is for loop doing in the background? 
- It is calling __iter__() in the background, which returns the iter object.
- After that for loop over this object. 


Now, we know that list is iterable but not iterator, 
when we run __iter__() method on list, it returns iterator object. 
Now this object is responsible for iteration. 


What is iterator?
-Iterator is object with a state, which remembers it state during iteration.
- it also know how to get the next value (this is done with __next__())
"""