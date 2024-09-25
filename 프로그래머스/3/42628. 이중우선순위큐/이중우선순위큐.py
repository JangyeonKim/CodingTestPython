def solution(operations):
    answer = []
    
    for oper in operations :
        op, num = oper.split()
        
        if op == 'I' :
            answer.append(int(num))
            answer.sort()
        else :
            if answer and num == "1" :
                answer.pop()
            elif answer and num == "-1" :
                answer.pop(0)
                
    if not answer :
        return [0, 0]
    else :
        return [max(answer), min(answer)]