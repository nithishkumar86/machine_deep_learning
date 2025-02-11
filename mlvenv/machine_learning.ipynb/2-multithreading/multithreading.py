import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers {i}")

def print_letters():
    for i in "abcde":
        time.sleep(2)
        print(f"letters {i} ")


t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)

print(id(t1))
print(id(t2))

print(t1)
print(t2)

t=time.time()

t1.start()
t2.start()

t1.join() #Wait until the thread terminates.
t2.join()

finished_time=time.time()-t
print(f"the execution is finished {finished_time}")