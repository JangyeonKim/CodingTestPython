from itertools import permutations

def Explore(k, arr) :
    answer = 0
    for require, cost in arr :
        if k < require :
            return answer
        k -= cost
        answer += 1
    return answer

def solution(k, dungeons):
    permu = list(permutations(dungeons))
    # print(permu)
    
    ans_list = []
    for arr in permu :
        answer = Explore(k, arr)
        ans_list.append(answer)
    
    return max(ans_list)