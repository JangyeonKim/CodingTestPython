import sys

case = int(sys.stdin.readline().rstrip())

for _ in range(case) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)