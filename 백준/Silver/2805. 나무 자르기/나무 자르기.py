import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))

t = max(height)
b = 0

while b <= t :
    mid = (t+b) // 2
    
    rest = [x-mid for x in height if x >= mid]
    total = sum(rest)
    
    if total >= M :
        b = mid+1
    else :
        t = mid-1
    
print(t)