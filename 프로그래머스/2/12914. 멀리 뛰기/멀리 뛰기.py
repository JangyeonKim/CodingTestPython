def solution(n):
    
    if n <= 2 :
        return n
    
    arr = [1, 2] + [0]*(n-2)
    
    for i in range(2, len(arr)) :
        arr[i] = arr[i-2] + arr[i-1]
    
    
    return arr[-1] % 1234567