M, N, H = map(int, input().split())

storage = []

for h in range(H) :
    arr = [list(map(int, input().split())) for _ in range(N)]
    storage.append(arr)

from collections import deque
def bfs(queue, storage) :

    while queue :
        h, n, m = queue.popleft()
        #상하전후좌우
        dh = [-1, 1, 0, 0, 0, 0]
        dn = [0, 0, -1, 1, 0, 0]
        dm = [0, 0, 0, 0, -1, 1]
        
        for i in range(6) :
            hh = h + dh[i]
            nn = n + dn[i]
            mm = m + dm[i]
            
            if hh < 0 or nn < 0 or mm < 0 or hh >= len(storage) or nn >= len(storage[0]) or mm >= len(storage[0][0]):
                continue
            if storage[hh][nn][mm] == 0 :
                storage[hh][nn][mm] = storage[h][n][m] + 1
                queue.append((hh, nn, mm))

queue = deque([])

for h in range(H) :
    for n in range(N) :
        for m in range(M) :
            if storage[h][n][m] == 1 :
                queue.append((h, n, m))

bfs(queue, storage)

complete = True
answer = 0
for h in range(H) :
    for n in range(N) :
        for m in range(M) :
            if storage[h][n][m] == 0 :
                complete = False
            answer = max(answer, storage[h][n][m])

if not complete :
    print(-1)
else :
    print(answer-1)