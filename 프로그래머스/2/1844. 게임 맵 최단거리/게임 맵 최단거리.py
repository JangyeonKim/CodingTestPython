from collections import deque

def bfs(maps, N, M, start_x, start_y) :
    # 상하좌우로 움직이기 위한 리스트 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐가 빌 때까지 최단거리 구하기
    queue = deque()
    queue.append((start_x, start_y))
    
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            # 거리를 측정하지 않는 경우
                # 1. 미로의 범위를 벗어나는 경우
                # 2. 이동할 곳이 "0" 값인 경우
            if xx < 0 or xx >= N or yy < 0 or yy >= M :
                continue
            if maps[xx][yy] == 0 :
                continue
            
            # 처음 이동하는 곳인 경우 최단 거리 측정
            if maps[xx][yy] == 1:
                maps[xx][yy] = maps[x][y] + 1
                queue.append((xx,yy))
    
    return maps[-1][-1] # 출구까지의 최단거리 리턴

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    ans = bfs(maps, n, m, 0, 0)
    
    # ans가 1이면(최단 경로가 존재하지 않으면) -1 리턴, 아닌 경우 ans 리턴
    if ans == 1 :
        return -1
    else :
        return ans