from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    for k, v in counter.items() :
        if v >= 2 :
            answer += v*(v-1)//2 # 몸무개가 같은 v명중에 2명 짝꿍 경우의수. cC2
    
    
    weights = set(weights) # 이제 몸무게가 다른 사람들끼리 경우 생각
    
    for w in weights : # 짝꿍 경우의 수 : 2/3, 2/4, 3/4
        if w*2/3 in weights :
            answer += counter[w] * counter[w*2/3]
        if w*2/4 in weights :
            answer += counter[w] * counter[w*2/4]
        if w*3/4 in weights :
            answer += counter[w] * counter[w*3/4]
    
    return answer