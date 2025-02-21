import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n) :
    summ = 1
    answer = 0
    
    ox = sys.stdin.readline().strip()
    
    for a in ox :
        if a == "O" :
            answer += summ
            summ += 1
        else :
            summ = 1
        
    print(answer)