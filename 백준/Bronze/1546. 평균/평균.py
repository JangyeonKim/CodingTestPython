import sys

count = int(sys.stdin.readline().strip())

in_list = list(map(int, sys.stdin.readline().strip().split()))
if len(in_list) == 1 :
    print("100")
else : 
    in_list.sort()

    max_val = in_list.pop()

    ans = []
    for val in in_list :
        ans.append(val / max_val * 100)

    ans.append(100)
    print(sum(ans) / count)