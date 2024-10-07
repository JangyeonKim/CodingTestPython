def gcd(a, b) :
    A = max([a, b])
    B = min([a, b])
    
    a = A
    b = B
    
    if a % b == 0 :
        return b
    else :
        return gcd(b, a%b)

def solution(arr):
    answer = 0
    arr.sort(reverse = True)
    
    a = arr.pop(0)
    b = arr.pop(0)
    
    GCD  = gcd(a,b)
    LCM = a * b / GCD
    
    for a in arr :
        GCD = gcd(a, LCM)
        LCM = a * LCM / GCD
    
    
    return LCM