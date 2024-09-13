def isCorrect(arr) : # [](){}
    stack = []
    
    for a in arr :
        if stack :
            if stack[-1] == '[' and a == ']' :
                stack.pop()
            elif stack[-1] == '{' and a == '}' :
                stack.pop()
            elif stack[-1] == '(' and a == ')' :
                stack.pop()
            else :
                stack.append(a)
        else :
            stack.append(a)
    
    return True if not stack else False
    
def solution(s):
    answer = 0
    
    for i in range(len(s)) :
        temp = s[i:] + s[:i]
        if isCorrect(temp) :
            answer += 1
    
    return answer