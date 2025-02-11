#multithreading with thread pool executor
from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
        time.sleep(2)
        return f"numbers {number}"

numbers=[1,2,3,4,5,6,4,5,7,8,9,4,5]

with ThreadPoolExecutor(max_workers=3) as executer:
    results=executer.map(print_numbers,numbers)

for result in results:
        print(result)