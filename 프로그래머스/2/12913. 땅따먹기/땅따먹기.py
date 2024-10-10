def solution(land):

    for i in range(1, len(land)) :
        for j in range(len(land[i])) :
            prev_land = land[i-1].copy()
            prev_land.pop(j)
            
            land[i][j] += max(prev_land)
    
    answer = max(land[-1])
    
    return answer