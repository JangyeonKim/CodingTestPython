from collections import deque

def solution(n, words):
    answer = []
    
    queue = deque(words)
    spoken = []
    
    cnt_people, cnt_round = 0, 1
    
    while queue :
        q = queue.popleft()
        cnt_people +=1
        if cnt_people > n :
            cnt_people = 1
            cnt_round += 1
        
        if (spoken and not spoken[-1].endswith(q[0])) or (q in spoken) :
            return [cnt_people, cnt_round]
        
        spoken.append(q)
    

    return [0, 0]