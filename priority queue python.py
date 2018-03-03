import queue

q = queue.PriorityQueue()

q.put(10)
q.put(1)
q.put(15)

while q.empty() is not None:
    print (q.get())
