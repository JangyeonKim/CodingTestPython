from collections import deque

def isProcess(q, queue) :
    for qq in queue :
        if qq[0] > q[0] :
            return False
    return True

def solution(priorities, location):
    answer = 0
    
    queue = deque([])
    
    for idx, p in enumerate(priorities) :
        queue.append([p, idx])
        
    while True :
        q = queue.popleft()
        if not isProcess(q, queue) :
            queue.append(q)
        else :
            answer += 1
            if q[1] == location :
                return answer