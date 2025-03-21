import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M) :
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
visit = [False] * (N+1)

from collections import deque
def bfs(visit, v, arr) :
    visit[v] = True
    queue = deque([v])
    
    while queue :
        q = queue.popleft()
        for l in arr[q] :
            if not visit[l] :
                visit[l] = True
                queue.append(l)

cnt = 0
for i in range(1, N+1) :
    if not visit[i] :
        bfs(visit, i, arr)
        cnt += 1
        
print(cnt)          