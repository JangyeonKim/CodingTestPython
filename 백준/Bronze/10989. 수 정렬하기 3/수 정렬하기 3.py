import sys
input = sys.stdin.readline

N = int(input())

arr = [0 for _ in range(10000+1)]

for _ in range(N) :
    arr[int(input())] += 1
    
for i in range(len(arr)) :
    if arr[i] != 0 :
        for _ in range(arr[i]) :
            print(i)
        