"""
Starting from concep.py file, 

let us add *args & **kwargs into our functions...
then we can run both the function without errros. 
"""

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed before {}'.format(original_function.__name__))
        original_function(*args, **kwargs) 
    return wrapper_function 

@decorator_function
def display():
    print('Display function run') 

display()

@decorator_function
def display_info(name, age):
    print('display_info run with argument {} and {}'.format(name,age)) 

display_info('ujesh', 24) 

"""
Now let us implemment the decorator with the class, which works exactly the same... 
"""
print('\n \nExample 3 started... decorated with class')

class decorator_class:
    def __init__(self, original_function):
        self.original_function = original_function 

    # this __call__ behaves same as the wrapper function. 
    def __call__(self, *args, **kwargs) :
        print('Wrapper executed before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)  

@decorator_class
def display3():
    print('Third display run...') 

@decorator_class
def display4(name, age):
    print('Fourth display run with argument {} and {}'.format(name, age))

display3() 
display4('ujesh', 24) 