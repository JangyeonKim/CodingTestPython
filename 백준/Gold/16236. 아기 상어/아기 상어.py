from collections import deque
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
big = 2 # 최초 크기
eat_cnt = 0
time = 0 

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 9 :
            pos = (i, j) # 최초 위치
            arr[i][j] = 0
            break
            
def bfs(cur, tar) :
    global N, big
    queue = deque([cur])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    distance = [[-1] * N for _ in range(N)]
    distance[cur[0]][cur[1]] = 0
    
    while queue :
        x, y = queue.popleft()
        if x == tar[0] and y == tar[1] :
            break
        for i in range(4) :
            xx = x + dx[i]
            yy = y + dy[i]
            
            if 0 <= xx < N and 0 <= yy < N :
                if arr[xx][yy] <= big and distance[xx][yy] == -1 :
                    distance[xx][yy] = distance[x][y] + 1
                    queue.append((xx, yy))
    return distance[tar[0]][tar[1]]

def make_candidate(pos) :
    global N, big
    candidate = []
    for i in range(N) :
        for j in range(N) :
            if 0 < arr[i][j] < big :
                min_distance = bfs(pos, (i, j))
                if min_distance != -1 :
                    candidate.append((min_distance, i, j))
    return candidate
                
while True :
    candidate = make_candidate(pos)
    if not candidate :
        print(time)
        break
    else :
        candidate.sort(key = lambda x : (x[0], x[1], x[2]))
        t, x, y = candidate[0]
        
        time += t
        eat_cnt += 1
        if eat_cnt == big :
            big += 1
            eat_cnt = 0
        
        arr[x][y] = 0
        pos = (x, y)