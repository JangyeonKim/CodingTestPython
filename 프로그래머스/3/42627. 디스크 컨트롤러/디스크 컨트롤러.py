import heapq
def solution(jobs):
    answer = 0
    length = len(jobs)
    heapq.heapify(jobs)
    time = 0
    heap = []
    while(jobs):           
        while(jobs):      #그때그때 시간에 따라 가능한 목록을 힙에 넣고
            x,y= heapq.heappop(jobs)
            if x>time:
                heapq.heappush(jobs,[x,y])
                break
            else:
                heapq.heappush(heap,[y,x])

        if len(heap)==0:      #힙에 아무것도 없으면 time 증가, 있다면 pop한다
            time += 1
        else:
            a,b = heapq.heappop(heap)
            answer += (a+time-b)
            time += a
    while heap:              # 남아 있는 힙 순서대로 pop
        a,b = heapq.heappop(heap)
        answer += a+time-b
        time += a
        print(time)

    return answer//length