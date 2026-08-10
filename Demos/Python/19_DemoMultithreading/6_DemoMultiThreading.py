import threading
import requests


files = [
    "https://example.com/file1.zip",
    "https://example.com/file2.zip"
]


def download(url):
    response = requests.get(url)
    filename = url.split("/")[-1]

    with open(filename, "wb") as f:
        f.write(response.content)

    print(f"{filename} downloaded")


threads = []

for file in files:
    t = threading.Thread(target=download, args=(file,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()