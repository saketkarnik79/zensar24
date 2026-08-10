import threading
import time

event = threading.Event()

def waiter():
    print("Waiting...")
    event.wait()
    print("Started")

threading.Thread(target=waiter).start()
time.sleep(3)
event.set()