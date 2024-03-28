def possible(w, s) :
    for key, value in w.items() :
        if key not in s.keys() or w[key] > s[key] :
            return False
    return True

def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    
    for k, v in zip(want, number) :
        want_dict[k] = v
        
    
    for i in range(len(discount)-10+1) :
        sale_dict = {}
        sale = discount[i:i+10]
        
        for s in sale :
            if s not in sale_dict.keys() :
                sale_dict[s] = 1
            else :
                sale_dict[s] += 1

        if possible(want_dict, sale_dict) :
            answer += 1
    
    return answer