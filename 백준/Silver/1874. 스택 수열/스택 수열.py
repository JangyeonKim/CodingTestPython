import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = deque(int(input()) for _ in range(n)) 

stack = []
start = 1  
answer = []

while arr:
    target = arr.popleft() 

    if stack and stack[-1] == target:  # 스택의 최상단이 target이면 pop
        stack.pop()
        answer.append("-")

    elif start <= target:  # target보다 작은 수일때 push
        while start <= target:
            stack.append(start)
            answer.append("+")
            start += 1
        stack.pop()
        answer.append("-")

    else: 
        print("NO")
        exit()

# 결과 출력
print("\n".join(answer))
