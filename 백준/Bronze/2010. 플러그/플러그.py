import sys
input = sys.stdin.readline

n = int(input())

ans = 0
for i in range(n) :
    if i == n - 1:
        ans += int(input())
    else :
        ans += int(input())-1
        
print(ans)