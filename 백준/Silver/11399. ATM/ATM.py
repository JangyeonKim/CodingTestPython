import sys

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))

p.sort()

sum_list = [p[0]]

for i in range(1, n) :
    sum_list.append(sum_list[i-1] + p[i])

print(sum(sum_list))