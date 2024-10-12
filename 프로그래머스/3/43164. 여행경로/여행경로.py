from collections import deque

def bfs(queue, tickets) :
    answer = []
    
    while queue :
        start, route, check = queue.popleft()
        
        if len(route) == len(tickets) + 1:
            answer.append(route)
        
        for idx, ticket in enumerate(tickets) :
            if ticket[0] == start and not check[idx] :
                new_check = check.copy()
                new_check[idx] = True
                queue.append([ticket[1], route+[ticket[1]], new_check])
        
    return answer

def solution(tickets) :
    route = ["ICN"]
    check = [False] * len(tickets)
    queue = deque([["ICN", route, check]])
    
    answer = bfs(queue, tickets)
    answer.sort()
    return answer[0]
    
