M, N = map(int, input().split())

def isPrime(n) :
    if n < 2 : 
        return False
    
    for i in range(2, int(n**0.5)+1) :
        if n % i == 0 :
            return False
    return True

prime_arr = [False, False] + [True] * (N-1)

for i in range(2, N+1) :
    if prime_arr[i] :
        if isPrime(i) :
            for j in range(i*2, N+1, i) :
                prime_arr[j] = False
        else :
            prime_arr[i] = False
            
for i in range(M, N+1) :
    if prime_arr[i] :
        print(i)