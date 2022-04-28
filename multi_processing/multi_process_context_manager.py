import concurrent.futures
import time 

start = time.perf_counter() 

def do_something(seconds):
    print(f'Sleeping {seconds} second(s') 
    time.sleep(seconds) 
    return f'Done {seconds} sleeping...'


with concurrent.futures.ProcessPoolExecutor() as executor: 

    secs = [5,4,3,2,1]
    result = [executor.submit(do_something, sec) for sec in secs]


    # we can also get the process back once they are finish... 
    # Check in terminal 1 sec process finish after the 2&3. 
    # It is because my computer might have 4 core so it started 5,4,3,2 first and then 1. 
    for f in concurrent.futures.as_completed(result):
        print(f.result())

    """
    Below code is to know how we can use ProcesssPoolExucutor for submitting our process
    as we have seen in multoprocessing module. 
    """
    # # submit line up the process to execute.. 
    # # here f1, is a future object we can use it lator to know the process is running, or finish
    # f1 = executor.submit(do_something, 1)

    # # let us fetch the result of the f1 process 
    # print(f1.result())
    

finish = time.perf_counter() 
print(f'Finish in {round(finish-start, 2)} second(s)')