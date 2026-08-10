from concurrent.futures import ThreadPoolExecutor

def task(num):
    return num * num

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(task, range(10))
    print(list(results))