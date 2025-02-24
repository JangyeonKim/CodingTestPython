import sys

while True :
    tri_arr = list(map(int, sys.stdin.readline().strip().split()))
    tri_arr.sort()
    
    if tri_arr[0] == 0 and tri_arr[-1] == 0 :
        break
    
    if tri_arr[0] ** 2 + tri_arr[1] ** 2 == tri_arr[-1] ** 2 :
        print("right")
    else :
        print("wrong")