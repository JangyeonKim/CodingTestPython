from copy import deepcopy

arr = [[] for _ in range(4)]
for i in range(4) :
    temp = list(map(int, input().split()))
    start = 0
    for j in range(4) :
        arr[i].append(temp[start:start+2])
        start += 2

## 방향 : 반시계
### 1, 2, 3, 4, 5, 6, 7, 8
### ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

def dfs(s_x, s_y, score, arr) :
    global answer
    score += arr[s_x][s_y][0]
    answer = max(answer, score)
    arr[s_x][s_y][0] = 0 # 먹힘
    
    # 물고기 이동
    for fish in range(1, 17) :
        flag = False
        for x in range(4) :
            for y in range(4) :
                if arr[x][y][0] == fish :
                    f_d = arr[x][y][1]
                    
                    # 위치 바꾸기
                    for i in range(8) :
                        xx = x + dx[(f_d-1+i) % 8]
                        yy = y + dy[(f_d-1+i) % 8]
                        
                        if 0 <= xx < 4 and 0 <= yy < 4 :
                            if xx != s_x or yy != s_y : # 상어가 있으면 못감
                                arr[x][y][1] = (f_d-1+i) % 8 + 1
                                arr[x][y], arr[xx][yy] = arr[xx][yy], arr[x][y]
                                flag = True
                                break
                # 다음 물고기 이동시키기
                if flag == True : break
            if flag == True : break
                
    # 상어 이동
    s_d = arr[s_x][s_y][1]
    for s in range(1, 5) : # 최소 1칸, 최대 4칸 이동 가능
        s_xx = s_x + dx[s_d-1] * s
        s_yy = s_y + dy[s_d-1] * s
        
        if 0 <= s_xx < 4 and 0 <= s_yy < 4 :
            if arr[s_xx][s_yy][0] != 0 : # 물고기가 있는 칸으로만 이동 가능
                dfs(s_xx, s_yy, score, deepcopy(arr))
    
dfs(0, 0, 0, arr) # 상어_x, 상어_y, score, arr
print(answer)