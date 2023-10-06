from itertools import permutations
    
def solution(k, dungeons):
    
    per_list = list(permutations(dungeons))
    # print(len(per_list))
    
    ans = []
    
    for per in per_list :
        cnt = 0
        tire = k
        for require, cost in per :
            if tire < require :
                break
            else :
                tire -= cost
                cnt += 1
        ans.append(cnt)
        # print(f"per : {per} --> ans : {ans[-1]}")
    # print(f"total_ans : {ans}")
    
    return max(ans)