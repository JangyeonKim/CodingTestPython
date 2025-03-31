F, S, G, U, D = map(int, input().split())
cnt = 0

from collections import deque
queue = deque([(S, cnt)])
visit = [False] * (F+1)
visit[S] = True
flag = False
while queue :
    q, c = queue.popleft()
    if q == G:
        flag = True
        print(c)
        break
    arr = [q + U, q - D]
    for a in arr :
        if a > 0 and a <= F :
            if not visit[a] :
                visit[a] = True
                queue.append((a, c+1))

if flag == False :
    print("use the stairs")