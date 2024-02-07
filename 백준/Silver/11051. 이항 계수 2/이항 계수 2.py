import sys
from math import factorial
input = sys.stdin.readline

n, k = map(int, input().split())

print(factorial(n)//(factorial(k) * factorial(n-k)) % 10007)