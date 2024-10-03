from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue = deque([[y, answer]])
    
    while queue :
        cur_value, cnt = queue.popleft()
        if cur_value <= 0:
            break
        if cur_value == x :
            return cnt
        
        if cur_value % 2 == 0 :
            queue.append([cur_value//2, cnt+1])
        if cur_value % 3 == 0 :
            queue.append([cur_value//3, cnt+1])
        queue.append([cur_value-n, cnt+1])        
    
    return -1