def solution(n):
    
    ans_list = [0 for _ in range(n+1)]
    ans_list[0], ans_list[1] = 1, 1

    for i in range(2, n+1) :
        ans_list[i] = (ans_list[i-1] + ans_list[i-2]) % 1000000007
    
    return ans_list[-1] 