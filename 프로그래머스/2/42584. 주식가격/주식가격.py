from collections import deque

def solution(prices):
    answer = []
    
    d_prices = deque(prices) 
    
    while len(d_prices) > 1 :
        target_price = d_prices.popleft()
        
        ans = 0
        for dp in d_prices :
            if dp >= target_price :
                ans += 1
            else :
                ans += 1
                break
        answer.append(ans)
        
    return answer + [0]