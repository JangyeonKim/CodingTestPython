import sys

while True :
    in_list = list(map(int, sys.stdin.readline().strip().split()))
    in_list.sort()
    if in_list[0] == 0 and in_list[-1] == 0 :
        break
    else :
        c = in_list[-1]
        a, b = in_list[0], in_list[1]
        
        if c**2 == a**2 + b**2 :
            print("right")
        else :
            print("wrong")