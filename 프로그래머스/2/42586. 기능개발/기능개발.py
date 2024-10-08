from collections import deque

def solution(progresses, speeds):
    answer = []
    
    prog = deque(progresses)
    spds = deque(speeds)
    
    while prog :
        while prog[0] < 100 :
            for i in range(len(prog)) :
                prog[i] += spds[i]
                
        ans = 0
        while prog and prog[0] >= 100 :
            prog.popleft()
            spds.popleft()
            ans += 1
            
        answer.append(ans)
    
    return answer