
import time 
def causeError():
    try: 
       1/0
    except Exception as e:
       print(type(e))

causeError()
##############
def causeError():
    try: 
       1/0
    except Exception as e:
       print(e)
       print('user message')

causeError()
##############
def causeError():
    start = time.time()
    try: 
       time.sleep(0.5)
       1/0
    except Exception:
       print(f'the time taken to execute is {time.time() - start}')
    finally:
       print(f'the time taken to execute is {time.time() - start}')

causeError()
##############
def causeError():
    try: 
      # 1/'a'
       1/0
    except TypeError:
       print('There is a type error')
    except ZeroDivisionError:
       print('There is a zero division error')
    except Exception:
       print('there is some error!')
    
causeError()


def handleException(func):
   def wrapper():
      try:
         func()
      except TypeError:
         print('There is a type error')
      except ZeroDivisionError:
         print('There is a zero division error')
      except Exception:
         print('There is some error!')
   return wrapper

@handleException
def causeError():
   1/0

causeError()

#####################
def handleException(func):
   def wrapper(*args):
      try:
         func(*args)
      except TypeError:
         print('There is a type error')
      except ZeroDivisionError:
         print('There is a zero division error')
      except Exception:
         print('There is some error!')
   return wrapper

@handleException
def raiseError(n):
   if n == 0:
      raise Exception()
   print(n)

raiseError(56)
raiseError(0)


