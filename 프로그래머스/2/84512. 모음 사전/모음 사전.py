from itertools import product

def solution(word):
    answer = 0
    
    word_list = ["A", "E", "I", "O", "U"]
    total = []
    
    for i in range(1,6) :
        wd = list(product(word_list, repeat = i))
        wd = ["".join(w) for w in wd]
        total += wd
        
    total.sort()
    answer = total.index(word)+1
    
    return answer