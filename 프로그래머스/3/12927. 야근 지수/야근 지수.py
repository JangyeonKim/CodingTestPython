from heapq import heapify, heappush, heappop

def solution(n, works):
    answer = 0
    heap = []
    
    for w in works :
        heappush(heap, [-w, w])
    
    for _ in range(n) :
        h = heappop(heap)
        
        if h[1] == 0 :
            return 0
        else :
            val = h[1]-1
            heappush(heap, [-val, val])
    
    for _ in range(len(heap)) :
        answer += heappop(heap)[1] ** 2
    
    return answer