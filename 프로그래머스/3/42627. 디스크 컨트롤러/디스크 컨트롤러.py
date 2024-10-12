from heapq import heapify, heappop, heappush

def solution(jobs):
    answer = 0
    length = len(jobs)
    heap = []
    heapify(jobs)
    time = 0
    
    while jobs :
        while jobs :
            offer, consume = heappop(jobs)
            
            if offer > time :
                heappush(jobs, [offer, consume])
                break
            else :
                heappush(heap, [consume, offer])
        
        if len(heap) == 0 :
            time += 1
        else :
            consume, offer = heappop(heap)
            answer += consume+time-offer
            time += consume
        
    while heap : 
        consume, offer = heappop(heap)
        answer += consume+time-offer
        time += consume
    
    return answer // length