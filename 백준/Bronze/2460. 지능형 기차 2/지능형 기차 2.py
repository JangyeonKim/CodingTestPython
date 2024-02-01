import sys
input = sys.stdin.readline

ans = 0 
num_p = 0

for _ in range(10) :
    out, come = map(int, input().split())
    num_p = num_p - out + come
    
    if num_p > ans :
        ans = num_p

print(ans)