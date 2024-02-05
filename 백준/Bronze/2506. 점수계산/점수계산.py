import sys
input = sys.stdin.readline

N = int(input())

result = map(int, input().split())

ans = 0

plus = 0
for r in result : 
    if r == 0 :
        plus = 0
    else :
        plus += 1
        ans += plus
        
print(ans)