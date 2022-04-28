import multiprocessing
import time 

start = time.perf_counter() 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s') 
    time.sleep(seconds) 
    print('Done sleeping...') 


"""
Below part is without multiprocessing. 
"""
# do_something() 
# do_something()


"""
Below part is showing about the multiprocessing example. 
"""
# we just need to assign the orginal function, no need to call
# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something) 

# p1.start() 
# p2.start() 

# p1.join() 
# p2.join() 

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5]) 
    p.start() 
    processes.append(p) 


for process in processes:
    process.join()  

finish = time.perf_counter() 
print(f'Finish in {round(finish-start, 2)} second(s)')