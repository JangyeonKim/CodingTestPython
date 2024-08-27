def solution(n):
    if n < 3 :
        return n
    
    n_list = [0 for _ in range(n)]
    n_list[0] = 1
    n_list[1] = 2
    
    for i in range(2, n) :
        n_list[i] = n_list[i-1] + n_list[i-2]
    
    return n_list[-1] % 1234567