import sys

in_list = []

count = int(sys.stdin.readline().strip())
for _ in range(count) :
    in_list.append(int(sys.stdin.readline().strip()))

in_list.sort()
for i in range(len(in_list)) :
    print(in_list[i])