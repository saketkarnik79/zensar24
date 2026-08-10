import threading
import time

def load_file(filename):
    print(f"Loading {filename}")
    time.sleep(3)
    print(f"{filename} loaded")

start = time.time()

threads = []

for file in ["file1", "file2", "file3"]:
    t = threading.Thread(target=load_file, args=(file,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Total Time:", time.time() - start)