import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visit, start) :
    visit[start] = True
    print(start, end = " ")
    for v in sorted(graph[start]) :
        if not visit[v] :
            dfs(graph, visit, v)

def bfs(graph, visit, start) :
    queue = deque([start])

    while queue :
        q = queue.popleft()
        if not visit[q] :
            visit[q] = True
            print(q, end = " ")

            for qq in sorted(graph[q]) :
                if not visit[qq] :
                    queue.append(qq)

visit = [False] * (N+1)
dfs(graph, visit, V)
print()
visit = [False] * (N+1)
bfs(graph, visit, V)