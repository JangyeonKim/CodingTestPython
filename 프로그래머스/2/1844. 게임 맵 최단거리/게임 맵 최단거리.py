from collections import deque

def bfs(start, maps) :
    x, y = start.popleft()
    
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    
    for i in range(4) :
        x_ = x + move_x[i]
        y_ = y + move_y[i]
        
        if x_ < 0 or y_ < 0 or x_ >= len(maps) or y_ >= len(maps[0]) :
            pass
        else :
            if maps[x_][y_] == 1 :
                maps[x_][y_] = maps[x][y] + 1
                start.append([x_, y_])
    

def solution(maps):
    start = deque([[0, 0]])
    
    while start :
        bfs(start, maps)
    
    if maps[-1][-1] == 1 :
        return -1
    else :
        return maps[-1][-1]
