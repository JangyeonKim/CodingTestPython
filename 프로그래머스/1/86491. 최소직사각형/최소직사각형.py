def solution(sizes):
    
    ans_x = []
    ans_y = []
    for x, y in sizes :
        ans_x.append(min(x,y))
        ans_y.append(max(x,y))
        
    return max(ans_x) * max(ans_y)