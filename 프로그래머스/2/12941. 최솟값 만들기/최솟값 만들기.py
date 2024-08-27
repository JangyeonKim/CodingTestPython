def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    
    while A :
        a = A.pop()
        b = B.pop()
        
        answer += a*b

    return answer