def solution(elements):
    sum_arr = elements + [sum(elements)]
    # print(sum_arr)
    
    for i in range(2, len(elements)) :
        arr = elements + elements[:i-1]
        # print(arr)
        
        for j in range(len(elements)) :
            sum_arr.append(sum(arr[j:j+i]))
            
    answer = len(set(sum_arr))
    
    return answer