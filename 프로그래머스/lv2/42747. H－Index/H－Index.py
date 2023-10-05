def solution(citations):
#     max_value = max(citations)
#     min_value = min(citations)

#     for h in range(max_value, min_value-1, -1) :
        
#         cite = [x >= h for x in citations].count(True)
#         rest = [x <= h for x in citations].count(True) - 1 # "나머지" 논문이 h번 이하 인용 : -1해줌
        
#         if (cite >= h) and (cite + rest == len(citations)) :
#             return h

    citations.sort(reverse = True)
    
    for idx, cite in enumerate(citations) :
        if idx >= cite :
            return idx
    return len(citations)
