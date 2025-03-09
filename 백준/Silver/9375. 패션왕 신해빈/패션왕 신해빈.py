import sys
input = sys.stdin.readline

from collections import defaultdict

T = int(input())
for t in range(T) :
    N = int(input())
    d = defaultdict(list)
    for n in range(N) :
        v, k = input().strip().split()
        d[k].append(v)

    answer = 1
    for key in d.keys() :
        answer *= (len(d[key]) + 1)
    print(answer-1)