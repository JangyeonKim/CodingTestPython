from collections import deque

def solution(operations):
    answer = []
    
    oper = deque(operations)
    queue = []
    
    while oper :
        op, er = oper.popleft().split()
        
        if op == "I" :
            queue.append(int(er))
        elif queue and op == "D" and er == "-1" :
            queue.remove(min(queue))
        elif queue and op == "D" and er == "1" :
            queue.remove(max(queue))
            
    if not queue :
        return [0, 0]
    else :
        return [max(queue), min(queue)]
