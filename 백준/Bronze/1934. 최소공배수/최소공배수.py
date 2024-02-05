import sys
input = sys.stdin.readline

T = int(input())

def gcd(a, b) : # a가 b보다 큰 상태로 입력 들어와야함
    mod_a = a % b
    
    if mod_a == 0 :
        return b
    
    else :
        return gcd(b, mod_a)
    
for _ in range(T) :
    a, b = map(int, input().split())
    
    g = gcd(a, b)
    print(int(a*b/g))