import logging 

# INFO is constant behind the logging module. 
# debug < info < warning < criticle. 
# all the level has assigned with a constant number in code. 
logging.basicConfig(filename=__name__, level=logging.INFO,
                    format='%(levelname)s:%(message)s') 

def add(a,b):
    return a + b 

logging.info(add(7,8)) 

a,b,*c = (1,2,3,4,5) 
print(a,b,c)