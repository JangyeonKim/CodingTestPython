def solution(n):
    answer = 0
    fibo = [0, 1] + [0]*(n-1)
    
    for i in range(2, len(fibo)) :
        fibo[i] = fibo[i-1]+fibo[i-2]
    
    # print(fibo)
    
    return fibo[-1] % 1234567