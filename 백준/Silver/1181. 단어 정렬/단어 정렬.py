import sys

count = int(sys.stdin.readline().strip())

in_list = []
for i in range(count) :
    in_list.append(sys.stdin.readline().strip())

in_list = set(in_list)
in_len_list = [(x, len(x)) for x in in_list]
in_len_list.sort(key = lambda x : (x[1], x[0]))

for i in range(len(in_len_list)) :
    print(in_len_list[i][0])