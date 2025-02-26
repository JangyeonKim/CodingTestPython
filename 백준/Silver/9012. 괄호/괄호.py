N = int(input())

for _ in range(N) :
    stack = []
    
    string = input()
    
    for s in string :
        if s == "(" :
            stack.append(s)
        else :
            if stack and stack[-1] == "(" :
                stack.pop()
            else :
                stack.append(s)
                
    print("NO") if stack else print("YES")