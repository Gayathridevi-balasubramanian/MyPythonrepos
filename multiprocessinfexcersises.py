import threading
from multiprocess import Process
import time

def longSquare(num):
    time.sleep(1)
    print(num**2)
    print('this is process')

p1  = Process(target = longSquare , args= (1,))

p1.start()
p1.join()
