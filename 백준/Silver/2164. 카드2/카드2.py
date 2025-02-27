from collections import deque

N = int(input())

queue = deque([x for x in range(1, N+1)])

while len(queue) > 1 :
    queue.popleft()
    if len(queue) == 1:
        break
    
    queue.append(queue.popleft())
    
print(queue.popleft())