N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, arr))
answer = []

def dfs(x, y, region) :
    region[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]

        if xx < 0 or yy < 0 or xx >= len(region) or yy >= len(region[0]) :
            pass
        else :
            if region[xx][yy] == 1 :
                dfs(xx, yy, region)

from collections import deque
def bfs(x, y, region) :
    queue = deque([(x, y)])
    region[x][y] = 0
    
    while queue :
        x, y = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
    
            if xx < 0 or yy < 0 or xx >= len(region) or yy >= len(region[0]) :
                pass
            else :
                if region[xx][yy] == 1 :
                    region[xx][yy] = 0
                    queue.append((xx,yy))

for height in range(max_height) :
    region = []
    for a in arr[:] :
        region.append([1 if x > height else 0 for x in a])

    cnt = 0
    for i in range(len(region)) :
        for j in range(len(region)) :
           if region[i][j] == 1 :
               # dfs(i, j, region)
               bfs(i, j, region)
               cnt += 1

    answer.append(cnt)

print(max(answer))