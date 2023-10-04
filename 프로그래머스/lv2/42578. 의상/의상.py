def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1 # type에 해당하는 value가 있으면 가져오고 없으면 0 가져옴
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:   
        answer *= (hash_map[type] + 1) # 각 옷을 입지 않는 경우를 고려하기 위해 +1 씩하여 계산
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1