from itertools import combinations, permutations

def isPrime(n) :
    if n < 2 : 
        return False
    else :
        for i in range(2, int((n**0.5))+1) :
            if n%i == 0 :
                return False
        
        return True

def solution(numbers):
    answer = 0
    
    all_ = []
    
    for i in range(1, len(numbers)+1) :
        all_ += list(permutations(numbers, i))
    
    # print(all_)
    
    all_n = []
    for a in all_ :
        all_n.append(int("".join(a)))
        
    # print(all_n)
    all_n = set(all_n)
    # print(all_n)
    
    for n in all_n :
        if isPrime(n) :
            answer+=1
    
    return answer