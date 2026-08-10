import threading

def worker():
    print(f"Thread running")

for _ in range(3):
    t = threading.Thread(target=worker)
    t.start()