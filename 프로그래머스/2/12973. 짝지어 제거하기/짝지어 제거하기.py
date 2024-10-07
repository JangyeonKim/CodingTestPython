from collections import deque

def solution(s):
    
    queue = deque(s)
    stack = []
    
    while queue :
        while stack and queue and stack[-1] == queue[0] :
            stack.pop()
            queue.popleft()
        
        if queue :
            stack.append(queue.popleft())
    
    return 1 if not stack else 0