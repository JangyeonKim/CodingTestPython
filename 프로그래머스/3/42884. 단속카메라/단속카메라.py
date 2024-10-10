from collections import deque

def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    camera = -30001
    for in_, out_ in routes :
        if in_ <= camera <= out_ :
            pass
        else :
            camera = out_
            answer += 1
     
    return answer