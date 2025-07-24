'''theading'''
import threading
import time

def worker():
    print("Thread starting.")
    time.sleep(1)
    print("Thread finished")

# Create and start a thread
t = threading.Thread(target=worker)
t.start()
t.join() # Wait for thread to finish
# Use for I/O bound tasks like downloading files, reading sockets, etc.


'''concurrent.futures'''
# Threadpool Executor
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4])
    print(list(results)) # [1, 4, 9, 16]

# ProcessPool Executor
from concurrent.futures import ProcessPoolExecutor

# For CPU-bound tasks
with ProcessPoolExecutor() as executor:
    results = executor.map(square, range(5))
    print(list(results)) # [0, 1, 4, 9, 16]
# ThreadPoolExecutor for I/O, ProcessPoolExecutor for CPU-intensive work


'''multiprocessing'''
from multiprocessing import Process

def compute():
    print("Running in a separate process")

if __name__ == "__main__":
    p = Process(target=compute)
    p.start()
    p.join()
# This runs in a separate Python process - True parallel execution.


'''asyncio'''
import asyncio

async def task(name):
    print(f"{name} started")
    await asyncio.sleep(1)
    print(f"{name} done")

async def main():
    await asyncio.gather(task("Task A"), task("Task B"))

asyncio.run(main())
# Great for async web requests, socker programming or streaming.


'''queue'''
import queue
import threading
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(0.5)

def consumer():
    while True:
        item = q.get()
        print(f"Consuming {item}")
        q.task_done()

# Start threads
threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()

q.join() # Wait for all items to be processed
# Safely shares data between threads, Use for producer-consumer patterns.