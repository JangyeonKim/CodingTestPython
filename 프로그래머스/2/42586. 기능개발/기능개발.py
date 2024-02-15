from collections import deque

def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses :
        while True :
            for i in range(len(progresses)) :
                progresses[i] += speeds[i]
            
            if progresses[0] >= 100 :
                break
            
        cnt = 0
        while progresses :
            if progresses[0] < 100 :
                break
            else :
                progresses.popleft()
                speeds.popleft()
                cnt+=1
        answer.append(cnt)
    return answer