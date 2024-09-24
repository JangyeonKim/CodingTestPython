from collections import deque

def check(c, arr) :
    for a in arr :
        if a[0] > c[0] :
            return False
    return True

def solution(priorities, location):
    answer = 0
    pri = [[p, x] for x, p in enumerate(priorities)]
    
    while pri :        
        cur = pri.pop(0)
        if not check(cur, pri) :
            pri.append(cur)
        else :
            answer += 1
            if cur[1] == location :
                return answer
            
        