import sys
input= sys.stdin.readline

N = int(input())
T = []
P = []

for _ in range(N) :
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

##### 백트래킹 : N이 작아서 가능

# max_pay = 0

# def dfs(n, pay) :
#     global max_pay
#     if n >= N : # 종료 조건
#         max_pay = max(pay, max_pay)
#         return 

#     if n + T[n] <= N : # 상담 진행
#         dfs(n+T[n], pay+P[n])
#     # 상담 진행 x (항상 가능)
#     dfs(n+1, pay)

# dfs(0,0)
# print(max_pay)

##### DP

dp = [0] * (N+1)

for n in range(N-1, -1, -1) :
    if n + T[n] <= N :
        dp[n] = max(P[n] + dp[n+T[n]], dp[n+1])

    else :
        dp[n] = dp[n+1]

print(dp[0])