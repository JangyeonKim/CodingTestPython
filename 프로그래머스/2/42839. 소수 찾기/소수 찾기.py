from itertools import permutations

def isPrime(n) :
    if n < 2 :
        return False
    
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
    
    return True
    

def solution(numbers) :
    num_list = list(numbers)
    
    candidate = []
    
    for i in range(1, len(numbers)+1) :
        perm = list(permutations(num_list, i))
        perm = [int("".join(x)) for x in perm]

        candidate += perm
        
    candidate = set(candidate)
    
    answer = 0
    for c in candidate :
        if isPrime(c) :
            answer += 1
            
    return answer
        