import sys
from collections import defaultdict

input = sys.stdin.readline
d = defaultdict(int)

N = int(input())
N_arr = list(map(int, input().split()))
for n in N_arr :
    d[n] += 1

M = int(input())
M_arr = list(map(int, input().split()))

for m in M_arr :
    print(1) if m in d.keys() else print(0)