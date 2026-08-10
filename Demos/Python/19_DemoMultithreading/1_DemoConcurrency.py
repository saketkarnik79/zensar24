import threading
import time

def task(name):
    for i in range(5):
        if i==1:
            print(f"Stert time of thread {name} is: {time.time()}")
        print(f"{name} working {i}")
        time.sleep(1)

t1 = threading.Thread(target=task, args=("Task-1",))
t2 = threading.Thread(target=task, args=("Task-2",))

start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Completed in {time.time()-start:.2f} seconds")
