from collections import deque 

def solution(prices):
    answer = []
    
    queue = deque(prices)
    while queue :
        q = queue.popleft()
        ans = 0
        for qq in queue :
            if qq < q :
                ans += 1
                break
            ans += 1
        answer.append(ans)
    
    return answer 