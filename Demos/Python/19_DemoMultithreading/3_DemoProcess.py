from multiprocessing import Process
import os

def worker():
    print(f"Process ID = {os.getpid()}")

if __name__ == "__main__":
    for _ in range(3):
        p = Process(target=worker)
        p.start()

    # wait for all processes to finish
    p.join()