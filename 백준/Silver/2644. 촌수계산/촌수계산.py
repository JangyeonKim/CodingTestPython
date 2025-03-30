n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = [[] for _ in range(101)]
visit = [False] * 101

for _ in range(m) :
    par, chi = map(int, input().split())
    graph[par].append(chi)
    graph[chi].append(par)

from collections import deque 

def bfs(start, target, visit, graph) :
    queue = deque([[start, -1]])
    
    while queue :
        q, cnt = queue.popleft()
        if q == target :
            return cnt+1
            
        if not visit[q] :
            visit[q] = True
            for g in graph[q] :
                if not visit[g] :
                    queue.append([g, cnt+1])

    return -1

print(bfs(a, b, visit, graph))