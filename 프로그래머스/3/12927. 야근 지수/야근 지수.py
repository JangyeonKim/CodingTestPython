import heapq

def solution(n, works):
    answer = 0
    
    max_heap = []
    for w in works :
        heapq.heappush(max_heap, (-w, w))
        
    for _ in range(n) :
        val = heapq.heappop(max_heap)[1]
        if val == 0 :
            return 0
        else :
            val -= 1
            heapq.heappush(max_heap, (-val, val))
    
    # print(max_heap)
    
    while max_heap :
        ans = heapq.heappop(max_heap)[1]
        answer += ans ** 2
    
    return answer