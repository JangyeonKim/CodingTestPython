import sys

max_num, max_idx = 0, 0
for i in range(9) :
    n = int(sys.stdin.readline().strip())
    if n > max_num :
        max_num = n
        max_idx = i+1

print(max_num)
print(max_idx)