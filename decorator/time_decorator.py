"""
This is a practicle example of decorator where we calculate the run time of the function. 
"""

def my_timer(orginal_func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time() 
        result = orginal_func(*args, **kwargs) 
        t2 = time.time() - t1 
        print('{} run for time = {}'.format(orginal_func.__name__, t2)) 
        return result 

    return wrapper 

@my_timer
def display(name, age): 
    print('display run with argument ({}, {})'.format(name,age)) 

display('ujesh', 24)