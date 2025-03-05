import sys
input = sys.stdin.readline

from collections import defaultdict
d = defaultdict(int)

N = int(input())

arr = [] 
for _ in range(N) :
    arr.append(int(input()))

arr.sort()
for a in arr :
    d[a] += 1

mv = max(d.values())

arr2 = [] 
for key, value in d.items() :
    if value == mv :
        arr2.append(key)
arr2.sort()

print(round(sum(arr)/N))
print(arr[N//2])
if len(arr2) == 1:
    print(arr2[0])
else :
    print(arr2[1])
print(arr[-1]-arr[0])