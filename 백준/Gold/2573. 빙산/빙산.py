N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = True

def year_after(arr, N, M) :
    global flag
    zero_cnt = []
    for i in range(len(arr)) :
        for j in range(len(arr[0])) :
            if arr[i][j] != 0 :
                cnt = 0
                for k in range(4) :
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M :
                        if arr[nx][ny] == 0 :
                            cnt += 1
                zero_cnt.append((i,j,cnt))
    if zero_cnt :
        for i, j, c in zero_cnt :
            arr[i][j] -= c
            if arr[i][j] < 0 :
                arr[i][j] = 0
    else :
        flag = False

from collections import deque
def bfs(i, j, arr, visit) :
    visit[i][j] = True
    queue = deque([(i, j)])

    while queue :
        i, j = queue.popleft()
        for k in range(4) :
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < M :
                if arr[ni][nj] != 0 and not visit[ni][nj] :
                    visit[ni][nj] = True
                    queue.append((ni, nj))

year_cnt = 0
while True :
    island_cnt = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(len(arr)) :
        for j in range(len(arr[0])) :
            if arr[i][j] != 0 and not visit[i][j]:
                bfs(i, j, arr, visit)
                island_cnt += 1

    if island_cnt >= 2 :
        print(year_cnt)
        break
    else :
        year_after(arr, N, M)
        year_cnt +=1
        if not flag :
            print(0)
            break