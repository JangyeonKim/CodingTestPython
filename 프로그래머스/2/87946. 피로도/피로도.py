from itertools import permutations

def solution(k, dungeons):

    ans_list = []
    dd = list(permutations(dungeons))
    
    for d in dd :
        ans = 0
        power = k
        
        for need, consume in d :
            if need > power :
                break
            else :
                power -= consume
                ans += 1
        
        ans_list.append(ans)
        
    
    return max(ans_list)