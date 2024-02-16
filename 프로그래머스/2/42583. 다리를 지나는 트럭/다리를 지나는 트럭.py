from collections import deque

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    # done = []
    now = deque([])
    now_process = deque([])
    truck_weights = deque(truck_weights)
    
    while now or truck_weights : # 현재 다리를 건너고 있거나, 대기가 있는 동안 반복
        time += 1
        
        if now_process and (now_process[0] == bridge_length) : # 건너고 있는 트력이 있고 첫번째 건너고 있는 트럭이 다 건널 때가 됐으면
            now_process.popleft() # now process에서 제거
            # done.append(now.popleft()) # 건넌 트럭에 추가
            now.popleft()
        
        if len(now) < bridge_length and sum(now) < weight : # 트럭이 더 올라갈 수 있는 상태일 떄
            if truck_weights and (sum(now) + truck_weights[0] <= weight) : # 대기 트럭이 있고 더 올라가도 최대 무게 이하일 때
                now.append(truck_weights.popleft()) # 다리에 트럭 추가
                now_process.append(0)
                
        for i in range(len(now_process)) :
            now_process[i] += 1
        
        # print(f"time : {time}, done : {done}, now : {now}, truck_weights : {truck_weights}")
    
    return time