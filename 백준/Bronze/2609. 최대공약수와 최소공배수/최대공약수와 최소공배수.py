import sys

input = sys.stdin.readline

a, b = map(int, input().split())

a, b = max(a, b), min(a,b)

def gcd(a, b) :
    mod_a = a % b
    
    if mod_a == 0 :
        return b
    else :
        return gcd(b, mod_a)
        
g = gcd(a, b)
print(g)
print(int(a*b/g))