from queue import Queue
import threading

q = Queue()

def worker():
    while not q.empty():
        item = q.get()
        print(f"Processing {item}")
        q.task_done()

for i in range(10):
    q.put(i)

threads = []

for _ in range(3):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

print("Done")