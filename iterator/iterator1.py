"""
dir(x) can be used to check what methods are available for x.

-Iterator is object with state, means it remember where it is. 
so when we run next if gives us the next result.
-list are iterable but it is not iterator, we need to fetch its iterator object from iter()
which we can iter afterwards.check what methods are available for x.
list are iterable but it is not iterator, we need to fetch its iterator object from iter()
 which we can iter afterwards.
"""

nums = [1,2,3] 

# check how many methods are avialable for nums. 
print("list methods are = ",dir(nums)) 

# # This is fatched by foor loop in the background 
# i_nums = nums.__iter__()


# __iter__ // using dunder methods like this is bit ugly for practice.
# so, we have fuction to fetch the same value. 
i_nums = iter(nums)


print(next(i_nums))     # 1  
print(next(i_nums))     # 2 
print(next(i_nums))     # 3  
# print(next(i_nums))     # Exception - StopIteration


"""
Foor loop does this things in background.
1. it gets the iter object of the list which has next method to loop over the numbers. 
2. it keeps looping over the object untill it hits the StopIteration exception. 
3. this can only go forward, it can not go backward. 
"""
 
numbers = [11,22,33] 
i_number = iter(numbers)
while True: 
    try: 
        item = next(i_number) 
        print(item) 
    except StopIteration:
        break 






# # Now this has next method
# print("iter methods are = ", dir( i_nums))

range 

"""
 list object is not an iterator 
 next can only run iterator
"""
# print(next(nums))