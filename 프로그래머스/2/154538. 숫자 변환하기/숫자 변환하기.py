from collections import deque

def bfs(queue, x, n) :
    while queue :
        q, cnt = queue.popleft()
        if q == x :
            return cnt
        
        if q-n >= x :
            queue.append([q-n, cnt+1])
        if q%3 == 0 and q/3 >= x :
            queue.append([q/3, cnt+1])
        if q%2 == 0 and q/2 >= x :
            queue.append([q/2, cnt+1])
        
    return -1

def solution(x, y, n):
    answer = 0
    
    queue = deque([[y, 0]])
    
    answer = bfs(queue, x, n)
    
    return answer