import threading
import time

def calculate():
    total = 0

    for _ in range(50_000_000):
        total += 1

start = time.time()

t1 = threading.Thread(target=calculate)
t2 = threading.Thread(target=calculate)

t1.start()
t2.start()

t1.join()
t2.join()

print(time.time() - start)