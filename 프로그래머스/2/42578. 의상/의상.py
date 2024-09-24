def solution(clothes):
    answer = 1
    
    c_dict = {}
    for v, k in clothes :
        if k not in c_dict.keys() :
            c_dict[k] = [v]
        else :
            c_dict[k].append(v)
    
    for k, v in c_dict.items() :
        answer *= (len(v)+1)
    
    return answer -1