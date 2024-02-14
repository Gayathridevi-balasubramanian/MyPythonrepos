import threading
import time

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
t1 = threading.Thread(target=longSquare, args=(1, results))
t2 = threading.Thread(target=longSquare, args=(2, results))

t1.start()
t2.start()

t1.join()
t2.join()
print(results)


''''
 threading procedure  -- process has threads.. 
import threading 
declate a dictionary
define a function 
use the treading.threads function with parameters as target , args  
start the threads using start()
join the threads using the join() function 

'''

results = {}
# Dynamically calling multiple threads using lists data structure
threads = [threading.Thread(target= longSquare , args= (n, results)) for n in range(1,100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
            
