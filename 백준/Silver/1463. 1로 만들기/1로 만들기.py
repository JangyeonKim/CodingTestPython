from collections import deque

x = int(input())

# x -> 1

target = 1 
cnt = 0
queue = deque([(x, cnt)])

while queue :
    xx, c = queue.popleft()

    if xx == target :
        print(c)
        break
    
    if xx % 3 == 0 :
        queue.append((xx//3, c+1))
    if xx % 2 == 0 :
        queue.append((xx//2, c+1))
    if xx >= 1 :
        queue.append((xx-1, c+1))
