from collections import deque

def solution(n, wires):
    res = 0
    
    graph = [[] for _ in range(n+1)] # 1번 부터 n번 노드, 0번은 비어있게됨
    
    for a, b in wires : # 모든 연결 정보를 그래프에 기록
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start) : # 시작점을 기준으로 몇개의 노드가 연결되어 있는지 갯수 return
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        cnt = 1
        while queue :
            q = queue.popleft()
            for i in graph[q] :
                if not visited[i] :
                    visited[i] = True
                    queue.append(i)
                    cnt += 1
        return cnt
    
    res = n 
    for a, b in wires : # a와 b의 연결을 순차적으로 끊어가며 최소 개수 차이 갱신
        graph[a].remove(b)  
        graph[b].remove(a)
        
        res = min(abs(bfs(a) - bfs(b)), res)
        
        graph[a].append(b)
        graph[b].append(a)
    
    return res