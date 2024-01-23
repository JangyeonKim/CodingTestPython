def solution(s):
    answer = True
    
    stack = []
    
    if s.startswith(")") :
        return False
    
    for ss in s :
        if ss == "(" :
            stack.append(ss)
        elif ss == ")" and len(stack) != 0 :
            stack.pop()
        else :
            return False
        
    if len(stack) != 0 :
        return False
        
    return True