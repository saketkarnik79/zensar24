import threading
import requests


urls = [
    "https://zensar.com",
    "https://python.org",
    "https://github.com",
    "https://abcdefg.com/"
]

def scrape(url):
    response = requests.get(url)
    print(url, response.status_code)

threads = []

for url in urls:
    t = threading.Thread(target=scrape, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()