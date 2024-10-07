from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    t_dict = Counter(tangerine)
    
    t_list = [x for x in t_dict.values()]
    t_list.sort()
    
    while t_list :
        t = t_list.pop()
        
        k -= t
        answer += 1
        if k <= 0 :
            return answer
    return answer