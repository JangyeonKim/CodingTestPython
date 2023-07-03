# sys.stdin.readline() : 사용자로부터 입력을 최대한 빠르게 받아야하는 경우 사용
# '\n'가 입력되므로 rstrip() 메서드를 함께 이용

from sys import stdin

data = stdin.readline().rstrip()
print(data)