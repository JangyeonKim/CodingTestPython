import sys

while True : 
    a, b = map(int, sys.stdin.readline().strip().split())
    
    if a == 0 and b == 0 :
        break
    else :
        print(a+b)