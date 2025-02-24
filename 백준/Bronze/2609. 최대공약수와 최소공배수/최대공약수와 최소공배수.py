def gcd(aa, bb) :
    a = max(aa, bb)
    b = min(aa, bb)
    
    if a % b != 0 :
        return gcd(b, a%b)
    else :
        return b
        

a, b = map(int, input().split())

GCD = gcd(a, b)
print(GCD)
print(int(a*b/GCD))