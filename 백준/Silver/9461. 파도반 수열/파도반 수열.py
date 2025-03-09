import sys
input = sys.stdin.readline

arr = [0,1,1,1]

T = int(input())
for t in range(T) :
    n = int(input())
    if n <= 3 :
        print(arr[n])
    else :
        new_arr = arr + [0] * (n-3)
        for i in range(4, n+1) :
            new_arr[i] = new_arr[i-2] + new_arr[i-3]
        print(new_arr[n])