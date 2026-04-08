queue = [10, 20, 30]

if len(queue) == 0:
    print("Queue underflow! cannot dequeue")
else:
    removed = queue.pop(0)
    print("dequeued element: ", removed)

print("Queue after dequeue: ", queue)
