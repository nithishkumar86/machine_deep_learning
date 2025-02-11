from concurrent.futures import ProcessPoolExecutor
import time

def print_numbers(number):
        time.sleep(2)
        return f"numbers {number*number}"

numbers=[1,2,3,4,5,6,4,5,7,8,9,4,5]


if __name__=='__main__':
    with ProcessPoolExecutor(max_workers=3) as executer:
        results=executer.map(print_numbers,numbers)

    for result in results:
            print(result)