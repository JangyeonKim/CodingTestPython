import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

def dfs(x, y) :
    if x < 0 or y < 0 or x >= len(ground[0]) or y >= len(ground) :
        pass

    else :
        if ground[y][x] == 1 :
            ground[y][x] = 0

            # 상하좌우
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x+1, y)
            return True
        return False

for t in range(T) :
    M, N, K = map(int, input().split())
    
    ground = [[0 for m in range(M)] for n in range(N)]
    
    for k in range(K) :
        x, y = map(int, input().split())
        ground[y][x] = 1

    cnt = 0
    for yy in range(N) :
        for xx in range(M) :
            if dfs(xx, yy) :
                cnt += 1

    print(cnt)