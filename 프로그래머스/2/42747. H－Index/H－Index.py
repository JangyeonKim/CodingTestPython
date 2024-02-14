def solution(citations):
    if len(citations) == 1:
        return citations[0]
    if max(citations) == 0 :
        return 0
    
    citations.sort()
    
    h = len(citations)
    
    while True :
        idx = 0
        for i in range(len(citations)) :
            if citations[i] >= h : # h번 이상 인용
                idx = i
                break
        
        if len(citations[idx:]) >= h : # h개 이상
            return h
        else :
            h -= 1

