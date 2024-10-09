from collections import deque

def solution(n, computers):
    answer = 0
    
    visit = [False] * n
    queue = deque([])
    
    for i in range(n) :
        if not visit[i] :
            queue.append(i)
            answer += 1
            while queue :
                q = queue.popleft()
                visit[q] = True
                
                for com in range(len(computers[q])) :
                    if computers[q][com] == 1 and not visit[com] :
                        queue.append(com)
    
    return answer