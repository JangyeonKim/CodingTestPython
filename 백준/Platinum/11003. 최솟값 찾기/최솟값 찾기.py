import sys

n, l = map(int,sys.stdin.readline().strip().split())
in_list = list(map(int,sys.stdin.readline().strip().split()))

# 덱 사용
## 1. 최솟값 후보 아닌 데이터 삭제
## 2. 윈도우 범위 벗어나는 데이터 삭제

from collections import deque 

queue = deque()

for i in range(n) :
    while queue and queue[-1][0] > in_list[i] : # 덱의 마지막 위치에서부터 현재 값보다 큰 값들을 제거
        queue.pop()
    
    queue.append((in_list[i], i))
    
    if queue[0][1] <= i-l : # 덱의 처음에서 윈도우 범위를 벗어난 값 제거
        queue.popleft()
    
    print(queue[0][0], end = " ")
    