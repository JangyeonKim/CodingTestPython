from collections import deque

# [사람 번호, 몇 번째 차례]
def solution(n, words):
    stack = []
    cnt = 0
    
    queue = deque(words)
    
    while queue :
        q = queue.popleft()
        cnt += 1
        if stack and (q in stack or stack[-1][-1] != q[0]) :
            if cnt % n == 0 :
                return [n, cnt//n]
            else :
                return [cnt%n, cnt//n+1]
        
        stack.append(q)
        print(stack, cnt)
    
    return [0, 0]