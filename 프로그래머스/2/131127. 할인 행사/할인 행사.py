from collections import Counter

def canBuy(dict1, dict2) :
    for key in dict1.keys() :
        if key not in dict2.keys() :
            return False
        elif dict1[key] != dict2[key] :
            return False
    return True

def solution(want, number, discount):
    answer = 0
    
    want_dict = dict()
    
    for w, n in zip(want, number) :
        want_dict[w] = n
        
    for i in range(len(discount)-9) :
        temp_discount = discount[i:i+10]
        temp_dict = Counter(temp_discount)
        if canBuy(want_dict, temp_dict) :
            answer += 1
    
    return answer