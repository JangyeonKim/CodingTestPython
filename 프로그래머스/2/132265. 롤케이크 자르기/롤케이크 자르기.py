def solution(topping):
    answer =0
    
    old_dict = {}
    for t in topping :
        if t not in old_dict.keys() :
            old_dict[t] = 1
        else :
            old_dict[t] += 1
    
    young_dict = {}
    for i in range(len(topping)) :
        t = topping[i]
        
        if t not in young_dict.keys() :
            young_dict[t] = 1
        else :
            young_dict[t] += 1

        old_dict[t] -= 1
        if old_dict[t] == 0 :
            old_dict.pop(t)
        
        if len(old_dict.keys()) == len(young_dict.keys()) :
            answer += 1
        if len(old_dict.keys()) < len(young_dict.keys()) :
            break
    
    
    return answer