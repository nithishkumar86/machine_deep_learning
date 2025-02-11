#process that are executed parallely
#its going to be executed in process with both this process is separate memory
import multiprocessing
import multiprocessing.process
import time

def squared_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers {i*i}")


def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"numbers {i*i*i}")

if __name__=='__main__':

    t1=multiprocessing.Process(target=squared_numbers)
    t2=multiprocessing.Process(target=cube_numbers)

    print(id(t1))
    print(id(t2))

    print(t1)
    print(t2)

    t=time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finished_time=time.time()-t
    print(f"the execution is finished {finished_time}")