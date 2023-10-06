from collections import deque

def bigger(pri, process) :
    for p in pri :
        if p[1] > process[1] :
            return True
    return False

def solution(priorities, location):
    
    prior = []
    for idx, p in enumerate(priorities) :
        prior.append([idx,p])
    
    pri = deque(prior)
    ans = deque()
    
    while pri :
        process = pri.popleft()

        if bigger(pri, process) :
            pri.append(process)
        else :
            ans.append(process)
    
    for a in ans :
        if a[0] == location :
            answer = ans.index(a) + 1
    
    return answer