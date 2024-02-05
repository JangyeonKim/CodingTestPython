import sys
input = sys.stdin.readline

m, n = map(int, input().split())

def get_primes(num) :
    isPrime = [False, False] + [True] * (n-1) # 0, 1 은 소수 아님. 2부터 시작
    primes = []
    
    for i in range(2, n+1) :
        if isPrime[i] :
            primes.append(i)
            
            for j in range(2*i, n+1, i) : # 소수(i)의 배수 제거
                isPrime[j] = False
                
    return primes

prime = get_primes(n)

for p in prime :
    if p >= m :
        print(p)