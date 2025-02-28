import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

sum_arr = [arr[0]] + [0]*(len(arr)-1)
for i in range(1, len(sum_arr)) :
    sum_arr[i] = arr[i] + sum_arr[i-1]
sum_arr = [0] + sum_arr

for _ in range(M) :
    s, e = map(int, input().split())
    print(sum_arr[e] - sum_arr[s-1])