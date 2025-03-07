import sys
input = sys.stdin.readline

# dp : 점화식

n=int(input())
stairs=[]
for _ in range(n):
    stairs.append(int(input()))

dp=[0]*n

if n==1:
    print(stairs[0])
elif n==2:
    print(stairs[0]+stairs[1])
elif n==3:
    print(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
else:
    dp[0]=stairs[0]
    dp[1]=stairs[0]+stairs[1]
    dp[2]=max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3, n):
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[n-1])

#### 메모리 초과 ####

# n = int(input())
# stairs = dict()

# for i in range(1, n+1) :
#     stairs[i] = int(input())
    
# arr = [(0, 0, 0)]
# max_score = 0

# while True : 
#     temp = []
#     for stair, score, cnt1 in arr:
#         if stair == n :
#             max_score = max(score, max_score)
#         else :
#             if stair + 1 <= n and cnt1 < 2 :
#                 temp.append((stair+1, score + stairs[stair+1], cnt1+1))
#             if stair + 2 <= n :
#                 temp.append((stair+2, score + stairs[stair+2], 1))
        
#     if not temp :
#         break
#     arr = temp

# print(max_score)