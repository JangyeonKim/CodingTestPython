from collections import deque

T = int(input())

for _ in range(T) :
    N, M = map(int, input().split())
    I = list(map(int, input().split()))
    
    I = [(x, idx) for idx, x in enumerate(I)]
    queue = deque(I)
    cnt = 0
    
    while queue :
        now_x, now_i = queue.popleft()
        prev_len = len(queue)
        
        for i in range(len(queue)) :
            if queue[i][0] > now_x :
                queue.append((now_x, now_i))
                break
        
        if len(queue) == prev_len :
            cnt += 1
            
            if now_i == M :
                print(cnt)
                break