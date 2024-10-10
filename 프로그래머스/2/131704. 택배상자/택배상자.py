from collections import deque

def solution(order):
    answer = 0
    
    n = len(order)
    queue = deque(order)
    stack = []
    
    box = 1
    while queue :
        target = queue.popleft()
        
        while True :
            if stack and stack[-1] == target :
                break
            stack.append(box)
            box += 1
            if box > n :
                break
        
        if stack[-1] != target :
            return answer
        
        stack.pop()
        answer += 1

    return answer