import sys
input = sys.stdin.readline

while True : 
    string = input().rstrip()
    if string == "." :
        break
    
    stack = []
    
    for s in string :
        if s == "(" or s == "[" :
            stack.append(s)
        
        elif s == ")" :
            if stack and stack[-1] == "(" :
                stack.pop()
            else : 
                stack.append(s)
                break
        
        elif s == "]" :
            if stack and stack[-1] == "[" :
                stack.pop()
            else : 
                stack.append(s)
                break
            
    print("yes") if not stack else print("no")