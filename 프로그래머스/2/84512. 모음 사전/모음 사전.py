from itertools import product

def solution(word):
    answer = []
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6) :
        for j in product(alpha, repeat=i) :
            answer.append(list(j))
    
    answer.sort()
    
    for idx, a in enumerate(answer) :
        if "".join(a) == word :
            return idx+1