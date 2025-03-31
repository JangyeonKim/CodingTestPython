def solution(triangle):
    dp = [[0 for i in range(len(t))] for t in triangle]
    dp[0][0] = triangle[0][0]
    # print(dp)
    
    for i in range(1, len(dp)) :
        for j in range(len(dp[i])) :
            if j == 0 :
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif j == len(dp[i])-1 :
                dp[i][j] = dp[i-1][-1] + triangle[i][-1]
            else :
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
    # print(dp)
    
    return max(dp[-1])