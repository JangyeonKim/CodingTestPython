from collections import deque

def discriminate(process, queue) :
    for q in queue :
        if q[0] > process[0] :
            return False # 우선순위가 더 높은 프로세스가 있으면 false 리턴
    return True # 없으면 true 리턴


def solution(priorities, location):
    answer = 0
    
    queue = [[x, idx] for idx, x in enumerate(priorities)]
    queue = deque(queue)
    
    while True :
        process = queue.popleft()
        
        if discriminate(process, queue) :
            answer += 1
            if process[1] == location :
                return answer
        else :
            queue.append(process)
                
    
    
    return answer