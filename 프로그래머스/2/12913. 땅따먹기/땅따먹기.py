def solution(land):
    answer = 0
    
    for i in range(1, len(land)) :
        for j in range(4) :
            temp_land = land[i-1].copy()
            temp_land.pop(j)
            land[i][j] += max(temp_land)
            
    return max(land[-1])