from collections import deque

def bfs(queue, maps) :
    mv_x = [0, 0, -1, 1]
    mv_y = [-1, 1, 0, 0]
    
    while queue :
        y, x = queue.popleft()
        
        for i in range(4) :
            x_ = x + mv_x[i]
            y_ = y + mv_y[i]
            
            if x_ < 0 or y_ < 0 or x_ >= len(maps[0]) or y_ >= len(maps) :
                continue
            else :
                if maps[y_][x_] == 1 :
                    maps[y_][x_] = maps[y][x] + 1
                    queue.append([y_, x_])
    return maps


def solution(maps):
    queue = deque([[0, 0]])
    
    maps = bfs(queue, maps)
    
    if maps[-1][-1] == 1: 
        return -1
    else :
        return maps[-1][-1]