def solution(numbers, target):
    n = numbers.pop(0)
    answer = [-n, n]
    
    for i in range(len(numbers)) :
        temp = []
        for a in answer :
            temp.append(a+numbers[i])
            temp.append(a-numbers[i])
        answer = temp
    
    return answer.count(target)