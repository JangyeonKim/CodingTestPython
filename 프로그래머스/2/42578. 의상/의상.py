def solution(clothes):
    answer = 1
    
    c_dict = {}
    for v, k in clothes :
        if k not in c_dict.keys() :
            c_dict[k] = [v]
        else :
            c_dict[k].append(v)

    for v in c_dict.values() :
        answer *= (len(v) + 1) # 카테고리별 옷 수 + 안입는 경우 추가
        
    
    return answer - 1 # 아무것도 입지 않는 경우 제외