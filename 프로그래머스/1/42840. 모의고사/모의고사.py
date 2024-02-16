def repeat(li, answers) :
    lis = []
    while True :
        lis += li
        if len(lis) >= len(answers) :
            break
    lis = lis[:len(answers)]
    
    cnt = 0
    
    for i in range(len(answers)) :
        if lis[i] == answers[i] :
            cnt += 1
    
    return cnt

def solution(answers):
    answer = []
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    f = repeat(first, answers)
    s = repeat(second, answers)
    t = repeat(third, answers)
    
    result = [f,s,t]
    max_result = max(result)
    
    for i in range(len(result)) :
        if result[i] == max_result :
            answer.append(i+1)
    
    return answer