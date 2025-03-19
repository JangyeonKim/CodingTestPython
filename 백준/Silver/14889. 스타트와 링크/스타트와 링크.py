import sys
input= sys.stdin.readline

N = int(input())
matrix = []
M = N//2

for _ in range(N) :
    matrix.append(list(map(int, input().split())))

answer = 100*M*M

def dfs(n, arr_a, arr_b) :
    global answer
    if n == N :
        if len(arr_a) == len(arr_b) :
            answer = min(answer, cal(arr_a, arr_b))
        return

    dfs(n+1, arr_a + [n], arr_b)
    dfs(n+1, arr_a, arr_b + [n])

def cal(arr_a, arr_b) :
    aval = bval = 0 
    for i in range(M) :
        for j in range(M) :
            aval += matrix[arr_a[i]][arr_a[j]]
            bval += matrix[arr_b[i]][arr_b[j]]
    return abs(aval - bval)

dfs(0, [], [])
print(answer)