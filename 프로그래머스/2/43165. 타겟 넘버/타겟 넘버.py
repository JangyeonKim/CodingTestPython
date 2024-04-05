# 번호 하나 당 2개(+,-)로 2^len(numbers) 경우의 수 존재
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque([numbers[0], -numbers[0]])

    for i in range(1, len(numbers)) :
        middle = []
        while queue :
            middle.append(queue.popleft())
        
        for m in middle :
            plus = m + numbers[i]
            minus = m - numbers[i]
        
            queue.append(plus)
            queue.append(minus)
    
    for q in queue :
        if q == target :
            answer += 1
    # print(queue)
    return answer