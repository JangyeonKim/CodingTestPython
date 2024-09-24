from collections import deque

def solution(progresses, speeds):
    answer = []
    
    pro = deque(progresses)
    spd = deque(speeds)
    
    while pro : 
        ans = 0
        while pro[0] < 100 :
            for i in range(len(pro)) :
                pro[i] += spd[i]
            
        while pro and pro[0] >= 100 :
            pro.popleft()
            spd.popleft()
            ans += 1
            
        answer.append(ans)
            
    return answer