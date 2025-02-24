import sys

def isPrime(n) : 
    if n == 1 :
        return False
    
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 :
            return False
        
    return True

N = int(sys.stdin.readline().strip())

num_list = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
for num in num_list :
    if isPrime(num) :
        answer += 1
        
print(answer)