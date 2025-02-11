import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler('app1.log'),
              logging.StreamHandler() #this is responsible for pushing a log into the file
              ]
)

def add(a,b):
    result=a+b
    logging.debug(f"addition {a} + {b} = {result}")
    return result

def subtract(a,b):
    result=a-b
    logging.debug(f"subtract {a} - {b} = {result}")
    return result

def multiply(a,b):
    result=a*b
    logging.debug(f"multiply {a} * {b} = {result}")
    return result

def division(a,b):
    try:
        result=a/b
        logging.debug(f"division {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("zero division error occured")
        return None
    

add(12,12)
subtract(10,14)
multiply(13,16)
division(10,5)