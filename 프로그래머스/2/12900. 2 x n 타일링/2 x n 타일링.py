def solution(n):
    if n <= 2:
        return n
    
    num = [1, 2] + [0] * (n-2)
    
    for i in range(2, n) :
        num[i] = (num[i-1] + num[i-2])% 1000000007
    
    return num[-1] 