N = int(input())

arr = [list(map(int, input())) for _ in range(N)]

total = 0
answer = []

def dfs(x, y, arr) :
    global cnt
    arr[x][y] = 0
    cnt += 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4) :
        xx = x + dx[i]
        yy = y + dy[i]
        
        if xx < 0 or yy < 0 or xx >= len(arr) or yy >= len(arr[0]) :
            pass
        else :
            if arr[xx][yy] == 1 :
                dfs(xx, yy, arr)

for i in range(len(arr)) :
    for j in range(len(arr[0])) :
        if arr[i][j] == 1 :
            cnt = 0
            dfs(i, j, arr)
            total += 1
            answer.append(cnt)

print(total)
answer.sort()
for a in answer :
    print(a)