def solution(n,a,b):
    answer = 1
    
    arr = [x for x in range(1, n+1)] # 1 ~ 8
    group_len = 2
    
    while True :
        for i in range(int(len(arr) / group_len)) : # 0 ~ 3
            temp_arr = arr[i*group_len : i*group_len + group_len] # 0:2, 2:4, 4:6, 6:8
            if a in temp_arr and b in temp_arr :
                return answer
        answer += 1
        group_len *= 2