import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
for _ in range(K) :
    arr.append(int(input()))
    
left = 1
right = max(arr) 

while left <= right :
    mid = (left + right) // 2
    cnt = 0
    
    for a in arr :
        cnt += a // mid
        
    # print(f"{left} {right} -> {mid} -> {cnt}")
    
    if cnt >= N :
        left = mid + 1
    else :
        right = mid - 1

print(right) # left > right가 될 때의 right 값이 가장 긴 랜선의 길이