def solution(triangle):
    answer = 0
    
    for i in range(1, len(triangle)) :
        for t in range(len(triangle[i])) :
            if t == 0  :
                triangle[i][t] += triangle[i-1][0]
            elif t == len(triangle[i]) -1 :
                triangle[i][t] += triangle[i-1][-1]
            else :
                val = max(triangle[i-1][t-1], triangle[i-1][t])
                triangle[i][t] += val
    
    return max(triangle[-1])