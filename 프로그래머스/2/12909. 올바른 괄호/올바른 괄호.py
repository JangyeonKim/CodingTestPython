from collections import deque

def solution(s):
    if s.startswith(")") :
        return False
    
    else :
        queue = deque(s)

        stack = [queue.popleft()]
        while queue :
            a = queue.popleft()
            if stack and stack[-1] == "(" and a == ")" :
                stack.pop()
            else :
                stack.append(a)
                
    
        return False if stack else True
            