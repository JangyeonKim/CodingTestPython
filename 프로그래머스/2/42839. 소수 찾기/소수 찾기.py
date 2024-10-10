from itertools import permutations

def isPrime(num) :
    if num < 2 :
        return False
    
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    candidate = set()
    
    for i in range(1, len(numbers)+1) :
        possible = list(permutations(numbers, i))
        for p in possible :
            candidate.add(int("".join(p)))
    
    for c in candidate :
        if isPrime(c) :
            answer += 1
    
    return answer