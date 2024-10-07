from collections import deque

def isCorrect(arr) :
    queue = deque(arr)
    stack = []
    
    map_dict = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    }
    
    while queue :
        q = queue.popleft()
        if stack and q in map_dict.keys() and stack[-1] == map_dict[q] :
            stack.pop()
        else :
            stack.append(q)
    return True if not stack else False
    

def solution(s):
    answer = 0
    lens = len(s)
    s *= 2
    
    for i in range(lens) :
        circular = s[i:i+lens]
        if isCorrect(circular) :
            answer += 1
    
    return answer