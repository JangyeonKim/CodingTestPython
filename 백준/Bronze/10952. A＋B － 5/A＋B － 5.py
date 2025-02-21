import sys

while True :
    input = sys.stdin.readline().rstrip()
    a, b = map(int, input.split())
    if a == 0 and b == 0 :
        break
    print(a+b)