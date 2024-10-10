def solution(n, s):
    if n > s :
        return [-1]
    
    div = s // n
    rest = s % n
    
    arr = [div for _ in range(n)]
    
    for i in range(rest) :
        arr[i] += 1
        
    arr.sort()
    
    return arr