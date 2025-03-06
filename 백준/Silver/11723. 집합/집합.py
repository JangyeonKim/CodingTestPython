import sys
input = sys.stdin.readline

S = set()

M = int(input())

for _ in range(M) :
    order= input().strip()
    
    if not order.startswith("all") and not order.startswith("empty") :
        order, x = order.split()
        x = int(x)
    
    if order == "add" :
        S.add(x)
    elif order == "remove" and x in S :
        S.remove(x)
    elif order == "check" :
        print(1) if x in S else print(0)
    elif order == "toggle" :
        if x in S :
            S.remove(x)
        else :
            S.add(x)
    elif order == "all" :
        S = set([y for y in range(1,21)])
    elif order == "empty" :
        S = set()