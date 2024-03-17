import time
import sched

''' the schedular function is to schedule some event 
    1. import sched
    2. schedule_function() 
        create schedular object with the 2 parameters time_func, delay_func
        use enterabs() to enter into the queue
        run the scheduler
    3. define function'''
def schedule_function(event_time, function, *args):
    
    current_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print("The current time is ",formatted_time,"and the function is scheduled after ",event_time,"seconds")
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time ,1 , function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()
def test(a, b):
    print("The answer of the function test is : ",a+b)

schedule_function(time.time() + 1 , print, 'HOWDY!! How are you')

schedule_function(time.time() + 7 , test, 4, 56)
