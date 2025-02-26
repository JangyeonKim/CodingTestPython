import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N) :
    order = input().strip()
    if order.startswith("push") :
        order, n = order.split()
        
    if order == "push" :
        stack.append(int(n))
    elif order == "pop" :
        if stack :
            print(stack.pop())
        else :
            print(-1)
    elif order == "size" :
        print(len(stack))
    elif order == "empty" :
        print(0) if stack else print(1)
    elif order == "top" :
        print(stack[-1]) if stack else print(-1)