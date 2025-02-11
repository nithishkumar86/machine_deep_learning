from logger import logging

def add(a,b):
    logging.debug("addition opearation is calling")
    return a+b

logging.debug("answer is generated")
add(18,14)