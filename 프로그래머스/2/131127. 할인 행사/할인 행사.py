from collections import Counter

def same(dict1, dict2) :
    for key in dict1.keys() :
        if dict1[key] != dict2[key] :
            return False
    
    return True

def solution(want, number, discount):
    answer = 0
    
    w_dict = {}
    
    for w, n in zip(want, number) :
        w_dict[w] = n
        
    cal_days = len(discount) - 10
    
    for i in range(cal_days+1) :
        days_discount = discount[i:i+10]
        d_dict = Counter(days_discount)
        
        if same(w_dict, d_dict) :
            answer += 1
    
    return answer