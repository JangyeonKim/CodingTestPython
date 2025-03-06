import sys
input = sys.stdin.readline

n_com = int(input())
n_link = int(input())

arr = [[] for _ in range(n_com+1)]

for _ in range(n_link) :
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [False] * (n_com+1)

from collections import deque

def bfs(start, visit, arr) :
    queue = deque(arr[start]) # 1번 컴퓨터
    visit[start] = True
    cnt = 0
    
    while queue : 
        com = queue.popleft()

        if not visit[com] :
            visit[com] = True
            cnt += 1

            for c in arr[com] :
                if not visit[c] :
                    queue.append(c)

    return cnt

answer = bfs(1, visit, arr)
print(answer)