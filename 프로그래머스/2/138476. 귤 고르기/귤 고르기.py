def solution(k, tangerine):
    ans_dict = {}
    for t in tangerine :
        if t not in ans_dict.keys() :
            ans_dict[t] = 1
        else :
            ans_dict[t] += 1
    
    ans_list = sorted([x for _, x in ans_dict.items()])
    
    result = 0
    
    while True :
        a = ans_list.pop()
        k -= a
        result += 1
        
        if k <= 0 :
            break
            
    return result