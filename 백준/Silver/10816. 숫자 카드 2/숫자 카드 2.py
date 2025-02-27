from collections import defaultdict

d = defaultdict(int)

N = int(input())
card = list(map(int, input().split()))

for c in card :
    d[c] += 1

M = int(input())
num = list(map(int, input().split()))

for n in num :
    print(d[n], end = " ")