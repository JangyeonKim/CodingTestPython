def solution(k, tangerine):
    answer = 0
    
    t_dict = {}
    
    for t in tangerine :
        if t not in t_dict.keys() :
            t_dict[t] = 1
        else :
            t_dict[t] += 1
            
    # print(t_dict)
    kind = sorted(list(t_dict.values()), reverse=True)
    # print(kind)
    
    for kk in kind :
        k -= kk
        answer += 1
        
        if k <= 0 :
            return answer