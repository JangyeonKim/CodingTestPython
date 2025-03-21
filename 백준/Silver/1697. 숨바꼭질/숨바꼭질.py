N, K = map(int, input().split())
from collections import deque

visit = [False] * (100001)
visit[N] = True

if N >= K :
    print(N-K)
else :
    queue = deque([(N, 0)])
    
    while True :
        q, c = queue.popleft()
        if q == K : 
            print(c)
            break
        else :
            if q-1 <= 100000 and q-1 >= 0 :
                if not visit[q-1]  :
                    visit[q-1] = True
                    queue.append((q-1, c+1))
            if q+1 <= 100000 :
                if not visit[q+1] :
                    visit[q+1] = True
                    queue.append((q+1, c+1))
            if q*2 <= 100000 :
                if not visit[q*2] :
                    visit[q*2] = True
                    queue.append((q*2, c+1))