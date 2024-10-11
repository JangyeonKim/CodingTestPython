def gcd(a, b) :
    A = max(a, b)
    B = min(a,b)
    
    if A%B == 0 :
        return B
    else :
        return gcd(B, A%B)
    
def multigcd(arr) :
    while len(arr) > 1 :
        GCD = gcd(arr.pop(), arr.pop())
                  
        if GCD == 1 :
            return 1
        arr.append(GCD)
        
    return arr[0]

def condition(n,array) :
    if (n == 1) :
        return 0
    for a in array :
        if( a % n == 0) :
            return 0
    return 1

def solution(arrayA, arrayB):
    Agcd = multigcd(arrayA.copy())
    Bgcd = multigcd(arrayB.copy())
    
    A = Agcd if condition(Agcd, arrayB) else 0
    B = Bgcd if condition(Bgcd, arrayA) else 0
    
    answer = max(A,B)
    return answer
    
    