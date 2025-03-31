def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    dp[1][1] = 1
    for i, j in puddles :
        dp[j][i] = -1
    
    for i in range(1, n+1) :
        for j in range(1, m+1) :
            if i == 1 and j == 1 : 
                continue
            if dp[i][j] == -1 : # 웅덩이이면
                dp[i][j] = 0
            else :
                # 위쪽 경로 개수 + 왼쪽 경로 개수
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    return(dp[-1][-1])