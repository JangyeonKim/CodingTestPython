def solution(array, commands):
    answer = []
    
    for s, e, i in commands :
        s-= 1
        i-=1
        
        temp = array[s:e]
        answer.append(sorted(temp)[i])
    
    return answer