from collections import deque

def bfs(start, link) :
    visit = [False] * len(link)
    queue = deque([start])
    cnt = 0
    while queue :
        q = queue.popleft()
        if not visit[q] :
            cnt += 1
            visit[q] = True
            for l in link[q] :
                if not visit[l] :
                    queue.append(l)
    return cnt
    

def solution(n, wires) :
    link = [[] for _ in range(n+1)]
    
    for a, b in wires :
        link[a].append(b)
        link[b].append(a)
        
    answer = n
    
    for a, b in wires :
        link[a].remove(b)
        link[b].remove(a)
        
        answer = min(answer, abs(bfs(a, link) - bfs(b, link)))
        
        link[a].append(b)
        link[b].append(a)
    
    return answer