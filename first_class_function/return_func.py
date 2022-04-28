"""
Part 3 of First class function. 
Topic - Return function 

""" 

# Logger takes msg as argument.
def logger(msg):

    # Log_message just print msg & do not take any argument
    def log_message():
        print('Log: ',msg) 

    # Logger directly return the log_message function withour executing it. 
    return log_message 

# log_hi will hold, what logger return. 
# it return the function, then it will hold the function. 
log_hi = logger('Hi') 

# Log_hi is a function which logger returns (log_message, in this case).
# currently, log_hi = log_message, when we execute log_hi, we execute log_message.  
# Note: if log_message would taking argument then we need to pass it while executing log_hi.
log_hi()

"""
Note: we might think that, log_message has not store the value of msg. 
so, when we execute the log_hi, will it print the value of msg or not? 

well, answer is yes. It will print. (this is called the closure concept)
"""

print("First example finish here...")
print('\n')
############################################################# 
"""
This is the best practical example to learn about how returning function can make out
life easy. 

""" 

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))    # 0, 1 -> tag, msg

    return wrap_text 

# here we assign the tag h1 and pass that function to the print_h1
print_h1 = html_tag('h1')
 
# Now, here is the catch.... print_h1 hold the wrap_text which takes 1 argument.
# so, we have to pass msg to the print_h1 while executing. 
print_h1('Head line') 
print_h1('Another head line') 

# Now, let us make the another tag and print it. 
print_p = html_tag('p')
print_p("This is a paragraph")
print_p("This is another paragraph....")


print('Tutorial ends here, thanks for sticking till the end.....')