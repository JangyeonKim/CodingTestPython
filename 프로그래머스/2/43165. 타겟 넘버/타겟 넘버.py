def solution(numbers, target):
    answer = [0]
    
    for n in numbers :
        temp = []
        for ans in answer :
            temp.append(ans + n)
            temp.append(ans - n)
        answer = temp
    
    return answer.count(target)