def solution(n):
    answer = 0
    
    for i in range(1, n//2 + 1) :
        ans = 0
        while True :
            ans += i
            i+= 1
            if ans > n :
                break
            elif ans == n :
                answer += 1
                break
    
    return answer+1