"""
Here we will learn how to make custom iterator which we can use as builtin range. 
Vidoe source = https://www.youtube.com/watch?v=jTYiNjvnHZY
"""

"""
1. with help of the function.  
-Yeild is generator which has iter & next method inside it. 
-so we do not need to explicitly care about it. 
"""

def my_range(start, end):
    current = start 
    while current < end:
        yield current 
        current += 1 

nums = my_range(1,10)

for n in nums:
    print(n)   


"""
2. Custom range function by using the methods of iter & next in our class. 
""" 

class MyRange:

    def __init__(self, start, end):
        self.value = start 
        self.end = end  

    # this gives us iterator object 
    def __iter__(self):
        return self 

    # corey used __next__ // but i think in python 3.9 this changed to next only.
    def next(self):
        if self.value >= self.end:
            raise StopIteration 

        current = self.value 
        self.value += 1 
        return current  

numbers = MyRange(1,5)

for n in numbers:
    print(n)
