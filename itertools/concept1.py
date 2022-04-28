import itertools 

counter  =itertools.count() 

# count is helpful to count the numbers, default start with 0 & step is 1. 
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 


# let's start with 5 & step with 5. 
print("\n\nExample 2")

counter1 = itertools.count(start=5, step=5) 

print(next(counter1)) 
print(next(counter1)) 
print(next(counter1))        # 5,10,15


"""
Let's loop over the numbers with count 
"""
print("\n\nExample 3 started...") 
counter3 = itertools.count()  

nums = [10,20,30,40,50] 
nums_with_counter = (zip(counter3, nums)) 
print(nums_with_counter)    # zip return zip object, we need conver it into list.  

"""
we can do this in two ways... 

"""
# 1. loop over the zip object and get the result, but we can iterate only once. 
for i in nums_with_counter:
    print(i) 

# Below will not give any result.
for i in nums_with_counter:
    print(i)


# 2. convert it into list. 
nums_with_counter2 = list(zip(counter3, nums))  

print(nums_with_counter2) 
print(nums_with_counter2)   # we can use this anytime.


"""
ZIP - what is it?? 

it will zip 2 iterators till the iterators are common. 
zip end with the shortest iterable.
Ex. num1 = [11,12,13,14,15]
    num2 = [21,22,23]

    zip(num1,num2) = [(11,21), (12,22), (13,23)]
"""
print("\n\nExample 4 started...  - ZIP wiht list")

num1 = [11,12,13,14,15] 
num2 = [21,22,23] 
print(list(zip(num1, num2))) 

"""
Zip_longest - it zip the iterables till the longest iterable is exhausted. 

- when other iterables are exhusted then it add None for those pairs of data.
""" 

print("\n\nExample 5 started... - ZIP longest") 

print(list(itertools.zip_longest(num1, num2)))