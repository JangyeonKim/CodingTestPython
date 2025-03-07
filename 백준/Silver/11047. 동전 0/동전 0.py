import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# coin = [1]

# for i in range(1, N) :
#     if i % 2 != 0 :
#         coin.append(coin[i-1] * 5)
#     else :
#         coin.append(coin[i-1] * 2)

coin = [int(input()) for _ in range(N)]

cnt = 0

while K != 0 :
    c = coin.pop() 

    if c <= K :
        div = K//c
        K -= c * div
        cnt += div

print(cnt)