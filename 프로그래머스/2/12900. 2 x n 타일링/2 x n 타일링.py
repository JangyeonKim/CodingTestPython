def solution(n):
    if n < 2 :
        return n
    
    answer = [1, 2] + [0] * (n-2)
    
    for i in range(2, len(answer)) :
        answer[i] = (answer[i-1] + answer[i-2]) % 1000000007
    
    return answer[-1] 