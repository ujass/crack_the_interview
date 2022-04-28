import logging  
logging.basicConfig(filename='example.log', level=logging.INFO) 

"""
Example 1
"""
def logger(func):

    # *args mean, we can pass any number of argument
    def log_func(*args):

        # this will log the function name nad parameter in the log file. 
        logging.info('Running {} with arguments {}'.format(func.__name__, args)) 

        # below print the return value of the function that we have passed.
        print(func(*args)) 

    return log_func 


def add(x,y):
    return x + y 

def sub(x,y):
    return x-y 

add_logger = logger(add) 
sub_logger = logger(sub) 

add_logger(3,4) 
add_logger(5,6) 

sub_logger(4,3)
sub_logger(3,2)  

"""
Example 2 
""" 
print('\n \nStarting example 2...')
def add2(*args):
    return sum(args)

add2_logger = logger(add2) 

add2_logger(1,2,3,4)