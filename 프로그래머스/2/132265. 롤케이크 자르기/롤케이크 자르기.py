from collections import Counter

def solution(topping):
    answer = 0
    
    roll = Counter(topping)
    cut = set()
    
    for t in topping :
        roll[t] -= 1
        if roll[t] == 0 :
            del(roll[t])
        
        cut.add(t)
    
        if len(roll) == len(cut) :
            answer += 1
    
    return answer