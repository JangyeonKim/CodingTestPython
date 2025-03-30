N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# from collections import deque 
# visit = [False] * (N+1)
# def bfs(start, visit, graph) :
#     queue = deque([start])
#     cnt = -1
    
#     while queue :
#         q = queue.popleft()
#         if not visit[q] :
#             visit[q] = True
#             cnt += 1
#             for g in graph[q] :
#                 if not visit[g] :
#                     queue.append(g)
#     return cnt
# print(bfs(1, visit, graph))

visit = [False] * (N+1)
cnt = -1
def dfs(start, visit, graph) :
    global cnt
    visit[start] = True
    cnt += 1
    for g in graph[start] :
        if not visit[g] :
            dfs(g, visit, graph)
dfs(1, visit, graph)    
print(cnt)