from collections import deque

def solution(progresses, speeds):
    answer = []
    
    com_date = []
    
    for p, s in zip(progresses, speeds) :
        calculate_date = (100 - p)
        if calculate_date % s == 0 :
            com_date.append(calculate_date // s)
        else :
            com_date.append(calculate_date //s + 1)
    
    # print(com_date) # [5, 10, 1, 1, 20, 1]
    
    cnt=0
    
    while com_date :
        # print(com_date)
        if com_date[0] <= 0 :
            com_date.pop(0)
            cnt+=1
        else :
            if cnt != 0 :
                answer.append(cnt)
                cnt=0
            com_date = [x-1 for x in com_date]
    
    if cnt != 0 :
        answer.append(cnt)
            
    return answer
    