from heapq import heapify, heappush, heappop

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    
    while scoville :
        first = heappop(scoville)
        if first >= K :
            return answer
        else :
            if not scoville :
                return -1
            second = heappop(scoville)
            mix = first + (second * 2)
            heappush(scoville, mix)
            answer += 1
