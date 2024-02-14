import time
import random

def waiting_game():
    target = random.randint(2,4) # target seconds to wait
    print(f'\n Your target time is {target} seconds')
    

    input(' ---Press Enter to Begin--- ')
    start = time.perf_counter()

    input(f'\n ...Press Enter again after {target} seconds...   ')
    elapsed = time.perf_counter() - start

    print(f'\n Elapsed time : {elapsed:.3f} seconds')
    if elapsed == target:
        print('Unbelivevable! Perfect timing')
    elif target < elapsed:
        print(f'{target - elapsed:.3f} seconds too slow')   #.3f gives 3 floating point value after the decimal
    else:
        print(f'{target - elapsed:.3f} seconds too fast')

waiting_game()
