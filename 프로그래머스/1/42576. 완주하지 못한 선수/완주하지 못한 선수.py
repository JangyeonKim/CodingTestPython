def make_dict(p_list) :
    return_dict = {}
    
    for p in p_list :
        if p not in return_dict.keys() :
            return_dict[p] = 0
        else :
            return_dict[p] += 1
            
    return return_dict

def solution(participant, completion):
    p_dict = make_dict(participant)
    
    for c in completion :
        p_dict[c] -= 1
        
    for key, value in p_dict.items() :
        if value == 0 :
            return key
  