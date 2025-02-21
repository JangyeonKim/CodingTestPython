import sys

_ = int(sys.stdin.readline().rstrip())

num = sys.stdin.readline().rstrip()

ans = 0
for n in num :
    ans += int(n)
    
print(ans)