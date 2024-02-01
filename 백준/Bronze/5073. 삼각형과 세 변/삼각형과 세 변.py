import sys
input = sys.stdin.readline

while True :
    l = list(map(int, input().split()))
    l.sort()
    
    if l[0] == 0 and l[1] == 0 and l[2] == 0 :
        break
    
    elif l[-1] >= sum(l[:2]) :
        print("Invalid")
    
    else :
        if l[1] == l[2] and l[2] == l[0] :
            print("Equilateral")
        elif l[0] == l[1] or l[1] == l[2] :
            print("Isosceles")
        else :
            print("Scalene")