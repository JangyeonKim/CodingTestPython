def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for com in range(n) :
        if not visited[com] :
            bfs(n, computers, com, visited)
            answer+= 1 # dfs로 컴퓨터들을 최대한 방문후 빠져나오면 하나의 네트워크
    
    return answer

def dfs(n, computers, com, visited) :
    visited[com] = True # 해당 컴퓨터 방문처리
    
    for connect in range(n) :
        if connect != com and computers[connect][com] == 1 :
            if not visited[connect] :
                dfs(n, computers, connect, visited)
                
def bfs(n, computers, com, visited):
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)