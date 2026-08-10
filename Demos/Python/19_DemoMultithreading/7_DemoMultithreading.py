import threading
import requests


def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    print(response.json()["name"])

threads = []

for i in range(1, 10):
    t = threading.Thread(target=fetch_user, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()