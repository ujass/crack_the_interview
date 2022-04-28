"""
Let us use multi decorator in our for our functions. 
"""

def my_logger(orginal_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orginal_func.__name__), level=logging.INFO) 

    def wrapper_logger(*args, **kwargs):

        # when i put * & ** ahead of args & kwargs in format,age was considering as keyward arg.
        # when i remove it then both name, age was considering as args.
        logging.info('Run with args: {} and kwargs: {}'.format(args,kwargs)) 
        return orginal_func(*args, **kwargs) # at this point orginal function run

    return wrapper_logger   # return without calling so, we can run it later. 


def my_timer(orginal_func):
    import time
    def wrapper_timer(*args, **kwargs):
        t1 = time.time() 
        result = orginal_func(*args, **kwargs) 
        t2 = time.time() - t1 
        print('{} run for time = {}'.format(orginal_func.__name__, t2)) 
        return result 

    return wrapper_timer 

@my_logger
@my_timer
def display_info(name, age):
    print('Running display info with argument = ({}, {})'.format(name, age))

"""
Above decorator stacking is axactly same as 
display_info = my_logger(my_timer(display_info))

- inner decorator runs first or decorator stack run from bottom to top. 
""" 

display_info('ujesh', 24)   # Terminal output is fine. but check it created wrapper.log

"""
Why does this happend? 

- because @mytimer wraped original function and return wrapper. 
- then @my_logger wrapped wrapper rerturned by @my_timer. 

let us check how this thing happend. 
"""

# wrap fuction with only @my_time. 
one_decorator = my_timer(display_info) 

print('Name of func after 1 decorator {}'.format(one_decorator.__name__)) 

# wrap function with 2 decorator
two_decorator = my_logger(my_timer(display_info)) 
print('Name of the function after 2 decorator {}'.format(two_decorator.__name__)) 

"""
so, this is the proble. so how do we solve this? 
- use wrap from functools
""" 

print('\n\nThird - use wraps from functools...')
from functools import wraps
def my_logger(orginal_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orginal_func.__name__), level=logging.INFO) 

    @wraps(orginal_func)
    def wrapper_logger(*args, **kwargs):

        # when i put * & ** ahead of args & kwargs in format,age was considering as keyward arg.
        # when i remove it then both name, age was considering as args.
        logging.info('Run with args: {} and kwargs: {}'.format(args,kwargs)) 
        return orginal_func(*args, **kwargs) # at this point orginal function run

    return wrapper_logger   # return without calling so, we can run it later. 


def my_timer(orginal_func):
    import time

    @wraps(orginal_func)
    def wrapper_timer(*args, **kwargs):
        t1 = time.time() 
        result = orginal_func(*args, **kwargs) 
        t2 = time.time() - t1 
        print('{} run for time = {}'.format(orginal_func.__name__, t2)) 
        return result 

    return wrapper_timer  


@my_logger
@my_timer
def display_info(name, age):
    print('Running display info with argument = ({}, {})'.format(name, age))


# wrap fuction with only @my_time. 
one_decorator = my_timer(display_info) 

print('Name of func after 1 decorator {}'.format(one_decorator.__name__)) 

# wrap function with 2 decorator
two_decorator = my_logger(my_timer(display_info)) 
print('Name of the function after 2 decorator {}'.format(two_decorator.__name__)) 
 
display_info('ujesh', 24)       # this is log in display_info file. 


##############  Congratulations !!! You learned about decorators ###################