import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    
    while len(scoville) > 1 :
        min_val = heapq.heappop(scoville)
        
        if min_val >= K :
            return cnt
        else :
            min_val2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_val + (min_val2 * 2))
            cnt += 1
            
    if scoville[0] >= K :
        return cnt
    else :
        return -1