from collections import Counter

def solution(weights) :
    answer = 0
    counter = Counter(weights)
    
    for k, v in counter.items() :
        if counter[k] >= 2 : # counter[k]개 중에서 2개를 뽑는 경우의 수
            answer += (counter[k] * (counter[k] - 1)) /  2
        
    weight = set(weights)
    
    for wei in weight :
        if wei * 2/4 in weight :
            answer += counter[wei] * counter[wei * 2/4]
        if wei * 3/4 in weight :
            answer += counter[wei] * counter[wei * 3/4]
        if wei * 2/3 in weight :
            answer += counter[wei] * counter[wei * 2/3]
            
    return answer