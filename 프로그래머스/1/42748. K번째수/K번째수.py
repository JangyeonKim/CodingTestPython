def solution(array, commands):
    answer = []
    
    for c in commands :
        i, j, k = c[0], c[1], c[2]
        
        temp_list = array[i-1 : j]
        answer.append(sorted(temp_list)[k-1])
    
    return answer