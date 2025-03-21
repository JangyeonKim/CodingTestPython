import sys
import heapq

input = sys.stdin.readline

arr = []
heapq.heapify(arr)

N = int(input())

for _ in range(N) :
    n = int(input())
    
    if n == 0 :
        if not arr :
            print(0)
        else :
            print(heapq.heappop(arr)[1])
    else :
        heapq.heappush(arr, (-n, n))