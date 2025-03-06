import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = [arr[0]] + [0] * (len(arr)-1)
for i in range(1, len(arr)) :
    answer[i] = answer[i-1] + arr[i]

print(sum(answer))