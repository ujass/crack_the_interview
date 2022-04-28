"""
Islice - Slice the iterable  
"""
import itertools
result = itertools.islice(range(10), 5)     # slice result from till 5.

for item in result:
    print(item) 

#                           range  start  end 
result2 = itertools.islice(range(10), 2,5) 
print(result2)
"""
I can do this with list slice too, why do i need this?? 

- well, when we have large amount of data in iter object and just want some part of the data.
- we do not want to load whole data into the memeory and then slice. 
- at this point, islice comes into picture and win the game. 

Ex. let's open the file's top 5 line wihtout loading whole file into memery.
""" 

# file object f is actually iterator and when we apply next on it
# it gives us next line as output. 
with open('example.log', 'r') as f:
    onlyThreeLine = itertools.islice(f,3) 

    for line in onlyThreeLine:
        print(line)    



"""
Note: by default print add '\n' whenever we call print.
"""