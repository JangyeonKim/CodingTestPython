from collections import deque

def solution(s):
    
    stack = []
    queue = deque(s)
    
    while queue :
        q = queue.popleft()
        
        if stack and stack[-1] == "(" and q == ")" :
            stack.pop()
        else :
            stack.append(q)

    return False if stack else True