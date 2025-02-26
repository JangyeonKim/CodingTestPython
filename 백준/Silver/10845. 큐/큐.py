import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N) :
    order = input().strip()
    if order.startswith("push") :
        order, n = order.split()
    
    if order == "push" :
        queue.append(int(n))
    elif order == "pop" :
        print(queue.popleft()) if queue else print(-1)
    elif order == "size" :
        print(len(queue))
    elif order == "empty" :
        print(1) if not queue else print(0)
    elif order == "front" :
        print(queue[0]) if queue else print(-1)
    elif order == "back" :
        print(queue[-1]) if queue else print(-1)