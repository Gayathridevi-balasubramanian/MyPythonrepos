'''#custom exception
class customException(Exception):
    pass

def causeError():
    # raise customException('this is also a sample')
    raise customException('this is the statement sent to the class')

causeError()
'''
############
class HttpException(Exception):
    message = None
    status = None
    def __init__(self):
        super().__init__(f'the status code is : {self.status} and the message is : {self.message}')

class notFound(HttpException):
    message  = ' No data found'
    status = 103

class serverError(HttpException):
    message = 'Server Error'
    status = 404



class raiseServerError():
    raise serverError()



    