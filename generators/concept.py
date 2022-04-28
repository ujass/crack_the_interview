"""
Generators won't hold entire result in the memory, it yields one result at a time. 
It wait for to print next result. (we can use next method to print)
""" 

# This is return 
def square_numbers(nums):
    result = [] 
    for n in nums:
        result.append(n*n) 
    return result

my_num = square_numbers([1,2,3,4,5]) 

print(my_num)   # 1,4,9,16,25 

"""
Let's create generator object...
"""

print('\n\nGenerator concept start...') 

def square_nums(nums):
    for n in nums:
        yield n*n 

yield_nums = square_nums([1,2,3,4,5]) 

print(yield_nums)       # Generator object... 

print(next(yield_nums))     # print next number
print(next(yield_nums)) 
print(next(yield_nums)) 
print(next(yield_nums)) 
print(next(yield_nums)) 
# print(next(yield_nums))     # StopIteration exception. Exhausted entire generator. 


# Better way to pritn generator. 
for n in yield_nums:
    print(n) 

"""
[List comprehension] == (Generator comprehension)
"""
print('\n\nGenerator comprehension started...')
generator_obj = (x*x for x in [1,2,3,4,5]) 

print(generator_obj)            # generator_object 
print(list(generator_obj))      # Convert generator in to list,this creat whole list from
                                # generetor and we loose our performance here.

"""
Why we use generators? 

- it is good because it is not holding all the values in the memory 
- if we have big amount of data then it improves the performance. 
- Because it is not generating all the values at same time. 
- it generats value on the fly when we call next method...
"""