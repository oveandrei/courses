queue = []
queue.append("A")   # Enqueue: Add 'A' to the end of the queue
queue.append("B")   # Enqueue: Add 'B' behind 'A'
print(queue)        # Output: ['A', 'B']

print(queue.pop(0)) # Dequeue: Removes and returns 'A' (first in)
print(queue)        # Output: ['B']
