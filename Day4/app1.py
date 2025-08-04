
from demo1 import Logger

def add(a,b):
    return a+b

if __name__ == '__main__':
    log = Logger().get_logger()
    log.debug("This is a debug log")
    print(add(23,45))