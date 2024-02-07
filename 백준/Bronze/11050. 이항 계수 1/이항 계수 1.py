import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# n! / k!(n-k)!

def factorial(num) :
    mul = 1
    
    for i in range(1, num+1) :
        mul *= i
    
    return mul

print(int(factorial(n)/(factorial(k)*factorial(n-k))))