from collections import Counter

def solution(topping):
    answer = 0
    
    top_dict = Counter(topping)
    
    vs_set = set()
    for top in topping :
        top_dict[top] -= 1
        vs_set.add(top)
        
        if top_dict[top] == 0 :
            del(top_dict[top])
            
        if len(top_dict) == len(vs_set) :
            answer += 1
        
    return answer