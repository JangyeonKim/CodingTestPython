from collections import deque

def bfs(x, y, maps) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx < 0 or xx >= len(maps) or yy < 0 or yy >= len(maps[0]) :
                continue
            if maps[xx][yy] == 0 :
                continue
            if maps[xx][yy] == 1 :
                maps[xx][yy] = maps[x][y] + 1
                queue.append((xx,yy))
    

# bfs를 이용하여, map의 최단경로를 갱신하며 진행
def solution(maps) :
    bfs(0,0, maps)
    
    answer = maps[-1][-1]
    if answer == 1 :
        return -1
    else :
        return answer