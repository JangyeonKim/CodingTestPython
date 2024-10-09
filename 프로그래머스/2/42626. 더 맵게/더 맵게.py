from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while len(scoville) > 1 :
        first = heappop(scoville)
        if first >= K :
            return answer
        
        second = heappop(scoville)
        
        heappush(scoville, first + (second * 2))
        answer += 1
        
    if scoville[0] >= K :
        return answer
    else :
        return -1