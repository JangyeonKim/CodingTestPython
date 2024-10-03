def dfs(visited, com, computers) :
    for c in range(len(computers[com])) :
        if computers[com][c] == 1 and not visited[c] :
            visited[c] = True
            dfs(visited, c, computers)
    

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for com in range(n) :
        if visited[com] == False :
            visited[com] = True
            answer += 1
            dfs(visited, com, computers)
    
    return answer