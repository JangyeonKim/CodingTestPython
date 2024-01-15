import sys

while (1):
    try:
        A = list(map(int,(sys.stdin.readline().split())))
        print(A[0]+A[1])
    except:
        break