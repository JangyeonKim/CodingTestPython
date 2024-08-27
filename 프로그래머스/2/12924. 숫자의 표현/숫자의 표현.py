def solution(n):
    answer = 0
    
    half = n//2 + 1
    
    for i in range(1, half) :
        temp = 0
        
        j = i
        while temp < n :
            temp += j
            j += 1
        
        if temp == n :
            answer += 1
    
    return answer+1