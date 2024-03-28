def solution(n):
    answer = 1
    
    for i in range(1, n) :
        nn = i
        for j in range(i+1, n+1) :
            nn += j
            if nn == n :
                answer += 1
                break
            if nn > n :
                break
    
    return answer